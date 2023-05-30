N, B = map(int, input().split())

if B == 2:
    value = format(N, 'b')
elif B > 2 and B <= 4:
    temp = format((4-B) + int(N/10),'b')
    value = format(N, 'b')
    print(int(value) - int(temp))
''' 
elif B > 4 and B <= 8:
elif B > 8 and B <= 16:
elif B > 16 and B <= 32:
elif B > 32 and B <= 36:
'''
print(value)