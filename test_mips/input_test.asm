# Hello, world!
# MIPS Assembly

      .data               # Data segment

# String to be printed:
message: .asciiz "Hello, world!"
msg:     .asciiz "HELLO"

      .text               # Code segment (instructions go here)

main:                    # Main entry point

      li $v0, 4           # System call code for printing string = 4
      la $a0, message     # Load address of string into $a0
      bltz $t1, loop
      sw $t2, 4($t0)
      syscall             # Call operating system to perform operation
                          # specified in $v0
                          # syscall takes its arguments from $a0, $a1, etc.
loop:                     # test for parser, no make sence
      li $v1, 5
      li $v0, 10          # Terminate the program
      syscall

.data               # Data segment

# String to be printed:
message2: .asciiz "Hello!"
