def write_on_to_file(site,  password, name=None):
    info_dict = {"site": site, "password": password, "name": name}
    with open("forget_pass_vault_file.txt", mode="a") as file:
        info_string = str(info_dict) + "\n"
        file.write(info_string)



def find_password(site :int, name=None):
    with open("forget_pass_vault_file.txt", "r") as file:
        file_list = file.readlines()
        for item in file_list:
            array_dict = eval(item)
            if array_dict["site"] == site:
                return array_dict["password"]

def fake_hash(text):
    x = len(text)
    return "*" * x

