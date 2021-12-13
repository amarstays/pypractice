# Given a string consisting of only lowercase characters, create two methods that remove all the consonants or vowels from the given word. They must retain the original order of the characters in the returned strings.

class LetterFilter:
    def __init__(self, s):
        self.s = s

    def filter_vowels(self):
        res=[]
        for chr in self.s:
          if chr not in "aeiou":
            res.extend(chr)      
        return "".join(res) 

    def filter_consonants(self):

        res=[]
        for chr in self.s:
          if chr in "aeiou":
            res.extend(chr)      
        return "".join(res)

#Test here
# myObj = LetterFilter("onomatopoeia")
# print(myObj.filter_vowels())