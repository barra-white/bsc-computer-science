# Tiny Compiler

CA Assignment 2 — Compilation, Year 4, BSc Computer Science.

A compiler for the Tiny teaching language (Pascal-like): a recursive-descent parser and a code generator that emits three-address code to a `.tac` file. Reads a pickled parse tree and produces executable TAC.

**Note:** `pt_node.py` (the parse-tree node class) is a teaching file provided by the module lecturer (Kieran Herley). The scanner, parser and compiler are my own work.

## Files

| File | Description |
|------|-------------|
| `tiny_scanner.py` | Lexical analyser for Tiny source |
| `tiny_parser.py` | Recursive-descent parser — builds a parse tree |
| `tiny_compiler.py` | Loads a pickled parse tree, generates TAC to a `.tac` file |
| `pt_node.py` | Parse-tree node class |
| `pkl_test.py` | Loads and dumps the pickled parse trees for inspection |
| `parse_trees/` | Pickled parse trees (`factorial`, `readwrite`, `write17`) |

## Usage

```bash
python3 tiny_parser.py     # parse a Tiny program and dump its parse tree
python3 tiny_compiler.py   # compile parse_trees/write17_pt_kh.pkl to write17.tac
```

Standard library only.
