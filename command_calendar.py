""" Basic Calendar: On this project user will be able to interact with from
the command line, the user should be able to choose to: 
. view the calendar 
. add event to the calendar 
. update an existing event 
. delete an existing event

The program should behave in the following way:
1. Print a welcome message to the user
2. Prompt the user to view, add, update, or delete an event on the calendar
3. Depending on the user's input: view, add, update, or delete an event on the calendar
4. The program should never terminate unless the user decides to exit

"""

from time import sleep, strftime 

user_first_name = "Yarli"

calendar = {}

def welcome():
  print ("Welcome {}, this is our first calendar!").format(user_first_name)
  print ("The Calendar is opening ...")
  sleep(1)
  print ("Today is: " + strftime("%A %B %d, %Y"))
  print ("The current time is: " + strftime("%H, %M, %S"))
  sleep(1)
  print ("What would you like to do?")


def start_calendar(): 
    welcome()
    start = True
    while start: 
      user_choice = input("A to Add, U to Update, V to View, D to Delete, X to Exit: ")
      user_choice.upper()
      if user_choice == "V":
        if len(calendar.keys()) < 1:
          print ("Calendar empty.")
        else:
          print (calendar)
      elif user_choice == "U":
        date = input("What date? ")
        update = input("Enter the update: ")
        calendar[date] = update
        print ("The calendar was successfuly updated!")
      elif user_choice == "A":
        event = input("Enter event: ")
        date = input("Enter date (DD/MM/YYYY): ")
        if (len(date) > 10 or int(date[6:]) < int(strftime("%Y"))):
          print ("The date is invalid!")
          try_again = input("Try Again? Y for Yes, N for No: ")
          if try_again == "Y":
            continue
          else:
            start = False 
        else:
          calendar[date] = event
          print ("Event was successfuly added!")
          print (calendar)
      elif user_choice == "D":
        
        if len(calendar.keys()) < 1:
          print ("calendar empty.")
        else:
          event = "What event? "
          for date in calendar.keys():
            if event == calendar[date]:
              del calendar[date]
              print ("Event was successfuly deleted!")
              print (calendar)
            else:
              print ("Incorrect event was especified!")
      elif user_choice == "X":
         start = False
      else:
         print ("Invalid command line!")
         start = False

start_calendar()












        






