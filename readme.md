dot -Tpng graph.dot -o xx.png


def cfg_generator(segment_list):
    bb_dict <- {}
    flow_dict <- {}

    # read code in each block to each node
    for segment in segment_list:
        if segmment.stmt_list is not NULL:
            bb_dict[segment.index] <- segment.stmt_list
            flow_dict[segment.index] <- []
        
    # read edges between blocks:
    index_list <- sorted(list(bb_dict(keys)))
    for index, block in bb_dict:
        if Branch_instruction in block:
            flow_dict[index].extend([branch.index, next_bb.index)
        if JumpLabel_instruction in block:
            flow_dict[index].append(jump_bb.index)
        if JumpandReturn_instruction in block:
            flow_dict[index].append(return_bb.index)
        if Termnination_instruction in block:
            flow_dict[index] <- NULL
        else  flow_dict[index].append(next_bb.index)

    # dot printout: 
    with open ('./graph.dot', 'w') as out:
        out.write('digraph \"CFG for input function\" {')    
        for key, block in bb_dict: 
            out.write('{} [shape=record,label="{}"];\n'.format(key, block))
        for key, flow_list in flow_dict:
            if len(flow_list) == 1: out.write('{} -> {};\n'.format(key, flow_list[0]))
            if len(flow_list) >= 2: 
               if branch_instruction in bb_dict[key]:
                   out.write('{} -> {} [label = "T"];\n'.format(key, flow_list[0]))
                   out.write('{} -> {} [label = "F"];\n'.format(key, flow_list[1]))
                else: out.write('{} -> {};\n'.format(key, flow_list[i])) for i in range(l(flow_list))
     
                  

        

            