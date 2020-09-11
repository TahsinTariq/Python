def readfile(path):
    var = []
    try: os.system(f'py "{path}\\priorityQ.py"')
    except: pass
    with open(f"{path}\\grid.txt", 'r') as f:
        for line in f:
            v = line.split()
            var.append([])
            for value in v:
                if value == "0":
                    var[-1].append(0)
                else: var[-1].append(value)
    return var