str = 'X-DSPAM-Confidence:0.8475'
col = str.find(':')
snumber = (str[col+1:])
fnumber = float(snumber)
print(fnumber)
print(type(fnumber))
