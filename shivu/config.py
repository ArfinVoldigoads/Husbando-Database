class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6995317382"
    sudo_users = "6995317382", "5820365080", "5489586647", "6205444949", "5147271956", "158468045", "6686326398", "5147271956", "7177727796", "5008662958", "7127913934", "5843270062", "1495261563", "6708573850", "6489025882", "6752263178", "5157661772", "6353916710" 
    GROUP_ID = -1002046761940
    TOKEN = "8094433736:AAH5C0mmL4a3AD6WVPAvfhe_bf_AXNlCX1g"
    mongo_url = "mongodb+srv://Arfin1:Arfin1@cluster0.5axv7.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/8279229551c22fe1c17de.jpg", "https://telegra.ph/file/ddb237bcd33fc09941312.jpg"]
    SUPPORT_CHAT = "gc_animecommunity"
    UPDATE_CHAT = "Take_update"
    BOT_USERNAME = "Husbando_database_bot"
    CHARA_CHANNEL_ID = "-1002126509901"
    api_id = 21436816
    api_hash = "c269918dddddbc041d536207cab72155"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
