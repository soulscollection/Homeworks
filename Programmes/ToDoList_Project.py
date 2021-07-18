print("--> SUPER TO-DO LIST <--")

tasks = []

while True:
    cmd = input("CMD -> ")
    if cmd == "add":
        task = input("TASK -> ")
        if task != "":
            tasks.append(task)
            print("Done!")
        else:
            print("What u want?")
    elif cmd == "remove":
        num = int(input("Remove -> "))
        tasks.pop(num - 1)
        print("Done!")
    elif cmd == "show":
        for i in tasks:
            print(f"-- {i}")
    elif cmd == "clear":
        tasks.clear()
        print("Done!")
    elif cmd == "exit":
        break
    elif cmd == "":
        print("Whaiting...")