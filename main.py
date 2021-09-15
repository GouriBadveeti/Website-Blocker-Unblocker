import time
import Block
import Unblock
# change hosts path according to your OS
hosts_path = "C:\Windows\System32\drivers\etc\hosts"

# localhost's IP
redirect = "127.0.0.1"

# websites That you want to block
text = "Website Blocker/Unblocker"

print( text.center( 100 ))
while True:

    print( "To Block enter 1\n" )
    print( "To Unblock enter 2\n" )
    print( "To Exit enter 3" )
    Choice = int( input( "Do you want Block/Unblock the website:" ) )

    website_list = []
    if Choice == 1:
        num = int(input("Enter the number of website to be blocked:"))
        for i in range( 1,num + 1):
            Website = str(input("Enter the website to be blocked:"))
            website_list.append(Website)
        Block.Block(website_list)
    elif Choice == 2:
        num = int( input( "Enter the number of website to be Unblocked:" ) )
        for i in range( 1, num + 1 ):
            Website = str( input( "Enter the website to be Unkblocked:" ) )
        Unblock.Unblock(website_list)


    elif Choice == 3:
        print("Thanks for using this :)")
        break
    else:
        print("Please enter a valid input")

time.sleep( 5 )
