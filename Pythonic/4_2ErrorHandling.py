import _02_lets_play_catch_support as s

def main():
    #run_with_checks()
    #run_with_handling()
    run_with_handling_separate_errors()


def run_with_checks():
        if not s.check_network():
            print("cannot download no network")
            return
        if not s.check_dns():
            print("Cannot download, no DNS")
        data = s.download_file()
        print("downloaded data  -> {}".format(data))

def run_with_handling():
    try:
        data = s.download_file()
        print("downloaded data -> {}").format(data)
    except Exception as x:
        print("cannot download {} -> {}".format(type(x),x))





def run_with_handling_separate_errors():
    try:
        data = s.download_file()
        print("downloaded data -> {}".format(data))
    except PermissionError:
        print("No permissions")
    except ConnectionError:
        print("Network issue")
    except Exception as x:
        print("cannot download {} - {}").format(type(x), x)



if __name__ == '__main__':
    main()
