
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AL_IM_INSTRUCTION BRANCH_INSTRUCTION BRANCH_ZERO_INSTRUCTION COLON COMMENT COMPARISON_IM_INSTRUCTION COMPARISON_INSTRUCTION DATAMOVE_INSTRUCTION DIRECTIVE EOL JUMP_LABEL JUMP_REG LABEL LA_INSTRUCTION LP LS_INSTRUCTION L_IM_INSTRUCTION MOVE_INSTRUCTION NUMBER REGISTER RINSTRUCTION RP SEGMENT STRING SYSCALLprogram : stmt_liststmt_list : stmt\n                 | stmt_list stmtstmt : EOL\n             | instruction EOL\n             | segment EOL\n             | labelInstruction EOL\n             | controlInstruction EOLlabelInstruction : LABEL COLON\n                        | LABEL COLON DIRECTIVE STRING\n                        | LABEL COLON DIRECTIVE NUMBERcontrolInstruction : JUMP_LABEL LABEL\n                          | JUMP_REG REGISTER\n                          | BRANCH_ZERO_INSTRUCTION REGISTER LABEL\n                          | BRANCH_INSTRUCTION REGISTER REGISTER LABEL\n                          | BRANCH_INSTRUCTION REGISTER NUMBER LABEL\n                          segment : SEGMENTinstruction : SYSCALL\n                    | RINSTRUCTION REGISTER REGISTER REGISTER\n                    | RINSTRUCTION REGISTER REGISTER NUMBER\n                    | AL_IM_INSTRUCTION REGISTER REGISTER NUMBER\n                    | L_IM_INSTRUCTION REGISTER NUMBER\n                    | LS_INSTRUCTION REGISTER LABEL\n                    | LS_INSTRUCTION REGISTER LP REGISTER RP\n                    | LS_INSTRUCTION REGISTER NUMBER LP REGISTER RP\n                    | LA_INSTRUCTION REGISTER LABEL\n                    | COMPARISON_INSTRUCTION REGISTER REGISTER REGISTER\n                    | COMPARISON_IM_INSTRUCTION REGISTER REGISTER NUMBER\n                    | DATAMOVE_INSTRUCTION REGISTER\n                    | MOVE_INSTRUCTION REGISTER REGISTER\n                    '
    
