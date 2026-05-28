grammar evmTest;

program: statements EOF;

statements: statement+;

statement: variable_declaration | assignment | function_declaraion | if_statement | while_statement
            | for_statement | switch_statement;


// Variable Declaration
variable_declaration: variable_type id ASSIGN (value | expression) SEMICOLON;

variable_type: INT | FLOAT | STRING;

id: ID;

value: INT_LITERAL | FLOAT_LITERAL | STRING_LITERAL;

expression: expression ADD term | expression SUB term | term;

term: term MUL factor | term DIV factor | factor;

factor: SUB factor | id | value | '(' expression ')';


// Assignment
assignment: ID ASSIGN expression SEMICOLON ;


// Function Declaration
function_declaraion: function_type FUNCTION id '(' params? ')' function_body;

function_type: VOID | INT | FLOAT | STRING;

params: (variable_signature ',')* variable_signature;

variable_signature: variable_type id;

function_body: '{' (statement | return_statement)+ '}';

return_statement: RETURN (expression | id)? SEMICOLON;


// If Statement
if_statement: IF '(' condition ')' '{' (statement)* '}' elsif_statement* else_statement?;

condition: condition OR condition_and | condition_and;

condition_and: condition_and AND condition_compare | condition_compare;

condition_compare: expression operation expression | '(' condition ')';

operation: EQUAL | NOT_EQUAL | GREATER | GREATER_EQUAL | SMALLER | SMALLER_EQUAL;

elsif_statement: ELSIF '(' condition ')' '{' (statement)* '}';

else_statement: ELSE '{' (statement)* '}';


// While Statement
while_statement: WHILE '(' condition ')' '{' (statement)* '}';


// For Statement
for_statement: FOR '(' variable_declaration condition SEMICOLON update ')' '{' (statement)* '}';

update : id INC | id DEC | id ADD_ASSIGN expression | id SUB_ASSIGN expression | id ASSIGN expression;

// Switch Statement
switch_statement: SWITCH '(' expression ')' '{' case_statement+ '}' ;

case_statement: CASE '(' value ')' '{' (statement)* '}';



ASSIGN: '=';
SEMICOLON: ';';

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';

EQUAL: '==';
NOT_EQUAL: '!=';
GREATER: '>';
GREATER_EQUAL: '>=';
SMALLER: '<';
SMALLER_EQUAL: '<=';


INC: '++';
DEC: '--';
ADD_ASSIGN: '+=';
SUB_ASSIGN: '-=';

// Comment
LINE_COMMENT: LCSIGN ~[\r\n]* -> skip;
BLOCK_COMMENT: BCSIGN .*? BCSIGN -> skip;
LCSIGN: '^';
BCSIGN: '^^';

INT: 'int';
FLOAT: 'float';
STRING: 'string';
VOID: 'void';
FUNCTION: 'function';
RETURN: 'return';
IF: 'if';
ELSIF: 'elsif';
ELSE: 'else';
WHILE: 'while';
FOR: 'for';
SWITCH: 'switch';
CASE: 'case';
AND: 'and';
OR: 'or';

ID: ([a-zA-Z]|'_') ([a-zA-Z0-9]|'_')*;
INT_LITERAL: [0-9]+;
FLOAT_LITERAL: [0-9]+ '.' [0-9]*;
STRING_LITERAL: '"' ~["\r\n]* '"';

WS : [ \t] -> skip;
NEWLINE: [\n\r] ->skip;