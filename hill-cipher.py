import numpy as np

def encrypt(msg, key):
    msg = msg.upper().replace(' ', '')
    if len(msg) % 2 == 1:
        msg += 'X'
    msg = [ord(c) - ord('A') for c in msg]
    msg = np.array(msg).reshape(-1, 2)
    key = np.array(key).reshape(2, 2)
    encrypted_msg = np.matmul(msg, key) % 26
    return ''.join([chr(c + ord('A')) for c in encrypted_msg.flatten()])

if __name__ == '__main__':
    print("HILL CIPHER ENCRYPTION")
    print("Please enter the key as a 2x2 matrix (e.g. '2 5 1 3' for [2 5; 1 3]):")
    key = input().split()
    key = [int(k) for k in key]
    msg = input("Please enter the message: ")
    print('Encrypted message:', encrypt(msg, key))
 