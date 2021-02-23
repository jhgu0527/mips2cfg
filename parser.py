import ply.yacc as yacc
import lexer # Import lexer information

tokens = lexer.tokens # Need token list
filename = input("please input filename , end with .asm \n")
f = open(filename, "r")

class Segment():
    def __init__(self, label, seg_type, index, stmt_list, at_branch):
        self.label = label
        self.seg_type = seg_type
        self.index = index
        self.stmt_list = stmt_list
        self.at_branch = at_branch

class Program():
    def __init__(self, segment_list):
        self.segment_list = segment_list

curSegment = Segment('','',0,[], False)
curProgram = Program([])

def p_program(p):
    '''program : stmt_list'''

def p_stmt_list(p):
    '''stmt_list : stmt
                 | stmt_list stmt'''
    p[0] = []
    if p[1] is not None:
        p[0].append(p[1])
    if len(p) > 2:
        if p[2] is not None:
            p[1].append(p[2])
        p[0] = p[1]


def p_stmt(p):
    '''stmt : EOL
             | instruction EOL
             | segment EOL
             | labelInstruction EOL
             | controlInstruction EOL'''
    if len(p) != 2:
        p[0] = p[1]
        curSegment.stmt_list.append(p[1])
    if curSegment.at_branch == True:
        tempSegment = Segment(curSegment.label, curSegment.seg_type, curSegment.index, curSegment.stmt_list,
                              curSegment.at_branch)
        curProgram.segment_list.append(tempSegment)
        curSegment.label = ''
        curSegment.stmt_list = []
        curSegment.index += 1
        curSegment.at_branch = False

def p_labelInstruction(p):
    '''labelInstruction : LABEL COLON
                        | LABEL COLON DIRECTIVE STRING
                        | LABEL COLON DIRECTIVE NUMBER'''
    if(len(p) == 5):
        p[0] = []
        dict = {'declare label:': p[1]}
        p[0].insert(0, dict)
        p[0].insert(2, p[3])
        p[0].insert(3, p[4])
    else:
        p[0] = []
        dict = {'label:': p[1]}
        p[0].insert(0, dict)
        if len(curSegment.stmt_list) != 1:
            tempSegment = Segment(curSegment.label, curSegment.seg_type, curSegment.index, curSegment.stmt_list,
                                  curSegment.at_branch)
            curProgram.segment_list.append(tempSegment)
        else:
            curSegment.index -= 1
        curSegment.label = p[1]
        curSegment.stmt_list = []
        curSegment.index += 1

def p_controlInstruction(p):
    '''controlInstruction : JUMP_LABEL LABEL
                          | JUMP_REG REGISTER
                          | BRANCH_ZERO_INSTRUCTION REGISTER LABEL
                          | BRANCH_INSTRUCTION REGISTER REGISTER LABEL
                          | BRANCH_INSTRUCTION REGISTER NUMBER LABEL
                          '''
    p[0] = []
    for i in range(len(p)):
        if i != 0:
            p[0].append(p[i])
    curSegment.at_branch = True

def p_segment(p):
    '''segment : SEGMENT'''
    p[0] = p[1]
    new_index = curSegment.index + 1
    if new_index != 1:
        tempSegment = Segment(curSegment.label, curSegment.seg_type, curSegment.index, curSegment.stmt_list,
                              curSegment.at_branch)
        curProgram.segment_list.append(tempSegment)
        curSegment.index = new_index
        curSegment.seg_type = p[1]
        curSegment.label = ''
        curSegment.stmt_list = []
        # print("segment: {0}".format(p[1]))
    else:
        curSegment.index += 1

def p_instruction(p):
    '''instruction : SYSCALL
                    | RINSTRUCTION REGISTER REGISTER REGISTER
                    | RINSTRUCTION REGISTER REGISTER NUMBER
                    | AL_IM_INSTRUCTION REGISTER REGISTER NUMBER
                    | L_IM_INSTRUCTION REGISTER NUMBER
                    | LS_INSTRUCTION REGISTER LABEL
                    | LS_INSTRUCTION REGISTER LP REGISTER RP
                    | LS_INSTRUCTION REGISTER NUMBER LP REGISTER RP
                    | LA_INSTRUCTION REGISTER LABEL
                    | COMPARISON_INSTRUCTION REGISTER REGISTER REGISTER
                    | COMPARISON_IM_INSTRUCTION REGISTER REGISTER NUMBER
                    | DATAMOVE_INSTRUCTION REGISTER
                    | MOVE_INSTRUCTION REGISTER REGISTER
                    '''
    p[0] = []
    for i in range(len(p)):
        if i != 0:
            p[0].append(p[i])


