from qs import question_prompts
from question import question

Questions=[
    question(question_prompts[0],"c"),
    question(question_prompts[1],"b"),
    question(question_prompts[2], "a")
    ]
def run_test(questions):
    score=0
    for question in questions:
        answer=input(question.prompt)
        if answer==question.answer:
            score+=1


    print("You got " +str(score) + "/"+str(len(questions)))

run_test(Questions)


