from lib.tasks import *
import pytest

### Tests for Task class ###

## Tests for __init__ 

"""Test the initial creation of the Task object. Tasks should be
initialised to empty dict"""
def test_tasks_class_init():
    task = Task()
    assert task.tasks == {}



## Tests for .add_task()

"""Test for adding a task is correct"""
def test_add_task():
    task = Task()
    task.add_task("Write essay", "Complete essay for history project on Vietnam War")
    assert task.tasks == {"Write essay": "Complete essay for history project on Vietnam War"}

"""Test adding another differnt task"""
def test_add_task2():
    task = Task()
    task.add_task("read book", "Finish reading book art of war by Tsing Tao")
    assert task.tasks == {"read book": "Finish reading book art of war by Tsing Tao"}

"""Test adding muliple tasks to dictionary"""
def test_add_task_multiple_tasks_added_at_once():
    task = Task()
    task.add_task("Write essay", "Complete essay for history project on Vietnam War")
    task.add_task("read book", "Finish reading book art of war by Tsing Tao")
    task.add_task("Holiday", "Go on ski holiday in the alps in February")
    assert len(task.tasks) == 3

"""Test error is thrown if title or description is nothing"""
def test_add_task_title_or_decription_is_nothing():
    task = Task()
    with pytest.raises(Exception) as e:
        task.add_task('', '')
    assert str(e.value) == "Title or description can't be empty"



## Tests for .completed()

"""Test adding task to dict and then removing it and seeing
if dict is empty"""
def test_completed_removes_1_item_and_dict_is_empty():
    task = Task()
    task.add_task("Write essay", "Complete essay for history project on Vietnam War")
    task.completed("Write essay")
    assert task.tasks == {}

def test_completed_removes_1_item_and_multi_task_dict_only_one_removed():
    task = Task()
    task.add_task("Write essay", "Complete essay for history project on Vietnam War")
    task.add_task("read book", "Finish reading book art of war by Tsing Tao")
    task.add_task("Holiday", "Go on ski holiday in the alps in February")
    task.completed("Write essay")
    assert len(task.tasks) == 2

"""Test removing a task that doesn't exist. No error should be thrown
it should just do nothing"""
def test_completed_does_nothing_if_task_title_doesnt_exist():
    task = Task()
    task.add_task("Write essay", "Complete essay for history project on Vietnam War")
    task.completed('Read book')
    assert task.tasks == {"Write essay": "Complete essay for history project on Vietnam War"}



## Tests for .list_tasks()

"""Test when one task is added then the output is that one thing
formatted as a string {title: descrition}"""
def test_list_tasks_one_task_added():
    task = Task()
    task.add_task("Write essay", "Complete essay for history project on Vietnam War")
    result = task.list_tasks()
    assert result == "Write essay: Complete essay for history project on Vietnam War"

"""Test when muliple tasks have been added then list_tasks lists them
all formatted in a newline"""
def test_list_tasks_multiple_tasks_have_been_added():
    task = Task()
    task.add_task("Write essay", "Complete essay for history project on Vietnam War")
    task.add_task("read book", "Finish reading book art of war by Tsing Tao")
    task.add_task("Holiday", "Go on ski holiday in the alps in February")
    result = task.list_tasks()
    expected = "Write essay: Complete essay for history project on Vietnam War\nread book: Finish reading book art of war by Tsing Tao\nHoliday: Go on ski holiday in the alps in February"
    assert result == expected

"""Test to call .list_tasks() when no tasks have been added should show
a message telling the user that no tasks have been added"""
def test_list_tasks_when_no_tasks_have_been_added():
    task = Task()
    assert task.list_tasks() == 'No tasks have been added yet.'