#Ham nay cong hai so
def cong (x, y):
  return x + y
#Ham nay tru hay so
def tru(x, y):
  return x - y
#Ham nay nhan hai so
def nhan (x, y):
  return X * y
#Ham nay chia hai so
def chia (x, y):
  return x / y
print("Chon hoat dong:")
print("1.Cong")
print("2.tru")
print("3.Nhan")
print("4.Chia")
choice = input ("Nhap lua chon phep tinh (1/2/3/4):")
numl = int(input("Nhap so dau tien: "))
num2= int(input("Nhap so thu hai: "))
if choice == '1':
  print (numl,"+",num2,"=", cong (numl,num2))
elif choice == '2':
  print (numl,"-", num2,"=", tru (numl, num2))
elif choice == '3':
  print (numl,"*", num2,"=", nhan (numl, num2))
elif choice == '4':
  print(numl,"/",num2,"=", chia (numl,num2))
else:
  print("Khong hop le: ")
