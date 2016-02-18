#Richard Albert Nichols III (inhahe@gmail.com)

import re
word = raw_input("ENTER YOUR WORD: ").upper()
dict = open("cmudict.0.6d","r")
while True:
  line1 = dict.readline().split()   
  if line1 == []: break
  if line1[0]==word:
    dict.seek(0)
    while True:
      line2 = dict.readline().split()
      if line2==[]: break
      if line2[0][:2]=="##": continue
      for phonemes3, phonemes5, p in (([re.sub("\d","",x) for x in line1[1:]], [re.sub("\d", "", x) for x in line2[1:]], 0), (line1[1:][:], line2[1:], 1)):
        for phoneme in phonemes5:
          if phoneme in phonemes3: phonemes3.remove(phoneme)
          else: break
        else:
          print ("\n"+line2[0], "*")[p],





              


      



    

  
