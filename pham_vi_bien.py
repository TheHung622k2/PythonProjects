def my_function():
    global x 
    x = 10
    y = 5

    print("Trong hàm my_function()")
    print("Biến toàn cục x = ", x)
    print("Biến cục bộ y = ", y)

my_function()

print("Ngoài hàm my_function()")
print("Biến toàn cục x = ", x)