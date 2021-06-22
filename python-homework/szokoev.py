def leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False


ask_year = input("Kérem, adjon meg egy évszámot: ")
if leap_year(int(ask_year)) == True:
    print("A megadott évszám szökőév.")
else:
    print("A megadott évszám nem szökőév.")
