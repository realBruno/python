# Dados mutáveis
# 15/10/2024

a = ['Bruno', 'Fernandes']
b = a
print(b)
a[1] = 'Santos'
print(b)

print('#'*10)

b = a.copy()
a[1] = 'Fernandes'
print(b)