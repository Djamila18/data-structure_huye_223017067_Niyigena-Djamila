from collections import deque

projects = [] 
undo_stack = []
pending_queue = deque()

def add_project(project):
        projects.append(project)
        undo_stack.append( project)
        print(f'Added project: {project}')

def remove_project(project):
    if project in projects:
            projects.remove(project)
            print(f'Removed project: {project}')
    else:
     print(f'Project not found: {project}') 

def undo():
    if undo_stack:
            action = undo_stack.pop()
            pending_queue.remove(action)
            print(f'Undid action: {action} of project')
    else:
            print('Nothing to undo')

def submit_project(projects):
    if projects in projects:
            pending_queue.append(projects)
            print(f'Submitted project: {projects}')
    else:
            print(f'Project not found for submission:')
def process_submission():
    if pending_queue:
            project = pending_queue.popleft() 
            print(f'Processed submission for: {project}')
    else:
        print('No pending submissions')

def show_projects():
    print("Current Projects {projects}")

def show_pending_submissions():
        print('Pending Submissions:', list(pending_queue))

# Example usage
add_project('Project 1')
add_project('Project 2')
show_projects()
remove_project('Project 1')
submit_project('Project 2')
undo()
submit_project(projects)
process_submission()
show_pending_submissions()


  


