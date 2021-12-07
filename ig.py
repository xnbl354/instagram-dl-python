# ==================================================================== INSTAGRAM SERVER DOWNLOADER WITH LOGIN BETA ==================================================================== #


# Source Code : X - Nabil354
# Github : github.com/nabilhnzm354/

# Module
import instaloader

# MAIN CODE
def instagram():
    ig = instaloader.Instaloader()
    username = input('Input Your Username IG : ')
    password = input('Input Your Password IG : ')
    reqUsername = input('Input Username Want To Download : ')
    ig.login(username,password)
    ig.download_profile(reqUsername)
    print('Done...')

# Note : 
# The Files : Images, Videos, Document Will Be Saved In Your Target Username Want To Download!

# DEFAULT SYSTEM MAIN
if __name__=="__main__":
    while True:
        try:
            instagram()
        except KeyboardInterrupt:
                print('{}\nOke Byeee....'.format(cyan))
                exit()

                                                     # ============== COPYRIGHT BY ALL REVESERVED 2021 X- NABIL354 ============== #


