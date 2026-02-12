import numpy as np

x = np.random.randint(1, 101, 100000)
result=[] 


#print(x)
for i in x:
    result.append(str(i)[0])

#print(result)
np.savetxt('numeros.txt', result, fmt='%s')