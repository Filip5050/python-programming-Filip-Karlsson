import matplotlib.pyplot as plt
import numpy as np


X = []
Y = []

with open(r"C:\Code\python-programming-Filip-Karlsson\Labs\Labb3\Data\unlabelled_data.csv", "r") as f_read:
   lines = f_read.readlines()
   for line in lines:
      split = line.split()
      x, y = map(float,line.split(",")) #sepererar punkterna/kordinaterna så jag kan få in rätt nummer i respektive lista
      X.append(x) #lägger in x kordinaterna in i min X fil
      Y.append(y) #lägger in y kordinaterna in i min y fil

#Förbereder jag min linje till grafen, där jag har valt en x och y linje som sepererar grafen ungefär i mitten
x_line = [-5.53, 4.74]
y_line = [-4.19,3.40]

#här beräknar koden lutningen = K på grafen och interceptorn
slope = (y_line[1] - y_line[0]) / (x_line[1] - x_line[0])
intercept = y_line[0] - slope * x_line[0]

#Funktionen tar listan med x och y kordinater och linje parametern 
def classify_points(X, Y, slope, intercept):
    above_line = []
    below_line = []
    #for loopen går igenom alla punkter och ränkar ut y-värdet för linjen vid den x-koordinaten.
    #Beroende på y värdet är över eller under den uträknade y värdet så läggs värdena in i above_line listan eller below_line listan
    for x, y in zip(X, Y):
        y_on_line = slope * x + intercept
        if y > y_on_line:
            above_line.append((x, y))
        else:
            below_line.append((x, y))
    
    return above_line, below_line

#kallar på funktionen
above_line, below_line = classify_points(X, Y, slope, intercept)



plt.figure(figsize=(10, 6))
plt.plot(x_line, y_line, color='red', label='Line')
if above_line:
    plt.scatter(*zip(*above_line), color='black', label='Above Line', marker='o')
if below_line:
    plt.scatter(*zip(*below_line), color='yellow', label='Below Line', marker='o')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid()
plt.legend()
plt.show()

    
