from collections import defaultdict

def order_u(rules:dict, update_sequence:list[int]) -> list[int]:

    original_seq = update_sequence.copy()
    i = 0
    sequence_stack = []
    while i < len(original_seq):
            page = update_sequence[i]
            p_rules = rules[page]
            j = 0
            while j < len(p_rules):
                if p_rules[j] in sequence_stack:
                    # swap with i-1
                    prev = update_sequence[i-1]
                    curr = update_sequence[i]
                    update_sequence[i-1] = curr
                    update_sequence[i] = prev
                    sequence_stack.clear()
                    i = 0
                    break
                j += 1
            sequence_stack.append(page)
            i += 1
                    
    return update_sequence

def check_update(rules:dict,update_sequence:list[int]) -> bool:
    sequence_stack: list = [] 
    for page in update_sequence:
        p_rules = rules[page]
        for r in p_rules:
            if r in sequence_stack:
                return True
        sequence_stack.append(page)
    
    return False

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
            ordered_u = order_u(rules=rules,update_sequence=u)
            mid += ordered_u[len(ordered_u)//2]
    print(mid)
main()