'''
有一个字符串，里面包含各种类型的字符，现在需要做的是判断里面的括号是否匹配，
括号包括{ [ (三种，匹配返回true，不匹配返回false。举例 {  9 ( 1 )} ( )  返回true，{ ( } )返回false，（{ }）返回false
'''

_map  = {"{":"}","[":"]","(":")"}
# _str = "{[1(123)]}"
_str = "{[1(123)]}["

def judge_map(str_param):
    str_list = list(str_param)

    disk = []

    for str in str_list:
        if(str in _map.keys()):
            disk.append(str)
        elif(str in _map.values()):
            temp = disk.pop()
            print(temp)
            if(_map[temp] != str):
                print("false")

    print(disk)
    assert len(disk) == 0

judge_map(_str)

