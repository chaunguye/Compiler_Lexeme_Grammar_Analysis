import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: void main() {} """
        input = """func main() {return;}\n"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))
    def test_more_complex_program(self):
        """More complex program"""
        input = """func foo () {return;};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))
    def test_wrong_miss_close(self):
        """Miss ) void main( {}"""
        input = """func main({};"""
        expect = "Error on line 1 col 11: {"
        self.assertTrue(TestParser.checkParser(input,expect,203))
    def test_wrong_variable(self):
        input = """var int;"""
        expect = "Error on line 1 col 5: int"
        self.assertTrue(TestParser.checkParser(input,expect,204))
    def test_wrong_index(self):
        input = """var i ;"""
        expect = "Error on line 1 col 7: ;"
        self.assertTrue(TestParser.checkParser(input,expect,205))
    def test_normal_var_decl(self):
        input = """var i int = 10\n"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,206))
    def test_arr_decl(self):
        input = """var arr [5][6][con]int;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,207))
    def test_struct_decl(self):
        input = """type triBao struct {
        name int;
        age int;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,208))
    def test_struc_decl2(self):
        input = """type triBao Struct {
        name int
        age int
        };"""
        expect = "Error on line 1 col 13: Struct"
        self.assertTrue(TestParser.checkParser(input,expect,209))
    def test_interface_decl(self):
        input = """type triBao interface {
        Greet(a, b string, c float)\n};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,210))
    def test_interface_decl2(self):
        input = """type triBao interface {
        Add(a int, b int) int
        Sub(a float, b float)
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,211))
    # def test_expr(self):
    #     input = """1 + 2"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input,expect,212))
    def test_strucfunc(self):
        input = """func (p Person) Greet() string {
        x := peple.name + 3;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,213))
    def test_214(self):
        input = """var a int = 5 + 8 - 3\n"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,214))
    def test_215(self):
        input = """var a int = 5 + 8 - Cal(4,3)\n"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,215))
    def test_216(self):
        input = """var a int = 5 + People.age(\"chau\", 2252091);"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,216))
    def test_217(self):
        input = """func main() {
        if(a == true) {
        b := 5
        }
        else{
        b := 6
        }\n};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,217))
    def test_218(self):
        input = """var a int = 5 + People.age(\"chau\", 2252091)\n\n\n var b int\n"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,218))
    def test_219(self):
        input = """func main() {
        for a<11 {a+=1;};
        }\n"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,219))
    def test_220(self):
        input = """func main() {
        for i:=0;i<11;i+=1 {a+=1;}
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,220))
    def test_221(self):
        input = """func main() {
        for a,b := range arr{a+=1;}
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,221))
    def test_222(self):
        input = """func main(){for a,b := range arr{
        a+=1;
        if (a==1) {break;}
        add(a,b);
        }\n};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,222))
    def test_001(self):
        """Simple variable declaration"""
        input = "var x int;\n"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 223))
    def test_002(self):
        """Variable declaration with initialization"""
        input = "var x int = 5;\n"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 224))
    def test_003(self):
        """Constant declaration"""
        input = "const PI = 3.14;\n"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 225))
    def test_004(self):
        """Function declaration without parameters"""
        input = "func main() { return; }\n"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 226))
    def test_005(self):
        """Function declaration with parameters"""
        input = "func add(a int, b int) int { return a + b; }\n"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 227))
    def test_006(self):
        """Function returning a boolean"""
        input = "func isEven(n int) boolean { return n % 2 == 0; }\n"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 228))
    def test_007(self):
        """Function call"""
        input = "func main() { x := add(3, 4); }\n"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 212))
    def test_008(self):
        """If statement"""
        input = "func main() { if (x > 0) { return; }; }\n"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 229))
    def test_009(self):
        """If-else statement"""
        input = "func main() { if (x > 0) { return; } else { x := 0; }; }\n"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 230))
    def test_010(self):
        """For loop"""
        input = "func main() { for i := 0; i < 10; i += 1 { print(i); }\n }\n"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 231))
    def test_232(self):
        """Simple array declaration"""
        input = "var arr [5] int;\n"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 232))
    def test_233(self):
        """Array declaration with float type"""
        input = "var arr [10] float;\n"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 233))
    def test_234(self):
        """Boolean array declaration"""
        input = "var flags [3] boolean;\n"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 234))
    def test_235(self):
        """String array declaration"""
        input = "var names [7] string;\n"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 235))
    def test_236(self):
        """Multi-dimensional integer array"""
        input = "var matrix [3][3] int;\n"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 236))
    def test_237(self):
        """Three-dimensional float array"""
        input = "var tensor [2][2][2] float;\n"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 237))
    def test_238(self):
        """Array with size initialized by a variable"""
        input = "var n int;\nvar arr [n] int;\n"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 238))
    def test_239(self):
        """Array declaration inside a function"""
        input = "func main() { var arr [4] boolean; }\n"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 239))
    def test_240(self):
        """Array with struct type"""
        input = "type Person struct { name string; age int; }\nvar people [10] Person;\n"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 240))
    def test_241(self):
        """Array with interface type"""
        input = "type Shape interface { area() float; }\nvar shapes [5] Shape;\n"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 241))
    def test_242(self):
        """Array with interface type"""
        input = """func Add() {
        for var i = 0; i < 10; i += 1 {
                return; 
                }
            };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 242))
    def test_243(self):
        """Simple struct declaration"""
        input = "type Person struct { name string; age int; }\n"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 243))


    def test_244(self):
        """Struct with multiple fields"""
        input = "type Car struct { brand string; model string; year int; }\n"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 244))


    def test_245(self):
        """Struct declaration missing closing brace"""
        input = "type Book struct { title string; author string; pages int; \n"
        expect = "Error on line 2 col 1: <EOF>"
        self.assertTrue(TestParser.checkParser(input, expect, 245))


    def test_246(self):
        """Nested struct declaration"""
        input = "type Address struct { city string; zip int; }\ntype User struct { name string; addr Address; }\n"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 246))


    def test_247(self):
        """Struct with no fields"""
        input = "type Empty struct { }\n"
        expect = "Error on line 1 col 21: }"
        self.assertTrue(TestParser.checkParser(input, expect, 247))


    def test_248(self):
        """Struct missing struct keyword"""
        input = "type Car { brand string; model string; }\n"
        expect = "Error on line 1 col 10: {"
        self.assertTrue(TestParser.checkParser(input, expect, 248))


    def test_249(self):
        """Struct with invalid field type"""
        input = "type Point struct { x coordinate; y coordinate; }\n"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 249))


    def test_250(self):
        """Struct with function inside (invalid)"""
        input = "type Circle struct { radius float; func area() float { return 3.14 * radius * radius; } }\n"
        expect = "Error on line 1 col 36: func"
        self.assertTrue(TestParser.checkParser(input, expect, 250))
    
    def test_251(self):
        """Simple interface declaration"""
        input = "type Drawable interface { draw(); }\n"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 251))


    def test_252(self):
        """Interface with multiple methods"""
        input = "type Shape interface { area() float; perimeter() float; }\n"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 252))


    def test_253(self):
        """Interface missing closing brace"""
        input = "type Logger interface { log(msg string);\n"
        expect = "Error on line 2 col 1: <EOF>"
        self.assertTrue(TestParser.checkParser(input, expect, 253))


    def test_254(self):
        """Empty interface declaration"""
        input = "type Empty interface { }\n"
        expect = "Error on line 1 col 24: }"
        self.assertTrue(TestParser.checkParser(input, expect, 254))


    def test_255(self):
        """Interface with invalid method"""
        input = "type Test interface { invalid_method int; }\n"
        expect = "Error on line 1 col 38: int"
        self.assertTrue(TestParser.checkParser(input, expect, 255))


    def test_256(self):
        """Interface extending another interface"""
        input = "type AdvancedShape interface : Shape { volume() float; }\n"
        expect = "Error on line 1 col 30: :"
        self.assertTrue(TestParser.checkParser(input, expect, 256))

    def test_257(self):
        """Interface with inheritance"""
        input = "type A interface { foo(); }\ntype B interface { bar(); }\n"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 257))


    def test_258(self):
        """Interface with method returning an array"""
        input = "type Collection interface { getItems() [10] int; }\n"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 258))


    def test_259(self):
        """Interface with method using an interface as a parameter"""
        input = "type Processor interface { process(data Reader); }\n"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 259))


    def test_260(self):
        """Interface with incorrect syntax"""
        input = "type Broken interface { void brokenMethod(); }\n"
        expect = "Error on line 1 col 30: brokenMethod"
        self.assertTrue(TestParser.checkParser(input, expect, 260))
    def test_261(self):
        """If statement with multiple declarations and statements"""
        input = "func main() { var x int; if (x > 10)\n{ var y float; y := 3.14; print(y); }\n }\n"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 261))


    def test_262(self):
        """Nested if statements"""
        input = "func main() { if (a > 0) { if (b < 5) { print(a + b); }; }\n }\n"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 262))


    def test_263(self):
        """If-else with function call and variable assignment"""
        input = "func main() { if (flag) { doSomething(array[7]); } else { x := 42; }; }\n"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 263))


    def test_264(self):
        """If statement with loop inside"""
        input = "func main() { if (count > 0) { for i := 0; i < count; i += 1 { print(i); }; }\n }\n"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 264))
    def test_265(self):
        """For loop with break statement"""
        input = "func main() { for i := 0; i < 10; i += 1 { if (i == 5) { break; }; print(i); }; }\n"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 265))


    def test_266(self):
        """For loop with continue statement"""
        input = "func main() { for i := 0; i < 10; i += 1 { if (i % 2 == 0) { continue; }\n print(i); }\n }\n"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 266))


    def test_267(self):
        """For loop with return statement"""
        input = "func main() { for i := 0; i < 10; i > 1 { if (i == 7) { return; }; print(i); }; }\n"
        expect = "Error on line 1 col 37: >"
        self.assertTrue(TestParser.checkParser(input, expect, 267))


    def test_268(self):
        """Nested for loops with break and continue"""
        input = "func main() { for i := 0; i < 5; i += 1 { for j := 0; j < 5; j += 1 { if (j == 2) { continue; }\n if (i == 3) { break; }; print(i, j); }\n }; }\n"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 268))


    def test_269(self):
        """For loop with missing increment"""
        input = "func main() { for i := 0; i < 10; { print(i); } }\n"
        expect = "Error on line 1 col 35: {"
        self.assertTrue(TestParser.checkParser(input, expect, 269))
    def test_270(self):
        """Function call inside another function"""
        input = "func foo() int { return 42; }\nfunc main() { x := foo(); }\n"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 270))


    def test_271(self):
        """Method call on a struct"""
        input = "type Person struct { name string; }\nfunc (p Person) getName() string { return p.name; }\nfunc main() { p := Person{name: \"Alice\"}; x := p.getName(); }\n"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 271))


    def test_272(self):
        """Method call with parameters"""
        input = "type Calculator struct {a int\n}\nfunc (c Calculator) add(a int, b int) int { return a + b; }\nfunc main() { calc := Calculator{}; x := calc.add(3, 4); }\n"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 272))


    def test_273(self):
        """Function call within a loop"""
        input = "func square(n int) int { return n * n; }\nfunc main() { for i := 1; i <= 5; i += 1 { print(square(i)); }\n }\n"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 273))


    def test_274(self):
        """Recursive function call"""
        input = "func factorial(n int) int { if (n == 0) { return 1; }; return n * factorial(n - 1); }\nfunc main() { x := factorial(5); }\n"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 274))


    def test_275(self):
        """Function call returning multiple values"""
        input = "func divide(a int, b int) int { return a / b; }\nfunc main() {remainder := divide(10, 3); }\n"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 275))


    def test_276(self):
        """Function call with default parameters"""
        input = "func greet(name string) string { return \"Hello, \" + name; }\nfunc main() { print(greet()); print(greet(\"Alice\")); }\n"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 276))


    def test_277(self):
        """Method chaining"""
        input = "type StringBuilder struct { s string; }\nfunc (sb StringBuilder) append(str string) StringBuilder { sb.s += str; return sb; }\nfunc (sb StringBuilder) build() string { return sb.s; }\nfunc main() { sb := StringBuilder{}; x := sb.append(\"Hello\").append(\" World\").build(); }\n"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 277))


    def test_278(self):
        """Function passed as argument"""
        input = "func f(a int) int { return f(x); }\nfunc double(n int) int { return n * 2; }\nfunc main() { y := f(double, 5); return double(); }\n"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 278))


    def test_279(self):
        """Anonymous function call"""
        input = "func main() { x := hello(a,b); }\n"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 279))

    def test_280(self):
        """Complex variable and constant declarations"""
        input = """
            var x int = 10;
            var y float = 3.14;
            const pi = 3.1415;
            var message string = "Hello, MiniGo!";
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 280))

    def test_281(self):
        """Function with multiple return types"""
        input = """
            func compute(a int, b float) float {
                return a * 2;
            };
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 281))

    def test_282(self):
        """Struct with function inside"""
        input = """
            type Person struct {
                name string;
                age int;
                func getAge() int {
                    return age;
                };
            };
        """
        expect = "Error on line 5 col 17: func"
        self.assertTrue(TestParser.checkParser(input, expect, 282))

    def test_283(self):
        """Nested if-else statement with function calls"""
        input = """
            func checkValue(x int) string {
                if (x > 10) {
                    if (x % 2 == 0) {
                        return "Even and greater than 10";
                    } else {
                        return "Odd and greater than 10";
                    };
                } else {
                    return "Less than or equal to 10";
                };
            };
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 283))

    def test_284(self):
        """For loop with nested if-else"""
        input = """
            func main() {
                for i := 1; i <= 10; i += 1 {
                    if (i % 2 == 0) {
                        print("Even:", i);
                    } else {
                        print("Odd:", i);
                    };
                };
            };
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 284))

    def test_285(self):
        """Function with an array parameter"""
        input = """
            func sumArray(arr [5]) int {
                var sum int = 0;
                for i := 0; i < 5; i += 1 {
                    sum += arr[i];
                };
                return sum;
            };
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 285))

    def test_286(self):
        """Array initialization with struct literals"""
        input = """
            type Point struct {
                x int;
                y int;
            };

            var points [3]Point = [3]Point {
                {1, 2},
                {3, 4},
                {5, 6}};
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 286))

    def test_287(self):
        """Interface with method"""
        input = """
            type Reader interface {
                read() string;
            };

            type File struct {
                name string;
            };

            func (f File) read() string {
                return "Reading from " + f.name;
            };
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 287))

    def test_288(self):
        """Multiple nested loops"""
        input = """
            func printTable(n int) {
                for i := 1; i <= n; i += 1 {
                    for j := 1; j <= n; j += 1 {
                        print(i * j);
                    };
                };
            };
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 288))

    def test_289(self):
        """Invalid function call (missing semicolon)"""
        input = """
            func main() {
                print("Hello, MiniGo")
            };
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 289))

    def test_290(self):
        """Illegal escape sequence in string"""
        input = """
            func main() {
                var text string = "This is an invalid escape: \\q";
            };
        """
        expect = "This is an invalid escape: \q"
        self.assertTrue(TestParser.checkParser(input, expect, 290))

    def test_291(self):
        """Unclosed string literal"""
        input = """ var message string = "hello;
        """
        expect = """hello;

        """
        self.assertTrue(TestParser.checkParser(input, expect, 291))

    def test_292(self):
        """Array access with invalid index"""
        input = """
            func main() {
                var arr [5]int;
                var x int = arr[5];  
                // Out of bounds
            };
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 292))

    def test_293(self):
        """Struct initialization with missing fields"""
        input = """
            type Person struct {
                name string;
                age int;
            };
            func main() {
            peson:= Person{ name: "Alice" };
            };
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 293))

    def test_294(self):
        """Nested function calls with expressions"""
        input = """
            func complexCalculation(a int, b int) int {
                return add(multiply(a, b), subtract(a, b));
            };
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 294))

    def test_295(self):
        """Switch case equivalent with if-elif-else"""
        input = """
            func checkGrade(score int) string {
                if (score >= 90) {
                    return "A";
                } else if (score >= 80) {
                    return "B";
                } else if (score >= 70) {
                    return "C";
                } else {
                    return "F";
                };
            };
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 295))

    def test_296(self):
        """Recursive function"""
        input = """
            func factorial(n int) int {
                if (n <= 1) {
                    return 1;
                };
                return n * factorial(n - 1);
            };
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 296))

    def test_297(self):
        """Function with void return"""
        input = """
            func sayHello() {
                print("Hello, MiniGo!");
            };
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 297))

    def test_298(self):
        """Using boolean literals in expressions"""
        input = """
            func main() {
                var isDone boolean = false;
                if (!isDone) {
                    print("Still working...");
                };
            };
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 298))

    def test_299(self):
        """Invalid identifier name (starts with a digit)"""
        input = """
            func main() {
                var 1invalidName int = 10;
            };
        """
        expect = "Error on line 3 col 21: 1"
        self.assertTrue(TestParser.checkParser(input, expect, 299))

    def test_300(self):
        """Missing closing bracket in struct"""
        input = """
                                    func Add() {
                                        for i  := 0; foo().a.b(); i[3] := 1 {
                                            return; 
                                        }
                                    };"""
        expect = "Error on line 3 col 77: ["
        self.assertTrue(TestParser.checkParser(input, expect, 300))
    def test_301(self):
        """Missing closing bracket in struct"""
        input = """func main() { if (x > 0) { Person.call(1800)\n } else { Person.call(1801); } }\n"""
        expect = "Error on line 3 col 77: ["
        self.assertTrue(TestParser.checkParser(input, expect, 301))


        
