import time
import threading

def timeset():
              global timelimit
              timelimit=60
              question=0
              for i in range(60):
               timelimit-=1
               time.sleep(1)
count_thread=threading.Thread(target= timeset)
count_thread.start()
try:
                while timelimit>0: 
                                  list1=[]
                                  list2=[]
                                  total_questions=0
                                  count_correct_answer=0
                                  count_wrong_answer=0
                                  options=['a','b','c','d']
                                  print("Welcome to the Quiz ... !!! >>>>")
                                  print("--------------------------------")
                                  name=input("Enter your name : ").capitalize()
                                  print("\t")
                                  print(f'Start the quiz!!!!    {name}')
                                  print("\t")
                                  print("Instructions . . . are here >>> .Just check it >....>")
                                  print("...................................")
                                  print("1.The quiz will be in 60 seconds duration ")
                                  print("2.You can attempt the quiz only once.")
                                  print("3.There are total 5 questions.")
                                  print("4.Each question carries 20 mark. No negative marking for wrong answers.")
                                  print("5.Questions are of Multiple Choice.(a,b,c,d) choices are availabe for marking your answer. ")
                                  print("6.Read the questions correctly and marked the answer from the given choices(a,b,c,d) only.")
                                  print("\t")
                                  print(f'you have {timelimit} seconds to complete the quiz !!!! Try to finish with in the timelimit :>>> ')
                                  print(".......................................................................................................")
                                  print("Questions are here... >>>> ")
                                  print("------------------------------------------------")
                                  print(" 1. Which city is called Pearl City ?")
                                  print("---------------------------------------------")
                                  print("a.Mumbai")
                                  print("b.Kochi")
                                  print("c.Hyderbad")
                                  print("d.Chennai")
                                  answer1=None
                                  while answer1  not in options:
                                          answer1=input("Enter your choice (a,b,c,d):  ").lower()
                                  print("\t")
                                  if answer1=='c':
                                              print("Correct >>>") 
                                              list1.append(answer1)
                                  elif answer1=='a' or answer1=='b' or answer1=='c' or answer1=='d':
                                              print("Incorrect !!!")
                                              list2.append(answer1)
                                  else:
                                              print("Invalid Choice !!! Please enter correct Choice ::>>")
                                              print("Written the choice as Incorrect ! ! ! Please make sure correct choices are marked ::>>")

                                  total_questions+=1
                                  print("---------------------------------------------")
                                  print(f'{timelimit} seconds balanced ::>>')
                                  print(".........................................")
                                  time.sleep(1)
                                  if timelimit==0:
                                        print("Quiz end !! Time Out..")
                                        print(f'You attended {total_questions} questions . . . ! ! !  {5-total_questions} questions are not viewed !!!!')
                                        break
                                  print("\t")
                                  print("2. How many players are there in the cricket team?")
                                  print("---------------------------------------------")
                                  print("a.11")
                                  print("b.10")
                                  print("c.9")
                                  print("d.12")
                                  answer2=None
                                  while answer2  not in options:
                                            answer2=input("Enter your choice(a,b,c,d):  ").lower()
                                  print("\t")
                                  if answer2=='a':
                                         print("Correct >>>") 
                                         list1.append(answer2)
                                  elif answer2=='a' or answer2=='b' or answer2=='c' or answer2=='d':
                                         print("Incorrect !!!")
                                         list2.append(answer2)
                                  else:
                                          print("Invalid Choice !!! Please enter correct Choice ::>>")
                                          print("Written the choice as Incorrect ! ! ! Please make sure correct choices are marked ::>>")
                                  print("---------------------------------------------")
                                  total_questions+=1
                                  print(f'{timelimit} seconds balanced ::>>')
                                  print("...........................................")
                                  time.sleep(1)
                                  if timelimit==0:
                                         print("Quiz end !! Time Out..")
                                         print(f'You attended {total_questions} questions . . . ! ! !  {5-total_questions} questions are not viewed !!!!')
                                         break
                                  print("\t")
                                  print("3.Which planet is the smallest ?")
                                  print("---------------------------------------------")
                                  print("a.Neptune")
                                  print("b.Mars")
                                  print("c.Mercury")
                                  print("d.Jupiter")
                                  answer3=None
                                  while answer3  not in options:
                                              answer3=input("Enter your choice(a,b,c,d) : ").lower()
                                  print("\t")
                                  if answer3=='c':
                                          print("Correct >>>") 
                                          list1.append(answer3)
                                  elif answer3=='a' or answer3=='b' or answer3=='c' or answer3=='d':
                                           print("Incorrect !!!")
                                           list2.append(answer3)
                                  else:
                                          print("Invalid Choice !!! Please enter correct Choice ::>>")
                                          print("Written the choice as Incorrect ! ! ! Please make sure correct choices are marked ::>>")
                                  print("---------------------------------------------")
                                  total_questions+=1
                                  print(f'you have {timelimit} seconds to complete the quiz !!!! Try to finish with in the timelimit :>>> ')
                                  print("............................................................................")
                                  time.sleep(1)
                                  if timelimit==0:
                                          print("Quiz end !! Time Out..")
                                          print(f'You attended {total_questions} questions . . . ! ! !  {5-total_questions} questions are not viewed !!!!')
                                          break
                                  print("\t")
                                  print("4.What is the only animal that can’t jump ?")
                                  print("---------------------------------------------")
                                  print("a.Tiger")
                                  print("b.Elephant")
                                  print("c.Giraffe")
                                  print("d.Camel")
                                  answer4=None
                                  while answer4  not in options:
                                             answer4=input("Enter your choice(a,b,c,d):  ").lower()
                                  print("\t")
                                  if answer4=='b':
                                         print("Correct >>>") 
                                         list1.append(answer4)
                                  elif answer4=='a' or answer4=='b' or answer4=='c' or answer4=='d':
                                          print("Incorrect !!!")
                                          list2.append(answer4)
                                  else:
                                          print("Invalid Choice !!! Please enter correct Choice ::>>")
                                          print("Written the choice as Incorrect ! ! ! Please make sure correct choices are marked ::>>")
                                  total_questions+=1
                                  print("---------------------------------------------")
                                  print(f'you have only {timelimit} seconds to complete the quiz !!!! :>>> ')
                                  print("..........................................................")
                                  time.sleep(1)
                                  if timelimit==0:
                                         print("Quiz end !! Time Out..")
                                         print(f'You attended {total_questions} questions . . . ! ! !  {5-total_questions} questions are not viewed !!!! ')
                                         break
                                  print("\t")
                                  print("5.Which bird is the symbol of peace ?")
                                  print("---------------------------------------------")
                                  print("a.Swans")
                                  print("b.Parrot")
                                  print("c.Peacock")
                                  print("d.Dove")
                                  answer5=None
                                  while answer5  not in options:
                                             answer5=input("Enter your choice(a,b,c,d):  ").lower()
                                  print("\t")
                                  if answer5=='d':
                                           print("Correct >>>") 
                                           list1.append(answer5)
                                  elif answer5=='a' or answer5=='b' or answer5=='c' or answer5=='d':
                                            print("Incorrect !!!")
                                            list2.append(answer5)
                                  else:
                                            print("Invalid Choice !!! Please enter correct Choice ::>>")
                                            print("Written the choice as Incorrect ! ! ! Please make sure correct choices are marked ::>>")
        
                                  total_questions+=1
                                  print(f'you have {timelimit} seconds balanced !!! Compeleted the quiz with in the timelimit >>> Wait for the result ::>>')
                                  print("......................................................................................................")
                                  print("\t")
                                  if total_questions==5:
                                                print("Questions are over >>>>> ")
                                                break
                                  time.sleep(1)
                                  if timelimit==0:
                                            print("Quiz end !! Time Out..")
                                            print(f'You attended {total_questions} questions . . . ! ! !  {5-total_questions} questions are not viewed !!!!')
                                            break

                print("\t")
                print("<<<<<....RESULT....>>>>>")
                print("<===================>")
                if len(list1)==5:
                        print(f'Congratulation.... all answers are correct >>> {name} got score 100/100 ')
                elif len(list2)==5:
                        print(f'Sorry..... Try again>>> All answers are wrong >>> {name} got score 0/100')
                else: 
                        for i in list1:
                            count_correct_answer+=1
                        for i in list2:
                            count_wrong_answer+=1
                        score=count_correct_answer*20
                        print(f'{count_correct_answer} Correct answer out of 5 questions')
                        print(f'{name} got the Score : {score}/100 ')
except TypeError:
      print("Invalid Choice !!! Please enter correct Choice  in (a,b,c,d) ::>>")
      print("Written the choice as Incorrect ! ! ! Please make sure correct choices are marked ::>>")
except:
      print("Something went wrong ! ! ! An exception is occured . . . ")
finally:
      print("Nothing went wrong ! ! ! 'try except' is  finished . . . . ")
                                                       
                



