#Nhap so tu nguoi dung
so = int(input("Nhap mot so nguyen: "))
#Kiem tra xem so do co phai la so chan hay khong
if so % 2 == 0:
    print(so,"La so chan.")
else:
    print(so,"Khong phai la so chan.")