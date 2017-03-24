if __name__ == '__main__':
    try:
        print("ping!")
    except SyntaxError:
        print("Ping")

#create a zup file containing it by
# zip machine.zip __main__.py

# use it by
#python machine.zip

