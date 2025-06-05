def clean_word(word):
    return word.rstrip('*').strip(" \n\r'\"") if word else word

def parse_nodes(lines, prefix):
    nodes = []
    for line in lines:
        if prefix not in line:
            continue
        cols = [clean_word(w) for w in line.rstrip('\n').split()]
        subord = int(cols[3])
        bg = None
        for c in cols:
            if c.startswith('BG-'):
                bg = c
        forms = [w for w in cols[-3:]]
        nodes.append({'bg': bg, 'forms': forms, 'label': cols[-1], 'subord': subord})
    return nodes

def bg_head(bg_code, level=13):
    if not bg_code or not bg_code.startswith('BG-'):
        return None
    parts = bg_code.split('-')
    if level == 13:
        return '-'.join(parts[:4])
    elif level == 17:
        return '-'.join(parts[:5])
    else:
        return '-'.join(parts)

with open("test2.txt", encoding="utf-8") as f:
    lines = f.readlines()

KW_nodes = parse_nodes(lines, "KW")
KANEKO_nodes = parse_nodes(lines, "kaneko")

LEVELS = [17, 13]
output_bgs = set()
mapping = {}

# BGごとに一度だけ出力
for ka in KANEKO_nodes:
    bg = ka['bg']
    if bg in output_bgs:
        continue

    # 1. subord=0（通常語）
    zero_kaneko = [k for k in KANEKO_nodes if k['bg'] == bg and k['subord'] == 0]
    if zero_kaneko:
        label = zero_kaneko[0]['label']
        found = []
        for level in LEVELS:
            ka_head = bg_head(bg, level)
            normal_labels = [kw['label'] for kw in KW_nodes
                             if ka_head and bg_head(kw['bg'], level) == ka_head and kw['subord'] == 0]
            if normal_labels:
                found = normal_labels
                break
        mapping[label] = sorted(list(set(found)))
        output_bgs.add(bg)
        continue

    # 2. subord=1,3セット
    one_kaneko = [k for k in KANEKO_nodes if k['bg'] == bg and k['subord'] == 1]
    if one_kaneko:
        label1 = one_kaneko[0]['label']
        if ka['label'] == label1 or ka['label'] in one_kaneko[0]['forms']:
            # 1で一致
            found = []
            for level in LEVELS:
                ka_head = bg_head(bg, level)
                parent_labels = [kw['label'] for kw in KW_nodes
                                 if ka_head and bg_head(kw['bg'], level) == ka_head and kw['subord'] == 1]
                if parent_labels:
                    found = parent_labels
                    break
            mapping[label1] = sorted(list(set(found)))
            output_bgs.add(bg)
            continue
        # 3で一致
        three_kaneko = [k for k in KANEKO_nodes if k['bg'] == bg and k['subord'] == 3]
        found_label = None
        for k3 in three_kaneko:
            if ka['label'] == k3['label'] or ka['label'] in k3['forms']:
                found_label = k3['label']
                break
        if found_label:
            found = []
            for level in LEVELS:
                ka_head = bg_head(bg, level)
                child_labels = [kw['label'] for kw in KW_nodes
                                if ka_head and bg_head(kw['bg'], level) == ka_head and kw['subord'] == 3]
                if child_labels:
                    found = child_labels
                    break
            mapping[found_label] = sorted(list(set(found)))
            output_bgs.add(bg)
            continue

    # 3. subord=2（代替語）: すべて順に語一致を探す
    two_kaneko = [k for k in KANEKO_nodes if k['bg'] == bg and k['subord'] == 2]
    found_label = None
    for k2 in two_kaneko:
        if ka['label'] == k2['label'] or ka['label'] in k2['forms']:
            found_label = k2['label']
            break
    if found_label:
        found = []
        for level in LEVELS:
            ka_head = bg_head(bg, level)
            alt_labels = [kw['label'] for kw in KW_nodes
                          if ka_head and bg_head(kw['bg'], level) == ka_head and kw['subord'] == 2]
            if alt_labels:
                found = alt_labels
                break
        mapping[found_label] = sorted(list(set(found)))
        output_bgs.add(bg)
        continue

# 出力
for k, v in mapping.items():
    print(f"{k}\t-->\t{v}")
