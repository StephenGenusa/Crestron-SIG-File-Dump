from struct import unpack

RLSIG0001 = 1
LOGOSSIG001 = 2
 
sig_file_name = "Some Great Project.sig"

# Determine Signal file type
print("Determining signal file format...")
sig_file_type = ""
f = open(sig_file_name, "rb")
try:
    while True:
        sig_file_type += chr(unpack('B', f.read(1))[0])
        if sig_file_type[-1] == ']':
            break
    print("Signal file format is", sig_file_type)
    if sig_file_type == "[RLSIG0001]":
        sig_file_type = RLSIG0001
    elif sig_file_type == "[LOGOSSIG001.000]":
        sig_file_type = LOGOSSIG001
    else:
        print ("unknown sig file type. exiting.")
        exit()
    try:
        while True:
            sig_name_len = unpack("h", f.read(2))[0] - 8
            if sig_file_type == RLSIG0001:
                sig_name = f.read(sig_name_len)
            else:
                sig_name = f.read(sig_name_len).decode("utf-16")
            if sig_name:
                sig_index = unpack("I", f.read(4))[0]
                sig_type = f.read(1)
                sig_flags = f.read(1)
                print(sig_name.decode('ascii'), sig_index, sig_type, sig_flags)
            else:
                break
    except:
        pass
finally:    
    f.close()