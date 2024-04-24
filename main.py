# -----------
# Main space
# -----------
#import defen #(Just wants to import the things from defen,"defen.(Specific command #1)"
#from defen import nameit #(inserting something spcefic so you dont need "defen.")
#defen.nameit("Joe") #1
#nameit("Joe")
# -----------

# weather
import defen

a = input("Name of the city")
b = input("Date, Month/Day/Year")
c = input("Highest temp")
d = input("Lowest temp")

cprime = float(c)

defen.info(a,b,c,d)

if cprime >= 10:
    defen.niceday()
else:
    defen.notnice()
    
