class flashcards:
    def __init__(self,word,meaning):
        self.word=word
        self.meaning=meaning
    def __str__(self):
        return self.word+'('+self.meaning+')'
flash=[]
while (True):
    word=input("enter a word to add to your flashcards:")
    meaning=input("Add the definition of the word:")
    flash.append(flashcards(word,meaning))
    option=input("If you want to add some more words to your flashcards press 0 if not press 1:")
    if (option):
        break
for i in flash:
    print(">",i)