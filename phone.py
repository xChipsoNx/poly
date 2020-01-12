from dbhelper import DBHelper
db = DBHelper()

def check_phone(text):

    if not text[1:].isdigit():
        print("Номер может состоять из цифр и знака '+'.")
        return False

    if len(text) < 10:
        print("Номер слишком короткий номер.")
        return False
    else:
        phone = phone_refactor(str(text))
        if phone is not False:
            return phone
        else:
            print("Номер должен начинаться с (+79/89/9).")
            return False


def phone_refactor(phone):

    if phone.startswith('+79'):
        return phone
    elif len(phone) == 10 and phone[0] == '9':
        return '+7' + phone
    elif len(phone) == 11 and (phone.startswith('89') or phone.startswith('79')):
        return '+7' + phone[1:]
    else:
        return False


