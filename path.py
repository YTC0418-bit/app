class Textpath:
  def __init__(path,bin=False,new=True):
    self.__path=path
    self.__bin=bin
    self.__new=new
    self.__read=read
  def newconnect(self):
    if self.__bin and self.__new:
      self.__mode='wb'
    elif self.__bin and not self.__new:
      self.__mode='b+'
    self.__file=open(self.path,mode=self.__mode)

