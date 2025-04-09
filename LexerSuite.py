import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))
    
    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme("ab?sVN","ab,ErrorToken ?",102))
    def test_keyword_var(self):
        """test keyword var"""
        self.assertTrue(TestLexer.checkLexeme("var abc int ;","var,abc,int,;,<EOF>",103))
    def test_keyword_func(self):
        """test keyword func"""
        self.assertTrue(TestLexer.checkLexeme("""func abc ( ) ""","""func,abc,(,),<EOF>""",104))
    def test_boolean(self):
        """test true and false"""
        self.assertTrue(TestLexer.checkLexeme("true","true,<EOF>",105))
    def test_comment(self):
        """test comment"""
        self.assertTrue(TestLexer.checkLexeme("/* This is a comment */ int x = 5; /* Another comment */","int,x,=,5,;,<EOF>",106))
    def test_comment2(self):
        """test comment"""
        self.assertTrue(TestLexer.checkLexeme("/* This is a /* Another comment*/ comment */","<EOF>",107))
    def test_unclosestring(self):
        """test unclosed string, it stops after this error"""
        self.assertTrue(TestLexer.checkLexeme("\"Hello bro","Unclosed string: Hello bro",108))
    def test_vardecl(self):
        """test comment"""
        self.assertTrue(TestLexer.checkLexeme("var x int = 10;","var,x,int,=,10,;,<EOF>",109))
    def test_unclosestring2(self):
        """test unclosed string, it stops after this error"""
        self.assertTrue(TestLexer.checkLexeme("\"Hello bro\n","Unclosed string: Hello bro\n\n",110))
    def test_illegal_escape(self):
        """test unclosed string, it stops after this error"""
        self.assertTrue(TestLexer.checkLexeme("\"Hello bro\w","Illegal escape in string: Hello bro\w",111))
    def test_expr(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("1 + 2","1,+,2,<EOF>",112))
    def test_semi(self):
        self.assertTrue(TestLexer.checkLexeme("if\n}\n)\n","if,},;,),;,<EOF>",113))
    def test_114(self):
        self.assertTrue(TestLexer.checkLexeme("//hllo bro\n","<EOF>",114))
    def test_115(self):
        """test basic arithmetic operators"""
        self.assertTrue(TestLexer.checkLexeme("10 + 20 - 30 * 40 / 50", "10,+,20,-,30,*,40,/,50,<EOF>", 115))

    def test_116(self):
        """test assignment operators"""
        self.assertTrue(TestLexer.checkLexeme("x := 100; y += 2;", "x,:=,100,;,y,+=,2,;,<EOF>", 116))

    def test_117(self):
        """test comparison operators"""
        self.assertTrue(TestLexer.checkLexeme("a == b && c != d || e > f", "a,==,b,&&,c,!=,d,||,e,>,f,<EOF>", 117))

    def test_118(self):
        """test boolean literals"""
        self.assertTrue(TestLexer.checkLexeme("true false", "true,false,<EOF>", 118))

    def test_119(self):
        """test integer literals"""
        self.assertTrue(TestLexer.checkLexeme("42 0b101 0xABC", "42,0b101,0xABC,<EOF>", 119))

    def test_120(self):
        """test float literals"""
        self.assertTrue(TestLexer.checkLexeme("3.14 2.71e-3", "3.14,2.71e-3,<EOF>", 120))

    def test_121(self):
        """test string literals"""
        self.assertTrue(TestLexer.checkLexeme('"hello world"', 'hello world,<EOF>', 121))

    def test_122(self):
        """test variable declaration"""
        self.assertTrue(TestLexer.checkLexeme("var x int = 10;", "var,x,int,=,10,;,<EOF>", 122))

    def test_123(self):
        """test function declaration"""
        self.assertTrue(TestLexer.checkLexeme("func add(a int, b int) int { return a + b; }", 
            "func,add,(,a,int,,,b,int,),int,{,return,a,+,b,;,},<EOF>", 123))

    def test_124(self):
        """test array declaration"""
        self.assertTrue(TestLexer.checkLexeme("arr := [3]int{1, 2, 3}", "arr,:=,[,3,],int,{,1,,,2,,,3,},<EOF>", 124))

    def test_125(self):
        """test struct declaration"""
        self.assertTrue(TestLexer.checkLexeme("type Person struct { name string; age int; }", 
            "type,Person,struct,{,name,string,;,age,int,;,},<EOF>", 125))

    def test_126(self):
        """test comments (should be ignored)"""
        self.assertTrue(TestLexer.checkLexeme("// this is a comment\nvar x = 10;", "var,x,=,10,;,<EOF>", 126))
    def test_127(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme("\"This is an unclosed string", "Unclosed string: This is an unclosed string", 127))

    def test_128(self):
        """test illegal escape in string"""
        self.assertTrue(TestLexer.checkLexeme('"Illegal \\x escape"', 'Illegal escape in string: Illegal \\x', 128))

    def test_129(self):
        """test unknown character"""
        self.assertTrue(TestLexer.checkLexeme("@#$%^&*", "ErrorToken @", 129))

    def test_130(self):
        """test incorrect integer format"""
        self.assertTrue(TestLexer.checkLexeme("0123", "0,123,<EOF>", 130))  # Might be incorrect if leading zeros are disallowed

    def test_131(self):
        """test missing semicolon"""
        self.assertTrue(TestLexer.checkLexeme("var x = 10 var y = 20", "var,x,=,10,var,y,=,20,<EOF>", 131))  # Should fail if semicolon is mandatory

    def test_132(self):
        """test invalid identifier"""
        self.assertTrue(TestLexer.checkLexeme("123abc", "123,abc,<EOF>", 132))  # Should fail if identifiers cannot start with numbers

    def test_133(self):
        """test invalid float format"""
        self.assertTrue(TestLexer.checkLexeme(".5", ".,5,<EOF>", 133))  # Should be "0.5" if leading zero is required

    def test_134(self):
        """test multi-line unclosed string"""
        self.assertTrue(TestLexer.checkLexeme("\"Hello\nhi", "Unclosed string: Hello\n\nhi", 134))  # Should fail due to newline in string
    def test_135(self):
        """test hexadecimal literals"""
        self.assertTrue(TestLexer.checkLexeme("0x1A3F 0XABC", "0x1A3F,0XABC,<EOF>", 135))

    def test_136(self):
        """test binary literals"""
        self.assertTrue(TestLexer.checkLexeme("0b1010 0B1101", "0b1010,0B1101,<EOF>", 136))

    def test_137(self):
        """test octal literals"""
        self.assertTrue(TestLexer.checkLexeme("0o123 0O77", "0o123,0O77,<EOF>", 137))

    def test_138(self):
        """test invalid binary literal"""
        self.assertTrue(TestLexer.checkLexeme("0b102", "0b10,2,<EOF>", 138))  # '2' is invalid in binary

    def test_139(self):
        """test invalid octal literal"""
        self.assertTrue(TestLexer.checkLexeme("0o89", "0,o89,<EOF>", 139))  # '8' and '9' are invalid in octal

    def test_140(self):
        """test float literals with exponents"""
        self.assertTrue(TestLexer.checkLexeme("1.23e10 4.56E-2", "1.23e10,4.56E-2,<EOF>", 140))

    def test_141(self):
        """test invalid float literals"""
        self.assertTrue(TestLexer.checkLexeme("1.", "1.,<EOF>", 141))  # Should fail if no decimal digits after '.'

    def test_142(self):
        """test unterminated block comment"""
        self.assertTrue(TestLexer.checkLexeme("/* This is an unterminated comment*/", "<EOF>", 142))

    def test_143(self):
        """test unterminated line comment"""
        self.assertTrue(TestLexer.checkLexeme("// No newline here", "<EOF>", 143))

    def test_144(self):
        """test multiple operators"""
        self.assertTrue(TestLexer.checkLexeme("+= -= *= /= %= && || !=", "+=,-=,*=,/=,%=,&&,||,!=,<EOF>", 144))

    def test_145(self):
        """test invalid identifiers"""
        self.assertTrue(TestLexer.checkLexeme("9abc", "9,abc,<EOF>", 145))  # Identifier cannot start with a number

    def test_146(self):
        """test identifiers with underscores"""
        self.assertTrue(TestLexer.checkLexeme("_abc _123", "_abc,_123,<EOF>", 146))

    def test_147(self):
        """test reserved keywords"""
        self.assertTrue(TestLexer.checkLexeme("if else return break continue", "if,else,return,break,continue,<EOF>", 147))

    def test_148(self):
        """test single character tokens"""
        self.assertTrue(TestLexer.checkLexeme("{ } ( ) [ ] , ;", "{,},(,),[,],,,;,<EOF>", 148))

    def test_149(self):
        """test function call"""
        self.assertTrue(TestLexer.checkLexeme("func(123, a, b+c)", "func,(,123,,,a,,,b,+,c,),<EOF>", 149))

    def test_150(self):
        """test logical operators"""
        self.assertTrue(TestLexer.checkLexeme("x && y || !z", "x,&&,y,||,!,z,<EOF>", 150))

    def test_151(self):
        """test bitwise operators"""
        self.assertTrue(TestLexer.checkLexeme("x & y | z ^ w", "x,ErrorToken &", 151))

    def test_152(self):
        """test increment and decrement operators"""
        self.assertTrue(TestLexer.checkLexeme("i++ j--", "i,+,+,j,-,-,<EOF>", 152))

    def test_153(self):
        """test invalid escape sequence"""
        self.assertTrue(TestLexer.checkLexeme('"hello\\q"', 'Illegal escape in string: hello\\q', 153))

    def test_154(self):
        """test nested comments"""
        self.assertTrue(TestLexer.checkLexeme("/* outer /* inner */ comment */", "<EOF>", 154))

    def test_155(self):
        """test empty string"""
        self.assertTrue(TestLexer.checkLexeme("\"\"", ",<EOF>", 155))

    def test_156(self):
        """test string with special characters"""
        self.assertTrue(TestLexer.checkLexeme('"hello\\nworld"', 'hello\\nworld,<EOF>', 156))

    def test_157(self):
        """test boolean expressions"""
        self.assertTrue(TestLexer.checkLexeme("true && false || !true", "true,&&,false,||,!,true,<EOF>", 157))

    def test_158(self):
        """test string concatenation"""
        self.assertTrue(TestLexer.checkLexeme('"hello" + "world"', 'hello,+,world,<EOF>', 158))

    def test_159(self):
        """test invalid character"""
        self.assertTrue(TestLexer.checkLexeme("#", "ErrorToken #", 159))

    def test_160(self):
        """test newline handling"""
        self.assertTrue(TestLexer.checkLexeme("x = 10\ny = 20", "x,=,10,;,y,=,20,<EOF>", 160))

    def test_161(self):
        """test tab handling"""
        self.assertTrue(TestLexer.checkLexeme("x\t=\t10", "x,=,10,<EOF>", 161))

    def test_162(self):
        """test carriage return handling"""
        self.assertTrue(TestLexer.checkLexeme("x = 10\r y = 20", "x,=,10,y,=,20,<EOF>", 162))

    def test_163(self):
        """test function definition"""
        self.assertTrue(TestLexer.checkLexeme("func foo() { return; }", "func,foo,(,),{,return,;,},<EOF>", 163))

    def test_164(self):
        """test missing closing parenthesis"""
        self.assertTrue(TestLexer.checkLexeme("func foo( { return; }", "func,foo,(,{,return,;,},<EOF>", 164))

    def test_165(self):
        """test missing closing brace"""
        self.assertTrue(TestLexer.checkLexeme("func foo() { return;", "func,foo,(,),{,return,;,<EOF>", 165))

    def test_166(self):
        """test class definition"""
        self.assertTrue(TestLexer.checkLexeme("class A { var x int; }", "class,A,{,var,x,int,;,},<EOF>", 166))

    def test_167(self):
        """test unexpected end of input"""
        self.assertTrue(TestLexer.checkLexeme("func foo(", "func,foo,(,<EOF>", 167))

    def test_168(self):
        """test unterminated string with escape sequence"""
        self.assertTrue(TestLexer.checkLexeme("\"hello\\n", "Unclosed string: hello\\n", 168))

    def test_169(self):
        """test valid identifier starting with underscore"""
        self.assertTrue(TestLexer.checkLexeme("_validIdentifier123", "_validIdentifier123,<EOF>", 169))

    def test_170(self):
        """test invalid identifier with special characters"""
        self.assertTrue(TestLexer.checkLexeme("abc$xyz", "abc,ErrorToken $", 170))

    def test_171(self):
        """test single-line block comment"""
        self.assertTrue(TestLexer.checkLexeme("/* single line comment */", "<EOF>", 171))

    def test_172(self):
        """test invalid identifier with hyphen"""
        self.assertTrue(TestLexer.checkLexeme("abc-xyz", "abc,-,xyz,<EOF>", 172))
    def test_173(self):
        """test function declaration with parameters"""
        self.assertTrue(TestLexer.checkLexeme("func sum(a int, b int) int { return a + b; }",
            "func,sum,(,a,int,,,b,int,),int,{,return,a,+,b,;,},<EOF>", 173))

    def test_174(self):
        """test function without return type"""
        self.assertTrue(TestLexer.checkLexeme("func printMessage() { print(\"Hello\"); }",
            "func,printMessage,(,),{,print,(,Hello,),;,},<EOF>", 174))

    def test_175(self):
        """test function with multiple return statements"""
        self.assertTrue(TestLexer.checkLexeme("func max(a int, b int) int { if (a > b) return a; return b; }",
            "func,max,(,a,int,,,b,int,),int,{,if,(,a,>,b,),return,a,;,return,b,;,},<EOF>", 175))

    def test_176(self):
        """test function call with arguments"""
        self.assertTrue(TestLexer.checkLexeme("result := sum(10, 20);", "result,:=,sum,(,10,,,20,),;,<EOF>", 176))

    def test_177(self):
        """test function returning void"""
        self.assertTrue(TestLexer.checkLexeme("func doNothing() { return; }", "func,doNothing,(,),{,return,;,},<EOF>", 177))

    def test_178(self):
        """test function with local variable"""
        self.assertTrue(TestLexer.checkLexeme("func compute() int { var x int = 5; return x * x; }",
            "func,compute,(,),int,{,var,x,int,=,5,;,return,x,*,x,;,},<EOF>", 178))

    def test_179(self):
        """test nested function calls"""
        self.assertTrue(TestLexer.checkLexeme("print(sum(5, multiply(2, 3)));",
            "print,(,sum,(,5,,,multiply,(,2,,,3,),),),;,<EOF>", 179))

    def test_180(self):
        """test if statement"""
        self.assertTrue(TestLexer.checkLexeme("if (x > 0) { print(\"Positive\"); }",
            "if,(,x,>,0,),{,print,(,Positive,),;,},<EOF>", 180))

    def test_181(self):
        """test if-else statement"""
        self.assertTrue(TestLexer.checkLexeme("if (x > 0) { print(\"Positive\"); } else { print(\"Negative\"); }",
            "if,(,x,>,0,),{,print,(,Positive,),;,},else,{,print,(,Negative,),;,},<EOF>", 181))

    def test_182(self):
        """test if-else if ladder"""
        self.assertTrue(TestLexer.checkLexeme("if (x > 0) print(\"Positive\"); else if (x == 0) print(\"Zero\"); else print(\"Negative\");",
            "if,(,x,>,0,),print,(,Positive,),;,else,if,(,x,==,0,),print,(,Zero,),;,else,print,(,Negative,),;,<EOF>", 182))

    def test_183(self):
        """test while loop"""
        self.assertTrue(TestLexer.checkLexeme("while (i < 10) { i = i + 1; }",
            "while,(,i,<,10,),{,i,=,i,+,1,;,},<EOF>", 183))

    def test_184(self):
        """test for loop"""
        self.assertTrue(TestLexer.checkLexeme("for (i := 0; i < 10; i+=1) { print(i); }",
            "for,(,i,:=,0,;,i,<,10,;,i,+=,1,),{,print,(,i,),;,},<EOF>", 184))

    def test_185(self):
        """test break statement"""
        self.assertTrue(TestLexer.checkLexeme("while (true) { if (x == 5) break; x = x + 1; }",
            "while,(,true,),{,if,(,x,==,5,),break,;,x,=,x,+,1,;,},<EOF>", 185))

    def test_186(self):
        """test continue statement"""
        self.assertTrue(TestLexer.checkLexeme("for (i := 0; i < 10; i/=5) { if (i % 2 == 0) continue; print(i); }",
            "for,(,i,:=,0,;,i,<,10,;,i,/=,5,),{,if,(,i,%,2,==,0,),continue,;,print,(,i,),;,},<EOF>", 186))

    def test_187(self):
        """test return statement inside loop"""
        self.assertTrue(TestLexer.checkLexeme("func findEven(arr []int) int { for (x in arr) { if (x % 2 == 0) return x; } return -1; }",
            "func,findEven,(,arr,[,],int,),int,{,for,(,x,in,arr,),{,if,(,x,%,2,==,0,),return,x,;,},return,-,1,;,},<EOF>", 187))

    def test_188(self):
        """test switch statement"""
        self.assertTrue(TestLexer.checkLexeme("switch (x) { case 1: print(\"One\"); break; case 2: print(\"Two\"); break; default: print(\"Other\"); }",
            "switch,(,x,),{,case,1,:,print,(,One,),;,break,;,case,2,:,print,(,Two,),;,break,;,default,:,print,(,Other,),;,},<EOF>", 188))

    def test_189(self):
        """test array indexing"""
        self.assertTrue(TestLexer.checkLexeme("arr[2] = 10;", "arr,[,2,],=,10,;,<EOF>", 189))

    def test_190(self):
        """test array iteration"""
        self.assertTrue(TestLexer.checkLexeme("for (i in arr) { print(i); }",
            "for,(,i,in,arr,),{,print,(,i,),;,},<EOF>", 190))

    def test_191(self):
        """test struct declaration"""
        self.assertTrue(TestLexer.checkLexeme("type Person struct { name string; age int; }",
            "type,Person,struct,{,name,string,;,age,int,;,},<EOF>", 191))

    def test_192(self):
        """test struct instantiation"""
        self.assertTrue(TestLexer.checkLexeme("p := Person{name: \"John\", age: 30};",
            "p,:=,Person,{,name,:,John,,,age,:,30,},;,<EOF>", 192))

    def test_193(self):
        """test struct field access"""
        self.assertTrue(TestLexer.checkLexeme("x = p.name;", "x,=,p,.,name,;,<EOF>", 193))

    def test_194(self):
        """test nested struct"""
        self.assertTrue(TestLexer.checkLexeme("type Address struct { city string; } type Person struct { name string; address Address; }",
            "type,Address,struct,{,city,string,;,},type,Person,struct,{,name,string,;,address,Address,;,},<EOF>", 194))

    def test_195(self):
        """test method inside struct"""
        self.assertTrue(TestLexer.checkLexeme("func (p Person) greet() { print(\"Hello\" + p.name); }",
            "func,(,p,Person,),greet,(,),{,print,(,Hello,+,p,.,name,),;,},<EOF>", 195))

    def test_196(self):
        """test method call"""
        self.assertTrue(TestLexer.checkLexeme("p.greet();", "p,.,greet,(,),;,<EOF>", 196))

    def test_197(self):
        """test return struct"""
        self.assertTrue(TestLexer.checkLexeme("func getPerson() Person { return Person{name: \"John\", age: 25}; }",
            "func,getPerson,(,),Person,{,return,Person,{,name,:,John,,,age,:,25,},;,},<EOF>", 197))
    def test_198(self):
        """test nested loops"""
        self.assertTrue(TestLexer.checkLexeme("for (i := 0; i < 5; i++) { for (j := 0; j < 5; j++) { print(i * j); } }",
            "for,(,i,:=,0,;,i,<,5,;,i,+,+,),{,for,(,j,:=,0,;,j,<,5,;,j,+,+,),{,print,(,i,*,j,),;,},},<EOF>", 198))

    def test_199(self):
        """test function returning a struct"""
        self.assertTrue(TestLexer.checkLexeme("func createPerson(name string, age int) Person { return Person{name: name, age: age}; }",
            "func,createPerson,(,name,string,,,age,int,),Person,{,return,Person,{,name,:,name,,,age,:,age,},;,},<EOF>", 199))

    def test_200(self):
        """test complex expression"""
        self.assertTrue(TestLexer.checkLexeme("result = (a + b) * (c - d) / (e % f);",
            "result,=,(,a,+,b,),*,(,c,-,d,),/,(,e,%,f,),;,<EOF>", 200))