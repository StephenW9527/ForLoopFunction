

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


# writing in a specific case
for each_thing in outside_list:  # in this case, BiliBili as outside_list
    # check if each_thing is a list
    if isinstance(each_thing, list):
        for nested_thing in each_thing:
            if isinstance(nested_thing, list):
                for inner_thing in nested_thing:
                    if isinstance(inner_thing, list):
                        for deepest_thing in inner_thing:
                            print(deepest_thing)
                    else:
                        print(inner_thing)
            else:
                print(nested_thing)
    else:
        print(each_thing)


# as a recursion function (general case form)
def print_nested_list(somelist):  # 參數不能使用list，因為list是Python的保留字
    for each_item in somelist:
        if isinstance(each_item, list):  # list是類型(型別)，isinstance第二個參數放的是類型(型別)
            print_nested_list(each_item)  # Recursive call
        else:
            print(each_item)


print_nested_list(somelist)
# Call the function with somelist
