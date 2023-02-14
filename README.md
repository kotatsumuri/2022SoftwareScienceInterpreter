# 2022SoftwareScienceInterpreter

これは筑波大学の GB27001 ソフトウェアサイエンス特別講義 A の水島先生の課題で作成した簡単なプログラミング言語です。

## 仕様

このプログラミング言語では以下のようなことができます。

- 四則演算
- 比較演算
- 変数定義
- 変数呼び出し
- if 文
- while 文
- 関数定義
- 関数呼び出し
- Print

## 文法

※ 以下空白や改行は省略せずに

### 四則演算

- 足し算 : `1 + 2`
- 引き算 : `1 - 2`
- 掛け算 : `1 * 2`
- 割り算 : `1 / 2`
- 剰余 : `1 % 2`
- 結合 : `2 * (1 + 2)` == `2 * 3` == `6`
- 負数 : `-1`, `-123`

四則演算は計算結果を返す

### 比較演算

- 等号 : `==`
- 不等号 : `!=`
- 大なり : `>`
- 小なり : `<`
- 大なりイコール : `>=`
- 小なりイコール : `<=`
- AND : `&`
- OR : `|`

比較演算は True(1)または False(0)を返す

### 変数定義

`変数名 = 定義`

#### 例

```
one = 1
two = 2
```

変数定義は変数の値を返す

### 変数呼び出し

`変数名`

#### 例

```
one = 1
one = one + 2
```

これで`one == 3`となる

### if 文

```
if 条件文
    処理1
else
    処理2
end

if 条件文
    処理
end
```

#### 例

```
i = 12123134022
if i % 2 == 0
    i = i + 1
else
    i = i - 1
end
```

if 文は条件文が True の場合は、処理 1 の最後の処理が返した値を返す。
else がある場合で、False の場合は処理 2 の最後の処理が返した値を返す。
else がない場合は、0 を返す。

### while 文

```
while 条件文
    処理
end
```

#### 例

```
i = 1
sum = 0
while i <= 10
    sum = sum + i
    i = i + 1
end
```

while 文は処理のうち、最後のループでの処理内の最後の処理が返した値を返す。

### 関数定義

```
fn 関数名 ( 変数1, 変数2, ..., 変数n )
    処理
end
```

例

```
fn fib ( n )
    if n == 0 | n == 1
        1
    else
        fib ( n - 1 ) + fib ( n - 2 )
    end
end
```

関数は、関数内の処理で最後に行われた処理が返した値を返す。
例の場合、n == 1 or n == 2 の時は 1 を返し、それ以外の場合は`fib ( n - 1 ) + fib ( n - 2 )`を返す。

### 関数呼び出し

```
関数名 ( 変数1, 変数2, ..., 変数n )
```

### Print

```
Print 処理
```

#### 例

```
fn fib ( n )
    if n == 0 | n == 1
        1
    else
        fib ( n - 1 ) + fib ( n - 2 )
    end
end

i = 0

while i < 10
    print fib ( i )
    i = i + 1
end
```

##### 出力

```
1
1
2
3
5
8
13
21
34
55
```

##　実行方法

```
python exec.py コードファイル名
```

※ python のバージョンは 3.10 以上を使用してください

## ディレクトリ構成

```
.
├── README.md
├── exec.py // 実行コード
├── fib // サンプルコード
├── src // 実装コード
│   ├── expression // 表現実装コード
│   │   ├── Assignment.py // 変数定義
│   │   ├── BinExpr.py // 四則演算 & 比較演算
│   │   ├── Call.py // 関数呼び出し
│   │   ├── Expr.py // 基底クラス
│   │   ├── Func.py // 関数定義
│   │   ├── Ident.py // 変数呼び出し
│   │   ├── If.py // if文
│   │   ├── Int.py // 定数
│   │   ├── Print.py // print文
│   │   ├── Seq.py // 連接
│   │   └── While.py // while文
│   └── parser //　構文解析コード
│       ├── AssignmentParser.py // 変数定義の細かい構文解析
│       ├── BinExprParser.py // 四則演算 & 比較演算の細かい構文解析
│       ├── interpreter.py // 行分割 & トークン分割
│       └── parser.py // 全体の構文解析
└── test // テストコード
    ├── testAssignment.py
    ├── testAssignmentParser.py
    ├── testBinExpr.py
    ├── testBinExprParser.py
    ├── testFuncCall.py
    ├── testFuncParser.py
    ├── testIdent.py
    ├── testIf.py
    ├── testIfParser.py
    ├── testInt.py
    ├── testSeq.py
    ├── testWhile.py
    └── testWhileParser.py
```
