import random  #for random no.s
class Fun1: #classname is Fun1
    def display(self):
        a=range(10) #returns the values in the range of (0,10)
        c=random.choice(a)  #gives random no. between 0-10
        print("Select the numbers between 0 to 10",a)
        print("the no. to be guessed",c)
        
        k=len(a)
        for i in range(k-1):
            b=int(input("select a no."))
            if b==c:
                print("your guess is correct...You won the match")
                break;
            else:
                print("you have only",(k-1-i),"choices")
    
            
                
                
m=Fun1()
m.display()