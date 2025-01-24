import ripmodule as rp

if __name__ == '__main__':
    file = input("Please input the path of the file you wish to input in Ripser.")
    output = input("Please input the name of the file you want the results written to.")

    rp.ripser_input(file, output)