hosts_path = "C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
def Unblock(website_list):
    with open( hosts_path, 'r+' ) as file:
        content = file.readlines()

        for line in content:
            if not any( website in line for website in website_list ):
                file.write( line )

    # removing hostnmes from host file
                file.truncate(0)

    print("Unblocked")