"""
Personal Pattern Maker. A fun program which makes unique patterns
depending on the person's first and last name and month and day of birth.
"""

import numpy as np
import matplotlib.colors as col
import matplotlib.pyplot as plt
import wx

# GUI for first name
app = wx.App()
       
def my_input():
    """first name will initially be equal to first"""
    box = wx.TextEntryDialog(None, "What is your first name?", "First Name Box")
    
    if box.ShowModal() == wx.ID_OK:
         
         if box.GetValue() == "":
             print "please enter valid name"
             return my_input()
         else:
             first = box.GetValue()
             return first
                
first = my_input()

# converts 1st character to hex value then to int value    
for item in first.split():    
            N = item[0]
            print N
            x = N.encode("hex")
            print x
            r = int(x, 16)
            print r
            f = (r - 23) * .01
            print f

# GUI for last name
app2 = wx.App()
        
def my_input():
    """last name will initially be equal to last_name"""
    box = wx.TextEntryDialog(None, "What is your last name?", "Last Name Box")
    if box.ShowModal() == wx.ID_OK:
        if box.GetValue() == "":
            print "please enter valid name"
            return my_input()
        else:
            last_name = box.GetValue()
            return last_name

last_name = my_input

# length of last name is converted into a value    
for (last_name) in iter(my_input, ""):    
    last_value = len(last_name)
    print int(last_value)
    if (last_value) > 1 and (last_value) < 9:
        v = (last_value) * 0.1 
        print v
        break
    elif (last_value) == 9:
        v = (last_value) * 0.1
        print v
        break
    elif (last_value) > 9:
        if int(last_value) >= 9 and int(last_value) <= 19:
            v = ((last_value) / 2) * 0.1
            print v  
            break
        elif int(last_value/2) >= 9 and int(last_value/2) <= 19:
            v = ((last_value) / 4) * 0.1
            print v
            break
        else:
            print "Please type a shorter last name please!"
            continue
    else:
        v = (last_value) * 0.1 * 2
        print v
        break
# v value is plugged into formulas towards bottom  
    
# GUI for month of birth
app3 = wx.App()

def my_input():
    """month will initially be equal to month_name"""
    box = wx.TextEntryDialog(None, "What month were you born?", "Month Box")
    if box.ShowModal() == wx.ID_OK:
        
        if box.GetValue() == "":
            print "please enter valid month"
            return my_input()
        else:
            month_name = box.GetValue().lower()
            return month_name

month_name = my_input
        
# months are converted to numbers. the various options
# allows for multiple user entry variations.    
for (month_name) in iter(my_input, ""):    
    if (month_name) in {"january", "jan", "1", "01"}:
        month_value = 1
        print month_value
        break
    elif (month_name) in {"february", "feb", "2", "02"}:
        month_value = 2
        print month_value
        break 
    elif (month_name) in {"march", "mar", "3", "03"}:
        month_value = 3
        print month_value
        break   
    elif (month_name) in {"april", "apr", "4", "04"}:
        month_value = 4
        print month_value
        break  
    elif (month_name) in {"may", "5", "05"}:
        month_value = 5
        print month_value
        break  
    elif (month_name) in {"june", "6", "06"}:
        month_value = 6
        print month_value
        break 
    elif (month_name) in {"july", "7", "07"}:
        month_value = 7
        print month_value
        break    
    elif (month_name) in {"august", "aug", "8", "08"}:
        month_value = 8
        print month_value
        break 
    elif (month_name) in {"september", "sep", "9", "09"}:
        month_value = 9
        print month_value
        break 
    elif (month_name) in {"october", "oct", "10"}:
        month_value = 10
        print month_value
        break          
    elif (month_name) in {"november", "nov", "11"}:
        month_value = 11
        print month_value
        break
    elif (month_name) in {"december", "dec", "12"}:
        month_value = 12
        print month_value
        break
    else:
        print "Please spell your month correctly or type the month's numbers again." 
        continue

mv = int(month_value) * .01
print mv 
# mv value is plugged into formulas towards bottom

# GUI for date of birth
app4 = wx.App()

def my_input():
    """day of birth will initially be equal to date"""
    box = wx.TextEntryDialog(None, "What day of the month were you born?", "Day Box")
    if box.ShowModal() == wx.ID_OK:
        if box.GetValue() == "":
            print "please enter valid date"
            return my_input()
        else:
            date = box.GetValue()
            return date

date = my_input
       
error_template = "'{}' not a valid day."    
for (date) in iter(my_input, ""):
    try:
        date = int(date)
    except ValueError:
        pass
    if 0 < date < 32:
        day = date
        print day
        break
    print error_template.format(date)

d = day * .01 * 9
print d
# mv value is plugged into formulas towards bottom

# the mathematical formulas below, that make the patterns, are adapted from 
# matplotlib's library and gallery found at 
# http://matplotlib.org/gallery.html. 
# it is a combination of various patterns and formulas. 

# variables from above GUIs change the color values below in r, g, b
cdict1 = {'red': ((0.0, mv, mv),    
                     ((v-0.1), f, 0.5),
                     (v, 0.7, 0.7),
                     (0.9, 0.8, (mv*6)), 
                     (1.0, f, d)),
                                         
          'green':  ((0.0, mv, 0.0),  
                    (0.2, 0.8, 0.8), 
                    (v, (mv*6), (mv*6)),  
                    (0.9, 0.0, 0.0),
                    (1.0, f, 0.7)),
          
          'blue':   ((0.0, 1.0, 1.0), 
                    ((v-0.1), (7*mv), (7*mv)),  
                    (v, 0.0, 0.0),
                    (0.9, f, 0.0), 
                    (1.0, d, 1.0))}  
                    
# day of the month (variable d) changes gamma below                     
blue_red1 = col.LinearSegmentedColormap('my_colormap', cdict1, N=256, gamma=d)

# month value changes last number in both X and Y below
X,Y = np.mgrid[-10:10:mv,20:40:mv]

# day of the month (d) and first name (f) change below
Z = v**np.sqrt(f**X**2+Y**d)+np.sin(v*X**2+Y**d)

plt.figure(figsize=(9,9))
plt.subplots_adjust(left=0.02, bottom=0.06, right=0.95, top=0.94, wspace=0.05)

plt.subplot(1,1,1)
plt.imshow(Z, interpolation='bicubic', cmap=blue_red1,visible=True) 

plt.show()

