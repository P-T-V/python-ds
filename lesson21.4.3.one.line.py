# print([{0: 0, 1: 100, 2: 144, 3: 20, 4: 19}[i_key] for i_key in {0: 0, 1: 100, 2: 144, 3: 20, 4: 19}
#        if {0: 0, 1: 100, 2: 144, 3: 20, 4: 19}[i_key] % 2 == 0])

[print(i_value, end=' ') for i_key, i_value in {0: 0, 1: 100, 2: 144, 3: 20, 4: 19}.items()
        if i_key % 2 == 0]
