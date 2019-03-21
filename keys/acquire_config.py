import configparser


config = configparser.ConfigParser()
config.read(r"E:\bookshelf\ali\ali_par.ini",encoding="utf-8")
SECRET_KEY = config.get("DEFAULT","scrset_key")
def get_all_message_parameter():
    message_parameter = {}
    message_parameter["SECRET_KEY"] = SECRET_KEY
    message_parameter["Action"] = config.get("alimessage","Action")
    message_parameter["AccessKeySecret"] = config.get("alimessage","AccessKeySecret")
    message_parameter["AccessKeyId"] = config.get("alimessage","AccessKeyId")
    message_parameter["TemplateCode"] = config.get("alimessage","TemplateCode")
    message_parameter["SignName"] = config.get("alimessage","SignName")

    return message_parameter

def ali_pay_parameter():
    ali_pay_parameter = {}
    ali_pay_parameter["SECRET_KEY"] = SECRET_KEY
    ali_pay_parameter["ali_private_key"] =  config.get("alipay","ali_private_key")
    ali_pay_parameter["ali_public_key"] =  config.get("alipay","ali_public_key")
    ali_pay_parameter["ali_app_id"] =  config.get("alipay","ali_app_id")
    
    return ali_pay_parameter


