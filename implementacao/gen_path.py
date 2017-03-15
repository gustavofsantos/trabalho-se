#!/usr/bin/python3
from random import randint, choice

def isInBorder(p, max):
  x, y = p
  if x == 0 or y == 0:
    return True
  elif x == max - 1 or y == max - 1:
    return True
  else:
    return False

def isCorner(p, max):
  x, y = p;
  if x == y == 0:
    return True
  elif x == y == max -1:
    return True
  elif x == 0 and y == max - 1:
    return True
  elif x == max - 1 and y == 0:
    return True
  else:
    return False

def isInLeftBorder(p, m):
  x, y = p
  if x == 0:
    return True
  else:
    return False

def isInUpBorder(p, m):
  x, y = p
  if y == m - 1:
    return True
  else:
    return False

def isInRightBorder(p, m):
  x, y = p
  if x == m - 1:
    return True
  else:
    return False

def isInBottonBorder(p, m):
  x, y = p
  if y == 0:
    return True
  else:
    return False

def possibleNextPosition(p, m):
  x, y = p
  if isCorner(p, m):
    if x == m - 1 and y == m - 1:
      np = choice([(x - 1, y), (x, y - 1)])
    elif x == 0 and y == 0:
      np = choice([(x + 1, y), (x, y + 1)])
    elif x == 0 and y == m - 1:
      np = choice([(x, y - 1), (x + 1, y)])
    elif x == m - 1 and y == 0:
      np = choice([(x - 1, y), (x, y + 1)])
  elif isInBorder(p, m):
    if isInLeftBorder(p, m):
      np = choice([(x, y+1), (x, y-1), (x+1, y)])
    elif isInRightBorder(p, m):
      np = choice([(x, y+1), (x, y-1), (x-1, y)])
    elif isInBottonBorder(p, m):
      np = choice([(x-1, y), (x+1, y), (x, y+1)])
    elif isInUpBorder(p, m):
      np = choice([(x-1, y), (x+1, y), (x, y-1)])
  else:
    np = choice([(x+1, y), (x-1,y), (x, y+1), (x, y-1)])
  return np

def safeNextPosition(p1, p2, m):
  x, y = p2
  l = []
  if isCorner(p2, m):
    if x == m - 1 and y == m - 1:
      l.append((x - 1, y))
      l.append((x, y - 1))
    elif x == 0 and y == 0:
      l.append((x + 1, y))
      l.append((x, y + 1))
    elif x == 0 and y == m - 1:
      l.append((x, y - 1))
      l.append((x + 1, y))
    elif x == m - 1 and y == 0:
      l.append((x - 1, y))
      l.append((x, y + 1))
  elif isInBorder(p2, m):
    if isInLeftBorder(p2, m):
      l.append((x, y+1))
      l.append((x, y-1))
      l.append((x+1, y))
    elif isInRightBorder(p2, m):
      l.append((x, y+1))
      l.append((x, y-1))
      l.append((x-1, y))
    elif isInBottonBorder(p2, m):
      l.append((x-1, y))
      l.append((x+1, y))
      l.append((x, y+1))
    elif isInUpBorder(p2, m):
      l.append((x-1, y))
      l.append((x+1, y))
      l.append((x, y-1))
  else:
    l.append((x+1, y))
    l.append((x-1, y))
    l.append((x, y+1))
    l.append((x, y-1))

  l2 = list(filter(lambda p: p != p1, l))
  np = choice(l2)
  return np

def getPath(m: int, n: int):
  """return a list of positions"""
  l = []
  ip = (randint(0, m -1), randint(0, m - 1))
  l.append(ip)
  l.append(possibleNextPosition(l[-1], m))
  for i in range(n - 1):
    l.append(safeNextPosition(l[-2], l[-1], m))

  l.reverse()
  return l