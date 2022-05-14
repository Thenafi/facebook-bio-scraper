import os
from profile_url import *
from getting_bio import *

# this is the main that first gathers the profile url
# and then runs the bio gathering process
# its a bit slow process bceasue you will get temoporary block by facebook if you collect bio faster
# but its your wish to make it faster or solwer.
# to contol it change the timer(range) in getting_bio  line 44 (wait variable)


# NOTE Sample.json file is the main output or databse..  where all your data will be stored
# after running the programe use the
# updated file and convert it to our needs
# NOTE if there is no crd.json file create one like this https://f000.backblazeb2.com/file/ShareX2022/ShareX/Code_kCSU7eE5BC.png
#  it holds your password and id


# checking if you have the Sample.json file.. if not  import profile will run and create the json file
meh = os.path.isfile("./Sample.json")

if meh != True:
    print("Collecting Profile Url")
    profile()
    print("Bio Collection Starting")
    bio()
else:
    print("Bio Collection Starting")
    bio()

# now the json file will be updated (per run) and you can use that file get our bios.
## NOTE -#########################
# you can stop it and rerun as u wish. and collect few friends from the top
# script automatically understands from where to resume
######################################
# use the updated file and convert it to urls suitable needs .
# you can use this site #  https://data.page/json/csv # or  this   https://jsongrid.com/json-grid
# or use my convet.py file ur wish

# lastly if you have a lot of friends like 4k or 3k ... its going to be painfullly long process.  enjoy ❤
