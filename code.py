import time
import math
print("Know Your attendence")
tc=int(input("Enter TOTAL NUMBER OF CLASSES:"))
tca=int(input("Enter CLASS YOU ATTENDED:"))
print()
if tc>tca:
    per=((tca/tc)*100)
    time.sleep(0.3)
    print("Your Latest Attendance is: {:.2f}%".format(per))
    print()
    time.sleep(0.3)
    print("Absent Classes:",tc-tca)
    print()
    if per < 75:
        if per < 75:
            i=0
            while per < 75:
                tca += 1
                tc += 1
                per = (tca / tc) * 100
                i+=1
            print("You need to attend ",i,"class more for 75% attendance")
            
        if per < 80:
            j=0
            while per < 80:
                tca += 1
                tc += 1
                per = (tca / tc) * 100
                j+=1
            print("and",i+j,"class more for 80% attendance")

    elif per > 75 and per < 80:
        if per > 75:
            i=0
            j=0
            while per > 75:
                tc +=1
                per = (tca / tc) * 100
                i += 1
            print("You can bunk ",i+j-1,"class(es) and maintain 75% attendance")
        if per < 80:
            j=0
            i=0
        while per < 80:
            tca += 1
            tc += 1
            per = (tca / tc) * 100
            j+=1
        print("and attend ",i+j,"class(es) more for 80% attendance")
    
    else:
        if per > 75:
            j = 0
            while per > 80:
                tc += 1
                per = (tca / tc) * 100 
                j += 1
            print("You can bunk", j-1 , "class(es) and maintain 80% attendance")
        
            if per > 75:
                i=0
                while per > 75:
                    tc +=1
                    per = (tca / tc) * 100
                    i += 1
                print("and bunk ",i+j-1,"class(es) and still maintain 75% attendance")
else:
    print('Enter valid details')
 # type: ignore
