# importing the tkinter module
from optparse import Values
import tkinter as tk;
from tkinter.ttk import *

def knapSack(W, wt, val, n):
 
    # Base Case
    if n == 0 or W == 0:
        return 0
 
    # If weight of the nth item is
    # more than Knapsack of capacity W,
    # then this item cannot be included
    # in the optimal solution
    if (wt[n-1] > W):
        return knapSack(W, wt, val, n-1)
 
    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        return max(
            val[n-1] + knapSack(
                W-wt[n-1], wt, val, n-1),
            knapSack(W, wt, val, n-1))

# initializing the tkinter
root = tk.Tk()

# setting the width and height of the gui
root.geometry("1200x1200")  

values = tk.StringVar()
weights = tk.StringVar()
w = tk.IntVar()
output = tk.IntVar()
output.set(0)


tk.Label(root, text="Knapsack Solver", font="calibri 20 bold")

# Creating a text label widget

# Creating a entry widget to take password length entered by the 
# user
entry1 = tk.Label(root, text="Enter values in the form (12 14 17)")
entry2 = tk.Label(root, text="Enter the corresponding weights in the form (5 6 9)")
entry3 = tk.Label(root,text="Enter max weight W")
an = tk.Label(root,text="output")

entry1.grid(row = 0, column = 0, sticky = 'w', pady = 2)
entry2.grid(row = 1, column = 0, sticky = 'w', pady = 2)
entry3.grid(row = 2, column = 0, sticky = 'w', pady = 2)
an.grid(row = 3, column = 0, sticky = 'w', pady = 2)

e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)
an = Entry(root, textvariable=output)

e1.grid(row = 0, column = 2, pady = 2)
e2.grid(row = 1, column = 2, pady = 2)
e3.grid(row = 2, column = 2, pady = 2)
an.grid(row = 3, column = 2, pady = 2)

b1 = Button(root, text = "submit")
b1.grid(row = 4, column = 1, sticky = 'E')







root.mainloop()

def enterItems():
    items1 = entry1.get()
    items2 = entry2.get()
    lst1 = [int(item) for item in items1.split()]
    lst2 = [int(item) for item in items2.split()]
    weight = w.get()
    entry1.destroy()
    entry2.destroy()
    ans = knapSack(weight,items1,items2,len(items1))
    output.set(ans)
   


tk.Button(root, text="Submit", command=enterItems)




 
#Driver Code
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print (knapSack(W, wt, val, n))