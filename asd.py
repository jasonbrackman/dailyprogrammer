import os
import binascii
b = os.urandom(128)
a = binascii.hexlify(b)
for i in range(0, len(a)-1, 8):
    e = "\t{ 0x" + str(a[i + 0]) + str(a[i + 1]) + str(a[i + 2]) + str(a[i + 3])\
        + str(a[i + 4]) + str(a[i + 5]) + str(a[i + 6]) + str(a[i + 7]) + " }, "
    print(e)

import os
import sys
import binascii
b = os.urandom(2048)
a = binascii.hexlify(b)

# write out a c source code for the binary data
fd1 = open("config.cpp","wb")
fd1.write(b"#ifdef __cplusplus\nextern \"C\" {\n#endif //__cplusplus\n\n\nunsigned int config[] = \n{\n")
nop = [fd1.write(b"\t{ 0x" + a[i + 0] + a[i + 1] + a[i + 2] + a[i + 3] + a[i + 4] + a[i + 5] + a[i + 6] + a[i + 7] + b" }, \n") for i in range(0, len(a)-1, 8)]
fd1.write(b"};\n\n\nunsigned int config_size = sizeof(config) / sizeof(config[0]);\n\n#ifdef __cplusplus\n} // extern \"C\"\n#endif //__cplusplus\n")
fd1.close()

# write out a binary template
fd2 = open("config.bin","wb")
for i in range(0, len(b), 4):
  for j in range(i+3, i-1, -1):
    fd2.write(b[j])
fd2.close()
