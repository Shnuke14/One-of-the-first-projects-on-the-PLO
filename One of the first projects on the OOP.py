from re import split
from string import ascii_letters
from typing import Type

class Person:
  S_RUS = "йцукенгшщзхъфывапролджжэячсмитьбю-"
  S_RUS_UPPER = S_RUS.upper()
  def init(self, fio, old, ps, weight):
    self.verify_fio(fio)
    self.verify_old(old)
    self.verify_ps(ps)
    self.verify_weight(weight)
    
    self.fio = fio.split()
    self.__old = old
    self.__ps = ps
    self.__weight = weight

  @classmethod
  def verify_fio(cls, fio):
    if type(fio) != str:
      raise TypeError("ФИО должно быть строкой")
    f = fio.split()

    if len(f) != 3:
      raise TypeError("Неверный формат записи")
    
    letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
    for s in f:
      if len(s) < 1:
        raise TypeError("В ФИО должен быть хотя бы один символ")
      if len(s.strip(letters)) != 0:
        raise TypeError("В ФИО должны быть только буквы и дефис")

  @classmethod
  def verify_old(cls, old):
    if type(old) != int or old < 14 or old > 120:
      raise TypeError("Возраст должен быть целым числом в диапазоне [14, 120]")
    
  @classmethod
  def verify_weight(cls, weight):
    if type(weight) != float or weight < 20 or weight > 100:
      raise TypeError("Вес должен быть числом в диапазоне [20, 100]")

  @classmethod
  def verify_ps(cls, ps):
    if type(ps) != str:
      raise TypeError("Паспортные данные должны быть в виде строки")
    s = ps.split()
    if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
      raise TypeError("Неверный формат паспорта")
    for p in s:
      if not p.isdigit():
        raise TypeError("Серия и номер должны быть числами")

  @property
  def fio(self):
    return self.__fio

  @property
  def old(self):
    return self.__old

  @old.setter
  def old(self, old):
    self.verify_old(old)
    self.__old = old

  @property
  def weight(self):
    return self.__weight

  @weight.setter
  def weight(self, weight):
    self.verify_weight(weight)
    self.__weight = weight

  @property
  def ps(self):
    return self.__ps

  @ps.setter
  def ps(self, ps):
    self.verify_ps(ps)
    self.__ps = ps

p = Person("Дядя Корней Корнеевич", 17, "1111 141322", 56.3)
p.old = 18
p.weight = 62.7
p.ps = "1234 567890"
print(p.__dict)