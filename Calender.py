import calendar
import datetime
import os
from colorama import Back, init
if os.name=="nt": init(convert=True);

now = datetime.datetime.now()
month = calendar.monthcalendar(now.year,now.month);

for i in range (len(month[0])):
    if month[0][i]!=0: monthStart=i; break;

calendarPath ="Documents\\calendar.txt"
hovered = ""
today= ""
selected =[0,monthStart]
def grep (file, search, printy):
    i=0
    dayline = 0;
    with open(file,'r') as f:
        for line in f.readlines():
            i+=1;
            if search in line:
                dayline=i;
                if printy:
                    print(line, end ='');
        return dayline;
def drawCalender():
    cal=   "  __________________________________\n /"+calendar.month_name[now.month]
    for i in range (34-len(calendar.month_name[now.month])):cal+= " "
    cal += "\\\n │_Mo_│_Tu_│_We_│_Th_│_Fr_│_Sa_│_Su_│\n"
    for w in range (len(month)):
        for d in range (len(month[w])):
            if w==selected[0] and d==selected[1]: hovered=Back.GREEN
            else: hovered=""
            if w==(now.day+monthStart)//7 and d==(now.day-2)%7: today=Back.CYAN #I have no clue why this -2 makes it work
            else: today=""
            if d ==(len(month[w])-1):
                    if month[w][d] == 0:cal+=" │    │\n";break
                    if(month[w][d])<10:cal+=" │  " +today+hovered+str(month[w][d])+Back.RESET+ " │\n" ;break
                    cal+=" │ "+today+hovered+str(month[w][d])+Back.RESET + " │\n" ;break        
            if month[w][d] == 0 and w==0: cal += " │   "
            else:
                if month[w][d] <10:
                    cal+=" │  " +today+hovered+str(month[w][d])+Back.RESET
                else:
                    cal+=" │ "+today+hovered+str(month[w][d])+Back.RESET
    cal+=" \\__________________________________/"
    os.system('cls' if os.name == 'nt' else 'clear')
    print(cal)

def getDate():
    date = input()
    if date.isdigit() :
        return int(date)
    else:
        if date=="" or date is None:
            drawCalender();
            return getDate();

        if date.find("q")==0 and date.find('@')==-1:
            os.system("cls" if os.name =="nt" else "clear");
            exit();   

        if date.find("@")==0:
            grep(calendarPath,date,True)
            return getDate()

        if date.find("w")==0:
            if date[0:].isdigit and len(date)>1:
                if((int(date[1:])*7-monthStart-6)<0):
                    return 1
                else:
                    return int(date[1:])*7-monthStart-6
            else:
                os.system("cls" if os.name =="nt" else "clear");
                drawCalender()
                return getDate()
        if date.find("e")==0: 
            if os.name!='nt':  
                if date[1:].isdigit():
                    os.system("nvim +"+ grep(calendar,str(now).split("-")[0]+"-"+str(now).split("-")[1]+"-"+(str(singleDate(date))[0:]),False)+" ~"+calendarPath)
                    return int(date[1:])
                else:
                    drawCalender();
                    return getDate();
            else:
                if date[1:].isdigit():
                    tmp = grep(calendarPath, str(now)[:8]+str(singleDate(int(date[1:]))), False)
                    os.system("subl %userprofile%\\"+calendarPath+":"+str(tmp))
                    return int(date[1:])
                else:
                    drawCalender();
                    return getDate();
        else:
            drawCalender();
            return int(getDate());

def singleDate(num):
    if num<10:
        num=str(("{:02d}".format(num)))
        return num
    else:
        return num
        
def moveCursor(Intdate):
        selected[0] = (Intdate+int(monthStart)-1)//7
        selected[1]=  (Intdate+int(monthStart)-1)%7
        drawCalender()
    
drawCalender()
grep(calendarPath,str(now).split(" ")[0],True);
while True:
    date=getDate()
    moveCursor(date)
    grep(calendarPath, str(now)[:8]+str(singleDate(date))[0:], True)
#Get back highlighting for today
#Add highlighting for days with @ tags
#Add config/options
#Add being able to see other months
#Add todo veiw on the right or below the calender
#Add proper editing - i think i did it
#make sure things work on other OSes - i think i did this too
