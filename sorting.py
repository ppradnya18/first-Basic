
def sorrtig_string():
    std = input()
    smallletter=""
    uppercase =""
    odddigit =""
    evendigit=""

    if std.isalnum() == True:
        for i in std:

            if i.isupper() == True:
                uppercase+=i
            elif i.islower() == True:
                smallletter+=i
            elif i.isdigit() == True:
                if int(i)%2 != 0:
                    odddigit+=str(i)
                else:
                    evendigit+=i

        return smallletter+uppercase+odddigit+evendigit
                

sorrtig_string()