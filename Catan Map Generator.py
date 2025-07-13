import tkinter as tk
import random as rnd
#-----------VARIABLES-------------
squareSize = 100
offset = 50
windowHeight = 500
windowWidth = 500
fontSize = 17
fontStyle = "Arial"
#-----------WINDOW---------------
window = tk.Tk()
window.title("Catan Map")
window.geometry(f"{windowWidth}x{windowHeight}")

canvas = tk.Canvas(master=window, width=windowWidth, height=windowHeight, background="lightblue")
canvas.pack()
#--------------CLASS--------------
class Hex:
	def __init__(self, type, value):
		self.type = type
		self.value = value
	def display(self):
		print(f"Type: {self.type}, Value: {self.value}")
#----------------------------------
terrains = ["grain","grain","grain","grain",
			"forest","forest","forest","forest",
			"pasture","pasture","pasture","pasture",
			"mountain","mountain","mountain",
			"hill","hill","hill","desert"]
colorMap = {"grain":"#EDD836",
			"forest":"#13470B",
			"pasture":"#6BF15C",
			"mountain":"#929292",
			"hill":"#BC4A3C",
			"desert":"#CCAD60"}
nums = [2,3,3,4,4,5,5,6,6,8,8,9,9,10,10,11,11,12] # token values
#----------ADJACENCY LIST-----------
adjacency_list = {
    0:  [1, 3, 4],
    1:  [0, 2, 4, 5],
    2:  [1, 5, 6],
    3:  [0, 4, 7, 8],
    4:  [0, 1, 3, 5, 8, 9],
    5:  [1, 2, 4, 6, 9, 10],
    6:  [2, 5, 10, 11],
    7:  [3, 8, 12],
    8:  [3, 4, 7, 9, 12, 13],
    9:  [4, 5, 8, 10, 13, 14],
    10: [5, 6, 9, 11, 14, 15],
    11: [6, 10, 15],
    12: [7, 8, 13, 16],
    13: [8, 9, 12, 14, 16, 17],
    14: [9, 10, 13, 15, 17, 18],
    15: [10, 11, 14, 18],
    16: [12, 13, 17],
    17: [13, 14, 16, 18],
    18: [14, 15, 17],
}
#-----------GENERATE HEXES------------ 
rnd.shuffle(terrains)
desertIndex = terrains.index("desert")
goodShuffle = False
while not goodShuffle:
    goodShuffle = True
    rnd.shuffle(nums)
    numsForMap = nums.copy()
    numsForMap.insert(desertIndex, 0) # insert token with value zero for desert
    for i in adjacency_list:
        for j in adjacency_list[i]:
            if j <= i:
                continue
            if (numsForMap[i] in (6, 8)) and (numsForMap[j] in (6, 8)):
                goodShuffle = False
                break
#-------MAKE HEXES-------
hexes = []
for i in range(19):
    hexes.append(Hex(terrains[i], numsForMap[i]))
#----------COLORS---------------
fillColors = []
for i in hexes:
	fillColors.append(colorMap[i.type])
#---------DRAW BOARD---------------
hexesCopy = hexes.copy()
for i in range(0,5):
	if i == 0 or i == 4:
		for j in range(0,3):
			canvas.create_rectangle(2*offset+j*squareSize,i*squareSize, 2*offset+j*squareSize+100, i*squareSize+100,fill=fillColors.pop())
			canvas.create_text(3*offset+j*squareSize, i*squareSize+offset, text=numsForMap.pop(), font=(fontStyle,fontSize), fill="black")
			hexesCopy.pop()
	elif i == 1 or i == 3:
		for j in range(0,4):
			canvas.create_rectangle(offset+j*squareSize,i*squareSize, offset+j*squareSize+100, i*squareSize+100,fill=fillColors.pop())
			canvas.create_text(2*offset+j*squareSize, i*squareSize+offset, text=numsForMap.pop(), font=(fontStyle,fontSize), fill="black")
			hexesCopy.pop()	
	else:
		for j in range(0,5):
			canvas.create_rectangle(j*squareSize,i*squareSize, j*squareSize+100, i*squareSize+100,fill=fillColors.pop())
			canvas.create_text(offset+j*squareSize, i*squareSize+offset, text=numsForMap.pop(), font=(fontStyle,fontSize), fill="black")
			hexesCopy.pop()
#-----------------------------------
for i in hexes:
	i.display()
window.mainloop()
