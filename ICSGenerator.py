import sys
def getData():
    inp=input("Enter event title(type ENDE to end entering events): ")
    if inp=="ENDE":
        return "END"
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
    f = open(l+'.ics', 'ab')
    f.write(bytes("BEGIN:VCALENDAR\n", 'UTF-8'))
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
