.data
	count: .word 162
.text
	ll $t0, count
	
	li $v0, 1
	move $a0, $t0
	syscall 
	
	
	li $v0, 1
	syscall