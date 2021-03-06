# -*- encoding: utf-8 -*-
"""
単語グループの定義
"""
groups = [
# 言語や処理系
"""Python, Perl, PHP, Ruby, JavaScript, C, C++, C#, CLR, Java Script,
   Java, OCaml, LISP, Lisp, Scala, Groovy, Haskell, Smalltalk, Squeak, awk, sed, COBOL, Fortran,
   Tcl, Tk, Tck/Tk, Erlang, Prolog, PCRE, Clojure, Scheme, FORTRAN, Gauche, JRuby, Jython, IronPython, CPython,
   MRI, YARV, Ada, ALGOL, VBA, Pascal, Delphi, Eiffel, Algol, B, BCPL, R, J, Groovy, Prolog,
   Rhino, Selenium, ML, Scheme, Lua, CoffeeScript, ksh, csh, grep, APL, ColdFusion, Flash,
   VisualBasic, BASIC, Basic, IDL, VBA, Dreamweaver, BPQL, UML, DTML, HTML, SGML, SML, RPG, SQL,
   なでしこ, ドリトル, JSX, Haxe""",

# プログラミング関連用語
"""クラス, トレイト, インターフェイス, 継承, オーバーライド, インスタンス, オブジェクト,
ミックスイン, デリゲート, プロパティ, 属性, フィールド,
""",

"""goto, continue, break, rescue, redo, while, until, if, return, try, catch, except, finally,
""",

"""class, interface, extends, import, implements, public, protected, friend, private, Override,
""",

"""関数, サブルーチン, メソッド, クロージャ, マクロ, ルーチン, 無名関数, 関数呼出し,
""",

"""ライブラリ, モジュール,
""",

"""グローバル, 大域, スコープ, レキシカル, 動的, 静的,
""",

"""コルーチン, ファイバー, スレッド, 協調的, マルチタスク,
""",

"""
イテレータ, リスト, タプル, 配列, コレクション, ストリング, 辞書, ベクタ, アレイ,
""",

# OS
"""Fedora, RedHat, CentOS, RHEL, Ubuntu, Debian, FreeBSD, Xen, Windows, Macintosh, MacOS, MacOSX,
Solaris, NetBSD, Gentoo, SUSE, Sarge, OpenBSD, KVM, VMWare, Vista, Mac, Mandrake, Miracle, Kondara, TOMOYO,
TRON, ITron, BTRON, AIX, Turbo,
Panther, Tiger, Leopard, Lion, Mavericks,
95, 98, 2000, Me, XP, NT
""",

# DB
"""PostgreSQL, MySQL, MongoDB, SQLite, PostGIS, HBase, Hive, Jubatas, NoSQL, KVS, memcached, Redis,
""",

# machine
"""iPhone, iPad, Nexus, MacBook, MBA, Nokia, PSP, PS2, PS3, Symbian,
""",

# server
"""
apache, nginx, memcached, lighttpd, lighttpd, OpenLDAP, Asterisk, Apache,
""",

# command / user
"""
mkdir, ln, ls, cd, mv, cp, rm, chmod, chown, chroot, su, sudo, root, nobody, ssh, scp, git, hg, svn, cvs,
""",

"""
Tapestry, Django, Zope, Rails,
""",

"""
Word, Excel, PowerPoint, Photoshop, Illustrator, InDesign, Fireworks, Pages, Numbers, Access,
""",

"""条件分岐, 代入, 変数, 束縛,
   XPCOM, データモデル, 派生型, 抽象型,
   スライシング, ガベージコレクション, 複文, ガード,
   束縛, 加算, 減算, インクリメント, デクリメント, 四捨五入, 切り捨て,
   スカラー,
   ブレス, アロケート, クオート, スコープチェーン,
   ライブラリ, パッケージ, モジュール, ユーティリティ, ドライバ, プラグマ, 添字,
   CORBA, DCOM, COM, WebSphere, .NET, RubyGems
""",

]

for i, g in enumerate(groups):
    words = [x.strip() for x in g.split(',')]
    groups[i] = words
