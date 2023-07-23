get_ip=input("fuwuqi's ip:")
post_ip="192.168.1.1"
message="wzx is a boy"
header = [get_ip,post_ip,message]
class fwq:
    def __init__(self,ip,msg):
        self.ip=ip
        self.msg=msg
fwq1=fwq("192.168.0.1","first")
fwq2=fwq("192.168.0.2","second")
while True:
    if header[0] == fwq1.ip:
        print(fwq1.msg)
        break
    elif header[0] == fwq2.ip:
        print(fwq2.msg)
        break