questions=[
    ["Which programming language is used to create instagram","Python","Java","HTML","CSS",1],

    ["Which programming language is used to create instagram", "Python", "Java", "HTML", "CSS", 1],

    ["Which programming language is used to create instagram", "Python", "Java", "HTML", "CSS", 1],

    ["Which programming language is used to create instagram", "Python", "Java", "HTML", "CSS", 1],

    ["Which programming language is used to create instagram", "Python", "Java", "HTML", "CSS", 1],

    ["Which programming language is used to create instagram", "Python", "Java", "HTML", "CSS", 1],

    ["Which programming language is used to create instagram", "Python", "Java", "HTML", "CSS", 1],

    ["Which programming language is used to create instagram", "Python", "Java", "HTML", "CSS", 1],

    ["Which programming language is used to create instagram", "Python", "Java", "HTML", "CSS", 1],

    ["Which programming language is used to create instagram", "Python", "Java", "HTML", "CSS", 1]
    ]
levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000]
money=0
# reply=int(input("Enter your answer in b/w (1-4):"))
for i in range(0,len(questions)):
    question=questions[i]
    print(f"Your question for Rs.{levels[i]}")
    print(f"a.{question[1]}  b.{question[2]}")
    print(f"c.{question[3]}  d.{question[4]}")
    reply = int(input("Enter your answer in b/w (1-4):"))
    if reply==question[-1]:
        print(f"Correct answer,you have won {levels[i]}")
        if i==4:
            money=10000
        elif i==9:
            money=320000
    else:
        print("Wrong answer")
        break



