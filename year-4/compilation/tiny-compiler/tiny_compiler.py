import pickle as pkl
import os

from tiny_parser import *
from pt_node import *

class TinyCompiler:
    def __init__(self, pkl_filename):
        """
        Load pkl file containing validly formatted parse tree for a syntactically correct Tiny program
        """
        with open(pkl_filename, 'rb') as file:
            self.parse_tree = pkl.load(file)
        self.__varcount = 0
        self.__labcount = 0
        self.basename = os.path.splitext(os.path.basename(pkl_filename))[0]
        
        self.filename = self.basename+".tac"
        
        self.tac_code = []
    
    def translate(self):
        """
        Generates three-address-code (TAC) from Tiny program represented by parse_tree
        """
        self.__varcount, self.__labcount = 0, 0
        self.__codegen(self.parse_tree)
        self._append("halt;")
        self._write_to_file()
        
    def _append(self, code):
        self.tac_code.append(code+"\n")
        
    def _write_to_file(self):
        with open(self.filename, "w") as file:
            file.writelines(self.tac_code)
        
        
    def __new_var(self):
        """
        Generate and return fresh temporary variable name
        """
        self.__varcount += 1
        return f"t{self.__varcount}"

    def __new_label(self):
        """
        Generate and return fresh label name
        """
        self.__labcount += 1
        return f"l{self.__labcount}"
    
    def __codegen(self, root):
        """
        Generate TAC code represented by subtree 'root'
        """
        label = root.label
        children = root.children
        value = root.value
        
        actions = {
            "ifstmt": self.__codegen_if,
            "assignstmt": self.__codegen_assign,
            "readstmt": self.__codegen_read,
            "writestmt": self.__codegen_write,
            "repeatstmt": self.__codegen_repeat,
            "stmtseq": self.__codegen_stmtseq
        }
        
        if label in actions:
            actions[label](root)
        else:
            self.__codegen(children[0])
            
    def __codegen_stmtseq(self, root):
        """
        Generate TAC code for stmtseq represented by subtree 'root'
        """
        for child in root.children:
            if child.label != "SEMI":
                self.__codegen(child)
            
    def __codegen_if(self, root):
        """
        Generate TAC code for ifstmt represented by subtree 'root'
        """
        skiptrue_label = self.__new_label()
        expvar = self.__codegen_exp(root.children[0])
        self._append(f"if ({expvar} == 0) goto {skiptrue_label}")
        self.__codegen(root.children[1])
        
        if len(root.children) <= 2:
            self._append(f"{skiptrue_label}:")
        else:
            skipfalse_label = self.__new_label()
            self._append(f"goto {skipfalse_label}")
            self._append(f"{skiptrue_label}:")
            self.__codegen(root.children[2])
            self._append(f"{skipfalse_label}:")
        
    def __codegen_assign(self, root):
        """
        Generate TAC code for assignstmt represented by subtree 'root'
        """
        destvar = root.children[0].value
        rhsvar = self.__codegen_exp(root.children[-1])
        self._append(f"{destvar} := {rhsvar};")
    
    def __codegen_read(self, root):
        """
        Generate TAC code for readstmt represented by subtree 'root'
        """
        varname = root.children[0].value
        self._append(f"{varname} := in;")
    
    def __codegen_write(self, root):
        """
        Generate TAC code for writestmt represented by subtree 'root'
        """
        expvar = self.__codegen_exp(root.children[0])
        self._append(f"out := {expvar};")
    
    def __codegen_repeat(self, root):
        """
        Generate TAC code for repeatstmt represented by subtree 'root'
        """
        top_label = self.__new_label()
        self._append(f"{top_label}:")
        self.__codegen(root.children[0])
        expvar = self.__codegen_exp(root.children[1])
        self._append(f"if ({expvar} == 0) goto {top_label}")
            
    def __codegen_exp(self, root):
        """
        Generate TAC code for exp represented by subtree 'root'
        """

        if not root.children:
            return root.value
        total_var = self.__codegen_simple_expr(root.children[0])
        for i in range(1, len(root.children), 2):
            compop = root.children[i].children[0].value
            sevar = self.__codegen_simple_expr(root.children[i+1])
            newvar = self.__new_var()
            self._append(f"{newvar} := {total_var} {compop} {sevar}")
            total_var = newvar
        return total_var
        
        
    def __codegen_simple_expr(self, root):
        """
        Generate TAC code for simple-expr represented by subtree 'root'
        """

        if not root.children:
            return root.value
        total_var = self.__codegen_term(root.children[0])
        for i in range(1, len(root.children), 2):
            addop = root.children[i].children[0].value
            tvar = self.__codegen_term(root.children[i+1])
            newvar = self.__new_var()
            self._append(f"{newvar} := {total_var} {addop} {tvar}")
            total_var = newvar
        return total_var
        
    
    def __codegen_term(self, root):
        """
        Generate TAC code for term represented by subtree 'root'
        """

        if not root.children:
            return root.value
        total_var = self.__codegen_factor(root.children[0])
        for i in range(1, len(root.children), 2):
            mulop = root.children[i].children[0].value
            fvar = self.__codegen_factor(root.children[i+1])
            newvar = self.__new_var()
            self._append(f"{newvar} := {total_var} {mulop} {fvar}")
            total_var = newvar
        return total_var
    
    def __codegen_factor(self, root):
        """
        Generate TAC code for factor represented by subtree 'root'
        """
        fval=root.value
        if root.children[0].label == 'leaf':
            var = self.__new_var()
            varname = root.children[0].value
            self._append(f"{var} := {varname};")
            return var
        elif isinstance(fval, (int, str)):
            var = self.__new_var()
            self._append(f"{var} := {fval};")
            return var
        else:
            return self.__codegen_exp(root.children[0])
        
        
if __name__ == "__main__":
    tc = TinyCompiler("parse_trees/write17_pt_kh.pkl")
    tc.translate()