# 1. Add Task
# 2. Delete Task
# 3. View Task
# 4. Mark Done
# 5. Exit

print('Welcome to the TO-Do list')

options = [
    'Add Task',
    'Delete Task',
    'View Task',
    'Mark Done',
    'Exit',    
]

print('These are your options,\n', 
'Add Task\n',
'Delete Task\n',
'View Task\n',
'Mark Done\n',
'Exit'
)

choice = input('Enter your choice: ')
tsk = ''
if choice == 'Add Task':
    tasks = input('Enter your tasks: ')
    tsk += tasks
print(tsk)