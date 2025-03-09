def xor(a, b): 
    result = [] 
    for i in range(1, len(b)): 
        if a[i] == b[i]: 
            result.append('0') 
        else: 
            result.append('1') 
    return ''.join(result) 

def mod2div(dividend, divisor): 
    pick = len(divisor) 
    tmp = dividend[0: pick]  
    while pick < len(dividend): 
        if tmp[0] == '1':   
            tmp = xor(divisor, tmp) + dividend[pick] 
        else:  
            tmp = xor('0'*pick, tmp) + dividend[pick]    
        pick += 1
    if tmp[0] == '1': 
        tmp = xor(divisor, tmp) 
    else: 
        tmp = xor('0'*pick, tmp) 
    checkword = tmp 
    return checkword 

def create_error(data, point):
    data = list(data) 
    if data[point] == '0':
        data[point] = '1'
    else:
        data[point] = '0'
    return ''.join(data)  

def encodeData(data, key):  
    l_key = len(key) 
    appended_data = data + '0'*(l_key-1) 
    remainder = mod2div(appended_data, key)   
   
    codeword = data + remainder     
    print("Remainder : ", remainder) 
    print("Encoded Data (Data + Remainder) : ", 
          codeword) 
    point = 3
    errorData=create_error(codeword, point)
    #watch this out for the error
    #print("Error Data : ", errorData)
    #recieve(errorData, key)

    recieve(codeword, key)

def recieve(errorData, key): 
    l_key = len(key) 
    remainder = mod2div(errorData, key) 
    print("Remainder : ", remainder)
    if remainder == '0'*len(remainder):
        print("Data recieved correctly")
    else:
        print("Data recieved incorrectly")

# Driver code 
#data = "100011011"
#key = "10101"
data = input("enter the data: ")
key = input ("enter the key: ")
encodeData(data, key) 