# dictionaries function just like objects in JavaScript representing key-value pairs

ages = {"Christian": 22, "Eder": 25, "James": 23}

ages["Christian"] = 23
ages["James"] += 2
ages["Random"] = 30  # this will be added to the dictionary

ages["hello"] = set()

ages["hello"].add(1)
ages["hello"].add(2)
ages["hello"].add(1)

print(ages)

print(ages.get("Christi"))
