"""Docstring"""
def main():
    """Woah! HTML is not a programming languages!?"""
    html = input()
    started = True
    result = ""
    result_list = []
    for txt in html:
        if txt == "<":
            if result:
                result_list.append(result.strip())
                result = ""
            started = False
            continue
        if txt == ">":
            started = True
            continue
        if started:
            if txt == " ":
                if result:
                    result_list.append(result)
                    result = ""
                continue
            result += txt
    if result:
        result_list.append(result)
        result = ""
    print(result_list)
main()
