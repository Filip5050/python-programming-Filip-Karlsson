
X = []
Y = []
with open(r"C:\Code\python-programming-Filip-Karlsson\Data\unlabelled_data.csv", "r") as f_read, open(r"C:\Code\python-programming-Filip-Karlsson\Data\unlabelled_data.csv", "a") as f_append:
   lines = f_read.readlines()
   for line in lines:
      split = line.split()
      x, y = map(float,line.split(",")) #sepererar punkterna/kordinaterna så jag kan få in rätt nummer i respektive lista
      X.append(x) #lägger in x kordinaterna in i min X fil
      Y.append(y) #lägger in y kordinaterna in i min y fil