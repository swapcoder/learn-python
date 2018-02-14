

class SpellChecker:
    def __init__(self, filepath) :
        #get commonly used words in memory
        self.words = open(filepath).readlines()
        self.words = [word.strip() for word in self.words]

    def checkSpell(self, spell):
        return spell in self.words


if __name__ == '__main__':
    sc = SpellChecker("spell.word")
    print (sc.checkSpell("the"))
    print ("hello")
