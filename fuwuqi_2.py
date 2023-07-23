acm_ip=["192.168.1.1","192.168.2.1"]
acm_msg=[[],[]]
header = [1,1,1]
fwq_ip = "192.168.0.0"

class poster:
    def __init__(self,ip_a,msg_a):
        self.ip_a=ip_a
        self.msg_a=msg_a
class geter:
    def __init__(self,ip_b,msg_b):
        self.ip_b=ip_b
        self.msg_b=msg_b

def header_judge():
    if header[0] == poster1.ip_a:
        pass
    elif header[0] == fwq_ip:
        acm_msg[1].append(poster1.msg_a)
    elif header[0] == geter1.ip_b:
        print("---------------------------------------------------")
        for i in header[2]:
            print(i)
        print("---------------------------------------------------")
    else:
        print("error")

while True:
    cmd = input("->")
    if cmd == "poster1":
        p_msg = input(":")
        poster1=poster("192.168.1.1",p_msg)
        header[0]="192.168.0.0"
        header[1]=poster1.ip_a
        header[2]=poster1.msg_a
        header_judge()
    elif cmd == "geter1":
        geter1 = geter("192.168.2.1","none")
        header[0]="192.168.2.1"
        header[1]="192.168.0.0"
        header[2]=acm_msg[1]
        header_judge()
    elif cmd =="exit":
        break
    else:
        print("error")

        