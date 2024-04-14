def reorderLogFiles1(self, logs: List[str]) -> List[str]:
    log = []
    let = []

    for i in range(len(logs)):
        if logs[i].split(' ')[1].isdigit():
            log.append(logs[i])
        else:
            let.append(logs[i])

    let.sort(key= lambda x: (x.split()[1:], x.split()[0]))

    return let+log

