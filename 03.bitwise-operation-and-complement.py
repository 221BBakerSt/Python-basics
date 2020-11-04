"""
对于无符号数，最高位被计算机系统规定为数据位。对于有符号数signed，最高位被计算机系统规定为符号位。
内存溢出就是计算机给数据分配内存不足，数据溢出到内存里，影响到其他数据。比如变量在内存占2 Bytes，用来存储一个天文数字。
假设分配2 Bytes来表示一个整数，原码会有16位。比如-3表示为1000 0000 0000 0011
原码(original code)最左位表示符号，0就是正数，1就是负数
反码(one's complement)就是原码的最左位不变，其它位都取反
补码(complemental code)就是反码+1
for postive numbers, original code = one's complement = comlemental code
加法就是补码相加，保留相同位数，移除多出来的位
"""
# 0b开头表示二进制，比如把decimal的-18转换成binary是-0b10010
print(bin(-18))
# 0o开头表示八进制，比如把decimal的18转换成Octonary是0o22
print(oct(18))
# 0x开头表示十六进制，比如把decimal的18转换成Hexadecimal是0x12
print(hex(18))
# 把16进制的0x12转换成decimal
print(int("0x12", 16))
# 把8进制的0o12转换成decimal
print(int("0o12", 8))


print(40>>3) #右移3位 x shifted right by 3 bits 右移n位就是除以2的n次方
#把decimal的数都写成binary，然后进行与或逻辑运算
print(9&5) #按位与 bitwise AND 两个二进制数上下对比，都为1才计作1
print(9|5) #按位或 bitwise OR 两个二进制数上下对比，只要有1就计作1
print(9^5) #按位异或 bitwise XOR 两个二进制数上下对比，不相同才计作1
print(~9) #取反 bitwise negation / bitwise NOT 正数取反就是+1后变为负数
#取反的过程：原数字--转化为补码--所有位取反，得到答案的补码--转化为原码
a=20
a<<=2
print(a)