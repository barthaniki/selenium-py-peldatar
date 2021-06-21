drink1 = "sör"
drink2 = "kóla"
ok_drink1 = "Parancsoljon a söre."
ok_drink2 = "Parancsoljon a kólája"
no_drink = "Csak sört és kólát tartunk."
warn_drink1 = "Sört nem adhatok."
warn_drink2 = "A koffein megemelheti a vérnyomását."

user_age = input("Kérem, adja meg az életkorát: ")
print(user_age)
if int(user_age) < 18:
    print("Mit iszik?")
    user_drink = input()
    if user_drink == drink1:
        print(warn_drink1)
    elif user_drink == drink2:
        print(ok_drink2)
    else:
        print(no_drink)
elif int(user_age) >= 18:
    print("Mit iszik?")
    user_drink = input()
    if user_drink == drink1:
        print(ok_drink1)
    elif user_drink == drink2:
        if int(user_age) >= 60:
            print(warn_drink2)
        else:
            print(ok_drink2)
    else:
        print(no_drink)
else:
    print(no_drink)
