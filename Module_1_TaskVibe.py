#!/usr/bin/env python3

class Task:   #individual task class
    def __init__(self):  #constructor for the individual task, creates a new task object
	    self.task_name = "name"
	    self.task_description ="description"
	    self.task_status = "Incomplete"

class TaskTracker:   #task list class 
    def __init__(self): #constructor for the list of tasks, create a new task list object 
	    self.task_list_name = "name"
        self.list_date = "January 1, 2020"
        self.task_item = []		
       	   

    def add_task(self, Task): #adds a new task only 
        self.task_item.append(Task)
	
	def mark_as_compete(self,name): #Changes status of task from incomplete to competed
	
	def remove_task(self, name): #Deletes a task 
        for item in self.task_item
            if item.task_name == name:
                self.task_item.remove(item)
	
	def view_tasks(self,date): #views all daily tasks 
        date_task_list =[]
        for item in self.task_item
           if item.task_date = date:
               date_task_list.append(item)
        
        for item in date_task_list
            print(item)        


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
	       