from collections import defaultdict

def check_update(rules:dict,update_sequence:list[int]) -> bool:
    sequence_stack: list = [] 
    for page in update_sequence:
        p_rules = rules[page]
        for r in p_rules:
            if r in sequence_stack:
                return False
        sequence_stack.append(page)
    
    return True

def main():
    fn = "input_all.txt"
    rules = defaultdict(list)
    updates = []
    with open(fn) as file:
        while l:=file.readline():
            if "|" in l:
                k,v = l.split("|")
                rules[int(k)].append(int(v))
            elif "," in l:
                updates.append([int(s) for s in l.strip().split(",")])
    
    mid = 0
    counts = 0  
    for u in updates:
        res = check_update(rules=rules, update_sequence=u)
        if res:
            mid += u[len(u)//2]

    print(mid)
main()