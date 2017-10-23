# simple count-to-zero timer set by user input
import tkinter
import time
# import sys
import os


# calls the tic function and update the time GUI
def tic_clock(mins, sec):
	try:
		mins, sec = tic(mins, sec)
		str_mins = str(mins)
		str_sec = str(sec)
		if mins < 10:
			str_mins = '0' + str_mins
		if sec < 10:
			str_sec = '0' + str_sec
		str_time =  str_mins + ':' + str_sec
		t = time.strptime(str_time, "%M:%S")
		rel['text'] = time.strftime('%M:%S', t) # update timer count
# this method continuously call the same function after a period of time
		rel.after(990, tic_clock, mins, sec) 
	except: # once the minutes becomes negative play a 'beep' sound
		print("Time's up!!")
		rel['text'] = "TIME'S UP!!"
		rel['font'] = 'Helvetica 120 bold'
		for i in range(10):  # repeats a beep sound 10 times
			os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (0.2, 400))
			time.sleep(0.5) # stand by of 0.5 secs
		return
		# sys.exit(1)

	

# decrease by a second and verify all digits
def tic(mins, sec):
	sec -= 1
	if sec == -1:
		sec = 59
		mins -= 1
	return mins, sec




# Timer setting by the user (minutes)
mins = int(input("Input the number of minutes: "))
sec = 0


max_unity = 'minute' 
if mins > 1:
	max_unity = max_unity + 's'
# prompt message with the timer minutes setting 
print(('Your timer is set to {} ' + max_unity).format(mins))



rel = tkinter.Label() # generates a GUI window
str_time = str(mins) + ':00'
t = time.strptime(str_time, "%M:%S") 
rel['text'] = time.strftime('%M:%S', t) # intial timer set 
rel['font'] = 'Helvetica 120 bold'
rel.pack()



tic_clock(mins, sec)
rel.mainloop() # this assures the GUI will run forever


print('The timer has finished.')