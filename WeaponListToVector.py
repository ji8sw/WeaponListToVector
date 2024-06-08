import requests
Raw = ""

# download raw info from Github
Response = requests.get("https://raw.githubusercontent.com/DurtyFree/gta-v-data-dumps/master/WeaponList.ini")
if Response.status_code == 200:
    Raw = Response.text
else:
    print(f"Failed to proceed. Status code: {Response.status_code}")
    exit()

# split into lines
Hashes = [line.split('=')[1] for line in Raw.strip().split('\n')]

# create vector format
HashVector = "std::vector<uint32_t> eWeaponArray = {\n" + ", ".join(Hashes) + "\n};"

# write to file
with open('Result.cpp', 'w') as File:
    File.write(HashVector)
