import os
import datetime
local_time = datetime.datetime.now()

while True:
    print("""\
        ::::::::::::::::::::::::::::::::
                   Check List 

        1. Add     Check  List
        2. Update  Check  Point
        3. Remove  Check  List
        4. Show    Check  List
        5. Exit
        ::::::::::::::::::::::::::::::::
        """)
    option = int(input(" Select the Option :- "))
    # print(option)
    if option == 1:
        f = open("checklistname.txt","rt")
        content =f.read()
        a = eval(content)
        size_dic = len(a)+1
        check_name = input("Enter the New check point Name :- ")
        f = open("checklistname.txt","w")
        a[size_dic]=check_name
        dics = str(a)
        f.write(dics)
        f.close()
    elif option == 2:
        f = open("checklistname.txt","rt")
        content =f.read()
        a = eval(content)
        for i in a :
            print(i,".",a[i])
        options = int(input("Enter the option :- "))
        file_name =a[options] +'.txt'
        f = open(file_name,"a")
        data = input("Enter commit :- ")
        datas = data+'   ---->   '+str(local_time)+'\n'

        f.write(datas)
        f.close()
        
    elif option == 3:
        f = open("checklistname.txt","rt")
        content =f.read()
        a = eval(content)
        for i in a :
            print(i,".",a[i])
        optionse = int(input("Enter the option :- "))
        file_name =a[optionse] +'.txt'
        # remove file
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print("The file does not exist")
        # remove name to checklistname
        b={}
        n=1
        f = open("checklistname.txt","w")
        if optionse != a[i]:
            b[n]=a[i]
            n+=1
        dics = str(b)
        f.write(dics)
        f.close()

    elif option == 4:
        f = open("checklistname.txt","rt")
        content =f.read()
        a = eval(content)
        for i in a :
            print(i,".",a[i])
        optionse = int(input("Enter the option :- "))
        file_name =a[optionse] +'.txt' 
        f = open(file_name,"rt")
        print("""
        ::::::::::::::::::::::::::::::::
        """)
        print('\t',a[optionse],"Check List\n")
        for line in f:
           
            print('\t',line,end="")
        f.close()
        print("""\
        ::::::::::::::::::::::::::::::::
        """)
    elif option == 5:
        print("Are you want exit y/n")
        n = input("Enter y for yes & n for No")
        if n =='y':
            break
        else:
            continue

    else:
        print("please select rigth option")
        continue

