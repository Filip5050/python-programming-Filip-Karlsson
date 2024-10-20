
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
        return "1"
    else:
        return "0"
    
positions = []   
# Check position of each point relative to the line
for x, y in zip(X, Y):
    position = point_position(x, y, x_line, y_line)
    positions.append(position)


with open(r"C:\Code\python-programming-Filip-Karlsson\Data\labelled_data.csv", "w") as f_write:
    # Optionally write a header
    f_write.write("x,y,position\n")
    
    for x, y in zip(X, Y):
        position = point_position(x, y, x_line, y_line)
        # Write the point and its classification to the new file
        f_write.write(f"{x},{y},{position}\n")