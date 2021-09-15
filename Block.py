hosts_path = "C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
def Block(website_list):

    with open( hosts_path, 'r+' ) as file:
        content = file.read()
        for website in website_list:
            if website in content:
                pass
            else:
            # mapping hostnames to your localhost IP address
                file.write( redirect + " " + website + "\n" )
    print("Blocked")
