.data
	prompt:	.asciiz	"Your Input: "
	message: .asciiz "\nMy name is "
	userInput:	.space 15
	
.text	
	li $v0, 4
	la $a0, prompt2
	syscall	
	
	li $v0, 8
	la $a0, userInput
	la $a1, 15
	syscall

    
.data
	prompt2:	.asciiz	"Your Input 2: "
	
.text	
	li $v0, 4
	la $a0, message
	syscall	
	
	li $v0, 4
	la $a0, userInput
	syscall	
    
    li $v0, 10
    syscall
	
