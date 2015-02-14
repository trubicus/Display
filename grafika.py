import os, time
__author__ = 'truba'


class Display(object):
    def __init__(self, width, height):
        self.display = [["O" for i in range(width)] for j in range(height)]

    def set_display(self, x, y):
        self.display[x][y] = "X"

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


        


def main():
	#DISPLAY SETTINGS
	display_width = 30
	display_height = 1
	display = Display(display_width, display_height)
	display_string = "opasni_displej" #kaj ce ispisati
	x = display_width-1
	y = display_height-1
	c = 0
	#-----------------------------------------------------

	#THE MAGIC
	display.print_display()
   	for strings in range(display_width + len(display_string)):
   		display.set_char(x, y, display_string, c)
   		c += 1
   		os.system("clear")
   		display.print_display()
   		time.sleep(0.07) #Kolko brzo mjenja "slike"
   	#----------------------------------------------------
    

if __name__ == "__main__":
    main()
