# Ripser-Input-Generator
Generates a text file containing pairwise distances of points from a csv file.

To run program enter the following command in WSL:

python main.py

It will then ask you to input the path of the file which you want to convert to a lower-triangular distance matrix. Then it will ask you what you want your output
to be called. 

Finally, run 

./ripser (output from previous step)

You must format the csv file as

v11 v12 v13 ... v1n
v21 v22 v23 ... v2n
...
vm1 vm2 vm3 ... vmn