def p_error( p ):
    print("Syntax error in input:")
    print(p)


def read_flow(segment_list):
    bb_dict = {}
    label_dict = {}
    flow_dict = {}
    jr_list = []
    j_list =[]
    jal_list = []
    final_list=[]
    label_list = []
    branch_ins = ['beq','bne','bgt','bge','blt','ble','bgtz','bltz','bgez','blez']
    branch_list=[]
    for segment in segment_list:
        # print(segment.at_branch)
        if len(segment.stmt_list):
             bb_dict[segment.index] = segment
        if segment.label != '':
             temp=segment.label.replace(':', '')
             label_dict[temp] = segment.index
             if segment.label !='main': label_list.append(segment.index)
    # print(bb_dict)
    # print(label_dict)
    # print(label_list)
    index_list = sorted(list(bb_dict.keys()))
    # print(index_list)
    for index in index_list:
        flow_dict[index]=[]
        if bb_dict[index].at_branch:
            if 'jr' in bb_dict[index].stmt_list[-1] and '$ra' in bb_dict[index].stmt_list[-1]:
                jr_list.append(index)
            if 'j' in bb_dict[index].stmt_list[-1]: 
                j_list.append(index)
            if 'jal' in bb_dict[index].stmt_list[-1]:
                jal_list.append(index)
            for ins in branch_ins:
                if ins in bb_dict[index].stmt_list[-1]:
                    branch_list.append(index)
        if ['li', '$v0', 10] in bb_dict[index].stmt_list  :
            final_list.append(index)
   
    if len(branch_list):          
        for i, index in enumerate(index_list):
            if index in branch_list:
                for element in bb_dict[index].stmt_list[-1]:
                    # if isinstance(element, str): element = element.replace(' ', '')
                    if element in list(label_dict.keys()):
                         flow_dict[index].append(label_dict[element])
                         if i< len(index_list)-1:
                             flow_dict[index].append(index_list[i+1])
                        #  index_list.remove(label_dict[element])   
    
    if len(j_list):
        for index in j_list:
            for element in bb_dict[index].stmt_list[-1]:
                if element in list(label_dict.keys()):
                     flow_dict[index].append(label_dict[element])
                    #  index_list.remove(label_dict[element])
    if len(jal_list):
        for index in jal_list:
            for element in bb_dict[index].stmt_list[-1]:
                if element in list(label_dict.keys()):
                     flow_dict[index].append(label_dict[element])
                    #  if label_dict[element] in jr_list:
                    #      x = index_list.index(label_dict[element])
                    #      if x< len(index_list)-1:
                    #         flow_dict[index].append(index_list[x+1])

    if len(jr_list):
        for index in jr_list:
            temp2= []
            for key in list(flow_dict.keys()): 
                 if index in flow_dict[key]:  temp2.append(key)                      
            for res in temp2:
                 i = index_list.index(res)
                 flow_dict[index].append(index_list[i+1])
            if index in index_list: index_list.remove(index)

    # print(j_list)
    # print(jr_list)
    # print(branch_list)
    # print(final_list)
    for i ,index in enumerate(index_list):
        if i< len(index_list)-1:
             if not flow_dict[index]:
                 flow_dict[index].append(index_list[i+1])
             if index not in label_list and index not in j_list and index not in jal_list: 
                 if index_list[i+1] not in label_list and index_list[i+1] not in flow_dict[index]:
                     flow_dict[index].append(index_list[i+1])
             

             if index in final_list:
                 flow_dict[index]=[]
    # print(flow_dict)     
    return bb_dict, flow_dict, branch_list    
       

    # for i, index in enumerate(index_list):
    #     # if not bb_dict[index].at_branch:
    #     #     if i< len(index_list)-1:
    #     #         flow_dict[index] = index_list[i+1]
    #     if bb_dict[index].at_branch:
    #         if 'jr' in bb_dict[index].stmt_list[-1] and '$ra' in bb_dict[index].stmt_list[-1]:
    #             jr_list.append(index)
    #         if 'j' in bb_dict[index].stmt_list[-1] or 'jal' in bb_dict[index].stmt_list[-1]:
    #             j_list.append(index)
    #         for ins in branch_ins:
    #             if ins in bb_dict[index].stmt_list[-1]:
    #                 branch_list.append(index)

    # print(j_list)
    # print(jr_list)
    # print(branch_list) 

    # if len(branch_list):          
    #     for i, index in enumerate(index_list):
    #         if index in branch_list:
    #             for element in bb_dict[index].stmt_list[-1]:
    #                 # if isinstance(element, str): element = element.replace(' ', '')
    #                 if element in list(label_dict.keys()):
    #                      k=[]
    #                      k.append(label_dict[element])
    #                      if i< len(index_list)-1:
    #                          k.append(index_list[i+1])
    #                      flow_dict[index] = k
    #                     #  index_list.remove(label_dict[element])                        

    # if len(j_list):
    #     for index in j_list:
    #         for element in bb_dict[index].stmt_list[-1]:
    #             if element in list(label_dict.keys()):
    #                  flow_dict[index] = label_dict[element]
    #                 #  index_list.remove(label_dict[element])
    
    # if len(jr_list):
    #     for index in jr_list:
    #         for key in list(flow_dict.keys()):
    #             if flow_dict[key] == index: temp2 = key
    #                 # print(temp2)

    #             if type(flow_dict[key]) == list:
    #                 if index in flow_dict[key]:  temp2 = key
    #                     # print(temp2)
    #         i = index_list.index(temp2)
    #         flow_dict[index] = index_list[i+1]
    #         if index in index_list: index_list.remove(index)

    # for i in range(len(index_list)):
    #     if i< len(index_list)-1:
    #          if index_list[i] not in list(flow_dict.keys()) and not bb_dict[index_list[i]].at_branch:

    #              flow_dict[index_list[i]] = index_list[i+1]
    
   
        
