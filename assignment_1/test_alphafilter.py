
#Test cases for testing functionality of LetterFilter class
#Run `pytest` for a terminal to run all th test
import alphafilter
import re

class Test_Case_1: #normal positive cases
  
  myObj = alphafilter.LetterFilter("onomatopoeia")
  
  def test_filter_vowels(self):    
    assert self.myObj.filter_vowels() == "nmtp" #Test if vowels are filtered
  
  def test_filter_consonants(self):  
    assert self.myObj.filter_consonants() == "ooaooeia" #Tests if consonents are filtered

class Test_Case_2: #Using regex for wider coverages
 
  myObj = alphafilter.LetterFilter("abracadabra")
  
  def test_filter_vowels(self):    
    assert self.myObj.filter_vowels() != "aaaaa" #assert using regex if only consonants remains after filtering vowels
    assert not re.match("^[aeiou]", self.myObj.filter_vowels())

  def test_filter_consonants(self):  
    #assert using regex if only vowels remains after filtering consonants
    assert re.match("^[aeiou]", self.myObj.filter_consonants())