.data
	newLine:    .asciiz "\n"
.text
	main:
		addi $s0, $zero, 19
		
		jal increaseReg
		
		li  $v0, 4
		la, $a0, newLine
		
		syscall
		
		jal printValue
		
	li $v0, 10
	syscall
	
	increaseReg:
		addi $sp, $sp, -8
		sw   $s0, 0($sp)
		sw   $ra, 4($sp)
		
		addi $s0, $s0, 23
		
		jal printValue
		
		lw   $s0, 0($sp)
		lw   $ra, 4($sp)
		addi $sp, $sp, 8
		
		jr $ra
		
	printValue:
		li $v0, 1
		move $a0, $s0
				
		syscall
		
		jr $ra
		
