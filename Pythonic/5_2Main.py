print("About to import support lib")
# no inspection PyprotectMember
print("done importing support lib")
import ch_06_packages_02_what_is_main_support as s


def main():
    print()
    print("The variable is {}".format(s.var))
    print("The name of the executed python module is {}".format(__name__))


if __name__ == '__main__':
    main()
