import requests
import json
import os
 

class NFTUploaderError(Exception):
    """
    nft_uploader 专用错误
    """
    pass

class nft_uploader:
    def __init__(self, base_url = "https://api.nft.storage", nft_storage_key = os.getenv("NFT_STORAGE_KEY")):
        if nft_storage_key == None:
            raise NFTUploaderError("no nft.storage API key")
        self.base_url = base_url
        self.urls = {
                'upload':self.base_url + '/upload',
                'store':self.base_url + '/store',
                'upload':self.base_url + '/upload',
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
          dict:
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
          dict:
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

    def upload_erc1155_nft(self, image_path, nft_name, nft_properties={}):
        """
        Store an ERC-1155-compatible NFT as a collection of content-addressed objects connected by IPFS CID links.

        TODO
        """
        with open(image_path, 'rb') as f:
            meta_json_str = '{"name": "' + nft_name + '","image": "undefined"'
            """
            if len(nft_properties) > 0:
                meta_json_str += ',"properties":{'
                for pro in nft_properties:
            """
            meta_json_str += ',"properties": {"videoClip": "undefined"}}'
            files = {'meta':(None, meta_json_str), 
                    'image': ("res.png", f),
                    'properties.videoClip': ("head.png", f),
                    }
            response = requests.post(self.urls["store"],files=files,headers=self.headers)
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
        return -1, {}

    def upload_nft(self):
        """
        自定义nft上传
        """
        pass

    def list(self,before, limit = 10):
        """
        list all stored files


        Params:
          before: string($date-time), eg. 2020-07-27T17:32:28Z
          limit: int
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
    nftL = nft_uploader()
    #err_code, json = nftL.upload_erc1155_nft('./head.png','resss',{"videoClip": 'no'})
    #err_code, json = nftL.list("2022-07-14T17%3A32%3A28Z",10)
    err_code, json = nftL.upload_file_from_path("./head.png","image/png")
    if err_code == 0:
        print(json)
    else:
        print("failed")
