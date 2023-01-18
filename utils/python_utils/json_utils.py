"""
主要是一些json文件的操作，包括：
* 读取
* 写json文件
* 修改json文件中某个字段
"""
import json

"""
读取json格式的文件，并生成json类
如果json格式错误，返回空
"""
def read_json_file(json_f):
    try:
        with open(json_f, 'r') as json_file:
            return json.loads(json_file.read());
    except:
        return None

"""
将json类写入outfile文件
写入成功返回True，否则返回False
"""
def write_json_to_file(json_class, outfile):
    try:
        with open(outfile, "w") as write_file:
            json.dump(json_class, write_file, indent=4)
    except:
        return False
    else:
        return True

"""
修改json文件中的某些字段
json_f为目标文件
modify_dicts，表示需要修改的字段，例如
    {"name":"Jerry", "attributes":[{"k21":"v21"}, {"k22":"v22"}]}
任一key不存在就会报错
"""
def modify_json_file(json_f, modify_dicts):
    json_class = read_json_file(json_f)
    if not json_class:
        return False

    for k,v in modify_dicts.items():
        if not k in json_class:
            return False
        json_class[k] = v
    return write_json_to_file(json_class, json_f)

"""
想json文件中增加字段
json_f为目标文件
new_dicts表示需要增加的字段，例如
    {"name":"Jerry", "attributes":[{"k21":"v21"}, {"k22":"v22"}]}
任一字段已经存在就报错
"""
def add_key_in_json(json_f, new_dicts):
    json_class = read_json_file(json_f)
    if not json_class:
        return False

    for k,v in new_dicts.items():
        if k in json_class:
            return False
        json_class[k] = v
    return write_json_to_file(json_class, json_f)

"""
想json文件中删除字段
json_f为目标文件
new_dicts表示需要增加的字段，例如
    {"name":"Jerry", "attributes":[{"k21":"v21"}, {"k22":"v22"}]}
任一字段不存在就报错
"""
def delete_key_in_json(json_f, delete_dicts):
    json_class = read_json_file(json_f)
    if not json_class:
        return False

    for k,v in delete_dicts.items():
        if not k in json_class:
            return False
        json_class.pop(k)
    return write_json_to_file(json_class, json_f)


def test():
    modify_json_file("metadata.json", {"name":"Jerry", "attributes":[{"k21":"v21"}, {"k22":"v22"}]})
    delete_key_in_json("metadata.json", {"b":"Jerry", "a":[{"k21":"v21"}, {"k22":"v22"}]})


if __name__ == "__main__":
    test()
