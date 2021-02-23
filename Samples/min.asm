.data
	a:		.word 1
	b:		.word 0
	c:		.word 7
	message:	.asciiz "The min is: "

.text	
	main:
	#load 3 int
		lw $t1, a
		lw $t2, b
		lw $t3, c
	
	#compare a and b, and store the smaller 1 in $t1
		bgt $t1, $t2, exchange1_2
	
	compare13:
		bgt $t1, $t3, exchange1_3
		
	printMIN:
		li $v0, 4
		la $a0, message
		syscall
		
		li $v0, 1
		move $a0, $t1
		syscall
	
	li $v0, 10
	syscall
	
	exchange1_2:
		move $t9, $t1
		move $t1, $t2
		move $t2, $t9
		
		j compare13
	
	exchange1_3:
		move $t9, $t1
		move $t1, $t3
		move $t3, $t9
		
		j printMIN
		