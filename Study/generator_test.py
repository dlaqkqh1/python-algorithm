from async_generator import yield_from_


def file_read():
    with open("./words.txt") as file:
        yield from file.readlines()
                                   
 
for i in file_read():
    print(i)