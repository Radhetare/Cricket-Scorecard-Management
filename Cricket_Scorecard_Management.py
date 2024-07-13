# random and mysql.connector module is imported
import random
import mysql.connector as sql

# Identifiers used in program
t = None
choice1 = None
choice2 = None
myteam = []
opponentteam = []
total = []
run_can_be=["0","1","2","3","4","6","Out","out"]
teamnames = ["CSK","DC","KKR","MI","PK","RR","RCB","SRH"]
CSK = ["Ruturaj Gaikwad","Faf du Plessis","Moeen Ali","Robin Uthappa","Ambati Rayudu",
             "M.S.Dhoni","Ravindra Jadeja","Dwayne Bravo","Shardul Thakur","Deepak Chahar","Josh Hazlewood"]
DC = ["Shikhar Dhawan","Prithvi Shaw","S.Smith","Rishabh Pant","Shreyas Iyer",
            "Shimron Hetmyer","Marcous Stoinis","Axar Patel","Ravichandran Ashwin","Kagiso Rabada","Avesh Khan"]
KKR = ["Venkatesh Iyer","Shubhman Gill","Nitish Rana","Rahul Tripathi","Eoin Morgan",
             "Dinesh Karthik","Andhre Russell","Sunil Narine","Varun Chakravarthy","Shivam Manvi","Lockis Ferguson"]
MI = ["Rohit Sharma","Quinton de Cock","Ishan Kisan","Suryakumar Yadav","Krunal Pandya",
            "Hardik Pandya","Keiron Pollard","Adam Milne","Rahul Chahar","Jasprit Bumrah","Trent Boult"]
PK = ["K.L.Rahul","Mayank Aggarawal","Chris Gayle","David Malan","Deepak Hooda","Shahruk Khan",
            "Chris Jordan","Harpreet Brar","Ravi Bishnoi","Mohammed Shami","Riley Meredith"]
RR = ["Evin Lewis","Jos Buttler","Y.Jaiswal","Sanju Samson","L.Livingstone","Ben Stroke",
            "M.Lomror","Riyan Parag","Rahul Tewatiya","Chris Moris","Chetan Sakariya"]
RCB = ["Virat Kohli","Devdutt Padikkal","S.Bharat","Glenn Maxwell","A.B.de Villiers",
             "D.Christian","Shahbaz Ahmed","Mohammed Siraj","Harshal Patel","Yuzendra Chahal","Kyle Jamieson"]
SRH = ["Jason Roy","David Warner","Kane Williamson","Priyam garg","Abhishek Sharma","Abdul Samad",
             "Jason Holder","Rashid Khan","Bhuvneshwar Kumar","Sandeep Sharma","Umran Malik"]

# Design Function used to print design
def design(side, ending = 81, middle = "", title = ""):
    for x in range(ending):
        if x == middle:
            print(title, end=side)
        else:
            print(side, end = "")
    print()
    print()

# Function to check whether the input is number or not
def number_checker(no, list = None):
    if no.isdigit() and list == None:
        return True
    elif no.isdigit() and no in list :
        return True
    else:
        return False

# Function to check whether value is provided or not
def nothing(a):
    if a in [""] :
        return True
    elif a.isspace():
        return True
    else:
        return False

