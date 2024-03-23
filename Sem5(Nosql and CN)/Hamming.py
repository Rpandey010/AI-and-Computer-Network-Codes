def calcRedundantBits(m):
    r = 0
    while 2 ** r < m + r + 1:
        r += 1
    return r

def posRedundantBits(data, r):
    m = len(data)
    res = ''
    j = 0
    k = 1
    for i in range(1, m + r + 1):
        if i == 2 ** j:
            res = '0' + res
            j += 1
        else:
            res = data[-k] + res
            k += 1
    return res

def calcParityBits(arr, r):
    n = len(arr)
    for i in range(r):
        val = 0
        for j in range(1, n + 1):
            if j & (2 ** i):
                val ^= int(arr[-j])
        arr = arr[:n - (2 ** i)] + str(val) + arr[n - (2 ** i) + 1:]
    return arr

def detectError(arr, nr):
    n = len(arr)
    res = 0
    for i in range(nr):
        val = 0
        for j in range(1, n + 1):
            if j & (2 ** i):
                val ^= int(arr[-j])
        res = val * (10 ** i) + res
    return int(str(res), 2)

def hammingCode(data):
    m = len(data)
    r = calcRedundantBits(m)
    arr = posRedundantBits(data, r)
    arr = calcParityBits(arr, r)
    return arr

def simulateError(received_data):
    print("Received Data is " + received_data)
    correction = detectError(received_data, calcRedundantBits(len(received_data)))
    if correction == 0:
        print("There is no error in the received message.")
    else:
        print("The position of error is", len(received_data) - correction + 1, "from the left")

# Enter the data to be transmitted
data = '1011001'
transmitted_data = hammingCode(data)
print("Data transmitted is " + transmitted_data)

# Simulate error in transmission by changing a bit value.
# Change the 5th bit (0-based index) to introduce an error.
received_data = transmitted_data[:5] + ('0' if transmitted_data[5] == '1' else '1') + transmitted_data[6:]
simulateError(received_data)
