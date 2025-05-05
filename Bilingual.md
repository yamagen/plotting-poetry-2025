# Bilingual Markdown Presentation

## Marp の「複数テーマ・複数出力戦略」で擬似的に分ける

たとえば、同じ slide.md から：

- 日本語版：marp slide.md -o slide-ja.pdf
- 英語版：marp slide.md -o slide-en.pdf

を出力する場合、以下のようにコメントベースで制御できます：

```markdown
<!-- JPN_ONLY_START -->

## このスライドは日本語だけ

これは日本語用スライドです。

<!-- JPN_ONLY_END -->

<!-- ENG_ONLY_START -->

## This slide is English only

This is for English version.

<!-- ENG_ONLY_END -->
```

## sed スライドの中に言語を混在させる

### 日本語版のマークダウンを生成

```
sed '/<!-- ENG_ONLY_START -->/,/<!-- ENG_ONLY_END -->/d' slide.md > slide-ja.md
```

### 英語版のマークダウンを生成

```
sed '/<!-- JPN_ONLY_START -->/,/<!-- JPN_ONLY_END -->/d' slide.md > slide-en.md
```

### それぞれを PDF に変換

```
marp slide-ja.md -o slide-ja.pdf
marp slide-en.md -o slide-en.pdf
```
