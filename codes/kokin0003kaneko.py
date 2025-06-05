import matplotlib.pyplot as plt
import networkx as nx

# 日本語→英語 対応表
jp_to_en = {
    'うめ': 'plum',
    'え': 'branch',
    'きゐる': 'perch',
    'うぐひす': 'warbler',
    'はる': 'spring',
    '心': 'heart',
    '寄せる': 'lean-to',
    '慕う': 'yearn',
    'なお': 'still',
    'まだ': 'not-yet',
    '雪': 'snow',
    'ゆき': 'snow',
    'ふる': 'fall',
    '繰り返す': 'repeat',
}

# 元データ（日本語ノード）
CT_nodes = ['うめ', 'え', 'きゐる', 'うぐひす', 'はる', '心', '寄せる', '慕う', 'なお', 'まだ', '雪', 'ふる', '繰り返す']
OP_nodes = ['うめ', 'え', 'きゐる', 'うぐひす', 'はる', 'ゆき', 'ふる']

aggregation_map = {
    'きゐる': ['心', '寄せる', '慕う'],
    'ゆき': ['なお', 'まだ', '繰り返す']
}

# ノード名を英語化
CT_nodes_en = [jp_to_en.get(n, n) for n in CT_nodes]
OP_nodes_en = [jp_to_en.get(n, n) for n in OP_nodes]
aggregation_map_en = {jp_to_en.get(k, k): [jp_to_en.get(n, n) for n in v] for k, v in aggregation_map.items()}

G = nx.DiGraph()

for i in range(len(CT_nodes_en) - 1):
    G.add_edge(CT_nodes_en[i], CT_nodes_en[i+1], style='dotted')

for i in range(len(OP_nodes_en) - 1):
    G.add_edge(OP_nodes_en[i], OP_nodes_en[i+1], style='solid')

for agg, absorbed_list in aggregation_map_en.items():
    for absorbed in absorbed_list:
        G.add_edge(absorbed, agg, style='dashed')

pos = {}
y_ct = 2
y_op = 1
for i, n in enumerate(CT_nodes_en):
    pos[n] = (i, y_ct)
for i, n in enumerate(OP_nodes_en):
    pos[n] = (i, y_op)

plt.figure(figsize=(14, 4))

solid_edges = [(u, v) for u, v, d in G.edges(data=True) if d['style']=='solid']
dotted_edges = [(u, v) for u, v, d in G.edges(data=True) if d['style']=='dotted']
dashed_edges = [(u, v) for u, v, d in G.edges(data=True) if d['style']=='dashed']

nx.draw_networkx_nodes(G, pos, node_size=2000, node_color='lightyellow', edgecolors='gray')
nx.draw_networkx_labels(G, pos, font_family='sans-serif', font_size=10)
nx.draw_networkx_edges(G, pos, edgelist=solid_edges, width=3, edge_color='mediumblue')
nx.draw_networkx_edges(G, pos, edgelist=dotted_edges, width=1, edge_color='gray', style='dotted')
nx.draw_networkx_edges(G, pos, edgelist=dashed_edges, width=2, edge_color='orangered', style='dashed')

plt.axis('off')
plt.title('Node Aggregation: CT (upper, thin) → OP (lower, thick)\nRed dashed = aggregation', fontsize=10, fontname='sans-serif')
plt.tight_layout()
plt.show()
