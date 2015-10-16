import sys
def getData():
    inp=input("Enter event title : ")
    if inp=="ENDE":
        return
    else:
        f=""
        f+=('BEGIN:VEVENT\nSUMMARY:'+inp+"\n")
        inp=input("Enter start date and time (in format YYYYMMDDTHHMMSS) : ")
        f+=('DTSTART:'+inp+"\n")
        inp=input("Enter end date and time (in format YYYYMMDDTHHMMSS) : ")
        f+=('DTEND:'+inp+"\n")
        print("Enter Description (Use Ctrl-D to end writing description) : ")
        message = sys.stdin.readlines()
        f+=('DESCRIPTION:'+''.join(message)+"\n")
        f+=("END:VEVENT\n")
        return f
def process():
    k=input("Enter number of events : ")
    l=input("Enter filename : ")
    for i in range(0,int(k)):
        string = getData()
        m = input("Is this event alright?(Y/N) : ")
        if m=='Y':
            f = open(l+'.ics', 'wb')
            print("Writing " + string + "...\n")
            f.write(bytes(string, 'UTF-8'))
            f.close()
        else:
            print("Rerunning the event maker...\n")
def menu():
    
if __name__ == "__main__":
    menu()
