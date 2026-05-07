# definicja prostej struktury danych obejmujacej przykladowego ujzytkownika
from os import remove
from random import choice

users=[
    {"name":"oliwia","location":"skierniewice",
     "posts":["sprzedma mercedasa", "kupie skrzynie biegow", "ratunku co robic po wypadku"]},
    {"name":"daniel","location":"legionowo",
     "posts":["moj kod nie dziala pomocya"]},
    {"name":"kamil","location":"debica",
     "posts":["czy ktos zrobil sprawozdanie"]},

]
def read_users(users_data:list)->None:
    for user in users_data:
        print(f'twoj znajomy {user["name"]} z miejscowosci {user["location"]} opublikowal post {user["posts"][-1]}')

read_users(users)

def adder_user(users_data:list)->None:
    users_data.append({"name":input("podaj imię użytkowanika:"),"location": input("Podaj swoją lokalizację:"),
     "posts":["Dołączyłem do znajomych"]})



def remove_user(users_data:list)->None:
    user_to_remove=input("Podaj imię znajomego do usunięcia: ")
    for users in users_data:
        if users["name"]==user_to_remove:
            users.remove(user)



def update_user(users_data:list)->None:
    user_to_update=input("Podaj imię znajomego do update: ")
    for users in users_data:
        if users["name"]==user_to_update:
            user["name"]=input("Podaj imię użytkownika: ")
            user["location"]= input("Podaj nową lokaliację")

def update_user_post(users_data:list)->None:
    user_to_update=input("Podaj imię znajomego do update: ")
    for users in users_data:
        if users["name"]==user_to_update:
            user["posts"].append(input("Co słychać? "))



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
        update_user_post(1users)

