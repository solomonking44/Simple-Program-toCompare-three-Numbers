def compare(a, b, c):
    if a == b == c:
        print(f"All numbers are equal therefore {a} is the largest")
    else:
        if a > b:
            if a > c:
                print(f"{a} -> a is the largest")
            elif c > a:
                print(f"{c} -> c is the largest")
            else:
                print(f"{c} -> a and c are the largest")
        else:
            if a == b:
                if a > c:
                    print(f"{a} -> a & b are the largest")
                else:
                    print(f"{c} -> c is the largest")
            else: 
                if b > c:
                    print(f"{b} -> b is the largest")
                elif c > b:
                    print(f"{c} -> c is the largest")
                elif b==c:
                    print(f"{c} -> b and c are the largest")
            
    


print("Enter A")
a = input()
print("Enter B")
b = input()
print("Enter C")
c = input()

print(f"a = {a}, b = {b} and c = {c}")


compare(a, b, c)
