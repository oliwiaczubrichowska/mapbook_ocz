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

