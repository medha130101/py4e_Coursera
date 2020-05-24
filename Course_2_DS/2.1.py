text = "X-DSPAM-Confidence:    0.8475";
spos = text.find('0')
epos = text.find('5')
zap = text[spos:epos+1]
val = float(zap)
print(val)
