while True:
    print("Welcome to Time Conversion")
    a=input("enter 12hr or 24hr format time you have")
    if(a=="12"):
        def timeconvert(str1):
            if str1[-2:] == "AM" and str1[:2] == "12":
                return "00" + str1[2:-2]
            elif str1[-2:] == "AM":
                return str1[:-2]
            elif str1[-2:] == "PM" and str1[:2] == "12":
                return str1[:-2]
            else:
                return str(int(str1[:2]) + 12) + str1[2:8]
        if __name__ == '__main__':
            n=input("enter hours")
            if(int(n)<=12):
                m=input("enter minutes")
                if(int(m)<=60):
                    o=input("enter seconds")
                    if(int(o)<=60):
                        str1=n+":"+m+":"+o
                        if(int(n)==00):
                            print("12 hr format",str1)
                            print("24 hr format",str1)
                        else:
                            mr=input("morning or noon")
                            if(mr=="morning"):
                                str1=n+":"+m+":"+o+"AM"
                                print("12 hr format",str1)
                                print("24 hr format",timeconvert(str1))
                            else:
                                str1=n+":"+m+":"+o+"PM"
                                print("12 hr format",str1)
                                print("24 hr format",timeconvert(str1))
                    else:
                        print("enter correct value of seconds")
                else:
                    print("enter correct value of minutes")
            else:
                print("enter valid 12hr format")
    elif(a=="24"):
        def convert(string):
            if int(string[:2]) >= 12:
                if(int(string[:2])==12):
                    return str(int(string[:2])) + string[2:8]+"PM"
                else:
                    return str(int(string[:2]) -12) + string[2:8]
                
            else:
                return n+":"+m+":"+o

        n=input("enter hours")
        if(int(n)<=24):
            m=input("enter minutes")
            if(int(m)<=60):
                o=input("enter seconds")
                if(int(o)<=60):
                    time=n+":"+m+":"+o
                    if(int(n)>=12):
                        if(int(n)==12):
                            print("24 hr format:",n+":"+m+":"+o)
                            print("12 hr format:",convert(time))
                        else:
                            print("24 hr format:",n+":"+m+":"+o)
                            print("12 hr format:",convert(time)+"PM")
                    else:
                        if(int(n)==00):
                            print("24 hr format:",n+":"+m+":"+o)
                            print("12 hr format:",str(int(n)+12)+":"+m+":"+o+"AM")
                        else:
                            print("24 hr format:",n+":"+m+":"+o)
                            print("12 hr format:",convert(time)+"AM")
                else:
                    print("enter correct value of seconds")
            else:
                print("enter correct value of minutes")
        else:
            print("enter valid 24hr format")
    else:
        print("choose correct format")
