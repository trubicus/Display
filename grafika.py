import os, time
__author__ = 'truba'


class Display(object):
    def __init__(self, width, height):
        self.display = [[" " for i in range(width)] for j in range(height)]

    def print_display(self):
        for each in self.display:
            print " ".join(each)

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
   display_width = 60
   display_height = 7
   display = Display(display_width, display_height)
   display_string = "" #kaj ce ispisati
   if display_string == "":
      display_string = raw_input("Your Message: ")
   display_string = display_string.upper()
   x = display_width-1
   y = display_height-1
   c = 0
   #-----------------------------------------------------

   display.print_display()

   #THE MAGIC PRAVI
   while 1:
      for c in display_string:
         if c != " ":
            character = open("font/matrix/"+c+".txt", "r") #otvara file za pojedino slovo
         else:
            character = open("font/matrix/\ .txt", "r") #poseban slucaj za space
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

      #PRINTANJE PRAZNINE DA TEKST PROSKROLA DO KRAJA EKRANA
      for i in range(display_width):
            display.next(display_width, display_height)
            display.new_col(ln, x, y)
            os.system("clear")
            display.print_display()
            time.sleep(0.04) #Kolko brzo mjenja
      #------------------------------------------------------
   #---------------------------------------------------------

if __name__ == "__main__":
    main()
