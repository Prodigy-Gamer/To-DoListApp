def showmenu():
  print('\n Welcome To The To-Do List App')
  print('1. View Tasks')
  print('2. Add Task')
  print('3. Mark Task Complete')
  print('4. Delete Task')
  print('5. Save & Exit')

tasks = []

def view_tasks():
  if not tasks:
    print('No Tasks Yet!')
  for task in tasks:
    status = "✅" if task['completed'] else "❌"
    position = tasks.index(task) + 1
    name = task['task']
    print(f"{position}. {name} - [{status}]")

def add_task():
  task_name = input('Enter The Name of Your Task: ')
  tasks.append({'task': task_name, 'completed': False})
  print('your task has been added')

def mark_complete():
  view_tasks()
  num = int(input('Enter your task: ')) - 1
  tasks[num]['completed'] = True
  print('Task Has Been Completed')

def delete_task():
  view_tasks()
  num = int(input('Enter your task: ')) - 1
  removed_task = tasks.pop(num)    
  name = removed_task['task']
  print(name + 'has been removed')      

a = 2
while a < 3:
    showmenu()
    num = int(input('Enter What You Would Like To Do: '))
    if num == 1:
      view_tasks()
    if num == 2:
      add_task()
    if num == 3:
      mark_complete()
    if num == 4:
      delete_task()
    if num == 5:
      print('goodbye')
      break
    