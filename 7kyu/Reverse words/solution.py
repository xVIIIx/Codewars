def reverse_words(txt):
  #go for it
  sp = txt.split(' ')
  for i in range(len(sp)):
      sp[i] = sp[i][::-1]
      
 # print(' '.join(sp))
  
  return ' '.join(sp)
