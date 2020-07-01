# Couroutines

# use yield function
def print_fancy_name(prefix):
    try:
        while True:
            name = (yield)
            print(prefix + ":" + name)
    except GeneratorExit:
        print("Done!")
co = print_fancy_name("cool")
# Initialization
next(co)
# sending data and control
co.send("Leonardo Rodrigues ")
co.close()