import requests
import os
from json_utils import write_json_to_file, read_json_file


"""
期望达到的目的：
* 在一个文件夹中存储若干“对”文件，一“对”文件包括1个图片文件和一个无后缀的文件，无后缀文件中是json格式
  例如
    0.png <-> 0
    1.png <-> 1
    2.png <-> 2
    ......
    n.png <-> n
  * 文件名中的数字从0开始，一次递增
  * json格式的文件中，记录的是满足ERC721格式NFT的metadata
* 将文件夹中所有“对”中的图片上传到ipfs，并修改对应json文件，将图片在ipfs中的地址记录在json.image中，最后将所有json格式文件放在一个新的文件夹中
* 将生成的包含所有json文件的文件夹上传到ipfs
"""


"""
另一种需求：图片数量很少，但每张图片对应多个json文件，
比如0-39json文件中内容是相同的

可以利用上面需求的结果，结合脚本实现
   
"""


projectId = os.getenv("INFURA_IPFS_AIP_KEY")
projectSecret = os.getenv("INFURA_IPFS_AIP_KEY_SECRET")
endpoint = "https://ipfs.infura.io:5001"

"""
获取路径下所有json文件
"""
def get_json_files(path):
    file_names = os.listdir(path)
    res = []
    for file_name in file_names:
        if os.path.splitext(file_name)[1] == '.json':
            res.append(file_name)
    return res

"""
把图片上传到ipfs，返回文件在ipfs上的hash
"""
def upload_file_to_ipfs(file_name):
    ### CREATE AN ARRAY OF TEST FILES ###
    files = {
        'file': open(file_name,'rb')
    }
    ### ADD FILE TO IPFS AND SAVE THE HASH ###

    response1 = requests.post(endpoint + '/api/v0/add', files=files, auth=(projectId, projectSecret))
    if response1.status_code != 200:
        return None

    print(response1.text)
    hash = response1.text.split(",")[1].split(":")[1].replace('"','')
    return hash

"""
根据hash从ipfs上获取文件内容
"""
def get_file_content(hash):
    ### READ FILE WITH HASH ###
    params = {
        'arg': hash
    }
    response2 = requests.post(endpoint + '/api/v0/cat', params=params, auth=(projectId, projectSecret))
    print(response2)
    print(response2.text)

"""
根据hash，从目标机器上删除pin的文件
"""
def remove_pined_file(hash):
    params = {
        'arg': hash
    }
    ### REMOVE OBJECT WITH PIN/RM ###
    response3 = requests.post(endpoint + '/api/v0/pin/rm', params=params, auth=(projectId, projectSecret))
    print(response3.json())

"""
@ description:
    生成个NFT的metadata文件：
    1. 上传nft_file到IPFS，获取其在IPFS的URI
    2. 根据该URI以及nft_name，nft_description以及nft_attributes，生成NFT metadata文件
    3. 将将生成的metadata命名为out_file
    以无聊猿为例，其metadata格式如下：
    {
        "image":"ipfs://QmaFrLffAFdrgNHcppRvMjucVA4fekhPQczy6wVCDMcyy3",
        "attributes":[
            {"trait_type":"Hat","value":"S&m Hat"},
            {"trait_type":"Mouth","value":"Discomfort"},
            {"trait_type":"Fur","value":"Black"},
            {"trait_type":"Clothes","value":"Prison Jumpsuit"},
            {"trait_type":"Eyes","value":"Crazy"},
            {"trait_type":"Background","value":"New Punk Blue"}
        ]
    }
    在此基础之上，可以增加name & description
@ params:
    * nft_file: String，表示NFT对应的文件，这里特指图片
    * nft_name: String，metadata文件中，该NFT的名称
    * nft_description: String，metadata文件中，该NFT的描述
    * nft_attributes: Dict，metadata文件中，该NFT的属性
    * out_file: String
"""
def generate_nft_metadata(nft_file, nft_name, nft_description, nft_attributes, out_file):
    hash = upload_file_to_ipfs(nft_file)
    if not hash:
        return False
    json_class = {}
    json_class["name"] = nft_name
    json_class["description"] = nft_description
    json_class["image"] = "ipfs://" + hash
    json_class["attributes"] = nft_attributes
    return write_json_to_file(json_class, out_file)

"""
生成个NFT的metadata文件：
1. 上传nft_file到IPFS，获取其在IPFS的URI
2. 增加 or 修改json_file中的image字段，设置为nft_file的URI
3. 将将生成的metadata命名为out_file
"""
def generate_nft_metadata_from_file(json_file, out_file):
    json_class = read_json_file(json_file)
    if not json_class:
        return False

    if not "image" in json_class:
        return False

    # if not "name" in json_class:
        #json_class["name"] = ""

    return generate_nft_metadata(json_class["image"], json_class["name"], json_class["description"], json_class["attributes"], out_file)

"""
复制metadata_file，并将这些文件命名为start_id, start_id + 1, ... , start_id + num - 1
"""
def copy_metadata(metadata_file, start_id, num, target_path):
    json_class = read_json_file(metadata_file)
    if not json_class:
        return False
    for num in range(start_id,start_id + num): 
        write_json_to_file(json_class, target_path + "/" + str(num))


"""
批量生成NFT matadata
给定path下又若干json后缀文件，其中包含原始metadata，image字段制定其对应NFT的图片
原始metadata中制定的image路径，是相对于python文件而言的
"""
def batch_generate_metadata(path):
    json_files = get_json_files(path)
    print(json_files)
    for file in json_files:
        file_path = path + "/" + file
        generate_nft_metadata_from_file(file_path, file_path)
        


def test():
    #get_json_files("./")
    #generate_nft_metadata('./myNFT.png', "Tom", "nft test", [{"key1":"value1"}, {"key2":"value2"}], "test.json")
    #generate_nft_metadata_from_file('metadata.json', "test2.json")
    #copy_metadata("test.json", 40, 40)
    # batch_generate_metadata("./nft_metadatas")
    copy_metadata("./nft_metadatas/metadata1.json", 0, 40, "./out")
    copy_metadata("./nft_metadatas/metadata2.json", 40, 40, "./out")
    copy_metadata("./nft_metadatas/metadata3.json", 80, 40, "./out")
    copy_metadata("./nft_metadatas/metadata4.json", 120, 40, "./out")
    copy_metadata("./nft_metadatas/metadata5.json", 160, 40, "./out")
    copy_metadata("./nft_metadatas/metadata6.json", 200, 40, "./out")
    copy_metadata("./nft_metadatas/metadata7.json", 240, 40, "./out")
    copy_metadata("./nft_metadatas/metadata8.json", 280, 40, "./out")

if __name__ == "__main__":
    test()
    
