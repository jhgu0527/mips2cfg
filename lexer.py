import ply.lex as lex

tokens = (
    'LP', 'RP', 'AL_IM_INSTRUCTION', 'RINSTRUCTION', 'L_IM_INSTRUCTION', 'LS_INSTRUCTION', 'LA_INSTRUCTION', 'JUMP_LABEL', 'JUMP_REG',
    'BRANCH_INSTRUCTION', 'BRANCH_ZERO_INSTRUCTION', 'COMPARISON_INSTRUCTION', 'COMPARISON_IM_INSTRUCTION', 'DATAMOVE_INSTRUCTION', 'MOVE_INSTRUCTION',
    'SYSCALL', 'REGISTER', 'SEGMENT', 'DIRECTIVE', 'LABEL','COLON','COMMENT', 'STRING', 'NUMBER', 'EOL'
)

def t_LP(t):
    r'\('
    return t

def t_RP(t):
    r'\)'
    return t

def t_AL_IM_INSTRUCTION(t):
    # r'(addi\b|addiu\b|subi\b|andi\b|ori\b|xori\b)'
    r'(addi\b|addiu\b|subi\b|subiu\b|andi\b|ori\b|xori\b)'
    return t

def t_RINSTRUCTION(t):
    # r'(add\b|sub\b|mul\b|div\b|and\b|or\b|xor\b|nor\b|slt\b|sll\b|srl\b|sra\b)'
    r'(add\b|addu\b|sub\b|subu\b|mul\b|div\b|and\b|or\b|xor\b|nor\b|slt\b|sll\b|srl\b|sra\b)'
    return t

def t_LS_INSTRUCTION(t):
    r'(lw\b|lb\b|lbu\b|lh\b|lhu\b|sw\b|sh\b|sb\b)'
    return t

def t_LA_INSTRUCTION(t):
    r'la\b'
    return t

def t_L_IM_INSTRUCTION(t):
    r'(li\b|lui\b)'
    return t

def t_JUMP_LABEL(t):
    r'(j\b|jal\b)'
    return t

def t_JUMP_REG(t):
    r'(jr\b|jalr\b)'
    return t

def t_BRANCH_INSTRUCTION(t):
    r'(beq\b|bne\b|bgt\b|bge\b|blt\b|ble\b)'
    return t

def t_BRANCH_ZERO_INSTRUCTION(t):
    r'(bgtz\b|bltz\b|bgez\b|blez\b)'
    return t

def t_COMPARISON_INSTRUCTION(t):
    r'(slt\b|sltu\b)'
    return t

def t_COMPARISON_IM_INSTRUCTION(t):
    r'(slti\b|sltiu\b)'
    return t

def t_DATAMOVE_INSTRUCTION(t):
    r'(mfhi\b|mflo\b|mthi\b|mtlo\b)'
    return t

def t_MOVE_INSTRUCTION(t):
    r'move\b'
    return t

def t_SYSCALL(t):
    r'syscall\b'
    return t

def t_REGISTER(t):
    # r'(\$(t|v|a)[0-9]|\$zero\b|\$ra\b)'
    r'(\$(v|k)[0-1]\b|\$a[0-3]\b|\$t[0-9]\b|\$s[0-7]\b|\$zero\b|\$ra\b|\$gp\b|\$sp\b|\$fp\b)'
    return t

def t_SEGMENT(t):
    r'(.text\b|.data\b|.rdata\b|.sdata\b)'
    return t

def t_DIRECTIVE(t):
    r'(.align\b|.ascii\b|.asciiz\b|.word\b)'
    return t

def t_NUMBER( t ) :
    r'-?[0-9]+'
    t.value = int( t.value )
    return t

def t_LABEL(t):
    r'[a-zA-Z0-9_]+'
    return t

def t_COLON(t):
    r':[\b\t]?'
    return t

def t_COMMENT(t):
    r'\#.+'
    pass

# def t_NUMBER( t ) :
#     r'[0-9]+'
#     t.value = int( t.value )
#     return t

def t_EOL( t ):
    r'\n+'
    t.lexer.lineno += len( t.value )
    return t

t_STRING = r'[ a-zA-Z0-9~!@$%^&*()_+\{\}|:"<>?`\[\]\;\',\\]+'

t_ignore = ' ,\t'

def t_error( t ):
    print("Invalid Token:", t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

# f = open("./input.asm", "r")
# s = f.read()
# lex.input(s)
# while True:
#     tok = lex.token()
#     if not tok: break
#     print(str(tok.type), str(tok.value))

s = '''
.data
    Hello_Msg: .asciiz "Hello"
.text
    j sdf
    mtlo $t3
    mfhi $a2
    mflo $t1
'''
# lex.input(s)
# while True:
#     tok = lex.token()
#     if not tok: break
#     print(str(tok.type), ':',str(tok.value))