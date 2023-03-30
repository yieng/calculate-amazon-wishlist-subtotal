# Javascript to extract prices from wishlist:
# document.querySelectorAll(".a-offscreen").forEach(x=>console.log(x.innerHTML))

with open("prices.txt","r") as f:
    prices = f.read()

A1=prices.replace('\n','$').split('$')

A2=[a for a in A1 if ("Log" not in a) and ("VM" not in a)]

A3a = [a for a in A2 if 'x' in a]
print('A3a = ', A3a)
A3b = [a for a in A2 if 'x' not in a and '.' in a]
print('A3b = ', A3b)
A3c = [a.replace('\u200b ','') for a in A2 if '.' not in a]
#print('A3c = ', A3c)

if '' in A3b:
    A3b.remove('')
elif '\u200b ' in A3b:
    A3b.remove('\u200b ')
    
for i in range(len(A3c)):
    if A3c[i]=='':
        A3c[i]=1
    else:
        A3c[i]=int(A3c[i])
print('A3c = ', A3c)

#print(len(A3b),len(A3c))

B=[a.replace('.','') for a in A3b]
#print(len(B))

while True:
    try:
        #single = sum([float(a) for a in A3b])
        single100 = sum([int(b) for b in B])
        single = single100/100
        #multiple = [float(a[:-4]) for a in A3a]
        multiple = [int(b)/100 for b in B]
        #factors = [int(a[-2:-1]) for a in A3a]
        factors = [a-1 for a in A3c]
        #print(factors)
        break
    except ValueError:
        if '' in A3b:
            A3b.remove('')
        elif '\u200b ' in A3b:
            A3b.remove('\u200b ')
        print(A3b)
        
##        elif '\u200b ' in A3b:
##            A3b.remove('\u200b ')
##        else:
##            break

total = single + sum([multiple[i]*(factors[i]) for i in range(len(factors))])
print('TOTAL = ',total)

target_value = 0
tv100 = target_value*100
print('DIFFERENCE = ',(tv100-single100)/100)
