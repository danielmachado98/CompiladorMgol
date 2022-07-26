base = open("ProgBase/base.alg", 'r')
file = base.read()
l = 1
c = 0



for character in file:
    if(character == '\n'):
        l+=1
        c=0

    c+=1
    print('character',character,'linha',l,'coluna',c)