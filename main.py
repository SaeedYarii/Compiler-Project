from antlr4 import *
import argparse
from gen.evmTestLexer import evmTestLexer
from gen.evmTestParser import evmTestParser
from custom_listener import evmTestCustomListener
from required_code_collection.ast_to_networkx_graph import show_ast

def main(arguments):
    # 1. Setup Input Stream
    stream = FileStream(arguments.input, encoding='utf8')

    # 2. Lexical Analysis
    lexer = evmTestLexer(stream)
    token_stream = CommonTokenStream(lexer)

    # 3. Parsing
    parser = evmTestParser(token_stream)
    parse_tree = parser.program()

    # 4. Semantic Analysis via Listener
    semantic_analyzer = evmTestCustomListener()
    semantic_analyzer.rule_names = parser.ruleNames

    walker = ParseTreeWalker()
    print(f"--- Starting Semantic Analysis on {arguments.input} ---")
    walker.walk(t=parse_tree, listener=semantic_analyzer)
    print("--- Analysis Complete ---")

    print("\n--- Variables Table ---")
    for name, info in semantic_analyzer.variables.items():
        print(f"{name}: {info}")

    print("\n--- Functions Table ---")
    for name, info in semantic_analyzer.functions.items():
        print(f"{name}: {info}")

    ast = semantic_analyzer.ast
    show_ast(ast.root)
    traversal = ast.traverse_ast(ast.root)
    print(traversal)

if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument('-i', '--input', help='Input source', default='input/test.txt')
    argparser.add_argument('-o', '--output', help='Output path', default='output/analysis_log.txt')
    args = argparser.parse_args()
    main(args)