_lr_action_items = {'EOL':([0,2,3,4,5,6,7,8,9,20,25,26,27,28,29,34,38,40,41,46,47,51,54,55,58,59,60,63,64,65,66,67,68,69,71,],[4,4,-2,-4,26,27,28,29,-18,-17,-3,-5,-6,-7,-8,-9,-29,-12,-13,-22,-23,-26,-30,-14,-19,-20,-21,-10,-11,-27,-28,-15,-16,-24,-25,]),'SYSCALL':([0,2,3,4,25,26,27,28,29,],[9,9,-2,-4,-3,-5,-6,-7,-8,]),'RINSTRUCTION':([0,2,3,4,25,26,27,28,29,],[10,10,-2,-4,-3,-5,-6,-7,-8,]),'AL_IM_INSTRUCTION':([0,2,3,4,25,26,27,28,29,],[11,11,-2,-4,-3,-5,-6,-7,-8,]),'L_IM_INSTRUCTION':([0,2,3,4,25,26,27,28,29,],[12,12,-2,-4,-3,-5,-6,-7,-8,]),'LS_INSTRUCTION':([0,2,3,4,25,26,27,28,29,],[13,13,-2,-4,-3,-5,-6,-7,-8,]),'LA_INSTRUCTION':([0,2,3,4,25,26,27,28,29,],[15,15,-2,-4,-3,-5,-6,-7,-8,]),'COMPARISON_INSTRUCTION':([0,2,3,4,25,26,27,28,29,],[16,16,-2,-4,-3,-5,-6,-7,-8,]),'COMPARISON_IM_INSTRUCTION':([0,2,3,4,25,26,27,28,29,],[17,17,-2,-4,-3,-5,-6,-7,-8,]),'DATAMOVE_INSTRUCTION':([0,2,3,4,25,26,27,28,29,],[18,18,-2,-4,-3,-5,-6,-7,-8,]),'MOVE_INSTRUCTION':([0,2,3,4,25,26,27,28,29,],[19,19,-2,-4,-3,-5,-6,-7,-8,]),'SEGMENT':([0,2,3,4,25,26,27,28,29,],[20,20,-2,-4,-3,-5,-6,-7,-8,]),'LABEL':([0,2,3,4,21,25,26,27,28,29,33,35,42,56,57,],[14,14,-2,-4,40,-3,-5,-6,-7,-8,47,51,55,67,68,]),'JUMP_LABEL':([0,2,3,4,25,26,27,28,29,],[21,21,-2,-4,-3,-5,-6,-7,-8,]),'JUMP_REG':([0,2,3,4,25,26,27,28,29,],[22,22,-2,-4,-3,-5,-6,-7,-8,]),'BRANCH_ZERO_INSTRUCTION':([0,2,3,4,25,26,27,28,29,],[23,23,-2,-4,-3,-5,-6,-7,-8,]),'BRANCH_INSTRUCTION':([0,2,3,4,25,26,27,28,29,],[24,24,-2,-4,-3,-5,-6,-7,-8,]),'$end':([1,2,3,4,25,26,27,28,29,],[0,-1,-2,-4,-3,-5,-6,-7,-8,]),'REGISTER':([10,11,12,13,15,16,17,18,19,22,23,24,30,31,36,37,39,43,44,48,52,62,],[30,31,32,33,35,36,37,38,39,41,42,43,44,45,52,53,54,56,58,61,65,70,]),'COLON':([14,],[34,]),'NUMBER':([32,33,43,44,45,50,53,],[46,49,57,59,60,64,66,]),'LP':([33,49,],[48,62,]),'DIRECTIVE':([34,],[50,]),'STRING':([50,],[63,]),'RP':([61,70,],[69,71,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'stmt_list':([0,],[2,]),'stmt':([0,2,],[3,25,]),'instruction':([0,2,],[5,5,]),'segment':([0,2,],[6,6,]),'labelInstruction':([0,2,],[7,7,]),'controlInstruction':([0,2,],[8,8,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> stmt_list','program',1,'p_program','parser.py',22),
  ('stmt_list -> stmt','stmt_list',1,'p_stmt_list','parser.py',25),
  ('stmt_list -> stmt_list stmt','stmt_list',2,'p_stmt_list','parser.py',26),
  ('stmt -> EOL','stmt',1,'p_stmt','parser.py',37),
  ('stmt -> instruction EOL','stmt',2,'p_stmt','parser.py',38),
  ('stmt -> segment EOL','stmt',2,'p_stmt','parser.py',39),
  ('stmt -> labelInstruction EOL','stmt',2,'p_stmt','parser.py',40),
  ('stmt -> controlInstruction EOL','stmt',2,'p_stmt','parser.py',41),
  ('labelInstruction -> LABEL COLON','labelInstruction',2,'p_labelInstruction','parser.py',55),
  ('labelInstruction -> LABEL COLON DIRECTIVE STRING','labelInstruction',4,'p_labelInstruction','parser.py',56),
  ('labelInstruction -> LABEL COLON DIRECTIVE NUMBER','labelInstruction',4,'p_labelInstruction','parser.py',57),
  ('controlInstruction -> JUMP_LABEL LABEL','controlInstruction',2,'p_controlInstruction','parser.py',79),
  ('controlInstruction -> JUMP_REG REGISTER','controlInstruction',2,'p_controlInstruction','parser.py',80),
  ('controlInstruction -> BRANCH_ZERO_INSTRUCTION REGISTER LABEL','controlInstruction',3,'p_controlInstruction','parser.py',81),
  ('controlInstruction -> BRANCH_INSTRUCTION REGISTER REGISTER LABEL','controlInstruction',4,'p_controlInstruction','parser.py',82),
  ('controlInstruction -> BRANCH_INSTRUCTION REGISTER NUMBER LABEL','controlInstruction',4,'p_controlInstruction','parser.py',83),
  ('segment -> SEGMENT','segment',1,'p_segment','parser.py',92),
  ('instruction -> SYSCALL','instruction',1,'p_instruction','parser.py',108),
  ('instruction -> RINSTRUCTION REGISTER REGISTER REGISTER','instruction',4,'p_instruction','parser.py',109),
  ('instruction -> RINSTRUCTION REGISTER REGISTER NUMBER','instruction',4,'p_instruction','parser.py',110),
  ('instruction -> AL_IM_INSTRUCTION REGISTER REGISTER NUMBER','instruction',4,'p_instruction','parser.py',111),
  ('instruction -> L_IM_INSTRUCTION REGISTER NUMBER','instruction',3,'p_instruction','parser.py',112),
  ('instruction -> LS_INSTRUCTION REGISTER LABEL','instruction',3,'p_instruction','parser.py',113),
  ('instruction -> LS_INSTRUCTION REGISTER LP REGISTER RP','instruction',5,'p_instruction','parser.py',114),
  ('instruction -> LS_INSTRUCTION REGISTER NUMBER LP REGISTER RP','instruction',6,'p_instruction','parser.py',115),
  ('instruction -> LA_INSTRUCTION REGISTER LABEL','instruction',3,'p_instruction','parser.py',116),
  ('instruction -> COMPARISON_INSTRUCTION REGISTER REGISTER REGISTER','instruction',4,'p_instruction','parser.py',117),
  ('instruction -> COMPARISON_IM_INSTRUCTION REGISTER REGISTER NUMBER','instruction',4,'p_instruction','parser.py',118),
  ('instruction -> DATAMOVE_INSTRUCTION REGISTER','instruction',2,'p_instruction','parser.py',119),
  ('instruction -> MOVE_INSTRUCTION REGISTER REGISTER','instruction',3,'p_instruction','parser.py',120),
]
