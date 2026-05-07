from mapbook_ocz.model import users
from mapbook_ocz.controler import read_users,update_user, remove_user, adder_user, update_user_post

def main():
    while True:
            print("==========MENU==========")
            print("0- zakończ program")
            print("1- wyświetl znajomych")
            print("2- dodawanie znajomych")
            print("3- usuwanie znajomego")
            print("4- edytowanie znajomego")
            print("5- update posta")
            choice=input("Wybierz opcje menu: ")
            print(f"Wybrano opcję {choice}")
            if choice=="0":
                break
            if choice=="1":
                read_users(users)
            if choice=="2":
                adder_user(users)
            if choice=="3":
                remove_user(users)
            if choice== "4":
                update_user(users)
            if choice== "5":
                update_user_post(users)
if __name__=="__main__":
    main()

