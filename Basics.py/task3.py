x=input('Name of friend 1:')
y=input('Name of friend 2:')
z=input('Name of friend 3:')
a=float(input('CGPA of ' + x))
b=float(input('CGPA of ' + y))
c=float(input('CGPA of ' + z))
t=a+b+c
m= t/3

if a<b and a<c:
    print('CGPA of '+ x +' is lowest')
elif b<c and b<a:
    print('CGPA of '+ y +' is lowest')
else :
    print('CGPA  of '+ c +' is lowest')

print('Average CPGA is', m )