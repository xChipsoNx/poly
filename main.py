import datetime

from phone import db, check_phone
from user import User, Drug

now = datetime.datetime.now()


def reg():
    phone = input("Введите номер телефона.")
    check_phone(phone)
    phones = db.get_all_phones()
    for x in phones:
        if phone == x:
            print("Номер существует, продолжить покупку.")
            return shop(phone)
    u = User
    u.phone = phone
    u.name = input("Введите имя.")
    u.age = input("Введите возраст")
    db.new_user(u.phone, u.name, u.age)
    return shop(phone)




def shop(phone):

    box = []
    drug = Drug
    box.append(drug)



def main():

    end = False

    while end == False:

        answer = input("Введите 1 - Покупка.\nВведите 2 - Регистрация.")
        if answer == 1:
            phone = input("Введите номер телефона.")
            check_phone(phone)
            phones = db.get_all_phones()
            for x in phones:
                if phone == x:
                    print("Номер существует, продолжить покупку.")
                   return shop(phone)


        elif answer == 2:
            reg()

        else:
            print("Введено недопустимое значение. Повторите ввод.")
            continue


if __name__ == '__main__':
    main()
