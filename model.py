def fanstr(s:str):
  str=''
  list=[]
  for s1 in s:
    list.insert(s1, 0)
  for st in list:
    str=str+st
  return str
