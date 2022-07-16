
## nft_info类

nft_info(nft_name, image_content)

nft的数据类，用于管理nft相关数据，包括：
  - nft_name: string，nft的名称

  - image_content: binary or _io.BufferedReader, nft对应图片的内容

  - properties: dict，nft的属性，在opensea中会单独显示，因此和other_info分离开，比如:
    {
      "background":"orange",
      "clothes":"vietnum jacket",
      "eyes":"blue beams",
      "fur":"robot",
      "mouth":"grin"
    }

  - nft_info: dict，nft的其他信息
    {
      "character_authors" : {"body_author": "tom", "cloth_author": "jerry"},
      "character_models" : {"head_model": model_data, "hair_model": model_data}
    }

  - nft_str_info: dict，记录nft其他信息中，属性是字符串的，nft_str_info是nft_info的一部分
    {
      "character_authors" : {"body_author": "tom", "cloth_author": "jerry"}
    }

  - nft_file_info: dict，记录nft其他信息中，属性是文件的， nft_file_info是nft_info的一部分
    {
      "character_models" : {"head_model": model_data, "hair_model": model_data}
    }

nft最终对应的json格式应该是：
{
  "name":"nft name",
  "image":"url of image",
  "properties" : {
    "background":"orange",
    "clothes":"vietnum jacket",
    ...
  },
  "character_authors" : {
    "body_author": "tom",
    "cloth_author": "jerry"
  },
  "character_models" : {
    "head_model": model_data,
    "hair_model": model_data
  }
}
另外，无聊猿对应的json格式如下
{
  "image":"ipfs://QmPbxeGcXhYQQNgsC6a36dDyYUcHgMLnGKnF8pVFmGsvqi",
  "attributes":[
    {
      "trait_type":"Mouth",
      "value":"Grin"
    },{
      "trait_type":"Clothes",
      "value":"Vietnam Jacket"
    },{
      "trait_type":"Background",
      "value":"Orange"
    },{
      "trait_type":"Eyes",
      "value":"Blue Beams"
    },{
      "trait_type":"Fur",
      "value":"Robot"
    }
  ]
}
上述两种格式，opensea都能识别

### Methods defined here:

#### add_nft_file_info_dict(self, info_dict)
      增加单个nft file info
    Params:
      info: dict

#### add_nft_info(self, info_key, info_dict)
      针对某个nft_key，增加属性，这里nft_key和properties同级
    
    Params:
      info_key: string
      info_dict: dict

#### add_nft_str_info_dict(self, info_dict)
      增加多个nft string info
    Params:
      info: dict

#### add_properties(self, properties_dict)
      增加多个propertie
    
    Params:
      property_dict: dict，其中有一个或多个属性
    
    Returns:
      bool:表示添加是否成功

#### add_property(self, property_name, property_value)
      增加单个propertie
    
    Params:
      property_name: str
      property_value: str
    
    Returns:
      bool:表示添加是否成功

#### generate_nft_storage_requst_dict(self)
    为nft.storage http api中store接口请求生成要求的json结构，参考官方文档：https://nft.storage/api-docs/
    
    Returns:
      dict: 最终结构类似于：
      {
        "meta": {
          "name":"nft name",
          "image":"undefined",
          "properties" : {
            "background":"orange",
            "clothes":"vietnum jacket",
            ...
          },
          "character_authors" : {
            "body_author": "tom",
            "cloth_author": "jerry"
          },
          "character_models" : {
            "head_model": "data_undefined",
            "hair_model": "data_undefined"
          }
        },
        "image": image_content,
        "character_models.head_model": model_content,
        "character_models.hair_model": model_content,
      }

#### print_nft_info(self)
    打印nft info的信息

## nft_storage_uploader类

用于向nft.storage上传数据

nft_storage_uploader(base_url='https://api.nft.storage', nft_storage_key="")

### Methods defined here:

#### list(self, before, limit=10)
    list all stored files
    
    Params:
      before: string($date-time), eg. 2020-07-27T17:32:28Z
      limit: int
    Return:
      int: 0 表示成功，否则表示失败
      dict: 成功/失败信息

#### upload_erc1155_nft(self, image_path, nft_name, nft_properties={}, nft_str_info={}, nft_file_info={})
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

#### upload_erc1155_nft_content(self, image_content, nft_name, nft_properties={}, nft_str_info={}, nft_file_info={})
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

#### upload_erc1155_nft_info(self, nft_info_obj)
    Store an ERC-1155-compatible NFT as a collection of content-addressed objects connected by IPFS CID links.
    Params:
      nft_info_obj： nft_info类，通过nft_info类，传递nft信息
    Return:
      int: 0 表示成功，否则表示失败
      dict: 成功/失败信息

#### upload_file_from_content(self, file_name, file_content, file_type=None)
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

#### upload_file_from_path(self, file_path, file_type=None)
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

#### upload_nft(self, image_path, nft_name, nft_properties={}, nft_file_properties={})
    自定义nft上传，目前暂时使用self.upload_erc1155_nft。
    TODO: 改成自定义
