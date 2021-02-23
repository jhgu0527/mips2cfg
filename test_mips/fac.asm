function1:
#Store return address
addi $sp, $sp, -12
sw $ra, 0($sp)
sw $s0, 4($sp)
sw $s1, 8($sp)

#If($a0<3):$t0=1:$t0=0
slti $t0, $a0, 3

#if($t0=0):math
beq $t0, $zero, math
addi $v0, $zero, 1
j exit

math:
addi $sp, $sp, -4
sw $a0, 0($sp)
addi $a0, $a0, -2
jal function1
lw  $a0, 0($sp)
addi    $sp, $sp, 4

addi $t6, $zero, -3
mul $s0 $v0, $t6

addi $sp, $sp, -4
sw $a0, 0($sp)
addi $a0, $a0, -3
jal function1
lw  $a0, 0($sp)
addi    $sp, $sp, 4

addi $t6, $zero, 7
mul $s1, $v0, $t6
add $s1, $s0, $s1
addi $v0, $s1, 15

#Retrieve from stack
exit:
lw $ra, 0($sp)
lw $s0, 4($sp)
lw $s1, 8($sp)
addi    $sp, $sp, 12

jr $ra
