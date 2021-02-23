.data
	myDouble: .double 0.573
	zero:     .double 0.123
.text
	li $v0, 3
	ldc1 $f6, myDouble
	ldc1 $f0, zero
	
	add.d $f12, $f6, $f0

	syscall 