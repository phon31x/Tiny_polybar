# Based on idea https://github.com/phon31x/Tiny_polybar from @phon31x @pietryszak (Github)
# Python version https://github.com/AmmarHaddadi/betterTray from @AmmarHaddadi (Github)

import subprocess
#replace tray with ur tray bar name ([bar/'name'])or keep it tray   
name = "tray"

tray_PID = subprocess.run(
	"xprop -name 'Polybar tray window' _NET_WM_PID | grep -o \'[[:digit:]]*'", 
	shell=True,
	capture_output=True)

if tray_PID.returncode == 0:
	subprocess.run(f'kill {tray_PID.stdout.decode()}',shell=True)
else:
	subprocess.run(f'polybar {name}', shell=True)

#ubuntu ships with python , arch too , almost every distro out there
