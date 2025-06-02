#!/usr/bin/env perl
# ディレクトリ内の.datファイルをマージするスクリプト
# ただし、1...1000.dat のように番号順に読み込む。
# マージ後のファイルは、output.dat として保存される。
#

use strict;
use warnings;
use File::Glob ':glob';
use File::Copy;
use File::Basename;
use Cwd;
my $output_file = 'output.dat';
my $current_dir = $ARGV[0]; # コマンドライン引数がなければカレントディレクトリを使用

#print "Target directory: $current_dir\n";

for (my $i = 0; $i < 1000; ) {
  $i++;
  open my $f, $current_dir . "/$i.dat", or next; # ファイルを開く
#  print "Processing file: $current_dir/$i.dat\n"; # デバッグ用に出力
  while (my $line = <$f>) {
     chomp $line;
     my @fields = split /\s+/, $line;
     next if $fields[3] > 1; # 4番目のフィールドが0でない場合はスキップ
#     printf "%0000d ",$i; 
    print $line."\n"; # ファイルの内容を出力
  }
  close $f; # ファイルを閉じる

}

#1   2         3   4  5  6  7  8                   9  10    11
#1 komachiya 0001 0 02 00 00 BG-01-3162-03-080-A 暦 こよみ 暦
#1 komachiya 0001 0 71 00 00 BG-08-0071-01-010-A の の の
#1 komachiya 0001 0 22 00 00 BG-01-1741-01-030-A 上 うえ 上
#1 komachiya 0001 0 61 00 00 BG-08-0061-03-010-A で で で
#1 komachiya 0001 0 65 00 00 BG-08-0065-07-010-A は は は
#1 komachiya 0001 0 56 00 00 BG-03-1650-01-010-A まだ まだ まだ
#1 komachiya 0001 0 02 00 00 BG-01-1632-01-140-A 十二月 じゅうにがつ 十二月
#1 komachiya 0001 0 74 55 01 BG-09-0050-01-030-A だ だ だ
#1 komachiya 0001 0 62 00 00 BG-08-0062-01-010-A と と と
#2 komachiya 0001 2 62 00 00 BG-08-0064-18-010-A と と と
#2 komachiya 0001 2 62 00 00 BG-04-1120-05-170-A -- と と
#1 komachiya 0001 0 47 21 01 BG-02-3120-01-010-A いう いう いう
# 4 が 0 ならば、ファイルを読み込む、それ以外はスキップ


#  while (my $line = <$fh>) {
#     chomp $line;
#     my @fields = split /\s+/, $line;
#     next if $fields[4] != 0; # 4番目のフィールドが0でない場合はスキップ
#     # ファイルの内容を読み込む
#     # ここでは何もしないが、必要に応じて処理を追加可能
#     print "$line\n"; # デバッグ用に出力
#   }
#   close $fh;
# }

