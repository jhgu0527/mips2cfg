.text	
main:
	li	$s0, 1			# $s0:  i = 1
	li	$s4, 0			# $s4:  sum = 0

Loop:	
    bgt	$s1, 100, End      # when i > 100, then stop
	
	add	$s4, $s4, $s0		# $s4:  sum = sum + i
	addi	$s0, $s0, 1		# $s0:  i = i + 1
	j	Loop
	
End:	
	li	$v0, 1
	move	$a0, $s4		# $s7:  sum's final value
	syscall
	
	li $v0, 10
	syscall
	
