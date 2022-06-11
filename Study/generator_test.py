from async_generator import yield_from_


def file_read():
    with open("./Study/words.txt") as file:
        lines = file.readlines()
        yield from map(lambda x: x.strip(), lines)
                                   
 
for i in file_read():
    print(i)