

BiliBili = [
    "Anchor",
    ["Cat_Was_Born_In_Summer", "Fox_With_9_Tails",
        ["SevenHills", "During", "Dough"]]]


# for characters in BiliBili:
#     if isinstance(characters, list):
#         for host in characters:
#             if isinstance(host, list):
#                 for husbands in host:
#                     print("Darlings:", husbands)

#             else:
#                 print("host:", host)

#     else:
#         print("roles:", characters)


# writing with recursion function
def print_nested_list(somelist):  # 参数不能使用list，因为list是Python的保留字
    for each_item in somelist:
        if isinstance(each_item, list):
            print_nested_list(each_item)  # Recursive call
        else:
            print(each_item)


print_nested_list(BiliBili)
