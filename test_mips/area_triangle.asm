li	$s0, 10		# $s0 = height of triangle
li	$s1, 5		# $s1 = width of triangle
mul	$s2, $s0, $s1	# $s2 = area of rectangle with height and width of $s0, $s1
srl	$s3, $s2, 1	# $s3 = area of triangle = area rectangle / 2

