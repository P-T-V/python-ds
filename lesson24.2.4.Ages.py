import os

try:
    filename = 'numbers.txt'
    # filename = 'new'
    # filename = os.path.abspath(os.path.join('..', 'index.html'))
    print(filename)
    if os.path.isdir(filename):
        print("It's directory. File expected")
    ages = open(filename)
    line = ages.read().rstrip()
    list_ages = line.split('\n')
    print(list_ages)

    result = open('result.txt', 'x')
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(10):
        age = int(list_ages[i])
        string = ''.join((str(age), '-', alphabet[i]))
        print(string)
        result.write(string)
        result.write('\n')
    ages.close()
    result.close()
except FileNotFoundError:
    print("No such file or directory")
except FileExistsError:
    print("File already exists")
except ValueError:
    print("Invalid literal")
except PermissionError:
    print("Permission denied")
# except:
#     print("Something goes wrong!")
