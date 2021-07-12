
grammar Smolang;


/*
 * Parser Rules
 */

program     : line+ lastline;

line        : assignment NL
            | global_assignment NL
            | funcall NL
            | func_declaration NL
            | while_st NL
            | if_st NL
            | return_st NL
            | NL
            ;

lastline    : assignment EOF
            | global_assignment EOF
            | funcall EOF
            | func_declaration EOF
            | while_st EOF
            | if_st EOF
            | EOF
            ;

while_st     : 'while' LP condition RP codeblock ;

if_st       : 'if' LP condition RP codeblock
            | 'if' LP condition RP codeblock 'else' codeblock
            ;

return_st   : 'return' value ;

condition   : value operator value ;

operator    : ( '==' | '!=' | '>' | '<' | '>=' | '<=' ) ;

func_declaration 
            : 'function' typ ID LP (typ ID)? (',' typ ID)* RP codeblock;

codeblock   : '{' line+ '}' ;

funcall     : show_func 
            | read_func
            | custom_func
            ;

show_func   : 'show' LP value RP ;

read_func   : 'read' LP RP ;

custom_func : ID LP value? (',' value)* RP ;

global_assignment  
            : 'global' ID ASSIGN custom_func
            | 'global' ID ASSIGN value
            | 'global' ID ASSIGN read_func
            ;

assignment  : ID ASSIGN custom_func
            | ID ASSIGN read_func
            | ID ASSIGN value
            | ID '[' INT ']' ASSIGN read_func
            | ID '[' INT ']' ASSIGN custom_func
            | ID '[' INT ']' ASSIGN value
            ;

value       : ID
            | INT
            | REAL
            | STRING
            | ID '[' INT ']'
            | arithmetic
            | '[' list_value ']'      
            ;

list_value  : value? (',' value)* ;

arithmetic  : arithmetic ('*' | '/') arithmetic
            | arithmetic ('+' | '-') arithmetic
            | LP arithmetic RP
            | ar_value
            ;

ar_value    : (ID | INT | REAL)
            | ID '[' INT ']'
            | custom_func
            ;

typ         : ('int' | 'real' | 'void') ;

/*
 * Lexer Rules
 */
REAL        : [+-]?[0-9]*[.][0-9]+ ;
INT         : [+-]?[0-9]+ ;
STRING      : '"'.*?'"' ;
ID          : [a-z]+ ;
NL          : [;\n]  ;
LP          : '(' ;
RP          : ')' ;
ASSIGN      : '=' ;
WHITESPACE  : [ \t\r]+ -> skip ;
