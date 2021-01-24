def bin2hex(bstr):
    if ' ' in bstr:
        bstr_nospace = bstr.replace(' ', '')
        hstr = '%0*X' % ((len(bstr_nospace) + 3) // 4, int(bstr_nospace, 2))
    else:
        hstr = '%0*X' % ((len(bstr) + 3) // 4, int(bstr, 2))

    print(hstr)

def hex2bin(hstr):
    hex_form = int(hstr, 16)                    #convert to integer
    bin_form = f'{hex_form:0>b}'                #convert to binary f string
    remainder = len(bin_form) % 4               #calculate remainder when dividing by 4
    if remainder == 0:                          #check if remainder is 0 and set length to length of
        length = len(bin_form)                  #binary f string if divisible by 4, else var length
    else:                                       #to length of binary f string plus 4 minus remain to
        length = len(bin_form) + (4-remainder)  #set length to the next highest number divisble by 4
    bin_full = f'{bin_form:0>{length}}'         #add leading zeros to string if needed
    bin_full = str(bin_full)                    #convert to string for split_four() function
    bin_final = split_four(bin_full, 4)         #send binary full variable to split_four() function
    print(bin_final)                            #print binary final

def split_four(string, length):                 #function to add spaces every fourth character in binary
    return ' '.join(string[i:i+length] for i in range(0, len(string), length))

hex_string = input("enter hexdecimal: ")
hex2bin(hex_string)
bin_string = input("enter binary: ")
bin2hex(bin_string)
