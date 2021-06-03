def humor(pt, st, tt):
  if st < pt and tt >= st:
    return ":)"
  elif st > pt and tt <= st:
    return ":("
  elif st > pt and tt > st and tt-st < st-pt:
    return ":("
  elif st > pt and tt > st and tt-st >= st-pt:
    return ":)" 
  elif st < pt and tt < st and tt-st < st-pt:
    return ":)"
  elif st < pt and tt < st and tt-st >= st-pt:
    return ":("
  elif pt == st:
    if tt > st:
      return ":)"
    else:
      return ":("

a = 4
b = 10
c = 20
print( humor(a, b, c) )