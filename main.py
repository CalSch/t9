import time
input_text=input("type: ")
`

chars={
'1':list('@#$%&!"\':;?='),
'2':list('abc'),
'3':list('def'),
'4':list('ghi'),
'5':list('jkl'),
'6':list('mno'),
'7':list('pqrs'),
'8':list('tuv'),
'9':list('wxyz'),
'0':list(' '),
}

output=''

index=-1
last_char=None

for char in input_text:
    if char == ".":
        if last_char==None or index==-1:
            continue
        output+=chars[last_char][index%len(chars[last_char])]
        index=-1
        last_char=None
    elif char in chars:
        index+=1
        last_char=char

print(output)