# Function for bating 
def bating(over,inning=1,Target=0):
    count = 0
    Run = 0
    bat_inn1 = {}
    bowl_inn1 = {}
    for Balls in range(1,(over*6)+1):
        if (Balls==1):
            design("-")
            while True:
                bat =input("\nEnter name of batsman from your team : ")
                if (bat not in myteam):
                    print("Please enter name from the given list :\n",myteam)
                else:
                    myteamcheck=list()
                    myteamcheck.append(bat)
                    bat_inn1[bat] = {"Ball":0,"6s" : 0,"4s" : 0, "Total" : 0}
                    break
            bowl =random.choice(opponentteam)
            bowl_inn1[bowl] = {"Overs":0,"Wickets" : 0, "Total" : 0}
            print("\nBowler for the over is :",bowl)
            print()
        
        while True: # To check for vaild input
            run=input("Enter run scored on current ball : ")
            if run in ["Out","OUT"]:
                run="Out"
                break
            if run not in run_can_be:
                print("\nPlease enter",run_can_be,"from this only\n")
            else:
                break

        if run in ["Out","out"] : # To check whether player is out or not
            bowl_inn1[bowl]["Wickets"] += 1
            print(bat,"is out")
            count+=1
            if(Balls==over*6):
                pass
            elif(count==10):
                print("\nYour 10 batsman are out")
                break
            else:
                while True:
                    bat=input("Enter name of next batsman : ")
                    if(bat not in myteam):
                        print("Please enter name from the given list :\n",myteam)
                    elif(bat in myteamcheck):
                        print("This batsman is already out\nPlease choose another one from the given list :\n",myteam)
                    else:
                        myteamcheck.append(bat)
                        bat_inn1[bat] = {"Ball":0,"6s" : 0,"4s" : 0, "Total" : 0}
                        break
        else: # To append values in dictionaries
            bat_inn1[bat]["Total"] += int(run)
            bat_inn1[bat]["Ball"] += 1
            if run=="4":
                bat_inn1[bat]["4s"] += 1
            elif run == '6':
                bat_inn1[bat]["6s"] += 1
            
            bowl_inn1[bowl]["Overs"] += 1
            bowl_inn1[bowl]["Total"] += int(run)

        if(Balls%6==0): # To check for a over completion
            design("-")
            bowl=random.choice(opponentteam)

            if(Balls==over*6):
                pass
            else:
                if bowl_inn1.get(bowl,True) == True:
                    bowl_inn1[bowl] = {"Overs":0,"Wickets" : 0, "Total" : 0}
                print("\nBowler for the over is :",bowl)
                print()

        if(run.isdigit()):
            A = int(run)
            Run += A

        if inning == 1:
            pass
        else:
            if Run > Target : # To check for target achieved
                print("\nTotal run scored by",opponentteamname,"=",Target)
                print("Total run scored by",myteamname,"=",Run)
                print()
                print(myteamname,"won the match")
                design("-")
                break

    for x in bowl_inn1:   # To convert no. of balls to no. of overs
        bal = bowl_inn1[x]["Overs"]
        ov = bal//6
        rem = (bal%6) * 0.1
        ov += rem
        bowl_inn1[x]["Overs"] = ov

    if inning ==2 :
        if Run <= Target:
            print("\nTotal run scored by",opponentteamname,"=",Target)
            print("Total run scored by",myteamname,"=",Run)
            print()
            if Run < Target :
                print(myteamname,"won the match")
            else:
                print("\nThe match is tie between both the teams")
            design("-")

        return Run , bat_inn1 , bowl_inn1

    else:
        print("Total run scored by",myteamname,"=",Run)
        print("\nNow",opponentteamname,"has to make",Run+1,"run to win the match")
        return Run , bat_inn1 , bowl_inn1

