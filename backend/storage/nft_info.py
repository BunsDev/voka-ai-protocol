class nft_info:
    """
    nft的数据类，包括：
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
    """
    properties = {}
    nft_info = {}
    nft_str_info = {}
    nft_file_info = {}
    def __init__(self, nft_name, image_content):
        self.nft_name = nft_name
        self.image_content = image_content

    def add_property(self, property_name, property_value):
        """
          增加单个propertie

        Params:
          property_name: str
          property_value: str

        Returns:
          bool:表示添加是否成功
        """
        if isinstance(property_name,str) and isinstance(property_value,str):
            self.properties[property_name] = property_value
            return True
        return False

    def add_properties(self, properties_dict):
        """
          增加多个propertie

        Params:
          property_dict: dict，其中有一个或多个属性

        Returns:
          bool:表示添加是否成功
        """
        if isinstance(properties_dict, dict):
            for key, value in properties_dict.items():
                self.properties[key] = value
            return True
        return False

    def add_nft_info(self, info_key, info_dict):
        """
          针对某个nft_key，增加属性，这里nft_key和properties同级

        Params:
          info_key: string
          info_dict: dict

        """
        if isinstance(info_dict, dict):
            for key, value in info_dict.items():
                self.nft_info[info_key][key] = value
                if isinstance(value, str):
                    if info_key in self.nft_str_info:
                        self.nft_str_info[info_key][key] = value
                else:
                    if info_key in self.nft_file_info:
                        self.nft_file_info[info_key][key] = value
            return True
        return False

    def add_nft_str_info_dict(self, info_dict):
        """
          增加多个nft string info
        Params:
          info: dict
        """
        if isinstance(info_dict, dict):
            for key, value in info_dict.items():
                self.nft_info[key] = value
                self.nft_str_info[key] = value
            return True
        return False

    def add_nft_file_info_dict(self, info_dict):
        """
          增加单个nft file info
        Params:
          info: dict
        """
        if isinstance(info_dict, dict):
            for key, value in info_dict.items():
                self.nft_info[key] = value
                self.nft_file_info[key] = value
            return True
        return False

    def generate_nft_storage_requst_dict(self):
        """
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
        """
        meta_json_str = '{"name": "' + self.nft_name + '","image": "undefined",'
        if len(self.properties) > 0:
            meta_json_str += '"properties":{'
            for k,v in self.properties.items():
                meta_json_str += '"' + k + '":"' + v + '",'
        meta_json_str = meta_json_str[:-1]
        meta_json_str += '},'

        if len(self.nft_str_info) > 0:
            for k,v in self.nft_str_info.items():
                meta_json_str += '"' + k + '":{'
                for sub_k, sub_v in v.items():
                    meta_json_str += '"' + sub_k + '":"' + sub_v + '",'
            meta_json_str = meta_json_str[:-1]
            meta_json_str += '},'

        if len(self.nft_file_info) > 0:
            for k,v in self.nft_file_info.items():
                meta_json_str += '"' + k + '":{'
                for sub_k, sub_v in v.items():
                    meta_json_str += '"' + sub_k + '":"undefined",'
            meta_json_str = meta_json_str[:-1]
            meta_json_str += '},'

        meta_json_str = meta_json_str[:-1]
        if len(self.properties) > 0 or len(self.nft_info) > 0:
            meta_json_str += '}'

        res_dict = {
                "meta": (None,meta_json_str),
                "image":(self.nft_name, self.image_content)
                }

        if len(self.nft_file_info) > 0:
            for k,v in self.nft_file_info.items():
                #res_json_str += '"' + k + '":{'
                for sub_k, sub_v in v.items():
                    res_dict[k + '.'  + sub_k] = (sub_k, sub_v)

        return res_dict

    def print_nft_info(self):
        """
        打印nft info的信息
        """
        print("nft name: ", self.nft_name)
        print("nft properties: ", self.properties)
        print("nft other info: ", self.nft_info)

if __name__ == "__main__":
    with open("head.png", 'rb') as f:
        nft_info_obj = nft_info("head", f)
        #nft_info_obj.add_property("1","a")
        nft_info_obj.add_properties({"2":"b", "3":"c"})
        nft_info_obj.add_nft_str_info_dict({"authors":{"head_author":"tom", "body_author":"jerry"}})
        nft_info_obj.add_nft_file_info_dict({"models":{"head_model":f, "body_model":f}})
        nft_info_obj.add_nft_info("models", {"hair_model":f, "hair_author":"tttom"})
        nft_info_obj.print_nft_info()
        print(nft_info_obj.generate_nft_storage_requst_dict())

