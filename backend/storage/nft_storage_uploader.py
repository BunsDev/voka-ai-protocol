import requests
import json
import os
 

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

    def upload_erc1155_nft(self, image_path, nft_name, nft_properties={},nft_file_properties={}):
        """
        Store an ERC-1155-compatible NFT as a collection of content-addressed objects connected by IPFS CID links.
        Params:
          image_path: nft对应图片的地址
          nft_name: nft的名字
          nft_properties: 
            nft的属性，比如:
              {"background":"orange", "clothes":"vietnum jacket", "eyes":"blue beams", "fur":"robot", "mouth":"grin"}
          nft_file_properties
            nft的文件属性，比如:
              {"videoclip": <video file content>, "avatormesk" <mest>}
        Return:
          int: 0 表示成功，否则表示失败
          dict:
        """
        with open(image_path, 'rb') as f:
            return self.upload_erc1155_nft_content(f, nft_name,nft_properties,nft_file_properties)

    def upload_erc1155_nft_content(self, image_content, nft_name, nft_properties={}, nft_file_properties={}):
        """
        Store an ERC-1155-compatible NFT as a collection of content-addressed objects connected by IPFS CID links.
        Params:
          image_content: nft对应图片文件内容
          nft_name: nft的名字
          nft_properties: 
            nft的属性，比如:
              {"background":"orange", "clothes":"vietnum jacket", "eyes":"blue beams", "fur":"robot", "mouth":"grin"}
          nft_file_properties
            nft的文件属性，比如:
              {"videoclip": <video file content>, "avatormesk" <mest>}
        Return:
          int: 0 表示成功，否则表示失败
          dict:
        """
        if not isinstance(nft_properties, dict) or not isinstance(nft_file_properties,dict):
            raise NFTStorageUploaderError("type of nft_properties/nft_file_properties are not dict")
        meta_json_str = '{"name": "' + nft_name + '","image": "undefined",'
        if len(nft_properties) > 0 or len(nft_file_properties) > 0:
            meta_json_str += '"properties":{'

        if len(nft_properties) > 0:
            for pro in nft_properties:
                meta_json_str += '"' + pro + '":"' + nft_properties[pro] + '",'
        if len(nft_file_properties) > 0:
            for f_pro in nft_file_properties:
                meta_json_str += '"' + f_pro + '":"undefined",'

        meta_json_str = meta_json_str[:-1]
        if len(nft_properties) > 0 or len(nft_file_properties) > 0:
            meta_json_str += '}'
        meta_json_str += '}'
        files = {'meta':(None, meta_json_str), 
                'image': (nft_name, image_content),
                }
        if len(nft_file_properties) > 0:
            for f_pro in nft_file_properties:
                files["properties." + f_pro] = (f_pro,nft_file_properties[f_pro])
        print(files)
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
    # usage demos
    nftL = nft_storage_uploader()
    with open("head.png", 'rb') as f:
        err_code, json = nftL.upload_erc1155_nft('./head.png','resss',nft_properties={"aaa":"bbb"},nft_file_properties = {"videoClip": f})
    #err_code, json = nftL.list("2022-07-14T17%3A32%3A28Z",10)
    #err_code, json = nftL.upload_file_from_path("./head.png","image/png")
    if err_code == 0:
        print(json)
    else:
        print("failed")
        print(json)