# Function for bowling
def bowling(over,inning=1,Target=0):
    count = 0
    Run = 0
    bat_inn2 = {}
    bowl_inn2 = {}
    for Balls in range(1,(over*6)+1):
        if(Balls==1):
            design("-")
            while True:
                bowl=input("\nEnter name of the bowler for this over : ")
                if(bowl not in myteam):
                    print("Please enter name from the given list :",myteam)
                else:
                    bowl_inn2[bowl] = {"Overs":0,"Wickets" : 0, "Total" : 0}
                    break
            bat=random.choice(opponentteam)
            bat_inn2[bat] = {"Ball":0,"6s" : 0,"4s" : 0, "Total" : 0}
            opponentteamcheck=list()
            opponentteamcheck.append(bat)
            print("\nBatsman :",bat)
            print()

        run =random.choice(["0","1","2","3","4","6","Out"])
        print("Run scored on the current ball :",run)

        if(run == "Out"):
            bowl_inn2[bowl]["Wickets"] += 1
            print(bat,"is out")
            count +=1
            if(Balls==over*6):
                pass
            elif(count == 10):
                print("\n10 Batsman are out")
                break
            else:
                bat =random.choice(opponentteam)
                while True:
                    if(bat in opponentteamcheck):
                        bat =random.choice(opponentteam)
                    else:
                        opponentteamcheck.append(bat)
                        bat_inn2[bat] = {"Ball":0,"6s" : 0,"4s" : 0, "Total" : 0}
                        break
                print("\nBatsman :",bat)
        else:
            bat_inn2[bat]["Total"] += int(run)
            bat_inn2[bat]["Ball"] += 1  
            if run=="4":
                bat_inn2[bat]["4s"] += 1
            elif run == '6':
                bat_inn2[bat]["6s"] += 1
            
            bowl_inn2[bowl]["Overs"] += 1
            bowl_inn2[bowl]["Total"] += int(run)

        if(Balls%6==0):
            design("-")
            if(Balls==over*6):
                pass
            else:      
                while True:
                    bowl=input("Enter name of bowler for this over : ")
                    if(bowl not in myteam):
                        print("Please enter name from the given list :",myteam)
                    else:
                        if bowl_inn2.get(bowl,True) == True:
                            bowl_inn2[bowl] = {"Overs":0,"Wickets" : 0, "Total" : 0}
                        break

        if(run.isdigit()):
            B=int(run)
            Run += B

        if inning == 2 and Run > Target:
            print("\nTotal run scored by",myteamname,"=",Target)
            print("Total run scored by",opponentteamname,"=",Run)
            print()
            print(opponentteamname,"won the match")
            design("-")
            break

    for x in bowl_inn2:
        bal = bowl_inn2[x]["Overs"]
        ov = bal//6
        rem = (bal%6) * 0.1
        ov += rem
        bowl_inn2[x]["Overs"] = ov

    if inning ==2 :
        if Run <= Target :
            print("\nTotal run scored by",myteamname,"=",Target)
            print("Total run scored by",opponentteamname,"=",Run)
            print()
            if Run < Target :
                print(opponentteamname,"won the match")
            else:
                print("\nThe match is tie between both the teams")
            design("-")

        return Run , bat_inn2 , bowl_inn2
    elif inning == 1:
        print("Total run scored by",opponentteamname,"=",Run)
        print("\nNow",myteamname,"has to make",Run+1,"run to win the match")
        return Run , bat_inn2 , bowl_inn2

# Function to print a specific line in particular order
def Print(y,val,space=" "):
    index = 0
    for x in y:
        sp = space
        lth = val[index]
        t=lth - len(str(x))
        l=t//2
        sp1 = sp*l
        if t%2 == 1:
            sp2 = (sp*l)+sp
        else:
            sp2 = sp*l
        index += 1
        sp3 = sp*len(str(x))
        if sp == "-":
            print("+-{0}{1}{2}-".format(sp1,sp3,sp2),end="")
        else:
            print("| {0}{1}{2} ".format(sp1,x,sp2),end="")
    if sp == " ":
        print("|")
    else:
        print("+")

# Function to create table of given columns and rows
def table(column,rows):
    count = 0
    lengths = []

    while count < len(column):
        y = 0
        for x in rows:
            if y < len(str(x[count])):
                y = len(str(x[count]))
        if y < len(str(column[count])):
            y = len(str(column[count]))
        lengths.append(y)
        count += 1
    
    Print(column,lengths,"-")
    Print(column,lengths)
    Print(column,lengths,"-")

    for y in rows:
        Print(y , lengths)

    Print(column,lengths,"-")

design("-")

design("-",40,20," Welcome to Cricket Scorecard Management ")

