# Kroc Compiler

CA Assignment 1 — Compilation, Year 4, BSc Computer Science.

A compiler for the Kroc teaching language: a lexical scanner, a tree-building parser, and a tree-walking code generator that emits three-address code (TAC), plus an interpreter that executes TAC programs.

**Note:** the scanner, parser, parse-tree node, compiler and TAC interpreter are a teaching skeleton provided by the module lecturer (Kieran Herley). The sample programs in `programs/` are my own work.

## Files

| File | Description |
|------|-------------|
| `kroc_scanner.py` | Lexical analyser — turns Kroc source into tokens |
| `kroc_parser_tree.py` | Recursive-descent parser — builds a parse tree |
| `pt_node.py` | Parse-tree node class |
| `kroc_to_tac_compiler.py` | Walks the parse tree and emits three-address code |
| `tac_engine.py` | Reads and executes TAC programs |
| `programs/` | Sample Kroc programs (`fact`, `readwrite`, `write17`) |

## Usage

```bash
python3 kroc_to_tac_compiler.py   # compiles programs/fact.krc to TAC
python3 tac_engine.py             # reads and runs a .tac program
```

Standard library only.
