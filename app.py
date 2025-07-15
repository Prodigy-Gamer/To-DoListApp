def showmenu():
  print('\n Welcome To The To-Do List App')
  print('1. View Tasks')
  print('2. Add Task')
  print('3. Mark Task Complete')
  print('4. Delete Task')
  print('5. Save & Exit')

tasks = [{"task": "Complete Homework", "completed": False}]

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
