class ReviewTypeDetector:
    print("Welcome to the Review Type Detector ")
    try:
        filePositive = open("positive.txt", "rt")
        fileNegative = open("negative.txt", "rt")
        dataPositive = filePositive.read()
        dataNegative = fileNegative.read()
        wordsPositive = dataPositive.split()
        wordsNegative = dataNegative.split()
        print("Loaded the default dataset")
    except Exception as e:
        print(e)
        print("System will now terminate ")
        exit(0)
    positive = False
    Negative = False
    # s = input("Please enter the review to detect : ")
    fileRead = open("input.txt", "r", encoding="utf-8")
    s = fileRead.read()
    fileRead.close()
    pc = 0
    nc = 0
    sw = s.split()
    sw = set(sw)
    n = len(sw)
    pos = []
    neg = []
    for p in wordsPositive:
        for j in sw:
            if j.lower().__eq__(p):
                pc = pc + 1
                pos.append(j)
                if pc == 1:
                    positive = True
    pr = int(round((pc / n) * 100))
    s1 = ""
    fileWrite = open("Result-Type.txt", "w", encoding="utf-8")
    if positive:
        s1 = "and it is a Positive Review"
        print("This review is a Positive Review \nPercentage of positive word is : {} %".format(pr))
        if pc == 1:
            print("The positive word is : ", pos)
        else:
            print("The positive words are : ", pos)
        fileWrite.write(s1)
        print("wrote")
        fileWrite.close()
        exit(0)
    for ne in wordsNegative:
        for j in sw:
            if j.lower().__eq__(ne):
                nc = nc + 1
                neg.append(j)
                if nc == 1:
                    Negative = True
    nr = ((nc / n)) * 100
    nr = int(round(nr))
    if Negative:
        s1 = "and it is a  Negative Review"
        print("This review is a Negative Review \nPercentage of positive word is : {} %".format(nr))
        if nc == 1:
            print("The negative word is : ", neg)
        else:
            print("The negative words are : ", neg)
    fileWrite.write(s1)
    print("wrote")
    fileWrite.close()
