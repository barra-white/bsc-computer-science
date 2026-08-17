from pt_node import *
from tiny_scanner import *

class TinyParser:
    """
    Implementation of Tiny parser
    Uses recursive descent parsing to generate parse tree with a collection of mutually recursive parsing functions (one per grammar production)
    Generates a parse tree from a token stream
    """
    
    # single param for init is file path of text file containing tiny source code
    def __init__(self, filepath: str):
        self.__scanner = TinyScanner(filepath, verbose=True)
    
    def parse_program(self):
        """
        Parse tokens matching following production:
        <program> ::= <stmtseq>
        """
        self.__scanner.log("Parsing <program> ::= <stmtseq>")
        c = self.parse_stmtseq()
        return PTNode("program", [c])
    
    def parse_stmtseq(self):
        """
        Parse tokens matching following production:
        <stmtseq> ::= <statement> { SEMI <statement> }
        """
        self.__scanner.log("Parsing <stmtseq> ::= <statement> { SEMI <statement> }")
        c = self.parse_statement()
        children = [c]
        while self.__scanner.current.kind == "SEMI":
            self.__scanner.match("SEMI")
            children.append(self.parse_statement())
        return PTNode("stmtseq", children)
    
    def parse_statement(self):
        """
        Parse tokens matching following production:
        <statement> ::= <ifstmt>
                    |   <repeatstmt>
                    |   <assignstmt>
                    |   <readstmt>
                    |   <writestmt>
        """
        self.__scanner.log("Parsing <statement> ::= <ifstmt> | <repeatstmt> | <assignstmt> | <readstmt> | <writestmt>")
        if self.__scanner.current.kind == "IF":
            c = self.parse_ifstmt()
        elif self.__scanner.current.kind == "REPEAT":
            c = self.parse_repeatstmt()
        elif self.__scanner.current.kind == "ID":
            c = self.parse_assignstmt()
        elif self.__scanner.current.kind == "READ":
            c = self.parse_readstmt()
        elif self.__scanner.current.kind == "WRITE":
            c = self.parse_writestmt()
        else:
            self.__scanner.shriek("Illegal statement!!!")
            return PTNode("statement", [])
        return PTNode("statement", [c])
    
    def parse_ifstmt(self):
        """
        Parse tokens matching following production:
        <ifstmt> ::= IF <exp> THEN <stmtseq> END
                 |   IF <exp> THEN <stmtseq> ELSE <stmtseq> END
        """
        self.__scanner.log("Parsing <ifstmt> ::= IF <exp> THEN <stmtseq> END | IF <exp> THEN <stmtseq> ELSE <stmtseq> END")
        self.__scanner.match("IF")
        c = self.parse_exp()
        self.__scanner.match("THEN")
        s1 = self.parse_stmtseq()
        children = [c, s1]
        if self.__scanner.current.kind == "ELSE":
            self.__scanner.match("ELSE")
            s2 = self.parse_stmtseq()
            children.append(s2)
        self.__scanner.match("END")
        return PTNode("ifstmt", children)
            
    
    def parse_repeatstmt(self):
        """
        Parse tokens matching following production:
        <repeatstmt> ::= REPEAT <stmtseq> UNTIL <exp>
        """
        # log
        self.__scanner.log("Parsing <repeatstmt> ::= REPEAT <stmtseq> UNTIL <exp>")
        
        # match for REPEAT statement
        self.__scanner.match("REPEAT")
        # parse stmtseq
        s = self.parse_stmtseq()
        # match for UNTIL
        self.__scanner.match("UNTIL")
        # parse exp
        e = self.parse_exp()
        # return repeat node with parsed values in children
        return PTNode("repeatstmt", [s, e])
    
    def parse_assignstmt(self):
        """
        Parse tokens matching following production:
        <assignstmt> ::= ID ASSIGN <exp>
        """
        # log
        self.__scanner.log("Parsing <assignstmt> ::= ID ASSIGN <exp>")
        
        # match for identifier
        id = self.__scanner.match("ID")
        # match for assign
        self.__scanner.match("ASSIGN")
        # return assign node with expression in children and id value
        return PTNode("assignstmt", [self.parse_exp()], value = id)
        
    
    def parse_readstmt(self):
        """
        Parse tokens matching following production:
        <readstmt> ::= READ ID
        """
        # log
        self.__scanner.log("Parsing <readstmt> ::= READ ID")
        
        # match for READ statement
        self.__scanner.match("READ")
        # assign value
        varname = self.__scanner.current.value
        # match for identifier
        self.__scanner.match("ID")
        # return read node with value
        return PTNode("readstmt", [], value = varname)
        
    def parse_writestmt(self):
        """
        Parse tokens matching following production:
        <writestmt> ::= WRITE <exp>
        """
        # log
        self.__scanner.log("Parsing <writestmt> ::= WRITE <exp>")
        
        # match for WRITE statement
        self.__scanner.match("WRITE")
        # return write node with expression in children
        return PTNode("writestmt", [self.parse_exp()])
    
    def parse_exp(self):
        """
        Parse tokens matching following production:
        <exp> ::= <simple-expr> { <comp-op> <simple-expr> }
        """
        # log
        self.__scanner.log("Parsing <exp> ::= <simple-expr> { <comp-op> <simple-expr> }")
        
        # add simple-expr to chidlren
        children = [self.parse_simple_expr()]
        
        if self.__scanner.current.kind in {"LT", "EQ"}:
            # add compop to children
            children.append(self.parse_comp_op())
            # advance
            self.__scanner.advance()
            # add simple-expr to children
            children.append(self.parse_simple_expr())
        # return expression node with children
        return PTNode("exp", children)
    
    def parse_comp_op(self):
        """
        Parse tokens matching following production:
        <comp-op> ::= LT | EQ
        """
        # log
        self.__scanner.log("Parsing <comp-op> ::= LT | EQ")
        # return comp-op node with value
        return PTNode("comp-op", [], value = self.__scanner.current.value)

    def parse_simple_expr(self):
        """
        Parse tokens matching following production:
        <simple-expr> ::= <term> { <addop> <term> }
        """
        # log
        self.__scanner.log("Parsing <simple-expr> ::= <term> { <addop> <term> }")
        
        # add term to children
        children = [self.parse_term()]
        
        while self.__scanner.current.kind in {"PLUS", "MINUS"}:
            # add addop to children
            children.append(self.parse_addop())
            # append term to children
            children.append(self.parse_term())
        # return simple-expr node with children
        return PTNode("simple-expr", children)
    
    def parse_addop(self):
        """
        Parse tokens matching following production:
        <addop> ::= PLUS | MINUS
        """
        # log
        self.__scanner.log("Parsing <addop> ::= PLUS | MINUS")
        r = PTNode("addop", [], value = self.__scanner.current.value)
        
        if self.__scanner.current.kind in {"PLUS", "MINUS"}:
            self.__scanner.advance()
        return r
    
    def parse_term(self):
        """
        Parse tokens matching following production:
        <term> ::= <factor> { <mulop> <factor> }
        """
        # log
        self.__scanner.log("Parsing <term> ::= <factor> { <mulop> <factor> }")
        
        # add factor to children
        children = [self.parse_factor()]
        
        while self.__scanner.current.kind in {"TIMES", "OVER"}:
            # append mulop to children
            children.append(self.parse_mulop())
            # append factor to children
            children.append(self.parse_factor())
        # return term node with children
        return PTNode("term", children)
    
    def parse_mulop(self):
        """
        Parse tokens matching following production:
        <mulop> ::= TIMES | OVER
        """
        # log
        self.__scanner.log("Parsing <mulop> ::= TIMES | OVER")
        r = PTNode("mulop", [], value=self.__scanner.current.value)
        if self.__scanner.current.kind in {"TIMES", "OVER"}:
            self.__scanner.advance()
        return r
    
    def parse_factor(self):
        """
        Parse tokens matching following production:
        <factor> ::= LPAREN <exp> RPAREN | NUM | ID
        """
        # log
        self.__scanner.log("Parsing <factor> ::= LPAREN <exp> RPAREN | NUM | ID")
        # check for parenthesis
        if self.__scanner.current.kind == "LPAREN":
            self.__scanner.match("LPAREN")
            c = self.parse_exp()
            self.__scanner.match("RPAREN")
            return PTNode("factor", [c])
        # check if type is ID or num
        elif self.__scanner.current.kind in {"ID", "NUM"}:
            val = self.__scanner.current.value
            self.__scanner.advance()
            return PTNode("factor", [], val)
        else:
            self.__scanner.shriek("Invalid!!!")
            
if __name__ == "__main__":

    fpath = "../kroc-compiler/programs/write17.tny"
  
    parser = TinyParser(fpath)
    ptroot = parser.parse_program()

    print("Parse tree:")
    print("-" * 25)
    ptroot.dump()
    print("=" * 25)
    print()