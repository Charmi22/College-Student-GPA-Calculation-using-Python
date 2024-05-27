""" 
        Group-8
Maaz Jinwala : N01531110
Praveen Nallu : N01510745
Teja Varma Yeggadi : N01530436

"""
# import statement 
from ClassFile import Humber_college 

Student=[] # created the list to store the objects 

# main function The program execution starts from here  
def  BIA():
    print("---------------------------- Welcome in Humber College ----------------------------")
    Humber=Humber_college() # creating rhe object to check the authantication 
    # if condition which call the method and check the password is correcct or not 
    if (Humber.authantication()):
        counter=0
        
        # while loop to coun the wrong attemps of user 
        while  counter<3:
            Total_Students=int(input("Enter How many Students of data u want to enter(1-50) : "))
            #if statement to check conditon that number is between 1-50 or not 
            if(Total_Students>0 and Total_Students<=50):

                # taking all the student's detail 
                for i in range (0,Total_Students):
                    print("--------------------Please Enter ",i+1," Student details--------------------")
                    name=input("Please enter student name :")
                    print("\n")
                    math=int(input("Please enter student's Math grade :"))
                    science=int(input("Please enter student's Science grade :"))
                    language=int(input("Please enter student's Language grade :"))
                    drama=int(input("Please enter student's Drama grade :"))
                    music=int(input("Please enter student's Music grade :"))
                    biology=int(input("Please enter student's Biology grade :"))
                    print("\n\n")
                    Student.append(Humber_college(name,math,science,language,drama,music,biology)) # statement which append the object in the list 
                
                # for loop for calling the calculation method for all  objeccts which is i the list 
                for i  in range(len(Student)):
                    Student[i].GPA_Calculation()
                
                #statement to call the dispay_report() methos which display all the reports 
                Student[0].display_reports() 
                break
            else:
                counter +=1
                   
    else:
        print("Thank you so much !!")        
    

# calling the main method in the beginning of the execution 
BIA()