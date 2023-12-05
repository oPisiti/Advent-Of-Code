from timeMe import timeMe

def getLoopSize(pubKey: int, initialSN: int, initValue = 1):
    loopSize = 0    
    value = initValue
    subjectNumber = initialSN

    while True:
        value *= subjectNumber
        value = value%20201227
        loopSize += 1

        if value == pubKey: break
    
    return loopSize


def transformSN(initialSN: int, loopSize: int, initValue = 1):
    value = initValue

    for i in range(loopSize):
        value *= initialSN
        value = value%20201227
    
    return value

@timeMe
def findEncryptionKey():
    cardPub, doorPub =           2069194, 16426071
    cardLoopSize, doorLoopSize = 0, 0
    initialSN =                  7

    # Finding card loop size
    cardLoopSize = getLoopSize(cardPub, initialSN)
    print(f"Card loop size: {cardLoopSize}")

    # Finding the encryption key
    encKey = transformSN(doorPub, cardLoopSize)
    print(f"Encryption key: {encKey}")



if __name__ == '__main__':
    findEncryptionKey()
