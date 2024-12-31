import requests
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CommandHandler, CallbackContext
from shivu import application
import os

async def tgm_command(update: Update, context: CallbackContext) -> None:
    # Pastikan perintah ini adalah balasan terhadap foto, video, atau GIF
    if update.message.reply_to_message:
        file = None
        file_path = "/tmp/media"  # Nama file default

        # Cek jika pesan balasan adalah foto
        if update.message.reply_to_message.photo:
            file_id = update.message.reply_to_message.photo[-1].file_id
            file_path += ".jpg"

        # Cek jika pesan balasan adalah video pendek
        elif update.message.reply_to_message.video and update.message.reply_to_message.video.file_size <= 100 * 1024 * 1024:  # Batas 100 MB
            file_id = update.message.reply_to_message.video.file_id
            file_path += ".mp4"

        # Cek jika pesan balasan adalah GIF
        elif update.message.reply_to_message.animation:
            file_id = update.message.reply_to_message.animation.file_id
            file_path += ".gif"

        else:
            await update.message.reply_text("Please reply to a photo, video (under 100 MB), or GIF to get a link.")
            return

        try:
            # Dapatkan file melalui bot
            file = await context.bot.get_file(file_id)
            
            # Unduh file sementara ke sistem
            await file.download_to_drive(file_path)

            # Debug: Informasikan bahwa file berhasil diunduh
            await update.message.reply_text(f"File downloaded to: {file_path}")

            # Unggah ke Uguu.se
            with open(file_path, 'rb') as f:
                response = requests.post(
                    'https://uguu.se/api.php?d=upload-tool',
                    files={'file': f}
                )

            # Debug: Periksa respons
            await update.message.reply_text(f"Response status: {response.status_code}, Response text: {response.text}")

            # Periksa apakah unggahan berhasil
            if response.status_code == 200 and response.text.startswith("https://"):
                uguu_url = response.text.strip()  # Dapatkan URL dari respons
                
                # Kirim pesan dengan tautan media
                await update.message.reply_text(
                    f"Here is the link to the media: {uguu_url}",
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("Open Media", url=uguu_url)]
                    ])
                )
            else:
                # Jika gagal mengunggah
                await update.message.reply_text("Failed to upload the media to Uguu.se. Please try again later.")
        
        except Exception as e:
            # Tangkap kesalahan dan tampilkan
            await update.message.reply_text(f"An error occurred: {str(e)}")
        
        finally:
            # Hapus file sementara setelah selesai
            if os.path.exists(file_path):
                os.remove(file_path)
    else:
        # Jika pesan tidak membalas media
        await update.message.reply_text("Please reply to a photo, video (under 100 MB), or GIF to get a link.")

# Tambahkan handler untuk perintah /tgm
application.add_handler(CommandHandler("tgm", tgm_command))
