import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from redminelib import Redmine 

# ------- Modify here ------- #
keyRedmine="5b0fd80da4413c8d7f33dec58942b96346dc9f51"
userID="5158"
module = "GPT"
pic = "Kiet Tran"
sublead = "Bang Nguyen"
progress = "0 -> 100%"
deadline = "19 - Apr"
delay = "0"
fromDate = ""
toDate = ""
# --------------------------- #

root = tk.Tk()
def Get_from_date():
    global fromDate
    fromDate = str(cal.selection_get())

def Get_to_date():
    global toDate
    toDate = str(cal.selection_get())
    
cal = Calendar(root,font="Arial 12", selectmode='day',cursor="hand2")
cal.pack(fill="both", expand=True)
ttk.Button(root, text="From this date", command=Get_from_date).pack()
ttk.Button(root, text="To this date", command=Get_to_date).pack()
root.mainloop()
redmine = Redmine('https://socrm.dgn.renesas.com', key=keyRedmine,requests={'verify': False})

print ("-------------------------------------------------------------------------------------------------")
print ("||Module||PIC||Sub-leader||Task||Progress||Deadline||Delays(in days)||Issue/risk||Countermeasure||Note")
time = redmine.time_entry.filter(user_id=userID, from_date=fromDate, to_date=toDate)
for log in time:  
    issue = redmine.issue.get(int(log.issue))
    res = "#"+str(log.issue)+" - "+str(issue)
    res = res.replace('[', '[[')
    res = res.replace(']', ']]')
    print ("|"+module+"|"+pic+"|"+sublead+"|"+res+"|"+progress+"|"+deadline+"|"+delay+"|-|-|-|")
