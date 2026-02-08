import json

def isIntersect(a, b, c):
    a = set(json.loads(a))
    b = set(json.loads(b))
    c = set(json.loads(c))
    
    for i in a:
        if i in b:
            for x in c:
                if i in c:
                    return True
    return False
            

print(isIntersect(input(),input(),input()))