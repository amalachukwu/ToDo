"""This is a system that allows users enter tasks.
View  task
Update status of task
delete task 
"""

lists = []

def main():
    
    print("Todo List")
    plans= input('Enter your plans for the day (seperate each by a comma): ')
    print(f'These are your plans for the day:\n{collect_task(plans)}')
    toremove= input('Enter completed plans:')
    print(f'These are your updated plans for the day:\n{delete_task(toremove)}')


def collect_task(plan):
    tasks = plan.split(',')
    for task in tasks:
        lists.append(task.strip())
    return lists
        

          
def delete_task(completed):
    
    if completed in lists:
        lists.remove(completed)
        print(f"\n{completed} has been removed from the list.")
    else:
        print('You can only romove existing plans')
    return lists


if __name__ == "__main__":
    main()



