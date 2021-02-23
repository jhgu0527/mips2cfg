.data
	end_loop: .asciiz "End of Loop"
	cur_sum: .asciiz " Sum: "
	space: .asciiz ", "
	newline: .asciiz "\n"

.text
	main:
		addi $t0, $zero, 0
		addi $t1, $zero, 0
	
	while:
		bgt $t0, 10, exit 
		jal printNum
		
		addi $t0, $t0, 1
		add  $t1, $t1, $t0
		syscall
		
		j while
	
	exit:
		li, $v0, 4
		la, $a0, end_loop
		syscall
		
	li $v0, 10
	syscall
	
	printNum:
		li $v0, 1
		add $a0, $t0, $zero
		syscall
		
		li $v0, 4
		la, $a0, space
		syscall
		
		li $v0, 4
		la, $a0, cur_sum
		syscall
		
		li $v0, 1
		move $a0, $t1
		syscall
		
		li $v0, 4
		la, $a0, newline
		syscall
		
		jr $ra
