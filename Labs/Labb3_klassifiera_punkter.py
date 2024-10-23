import matplotlib.pyplot as plt
import numpy as np



X = []
Y = []

with open(r"C:\Code\python-programming-Filip-Karlsson\Data\unlabelled_data.csv", "r") as f_read:
    lines = f_read.readlines()
    for line in lines:
        x, y = map(float, line.split(","))
        X.append(x)
        Y.append(y) 


x_line = [-5.53, 4.74]
y_line = [-4.19, 3.40]


slope = (y_line[1] - y_line[0]) / (x_line[1] - x_line[0])
intercept = y_line[0] - slope * x_line[0]

def classify_points(X, Y, slope, intercept):
    labels = []
    #for loopen går igenom alla punkter och ränkar ut y-värdet för linjen vid den x-koordinaten.
    #Beroende på y värdet är över eller under den uträknade y värdet så läggs värdena in i above_line listan eller below_line listan
    for x, y in zip(X, Y):
        y_on_line = slope * x + intercept
        if y > y_on_line:
            labels.append((x, y, 1))  # Sparar 1 ifall den är över linjen
        else:
            labels.append((x, y, 0))  # Spara 0 ifall den är under linjen
    
    return labels

#kallar på funktionen
labelled_points = classify_points(X, Y, slope, intercept)

# Write labelled points to a new file
with open(r"C:\Code\python-programming-Filip-Karlsson\Data\labelled_data.csv", "w") as f_write:
    f_write.write("1 above the line, 0 under the line \n")
    for x, y, label in labelled_points:
        f_write.write(f"{x},{y},{label}\n")
