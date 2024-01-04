print("Enter a number")
num1 = int(input())
print("ENter another number")
num2 = int(input())
try:
    print("The sum is ",num1+num2)
except Exception:
    print("Wrong")

print("This line is important")

x = 'From marquard@uct.ac.za'
print(x[14:17])

data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3])


text = "X-DSPAM-Confidence:    0.8475"
p = text.find('0')
q = text[p:]
print(float(q))
print(type(q))
