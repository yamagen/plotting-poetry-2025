def clean_word(word):
    return word.rstrip('*').strip(" \n\r'\"") if word else word

def parse_nodes(lines, prefix):
    nodes = []
    for line in lines:
        if prefix not in line:
            continue
        cols = [clean_word(w) for w in line.rstrip('\n').split()]
        group_id = cols[0]          # 行頭番号
        author = cols[1]            # 翻訳者名 (kanekoなど)
        waka_number = cols[2]       # 和歌番号 (KW000005など)
        priority_level = int(cols[4])
        bg = next((c for c in cols if c.startswith('BG-')), None)
        label = cols[-1]
        nodes.append({
            'group_id': group_id,
            'author': author,
            'waka_number': waka_number,
            'priority_level': priority_level,
            'bg': bg,
            'label': label,
        })
    return nodes

def bg_head(bg_code, level=13):
    if not bg_code or not bg_code.startswith('BG-'):
        return None
    parts = bg_code.split('-')
    if level == 17:
        return '-'.join(parts[:5])
    else:
        return '-'.join(parts[:4])

def get_search_priorities(kp):
    if kp == 0:
        return [0, 2]
    elif kp == 1:
        return [1, 3]
    elif kp == 2:
        return [2]
    elif kp == 3:
        return [3]
    else:
        return [kp]

with open("test2.txt", encoding="utf-8") as f:
    lines = f.readlines()

source_entries = parse_nodes(lines, "kaneko")
target_entries = parse_nodes(lines, "KW")

aggregation = {}

for se in source_entries:
    # group_idでKW絞り込み
    kw_candidates = [te for te in target_entries if te['group_id'] == se['group_id']]
    prios = get_search_priorities(se['priority_level'])

    found = []
    found_waka_numbers = set()
    for level in [17, 13]:
        for prio in prios:
            for te in kw_candidates:
                if te['priority_level'] == prio and bg_head(te['bg'], level) == bg_head(se['bg'], level):
                    found.append(te['label'])
                    found_waka_numbers.add(te['waka_number'])
            if found:
                break
        if found:
            break

    key = (se['waka_number'], se['label'], tuple(sorted(set(found))))
    if key not in aggregation:
        aggregation[key] = {
            'authors': set(),
            'waka_numbers': set(),
            'label': se['label'],
            'translations': sorted(set(found)),
        }
    aggregation[key]['authors'].add(se['author'])
    aggregation[key]['waka_numbers'].update(found_waka_numbers)

for key, data in aggregation.items():
    waka_num, label, trans = key
    authors = ','.join(sorted(data['authors']))
    waka_nums = ','.join(sorted(data['waka_numbers'])) if data['waka_numbers'] else 'なし'
    print(f"{waka_num} {authors} {label}\t-->\t{list(trans)}")
