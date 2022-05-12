class Question:
    def __init__(self,text,choices,answer):
        self.text=text
        self.choices=choices
        self.answer=answer
    def checkAnswer(self,answer):
        return self.answer==answer


class Quiz: 
    def __init__(self,questions):
        self.questions=questions
        self.score=0
        self.questionIndex=0

    def getQuestions(self):         # bu methoda question göndericez.
            # return  sınav.questions[sınav.questionIndex] normalde böyle yazmamız lazım ama sınav nesnesi burada tanımlı değil onun yerine sınav objesi varmış gibi davranan self anahtar kelimesini kullanacağız.
            return self.questions[self.questionIndex]

    def displayq(self):
        soru=self.getQuestions()
        print(f'soru {self.questionIndex +1}: {soru.text}')

        for q in soru.choices:
            print('- '+q)
        answer=input('cevap :')
        self.guess(answer)
        self.loadQuestions()

    def guess(self,answer):
       question=self.getQuestions()
       if question.checkAnswer(answer):
           self.score +=1
           self.questionIndex +=1
          

    def loadQuestions(self):
        if len(self.questions)==self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayq()    
    
    def showScore(self):
       
        print('sorular bitti skorunuz:',self.score)

    def displayProgress(self):
        totalQ=len(self.questions)
        currentQ=self.questionIndex+1
        if currentQ>totalQ:
            print('quiz bitti')
        else:
            print(f'questions {totalQ} of {currentQ}'.center(100,'*'))    



q1=Question('en iyi programlama dili hangisi?',['c#','java','python'],'python')
q2=Question('en popüler programlama dili hangisi?',['c#','java','python'],'java')
q3=Question('en çok kazandıran programlama dili hangisi?',['c#','java','python'],'c#')
questions=[q1,q2,q3]

sınav=Quiz(questions)
# soru= sınav.questions[sınav.questionIndex] böyle yazıyorduk getQuestion methodu olmadan önce
sınav.displayq()



