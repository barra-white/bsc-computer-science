import re
import sys
import traceback
"""
Tiny Language Details:
    - pascal-like syntax
    - program = seq. of stmts separated by semicolons
    - ints only, no declarations
    - exps and assignments
        - arithmetic: vars, consts, +, -, *, /, ()
        - pascal-style identifiers
        - boolean: comparison ops, <, =
    - control
        - if-then-end
        - if-then-else-end
        - repeat-until
    - read, write perform simple I/O
    - comments enclosed in {}
    - features left recursion
"""
# define RE to capture Tiny comments
# group = captures any character (incl whitespace) one or unlimited times inside {}
COMMENT_RE = re.compile(r"\{([\s\S]*?)\}")

# define RE to capture Tiny tokens
TOKENS_RE = re.compile(r"[a-z]+"
                       r"|[0-9]+"
                       r"|[()+\-/*;]" # (\escape for -)
                       r"|:=|<|="
                    )

# define reserved words and their labels
RESERVED_WORDS = {
    "if": "IF", "then": "THEN", "else": "ELSE", "end": "END",
    "repeat": "REPEAT", "until": "UNTIL",
    "read": "READ", "write": "WRITE", "EOS": "EOS"
}

# define tiny's symbols and labels
SYMBOLS = {
    ";": "SEMI",
    "(": "LPAREN", ")": "RPAREN", 
    ":=": "ASSIGN",
    "<": "LT", "=": "EQ",
    "+": "PLUS", "-": "MINUS", "*": "TIMES", "/": "OVER",
    "STATEMENT": "STATEMENT"
}

# define padding for logging
LOGPAD = " " * 10

class TinyToken:
    """
    Encodes token kind and value
        string: string representation of token
        kind: label for token
        value: numerical value (integers only)
    """
    def __init__(self, tkn):
        self.string = tkn
        self.value = tkn
        # check if token is an identifier
        if tkn.isalpha():
            self.spelling = tkn
            if tkn in RESERVED_WORDS:
                self.kind = RESERVED_WORDS[tkn]
            else:
                self.kind = "ID"
        # check if token is an number
        elif tkn.isdigit():
            self.kind = "NUM"
            self.value = int(tkn)
        # check if token is a symbol
        elif tkn in SYMBOLS:
            self.kind = SYMBOLS[tkn]
        # invalid token
        else:
            self.shriek("Invalid token: '%s'." % tkn)
            
    def __str__(self):
        return ("Token: '%s' (%s)" % (self.string, self.kind))
            
class TinyScanner:
    def __init__(self, filepath: str, verbose: bool = False):
        """
        Create scanner object with source code from file at filepath
        """
        try:
            self.__source = open(filepath, "r").read()
        except Exception:
            traceback.print_exc()
            sys.exit(-1)
            
        self.verbose = verbose
        # remove comments
        self.__source = COMMENT_RE.sub("", self.__source)
        
        # setup token sequence
        self.__tokens = TOKENS_RE.findall(self.__source)
        self.__tokens.append("EOS")
        
        # init first token
        self.current = None
        self.advance()
        
    def __next_token(self):
        """
        Return next token or None
        """
        if self.current != "EOS":
            tkn = self.__tokens.pop(0)
            return TinyToken(tkn)
        return None
    
    # debugging
    def shriek(self, msg):
        """
        Print error message and terminate
        """
        self.log("*SCANNER*: %s" % msg, pad=False)
        sys.exit(-1)
    
    def log(self, msg, pad=True):
        """
        Print message (padding if True)
        """
        if self.verbose:
            print("%s%s" % (LOGPAD if pad else "", msg))
            
    def log_nopad(self, msg):
        """
        Print message (no padding)
        """
        if self.verbose:
            print(msg)
            
    # public methods
    def has_more(self):
        """
        Check if there are more tokens
        """
        return len(self.__tokens) > 0
    
    def advance(self):
        """
        Advance to next token
        """
        if self.has_more():
            self.current = self.__next_token()
            self.log_nopad("['%s']" % self.current.string)
    
    def match(self, t):
        """
        Check if current token matches token t
            True: advance
            False: error + terminate
        """
        val = self.current.value
        kind = self.current.kind
        
        if kind != t:
            self.shriek("Expected '%s', saw '%s'." % (t, self.current.string))
        self.advance()
        return val    