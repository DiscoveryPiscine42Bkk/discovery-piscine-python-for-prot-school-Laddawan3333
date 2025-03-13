def greeting(name="noble stranger"):
    if not isinstance(name, str):
        print(f"Welcome, {name}!")
    else:
        print(f"Welcome, {name}!")
greeting()
greeting("John")
greeting(123)