design("-")

while True: # To check username and password of mysql
    try :
        username = input("Username : ")
        passward = input("Passward : ")
        
        # Connection between mysql and python
        connector = sql.connect(host = "localhost" , user = username , passwd = passward)
        if connector.is_connected():
            print("\nYou are successfuly connected with MySQL\n")
            break
        else:
            print("\nPython is not able to connect with MySQL , try again\n")
    except :
        print("\nUsername or passward is incorrect , try again\n")

radhe = connector.cursor()

radhe.execute("show databases")

# To check for database cricket_scorecard_management
check_database = radhe.fetchall()
for x in check_database :
    if (x[0]).lower() == "cricket_scorecard_management":
        t = 1

# To create database if not exist
if t != 1:
    radhe.execute("create database cricket_scorecard_management")
    print("New database for this program is been created\n")

radhe.execute("use cricket_scorecard_management")
radhe.execute("show tables")

check_tables = radhe.fetchall()
if check_tables == []:
    done = 0
else:
    done = len(check_tables)

# Choice to play or to have look on previous gameplay
if done != 0:
    print("If you want to play the game , write 'Play' &")
    play_or_print = (input("If you want to see previous records , write 'Show' : ")).lower()
    while True:
        if play_or_print in ["play","show"] :
            break
        else:
            print("Invaild input")
            play_or_print = (input("Enter only 'Play' or 'Show' : ")).lower()
else:
    play_or_print = "play"

if done == 0:
    done = 1
else:
    done //= 4
    done += 1

