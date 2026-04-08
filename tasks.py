TASKS = [
    # -------- BASIC --------
    {"input": {"raw_data": "name=john", "task_type": "format"}, "output": 
"Name: John"},
    {"input": {"raw_data": "name=alice", "task_type": "format"}, "output": 
"Name: Alice"},

    # -------- NORMALIZATION --------
    {"input": {"raw_data": "name=john||age=25", "task_type": "normalize"}, 
"output": "Name: John, Age: 25"},
    {"input": {"raw_data": "name=MIKE||age=30", "task_type": "normalize"}, 
"output": "Name: Mike, Age: 30"},

    # -------- CITY --------
    {"input": {"raw_data": "name=john||city=chennai", "task_type": 
"normalize"}, "output": "Name: John, City: Chennai"},
    {"input": {"raw_data": "name=sara||city=mumbai", "task_type": 
"normalize"}, "output": "Name: Sara, City: Mumbai"},

    # -------- EMAIL --------
    {"input": {"raw_data": "email=TEST@GMAIL.COM", "task_type": 
"normalize"}, "output": "Email: test@gmail.com"},
    {"input": {"raw_data": "name=alex||email=ALEX@YAHOO.COM", "task_type": 
"normalize"}, "output": "Name: Alex, Email: alex@yahoo.com"},

    # -------- COUNTRY --------
    {"input": {"raw_data": "name=john||country=india", "task_type": 
"normalize"}, "output": "Name: John, Country: INDIA"},

    # -------- MIXED --------
    {
        "input": {"raw_data": "name=joHN||age=25||city=chenNAI", 
"task_type": "deduplicate"},
        "output": "Name: John, Age: 25, City: Chennai"
    },
    {
        "input": {"raw_data": 
"name=sara||age=19||city=delhi||email=SARA@MAIL.COM", "task_type": 
"deduplicate"},
        "output": "Name: Sara, Age: 19, City: Delhi, Email: sara@mail.com"
    },

    # -------- HARD CASES --------
    {
        "input": {"raw_data": "name=  john  || age= 25 || city= chennai ", 
"task_type": "normalize"},
        "output": "Name: John, Age: 25, City: Chennai"
    },
    {
        "input": {"raw_data": "NAME=JOHN||CITY=CHENNAI||COUNTRY=india", 
"task_type": "normalize"},
        "output": "Name: John, City: Chennai, Country: INDIA"
    },

    # -------- NOISE --------
    {
        "input": {"raw_data": "name=john@@@||age=25###", "task_type": 
"normalize"},
        "output": "Name: John, Age: 25"
    },

    # -------- EDGE --------
    {
        "input": {"raw_data": "", "task_type": "normalize"},
        "output": ""
    },
]
