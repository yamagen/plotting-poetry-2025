---
marp: true
theme: default
paginate: true
backgroundColor: "#f5f5dc"
color: "#333"
---

### Plotting Poetry 2025

# <span class="red">Transforming Poetic Thought into Waka:</span>

### How to Pack the Skeleton into a 31-Syllable Closet

- Bor Hodošček, <span class="blue">The University of Osaka</span>
- Hilofumi Yamamoto, <span class="blue">Institute of Science Tokyo</span>

![thought2waka](./images/thought2waka01.png)

---

## Project Goals

- Reverse-engineer modern interpretations into waka
- Identify compression patterns for poetic thought
- Explore constraints and expression in 31-mora form

---

## Basics of WAKA

### **Japanese Song (Poem)**

- WA &rarr; Japanese / Japanese style
- KA &rarr; Song

---

### **Early Established Waka**

- The Man'yoshu: est. around 7th -- 8th century in Chinese notation.
- The Kokinshu: est. ca. 905 in Japanese notation.

---

### **Style and Rhetorics**

<!-- JPN_ONLY_START
- Only 31 syllables with 5,7,5,7,7 sounds
- JPN:自然や感情を簡潔に表現する特徴
- 掛詞、枕詞、序詞
JPN_ONLY_END -->

- Include only 31 syllables with 5,7,5,7,7 sounds
- Express natural views and emotions in a simple sentence.
- Use of rhetorics to create a poetic atmosphere:
  - Pun (kakekotoba),
  - Pillow words (makurakotoba), and
  - Introductory words (jo-kotoba)

---

## Poetic Rules may include:

- Omission of grammatical elements
- Inversion of word order
- Symbolic substitutionk
- Nominalization
- Manipulation of ambiguity
- Compression of meaning
- Expansion of meaning
- Reinterpretation of context
  ...

<!-- JPN_ONLY_START

\ifJPN
本研究の目的は、現代日本語訳を和歌の厳格な31音の形式に圧縮するために使用される詩的戦略を特定し、分類することである。
詩的思考が31音の厳格な構造に変形される過程を分析することで、そのような変換を可能にする根本的なルール（明示的および暗黙的）を明らかにしようとする。
これらのルールには、文法要素の省略、語順の逆転、象徴的な置換、名詞化、曖昧さの操作などが含まれる可能性がある。
\else
This study aims to identify and classify the poetic strategies used to compress expansive modern Japanese translations into the condensed form of waka poetry.
By analyzing how poetic thought is transfigured into the rigid structure of a 31-syllable tanka, we seek to uncover the underlying rules—both overt and covert—that make such transformation possible.
These rules may include omission of grammatical elements, inversion of word order, symbolic substitution, nominalization, and manipulation of ambiguity.
\fi

JPN_ONLY_END -->

---

## Material

- A) Kokinshu: a collection of 1000 waka poems
- B) Modern Japanese translations: 10 sets of translations

Parallel corpus of 1000 waka and 10 modern Japanese translations

---

## Computer programms

- Align waka with contemporary paraphrases
- Use phrase gloss and structured data
- Analyze rule types and transformation limits

---

## Challenges

- Literal vs. interpretive gaps
- Compression loss in reverse mapping
- Ambiguity in source expressions

---

## Toward a Model

- Create typology of transformation rules
- Visualize linguistic constraints
- Evaluate poetic fidelity and transformation cost

---

## Methods

- Using a parallel corpus of waka and modern Japanese translations
- Align waka with contemporary paraphrases
- Use phrase gloss and structured data
- Analyze rule types and transformation limits
- Identify compression patterns for poetic thought

---

### Steps

1. Calculating of the frequency of the conversion patterns
2. Clustering of the conversion patterns:
   - Grammatical, Lexical, Structural, Rhetorical etc.
3. Modeling of the conversion patterns:
   - Rule based, Statistical based etc.

<!-- JPN_ONLY_START
1. 高頻度の変換ルールをリストアップ
- 1000首×10訳 = 1万件 の現代語訳があるため、まず高頻度の変換パターンを抽出
  例: 「～してしまった」→「～にけり」が頻繁に出現するか？
- 形態素解析を用いて、文法変化のパターン を統計的に分析

2. 変換パターンのクラスタリング

- 文法変換（助詞の変更、動詞の時制変化）
- 語彙変換（現代語 → 和歌語彙）
- 構造変換（主語の省略、語順の変更）
- 修辞技法（掛詞、縁語、比喩など）

3. 変換ルールを機械学習でモデル化できるか検討

- ルールベースの変換モデル（決定木やルールマイニング）
- 統計的手法（n-gram分析で和歌に特徴的な表現を抽出）

JPN_ONLY_END -->

---

## Results

- Identify and classify poetic strategies
- Analyze how poetic thought is transfigured
- Uncover underlying rules (overt and covert)
- Explore the implications of compression
- Simulate the transformation process:

---

## Discussion

- Explore poetic compression in modern Japanese
- Analyze constraints in poetic expression
- Discuss implications for translation and interpretation
- Consider cultural and linguistic factors

---

## Conclusion

- Waka as a lens for poetic thought
- Compression as a creative constraint
- Future research directions
- Implications for translation studies

---

### Conclusion

- Content of the work is impressive
- Author's skill is impressive as well

<!-- JPN_ONLY_START
作品を通して、和歌は詩的思考のレンズとして機能し、圧縮は創造的な制約として機能することを示す。
作品の内容のすごさを感じるだけでなく、作者のすごさも感じることができる。
JPN_ONLY_END -->
