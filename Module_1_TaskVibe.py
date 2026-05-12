#!/usr/bin/env python3

class Task:   #individual task class
    def __init__(self):
	    self.task_name = "name"
	    self.task_description ="description"
	    self.task_status = "Incomplete"

class TaskTracker:  #indi
    def __init__(self):
	    self.list_date = "January 1, 2020"
        self.task_item = []		
       	   

    def add_task(self, Task):
	
	def mark_as_compete(self,name):
	
	def remove_task(self, name):
	
	def view_tasks(self):


def print_menu(task): #function to create the menu
    menu = (
        "\nMENU\n"
        "a - Add new Task\n"
        "d - Delete Task\n"
        "c - Complete Task\n"
        "v - View list of tasks\n"
        "q - Exit\n"
    )
	
    menuChoice = ""
	while menuChoice != "q":
	    print(menu)
	    menuChoice = input("Choose an option:\n).lower()
	    if menuChoice = "a":
	    elif menuChoice = "d":
	    elif menuChoice = "c":
	    elif menuChoice = "v":
	   
	    elif menuChoice = "q":
	        print("Thank you four using TaskVibe, Good By")
		    break
	   
	    else: 
	        print("Invalid option. Please try again.\n"
	       