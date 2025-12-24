"""Docstring"""
def main():
    """You're next!"""
    num = int(input())
    members = ""
    current_user = 1
    for _ in range(num):
        name = input()
        members += name+"#"
    for i in members:
        if i == "#":
            if current_user >= num:
                members = members.replace("#","_"+str(current_user),1)
                break
            if current_user%2:
                members = members.replace("#","*"*current_user,1)
            else:
                members = members.replace("#","-"*current_user,1)
            current_user += 1
    print(members)
main()
