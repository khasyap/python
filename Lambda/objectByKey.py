obj = {"a": 1, "b": 2, "c": 3, "d": 4}

keys = ["b", "c"]

result = {k: obj[k] for k in keys}

print(result)