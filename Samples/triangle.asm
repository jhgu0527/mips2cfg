.data
	a:		.word 15
	b:		.word 5
	c:		.word 7
	trueMsg:	.asciiz "The three lines can form a triangle"
	falseMsg:	.asciiz "The three lines can not form a triangle"
	
.text 
	main:
	#load 3 int
		lw $t1, a
		lw $t2, b
		lw $t3, c
		
		add $t4, $t1, $t2
		add $t5, $t1, $t3
		add $t6, $t2, $t3
		
		slt $s0, $t3, $t4
		slt $s1, $t2, $t5
		slt $s2, $t1, $t6
		
		#s0, s1, s3 should be all true, then a triangle can be formed
		and $s1, $s1, $s2
		and $s0, $s0, $s1
		
		beq $s0, $zero, printFalse
		
		li $v0, 4
		la $a0, trueMsg
		syscall
		
		li $v0, 10
		syscall
	
	printFalse:
		li $v0, 4
		la $a0, falseMsg
		syscall
		