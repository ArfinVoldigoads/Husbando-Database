class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6995317382"
    sudo_users = "6995317382", "5820365080", "5489586647", "6205444949", "5147271956", "158468045", "6686326398", "5147271956", "7177727796", "5008662958", "7127913934", "5843270062", "1495261563", "6708573850", "6489025882", "6752263178", "5157661772", "6353916710" 
    GROUP_ID = -1002046761940
    TOKEN = "6829947391:AAHqz3aEnQw8TMJ931Qq-4BlLwBLZrH917c"
    mongo_url = "mongodb+srv://Husbando:Husbando@cluster0.lai7z.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    PHOTO_URL = ["https://telegra.ph/file/8279229551c22fe1c17de.jpg", "https://telegra.ph/file/ddb237bcd33fc09941312.jpg"]
    SUPPORT_CHAT = "gc_animecommunity"
    UPDATE_CHAT = "Take_update"
    BOT_USERNAME = "take_Husband_bot"
    CHARA_CHANNEL_ID = "-1002126509901"
    api_id = 21436816
    api_hash = "c269918dddddbc041d536207cab72155"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
