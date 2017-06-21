#!/usr/bin/env python

import subprocess
import os
import time

temps = []
fans = []
init = False

def read_temps():
	global temps
	global init
	temps = []
	output = subprocess.check_output("nvidia-smi -q -d temperature | grep GPU", shell=True)

	for row in output.split('\n'):
		if 'GPU Current Temp' in row:
			key, value = row.split(': ')
			temps.append(int(value.strip(' C')))
			if init == False:
				fans.append(60)

	init = True

def fan_control():
	global temps
	global fans

	id = 0
	for temp in temps:
		if fans[id] == 60:
			if temp > 65:
				fans[id] = 70
				print str(id) + ": Fan set to %70"
				set_fan(id, 70)
		elif fans[id] == 70:
			if temp > 70:
                        	fans[id] = 80
                        	print str(id) + ": Fan set to %80"
				set_fan(id, 80)
			elif temp <= 60:
				fans[id] = 60
                                print str(id) + ": Fan set to %60"
				set_fan(id, 60)
		elif fans[id] == 80:
			if temp > 75:
                                fans[id] = 90
                                print str(id) + ": Fan set to %90"
				set_fan(id, 90)
                        elif temp <= 65:
                                fans[id] = 70
                                print str(id) + ": Fan set to %70"
				set_fan(id, 70)

		elif fans[id] == 90:
			if temp > 80:
                                fans[id] = 100
                                print str(id) + ": Fan set to %100"
				set_fan(id, 100)
                        elif temp <= 70:
                                fans[id] = 80
                                print str(id) + ": Fan set to %80"
				set_fan(id, 80)

		elif fans[id] == 100:
			if temp <= 75:
                                fans[id] = 90
                                print str(id) + ": Fan set to %90"
				set_fan(id, 90)
		id = id + 1

def set_fan(id, fan):
	new_env = dict(os.environ)
        new_env['Display'] = '0'

	cmd = 'nvidia-settings -a \'[fan:' + str(id) + ']/GPUTargetFanSpeed=' + str(fan) + '\''

	subprocess.Popen(cmd, env=new_env, shell=True)

def main():
	global temps
	global fans
	while True:
		read_temps()
		fan_control()
		print "Temps:" + str(temps)
		print "Fans:" + str(fans)
		print "------------------------------------"
		time.sleep(1)

if __name__ == "__main__":
    	main()
