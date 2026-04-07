TASKS = [
    {
        "input": {"raw_data": "name: john", "task_type": "format"},
        "output": "Name: John"
    },
    {
        "input": {"raw_data": "name: john , age:25", "task_type": "normalize"},
        "output": "Name: John, Age: 25"
    },
    {
        "input": {"raw_data": "NAME=joHN||age= 25||CITY=chenNAI", "task_type": "deduplicate"},
        "output": "Name: John, Age: 25, City: Chennai"
    }
]