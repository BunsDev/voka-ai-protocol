import requests
import json
import os
from nft_info import nft_info
 

class NFTStorageUploaderError(Exception):
    """
    nft_storage_uploader 专用错误
    """
    pass

class nft_storage_uploader:
    def __init__(self, base_url = "https://api.nft.storage", nft_storage_key = os.getenv("NFT_STORAGE_KEY")):
        if nft_storage_key == None:
            raise NFTStorageUploaderError("no nft.storage API key")
        self.base_url = base_url
        self.urls = {
                'upload':self.base_url + '/upload',
                'store':self.base_url + '/store',
                }

        self.headers = {'Authorization':'Bearer ' + nft_storage_key}

    def upload_file_from_content(self, file_name, file_content, file_type = None):
        """
        Store a file with nft.storage

        Params:
          file_name: string, file's name
          file_content: 
            - binary
            - _io.BufferedReader
          file_type: string, file's type, eg. image/png, etc.

        Returns:
          int: 0 表示成功，否则表示失败
          dict: 成功/失败信息
            成功时：
            'cid': 'ipfs地址'
            'created': '上传时间'
            'type': 'directory'
            'scope': ''
            'files': [{'name': '文件名', 'type': '文件类型'}]
            'size': 文件大小
            'name': ''
            'pin': {
                'cid': ''
                'created': ''
                'size': 
                'status': 'pinned'}
            'deals': []
        """
        if file_type != None and  isinstance(file_type, str):
            files = {'file': (file_name, file_content, file_type)}           
        else:
            files = {'file': (file_name, file_content)}           
        response = requests.post(self.urls["upload"], files=files, headers=self.headers)
        if response.status_code == 200:
            try:
                json = response.json()
            except:
                return -1, {}
            else:
                if json['ok']:
                    return 0, json['value']
        return -1, {}

    def upload_file_from_path(self, file_path, file_type = None):
        """
        Store a file with nft.storage

        Params:
          file_path: string, path to upload file
          file_type: string, file's type, eg. image/png, etc.

        Returns:
          int: 0 表示成功，否则表示失败
          dict: 成功/失败信息
            成功时：
            'cid': 'ipfs地址'
            'created': '上传时间'
            'type': 'directory'
            'scope': ''
            'files': [{'name': '文件名', 'type': '文件类型'}]
            'size': 文件大小
            'name': ''
            'pin': {
                'cid': ''
                'created': ''
                'size': 
                'status': 'pinned'}
            'deals': []
        """
        file_name = file_path.split("/")[-1]
        with open(file_path, 'rb') as f:
            return self.upload_file_from_content(file_name, f, file_type)

    def upload_erc1155_nft(self, image_path, nft_name, nft_properties={}, nft_str_info = {}, nft_file_info = {}):
        """
        Store an ERC-1155-compatible NFT as a collection of content-addressed objects connected by IPFS CID links.
        Params:
          image_path: nft对应图片的地址
          nft_name: nft的名字
          nft_properties: 
            nft的属性，比如:
              {"background":"orange", "clothes":"vietnum jacket", "eyes":"blue beams", "fur":"robot", "mouth":"grin"}
          nft_str_info:
            nft除了properties外的其他字符串信息，比如：
            {"author":{"body_author":"a", "head_author":"b"}}
          nft_file_info
            nft除了properties外的其他文件信息，比如：
              {"models": {"head_model":<model file content>, "body_model":<model file content>"}}
        Return:
          int: 0 表示成功，否则表示失败
          dict: 成功/失败信息
        """
        with open(image_path, 'rb') as f:
            return self.upload_erc1155_nft_content(f, nft_name,nft_properties,nft_str_info, nft_file_info)

    def upload_erc1155_nft_info(self, nft_info_obj):
        """
        Store an ERC-1155-compatible NFT as a collection of content-addressed objects connected by IPFS CID links.
        Params:
          nft_info_obj： nft_info类，通过nft_info类，传递nft信息
        Return:
          int: 0 表示成功，否则表示失败
          dict: 成功/失败信息
        """
        if not isinstance(nft_info_obj, nft_info):
            raise NFTStorageUploaderError("type of nft_info must be nft_info")

        response = requests.post(self.urls["store"],files=nft_info_obj.generate_nft_storage_requst_dict(),headers=self.headers)
        if response.status_code == 200:
            try:
                json = response.json()
            except:
                return -1, {}
            else:
                if json['ok']:
                    return 0, json['value']
                else:
                    return -1, json['error']
        else:
            return -1, response.text



    def upload_erc1155_nft_content(self, image_content, nft_name, nft_properties={}, nft_str_info = {}, nft_file_info = {}):
        """
        Store an ERC-1155-compatible NFT as a collection of content-addressed objects connected by IPFS CID links.
        Params:
          image_content: nft对应图片文件内容
          nft_name: nft的名字
          nft_properties: 
            nft的属性，比如:
              {"background":"orange", "clothes":"vietnum jacket", "eyes":"blue beams", "fur":"robot", "mouth":"grin"}
          nft_str_info:
            nft除了properties外的其他字符串信息，比如：
            {"author":{"body_author":"a", "head_author":"b"}}
          nft_file_info
            nft除了properties外的其他文件信息，比如：
              {"models": {"head_model":<model file content>, "body_model":<model file content>"}}
        Return:
          int: 0 表示成功，否则表示失败
          dict: 成功/失败信息
        """
        if not isinstance(nft_properties, dict) or not isinstance(nft_str_info,dict) or not isinstance(nft_file_info, dict):
            raise NFTStorageUploaderError("type of nft_properties/nft_file_properties are not dict")
        nft_info_obj = nft_info(nft_name, image_content);
        nft_info_obj.add_properties(nft_properties)
        nft_info_obj.add_nft_str_info(nft_str_info)
        nft_info_obj.add_nft_file_info(nft_file_info)
        return self.upload_erc1155_nft_info(nft_info_obj)

    def upload_nft(self, image_path, nft_name, nft_properties={},nft_file_properties={}):
        """
        自定义nft上传，目前暂时使用self.upload_erc1155_nft。
        TODO: 改成自定义
        """
        return self.upload_erc1155_nft(image_path, nft_name, nft_properties,nft_file_properties)

    def list(self,before, limit = 10):
        """
        list all stored files


        Params:
          before: string($date-time), eg. 2020-07-27T17:32:28Z
          limit: int
        Return:
          int: 0 表示成功，否则表示失败
          dict: 成功/失败信息
        """
        list_url = self.base_url + "/?before=" + before + "&limit=" + str(limit)
        response = requests.get(list_url,headers=self.headers)
        if response.status_code == 200:
            try:
                json = response.json()
            except:
                return -1, {}
            else:
                if json['ok']:
                    return 0, json['value']
        else:
            return -1, {}

if __name__ == "__main__":
    # usage demos
    nftL = nft_storage_uploader()
    with open("head.png", 'rb') as f:
        #err_code, json = nftL.upload_erc1155_nft('./head.png','resss')
        err_code, json = nftL.upload_erc1155_nft('./head.png','resss',nft_properties={"aaa":"bbb"},nft_file_info = {"test":{"videoClip": f}})
    #err_code, json = nftL.list("2022-07-14T17%3A32%3A28Z",10)
    #err_code, json = nftL.upload_file_from_path("./head.png","image/png")
    if err_code == 0:
        print(json)
    else:
        print("failed")
        print(json)
