# def add(a,b):
#     return a+b
# def sub(c,d):
#     print(add(3,9))
#     return c-d
# print(sub(7,14))
# def num(e,f):
#     return e*f
# print(num(5,2))


# def my(a,b):
#     return a*b
# def sum(c,d):
#     print(my(7,3))
#     return c+d
# print(sum(7,9))
# def num(e,f):
#     return e-f
# print(num(5,3))




# flow of nested

# def sum(a,b):
#     print("Zoya")
# x=7
# def add(y):
#     if y==7:
#         sum(7,9)
# print(add(7))



# def fruit(a,b):
#     x=a+b
#     return x
# y=7
# def shop():
#     print(fruit("Apple","banana"))
#     return "chocolate"
# print(shop())


def my():
    i=0
    b=[]
    while i<=5:
        b.append(i)
        i=i+1
    return b
def self():
    a=my()
    i=0
    while i<len(a):
      if a[i]%2==0:
          print(a[i],"even")
      else:
          print("odd")
      i=i+1
self()

         