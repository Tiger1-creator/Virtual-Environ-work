#PROGRAM TO DISPLAY LENGTH OF ENTERED STRING
text = input("enter string you want:")
print(len(text))


#PROGRAM TO PRINT LENGTH OF ENTERED STRING BY EXCLUDING SPACES
text = input("enter string you want:")
text=text.replace(" ","")
print(len(text))


#PROGRA WHICH INPUTS 5 STRING PROGRAM AND DISPLAY THEIR LENGTHS EXCLUDES SPACES 

a = input("enter first string A: ")
b = input("enter second string B: ")
c = input("enter third string C: ")
d = input("enter forth string D: ")
e= input("enter fifth string E: ")
a = a.replace(" ", "")
b = b.replace(" ", "")
c = c.replace(" ", "")
d = d.replace(" ", "")
e = e.replace(" ", "")
print("length of A= ", len(a), "length of B= ", len(b), "length of C= ", len(c), "length of D= ", len(d), "length of E= ", len(e))


#KAJIPOTEFU PROGRAM

text=text.replace("a","k")
text=text.replace("i","j")
text=text.replace("e","t")
text=text.replace("u","f")
text=text.replace("o","p")
text=text.replace("A","K")
text=text.replace("I","J")
text=text.replace("E","T")
text=text.replace("U","F")
text=text.replace("O","P")

print(text)