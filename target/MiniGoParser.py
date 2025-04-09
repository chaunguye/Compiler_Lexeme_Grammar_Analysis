# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3?")
        buf.write("\u025e\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3\u0096")
        buf.write("\n\3\3\4\3\4\3\4\3\4\3\4\5\4\u009d\n\4\3\5\3\5\5\5\u00a1")
        buf.write("\n\5\3\6\3\6\3\6\5\6\u00a6\n\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\5\6\u00b1\n\6\3\7\3\7\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\t\3\t\5\t\u00bd\n\t\3\t\3\t\3\t\5\t\u00c2\n\t\3")
        buf.write("\t\3\t\3\t\3\n\3\n\5\n\u00c9\n\n\3\13\3\13\3\13\3\f\3")
        buf.write("\f\3\f\3\f\3\r\3\r\5\r\u00d4\n\r\3\16\3\16\3\16\3\16\3")
        buf.write("\16\5\16\u00db\n\16\3\17\3\17\3\17\3\17\5\17\u00e1\n\17")
        buf.write("\3\20\3\20\3\20\3\21\3\21\3\21\3\21\5\21\u00ea\n\21\3")
        buf.write("\22\3\22\5\22\u00ee\n\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\5\23\u00f6\n\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3")
        buf.write("\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u0107\n\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\27\5\27\u010f\n\27\3\30\3")
        buf.write("\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\32\3\33\3\33\3\33\3\33\5\33\u0123\n\33\3\34\3")
        buf.write("\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\36\3\36\3\36\3\36\5\36\u0135\n\36\3\37\3\37\3\37\5")
        buf.write("\37\u013a\n\37\3\37\3\37\3 \3 \3 \3 \3!\3!\3!\3!\3\"\3")
        buf.write("\"\3\"\3\"\3\"\5\"\u014b\n\"\3#\3#\5#\u014f\n#\3$\3$\3")
        buf.write("$\3$\3$\3%\3%\5%\u0158\n%\3&\3&\3&\3&\3&\5&\u015f\n&\3")
        buf.write("\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\7(\u016b\n(\f(\16(\u016e")
        buf.write("\13(\3)\3)\3)\3)\3)\3)\7)\u0176\n)\f)\16)\u0179\13)\3")
        buf.write("*\3*\3*\3*\3*\3*\7*\u0181\n*\f*\16*\u0184\13*\3+\3+\3")
        buf.write("+\3+\3+\3+\7+\u018c\n+\f+\16+\u018f\13+\3,\3,\3,\3,\3")
        buf.write(",\3,\7,\u0197\n,\f,\16,\u019a\13,\3-\3-\3-\5-\u019f\n")
        buf.write("-\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\7.\u01ac\n.\f.\16.")
        buf.write("\u01af\13.\3/\3/\3/\3/\3/\3/\3/\5/\u01b8\n/\3\60\3\60")
        buf.write("\3\60\3\60\3\60\3\61\3\61\5\61\u01c1\n\61\3\62\3\62\3")
        buf.write("\62\3\62\3\62\5\62\u01c8\n\62\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\63\5\63\u01d0\n\63\3\64\3\64\3\65\3\65\3\65\3\65\3")
        buf.write("\65\3\65\3\65\3\65\5\65\u01dc\n\65\3\66\3\66\3\66\3\66")
        buf.write("\3\66\3\67\3\67\3\67\3\67\3\67\3\67\5\67\u01e9\n\67\3")
        buf.write("8\38\38\38\38\58\u01f0\n8\38\38\38\38\58\u01f6\n8\38\3")
        buf.write("8\58\u01fa\n8\38\38\39\39\59\u0200\n9\3:\3:\5:\u0204\n")
        buf.write(":\3:\3:\3:\5:\u0209\n:\3;\3;\3;\3;\3;\5;\u0210\n;\3<\3")
        buf.write("<\3<\3<\3<\3<\5<\u0218\n<\3<\3<\3<\3<\5<\u021e\n<\3=\3")
        buf.write("=\3=\3=\5=\u0224\n=\3>\3>\3>\3>\3>\3>\3>\3?\3?\3?\5?\u0230")
        buf.write("\n?\3@\3@\3@\3@\3@\3@\3A\3A\3A\3A\3A\3A\5A\u023e\nA\3")
        buf.write("A\3A\5A\u0242\nA\3B\3B\3B\3B\3C\3C\3C\3C\3C\3C\3C\3D\3")
        buf.write("D\3D\3E\3E\3E\3F\3F\5F\u0257\nF\3F\3F\3G\3G\3G\3G\2\b")
        buf.write("NPRTVZH\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*")
        buf.write(",.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080")
        buf.write("\u0082\u0084\u0086\u0088\u008a\u008c\2\t\4\2\r\20<<\3")
        buf.write("\2\33 \3\2\26\27\3\2\30\32\4\2\27\27##\4\2\65\65<<\3\2")
        buf.write("$)\2\u025b\2\u008e\3\2\2\2\4\u0095\3\2\2\2\6\u009c\3\2")
        buf.write("\2\2\b\u00a0\3\2\2\2\n\u00b0\3\2\2\2\f\u00b2\3\2\2\2\16")
        buf.write("\u00b4\3\2\2\2\20\u00ba\3\2\2\2\22\u00c8\3\2\2\2\24\u00ca")
        buf.write("\3\2\2\2\26\u00cd\3\2\2\2\30\u00d3\3\2\2\2\32\u00da\3")
        buf.write("\2\2\2\34\u00e0\3\2\2\2\36\u00e2\3\2\2\2 \u00e9\3\2\2")
        buf.write("\2\"\u00eb\3\2\2\2$\u00f5\3\2\2\2&\u00f7\3\2\2\2(\u00fb")
        buf.write("\3\2\2\2*\u0100\3\2\2\2,\u010e\3\2\2\2.\u0110\3\2\2\2")
        buf.write("\60\u0114\3\2\2\2\62\u011a\3\2\2\2\64\u0122\3\2\2\2\66")
        buf.write("\u0124\3\2\2\28\u0128\3\2\2\2:\u0134\3\2\2\2<\u0136\3")
        buf.write("\2\2\2>\u013d\3\2\2\2@\u0141\3\2\2\2B\u014a\3\2\2\2D\u014e")
        buf.write("\3\2\2\2F\u0150\3\2\2\2H\u0157\3\2\2\2J\u015e\3\2\2\2")
        buf.write("L\u0160\3\2\2\2N\u0164\3\2\2\2P\u016f\3\2\2\2R\u017a\3")
        buf.write("\2\2\2T\u0185\3\2\2\2V\u0190\3\2\2\2X\u019e\3\2\2\2Z\u01a0")
        buf.write("\3\2\2\2\\\u01b7\3\2\2\2^\u01b9\3\2\2\2`\u01c0\3\2\2\2")
        buf.write("b\u01c7\3\2\2\2d\u01cf\3\2\2\2f\u01d1\3\2\2\2h\u01db\3")
        buf.write("\2\2\2j\u01dd\3\2\2\2l\u01e8\3\2\2\2n\u01ea\3\2\2\2p\u01ff")
        buf.write("\3\2\2\2r\u0208\3\2\2\2t\u020a\3\2\2\2v\u0211\3\2\2\2")
        buf.write("x\u0223\3\2\2\2z\u0225\3\2\2\2|\u022f\3\2\2\2~\u0231\3")
        buf.write("\2\2\2\u0080\u0241\3\2\2\2\u0082\u0243\3\2\2\2\u0084\u0247")
        buf.write("\3\2\2\2\u0086\u024e\3\2\2\2\u0088\u0251\3\2\2\2\u008a")
        buf.write("\u0254\3\2\2\2\u008c\u025a\3\2\2\2\u008e\u008f\5\4\3\2")
        buf.write("\u008f\u0090\7\2\2\3\u0090\3\3\2\2\2\u0091\u0092\5\6\4")
        buf.write("\2\u0092\u0093\5\4\3\2\u0093\u0096\3\2\2\2\u0094\u0096")
        buf.write("\5\6\4\2\u0095\u0091\3\2\2\2\u0095\u0094\3\2\2\2\u0096")
        buf.write("\5\3\2\2\2\u0097\u009d\5\20\t\2\u0098\u009d\5\n\6\2\u0099")
        buf.write("\u009d\5\16\b\2\u009a\u009d\5*\26\2\u009b\u009d\5\b\5")
        buf.write("\2\u009c\u0097\3\2\2\2\u009c\u0098\3\2\2\2\u009c\u0099")
        buf.write("\3\2\2\2\u009c\u009a\3\2\2\2\u009c\u009b\3\2\2\2\u009d")
        buf.write("\7\3\2\2\2\u009e\u00a1\5\60\31\2\u009f\u00a1\58\35\2\u00a0")
        buf.write("\u009e\3\2\2\2\u00a0\u009f\3\2\2\2\u00a1\t\3\2\2\2\u00a2")
        buf.write("\u00a3\7\22\2\2\u00a3\u00a5\7<\2\2\u00a4\u00a6\5\f\7\2")
        buf.write("\u00a5\u00a4\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6\u00a7\3")
        buf.write("\2\2\2\u00a7\u00a8\7*\2\2\u00a8\u00a9\5N(\2\u00a9\u00aa")
        buf.write("\7\63\2\2\u00aa\u00b1\3\2\2\2\u00ab\u00ac\7\22\2\2\u00ac")
        buf.write("\u00ad\7<\2\2\u00ad\u00ae\5\f\7\2\u00ae\u00af\7\63\2\2")
        buf.write("\u00af\u00b1\3\2\2\2\u00b0\u00a2\3\2\2\2\u00b0\u00ab\3")
        buf.write("\2\2\2\u00b1\13\3\2\2\2\u00b2\u00b3\t\2\2\2\u00b3\r\3")
        buf.write("\2\2\2\u00b4\u00b5\7\21\2\2\u00b5\u00b6\7<\2\2\u00b6\u00b7")
        buf.write("\7*\2\2\u00b7\u00b8\5N(\2\u00b8\u00b9\7\63\2\2\u00b9\17")
        buf.write("\3\2\2\2\u00ba\u00bc\7\t\2\2\u00bb\u00bd\5(\25\2\u00bc")
        buf.write("\u00bb\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd\u00be\3\2\2\2")
        buf.write("\u00be\u00bf\7<\2\2\u00bf\u00c1\5\26\f\2\u00c0\u00c2\5")
        buf.write("\22\n\2\u00c1\u00c0\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2")
        buf.write("\u00c3\3\2\2\2\u00c3\u00c4\5&\24\2\u00c4\u00c5\7\63\2")
        buf.write("\2\u00c5\21\3\2\2\2\u00c6\u00c9\5\f\7\2\u00c7\u00c9\5")
        buf.write("\24\13\2\u00c8\u00c6\3\2\2\2\u00c8\u00c7\3\2\2\2\u00c9")
        buf.write("\23\3\2\2\2\u00ca\u00cb\5 \21\2\u00cb\u00cc\5\f\7\2\u00cc")
        buf.write("\25\3\2\2\2\u00cd\u00ce\7,\2\2\u00ce\u00cf\5\30\r\2\u00cf")
        buf.write("\u00d0\7-\2\2\u00d0\27\3\2\2\2\u00d1\u00d4\5\32\16\2\u00d2")
        buf.write("\u00d4\3\2\2\2\u00d3\u00d1\3\2\2\2\u00d3\u00d2\3\2\2\2")
        buf.write("\u00d4\31\3\2\2\2\u00d5\u00d6\5\34\17\2\u00d6\u00d7\7")
        buf.write("\62\2\2\u00d7\u00d8\5\32\16\2\u00d8\u00db\3\2\2\2\u00d9")
        buf.write("\u00db\5\34\17\2\u00da\u00d5\3\2\2\2\u00da\u00d9\3\2\2")
        buf.write("\2\u00db\33\3\2\2\2\u00dc\u00dd\5$\23\2\u00dd\u00de\5")
        buf.write("\f\7\2\u00de\u00e1\3\2\2\2\u00df\u00e1\5\36\20\2\u00e0")
        buf.write("\u00dc\3\2\2\2\u00e0\u00df\3\2\2\2\u00e1\35\3\2\2\2\u00e2")
        buf.write("\u00e3\7<\2\2\u00e3\u00e4\5 \21\2\u00e4\37\3\2\2\2\u00e5")
        buf.write("\u00e6\5\"\22\2\u00e6\u00e7\5 \21\2\u00e7\u00ea\3\2\2")
        buf.write("\2\u00e8\u00ea\5\"\22\2\u00e9\u00e5\3\2\2\2\u00e9\u00e8")
        buf.write("\3\2\2\2\u00ea!\3\2\2\2\u00eb\u00ed\7\60\2\2\u00ec\u00ee")
        buf.write("\5f\64\2\u00ed\u00ec\3\2\2\2\u00ed\u00ee\3\2\2\2\u00ee")
        buf.write("\u00ef\3\2\2\2\u00ef\u00f0\7\61\2\2\u00f0#\3\2\2\2\u00f1")
        buf.write("\u00f2\7<\2\2\u00f2\u00f3\7\62\2\2\u00f3\u00f6\5$\23\2")
        buf.write("\u00f4\u00f6\7<\2\2\u00f5\u00f1\3\2\2\2\u00f5\u00f4\3")
        buf.write("\2\2\2\u00f6%\3\2\2\2\u00f7\u00f8\7.\2\2\u00f8\u00f9\5")
        buf.write("x=\2\u00f9\u00fa\7/\2\2\u00fa\'\3\2\2\2\u00fb\u00fc\7")
        buf.write(",\2\2\u00fc\u00fd\7<\2\2\u00fd\u00fe\7<\2\2\u00fe\u00ff")
        buf.write("\7-\2\2\u00ff)\3\2\2\2\u0100\u0101\7\22\2\2\u0101\u0102")
        buf.write("\7<\2\2\u0102\u0103\5,\27\2\u0103\u0106\5\f\7\2\u0104")
        buf.write("\u0105\7*\2\2\u0105\u0107\5> \2\u0106\u0104\3\2\2\2\u0106")
        buf.write("\u0107\3\2\2\2\u0107\u0108\3\2\2\2\u0108\u0109\7\63\2")
        buf.write("\2\u0109+\3\2\2\2\u010a\u010b\5.\30\2\u010b\u010c\5,\27")
        buf.write("\2\u010c\u010f\3\2\2\2\u010d\u010f\5.\30\2\u010e\u010a")
        buf.write("\3\2\2\2\u010e\u010d\3\2\2\2\u010f-\3\2\2\2\u0110\u0111")
        buf.write("\7\60\2\2\u0111\u0112\5f\64\2\u0112\u0113\7\61\2\2\u0113")
        buf.write("/\3\2\2\2\u0114\u0115\7\n\2\2\u0115\u0116\7<\2\2\u0116")
        buf.write("\u0117\7\13\2\2\u0117\u0118\5\62\32\2\u0118\u0119\7\63")
        buf.write("\2\2\u0119\61\3\2\2\2\u011a\u011b\7.\2\2\u011b\u011c\5")
        buf.write("\64\33\2\u011c\u011d\7/\2\2\u011d\63\3\2\2\2\u011e\u011f")
        buf.write("\5\66\34\2\u011f\u0120\5\64\33\2\u0120\u0123\3\2\2\2\u0121")
        buf.write("\u0123\5\66\34\2\u0122\u011e\3\2\2\2\u0122\u0121\3\2\2")
        buf.write("\2\u0123\65\3\2\2\2\u0124\u0125\7<\2\2\u0125\u0126\5\22")
        buf.write("\n\2\u0126\u0127\7\63\2\2\u0127\67\3\2\2\2\u0128\u0129")
        buf.write("\7\n\2\2\u0129\u012a\7<\2\2\u012a\u012b\7\f\2\2\u012b")
        buf.write("\u012c\7.\2\2\u012c\u012d\5:\36\2\u012d\u012e\7/\2\2\u012e")
        buf.write("\u012f\7\63\2\2\u012f9\3\2\2\2\u0130\u0131\5<\37\2\u0131")
        buf.write("\u0132\5:\36\2\u0132\u0135\3\2\2\2\u0133\u0135\5<\37\2")
        buf.write("\u0134\u0130\3\2\2\2\u0134\u0133\3\2\2\2\u0135;\3\2\2")
        buf.write("\2\u0136\u0137\7<\2\2\u0137\u0139\5\26\f\2\u0138\u013a")
        buf.write("\5\22\n\2\u0139\u0138\3\2\2\2\u0139\u013a\3\2\2\2\u013a")
        buf.write("\u013b\3\2\2\2\u013b\u013c\7\63\2\2\u013c=\3\2\2\2\u013d")
        buf.write("\u013e\5,\27\2\u013e\u013f\5\f\7\2\u013f\u0140\5@!\2\u0140")
        buf.write("?\3\2\2\2\u0141\u0142\7.\2\2\u0142\u0143\5B\"\2\u0143")
        buf.write("\u0144\7/\2\2\u0144A\3\2\2\2\u0145\u0146\5D#\2\u0146\u0147")
        buf.write("\7\62\2\2\u0147\u0148\5B\"\2\u0148\u014b\3\2\2\2\u0149")
        buf.write("\u014b\5D#\2\u014a\u0145\3\2\2\2\u014a\u0149\3\2\2\2\u014b")
        buf.write("C\3\2\2\2\u014c\u014f\5N(\2\u014d\u014f\5@!\2\u014e\u014c")
        buf.write("\3\2\2\2\u014e\u014d\3\2\2\2\u014fE\3\2\2\2\u0150\u0151")
        buf.write("\7<\2\2\u0151\u0152\7.\2\2\u0152\u0153\5H%\2\u0153\u0154")
        buf.write("\7/\2\2\u0154G\3\2\2\2\u0155\u0158\5J&\2\u0156\u0158\3")
        buf.write("\2\2\2\u0157\u0155\3\2\2\2\u0157\u0156\3\2\2\2\u0158I")
        buf.write("\3\2\2\2\u0159\u015a\5L\'\2\u015a\u015b\7\62\2\2\u015b")
        buf.write("\u015c\5J&\2\u015c\u015f\3\2\2\2\u015d\u015f\5L\'\2\u015e")
        buf.write("\u0159\3\2\2\2\u015e\u015d\3\2\2\2\u015fK\3\2\2\2\u0160")
        buf.write("\u0161\7<\2\2\u0161\u0162\7\64\2\2\u0162\u0163\5N(\2\u0163")
        buf.write("M\3\2\2\2\u0164\u0165\b(\1\2\u0165\u0166\5P)\2\u0166\u016c")
        buf.write("\3\2\2\2\u0167\u0168\f\4\2\2\u0168\u0169\7\"\2\2\u0169")
        buf.write("\u016b\5P)\2\u016a\u0167\3\2\2\2\u016b\u016e\3\2\2\2\u016c")
        buf.write("\u016a\3\2\2\2\u016c\u016d\3\2\2\2\u016dO\3\2\2\2\u016e")
        buf.write("\u016c\3\2\2\2\u016f\u0170\b)\1\2\u0170\u0171\5R*\2\u0171")
        buf.write("\u0177\3\2\2\2\u0172\u0173\f\4\2\2\u0173\u0174\7!\2\2")
        buf.write("\u0174\u0176\5R*\2\u0175\u0172\3\2\2\2\u0176\u0179\3\2")
        buf.write("\2\2\u0177\u0175\3\2\2\2\u0177\u0178\3\2\2\2\u0178Q\3")
        buf.write("\2\2\2\u0179\u0177\3\2\2\2\u017a\u017b\b*\1\2\u017b\u017c")
        buf.write("\5T+\2\u017c\u0182\3\2\2\2\u017d\u017e\f\4\2\2\u017e\u017f")
        buf.write("\t\3\2\2\u017f\u0181\5T+\2\u0180\u017d\3\2\2\2\u0181\u0184")
        buf.write("\3\2\2\2\u0182\u0180\3\2\2\2\u0182\u0183\3\2\2\2\u0183")
        buf.write("S\3\2\2\2\u0184\u0182\3\2\2\2\u0185\u0186\b+\1\2\u0186")
        buf.write("\u0187\5V,\2\u0187\u018d\3\2\2\2\u0188\u0189\f\4\2\2\u0189")
        buf.write("\u018a\t\4\2\2\u018a\u018c\5V,\2\u018b\u0188\3\2\2\2\u018c")
        buf.write("\u018f\3\2\2\2\u018d\u018b\3\2\2\2\u018d\u018e\3\2\2\2")
        buf.write("\u018eU\3\2\2\2\u018f\u018d\3\2\2\2\u0190\u0191\b,\1\2")
        buf.write("\u0191\u0192\5X-\2\u0192\u0198\3\2\2\2\u0193\u0194\f\4")
        buf.write("\2\2\u0194\u0195\t\5\2\2\u0195\u0197\5X-\2\u0196\u0193")
        buf.write("\3\2\2\2\u0197\u019a\3\2\2\2\u0198\u0196\3\2\2\2\u0198")
        buf.write("\u0199\3\2\2\2\u0199W\3\2\2\2\u019a\u0198\3\2\2\2\u019b")
        buf.write("\u019c\t\6\2\2\u019c\u019f\5X-\2\u019d\u019f\5Z.\2\u019e")
        buf.write("\u019b\3\2\2\2\u019e\u019d\3\2\2\2\u019fY\3\2\2\2\u01a0")
        buf.write("\u01a1\b.\1\2\u01a1\u01a2\5\\/\2\u01a2\u01ad\3\2\2\2\u01a3")
        buf.write("\u01a4\f\5\2\2\u01a4\u01a5\7\60\2\2\u01a5\u01a6\5f\64")
        buf.write("\2\u01a6\u01a7\7\61\2\2\u01a7\u01ac\3\2\2\2\u01a8\u01a9")
        buf.write("\f\4\2\2\u01a9\u01aa\7+\2\2\u01aa\u01ac\5\\/\2\u01ab\u01a3")
        buf.write("\3\2\2\2\u01ab\u01a8\3\2\2\2\u01ac\u01af\3\2\2\2\u01ad")
        buf.write("\u01ab\3\2\2\2\u01ad\u01ae\3\2\2\2\u01ae[\3\2\2\2\u01af")
        buf.write("\u01ad\3\2\2\2\u01b0\u01b8\5d\63\2\u01b1\u01b8\7<\2\2")
        buf.write("\u01b2\u01b3\7,\2\2\u01b3\u01b4\5N(\2\u01b4\u01b5\7-\2")
        buf.write("\2\u01b5\u01b8\3\2\2\2\u01b6\u01b8\5^\60\2\u01b7\u01b0")
        buf.write("\3\2\2\2\u01b7\u01b1\3\2\2\2\u01b7\u01b2\3\2\2\2\u01b7")
        buf.write("\u01b6\3\2\2\2\u01b8]\3\2\2\2\u01b9\u01ba\7<\2\2\u01ba")
        buf.write("\u01bb\7,\2\2\u01bb\u01bc\5`\61\2\u01bc\u01bd\7-\2\2\u01bd")
        buf.write("_\3\2\2\2\u01be\u01c1\5b\62\2\u01bf\u01c1\3\2\2\2\u01c0")
        buf.write("\u01be\3\2\2\2\u01c0\u01bf\3\2\2\2\u01c1a\3\2\2\2\u01c2")
        buf.write("\u01c3\5N(\2\u01c3\u01c4\7\62\2\2\u01c4\u01c5\5b\62\2")
        buf.write("\u01c5\u01c8\3\2\2\2\u01c6\u01c8\5N(\2\u01c7\u01c2\3\2")
        buf.write("\2\2\u01c7\u01c6\3\2\2\2\u01c8c\3\2\2\2\u01c9\u01d0\7")
        buf.write("\65\2\2\u01ca\u01d0\7\66\2\2\u01cb\u01d0\7\67\2\2\u01cc")
        buf.write("\u01d0\7:\2\2\u01cd\u01d0\5> \2\u01ce\u01d0\5F$\2\u01cf")
        buf.write("\u01c9\3\2\2\2\u01cf\u01ca\3\2\2\2\u01cf\u01cb\3\2\2\2")
        buf.write("\u01cf\u01cc\3\2\2\2\u01cf\u01cd\3\2\2\2\u01cf\u01ce\3")
        buf.write("\2\2\2\u01d0e\3\2\2\2\u01d1\u01d2\t\7\2\2\u01d2g\3\2\2")
        buf.write("\2\u01d3\u01dc\5\6\4\2\u01d4\u01dc\5j\66\2\u01d5\u01dc")
        buf.write("\5n8\2\u01d6\u01dc\5z>\2\u01d7\u01dc\5\u0086D\2\u01d8")
        buf.write("\u01dc\5\u008aF\2\u01d9\u01dc\5\u0088E\2\u01da\u01dc\5")
        buf.write("\u008cG\2\u01db\u01d3\3\2\2\2\u01db\u01d4\3\2\2\2\u01db")
        buf.write("\u01d5\3\2\2\2\u01db\u01d6\3\2\2\2\u01db\u01d7\3\2\2\2")
        buf.write("\u01db\u01d8\3\2\2\2\u01db\u01d9\3\2\2\2\u01db\u01da\3")
        buf.write("\2\2\2\u01dci\3\2\2\2\u01dd\u01de\5l\67\2\u01de\u01df")
        buf.write("\t\b\2\2\u01df\u01e0\5N(\2\u01e0\u01e1\7\63\2\2\u01e1")
        buf.write("k\3\2\2\2\u01e2\u01e9\7<\2\2\u01e3\u01e4\7<\2\2\u01e4")
        buf.write("\u01e9\5,\27\2\u01e5\u01e6\7<\2\2\u01e6\u01e7\7+\2\2\u01e7")
        buf.write("\u01e9\7<\2\2\u01e8\u01e2\3\2\2\2\u01e8\u01e3\3\2\2\2")
        buf.write("\u01e8\u01e5\3\2\2\2\u01e9m\3\2\2\2\u01ea\u01eb\7\5\2")
        buf.write("\2\u01eb\u01ec\7,\2\2\u01ec\u01ed\5N(\2\u01ed\u01ef\7")
        buf.write("-\2\2\u01ee\u01f0\7\63\2\2\u01ef\u01ee\3\2\2\2\u01ef\u01f0")
        buf.write("\3\2\2\2\u01f0\u01f1\3\2\2\2\u01f1\u01f2\7.\2\2\u01f2")
        buf.write("\u01f3\5x=\2\u01f3\u01f5\7/\2\2\u01f4\u01f6\7\63\2\2\u01f5")
        buf.write("\u01f4\3\2\2\2\u01f5\u01f6\3\2\2\2\u01f6\u01f7\3\2\2\2")
        buf.write("\u01f7\u01f9\5p9\2\u01f8\u01fa\5t;\2\u01f9\u01f8\3\2\2")
        buf.write("\2\u01f9\u01fa\3\2\2\2\u01fa\u01fb\3\2\2\2\u01fb\u01fc")
        buf.write("\7\63\2\2\u01fco\3\2\2\2\u01fd\u0200\5r:\2\u01fe\u0200")
        buf.write("\3\2\2\2\u01ff\u01fd\3\2\2\2\u01ff\u01fe\3\2\2\2\u0200")
        buf.write("q\3\2\2\2\u0201\u0203\5v<\2\u0202\u0204\7\63\2\2\u0203")
        buf.write("\u0202\3\2\2\2\u0203\u0204\3\2\2\2\u0204\u0205\3\2\2\2")
        buf.write("\u0205\u0206\5r:\2\u0206\u0209\3\2\2\2\u0207\u0209\5v")
        buf.write("<\2\u0208\u0201\3\2\2\2\u0208\u0207\3\2\2\2\u0209s\3\2")
        buf.write("\2\2\u020a\u020b\7\6\2\2\u020b\u020c\7.\2\2\u020c\u020d")
        buf.write("\5x=\2\u020d\u020f\7/\2\2\u020e\u0210\7\63\2\2\u020f\u020e")
        buf.write("\3\2\2\2\u020f\u0210\3\2\2\2\u0210u\3\2\2\2\u0211\u0212")
        buf.write("\7\6\2\2\u0212\u0213\7\5\2\2\u0213\u0214\7,\2\2\u0214")
        buf.write("\u0215\5N(\2\u0215\u0217\7-\2\2\u0216\u0218\7\63\2\2\u0217")
        buf.write("\u0216\3\2\2\2\u0217\u0218\3\2\2\2\u0218\u0219\3\2\2\2")
        buf.write("\u0219\u021a\7.\2\2\u021a\u021b\5x=\2\u021b\u021d\7/\2")
        buf.write("\2\u021c\u021e\7\63\2\2\u021d\u021c\3\2\2\2\u021d\u021e")
        buf.write("\3\2\2\2\u021ew\3\2\2\2\u021f\u0220\5h\65\2\u0220\u0221")
        buf.write("\5x=\2\u0221\u0224\3\2\2\2\u0222\u0224\5h\65\2\u0223\u021f")
        buf.write("\3\2\2\2\u0223\u0222\3\2\2\2\u0224y\3\2\2\2\u0225\u0226")
        buf.write("\7\7\2\2\u0226\u0227\5|?\2\u0227\u0228\7.\2\2\u0228\u0229")
        buf.write("\5x=\2\u0229\u022a\7/\2\2\u022a\u022b\7\63\2\2\u022b{")
        buf.write("\3\2\2\2\u022c\u0230\5N(\2\u022d\u0230\5~@\2\u022e\u0230")
        buf.write("\5\u0084C\2\u022f\u022c\3\2\2\2\u022f\u022d\3\2\2\2\u022f")
        buf.write("\u022e\3\2\2\2\u0230}\3\2\2\2\u0231\u0232\5\u0080A\2\u0232")
        buf.write("\u0233\7\63\2\2\u0233\u0234\5N(\2\u0234\u0235\7\63\2\2")
        buf.write("\u0235\u0236\5\u0082B\2\u0236\177\3\2\2\2\u0237\u0238")
        buf.write("\7<\2\2\u0238\u0239\7$\2\2\u0239\u0242\5N(\2\u023a\u023b")
        buf.write("\7\22\2\2\u023b\u023d\7<\2\2\u023c\u023e\5\f\7\2\u023d")
        buf.write("\u023c\3\2\2\2\u023d\u023e\3\2\2\2\u023e\u023f\3\2\2\2")
        buf.write("\u023f\u0240\7*\2\2\u0240\u0242\5N(\2\u0241\u0237\3\2")
        buf.write("\2\2\u0241\u023a\3\2\2\2\u0242\u0081\3\2\2\2\u0243\u0244")
        buf.write("\5l\67\2\u0244\u0245\t\b\2\2\u0245\u0246\5N(\2\u0246\u0083")
        buf.write("\3\2\2\2\u0247\u0248\7<\2\2\u0248\u0249\7\62\2\2\u0249")
        buf.write("\u024a\7<\2\2\u024a\u024b\7$\2\2\u024b\u024c\7\25\2\2")
        buf.write("\u024c\u024d\7<\2\2\u024d\u0085\3\2\2\2\u024e\u024f\7")
        buf.write("\24\2\2\u024f\u0250\7\63\2\2\u0250\u0087\3\2\2\2\u0251")
        buf.write("\u0252\7\23\2\2\u0252\u0253\7\63\2\2\u0253\u0089\3\2\2")
        buf.write("\2\u0254\u0256\7\b\2\2\u0255\u0257\5N(\2\u0256\u0255\3")
        buf.write("\2\2\2\u0256\u0257\3\2\2\2\u0257\u0258\3\2\2\2\u0258\u0259")
        buf.write("\7\63\2\2\u0259\u008b\3\2\2\2\u025a\u025b\5^\60\2\u025b")
        buf.write("\u025c\7\63\2\2\u025c\u008d\3\2\2\2\65\u0095\u009c\u00a0")
        buf.write("\u00a5\u00b0\u00bc\u00c1\u00c8\u00d3\u00da\u00e0\u00e9")
        buf.write("\u00ed\u00f5\u0106\u010e\u0122\u0134\u0139\u014a\u014e")
        buf.write("\u0157\u015e\u016c\u0177\u0182\u018d\u0198\u019e\u01ab")
        buf.write("\u01ad\u01b7\u01c0\u01c7\u01cf\u01db\u01e8\u01ef\u01f5")
        buf.write("\u01f9\u01ff\u0203\u0208\u020f\u0217\u021d\u0223\u022f")
        buf.write("\u023d\u0241\u0256")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'if'", "'else'", 
                     "'for'", "'return'", "'func'", "'type'", "'struct'", 
                     "'interface'", "'string'", "'int'", "'float'", "'boolean'", 
                     "'const'", "'var'", "'continue'", "'break'", "'range'", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", "'!='", 
                     "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", "'!'", 
                     "':='", "'+='", "'-='", "'*='", "'/='", "'%='", "'='", 
                     "'.'", "'('", "')'", "'{'", "'}'", "'['", "']'", "','", 
                     "';'", "':'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'nil'" ]

    symbolicNames = [ "<INVALID>", "LINE_CMT", "BLOCK_COMT", "IF", "ELSE", 
                      "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", 
                      "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", "VAR", 
                      "CONTINUE", "BREAK", "RANGE", "ADD", "SUB", "MUL", 
                      "DIV", "MOD", "EQUAL", "NEQUAL", "LESS", "LESSEQ", 
                      "GREAT", "GREATEQ", "AND", "OR", "NEG", "ASSIGN", 
                      "ADDASGN", "SUBASGN", "MULASGN", "DIVASGN", "MODASGN", 
                      "INIASSIGN", "DOT", "LPAR", "RPAR", "LCUR", "RCUR", 
                      "LSQU", "RSQU", "COMMA", "SEMICOL", "COL", "INT_LIT", 
                      "FLOAT_LIT", "STRING_LIT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "BOOL_LIT", "NIL_LIT", "ID", "NL", "WS", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decllist = 1
    RULE_decl = 2
    RULE_typdecl = 3
    RULE_vardecl = 4
    RULE_typ = 5
    RULE_condecl = 6
    RULE_funcdecl = 7
    RULE_functyp = 8
    RULE_arraytyp = 9
    RULE_para = 10
    RULE_paralist = 11
    RULE_paralistprime = 12
    RULE_paraelement = 13
    RULE_arraypara = 14
    RULE_nullabledimension = 15
    RULE_nulldimen = 16
    RULE_idlist = 17
    RULE_stm = 18
    RULE_strucinst = 19
    RULE_arraydecl = 20
    RULE_dimension = 21
    RULE_dimen = 22
    RULE_structdecl = 23
    RULE_field = 24
    RULE_fieldlistprime = 25
    RULE_fieldele = 26
    RULE_interfacedecl = 27
    RULE_methodprime = 28
    RULE_method = 29
    RULE_array_lit = 30
    RULE_arrayini = 31
    RULE_arrayinilist = 32
    RULE_arrayiniele = 33
    RULE_struct_lit = 34
    RULE_fieldinilist = 35
    RULE_fieldiniprime = 36
    RULE_fieldini = 37
    RULE_expr = 38
    RULE_expr1 = 39
    RULE_expr2 = 40
    RULE_expr3 = 41
    RULE_expr4 = 42
    RULE_expr5 = 43
    RULE_expr6 = 44
    RULE_expr7 = 45
    RULE_functioncall = 46
    RULE_exprlist = 47
    RULE_exprprime = 48
    RULE_literal = 49
    RULE_arrayaccess = 50
    RULE_statement = 51
    RULE_assignstm = 52
    RULE_lhs = 53
    RULE_ifstm = 54
    RULE_eliflist = 55
    RULE_elifstmlist = 56
    RULE_elstm = 57
    RULE_elifstm = 58
    RULE_statementlist = 59
    RULE_forstm = 60
    RULE_condi = 61
    RULE_inifor = 62
    RULE_forvarini = 63
    RULE_assignfor = 64
    RULE_rangefor = 65
    RULE_breakstm = 66
    RULE_continuestm = 67
    RULE_returnstm = 68
    RULE_callstm = 69

    ruleNames =  [ "program", "decllist", "decl", "typdecl", "vardecl", 
                   "typ", "condecl", "funcdecl", "functyp", "arraytyp", 
                   "para", "paralist", "paralistprime", "paraelement", "arraypara", 
                   "nullabledimension", "nulldimen", "idlist", "stm", "strucinst", 
                   "arraydecl", "dimension", "dimen", "structdecl", "field", 
                   "fieldlistprime", "fieldele", "interfacedecl", "methodprime", 
                   "method", "array_lit", "arrayini", "arrayinilist", "arrayiniele", 
                   "struct_lit", "fieldinilist", "fieldiniprime", "fieldini", 
                   "expr", "expr1", "expr2", "expr3", "expr4", "expr5", 
                   "expr6", "expr7", "functioncall", "exprlist", "exprprime", 
                   "literal", "arrayaccess", "statement", "assignstm", "lhs", 
                   "ifstm", "eliflist", "elifstmlist", "elstm", "elifstm", 
                   "statementlist", "forstm", "condi", "inifor", "forvarini", 
                   "assignfor", "rangefor", "breakstm", "continuestm", "returnstm", 
                   "callstm" ]

    EOF = Token.EOF
    LINE_CMT=1
    BLOCK_COMT=2
    IF=3
    ELSE=4
    FOR=5
    RETURN=6
    FUNC=7
    TYPE=8
    STRUCT=9
    INTERFACE=10
    STRING=11
    INT=12
    FLOAT=13
    BOOLEAN=14
    CONST=15
    VAR=16
    CONTINUE=17
    BREAK=18
    RANGE=19
    ADD=20
    SUB=21
    MUL=22
    DIV=23
    MOD=24
    EQUAL=25
    NEQUAL=26
    LESS=27
    LESSEQ=28
    GREAT=29
    GREATEQ=30
    AND=31
    OR=32
    NEG=33
    ASSIGN=34
    ADDASGN=35
    SUBASGN=36
    MULASGN=37
    DIVASGN=38
    MODASGN=39
    INIASSIGN=40
    DOT=41
    LPAR=42
    RPAR=43
    LCUR=44
    RCUR=45
    LSQU=46
    RSQU=47
    COMMA=48
    SEMICOL=49
    COL=50
    INT_LIT=51
    FLOAT_LIT=52
    STRING_LIT=53
    UNCLOSE_STRING=54
    ILLEGAL_ESCAPE=55
    BOOL_LIT=56
    NIL_LIT=57
    ID=58
    NL=59
    WS=60
    ERROR_CHAR=61

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decllist(self):
            return self.getTypedRuleContext(MiniGoParser.DecllistContext,0)


        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.decllist()
            self.state = 141
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecllistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(MiniGoParser.DeclContext,0)


        def decllist(self):
            return self.getTypedRuleContext(MiniGoParser.DecllistContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decllist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecllist" ):
                return visitor.visitDecllist(self)
            else:
                return visitor.visitChildren(self)




    def decllist(self):

        localctx = MiniGoParser.DecllistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decllist)
        try:
            self.state = 147
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 143
                self.decl()
                self.state = 144
                self.decllist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 146
                self.decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcdecl(self):
            return self.getTypedRuleContext(MiniGoParser.FuncdeclContext,0)


        def vardecl(self):
            return self.getTypedRuleContext(MiniGoParser.VardeclContext,0)


        def condecl(self):
            return self.getTypedRuleContext(MiniGoParser.CondeclContext,0)


        def arraydecl(self):
            return self.getTypedRuleContext(MiniGoParser.ArraydeclContext,0)


        def typdecl(self):
            return self.getTypedRuleContext(MiniGoParser.TypdeclContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = MiniGoParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 154
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 149
                self.funcdecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 150
                self.vardecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 151
                self.condecl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 152
                self.arraydecl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 153
                self.typdecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def structdecl(self):
            return self.getTypedRuleContext(MiniGoParser.StructdeclContext,0)


        def interfacedecl(self):
            return self.getTypedRuleContext(MiniGoParser.InterfacedeclContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_typdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypdecl" ):
                return visitor.visitTypdecl(self)
            else:
                return visitor.visitChildren(self)




    def typdecl(self):

        localctx = MiniGoParser.TypdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_typdecl)
        try:
            self.state = 158
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 156
                self.structdecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 157
                self.interfacedecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def INIASSIGN(self):
            return self.getToken(MiniGoParser.INIASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def SEMICOL(self):
            return self.getToken(MiniGoParser.SEMICOL, 0)

        def typ(self):
            return self.getTypedRuleContext(MiniGoParser.TypContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = MiniGoParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_vardecl)
        self._la = 0 # Token type
        try:
            self.state = 174
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.match(MiniGoParser.VAR)
                self.state = 161
                self.match(MiniGoParser.ID)
                self.state = 163
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.ID))) != 0):
                    self.state = 162
                    self.typ()


                self.state = 165
                self.match(MiniGoParser.INIASSIGN)
                self.state = 166
                self.expr(0)
                self.state = 167
                self.match(MiniGoParser.SEMICOL)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 169
                self.match(MiniGoParser.VAR)
                self.state = 170
                self.match(MiniGoParser.ID)
                self.state = 171
                self.typ()
                self.state = 172
                self.match(MiniGoParser.SEMICOL)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_typ

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTyp" ):
                return visitor.visitTyp(self)
            else:
                return visitor.visitChildren(self)




    def typ(self):

        localctx = MiniGoParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.ID))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(MiniGoParser.CONST, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def INIASSIGN(self):
            return self.getToken(MiniGoParser.INIASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def SEMICOL(self):
            return self.getToken(MiniGoParser.SEMICOL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_condecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondecl" ):
                return visitor.visitCondecl(self)
            else:
                return visitor.visitChildren(self)




    def condecl(self):

        localctx = MiniGoParser.CondeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_condecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(MiniGoParser.CONST)
            self.state = 179
            self.match(MiniGoParser.ID)
            self.state = 180
            self.match(MiniGoParser.INIASSIGN)
            self.state = 181
            self.expr(0)
            self.state = 182
            self.match(MiniGoParser.SEMICOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def para(self):
            return self.getTypedRuleContext(MiniGoParser.ParaContext,0)


        def stm(self):
            return self.getTypedRuleContext(MiniGoParser.StmContext,0)


        def SEMICOL(self):
            return self.getToken(MiniGoParser.SEMICOL, 0)

        def strucinst(self):
            return self.getTypedRuleContext(MiniGoParser.StrucinstContext,0)


        def functyp(self):
            return self.getTypedRuleContext(MiniGoParser.FunctypContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_funcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def funcdecl(self):

        localctx = MiniGoParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_funcdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(MiniGoParser.FUNC)
            self.state = 186
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.LPAR:
                self.state = 185
                self.strucinst()


            self.state = 188
            self.match(MiniGoParser.ID)
            self.state = 189
            self.para()
            self.state = 191
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSQU) | (1 << MiniGoParser.ID))) != 0):
                self.state = 190
                self.functyp()


            self.state = 193
            self.stm()
            self.state = 194
            self.match(MiniGoParser.SEMICOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(MiniGoParser.TypContext,0)


        def arraytyp(self):
            return self.getTypedRuleContext(MiniGoParser.ArraytypContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_functyp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctyp" ):
                return visitor.visitFunctyp(self)
            else:
                return visitor.visitChildren(self)




    def functyp(self):

        localctx = MiniGoParser.FunctypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_functyp)
        try:
            self.state = 198
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 196
                self.typ()
                pass
            elif token in [MiniGoParser.LSQU]:
                self.enterOuterAlt(localctx, 2)
                self.state = 197
                self.arraytyp()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraytypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nullabledimension(self):
            return self.getTypedRuleContext(MiniGoParser.NullabledimensionContext,0)


        def typ(self):
            return self.getTypedRuleContext(MiniGoParser.TypContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arraytyp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraytyp" ):
                return visitor.visitArraytyp(self)
            else:
                return visitor.visitChildren(self)




    def arraytyp(self):

        localctx = MiniGoParser.ArraytypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_arraytyp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.nullabledimension()
            self.state = 201
            self.typ()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAR(self):
            return self.getToken(MiniGoParser.LPAR, 0)

        def paralist(self):
            return self.getTypedRuleContext(MiniGoParser.ParalistContext,0)


        def RPAR(self):
            return self.getToken(MiniGoParser.RPAR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_para

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara" ):
                return visitor.visitPara(self)
            else:
                return visitor.visitChildren(self)




    def para(self):

        localctx = MiniGoParser.ParaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_para)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.match(MiniGoParser.LPAR)
            self.state = 204
            self.paralist()
            self.state = 205
            self.match(MiniGoParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParalistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paralistprime(self):
            return self.getTypedRuleContext(MiniGoParser.ParalistprimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_paralist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParalist" ):
                return visitor.visitParalist(self)
            else:
                return visitor.visitChildren(self)




    def paralist(self):

        localctx = MiniGoParser.ParalistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_paralist)
        try:
            self.state = 209
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 207
                self.paralistprime()
                pass
            elif token in [MiniGoParser.RPAR]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParalistprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paraelement(self):
            return self.getTypedRuleContext(MiniGoParser.ParaelementContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def paralistprime(self):
            return self.getTypedRuleContext(MiniGoParser.ParalistprimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_paralistprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParalistprime" ):
                return visitor.visitParalistprime(self)
            else:
                return visitor.visitChildren(self)




    def paralistprime(self):

        localctx = MiniGoParser.ParalistprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_paralistprime)
        try:
            self.state = 216
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 211
                self.paraelement()
                self.state = 212
                self.match(MiniGoParser.COMMA)
                self.state = 213
                self.paralistprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 215
                self.paraelement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParaelementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idlist(self):
            return self.getTypedRuleContext(MiniGoParser.IdlistContext,0)


        def typ(self):
            return self.getTypedRuleContext(MiniGoParser.TypContext,0)


        def arraypara(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayparaContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_paraelement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParaelement" ):
                return visitor.visitParaelement(self)
            else:
                return visitor.visitChildren(self)




    def paraelement(self):

        localctx = MiniGoParser.ParaelementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_paraelement)
        try:
            self.state = 222
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 218
                self.idlist()
                self.state = 219
                self.typ()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 221
                self.arraypara()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayparaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def nullabledimension(self):
            return self.getTypedRuleContext(MiniGoParser.NullabledimensionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arraypara

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraypara" ):
                return visitor.visitArraypara(self)
            else:
                return visitor.visitChildren(self)




    def arraypara(self):

        localctx = MiniGoParser.ArrayparaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_arraypara)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.match(MiniGoParser.ID)
            self.state = 225
            self.nullabledimension()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NullabledimensionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nulldimen(self):
            return self.getTypedRuleContext(MiniGoParser.NulldimenContext,0)


        def nullabledimension(self):
            return self.getTypedRuleContext(MiniGoParser.NullabledimensionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_nullabledimension

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNullabledimension" ):
                return visitor.visitNullabledimension(self)
            else:
                return visitor.visitChildren(self)




    def nullabledimension(self):

        localctx = MiniGoParser.NullabledimensionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_nullabledimension)
        try:
            self.state = 231
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 227
                self.nulldimen()
                self.state = 228
                self.nullabledimension()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 230
                self.nulldimen()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NulldimenContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSQU(self):
            return self.getToken(MiniGoParser.LSQU, 0)

        def RSQU(self):
            return self.getToken(MiniGoParser.RSQU, 0)

        def arrayaccess(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayaccessContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_nulldimen

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNulldimen" ):
                return visitor.visitNulldimen(self)
            else:
                return visitor.visitChildren(self)




    def nulldimen(self):

        localctx = MiniGoParser.NulldimenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_nulldimen)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.match(MiniGoParser.LSQU)
            self.state = 235
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.INT_LIT or _la==MiniGoParser.ID:
                self.state = 234
                self.arrayaccess()


            self.state = 237
            self.match(MiniGoParser.RSQU)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def idlist(self):
            return self.getTypedRuleContext(MiniGoParser.IdlistContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_idlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdlist" ):
                return visitor.visitIdlist(self)
            else:
                return visitor.visitChildren(self)




    def idlist(self):

        localctx = MiniGoParser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_idlist)
        try:
            self.state = 243
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 239
                self.match(MiniGoParser.ID)
                self.state = 240
                self.match(MiniGoParser.COMMA)
                self.state = 241
                self.idlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 242
                self.match(MiniGoParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCUR(self):
            return self.getToken(MiniGoParser.LCUR, 0)

        def statementlist(self):
            return self.getTypedRuleContext(MiniGoParser.StatementlistContext,0)


        def RCUR(self):
            return self.getToken(MiniGoParser.RCUR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStm" ):
                return visitor.visitStm(self)
            else:
                return visitor.visitChildren(self)




    def stm(self):

        localctx = MiniGoParser.StmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.match(MiniGoParser.LCUR)
            self.state = 246
            self.statementlist()
            self.state = 247
            self.match(MiniGoParser.RCUR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StrucinstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAR(self):
            return self.getToken(MiniGoParser.LPAR, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def RPAR(self):
            return self.getToken(MiniGoParser.RPAR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_strucinst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStrucinst" ):
                return visitor.visitStrucinst(self)
            else:
                return visitor.visitChildren(self)




    def strucinst(self):

        localctx = MiniGoParser.StrucinstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_strucinst)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.match(MiniGoParser.LPAR)
            self.state = 250
            self.match(MiniGoParser.ID)
            self.state = 251
            self.match(MiniGoParser.ID)
            self.state = 252
            self.match(MiniGoParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraydeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def dimension(self):
            return self.getTypedRuleContext(MiniGoParser.DimensionContext,0)


        def typ(self):
            return self.getTypedRuleContext(MiniGoParser.TypContext,0)


        def SEMICOL(self):
            return self.getToken(MiniGoParser.SEMICOL, 0)

        def INIASSIGN(self):
            return self.getToken(MiniGoParser.INIASSIGN, 0)

        def array_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Array_litContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arraydecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraydecl" ):
                return visitor.visitArraydecl(self)
            else:
                return visitor.visitChildren(self)




    def arraydecl(self):

        localctx = MiniGoParser.ArraydeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_arraydecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.match(MiniGoParser.VAR)
            self.state = 255
            self.match(MiniGoParser.ID)
            self.state = 256
            self.dimension()
            self.state = 257
            self.typ()
            self.state = 260
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.INIASSIGN:
                self.state = 258
                self.match(MiniGoParser.INIASSIGN)
                self.state = 259
                self.array_lit()


            self.state = 262
            self.match(MiniGoParser.SEMICOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimensionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dimen(self):
            return self.getTypedRuleContext(MiniGoParser.DimenContext,0)


        def dimension(self):
            return self.getTypedRuleContext(MiniGoParser.DimensionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_dimension

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimension" ):
                return visitor.visitDimension(self)
            else:
                return visitor.visitChildren(self)




    def dimension(self):

        localctx = MiniGoParser.DimensionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_dimension)
        try:
            self.state = 268
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 264
                self.dimen()
                self.state = 265
                self.dimension()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 267
                self.dimen()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimenContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSQU(self):
            return self.getToken(MiniGoParser.LSQU, 0)

        def arrayaccess(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayaccessContext,0)


        def RSQU(self):
            return self.getToken(MiniGoParser.RSQU, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_dimen

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimen" ):
                return visitor.visitDimen(self)
            else:
                return visitor.visitChildren(self)




    def dimen(self):

        localctx = MiniGoParser.DimenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_dimen)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.match(MiniGoParser.LSQU)
            self.state = 271
            self.arrayaccess()
            self.state = 272
            self.match(MiniGoParser.RSQU)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def STRUCT(self):
            return self.getToken(MiniGoParser.STRUCT, 0)

        def field(self):
            return self.getTypedRuleContext(MiniGoParser.FieldContext,0)


        def SEMICOL(self):
            return self.getToken(MiniGoParser.SEMICOL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_structdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructdecl" ):
                return visitor.visitStructdecl(self)
            else:
                return visitor.visitChildren(self)




    def structdecl(self):

        localctx = MiniGoParser.StructdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_structdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.match(MiniGoParser.TYPE)
            self.state = 275
            self.match(MiniGoParser.ID)
            self.state = 276
            self.match(MiniGoParser.STRUCT)
            self.state = 277
            self.field()
            self.state = 278
            self.match(MiniGoParser.SEMICOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCUR(self):
            return self.getToken(MiniGoParser.LCUR, 0)

        def fieldlistprime(self):
            return self.getTypedRuleContext(MiniGoParser.FieldlistprimeContext,0)


        def RCUR(self):
            return self.getToken(MiniGoParser.RCUR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_field

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField" ):
                return visitor.visitField(self)
            else:
                return visitor.visitChildren(self)




    def field(self):

        localctx = MiniGoParser.FieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.match(MiniGoParser.LCUR)
            self.state = 281
            self.fieldlistprime()
            self.state = 282
            self.match(MiniGoParser.RCUR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldlistprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fieldele(self):
            return self.getTypedRuleContext(MiniGoParser.FieldeleContext,0)


        def fieldlistprime(self):
            return self.getTypedRuleContext(MiniGoParser.FieldlistprimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_fieldlistprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldlistprime" ):
                return visitor.visitFieldlistprime(self)
            else:
                return visitor.visitChildren(self)




    def fieldlistprime(self):

        localctx = MiniGoParser.FieldlistprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_fieldlistprime)
        try:
            self.state = 288
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 284
                self.fieldele()
                self.state = 285
                self.fieldlistprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 287
                self.fieldele()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldeleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def functyp(self):
            return self.getTypedRuleContext(MiniGoParser.FunctypContext,0)


        def SEMICOL(self):
            return self.getToken(MiniGoParser.SEMICOL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_fieldele

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldele" ):
                return visitor.visitFieldele(self)
            else:
                return visitor.visitChildren(self)




    def fieldele(self):

        localctx = MiniGoParser.FieldeleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_fieldele)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            self.match(MiniGoParser.ID)
            self.state = 291
            self.functyp()
            self.state = 292
            self.match(MiniGoParser.SEMICOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfacedeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def INTERFACE(self):
            return self.getToken(MiniGoParser.INTERFACE, 0)

        def LCUR(self):
            return self.getToken(MiniGoParser.LCUR, 0)

        def methodprime(self):
            return self.getTypedRuleContext(MiniGoParser.MethodprimeContext,0)


        def RCUR(self):
            return self.getToken(MiniGoParser.RCUR, 0)

        def SEMICOL(self):
            return self.getToken(MiniGoParser.SEMICOL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_interfacedecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfacedecl" ):
                return visitor.visitInterfacedecl(self)
            else:
                return visitor.visitChildren(self)




    def interfacedecl(self):

        localctx = MiniGoParser.InterfacedeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_interfacedecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self.match(MiniGoParser.TYPE)
            self.state = 295
            self.match(MiniGoParser.ID)
            self.state = 296
            self.match(MiniGoParser.INTERFACE)
            self.state = 297
            self.match(MiniGoParser.LCUR)
            self.state = 298
            self.methodprime()
            self.state = 299
            self.match(MiniGoParser.RCUR)
            self.state = 300
            self.match(MiniGoParser.SEMICOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def method(self):
            return self.getTypedRuleContext(MiniGoParser.MethodContext,0)


        def methodprime(self):
            return self.getTypedRuleContext(MiniGoParser.MethodprimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_methodprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodprime" ):
                return visitor.visitMethodprime(self)
            else:
                return visitor.visitChildren(self)




    def methodprime(self):

        localctx = MiniGoParser.MethodprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_methodprime)
        try:
            self.state = 306
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 302
                self.method()
                self.state = 303
                self.methodprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 305
                self.method()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def para(self):
            return self.getTypedRuleContext(MiniGoParser.ParaContext,0)


        def SEMICOL(self):
            return self.getToken(MiniGoParser.SEMICOL, 0)

        def functyp(self):
            return self.getTypedRuleContext(MiniGoParser.FunctypContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod" ):
                return visitor.visitMethod(self)
            else:
                return visitor.visitChildren(self)




    def method(self):

        localctx = MiniGoParser.MethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self.match(MiniGoParser.ID)
            self.state = 309
            self.para()
            self.state = 311
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSQU) | (1 << MiniGoParser.ID))) != 0):
                self.state = 310
                self.functyp()


            self.state = 313
            self.match(MiniGoParser.SEMICOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dimension(self):
            return self.getTypedRuleContext(MiniGoParser.DimensionContext,0)


        def typ(self):
            return self.getTypedRuleContext(MiniGoParser.TypContext,0)


        def arrayini(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayiniContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_lit" ):
                return visitor.visitArray_lit(self)
            else:
                return visitor.visitChildren(self)




    def array_lit(self):

        localctx = MiniGoParser.Array_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_array_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.dimension()
            self.state = 316
            self.typ()
            self.state = 317
            self.arrayini()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayiniContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCUR(self):
            return self.getToken(MiniGoParser.LCUR, 0)

        def arrayinilist(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayinilistContext,0)


        def RCUR(self):
            return self.getToken(MiniGoParser.RCUR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayini

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayini" ):
                return visitor.visitArrayini(self)
            else:
                return visitor.visitChildren(self)




    def arrayini(self):

        localctx = MiniGoParser.ArrayiniContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_arrayini)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.match(MiniGoParser.LCUR)
            self.state = 320
            self.arrayinilist()
            self.state = 321
            self.match(MiniGoParser.RCUR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayinilistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrayiniele(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayinieleContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def arrayinilist(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayinilistContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayinilist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayinilist" ):
                return visitor.visitArrayinilist(self)
            else:
                return visitor.visitChildren(self)




    def arrayinilist(self):

        localctx = MiniGoParser.ArrayinilistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_arrayinilist)
        try:
            self.state = 328
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 323
                self.arrayiniele()
                self.state = 324
                self.match(MiniGoParser.COMMA)
                self.state = 325
                self.arrayinilist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 327
                self.arrayiniele()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayinieleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def arrayini(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayiniContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayiniele

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayiniele" ):
                return visitor.visitArrayiniele(self)
            else:
                return visitor.visitChildren(self)




    def arrayiniele(self):

        localctx = MiniGoParser.ArrayinieleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_arrayiniele)
        try:
            self.state = 332
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SUB, MiniGoParser.NEG, MiniGoParser.LPAR, MiniGoParser.LSQU, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT, MiniGoParser.BOOL_LIT, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 330
                self.expr(0)
                pass
            elif token in [MiniGoParser.LCUR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 331
                self.arrayini()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LCUR(self):
            return self.getToken(MiniGoParser.LCUR, 0)

        def fieldinilist(self):
            return self.getTypedRuleContext(MiniGoParser.FieldinilistContext,0)


        def RCUR(self):
            return self.getToken(MiniGoParser.RCUR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_lit" ):
                return visitor.visitStruct_lit(self)
            else:
                return visitor.visitChildren(self)




    def struct_lit(self):

        localctx = MiniGoParser.Struct_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_struct_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self.match(MiniGoParser.ID)
            self.state = 335
            self.match(MiniGoParser.LCUR)
            self.state = 336
            self.fieldinilist()
            self.state = 337
            self.match(MiniGoParser.RCUR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldinilistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fieldiniprime(self):
            return self.getTypedRuleContext(MiniGoParser.FieldiniprimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_fieldinilist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldinilist" ):
                return visitor.visitFieldinilist(self)
            else:
                return visitor.visitChildren(self)




    def fieldinilist(self):

        localctx = MiniGoParser.FieldinilistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_fieldinilist)
        try:
            self.state = 341
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 339
                self.fieldiniprime()
                pass
            elif token in [MiniGoParser.RCUR]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldiniprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fieldini(self):
            return self.getTypedRuleContext(MiniGoParser.FieldiniContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def fieldiniprime(self):
            return self.getTypedRuleContext(MiniGoParser.FieldiniprimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_fieldiniprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldiniprime" ):
                return visitor.visitFieldiniprime(self)
            else:
                return visitor.visitChildren(self)




    def fieldiniprime(self):

        localctx = MiniGoParser.FieldiniprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_fieldiniprime)
        try:
            self.state = 348
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 343
                self.fieldini()
                self.state = 344
                self.match(MiniGoParser.COMMA)
                self.state = 345
                self.fieldiniprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 347
                self.fieldini()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldiniContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COL(self):
            return self.getToken(MiniGoParser.COL, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_fieldini

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldini" ):
                return visitor.visitFieldini(self)
            else:
                return visitor.visitChildren(self)




    def fieldini(self):

        localctx = MiniGoParser.FieldiniContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_fieldini)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self.match(MiniGoParser.ID)
            self.state = 351
            self.match(MiniGoParser.COL)
            self.state = 352
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self):
            return self.getTypedRuleContext(MiniGoParser.Expr1Context,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def OR(self):
            return self.getToken(MiniGoParser.OR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
            self.expr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 362
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 357
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 358
                    self.match(MiniGoParser.OR)
                    self.state = 359
                    self.expr1(0) 
                self.state = 364
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self):
            return self.getTypedRuleContext(MiniGoParser.Expr2Context,0)


        def expr1(self):
            return self.getTypedRuleContext(MiniGoParser.Expr1Context,0)


        def AND(self):
            return self.getToken(MiniGoParser.AND, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)



    def expr1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_expr1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 373
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 368
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 369
                    self.match(MiniGoParser.AND)
                    self.state = 370
                    self.expr2(0) 
                self.state = 375
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(MiniGoParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(MiniGoParser.Expr2Context,0)


        def EQUAL(self):
            return self.getToken(MiniGoParser.EQUAL, 0)

        def NEQUAL(self):
            return self.getToken(MiniGoParser.NEQUAL, 0)

        def LESS(self):
            return self.getToken(MiniGoParser.LESS, 0)

        def LESSEQ(self):
            return self.getToken(MiniGoParser.LESSEQ, 0)

        def GREAT(self):
            return self.getToken(MiniGoParser.GREAT, 0)

        def GREATEQ(self):
            return self.getToken(MiniGoParser.GREATEQ, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 384
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 379
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 380
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQUAL) | (1 << MiniGoParser.NEQUAL) | (1 << MiniGoParser.LESS) | (1 << MiniGoParser.LESSEQ) | (1 << MiniGoParser.GREAT) | (1 << MiniGoParser.GREATEQ))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 381
                    self.expr3(0) 
                self.state = 386
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(MiniGoParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(MiniGoParser.Expr3Context,0)


        def ADD(self):
            return self.getToken(MiniGoParser.ADD, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 388
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 395
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 390
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 391
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.ADD or _la==MiniGoParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 392
                    self.expr4(0) 
                self.state = 397
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(MiniGoParser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(MiniGoParser.Expr4Context,0)


        def MUL(self):
            return self.getToken(MiniGoParser.MUL, 0)

        def DIV(self):
            return self.getToken(MiniGoParser.DIV, 0)

        def MOD(self):
            return self.getToken(MiniGoParser.MOD, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 84
        self.enterRecursionRule(localctx, 84, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 406
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 401
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 402
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 403
                    self.expr5() 
                self.state = 408
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(MiniGoParser.Expr5Context,0)


        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def NEG(self):
            return self.getToken(MiniGoParser.NEG, 0)

        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = MiniGoParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_expr5)
        self._la = 0 # Token type
        try:
            self.state = 412
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SUB, MiniGoParser.NEG]:
                self.enterOuterAlt(localctx, 1)
                self.state = 409
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.SUB or _la==MiniGoParser.NEG):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 410
                self.expr5()
                pass
            elif token in [MiniGoParser.LPAR, MiniGoParser.LSQU, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT, MiniGoParser.BOOL_LIT, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 411
                self.expr6(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr7(self):
            return self.getTypedRuleContext(MiniGoParser.Expr7Context,0)


        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


        def LSQU(self):
            return self.getToken(MiniGoParser.LSQU, 0)

        def arrayaccess(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayaccessContext,0)


        def RSQU(self):
            return self.getToken(MiniGoParser.RSQU, 0)

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)



    def expr6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 88
        self.enterRecursionRule(localctx, 88, self.RULE_expr6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
            self.expr7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 427
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 425
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expr6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 417
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 418
                        self.match(MiniGoParser.LSQU)
                        self.state = 419
                        self.arrayaccess()
                        self.state = 420
                        self.match(MiniGoParser.RSQU)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expr6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 422
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 423
                        self.match(MiniGoParser.DOT)
                        self.state = 424
                        self.expr7()
                        pass

             
                self.state = 429
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAR(self):
            return self.getToken(MiniGoParser.LPAR, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RPAR(self):
            return self.getToken(MiniGoParser.RPAR, 0)

        def functioncall(self):
            return self.getTypedRuleContext(MiniGoParser.FunctioncallContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)




    def expr7(self):

        localctx = MiniGoParser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_expr7)
        try:
            self.state = 437
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 430
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 431
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 432
                self.match(MiniGoParser.LPAR)
                self.state = 433
                self.expr(0)
                self.state = 434
                self.match(MiniGoParser.RPAR)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 436
                self.functioncall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctioncallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAR(self):
            return self.getToken(MiniGoParser.LPAR, 0)

        def exprlist(self):
            return self.getTypedRuleContext(MiniGoParser.ExprlistContext,0)


        def RPAR(self):
            return self.getToken(MiniGoParser.RPAR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_functioncall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctioncall" ):
                return visitor.visitFunctioncall(self)
            else:
                return visitor.visitChildren(self)




    def functioncall(self):

        localctx = MiniGoParser.FunctioncallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_functioncall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 439
            self.match(MiniGoParser.ID)
            self.state = 440
            self.match(MiniGoParser.LPAR)
            self.state = 441
            self.exprlist()
            self.state = 442
            self.match(MiniGoParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprprime(self):
            return self.getTypedRuleContext(MiniGoParser.ExprprimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_exprlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprlist" ):
                return visitor.visitExprlist(self)
            else:
                return visitor.visitChildren(self)




    def exprlist(self):

        localctx = MiniGoParser.ExprlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_exprlist)
        try:
            self.state = 446
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SUB, MiniGoParser.NEG, MiniGoParser.LPAR, MiniGoParser.LSQU, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT, MiniGoParser.BOOL_LIT, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 444
                self.exprprime()
                pass
            elif token in [MiniGoParser.RPAR]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def exprprime(self):
            return self.getTypedRuleContext(MiniGoParser.ExprprimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_exprprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprprime" ):
                return visitor.visitExprprime(self)
            else:
                return visitor.visitChildren(self)




    def exprprime(self):

        localctx = MiniGoParser.ExprprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_exprprime)
        try:
            self.state = 453
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 448
                self.expr(0)
                self.state = 449
                self.match(MiniGoParser.COMMA)
                self.state = 450
                self.exprprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 452
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(MiniGoParser.FLOAT_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(MiniGoParser.STRING_LIT, 0)

        def BOOL_LIT(self):
            return self.getToken(MiniGoParser.BOOL_LIT, 0)

        def array_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Array_litContext,0)


        def struct_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_litContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = MiniGoParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_literal)
        try:
            self.state = 461
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 455
                self.match(MiniGoParser.INT_LIT)
                pass
            elif token in [MiniGoParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 456
                self.match(MiniGoParser.FLOAT_LIT)
                pass
            elif token in [MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 457
                self.match(MiniGoParser.STRING_LIT)
                pass
            elif token in [MiniGoParser.BOOL_LIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 458
                self.match(MiniGoParser.BOOL_LIT)
                pass
            elif token in [MiniGoParser.LSQU]:
                self.enterOuterAlt(localctx, 5)
                self.state = 459
                self.array_lit()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 460
                self.struct_lit()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayaccessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayaccess

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayaccess" ):
                return visitor.visitArrayaccess(self)
            else:
                return visitor.visitChildren(self)




    def arrayaccess(self):

        localctx = MiniGoParser.ArrayaccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_arrayaccess)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 463
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.INT_LIT or _la==MiniGoParser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(MiniGoParser.DeclContext,0)


        def assignstm(self):
            return self.getTypedRuleContext(MiniGoParser.AssignstmContext,0)


        def ifstm(self):
            return self.getTypedRuleContext(MiniGoParser.IfstmContext,0)


        def forstm(self):
            return self.getTypedRuleContext(MiniGoParser.ForstmContext,0)


        def breakstm(self):
            return self.getTypedRuleContext(MiniGoParser.BreakstmContext,0)


        def returnstm(self):
            return self.getTypedRuleContext(MiniGoParser.ReturnstmContext,0)


        def continuestm(self):
            return self.getTypedRuleContext(MiniGoParser.ContinuestmContext,0)


        def callstm(self):
            return self.getTypedRuleContext(MiniGoParser.CallstmContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MiniGoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_statement)
        try:
            self.state = 473
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 465
                self.decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 466
                self.assignstm()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 467
                self.ifstm()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 468
                self.forstm()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 469
                self.breakstm()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 470
                self.returnstm()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 471
                self.continuestm()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 472
                self.callstm()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignstmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(MiniGoParser.LhsContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def SEMICOL(self):
            return self.getToken(MiniGoParser.SEMICOL, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def ADDASGN(self):
            return self.getToken(MiniGoParser.ADDASGN, 0)

        def SUBASGN(self):
            return self.getToken(MiniGoParser.SUBASGN, 0)

        def MULASGN(self):
            return self.getToken(MiniGoParser.MULASGN, 0)

        def DIVASGN(self):
            return self.getToken(MiniGoParser.DIVASGN, 0)

        def MODASGN(self):
            return self.getToken(MiniGoParser.MODASGN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assignstm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignstm" ):
                return visitor.visitAssignstm(self)
            else:
                return visitor.visitChildren(self)




    def assignstm(self):

        localctx = MiniGoParser.AssignstmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_assignstm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 475
            self.lhs()
            self.state = 476
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.ASSIGN) | (1 << MiniGoParser.ADDASGN) | (1 << MiniGoParser.SUBASGN) | (1 << MiniGoParser.MULASGN) | (1 << MiniGoParser.DIVASGN) | (1 << MiniGoParser.MODASGN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 477
            self.expr(0)
            self.state = 478
            self.match(MiniGoParser.SEMICOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def dimension(self):
            return self.getTypedRuleContext(MiniGoParser.DimensionContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = MiniGoParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_lhs)
        try:
            self.state = 486
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 480
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 481
                self.match(MiniGoParser.ID)
                self.state = 482
                self.dimension()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 483
                self.match(MiniGoParser.ID)
                self.state = 484
                self.match(MiniGoParser.DOT)
                self.state = 485
                self.match(MiniGoParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def LPAR(self):
            return self.getToken(MiniGoParser.LPAR, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RPAR(self):
            return self.getToken(MiniGoParser.RPAR, 0)

        def LCUR(self):
            return self.getToken(MiniGoParser.LCUR, 0)

        def statementlist(self):
            return self.getTypedRuleContext(MiniGoParser.StatementlistContext,0)


        def RCUR(self):
            return self.getToken(MiniGoParser.RCUR, 0)

        def eliflist(self):
            return self.getTypedRuleContext(MiniGoParser.EliflistContext,0)


        def SEMICOL(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMICOL)
            else:
                return self.getToken(MiniGoParser.SEMICOL, i)

        def elstm(self):
            return self.getTypedRuleContext(MiniGoParser.ElstmContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_ifstm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfstm" ):
                return visitor.visitIfstm(self)
            else:
                return visitor.visitChildren(self)




    def ifstm(self):

        localctx = MiniGoParser.IfstmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_ifstm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 488
            self.match(MiniGoParser.IF)
            self.state = 489
            self.match(MiniGoParser.LPAR)
            self.state = 490
            self.expr(0)
            self.state = 491
            self.match(MiniGoParser.RPAR)
            self.state = 493
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.SEMICOL:
                self.state = 492
                self.match(MiniGoParser.SEMICOL)


            self.state = 495
            self.match(MiniGoParser.LCUR)
            self.state = 496
            self.statementlist()
            self.state = 497
            self.match(MiniGoParser.RCUR)
            self.state = 499
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.state = 498
                self.match(MiniGoParser.SEMICOL)


            self.state = 501
            self.eliflist()
            self.state = 503
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ELSE:
                self.state = 502
                self.elstm()


            self.state = 505
            self.match(MiniGoParser.SEMICOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EliflistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elifstmlist(self):
            return self.getTypedRuleContext(MiniGoParser.ElifstmlistContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_eliflist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEliflist" ):
                return visitor.visitEliflist(self)
            else:
                return visitor.visitChildren(self)




    def eliflist(self):

        localctx = MiniGoParser.EliflistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_eliflist)
        try:
            self.state = 509
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 507
                self.elifstmlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElifstmlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elifstm(self):
            return self.getTypedRuleContext(MiniGoParser.ElifstmContext,0)


        def elifstmlist(self):
            return self.getTypedRuleContext(MiniGoParser.ElifstmlistContext,0)


        def SEMICOL(self):
            return self.getToken(MiniGoParser.SEMICOL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_elifstmlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElifstmlist" ):
                return visitor.visitElifstmlist(self)
            else:
                return visitor.visitChildren(self)




    def elifstmlist(self):

        localctx = MiniGoParser.ElifstmlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_elifstmlist)
        self._la = 0 # Token type
        try:
            self.state = 518
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 511
                self.elifstm()
                self.state = 513
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.SEMICOL:
                    self.state = 512
                    self.match(MiniGoParser.SEMICOL)


                self.state = 515
                self.elifstmlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 517
                self.elifstm()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElstmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def LCUR(self):
            return self.getToken(MiniGoParser.LCUR, 0)

        def statementlist(self):
            return self.getTypedRuleContext(MiniGoParser.StatementlistContext,0)


        def RCUR(self):
            return self.getToken(MiniGoParser.RCUR, 0)

        def SEMICOL(self):
            return self.getToken(MiniGoParser.SEMICOL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_elstm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElstm" ):
                return visitor.visitElstm(self)
            else:
                return visitor.visitChildren(self)




    def elstm(self):

        localctx = MiniGoParser.ElstmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_elstm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 520
            self.match(MiniGoParser.ELSE)
            self.state = 521
            self.match(MiniGoParser.LCUR)
            self.state = 522
            self.statementlist()
            self.state = 523
            self.match(MiniGoParser.RCUR)
            self.state = 525
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.state = 524
                self.match(MiniGoParser.SEMICOL)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElifstmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def LPAR(self):
            return self.getToken(MiniGoParser.LPAR, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RPAR(self):
            return self.getToken(MiniGoParser.RPAR, 0)

        def LCUR(self):
            return self.getToken(MiniGoParser.LCUR, 0)

        def statementlist(self):
            return self.getTypedRuleContext(MiniGoParser.StatementlistContext,0)


        def RCUR(self):
            return self.getToken(MiniGoParser.RCUR, 0)

        def SEMICOL(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMICOL)
            else:
                return self.getToken(MiniGoParser.SEMICOL, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_elifstm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElifstm" ):
                return visitor.visitElifstm(self)
            else:
                return visitor.visitChildren(self)




    def elifstm(self):

        localctx = MiniGoParser.ElifstmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_elifstm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 527
            self.match(MiniGoParser.ELSE)
            self.state = 528
            self.match(MiniGoParser.IF)
            self.state = 529
            self.match(MiniGoParser.LPAR)
            self.state = 530
            self.expr(0)
            self.state = 531
            self.match(MiniGoParser.RPAR)
            self.state = 533
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.SEMICOL:
                self.state = 532
                self.match(MiniGoParser.SEMICOL)


            self.state = 535
            self.match(MiniGoParser.LCUR)
            self.state = 536
            self.statementlist()
            self.state = 537
            self.match(MiniGoParser.RCUR)
            self.state = 539
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.state = 538
                self.match(MiniGoParser.SEMICOL)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(MiniGoParser.StatementContext,0)


        def statementlist(self):
            return self.getTypedRuleContext(MiniGoParser.StatementlistContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_statementlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatementlist" ):
                return visitor.visitStatementlist(self)
            else:
                return visitor.visitChildren(self)




    def statementlist(self):

        localctx = MiniGoParser.StatementlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_statementlist)
        try:
            self.state = 545
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 541
                self.statement()
                self.state = 542
                self.statementlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 544
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForstmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def condi(self):
            return self.getTypedRuleContext(MiniGoParser.CondiContext,0)


        def LCUR(self):
            return self.getToken(MiniGoParser.LCUR, 0)

        def statementlist(self):
            return self.getTypedRuleContext(MiniGoParser.StatementlistContext,0)


        def RCUR(self):
            return self.getToken(MiniGoParser.RCUR, 0)

        def SEMICOL(self):
            return self.getToken(MiniGoParser.SEMICOL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_forstm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForstm" ):
                return visitor.visitForstm(self)
            else:
                return visitor.visitChildren(self)




    def forstm(self):

        localctx = MiniGoParser.ForstmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_forstm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 547
            self.match(MiniGoParser.FOR)
            self.state = 548
            self.condi()
            self.state = 549
            self.match(MiniGoParser.LCUR)
            self.state = 550
            self.statementlist()
            self.state = 551
            self.match(MiniGoParser.RCUR)
            self.state = 552
            self.match(MiniGoParser.SEMICOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondiContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def inifor(self):
            return self.getTypedRuleContext(MiniGoParser.IniforContext,0)


        def rangefor(self):
            return self.getTypedRuleContext(MiniGoParser.RangeforContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_condi

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondi" ):
                return visitor.visitCondi(self)
            else:
                return visitor.visitChildren(self)




    def condi(self):

        localctx = MiniGoParser.CondiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_condi)
        try:
            self.state = 557
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 554
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 555
                self.inifor()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 556
                self.rangefor()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IniforContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def forvarini(self):
            return self.getTypedRuleContext(MiniGoParser.ForvariniContext,0)


        def SEMICOL(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMICOL)
            else:
                return self.getToken(MiniGoParser.SEMICOL, i)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def assignfor(self):
            return self.getTypedRuleContext(MiniGoParser.AssignforContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_inifor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInifor" ):
                return visitor.visitInifor(self)
            else:
                return visitor.visitChildren(self)




    def inifor(self):

        localctx = MiniGoParser.IniforContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_inifor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 559
            self.forvarini()
            self.state = 560
            self.match(MiniGoParser.SEMICOL)
            self.state = 561
            self.expr(0)
            self.state = 562
            self.match(MiniGoParser.SEMICOL)
            self.state = 563
            self.assignfor()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForvariniContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def INIASSIGN(self):
            return self.getToken(MiniGoParser.INIASSIGN, 0)

        def typ(self):
            return self.getTypedRuleContext(MiniGoParser.TypContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forvarini

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForvarini" ):
                return visitor.visitForvarini(self)
            else:
                return visitor.visitChildren(self)




    def forvarini(self):

        localctx = MiniGoParser.ForvariniContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_forvarini)
        self._la = 0 # Token type
        try:
            self.state = 575
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 565
                self.match(MiniGoParser.ID)
                self.state = 566
                self.match(MiniGoParser.ASSIGN)
                self.state = 567
                self.expr(0)
                pass
            elif token in [MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 568
                self.match(MiniGoParser.VAR)
                self.state = 569
                self.match(MiniGoParser.ID)
                self.state = 571
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.ID))) != 0):
                    self.state = 570
                    self.typ()


                self.state = 573
                self.match(MiniGoParser.INIASSIGN)
                self.state = 574
                self.expr(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignforContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(MiniGoParser.LhsContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def ADDASGN(self):
            return self.getToken(MiniGoParser.ADDASGN, 0)

        def SUBASGN(self):
            return self.getToken(MiniGoParser.SUBASGN, 0)

        def MULASGN(self):
            return self.getToken(MiniGoParser.MULASGN, 0)

        def DIVASGN(self):
            return self.getToken(MiniGoParser.DIVASGN, 0)

        def MODASGN(self):
            return self.getToken(MiniGoParser.MODASGN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assignfor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignfor" ):
                return visitor.visitAssignfor(self)
            else:
                return visitor.visitChildren(self)




    def assignfor(self):

        localctx = MiniGoParser.AssignforContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_assignfor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 577
            self.lhs()
            self.state = 578
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.ASSIGN) | (1 << MiniGoParser.ADDASGN) | (1 << MiniGoParser.SUBASGN) | (1 << MiniGoParser.MULASGN) | (1 << MiniGoParser.DIVASGN) | (1 << MiniGoParser.MODASGN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 579
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RangeforContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def RANGE(self):
            return self.getToken(MiniGoParser.RANGE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_rangefor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRangefor" ):
                return visitor.visitRangefor(self)
            else:
                return visitor.visitChildren(self)




    def rangefor(self):

        localctx = MiniGoParser.RangeforContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_rangefor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 581
            self.match(MiniGoParser.ID)
            self.state = 582
            self.match(MiniGoParser.COMMA)
            self.state = 583
            self.match(MiniGoParser.ID)
            self.state = 584
            self.match(MiniGoParser.ASSIGN)
            self.state = 585
            self.match(MiniGoParser.RANGE)
            self.state = 586
            self.match(MiniGoParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakstmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MiniGoParser.BREAK, 0)

        def SEMICOL(self):
            return self.getToken(MiniGoParser.SEMICOL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_breakstm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakstm" ):
                return visitor.visitBreakstm(self)
            else:
                return visitor.visitChildren(self)




    def breakstm(self):

        localctx = MiniGoParser.BreakstmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_breakstm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 588
            self.match(MiniGoParser.BREAK)
            self.state = 589
            self.match(MiniGoParser.SEMICOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinuestmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MiniGoParser.CONTINUE, 0)

        def SEMICOL(self):
            return self.getToken(MiniGoParser.SEMICOL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_continuestm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinuestm" ):
                return visitor.visitContinuestm(self)
            else:
                return visitor.visitChildren(self)




    def continuestm(self):

        localctx = MiniGoParser.ContinuestmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_continuestm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 591
            self.match(MiniGoParser.CONTINUE)
            self.state = 592
            self.match(MiniGoParser.SEMICOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnstmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MiniGoParser.RETURN, 0)

        def SEMICOL(self):
            return self.getToken(MiniGoParser.SEMICOL, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_returnstm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnstm" ):
                return visitor.visitReturnstm(self)
            else:
                return visitor.visitChildren(self)




    def returnstm(self):

        localctx = MiniGoParser.ReturnstmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_returnstm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 594
            self.match(MiniGoParser.RETURN)
            self.state = 596
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.SUB) | (1 << MiniGoParser.NEG) | (1 << MiniGoParser.LPAR) | (1 << MiniGoParser.LSQU) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT) | (1 << MiniGoParser.BOOL_LIT) | (1 << MiniGoParser.ID))) != 0):
                self.state = 595
                self.expr(0)


            self.state = 598
            self.match(MiniGoParser.SEMICOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallstmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functioncall(self):
            return self.getTypedRuleContext(MiniGoParser.FunctioncallContext,0)


        def SEMICOL(self):
            return self.getToken(MiniGoParser.SEMICOL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_callstm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallstm" ):
                return visitor.visitCallstm(self)
            else:
                return visitor.visitChildren(self)




    def callstm(self):

        localctx = MiniGoParser.CallstmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_callstm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 600
            self.functioncall()
            self.state = 601
            self.match(MiniGoParser.SEMICOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[38] = self.expr_sempred
        self._predicates[39] = self.expr1_sempred
        self._predicates[40] = self.expr2_sempred
        self._predicates[41] = self.expr3_sempred
        self._predicates[42] = self.expr4_sempred
        self._predicates[44] = self.expr6_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr1_sempred(self, localctx:Expr1Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def expr6_sempred(self, localctx:Expr6Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         




