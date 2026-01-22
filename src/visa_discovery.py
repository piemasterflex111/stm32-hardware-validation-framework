import pyvisa

def main():
    rm = pyvisa.ResourceManager()
    resouces = rm.list_resources()
    print("Available VISA Resources:")
    for r in resouces:
        print(r)


if __name__ == "__main__":
    main()  