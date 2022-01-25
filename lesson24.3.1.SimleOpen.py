import io


try:
    filename = 'result.24.3.1.txt'
    # filename = ''
    file = open(filename, 'w')
    string = input('Pls, insert data: ')
    file.write(str(int(string)))
    # file.close()
    print(file.closed)
except io.UnsupportedOperation:
    print("io.UnsupportedOperation: not writable")
except FileExistsError:
    print("File exists")
except ValueError:
    print("Invalid literal")
except FileNotFoundError:
    print('File not found')
except PermissionError:
    print("File open problem")
except SyntaxError:
    print('invalid syntax')
else:
    print("The program was executed without errors")
finally:
    file.close()
    print(file.closed)
