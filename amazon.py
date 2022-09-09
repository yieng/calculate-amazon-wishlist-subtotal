# Javascript to extract prices from wishlist:
# document.querySelectorAll(".a-offscreen").forEach(x=>console.log(x.innerHTML))

with open("prices.txt","r") as f:
    prices = f.read()

A1=prices.replace('\n','$').split('$')

A2=[a for a in A1 if "Log" not in a]

A3a = [a for a in A2 if 'x' in a]
print('A3a = ', A3a)
A3b = [a for a in A2 if 'x' not in a]
print('A3b = ', A3b)

A3b.remove('')

single = sum([float(a) for a in A3b])
multiple = [float(a[:-4]) for a in A3a]
factors = [int(a[-2:-1]) for a in A3a]

total = single + sum([multiple[i]*factors[i] for i in range(len(factors))])
print('TOTAL = ',total)
