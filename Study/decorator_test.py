def html_tag(tag1):
    def decorator(func):
        def wrapper():
            return "<{0}>{1}</{0}>".format(tag1, func(), tag1)
        return wrapper
    return decorator

a, b = input().split()
 
@html_tag(a)
@html_tag(b)
def hello():
    return 'Hello, world!'
 
print(hello())