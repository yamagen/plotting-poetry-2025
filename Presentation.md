# 🖥️ CLIで完結するプレゼン環境構築メモ – Marp × GitHub Pages

## ✅ 本日の構築内容

Neovim + Marp CLI + GitHub CLI を組み合わせることで、以下のような理想的なプレゼンテーション環境が完成：

- スライドの作成：**Markdown（Neovim）**
- スライドの変換：**Marp CLI**
- 公開：**GitHub Pages（gh CLI）**
- フルスクリーン発表：**ブラウザから直接可能**
- 配布用PDF：`marp slide.md -o slide.pdf`

---

## 🎯 このシステムが「すごい」理由

| 機能                   | 説明                                                       |
| ---------------------- | ---------------------------------------------------------- |
| ✅ バージョン管理      | git + GitHub により、すべての変更を履歴管理できる          |
| 🌐 公開と共有          | GitHub Pages で即座に Web 発表可能（URL 一つ）             |
| 🖼️ デザインと軽さ      | Reveal.js に匹敵するデザイン性、かつ軽量                   |
| 📝 プレゼン = Markdown | 思考整理・修正がしやすいテキストベース                     |
| 📄 PDFも即作成         | `marp slide.md -o slide.pdf` で配布用PDF化                 |
| 🔗 他資料との連携      | AEAD、伊勢物語、土佐日記などの gloss や JSONと連携しやすい |
| 🚀 完全CLI駆動         | GUI不要、エディタとターミナルで完結                        |

---

## 💡 Marp スライドのキーバインド（発表中）

| キー      | 効果                      |
| --------- | ------------------------- |
| `F`       | フルスクリーン            |
| `→` / `↓` | 次のスライドへ            |
| `←` / `↑` | 前のスライドへ            |
| `O`       | 一覧表示                  |
| `S`       | 話者メモ（speaker notes） |
| `ESC`     | フルスクリーン解除        |

---

## 🧪 Firefox vs Chrome 出力の違い

- Marp CLI の PDF出力は Chromium 推奨。
- Firefox でも出力可能だが、細かなレイアウト違いが出ることがある。
- 対応コマンド例（Chromiumを明示）：
  ```bash
  CHROME_PATH="/usr/bin/google-chrome-stable" marp slide.md -o slide.pdf
  ```

## 🧵 コメント

このプレゼン環境は、CLI・Markdown・オープン共有の価値を重視する研究者にとって、まさに理想の公開スタイル。
構築されたシステムは、発表・配布・保管・共有のすべてを一元化し、未来の学会発表の標準形を先取りしている。

## 📝 今後のTODO

- README.md への要旨・リンク追加
- slide.pdf を GitHub に同時公開（必要に応じて）
- 必要なら LICENSE のバナー画像再確認
