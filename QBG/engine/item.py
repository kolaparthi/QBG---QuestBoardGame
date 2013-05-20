# This class is copied from project http://code.google.com/p/pyquest/

__author__="Justin Neddo <jtneddo[at]gmail.com>"
__date__ ="$20 mai 2013 11:13:30$"


"""
Base Item class
"""
class Item(object):
  '''
  classdocs
  '''
  _name = ""
  _gold = 0
  _effects = []
  _type = None
  _magical = False
    
  def __init__(self, name=None, gold=0, effects=None):
    '''
    Constructor
    '''
    self._name = name
    self._gold = gold
    self._effects = effects
    self._type = None
    
  def equip(self, target):
    pass
  
  def unequip(self, target):
    pass
  
  def use(self, target):
    pass
  