# If player chooses to play
if play_or_print == "play":
    print("\nIf you want to play with IPL teams , write 'IPL' , &") # Choice for team 
    custom_or_IPL=(input("If you want to create your own team , write 'create' : ")).upper()

    while True:
        if custom_or_IPL not in ["CREATE","IPL"] :
            print("Invailid Input")
            custom_or_IPL=(input("Enter only 'Create' or 'IPL' : " )).upper()
        else:
            break

    if (custom_or_IPL=="CREATE"):
        while True:
            myteamname=(input("\nEnter name of your team : ")).title()
            if nothing(myteamname):
                print("Please write something")
            else:
                break
        while True:
            opponentteamname=(input("\nEnter name of opponents team : ")).title()
            if opponentteamname in myteamname :
                print("Please try another name because you already taken this name for your team")
                print("Please write something except",myteamname)
            elif nothing(opponentteamname) :
                print("Please write something")
            else:
                break

        print("\n🙏Please🙏 press enter in place of ',' to seperate the names of different players")
        print("\nEnter name of players of your team")
        for players in range(0,11):
            while True:
                b=input("👉 ")
                if b in myteam:
                    print("Please write another name. This name is already taken by you.")
                elif nothing(b):
                    print("Please write something")
                else:
                    myteam.append(b)
                    break

        total.extend(myteam)
        print("\nEnter name of players of opponents team")
        for players in range(0,11):
            while True:
                c=input("🤜 ")
                if c in total:
                    print("Please write another name. This name is already taken by you.")
                elif nothing(c):
                    print("Please write something")
                else:
                    opponentteam.append(c)
                    total.append(c)
                    break

    elif(custom_or_IPL=="IPL"):
        print("\nPlease select your team from below choices :\n1.Chennai Super Kings (CSK)\n2.Delhi Capitals (DC)")
        print("3.Kolkata Knight Riders (KKR)\n4.Mumbai Indians (MI)\n5.Punjab Kings (PK)\n6.Rajasthan Royals (RR)")
        print("7.Royal Challengers Banglore (RCB)\n8.Sunrises Hydrabad (SRH)")
        while True:
            myteamname=(input("Enter your team name : ")).upper()
            if myteamname in ["1","CHENNAI SUPER KING","CSK"]:
                myteamname , myteam = "CSK" , CSK
            elif myteamname in ["2","DELHI CAPITALS","DC"]:
                myteamname , myteam = "DC" , DC
            elif myteamname in ["3","KOLKATA KNIGHT RIDERS","KKR"]:
                myteamname , myteam = "KKR" , KKR
            elif myteamname in ["4","MUMBAI INDIANS","MI"]:
                myteamname , myteam = "MI" , MI
            elif myteamname in ["5","PUNJAB KINGS","PK"]:
                myteamname , myteam = "PK"  , PK
            elif myteamname in ["6","RAJASTHAN ROYALS","RR"]:
                myteamname , myteam = "RR" , RR
            elif myteamname in ["7","ROYAL CHALLENGERS BANGLORE","RCB"]:
                myteamname , myteam = "RCB" , RCB
            elif myteamname in ["8","SUNRISES HYDRABAD","SRH"]:
                myteamname , myteam = "SRH" , SRH
            else:
                print("Invaild Input")
            
            if myteamname in teamnames:
                teamnames.remove(myteamname)
                print()
                break

        while True:
            opponentteamname=(input("Enter opponent's team name : ")).upper()
            if opponentteamname in ["1","CHENNAI SUPER KING","CSK"]:
                opponentteamname , opponentteam = "CSK" , CSK
            elif opponentteamname in ["2","DELHI CAPITALS","DC"]:
                opponentteamname , opponentteam = "DC" , DC
            elif opponentteamname in ["3","KOLKATA KNIGHT RIDERS","KKR"]:
                opponentteamname , opponentteam = "KKR" ,KKR
            elif opponentteamname in ["4","MUMBAI INDIANS","MI"]:
                opponentteamname , opponentteam = "MI" ,MI
            elif opponentteamname in ["5","PUNJAB KINGS","PK"]:
                opponentteamname , opponentteam = "PK" , PK
            elif opponentteamname in ["6","RAJASTHAN ROYALS","RR"]:
                opponentteamname , opponentteam = "RR" , RR
            elif opponentteamname in ["7","ROYAL CHALLENGERS BANGLORE","RCB"]:
                opponentteamname , opponentteam = "RCB" , RCB
            elif opponentteamname in ["8","SUNRISES HYDRABAD","SRH"]:
                opponentteamname , opponentteam = "SRH" , SRH
            else:
                print("Invaild Input")
            
            if opponentteamname in teamnames:
                break

    print("\nPlayers of",myteamname,"are : ")
    for x in myteam:
        if x==myteam[-1]:
            print(x)
        else:
            print(x,end=" , ")
    print()
    print("\nPlayers of",opponentteamname,"are : ")
    for x in opponentteam:
        if x==opponentteam[-1]:
            print(x)
        else:
            print(x,end=" , ")
    print()

    while True:
        Toss=(input("\nEnter your choice [Head or Tail] : ")).title()
        if Toss not in ["Head","Tail"]:
            print("Invailid Input")
        else:
            break

    toss=random.choice(["Head","Tail"])
    if(toss==Toss):
        print("🎉Hurray🎉, You won the toss")
        while True:
            choice1 = (input("\nEnter your choice [Bating or Bowling] : ")).title()
            if choice1 not in ["Bating","Bowling"]:
                print("Invailid Input")
            else:
                break
    else:
        print(opponentteamname,"won the toss")
        choice2=random.choice(["Bating","Bowling"])
        print(opponentteamname,"choose to",choice2)

    if choice1 == "Bating":
        choice2 = "Bowling"
    elif choice1 == "Bowling":
        choice2 = "Bating"
    elif choice2 == "Bating":
        choice1 = "Bowling"
    else :
        choice1 = "Bating"

    while True:
        overs=input("\nEnter no. of overs you want to play : ")
        if number_checker(overs):
            overs = int(overs)
            break
        else:
            print("Invailid Input")
    
    # To create tables for both innings
    radhe.execute("create table match{0}_inning1_bat (Batsman varchar(30) , Balls int(5) , 6s int(5) , 4s int(5) , Total_Runs int(5))".format(done))
    radhe.execute("create table match{0}_inning2_bat (Batsman varchar(30) , Balls int(5) , 6s int(5) , 4s int(5) , Total_Runs int(5))".format(done))
    radhe.execute("create table match{0}_inning1_bowl (Bowler varchar(30) , Overs int(5) , Wictkets int(5) , Total_Runs int(5))".format(done))
    radhe.execute("create table match{0}_inning2_bowl (Bowler varchar(30) , Overs int(5) , Wictkets int(5) , Total_Runs int(5))".format(done))

    if choice1 == "Bating":
        target , Bat1 , Bowl1 = bating(overs,1)
        ok , Bat2 , Bowl2 = bowling(overs,2,target)
    else:
        target , Bat1 , Bowl1 = bowling(overs,1)
        ok , Bat2 , Bowl2 = bating(overs,2,target)
    
    # To insert match details into mysql table
    for x in Bat1: 
        ball = Bat1[x]["Ball"]
        Six = Bat1[x]["6s"]
        Four = Bat1[x]["4s"]
        Run = Bat1[x]["Total"]

        radhe.execute("insert into match{0}_inning1_bat values('{1}',{2},{3},{4},{5})".format(done,x,ball,Six,Four,Run))
        connector.commit()
    
    for x in Bat2:
        ball = Bat2[x]["Ball"]
        Six = Bat2[x]["6s"]
        Four = Bat2[x]["4s"]
        Run = Bat2[x]["Total"]

        radhe.execute("insert into match{0}_inning2_bat values('{1}',{2},{3},{4},{5})".format(done,x,ball,Six,Four,Run))
        connector.commit()
    
    for x in Bowl1:
        ball = Bowl1[x]["Overs"]
        Wicket = Bowl1[x]["Wickets"]
        Run = Bowl1[x]["Total"]

        radhe.execute("insert into match{0}_inning1_bowl values('{1}',{2},{3},{4})".format(done,x,ball,Wicket,Run))
        connector.commit()

    for x in Bowl2:
        ball = Bowl2[x]["Overs"]
        Wicket = Bowl2[x]["Wickets"]
        Run = Bowl2[x]["Total"]

        radhe.execute("insert into match{0}_inning2_bowl values('{1}',{2},{3},{4})".format(done,x,ball,Wicket,Run))
        connector.commit()

