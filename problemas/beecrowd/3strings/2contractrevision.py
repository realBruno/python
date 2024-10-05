# Contract Revision
# 05/10/2024

while True:
    try:
        flawed, contract = input().split()

        if flawed in contract:
            if set(flawed) == set(contract) and \
                int(flawed) != 0:
                print(0)
            elif set(flawed) == set(contract):
                break
            else:
                contract = contract.replace(flawed,'')
                print(int(contract))
        else:
            print(int(contract))

    except:
        break

# não precisa do try e except. percebi que o código para quando as entradas
# são zero e int(contract) == 0.