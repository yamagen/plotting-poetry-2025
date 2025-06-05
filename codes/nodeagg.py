import re


def clean_word(word):
    return word.rstrip('*') if word else word

def parse_nodes(lines, header):
    nodes = []
    in_block = False
    for line in lines:
        if line.strip().startswith(header):
            in_block = True
            continue
        if in_block:
            if line.strip() == '' or re.match(r'^[A-Z]{2}\s', line):
                break
            cols = line.strip().split()
            # BGコード, かな, 漢字
            bg = None
            kana = None
            kanji = None
            for c in cols:
                if c.startswith('BG-'):
                    bg = c
            if len(cols) >= 2 and cols[-2] != '--':
                kana = clean_word(cols[-2])
            else:
                kana = None
            kanji = clean_word(cols[-1])
            if re.match(r'^[、。,]$', kanji):
                continue
            nodes.append({'bg': bg, 'kana': kana, 'kanji': kanji})
    return nodes

def bg_head(bg_code, level=13):
    # BGコードを「-」区切りでN要素切り出し
    if not bg_code or not bg_code.startswith('BG-'):
        return None
    parts = bg_code.split('-')
    # level=13ならBG-08-0064-04
    # level=17ならBG-08-0064-04-050
    if level == 13:
        return '-'.join(parts[:4])
    elif level == 17:
        return '-'.join(parts[:5])
    else:
        return '-'.join(parts)

with open("test.txt", encoding="utf-8") as f:
    lines = f.readlines()

CT_nodes = parse_nodes(lines, "CT")
OP_nodes = parse_nodes(lines, "OP")

# BGコードのレベルを指定（13 or 17など）
BG_LEVEL = 13  # ←必要に応じて変更

mapping = {}
for ct in CT_nodes:
    candidates = []
    for op in OP_nodes:
        # (a) 漢字一致
        if ct['kanji'] == op['kanji']:
            candidates.append(op['kanji'])
            continue
        # (b) かな一致
        if ct['kana'] and op['kana'] and ct['kana'] == op['kana']:
            candidates.append(op['kanji'])
            continue
        # (c) BGコード（指定レベルまで）一致
        if ct['bg'] and op['bg']:
            if bg_head(ct['bg'], BG_LEVEL) == bg_head(op['bg'], BG_LEVEL):
                candidates.append(op['kanji'])
                continue
    # 重複除去・順序保持
    uniq = []
    [uniq.append(x) for x in candidates if x not in uniq]
    mapping[ct['kanji']] = uniq

for k, v in mapping.items():
    print(f"{k}\t-->\t{v}")
