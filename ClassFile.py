""" 
        Group-8
Maaz Jinwala : N01531110
Praveen Nallu : N01510745
Teja Varma Yeggadi : N01530436

"""

class Humber_college:

    # global dictionaries to store the data of student it will be same for all the object  
    Sch_Of_Eng={}
    Sch_Of_Bus={}
    Law_Sch={}
    Nt_Accpt={}
    
    # constructor with assign all the values in the variable 
    def __init__(self,name="nothing",Math=0,Science=0,Language=0,Drama=0,Music=0,Biology=0):    
        self.name=name
        self.math=Math
        self.science=Science
        self.language=Language
        self.drama=Drama
        self.music=Music
        self.biology=Biology
        self.counter=0
    
    # method to calculate GPA of Student 
    def GPA_Calculation(self):
        self.GPA=((self.math*4)+(self.science*5)+(self.language*4) +(self.drama*3 )+(self.music*2)+ (self.biology*4))/22
        if (self.GPA>=90 and self.GPA<=100):
            Humber_college.Sch_Of_Eng[self.name]="School of Engineering"
        elif(self.GPA<90 and self.GPA>=80):
            Humber_college.Sch_Of_Bus[self.name]="School of Business"
        elif(self.GPA>=70 and self.GPA<80):
            Humber_college.Law_Sch[self.name]="Law School"
        elif(self.GPA<70):
            Humber_college.Nt_Accpt[self.name]="not accepted"

    # function to check Password 
    def authantication(self):
        self.password=input("Please enter 10 digit password including (A-Z),(0-9)*2/3,(!@#$%^&*_) :")  # taking input from user
        digit_count =[1 for i in self.password if i.isdigit()]                                      # Extracting the digit from String
        special_char = [1 for i in self.password if not i.isdigit() and not i.isalpha()]            # checking special charectar from stringg
        upper_case =  [1 for i in self.password if i.isupper()]                                     # checking the upper letter from string 
        # checking every variable as per giver condition 
        if (len(self.password)>=10) and (len(upper_case)>=1) and (len(digit_count)==2 or len(digit_count)==3) and (len(special_char)==1):       
                
            print("password correct")
            return True
        else:
            # Condition For 3 Wrong attempts 
            if self.counter<2:
                self.counter +=1
                print("incorrect password")
                self.authantication()
            return False
    
    
   
    
    # function which display all the reports used for loop for iteration and Dictionary.get() method to fatch the data based on key 
    def display_reports(self):

        """
         printing Dictionaries to show in the PPT

        print("school of engineering",Humber_college.Sch_Of_Eng)
        print("school of business",Humber_college.Sch_Of_Bus)
        print("law school",Humber_college.Law_Sch)
        print("not accepted",Humber_college.Nt_Accpt) 
       
        """
        # printing of report 1
        print("\n\n-------------------------- Report 1 --------------------------")
        for i in Humber_college.Sch_Of_Eng:
            print(i,"--->", Humber_college.Sch_Of_Eng.get(i))
        for i in Humber_college.Sch_Of_Bus:
            print(i,"--->", Humber_college.Sch_Of_Bus.get(i))
        for i in Humber_college.Law_Sch:
            print(i,"--->", Humber_college.Law_Sch.get(i))
        
        # printing of report 2
        print("\n\n-------------------------- Report 2 --------------------------")
        print("Total Accepted student in Humber College : ",len(Humber_college.Sch_Of_Eng)+len(Humber_college.Sch_Of_Bus)+len(Humber_college.Law_Sch))
        print("\n\n----- Students of School of Engineering -----")
        for i in Humber_college.Sch_Of_Eng:
            print(i,"--->", Humber_college.Sch_Of_Eng.get(i))
        print("\nTotal Students in School of Engineering :",len(Humber_college.Sch_Of_Eng))

        print("\n\n----- Students of School of Business -----")
        for i in Humber_college.Sch_Of_Bus:
            print(i,"--->", Humber_college.Sch_Of_Bus.get(i))
        print("\nTotal Students in School of Business :",len(Humber_college.Sch_Of_Bus))
        
        print("\n\n----- Students of Law School -----")
        for i in Humber_college.Law_Sch:
            print(i,"--->", Humber_college.Law_Sch.get(i))
        print("\nTotal Students in Law School :",len(Humber_college.Law_Sch))

        # printing of report 3
        print("\n\n-------------------------- Report 3 --------------------------")

        print("\n\nNumber of  Not Accepted Students :",len(Humber_college.Nt_Accpt))

        for i in Humber_college.Nt_Accpt:
            print(i,"--->", Humber_college.Nt_Accpt.get(i))

        # printing of report 4            
        print("\n\n-------------------------- Report 4 --------------------------")
        self.total =len(Humber_college.Sch_Of_Eng)+len(Humber_college.Sch_Of_Bus)+len(Humber_college.Law_Sch)+len(Humber_college.Nt_Accpt)
        print("\n\nThe percentage of Students were accepted :",((len(Humber_college.Sch_Of_Eng)+len(Humber_college.Sch_Of_Bus)+len(Humber_college.Law_Sch))*100)/self.total,"%")

        
