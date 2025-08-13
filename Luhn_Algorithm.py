def luhn(number):
    digit=[int(v) for v in str(number)]
    sum=0
    for i,v in enumerate(reversed(digit)):
        if i%2==1:
            v*=2
            if v>9:
                v-=9
        sum+=v
    return sum%10==0
number=int(input())
print(luhn(number))