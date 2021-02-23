.data
	myID: .word 233 # this is comment

.text
	li $v0, 1
	lw $a0, myID
	syscall