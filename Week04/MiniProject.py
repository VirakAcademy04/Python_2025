import datetime

projects = {}

def add_project(name):
    if name in projects:
        print("This project already exist!")
        return 
    start_time = datetime.datetime.now()
    project_details = {
        "projct_start_time": start_time,
        "tasks": {}
    }
    projects[name] = project_details
    print(f"Project {name} Added!")


def ensure_project_exist(name):
    if name not in projects:
        print("Project not found!")
        return False 
    return True


def ensure_task_exist(project, name):
    if name not in projects[project]["tasks"]:
        print("Task not found!")
        return False 
    return True 


def add_task():
    project = input("Project name: ") 
    if not ensure_project_exist(project):
        return
    task_name = input("Task name: ")
    if task_name in projects[project]["tasks"]:
        print("Task exist!")
        return 
    desc = input("task description: ")
    start_time = datetime.datetime.now()
    data = {
        "description": desc,
        "start_time": start_time,
        "end_time": None,
        "duration": None,
        "done": False
    }
    projects[project]["tasks"][task_name] = data 
    print("Task Added!") 


def done():
    project = input("project name: ")
    if not ensure_project_exist(project):
        return 
    task = input("task name: ")
    if not ensure_task_exist(project, task):
        return
    end_str = input("End time(YYYY-MM-DD HH:MM): ")
    end_time = datetime.datetime.strptime(end_str, "%Y-%m-%d %H:%M")
    task_data = projects[project]["tasks"][task]
    if end_time < task_data["start_time"]:
        print("End time cannot be before start time.")
        return
    task_data["end_time"] = end_time
    task_data["duration"] = end_time - task_data["start_time"] 
    task_data["done"] = True 
    print("Task Done!")
    

def remove_task():
    project = input("project name: ")
    if not ensure_project_exist(project):
        return
    task = input("task name: ")
    if not ensure_task_exist(project, task):
        return
    del projects[project]["tasks"][task]
    print("Task removed!")


def edit_task():
    project = input("project name: ")
    if not ensure_project_exist(project):
        return
    task = input("task name: ")
    if not ensure_task_exist(project, task):
        return
    task_data = projects[project]["tasks"][task]
    new_title = input("enter new task title: ")
    if new_title in projects[project]["tasks"]:
        print("Task exist!")
        return 
    new_desc = input("enter new discription: ")
    task_data["description"] = new_desc
    projects[project]["tasks"].pop(task)
    projects[project]["tasks"][new_title] = task_data
    print("Task Updated!")


def show_project(name):
    project_info = projects[name]
    print(f"\nProject name: {name}")
    print(f"Start time: {project_info['projct_start_time'].strftime('%Y-%m-%d %H:%M')}")
    tasks = project_info["tasks"]
    if not tasks:
        print("Task not found!")
        return 
    for name, task_info in tasks.items():
        status = "Done" if task_info["done"] else "In process"
        print(f"-{name}: {task_info['description']} | {status}")


def search_project(project):
    if not ensure_project_exist(project):
        return
    show_project(project)  


def show_data():
    mode = input("Show 'all' projects or a single 'project': ")
    if mode == "all":
        for name in projects:
            show_project(name) 
    elif mode == "project":
        project = input("project name: ") 
        search_project(project)
    else:
        print("Invalid Input!")


def total():
    total_project = len(projects)
    total_duration = 0
    for p in projects.values():
        for t in p["tasks"].values():
            if t["done"]:
                total_duration += t["duration"].total_seconds()

    print(f"Total projects: {total_project}")
    hours = total_duration / 3600
    print(f"Total hours worjed: {hours}")


def project_summary(project):
    if not ensure_project_exist(project):
        return
    tasks = projects[project]["tasks"]
    done_tasks = []
    for t in tasks.values():
        if t["done"]:
            done_tasks.append(t)
    
    total_duration = 0
    for t in done_tasks:
        total_duration += t["duration"].total_seconds()
    
    print(f"Project name: {project}")
    print(f"Total Task: {len(tasks)}")
    print(f"Done tasks: {len(done_tasks)}")
    print(f"Worked Hours: {total_duration/3600:.2f}")


def help():
    print("\nProject and Task Manager Help:")
    print("-" * 50)
    print("add project     : Add a new project.")
    print("add task        : Add a task to an existing project.")
    print("remove          : Remove a task from a project.")
    print("done            : Mark a task as completed.")
    print("edit            : Edit the name and description of a task.")
    print("search          : Search and display a specific project.")
    print("display         : Show all tasks and projects or a specific project.")
    print("project summary : Show summary of a specific project.")
    print("total           : Show total summary of all projects and tasks.")
    print("exit            : Exit the program.")
    print("-" * 50)
    

while True:
    action = input("Select an option or 'help': ")
    if action == "add project":
        project_name = input("Enter your project name: ")
        add_project(project_name)

    elif action == "add task":
        add_task() 

    elif action == "done":
        done()

    elif action == "remove":
        remove_task()

    elif action == "edit":
        edit_task()

    elif action == "search":
        project_name = input("project name: ")
        search_project(project_name)

    elif action == "display":
        show_data() 

    elif action == "total":
        total() 

    elif action == "project summary":
        project = input("project name: ")
        project_summary(project)

    elif action == "help":
        help()
        
    elif action == "exit":
        break 
    elif action == "":
        continue
    else:
        print(f"{action}: Not Found!")