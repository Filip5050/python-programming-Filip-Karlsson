import matplotlib.pyplot as plt
import numpy as np


X = []
Y = []

with open(r"C:\Code\python-programming-Filip-Karlsson\Data\unlabelled_data.csv", "r") as f_read:
   lines = f_read.readlines()
   for line in lines:
      split = line.split()
      x, y = map(float,line.split(",")) #sepererar punkterna/kordinaterna så jag kan få in rätt nummer i respektive lista
      X.append(x) #lägger in x kordinaterna in i min X fil
      Y.append(y) #lägger in y kordinaterna in i min y fil



#Förberear jag min linje till grafen, där jag har valt en x och y linje som sepererar grafen ungefär i mitten
x_line = [-5.53, 4.74]
y_line = [-4.19,3.40]




import matplotlib.pyplot as plt
import numpy as np

def point_position(x, y, x_line, y_line):
    
    #här gör vi två variabler och ger dom värdena från listans som läggs in som argument i funktionen.
    x1, y1 = x_line
    x2, y2 = y_line
    #här räknar jag ut m värdet i linjära vinkeln ekvationen y=kx+m
    m = (y2 - y1) / (x2 - x1)
    b = y1 - m * x1
    y_on_line = m * x + b
    # Determine position
    if y > y_on_line:
        return "right"
    else:
        return "left"
   
   # Check position of each point relative to the line
for x, y in zip(X, Y):
    position = point_position(x, y, x_line, y_line)
    print(f"Point ({x}, {y}) is {position} the line.")


plt.figure(figsize=(10, 6))
plt.scatter(X,Y)
plt.plot(x_line,y_line)
plt.title('Scatter plot of the the coordinates in unlabelled_data')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid()




plt.show()

    
