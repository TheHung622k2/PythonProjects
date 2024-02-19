can = ['Canh', 'Tân', 'Nhâm', 'Quý', 'Giáp', 'Ất', 'Binh', 'Đinh', 'Mậu', 'Kỷ']
chi = ['Thân', 'Dậu', 'Tuất', 'Hợi', 'Tý', 'Sửu', 'Dần', 'Mão', 'Thìn', 'Tị', 'Ngọ', 'Mùi']

# Nhập năm dương lịch
namDL = int(input("Nhập năm dương lịch:"))
# Tính can
can1 = can[namDL % 10]
# Tính chi
chi1 = chi[namDL % 12]

print(f"Năm {namDL} âm lịch là {can1} {chi1}")
