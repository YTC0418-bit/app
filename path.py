class Textpath:
  def __init__(self,path,bin=False,new=True):
    self.__path=path
    self.__bin=bin
    self.__new=new
    self.__read=read
  def newconnect(self):
      if self.__bin and self.__new:
          self.__mode='wb'
      elif self.__bin and not self.__new:
          self.__mode='b+'
      elif not self.__bin and self.__new:
          self.__mode='w+'
      else: 
          self.__mode='a+'
      self.__file=open(self.path,mode=self.__mode)
   def write(self,text):
       self.__file.write(text)
   def clear(self):
       self.__file2=open(self.path,mode='w')
       self.__file.write('')





