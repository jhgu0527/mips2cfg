.data
	num:	.word	53
	isprimeMsg:  .asciiz " is Prime Number" 
	notprimeMsg: .asciiz " is not Prime Number"
.text	
	main:
		lw $t1, num
		
		addi $s0, $zero, 2
		div  $s1, $t1, 2
	
	while:
	# $s2 = num/$s0, $s3 = $s0 * $s2
		bgt  $s0, $s1, exit
		div  $s2, $t1, $s0
		mul  $s3, $s0, $s2
	
	# if $s3 == $t1, it is a prime number
		beq  $s3, $t1, notprime
		addi $s0, $s0, 1
		j while
	
	exit:
		li $v0, 1
		move $a0, $t1
		syscall
		
		li $v0, 4
		la $a0, isprimeMsg
		syscall
	
	li $v0, 10
	syscall
			
	notprime:
		li $v0, 1
		move $a0, $t1
		syscall
		
		li $v0, 4
		la $a0, notprimeMsg
		syscall
	
	li $v0, 10
	syscall
	