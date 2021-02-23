.data
	InputMsg:  .asciiz "Enter an integer for factorial: "
	AnswerMsg: .asciiz "The factorial of 10 is: "
	Number:	   .word 0
	Answer:	   .word 0

.text
	.globl main
	main:
		# Read Number from User
		li $v0, 4
		la $a0, InputMsg
		syscall
		
		li $v0, 5
		syscall
		
		sw $v0, Number
		
		# call the factorial function
		lw $a0, Number
		jal	factorial
		sw $v0, Answer
		
		# print the answer
		li $v0, 4
		la $a0, AnswerMsg
		syscall
		
		li $v0, 1
		lw $a0, Answer
		syscall
		
		li $v0 10
		syscall	

#-------------------------------------------
# factorial function
	.globl factorial
	factorial:
		subu $sp, $sp, 8
		sw   $ra, ($sp)
		sw   $s0, 4($sp)
		
		li $v0, 1
		beq $a0, 0, baseCase
		
		move $s0, $a0
		sub  $a0, $a0, 1
		jal factorial
		
		mul $v0, $s0, $v0
		
	baseCase:
		lw $ra, ($sp)
		lw $s0, 4($sp)
		addu $sp, $sp, 8
		
		jr $ra
		 
		
		