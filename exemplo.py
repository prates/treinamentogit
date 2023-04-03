



import json

def read_colaborar(x):
    return x



def read_olimpo(x):
    print(x)







def read_athena(X):
    return "athena"


if __name__ == "__main__":
    acess_key = "sdlshfdjksdfhdkjfhdshfjkshjghfjdgfhdjgsfd"
    secret_key = "aldjsajfgdsgfdshgdhghfsjhjkgfdhjkhdjkfhgsfdjgg"
    region = "sa-east-1"
    file_json = open("flags.json")
    data = file_json.read()
    flags = json.loads(data)
    if flags["colaborar"]:
        read_colaborar("teste")
    if flags["olimpo"]:
        read_olimpo("olimpo")
    if flags["Athena"]:
        read_athena("zdsd")
