.data
	a:		.word 336
	b:		.word 635
	c:		.word 216
	message:	.asciiz "The max is: "

.text	
	main:
	#load 3 int
		lw $t1, a
		lw $t2, b
		lw $t3, c
	
	#load $t1 and $t2 into $a0 and $a1
		add $a0, $zero, $t1
		add $a1, $zero, $t2
		
		jal returnMax
		add $t7, $zero, $v0
		
		# compare the larger of ($t1 and $t2) with $t3
		add $a0, $zero, $t7
		add $a1, $zero, $t3
		jal returnMax
		add $t7, $zero, $v0
		
		jal printMAX
		
	
	returnMax:
		slt $t5, $a0, $a1
		slt $t6, $a1, $a0
		
		mul $t5, $t5, $a1
		mul $t6, $t6, $a0
		add $v0, $t5, $t6
		
		jr $ra
		
	printMAX:
		li $v0, 4
		la $a0, message
		syscall
		
		li $v0, 1
		move $a0, $t7
		syscall
	
	li $v0, 10
	syscall
	