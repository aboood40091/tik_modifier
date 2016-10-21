import sys, time

print("tik_modifier")
print("(C) 2016 AboodXD")
print("")

if len(sys.argv) != 3:
    print("Err...")
    time.sleep(5)
    sys.exit(1)
    

with open(sys.argv[1], "rb") as tik:
    print("Opening .tik...")
    tik1 = tik.read()
    tik.close()


tik2 = bytearray(tik1)

value = int(sys.argv[2])

if value == 0:
    print("Modifing .tik...")
    tik2[0x1:0x1+1] = (1).to_bytes(1, 'big')
    tik2[0xF:0xF+1] = (int.from_bytes(tik2[0xF:0xF+1],'big') - 2).to_bytes(1, 'big')

elif value == 1:
    print("Modifing .tik...")
    tik2[0x1:0x1+1] = (1).to_bytes(1, 'big')
    tik2[0xF:0xF+1] = (int.from_bytes(tik2[0xF:0xF+1],'big') + 2).to_bytes(1, 'big')

else:
    print("Wrong value!")
    time.sleep(5)
    sys.exit(1)

name = os.path.splitext(sys.argv[1])[0]
    
with open(name + "_modified.tik", "wb+") as tik3:
    tik3.write(tik2)
    tik3.close()
    print("Modified!")