parser = yacc.yacc()

# read in file
# filename = input("please input filename , end with .asm \n")
# f = open(filename, "r")
# f = open("./samples/max.asm", "r")
s = f.read()

# s = '''
# .data
# 	end_loop: .asciiz "End of Loop"
# 	cur_sum: .asciiz " Sum: "
# 	space: .asciiz ", "

# .text
# 	main:
# 		addi $t0, $zero, 0
# 		addi $t1, $zero, 0
	
# 	while:
# 		bgt $t0, 100, exit 

# '''
# print(s)
s += 'EndOfFile: \n'

res = parser.parse(s)
bb_dict, flow_dict, branch_list = read_flow(curProgram.segment_list)
f = open("parser.txt", "w")
for segment in curProgram.segment_list:
    print('index: {0}, type: {1}, label: {2}'.format(segment.index, segment.seg_type, segment.label))
    f.write('index: {0},\ntype: {1},\n label: {2}'.format(segment.index, segment.seg_type, segment.label))
    f.write("\n")
    f.write(str(segment.stmt_list))
    f.write("\n")

with open ('./graph.dot', 'w') as out:
    for line in ('digraph \"CFG for input function\" {', 'size = "16,16";','label = \"CFG for input function\";'):
        out.write('{}\n'.format(line))
    for key in bb_dict: 
        label = str(bb_dict[key].stmt_list)
        
        label = label.replace('], [', '\l')
        label = label.replace(']', '\l')
        label = label.replace('[', '\l')
        symbols = [',','{','}',"\"",'\'']
        for sym in symbols:
           label = label.replace(sym, '')
        label = label.replace('::', ':')
        label = label.replace('\l\l', '\l')
        out.write('{} [shape=record,label="{}"];\n'.format(key, label))
    for key in list(flow_dict.keys()):
        # if type(flow_dict[key]) != list: 
        if len(flow_dict[key]) == 1:
            out.write('{} -> {};\n'.format(key, flow_dict[key][0]))
        # else:
        if len(flow_dict[key])>=2:
            if key in branch_list:
                 out.write('{} -> {} [label = "T"];\n'.format(key, flow_dict[key][0]))
                 out.write('{} -> {} [label = "F"];\n'.format(key, flow_dict[key][1]))
            else:
                for i in range(len(flow_dict[key])):
                     out.write('{} -> {};\n'.format(key, flow_dict[key][i]))
     
    out.write('}')
