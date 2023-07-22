acm = ["None"]
i=1
while True:
    cmd = input("->")
    if cmd=="SEND":
        send_massage = input(":")
        acm.append(send_massage)
    elif cmd=="GET":
        if i>len(acm)-1:
            print("Empety.")
        else:
            print(acm[i])
            i=i+1
    elif cmd=="EXIT":
        print("See You!")
        break
    else:
        print("ERROR!")
print(acm)