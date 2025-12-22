def autoEndLine(max_char, text):
    max_char-=4
    cur_maxchar = max_char
    line_data = text.split()
    linemanager = []
    returnedLineData = []
    for i in line_data:
        print(linemanager, cur_maxchar)
        if len(i) < max_char:
            if len(i) < cur_maxchar:
                cur_maxchar -= len(i)
                linemanager.append(i)
            else :
                cur_maxchar = max_char
                returnedLineData.append(" ".join(linemanager))
                linemanager.clear()
                cur_maxchar -= len(i)
                linemanager.append(i)
        else:
            linemanager.append(i[:cur_maxchar])
            returnedLineData.append(" ".join(linemanager))
            linemanager.clear()
            linemanager.append(i[(max_char - len(i)):])
    returnedLineData.append(" ".join(linemanager))
    print("\n".join(returnedLineData))

    for i in returnedLineData:
        print(len(i))

            

autoEndLine(26,"Tugas anda hari ini adalah coli sembarangan asu memek saddddddddddddddddddddddddddddddddddddddddddddddddd jembuten saddddddddddddddddddddddddddddddddddddddddddddddddd")
