import time
import threading
def timeset():
        global timelimit
        timelimit=50
        question=0
        for i in range(50):
               timelimit-=1
               time.sleep(1)
count_thread=threading.Thread(target= timeset)
count_thread.start()
try:
    print("Welcome to the Quiz !!! ... !!! >>>")
    print("------------------------------------")
    print("\t")
    name=input("Enter your name :  ").capitalize()
    print("\t")
    print(f'Start the quiz !!!! {name}')
    print("\t")
    print("Instructions . . . are here >>> .Just check it >....>")
    print("...................................")
    print("1.The quiz will be in 50 seconds duration. ")
    print("2.You can attempt the quiz only once.")
    print("3.There are total 5 questions.")
    print("4.Each question carries 20 mark. No negative marking for wrong answers.")
    print("5.Questions are of Multiple Choice.(a,b,c,d) choices are availabe for marking your answer. ")
    print("6.Read the questions correctly and marked the answer from the given choices(a,b,c,d) only.")
    print("\t")
    while timelimit>0:
        print(f'You have {timelimit} seconds to complete the quiz !!!! Try to finish with in the timelimit :>>> ')
        print(".......................................................................................................")
        print("Questions are here.... >>>>")
        
        questions=("1.Which city is called Pearl City? :",
                  "2.How many players are there in the cricket team ?:",
                  "3.Which planet is the smallest? :",
                  "4. What is the only animal that can’t jump? :",
                  "5.Which bird is the symbol of peace? :")
        choices=[('a.Mumbai','b.Kochi','c.Hyderabad','d.Chennai'),
                 ('a.11','b.12','c.9','d.10'),
                 ('a.Mars','b.Neptune','c.Mercury','d.Jupiter'),
                 ('a.Tiger','b.Elephant','c.Giraffe','d.Camel'),
                 ('a.Swans','b.Parrot','c.Peacock','d.Dove')]
        answers=['c','a','c','b','d']
        options=['a','b','c','d']
        
        user_choices=[]
        score=0
        total_question_no=0
        count_correct_answer=0
        count_incorrect_answer=0
        #while total_question_no>0:
        for question in questions:
            print("--------------------------------------------")
            print(question)
            print("--------------------------------------------")
            for choice in choices[total_question_no]:
                print(choice)
            user_input_choice=input("Enter your Choice (a,b,c,d) :  ").lower()
            time.sleep(1)
            user_choices.append(user_input_choice)
            #print(user_choices)
            
            if user_choices[total_question_no] == answers[total_question_no]:
                count_correct_answer+=1
                score+=1
                print("\t")
                print("Correct >>>")
            elif user_choices[total_question_no]=='a' or user_choices[total_question_no]=='b' or user_choices[total_question_no]=='c' or user_choices[total_question_no]=='d':
                print("\t")
                print("Incorrect !!!")
            else:
                print("\t")
                print("Invalid Choice !!! Please enter correct Choice ::>>")
                print("Written the choice as Incorrect ! ! ! Please make sure correct choices are marked ::>>")
            print("\t") 
            total_question_no+=1
            print(f'you have {timelimit} seconds balanced  !!!! :>>> ')
            print("\t")
            time.sleep(1)
            if timelimit==0:
                print("Quiz is Over !!! Time up...  ")
                print(f'You attended {total_question_no} questions . . . ! ! !  {5-total_question_no} questions are not viewed !!!!')
                break
                
            if total_question_no==5:
                print("Questions are Over .. ! ! !")
                print("...............................")
                print(f' Compeleted the quiz with in the timelimit >>> Wait for the result ::>>')
                
                break
        print("\t")
  
        print("<<<<<.....RESULTS....>>>>>")
        print("\t")
        print("Correct Answers are..!!! ",end="  ")
        for answer in answers:
            print(answer,end="  ")
        print("\t")
        print("Your Choices are ...!!!",end="  ")
        for user_input in user_choices:
            print(user_input,end="  ")
        print("\t")
        print(f'{name} got {count_correct_answer} correct answer out of 5 questions.')
        print(f'You got the Score : {(score/len(questions)*100)}/100 . . . . ! ! !')
        break
except TypeError:
      print("Invalid Choice !!! Please enter correct Choice  in (a,b,c,d) ::>>")
      print("Written the choice as Incorrect ! ! ! Please make sure correct choices are marked ::>>")
except:
     print("Something went wrong ! ! ! An exception is occured . . . ")
finally:
     print("Nothing went wrong ! ! ! 'try except' is  finished . . . . ")

       



