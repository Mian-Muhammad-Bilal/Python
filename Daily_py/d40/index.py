import random
flag = 0
while (flag < 1 or flag > 2):
    flag = int(input('''Select the option, if you want to encode or decode:
         1)Encode
         2)Decode
        '''))

if (flag == 1):
    encode_str = input('''Enter the phrase you want to encode: ''')
    if (len(encode_str) > 3):
        encode_str = encode_str+encode_str[0]
        encode_str = encode_str[1:]
        ram_st = ''.join((random.choice('abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
                         for i in range(3)))
        encode_str = ram_st+encode_str
        ram_end = ''.join((random.choice('abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
                          for i in range(3)))
        encode_str = encode_str+ram_end
        print(f"Your final encoded string is: {encode_str}")
    else:
        encode_str = encode_str+encode_str[0]
        encode_str = encode_str[1:]
        print(f"Your final encoded string is: {encode_str}")

elif (flag == 2):
    decode_str = input('''Enter the phrase you want to decode: ''')
    if (len(decode_str) > 3):
        decode_str = decode_str[3:]
        decode_str = decode_str[:-3]
        decode_str = decode_str[len(decode_str)-1]+decode_str
        decode_str = decode_str[:-1]
        print(f"Your final encoded string is: {decode_str}")
    else:
        decode_str = decode_str+decode_str[0]
        decode_str = decode_str[1:]
        print(f"Your final encoded string is: {decode_str}")
