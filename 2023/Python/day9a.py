def batched(iterable, n=1):
    l = len(iterable)
    for ndx in range(0, l-1):
        yield iterable[ndx:ndx+n]

with open("input9.txt", 'r') as fp:
    data = fp.read()
    
sequences = data.split("\n")

all_seq = []

for sq in sequences:
    original = list(map(int, sq.split()))
    out = [original.copy()]
    current_sq = original.copy()
    each = []
    while set(each) != {0}:
        each.clear()
        #print(current_sq)
        for idx in batched(current_sq, n=2):
            print(idx)
            if len(idx) == 2:
                #print(idx[0], idx[1], "Here I am")
                each.append(idx[1] - idx[0])
            else:
                #print(idx[0], "Here I am")
                each.append(0)
        #print(each)
        out.append(each.copy())
        current_sq = each.copy()
    
    all_seq.append(tuple(out))
    
print(all_seq)

def find_answer1(all_seq):
    answer = 0
    for seq in all_seq.copy():
        for i, idx in enumerate(seq[::-1]):
            if i == 0:
                idx.append(0)
            elif i == len(seq) - 1:
                answer += idx[-1] + seq[::-1][i-1][-1]
                idx.append(idx[-1] + seq[::-1][i-1][-1])
            else:
                idx.append(idx[-1] + seq[::-1][i-1][-1])
            print(idx, end=" ")
        print()

    return answer

def find_answer2(all_seq):
    answer = 0
    for seq in all_seq.copy():
        for i, idx in enumerate(seq[::-1]):
            if i == 0:
                idx.insert(0, 0)
            elif i == len(seq) - 1:
                idx.insert(0, idx[0] - seq[::-1][i-1][0])
                answer += idx[0]
            else:
                idx.insert(0, idx[0] - seq[::-1][i-1][0])
            print(idx, end=" ")
        print()
        
        return answer

# answer1 = find_answer1(all_seq)
answer2 = find_answer2(all_seq)
print(answer2)
