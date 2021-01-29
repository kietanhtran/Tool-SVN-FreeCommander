from jira import JIRA

 

options = {"server": "https://jira.banvien.com.vn"}
user = "kiet.tran-anh"  #your username log in JIRA
pw = "Pass1234"  #your password log in JIRA
jira = JIRA(options, basic_auth=(user,pw))
#issues = dict()
issues = jira.search_issues("issue='MUT-830' or (assignee=currentUser() and status!=done)")
#print (issues)
print "You have a total",len(issues),"tasks."

 

for i in range(0, len(issues)): 
    #print (issues[i])
    pos = i
    print "Task",pos+1, ":", issues[i], ":",issues[i].fields.summary
    #print (" -> Name: ",issues[i].fields.summary)
    #print ("      Status: ",issues[i].fields.status)
print ("==================================================")

while 1:
    value = raw_input("You choose task number ? ")
    ID_JIRA = issues[int(value)-1]
    print "=== ",issues[int(value)-1].fields.summary," ==="
    time = raw_input("Spent time (5h, 30m...): ")
    com = raw_input("Comment: ")
    print "You want to log work on: "
    print "    1. Today"
    print "    2. Other date"
    choice = raw_input("You choose 1 or 2 ? ")
    if int(choice) == 2:
        date = raw_input("Date (yyyy-mm-dd): ")
        date += "T17:20:00.000+0700"
    else:
        date = None
    yn = raw_input("You will continue to log work? (Y/N)? ")   
    if yn == "Y": 
        jira.add_worklog(ID_JIRA, timeSpent=time, comment=com, started=date)
        print ("======================= Done =====================")
    elif yn == "N":
        print ("===================== Canceled ===================")
    else:
        print ("===================== Try again ==================")