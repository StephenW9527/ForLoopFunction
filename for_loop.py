

BiliBili = [
    "Anchor",
    ["Cat_Was_Born_In_Summer", "Fox_With_9_Tails",
        ["SevenHills", "During", "Dough"]]]


""" for characters in BiliBili:
        if isinstance(characters, list):
            for host in characters:
                if isinstance(host, list):
                    for husbands in host:
                        print("Darlings:", husbands)

                else:
                    print("host:", host)

        else:
            print("roles:", characters)   """    # 三个双引号 可以注释多行代码


# writing with recursion function (generalized for nested lists)
def print_nested_list(somelist):  # 參數不能使用list，因為list是Python的保留字
    for each_item in somelist:
        if isinstance(each_item, list):  # list是類型(型別)，isinstance第二個參數放的是類型(型別)
            print_nested_list(each_item)  # Recursive call
        else:
            print(each_item)


# print_nested_list(BiliBili)


# as a function

print_nested_list(somelist)
