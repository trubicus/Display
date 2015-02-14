import os, time
__author__ = 'truba'


class Display(object):
    def __init__(self, width, height):
        self.display = [[" " for i in range(width)] for j in range(height)]

    def set_display(self, x, y):
        self.display[x][y] = '\033[1;31mO\033[1;m'

    def reset_display(self, x, y):
    	self.display[x][y] = "O"

    def print_display(self):
        for each in self.display:
            print " ".join(each)
            
    def set_char(self, x, y, display_string, c):
    	for i in range(x):
    		self.display[y][i] = self.display[y][i+1]
    	
    	if c < len(display_string):
    		self.display[y][x] = '\033[1;31m'+display_string[c]+'\033[1;m'
    	else:
    		self.display[y][x] = "O"

    def new_col(self, col, x, y):
    	for i in range(len(col)-1):
    		if col[i] == "1":
    			self.display[i][x] = "\033[1;31mX\033[1;m"
    		else:
    			self.display[i][x] = " "

    def next(self, display_width, display_height):
    	for i in range(display_height):
    		for j in range(display_width-1):
    			self.display[i][j] = self.display[i][j+1]
        


def main():
	#DISPLAY SETTINGS
	display_width = 40
	display_height = 7
	display = Display(display_width, display_height)
	display_string = "mnogo opasan displej" #kaj ce ispisati
	display_string = display_string.upper()
	x = display_width-1
	y = display_height-1
	c = 0
	#-----------------------------------------------------

	#THE MAGIC
	"""display.print_display()
   	for strings in range(display_width + len(display_string)):
   		display.set_char(x, y, display_string, c)
   		c += 1
   		os.system("clear")
   		display.print_display()
   		time.sleep(0.07) #Kolko brzo mjenja "slike"""
   	#----------------------------------------------------
   	display.print_display()
   	#THE MAGIC PRAVI
   	while 1:
	   	for c in display_string:
	   		if c != " ":
	   			character = open("font/matrix/"+c+".txt", "r")
	   		else:
	   			character = open("font/matrix/\ .txt", "r")
	   		while character:
	   			ln = character.readline()
	   			display.next(display_width, display_height)
	   			display.new_col(ln, x, y)
	   			os.system("clear")
	   			display.print_display()
	   			time.sleep(0.04) #Kolko brzo mjenja
	   			if not ln:
	   				break
	   		character.close()
	   		ln = "0000000"

   		for i in range(display_width):
   			display.next(display_width, display_height)
	   		display.new_col(ln, x, y)
	   		os.system("clear")
	   		display.print_display()
	   		time.sleep(0.04) #Kolko brzo mjenja
    

if __name__ == "__main__":
    main()
