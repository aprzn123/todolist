"""
Manages data about tasks
"""

from datetime import date
import project

class TaskError(Exception):
    pass

class Task(object):
    name = ""
    project = project.Project("")
    def __init__(self, name, project, **kwargs): # kwargs: due=date
        self.name = name
        self.project = project
        for key, value in kwargs:
            if key == "due" and isinstance(value, date):
                self.due_date = date
            else:
                raise TaskError("Either keyword " + key + " is not a valid keyword or " + str(value) + " is not a valid value.")