class Task:
    def __init__(self):
        """
        A dictionary to keep track of the tasks.
        Each task will have a title which will be the key
        for the dict and a decription which will be the value
        of the dict
        """
        self.tasks = {}


    def add_task(self, title, description):
        """
        Adds a new task to the dictionary
        Params:
            title of the task - str
            description of the task - str
        Returns:
            None
        Side effects:
            prints nothing and returns nothing
        """
        title, description = str(title), str(description)
        if title.strip() == '' or description.strip() == '':
            raise Exception("Title or description can't be empty")
        
        self.tasks[title] = description


    def completed(self, title):
        """
        Marks a task as completed i.e. removes it from the
        dictionary of tasks
        Params:
            title of the task - str
        Returns:
            None
        Side effects:
            returns nothing and prints nothing
        """
        if title in self.tasks:
            del self.tasks[title]


    def list_tasks(self):
        """
        Lists out the tasks so the user can view what needs
        to still be completed
        Params:
            None
        Returns:
            tasks that need to be completed - str
            this will be one string with each task separated
            by a newline
        Side effects:
            None
        """
        if not self.tasks:
            return 'No tasks have been added yet.'

        return '\n'.join([f"{key}: {value}" for key, value in self.tasks.items()])
    