import string
lcl_list = string.ascii_lowercase


for i in lcl_list:
    list = ord(i)
    list2 = list + 1
    list3 = list2 + 1
    print(chr(list), int(list), "\t", chr(list2), int(list2), "\t", chr(list3), int(list3), end="\n")
    if ord(i) + 2 == 122:
        break
