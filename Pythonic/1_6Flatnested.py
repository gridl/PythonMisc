# Flat is better than nested

def main():
    download_flat()


def download_flat():
    print("lets try to donwload a file")
    if not s.check_download_url():
        print("Bad URL")
        return

    if not s.check_network():
        print("No DNS")
        return

    if not s.check_dns():
        print("No DNS")
        return

    if not s.check_access_allowed():
        print("No access")
        return

main()
