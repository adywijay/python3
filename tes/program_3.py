# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 18:44:43 2022

@author: WIN_10_PRO
"""

def seto(n):
  result = []
  for x in range(1, n+1):
      if x % 3 == 0 and x % 5 == 0:
          result.append("snip snap")
      elif x % 3 == 0:
          result.append('snip')
      elif x % 5 == 0:
          result.append('snap')
      else:
          result.append(str(x))
  return result
def main():
    print(', '.join(seto(100)))
main()