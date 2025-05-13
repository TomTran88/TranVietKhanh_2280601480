print("Nhap cac dong van ban (Nhap 'done' de ket thuc): ")
lines = []
while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)
print("\nChuyen cac dong chu da nhap sau thanh chu in hoa: ")
for line in lines:
    print(line.upper())

