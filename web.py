import webbrowser as web 
import time
import os
import random
count = random.randint(2,4)
j=0
while j<count:
	i = 0
	while True:
		while i <= 4:	
			web.open_new_tab('google.bg')
			i = i + 1
			time.sleep(0.6)
		else:
			os.system('killall')
