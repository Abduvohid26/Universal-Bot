import os.path

from aiogram import types, F
from loader import bot, dp
from states.state import FileCompressState
from aiogram.fsm.context import FSMContext
import pikepdf
import asyncio
# Pdf compression function
async def compress_pdf_file(input_path, output_path):
    try:
        # Faylni ochish
        pdf = pikepdf.open(input_path)

        # Faylni siqish
        pdf.save(output_path, compress_streams=True)
        return output_path
    except Exception as e:
        print(f"❌ Siqishda xatolik yuz berdi: {e}")
        return None


async def clean_up_files(*file_paths):
    """Berilgan fayllarni xavfsiz o'chiradi."""
    for file_path in file_paths:
        if os.path.isfile(file_path):
            try:
                os.remove(file_path)
                print(f"Fayl o‘chirildi: {file_path}")
            except Exception as e:
                print(f"Faylni o‘chirishda xatolik: {file_path}, {e}")


@dp.message(F.text == '🗞 File compress')
async def get_file(message: types.Message, state: FSMContext):
    await message.answer(text="Fileni yuboring")
    await state.set_state(FileCompressState.start)


@dp.message(F.document, FileCompressState.start)
async def check_type(message: types.Message, state: FSMContext):
    file_type = message.document.file_name.split('.')[-1]
    file_id = message.document.file_id
    file_name = message.document.file_name
    file_path = f"downloads/{file_name}"
    if file_type == 'pdf':
        try:
            file = await bot.get_file(file_id=file_id)
            await bot.download_file(file_path=file.file_path, destination=file_path)
            compressed_file_path = f"downloads/compressed_{file_name}"
            await compress_pdf_file(input_path=file_path, output_path=compressed_file_path)
            await message.answer_document(
                document=types.input_file.FSInputFile(compressed_file_path),
                caption="✅ Siqilgan fayl tayyor!"
            )
            await clean_up_files(compressed_file_path, file_path)
            await state.clear()

        except Exception as e:
            await message.answer("❌ Faylni siqishda yoki yuklab olishda xatolik yuz berdi.")
            await state.clear()
            print(e)
        finally:
            await state.clear()
            pass
            # if compressed_file_path:
            #     await clean_up_files(compressed_file_path, file_path)
            # await state.clear()
    else:
        await message.answer("❌ Faqat PDF formatdagi fayllarni siqish mumkin.")
        await state.clear()