else: # To have a look on previous matches
    while True:
        print("\nTotal no. of matches played are {}".format(done-1))
        print("To watch match details , Enter")
        Match = input("\nMatch no. : ")
        if number_checker(Match) and int(Match) < done :
            Match = int(Match)
            break
        else:
            print("Invailid Input")
    
    design("-")
    print("Inning 1st :-\n")
    print("Highlights of Batsmen\n")
    
    radhe.execute("select * from match{}_inning1_bat".format(Match))
    detail = radhe.fetchall()

    table(["Batsman","Balls","6s","4s","Total Runs"],detail)
    
    print("\nHighlights of Bowlers\n")

    radhe.execute("select * from match{0}_inning1_bowl".format(Match))
    detail = radhe.fetchall()

    table(["Bowler","Overs","Wickets","Total Runs"],detail)
    
    design("-")

    design("-")
    print("Inning 2nd :-\n")
    print("Highlights of Batsman\n")
    
    radhe.execute("select * from match{}_inning2_bat".format(Match))
    detail = radhe.fetchall()

    table(["Batsman","Balls","6s","4s","Total Runs"],detail)
    
    print("\nHighlights of Bowlers\n")

    radhe.execute("select * from match{0}_inning2_bowl".format(Match))
    detail = radhe.fetchall()

    table(["Bowler","Overs","Wickets","Total Runs"],detail)

    design("-")

# To permanently save records on mysql tables 
connector.commit()
# To close connection between mysql and python
connector.close()
