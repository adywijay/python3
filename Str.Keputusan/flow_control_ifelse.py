versi = 2
strig = "pemrograman ulo"

if versi == 2:
    print(strig, str(versi))
else:
    print(strig)
    # print(strig)

# statis

ipk = eval(input("Input IPK : "))
lama_std = input("Lama Masa Studi : ")

at1 = ipk >= 3.51 and ipk <= 4.00
# at2 = at1 and lama_std <= 4.0

# print(at2)
if str(lama_std) == '':

    if ((ipk >= 2.80) and (ipk <= 3.00)):
        print("Grade Anda C")

    elif ((ipk >= 3.00) and (ipk < 3.51)):
        print("Grade Anda B")

    elif ((ipk >= 3.00) and (ipk < 3.51)):
        print("Grade Anda A denga predikat KEMELUD")

    # elif (at1 and lama_std <= 4.0):
    #     print("Grade Anda A denga predikat CUMLAUDE")
    else:
        # print("Anda Ghuoblock Sekale !!!!!!")
        pass  # mengabaikan perintah

elif str(lama_std) != '':
    if ((ipk >= 2.80) and (ipk <= 3.00)):
        print("Grade Anda C")

    elif ((ipk >= 3.00) and (ipk < 3.51)):
        print("Grade Anda B")

    elif ((ipk >= 3.51) and (eval(lama_std) > 4.0)):
        print("Grade Anda A denga predikat KEMELUD")

    elif (at1 and eval(lama_std) <= 4.0):
        print("Grade Anda A denga predikat CUMLAUDE")
    else:
        print("Anda Ghuoblock Sekale !!!!!!")
else:
    # print("asaqwwqe")
    pass  # mengabaikan perintah
