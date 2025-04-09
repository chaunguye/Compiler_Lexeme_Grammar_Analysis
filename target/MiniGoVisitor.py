# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniGoParser import MiniGoParser
else:
    from MiniGoParser import MiniGoParser

# This class defines a complete generic visitor for a parse tree produced by MiniGoParser.

class MiniGoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniGoParser#program.
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#decllist.
    def visitDecllist(self, ctx:MiniGoParser.DecllistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#decl.
    def visitDecl(self, ctx:MiniGoParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#typdecl.
    def visitTypdecl(self, ctx:MiniGoParser.TypdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#vardecl.
    def visitVardecl(self, ctx:MiniGoParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#typ.
    def visitTyp(self, ctx:MiniGoParser.TypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#condecl.
    def visitCondecl(self, ctx:MiniGoParser.CondeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#funcdecl.
    def visitFuncdecl(self, ctx:MiniGoParser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#functyp.
    def visitFunctyp(self, ctx:MiniGoParser.FunctypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arraytyp.
    def visitArraytyp(self, ctx:MiniGoParser.ArraytypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#para.
    def visitPara(self, ctx:MiniGoParser.ParaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#paralist.
    def visitParalist(self, ctx:MiniGoParser.ParalistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#paralistprime.
    def visitParalistprime(self, ctx:MiniGoParser.ParalistprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#paraelement.
    def visitParaelement(self, ctx:MiniGoParser.ParaelementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arraypara.
    def visitArraypara(self, ctx:MiniGoParser.ArrayparaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#nullabledimension.
    def visitNullabledimension(self, ctx:MiniGoParser.NullabledimensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#nulldimen.
    def visitNulldimen(self, ctx:MiniGoParser.NulldimenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#idlist.
    def visitIdlist(self, ctx:MiniGoParser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#stm.
    def visitStm(self, ctx:MiniGoParser.StmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#strucinst.
    def visitStrucinst(self, ctx:MiniGoParser.StrucinstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arraydecl.
    def visitArraydecl(self, ctx:MiniGoParser.ArraydeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#dimension.
    def visitDimension(self, ctx:MiniGoParser.DimensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#dimen.
    def visitDimen(self, ctx:MiniGoParser.DimenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structdecl.
    def visitStructdecl(self, ctx:MiniGoParser.StructdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#field.
    def visitField(self, ctx:MiniGoParser.FieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#fieldlistprime.
    def visitFieldlistprime(self, ctx:MiniGoParser.FieldlistprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#fieldele.
    def visitFieldele(self, ctx:MiniGoParser.FieldeleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interfacedecl.
    def visitInterfacedecl(self, ctx:MiniGoParser.InterfacedeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#methodprime.
    def visitMethodprime(self, ctx:MiniGoParser.MethodprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method.
    def visitMethod(self, ctx:MiniGoParser.MethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_lit.
    def visitArray_lit(self, ctx:MiniGoParser.Array_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrayini.
    def visitArrayini(self, ctx:MiniGoParser.ArrayiniContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrayinilist.
    def visitArrayinilist(self, ctx:MiniGoParser.ArrayinilistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrayiniele.
    def visitArrayiniele(self, ctx:MiniGoParser.ArrayinieleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_lit.
    def visitStruct_lit(self, ctx:MiniGoParser.Struct_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#fieldinilist.
    def visitFieldinilist(self, ctx:MiniGoParser.FieldinilistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#fieldiniprime.
    def visitFieldiniprime(self, ctx:MiniGoParser.FieldiniprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#fieldini.
    def visitFieldini(self, ctx:MiniGoParser.FieldiniContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr.
    def visitExpr(self, ctx:MiniGoParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr1.
    def visitExpr1(self, ctx:MiniGoParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr2.
    def visitExpr2(self, ctx:MiniGoParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr3.
    def visitExpr3(self, ctx:MiniGoParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr4.
    def visitExpr4(self, ctx:MiniGoParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr5.
    def visitExpr5(self, ctx:MiniGoParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr6.
    def visitExpr6(self, ctx:MiniGoParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr7.
    def visitExpr7(self, ctx:MiniGoParser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#functioncall.
    def visitFunctioncall(self, ctx:MiniGoParser.FunctioncallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#exprlist.
    def visitExprlist(self, ctx:MiniGoParser.ExprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#exprprime.
    def visitExprprime(self, ctx:MiniGoParser.ExprprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#literal.
    def visitLiteral(self, ctx:MiniGoParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrayaccess.
    def visitArrayaccess(self, ctx:MiniGoParser.ArrayaccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#statement.
    def visitStatement(self, ctx:MiniGoParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assignstm.
    def visitAssignstm(self, ctx:MiniGoParser.AssignstmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#lhs.
    def visitLhs(self, ctx:MiniGoParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#ifstm.
    def visitIfstm(self, ctx:MiniGoParser.IfstmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#eliflist.
    def visitEliflist(self, ctx:MiniGoParser.EliflistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#elifstmlist.
    def visitElifstmlist(self, ctx:MiniGoParser.ElifstmlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#elstm.
    def visitElstm(self, ctx:MiniGoParser.ElstmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#elifstm.
    def visitElifstm(self, ctx:MiniGoParser.ElifstmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#statementlist.
    def visitStatementlist(self, ctx:MiniGoParser.StatementlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forstm.
    def visitForstm(self, ctx:MiniGoParser.ForstmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#condi.
    def visitCondi(self, ctx:MiniGoParser.CondiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#inifor.
    def visitInifor(self, ctx:MiniGoParser.IniforContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forvarini.
    def visitForvarini(self, ctx:MiniGoParser.ForvariniContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assignfor.
    def visitAssignfor(self, ctx:MiniGoParser.AssignforContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#rangefor.
    def visitRangefor(self, ctx:MiniGoParser.RangeforContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#breakstm.
    def visitBreakstm(self, ctx:MiniGoParser.BreakstmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#continuestm.
    def visitContinuestm(self, ctx:MiniGoParser.ContinuestmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#returnstm.
    def visitReturnstm(self, ctx:MiniGoParser.ReturnstmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#callstm.
    def visitCallstm(self, ctx:MiniGoParser.CallstmContext):
        return self.visitChildren(ctx)



del MiniGoParser