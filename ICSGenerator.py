import sys
import time as t
TimeWC=0
def eachComp():
    inp = input("Enter year : default is [" + t.strftime("%Y") + "] : ")
    y=''
    if inp.strip() == '':
        y+= t.strftime("%Y")
    else:
        y+=inp
    inp = input("Enter month : default is [" + t.strftime("%m") + "] : ")
    if inp.strip() == '':
        y += t.strftime("%m")
    else:
        y+=inp
    inp = input("Enter day : default is [" + t.strftime("%d") + "] : ")
    if inp.strip() == '':
        y += t.strftime("%d")+ "T"
    else:
        y+=inp + "T"
    inp = input("Enter hours : default is [" + t.strftime("%H") + "] : ")
    if inp.strip() == '':
        y+= t.strftime("%H")
    else:
        y+=inp
    inp = input("Enter minutes : default is [" + t.strftime("%M") + "] : ")
    if inp.strip() == '':
        y += t.strftime("%M")
    else:
        y+=inp
    inp = input("Enter seconds : default is [" + t.strftime("%S") + "] : ")
    if inp.strip() == '':
        y += t.strftime("%S")
    else:
        y+=inp
    print(y)
    return y
def getStuff(prompt, forWhat):
    invalid=True
    while(invalid):
        inp=input(prompt)
        if inp=='woo':
            y = eachComp()
            global TimeWC
            if TimeWC == 0:
                print("Write down or copy-paste this format if you don't want to waste your time (Ha time :P) : " + y)
                TimeWC += 1
            elif TimeWC ==1:
                TimeWC += 1
                print("Dude, write down or copy-paste this format if you don't want to waste your time again. : " + y)
            elif TimeWC ==2:
                TimeWC+=1
                print("Dude, I'm serious. I'm not gonna suggest you anything the next time. : " + y)
            else:
                TimeWC+=1
                print("-.- wtv... : "+y)
                invalid=False
            return (forWhat+y+"\n")
            
        elif not(inp[0:8].isdigit() == True and inp[8]=='T' and len(inp)==15 and inp[9:].isdigit()):
            print("That's invalid.")
            invalid=True
            continue
        else:
            invalid=False
            return (forWhat+inp+"\n")
            
def getData():
    valid=False
    while not valid:
        inp=input("Enter event title(type ENDE to end entering events): ")
        if inp.strip()=='':
            print("Plz enter title... ")
            valid=False
        else:
            valid=True
    if inp=="ENDE":
        return "END"
    else:
        f=""
        f+=('BEGIN:VEVENT\nSUMMARY:'+inp+"\n")
        
        f+=getStuff("Enter start date and time (in format YYYYMMDDTHHMMSS) or type woo to enter each component separately : ", 'DTSTART:')
        f+=getStuff("Enter end date and time (in format YYYYMMDDTHHMMSS) or type woo to enter each component separately : ", 'DTEND:')
        print("Enter Description (Use Ctrl-D to end writing description) : ")
        message = sys.stdin.readlines()
        f+=('DESCRIPTION:'+r''.join(message)+r"\n")
        f+=("END:VEVENT\n")
        return f
def process():
    k=input("Enter number of events : ")
    l=input("Enter filename : ")
    f = open(l+'.ics', 'ab')
    f.write(bytes("BEGIN:VCALENDAR\nVERSION:2.0\nPRODID:!!!JOHNCENA!!!(Not rly)(satej1210)(<-Thass me)\n", 'UTF-8'))
    f.close()
    i=0
    while i < int(k):
        string = getData()
        if string=="END":
            print("Ending...")
            break
        m = input("Is this event alright?(Y/N) : ")
        if m=='Y':
            f = open(l+'.ics', 'ba')
            print("Writing event to ICS...\n")
            f.write(bytes(string, 'UTF-8'))
            f.close()
            i+=1
        else:
            print("Rerunning the event maker...\n")
            i=-1
    f = open(l+'.ics', 'ab')
    f.write(bytes("END:VCALENDAR", 'UTF-8'))
    f.close()
    print("Your file has been saved as " + l + ".ics")
if __name__ == "__main__":
    if len(sys.argv)==2:
        if sys.argv[-4:len(sys.argv[0])]==".csv":
            print("Woo! A CSV!\n")
        else:
            print("Please gimma a CSV file(yes, with the extension '.csv')\n")
    else:
        print("I see you wanna type in the events with this program... Let's start!\n")
        process()
