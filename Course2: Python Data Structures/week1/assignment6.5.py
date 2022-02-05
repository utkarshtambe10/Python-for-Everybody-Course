text = "X-DSPAM-Confidence:    0.8475"

pos = text.find("0")

len = float(text[pos : pos + 6])
print(len)
