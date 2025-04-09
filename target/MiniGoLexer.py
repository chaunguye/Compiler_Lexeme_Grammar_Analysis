# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2?")
        buf.write("\u01e6\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\3\2\3\2\3\2\3\2\7\2\u008c\n\2\f\2\16\2\u008f\13\2\3")
        buf.write("\2\3\2\3\3\3\3\3\3\3\3\3\3\7\3\u0098\n\3\f\3\16\3\u009b")
        buf.write("\13\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\7\4\u00a6\n")
        buf.write("\4\f\4\16\4\u00a9\13\4\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32")
        buf.write("\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3")
        buf.write("$\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3")
        buf.write(")\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3")
        buf.write("\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\7\65\u0160")
        buf.write("\n\65\f\65\16\65\u0163\13\65\3\65\3\65\3\65\3\65\6\65")
        buf.write("\u0169\n\65\r\65\16\65\u016a\3\65\3\65\3\65\6\65\u0170")
        buf.write("\n\65\r\65\16\65\u0171\3\65\3\65\3\65\6\65\u0177\n\65")
        buf.write("\r\65\16\65\u0178\5\65\u017b\n\65\3\66\6\66\u017e\n\66")
        buf.write("\r\66\16\66\u017f\3\66\3\66\7\66\u0184\n\66\f\66\16\66")
        buf.write("\u0187\13\66\3\66\5\66\u018a\n\66\3\67\3\67\7\67\u018e")
        buf.write("\n\67\f\67\16\67\u0191\13\67\3\67\3\67\3\67\38\38\58\u0198")
        buf.write("\n8\39\39\39\3:\3:\7:\u019f\n:\f:\16:\u01a2\13:\3:\3:")
        buf.write("\3:\5:\u01a7\n:\3:\3:\3;\3;\7;\u01ad\n;\f;\16;\u01b0\13")
        buf.write(";\3;\3;\3;\3;\3;\3<\3<\3=\3=\5=\u01bb\n=\3=\6=\u01be\n")
        buf.write("=\r=\16=\u01bf\3>\3>\3>\3>\3>\3>\3>\3>\3>\5>\u01cb\n>")
        buf.write("\3?\3?\3?\3?\3@\3@\7@\u01d3\n@\f@\16@\u01d6\13@\3A\3A")
        buf.write("\3A\5A\u01db\nA\3B\6B\u01de\nB\rB\16B\u01df\3B\3B\3C\3")
        buf.write("C\3C\4\u0099\u00a7\2D\3\3\5\4\7\2\t\5\13\6\r\7\17\b\21")
        buf.write("\t\23\n\25\13\27\f\31\r\33\16\35\17\37\20!\21#\22%\23")
        buf.write("\'\24)\25+\26-\27/\30\61\31\63\32\65\33\67\349\35;\36")
        buf.write("=\37? A!C\"E#G$I%K&M\'O(Q)S*U+W,Y-[.]/_\60a\61c\62e\63")
        buf.write("g\64i\65k\66m\67o\2q\2s8u9w\2y\2{:};\177<\u0081=\u0083")
        buf.write(">\u0085?\3\2\23\4\2\f\f\17\17\3\2\63;\4\2DDdd\3\2\62\63")
        buf.write("\4\2QQqq\3\2\629\4\2ZZzz\5\2\62;CHch\4\2$$^^\7\2$$^^p")
        buf.write("pttvv\3\3\f\f\3\2\62;\4\2GGgg\4\2--//\5\2C\\aac|\6\2\62")
        buf.write(";C\\aac|\5\2\13\13\17\17\"\"\2\u01fa\2\3\3\2\2\2\2\5\3")
        buf.write("\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2")
        buf.write("\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2")
        buf.write("\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2")
        buf.write("!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2")
        buf.write("\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3")
        buf.write("\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2")
        buf.write("\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2")
        buf.write("\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2")
        buf.write("\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3")
        buf.write("\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c")
        buf.write("\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2")
        buf.write("m\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2")
        buf.write("\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085")
        buf.write("\3\2\2\2\3\u0087\3\2\2\2\5\u0092\3\2\2\2\7\u00a1\3\2\2")
        buf.write("\2\t\u00ad\3\2\2\2\13\u00b0\3\2\2\2\r\u00b5\3\2\2\2\17")
        buf.write("\u00b9\3\2\2\2\21\u00c0\3\2\2\2\23\u00c5\3\2\2\2\25\u00ca")
        buf.write("\3\2\2\2\27\u00d1\3\2\2\2\31\u00db\3\2\2\2\33\u00e2\3")
        buf.write("\2\2\2\35\u00e6\3\2\2\2\37\u00ec\3\2\2\2!\u00f4\3\2\2")
        buf.write("\2#\u00fa\3\2\2\2%\u00fe\3\2\2\2\'\u0107\3\2\2\2)\u010d")
        buf.write("\3\2\2\2+\u0113\3\2\2\2-\u0115\3\2\2\2/\u0117\3\2\2\2")
        buf.write("\61\u0119\3\2\2\2\63\u011b\3\2\2\2\65\u011d\3\2\2\2\67")
        buf.write("\u0120\3\2\2\29\u0123\3\2\2\2;\u0125\3\2\2\2=\u0128\3")
        buf.write("\2\2\2?\u012a\3\2\2\2A\u012d\3\2\2\2C\u0130\3\2\2\2E\u0133")
        buf.write("\3\2\2\2G\u0135\3\2\2\2I\u0138\3\2\2\2K\u013b\3\2\2\2")
        buf.write("M\u013e\3\2\2\2O\u0141\3\2\2\2Q\u0144\3\2\2\2S\u0147\3")
        buf.write("\2\2\2U\u0149\3\2\2\2W\u014b\3\2\2\2Y\u014d\3\2\2\2[\u014f")
        buf.write("\3\2\2\2]\u0151\3\2\2\2_\u0153\3\2\2\2a\u0155\3\2\2\2")
        buf.write("c\u0157\3\2\2\2e\u0159\3\2\2\2g\u015b\3\2\2\2i\u017a\3")
        buf.write("\2\2\2k\u017d\3\2\2\2m\u018b\3\2\2\2o\u0197\3\2\2\2q\u0199")
        buf.write("\3\2\2\2s\u019c\3\2\2\2u\u01aa\3\2\2\2w\u01b6\3\2\2\2")
        buf.write("y\u01b8\3\2\2\2{\u01ca\3\2\2\2}\u01cc\3\2\2\2\177\u01d0")
        buf.write("\3\2\2\2\u0081\u01da\3\2\2\2\u0083\u01dd\3\2\2\2\u0085")
        buf.write("\u01e3\3\2\2\2\u0087\u0088\7\61\2\2\u0088\u0089\7\61\2")
        buf.write("\2\u0089\u008d\3\2\2\2\u008a\u008c\n\2\2\2\u008b\u008a")
        buf.write("\3\2\2\2\u008c\u008f\3\2\2\2\u008d\u008b\3\2\2\2\u008d")
        buf.write("\u008e\3\2\2\2\u008e\u0090\3\2\2\2\u008f\u008d\3\2\2\2")
        buf.write("\u0090\u0091\b\2\2\2\u0091\4\3\2\2\2\u0092\u0093\7\61")
        buf.write("\2\2\u0093\u0094\7,\2\2\u0094\u0099\3\2\2\2\u0095\u0098")
        buf.write("\5\7\4\2\u0096\u0098\13\2\2\2\u0097\u0095\3\2\2\2\u0097")
        buf.write("\u0096\3\2\2\2\u0098\u009b\3\2\2\2\u0099\u009a\3\2\2\2")
        buf.write("\u0099\u0097\3\2\2\2\u009a\u009c\3\2\2\2\u009b\u0099\3")
        buf.write("\2\2\2\u009c\u009d\7,\2\2\u009d\u009e\7\61\2\2\u009e\u009f")
        buf.write("\3\2\2\2\u009f\u00a0\b\3\2\2\u00a0\6\3\2\2\2\u00a1\u00a2")
        buf.write("\7\61\2\2\u00a2\u00a3\7,\2\2\u00a3\u00a7\3\2\2\2\u00a4")
        buf.write("\u00a6\13\2\2\2\u00a5\u00a4\3\2\2\2\u00a6\u00a9\3\2\2")
        buf.write("\2\u00a7\u00a8\3\2\2\2\u00a7\u00a5\3\2\2\2\u00a8\u00aa")
        buf.write("\3\2\2\2\u00a9\u00a7\3\2\2\2\u00aa\u00ab\7,\2\2\u00ab")
        buf.write("\u00ac\7\61\2\2\u00ac\b\3\2\2\2\u00ad\u00ae\7k\2\2\u00ae")
        buf.write("\u00af\7h\2\2\u00af\n\3\2\2\2\u00b0\u00b1\7g\2\2\u00b1")
        buf.write("\u00b2\7n\2\2\u00b2\u00b3\7u\2\2\u00b3\u00b4\7g\2\2\u00b4")
        buf.write("\f\3\2\2\2\u00b5\u00b6\7h\2\2\u00b6\u00b7\7q\2\2\u00b7")
        buf.write("\u00b8\7t\2\2\u00b8\16\3\2\2\2\u00b9\u00ba\7t\2\2\u00ba")
        buf.write("\u00bb\7g\2\2\u00bb\u00bc\7v\2\2\u00bc\u00bd\7w\2\2\u00bd")
        buf.write("\u00be\7t\2\2\u00be\u00bf\7p\2\2\u00bf\20\3\2\2\2\u00c0")
        buf.write("\u00c1\7h\2\2\u00c1\u00c2\7w\2\2\u00c2\u00c3\7p\2\2\u00c3")
        buf.write("\u00c4\7e\2\2\u00c4\22\3\2\2\2\u00c5\u00c6\7v\2\2\u00c6")
        buf.write("\u00c7\7{\2\2\u00c7\u00c8\7r\2\2\u00c8\u00c9\7g\2\2\u00c9")
        buf.write("\24\3\2\2\2\u00ca\u00cb\7u\2\2\u00cb\u00cc\7v\2\2\u00cc")
        buf.write("\u00cd\7t\2\2\u00cd\u00ce\7w\2\2\u00ce\u00cf\7e\2\2\u00cf")
        buf.write("\u00d0\7v\2\2\u00d0\26\3\2\2\2\u00d1\u00d2\7k\2\2\u00d2")
        buf.write("\u00d3\7p\2\2\u00d3\u00d4\7v\2\2\u00d4\u00d5\7g\2\2\u00d5")
        buf.write("\u00d6\7t\2\2\u00d6\u00d7\7h\2\2\u00d7\u00d8\7c\2\2\u00d8")
        buf.write("\u00d9\7e\2\2\u00d9\u00da\7g\2\2\u00da\30\3\2\2\2\u00db")
        buf.write("\u00dc\7u\2\2\u00dc\u00dd\7v\2\2\u00dd\u00de\7t\2\2\u00de")
        buf.write("\u00df\7k\2\2\u00df\u00e0\7p\2\2\u00e0\u00e1\7i\2\2\u00e1")
        buf.write("\32\3\2\2\2\u00e2\u00e3\7k\2\2\u00e3\u00e4\7p\2\2\u00e4")
        buf.write("\u00e5\7v\2\2\u00e5\34\3\2\2\2\u00e6\u00e7\7h\2\2\u00e7")
        buf.write("\u00e8\7n\2\2\u00e8\u00e9\7q\2\2\u00e9\u00ea\7c\2\2\u00ea")
        buf.write("\u00eb\7v\2\2\u00eb\36\3\2\2\2\u00ec\u00ed\7d\2\2\u00ed")
        buf.write("\u00ee\7q\2\2\u00ee\u00ef\7q\2\2\u00ef\u00f0\7n\2\2\u00f0")
        buf.write("\u00f1\7g\2\2\u00f1\u00f2\7c\2\2\u00f2\u00f3\7p\2\2\u00f3")
        buf.write(" \3\2\2\2\u00f4\u00f5\7e\2\2\u00f5\u00f6\7q\2\2\u00f6")
        buf.write("\u00f7\7p\2\2\u00f7\u00f8\7u\2\2\u00f8\u00f9\7v\2\2\u00f9")
        buf.write("\"\3\2\2\2\u00fa\u00fb\7x\2\2\u00fb\u00fc\7c\2\2\u00fc")
        buf.write("\u00fd\7t\2\2\u00fd$\3\2\2\2\u00fe\u00ff\7e\2\2\u00ff")
        buf.write("\u0100\7q\2\2\u0100\u0101\7p\2\2\u0101\u0102\7v\2\2\u0102")
        buf.write("\u0103\7k\2\2\u0103\u0104\7p\2\2\u0104\u0105\7w\2\2\u0105")
        buf.write("\u0106\7g\2\2\u0106&\3\2\2\2\u0107\u0108\7d\2\2\u0108")
        buf.write("\u0109\7t\2\2\u0109\u010a\7g\2\2\u010a\u010b\7c\2\2\u010b")
        buf.write("\u010c\7m\2\2\u010c(\3\2\2\2\u010d\u010e\7t\2\2\u010e")
        buf.write("\u010f\7c\2\2\u010f\u0110\7p\2\2\u0110\u0111\7i\2\2\u0111")
        buf.write("\u0112\7g\2\2\u0112*\3\2\2\2\u0113\u0114\7-\2\2\u0114")
        buf.write(",\3\2\2\2\u0115\u0116\7/\2\2\u0116.\3\2\2\2\u0117\u0118")
        buf.write("\7,\2\2\u0118\60\3\2\2\2\u0119\u011a\7\61\2\2\u011a\62")
        buf.write("\3\2\2\2\u011b\u011c\7\'\2\2\u011c\64\3\2\2\2\u011d\u011e")
        buf.write("\7?\2\2\u011e\u011f\7?\2\2\u011f\66\3\2\2\2\u0120\u0121")
        buf.write("\7#\2\2\u0121\u0122\7?\2\2\u01228\3\2\2\2\u0123\u0124")
        buf.write("\7>\2\2\u0124:\3\2\2\2\u0125\u0126\7>\2\2\u0126\u0127")
        buf.write("\7?\2\2\u0127<\3\2\2\2\u0128\u0129\7@\2\2\u0129>\3\2\2")
        buf.write("\2\u012a\u012b\7@\2\2\u012b\u012c\7?\2\2\u012c@\3\2\2")
        buf.write("\2\u012d\u012e\7(\2\2\u012e\u012f\7(\2\2\u012fB\3\2\2")
        buf.write("\2\u0130\u0131\7~\2\2\u0131\u0132\7~\2\2\u0132D\3\2\2")
        buf.write("\2\u0133\u0134\7#\2\2\u0134F\3\2\2\2\u0135\u0136\7<\2")
        buf.write("\2\u0136\u0137\7?\2\2\u0137H\3\2\2\2\u0138\u0139\7-\2")
        buf.write("\2\u0139\u013a\7?\2\2\u013aJ\3\2\2\2\u013b\u013c\7/\2")
        buf.write("\2\u013c\u013d\7?\2\2\u013dL\3\2\2\2\u013e\u013f\7,\2")
        buf.write("\2\u013f\u0140\7?\2\2\u0140N\3\2\2\2\u0141\u0142\7\61")
        buf.write("\2\2\u0142\u0143\7?\2\2\u0143P\3\2\2\2\u0144\u0145\7\'")
        buf.write("\2\2\u0145\u0146\7?\2\2\u0146R\3\2\2\2\u0147\u0148\7?")
        buf.write("\2\2\u0148T\3\2\2\2\u0149\u014a\7\60\2\2\u014aV\3\2\2")
        buf.write("\2\u014b\u014c\7*\2\2\u014cX\3\2\2\2\u014d\u014e\7+\2")
        buf.write("\2\u014eZ\3\2\2\2\u014f\u0150\7}\2\2\u0150\\\3\2\2\2\u0151")
        buf.write("\u0152\7\177\2\2\u0152^\3\2\2\2\u0153\u0154\7]\2\2\u0154")
        buf.write("`\3\2\2\2\u0155\u0156\7_\2\2\u0156b\3\2\2\2\u0157\u0158")
        buf.write("\7.\2\2\u0158d\3\2\2\2\u0159\u015a\7=\2\2\u015af\3\2\2")
        buf.write("\2\u015b\u015c\7<\2\2\u015ch\3\2\2\2\u015d\u0161\t\3\2")
        buf.write("\2\u015e\u0160\5w<\2\u015f\u015e\3\2\2\2\u0160\u0163\3")
        buf.write("\2\2\2\u0161\u015f\3\2\2\2\u0161\u0162\3\2\2\2\u0162\u017b")
        buf.write("\3\2\2\2\u0163\u0161\3\2\2\2\u0164\u017b\7\62\2\2\u0165")
        buf.write("\u0166\7\62\2\2\u0166\u0168\t\4\2\2\u0167\u0169\t\5\2")
        buf.write("\2\u0168\u0167\3\2\2\2\u0169\u016a\3\2\2\2\u016a\u0168")
        buf.write("\3\2\2\2\u016a\u016b\3\2\2\2\u016b\u017b\3\2\2\2\u016c")
        buf.write("\u016d\7\62\2\2\u016d\u016f\t\6\2\2\u016e\u0170\t\7\2")
        buf.write("\2\u016f\u016e\3\2\2\2\u0170\u0171\3\2\2\2\u0171\u016f")
        buf.write("\3\2\2\2\u0171\u0172\3\2\2\2\u0172\u017b\3\2\2\2\u0173")
        buf.write("\u0174\7\62\2\2\u0174\u0176\t\b\2\2\u0175\u0177\t\t\2")
        buf.write("\2\u0176\u0175\3\2\2\2\u0177\u0178\3\2\2\2\u0178\u0176")
        buf.write("\3\2\2\2\u0178\u0179\3\2\2\2\u0179\u017b\3\2\2\2\u017a")
        buf.write("\u015d\3\2\2\2\u017a\u0164\3\2\2\2\u017a\u0165\3\2\2\2")
        buf.write("\u017a\u016c\3\2\2\2\u017a\u0173\3\2\2\2\u017bj\3\2\2")
        buf.write("\2\u017c\u017e\5w<\2\u017d\u017c\3\2\2\2\u017e\u017f\3")
        buf.write("\2\2\2\u017f\u017d\3\2\2\2\u017f\u0180\3\2\2\2\u0180\u0181")
        buf.write("\3\2\2\2\u0181\u0185\7\60\2\2\u0182\u0184\5w<\2\u0183")
        buf.write("\u0182\3\2\2\2\u0184\u0187\3\2\2\2\u0185\u0183\3\2\2\2")
        buf.write("\u0185\u0186\3\2\2\2\u0186\u0189\3\2\2\2\u0187\u0185\3")
        buf.write("\2\2\2\u0188\u018a\5y=\2\u0189\u0188\3\2\2\2\u0189\u018a")
        buf.write("\3\2\2\2\u018al\3\2\2\2\u018b\u018f\7$\2\2\u018c\u018e")
        buf.write("\5o8\2\u018d\u018c\3\2\2\2\u018e\u0191\3\2\2\2\u018f\u018d")
        buf.write("\3\2\2\2\u018f\u0190\3\2\2\2\u0190\u0192\3\2\2\2\u0191")
        buf.write("\u018f\3\2\2\2\u0192\u0193\7$\2\2\u0193\u0194\b\67\3\2")
        buf.write("\u0194n\3\2\2\2\u0195\u0198\n\n\2\2\u0196\u0198\5q9\2")
        buf.write("\u0197\u0195\3\2\2\2\u0197\u0196\3\2\2\2\u0198p\3\2\2")
        buf.write("\2\u0199\u019a\7^\2\2\u019a\u019b\t\13\2\2\u019br\3\2")
        buf.write("\2\2\u019c\u01a0\7$\2\2\u019d\u019f\5o8\2\u019e\u019d")
        buf.write("\3\2\2\2\u019f\u01a2\3\2\2\2\u01a0\u019e\3\2\2\2\u01a0")
        buf.write("\u01a1\3\2\2\2\u01a1\u01a6\3\2\2\2\u01a2\u01a0\3\2\2\2")
        buf.write("\u01a3\u01a4\7\17\2\2\u01a4\u01a7\7\f\2\2\u01a5\u01a7")
        buf.write("\t\f\2\2\u01a6\u01a3\3\2\2\2\u01a6\u01a5\3\2\2\2\u01a7")
        buf.write("\u01a8\3\2\2\2\u01a8\u01a9\b:\4\2\u01a9t\3\2\2\2\u01aa")
        buf.write("\u01ae\7$\2\2\u01ab\u01ad\5o8\2\u01ac\u01ab\3\2\2\2\u01ad")
        buf.write("\u01b0\3\2\2\2\u01ae\u01ac\3\2\2\2\u01ae\u01af\3\2\2\2")
        buf.write("\u01af\u01b1\3\2\2\2\u01b0\u01ae\3\2\2\2\u01b1\u01b2\7")
        buf.write("^\2\2\u01b2\u01b3\n\13\2\2\u01b3\u01b4\3\2\2\2\u01b4\u01b5")
        buf.write("\b;\5\2\u01b5v\3\2\2\2\u01b6\u01b7\t\r\2\2\u01b7x\3\2")
        buf.write("\2\2\u01b8\u01ba\t\16\2\2\u01b9\u01bb\t\17\2\2\u01ba\u01b9")
        buf.write("\3\2\2\2\u01ba\u01bb\3\2\2\2\u01bb\u01bd\3\2\2\2\u01bc")
        buf.write("\u01be\5w<\2\u01bd\u01bc\3\2\2\2\u01be\u01bf\3\2\2\2\u01bf")
        buf.write("\u01bd\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0z\3\2\2\2\u01c1")
        buf.write("\u01c2\7v\2\2\u01c2\u01c3\7t\2\2\u01c3\u01c4\7w\2\2\u01c4")
        buf.write("\u01cb\7g\2\2\u01c5\u01c6\7h\2\2\u01c6\u01c7\7c\2\2\u01c7")
        buf.write("\u01c8\7n\2\2\u01c8\u01c9\7u\2\2\u01c9\u01cb\7g\2\2\u01ca")
        buf.write("\u01c1\3\2\2\2\u01ca\u01c5\3\2\2\2\u01cb|\3\2\2\2\u01cc")
        buf.write("\u01cd\7p\2\2\u01cd\u01ce\7k\2\2\u01ce\u01cf\7n\2\2\u01cf")
        buf.write("~\3\2\2\2\u01d0\u01d4\t\20\2\2\u01d1\u01d3\t\21\2\2\u01d2")
        buf.write("\u01d1\3\2\2\2\u01d3\u01d6\3\2\2\2\u01d4\u01d2\3\2\2\2")
        buf.write("\u01d4\u01d5\3\2\2\2\u01d5\u0080\3\2\2\2\u01d6\u01d4\3")
        buf.write("\2\2\2\u01d7\u01db\7\f\2\2\u01d8\u01d9\7\17\2\2\u01d9")
        buf.write("\u01db\7\f\2\2\u01da\u01d7\3\2\2\2\u01da\u01d8\3\2\2\2")
        buf.write("\u01db\u0082\3\2\2\2\u01dc\u01de\t\22\2\2\u01dd\u01dc")
        buf.write("\3\2\2\2\u01de\u01df\3\2\2\2\u01df\u01dd\3\2\2\2\u01df")
        buf.write("\u01e0\3\2\2\2\u01e0\u01e1\3\2\2\2\u01e1\u01e2\bB\2\2")
        buf.write("\u01e2\u0084\3\2\2\2\u01e3\u01e4\13\2\2\2\u01e4\u01e5")
        buf.write("\bC\6\2\u01e5\u0086\3\2\2\2\32\2\u008d\u0097\u0099\u00a7")
        buf.write("\u0161\u016a\u0171\u0178\u017a\u017f\u0185\u0189\u018f")
        buf.write("\u0197\u01a0\u01a6\u01ae\u01ba\u01bf\u01ca\u01d4\u01da")
        buf.write("\u01df\7\b\2\2\3\67\2\3:\3\3;\4\3C\5")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    LINE_CMT = 1
    BLOCK_COMT = 2
    IF = 3
    ELSE = 4
    FOR = 5
    RETURN = 6
    FUNC = 7
    TYPE = 8
    STRUCT = 9
    INTERFACE = 10
    STRING = 11
    INT = 12
    FLOAT = 13
    BOOLEAN = 14
    CONST = 15
    VAR = 16
    CONTINUE = 17
    BREAK = 18
    RANGE = 19
    ADD = 20
    SUB = 21
    MUL = 22
    DIV = 23
    MOD = 24
    EQUAL = 25
    NEQUAL = 26
    LESS = 27
    LESSEQ = 28
    GREAT = 29
    GREATEQ = 30
    AND = 31
    OR = 32
    NEG = 33
    ASSIGN = 34
    ADDASGN = 35
    SUBASGN = 36
    MULASGN = 37
    DIVASGN = 38
    MODASGN = 39
    INIASSIGN = 40
    DOT = 41
    LPAR = 42
    RPAR = 43
    LCUR = 44
    RCUR = 45
    LSQU = 46
    RSQU = 47
    COMMA = 48
    SEMICOL = 49
    COL = 50
    INT_LIT = 51
    FLOAT_LIT = 52
    STRING_LIT = 53
    UNCLOSE_STRING = 54
    ILLEGAL_ESCAPE = 55
    BOOL_LIT = 56
    NIL_LIT = 57
    ID = 58
    NL = 59
    WS = 60
    ERROR_CHAR = 61

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", "'struct'", 
            "'interface'", "'string'", "'int'", "'float'", "'boolean'", 
            "'const'", "'var'", "'continue'", "'break'", "'range'", "'+'", 
            "'-'", "'*'", "'/'", "'%'", "'=='", "'!='", "'<'", "'<='", "'>'", 
            "'>='", "'&&'", "'||'", "'!'", "':='", "'+='", "'-='", "'*='", 
            "'/='", "'%='", "'='", "'.'", "'('", "')'", "'{'", "'}'", "'['", 
            "']'", "','", "';'", "':'", "'nil'" ]

    symbolicNames = [ "<INVALID>",
            "LINE_CMT", "BLOCK_COMT", "IF", "ELSE", "FOR", "RETURN", "FUNC", 
            "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", 
            "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", "ADD", "SUB", 
            "MUL", "DIV", "MOD", "EQUAL", "NEQUAL", "LESS", "LESSEQ", "GREAT", 
            "GREATEQ", "AND", "OR", "NEG", "ASSIGN", "ADDASGN", "SUBASGN", 
            "MULASGN", "DIVASGN", "MODASGN", "INIASSIGN", "DOT", "LPAR", 
            "RPAR", "LCUR", "RCUR", "LSQU", "RSQU", "COMMA", "SEMICOL", 
            "COL", "INT_LIT", "FLOAT_LIT", "STRING_LIT", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "BOOL_LIT", "NIL_LIT", "ID", "NL", "WS", "ERROR_CHAR" ]

    ruleNames = [ "LINE_CMT", "BLOCK_COMT", "CMT", "IF", "ELSE", "FOR", 
                  "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", "STRING", 
                  "INT", "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", 
                  "BREAK", "RANGE", "ADD", "SUB", "MUL", "DIV", "MOD", "EQUAL", 
                  "NEQUAL", "LESS", "LESSEQ", "GREAT", "GREATEQ", "AND", 
                  "OR", "NEG", "ASSIGN", "ADDASGN", "SUBASGN", "MULASGN", 
                  "DIVASGN", "MODASGN", "INIASSIGN", "DOT", "LPAR", "RPAR", 
                  "LCUR", "RCUR", "LSQU", "RSQU", "COMMA", "SEMICOL", "COL", 
                  "INT_LIT", "FLOAT_LIT", "STRING_LIT", "STRING_CHAR", "ESCAPE", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "Digit", "Expo", "BOOL_LIT", 
                  "NIL_LIT", "ID", "NL", "WS", "ERROR_CHAR" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None



    prevToken = None  # Track the last emitted token

    def emit(self):
        tk = self.type
        result = super().emit()  # Get the next token
        if tk == self.UNCLOSE_STRING:
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        elif tk == self.NL:
            if self.prevToken and self.prevToken.type in [
            self.ID, self.INT_LIT, self.FLOAT_LIT, self.STRING_LIT, self.BOOL_LIT,
            self.BOOLEAN, self.STRING, self.INT, self.FLOAT, self.NIL_LIT,
            self.RPAR, self.RCUR, self.RSQU, self.RETURN, self.CONTINUE, self.BREAK]: 
                result.type = self.SEMICOL
                result.text = ";"
                self.prevToken = result
                return result 
            else:
                result = self.nextToken()
                self.prevToken = result
                #print(f"Token emitted: {result}")
                return result;
        else:
            self.prevToken = result
            #print(f"Token emitted: {result}")
            return result  


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[53] = self.STRING_LIT_action 
            actions[56] = self.UNCLOSE_STRING_action 
            actions[57] = self.ILLEGAL_ESCAPE_action 
            actions[65] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                raise UncloseString(self.text[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                raise IllegalEscape(self.text[1:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     


