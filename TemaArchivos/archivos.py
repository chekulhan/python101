with open("a3.txt", "r") as f:
  s = f.read()

# cambiar s a upper
s = s.upper()

with open("a3.txt", "w") as f:
  f.write(s)
