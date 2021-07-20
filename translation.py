from pyrogram.types import InlineKeyboardButton


class Translation(object):
    START_TEXT = "Hi {},\nI'm MangaLoader!\nYou can upload any manga to Telegram as a Zipfile!\n\n/help for more details!"
    HELP_TEXT = "How to use MangaLoader?!\n\n1. Sent Manga URL.\n2. Choose subdir option.\n3. Wait a few seconds and i will send your archived document\n\nIf bot didn't respond, contact @xgorn"
    UPLOAD = "Choose subdirs option (will uploaded as a Zipfile."
    CLEANDIR_SUCCESS = 'Successfully cleaned your download dir, now you can sent another link'
    CLEANDIR_UNSUCCESS = 'Your download dir are empty, use this command only if your bot are stuck'
    
    upload_buttons=[
        [
            InlineKeyboardButton("as PDF", callback_data="pdf"),
            InlineKeyboardButton("as ZIP", callback_data="zip"),
        ],
        [InlineKeyboardButton("as Folder", callback_data="folder")],
    ]
