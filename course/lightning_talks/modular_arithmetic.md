Dividing and Remainders
=======================
There are three operations in python that involve division.

1. a / b divides a by b, and returns a floating point number
2. a // b divides a by b, and returns an integer by rounding down
3. a % b finds the remainder of a // b

-------------------------------------------------------------------

1. What happens when these operations encounter edge cases?
    - If a or b are floating point numbers, what happens when you apply // or %?
    - If a or b are negative, what happens when you apply % or //?
    - What happens when b is 0?


2. The way Python handles modulo with negative numbers differs from how C handles modulo with negative numbers, as well as many other languages.  You can try the C operation with math.fmod.  The Python operation is intended to be more useful and intuitive for 'business logic'.  What is an example that demonstrates the difference in a non mathematical context?

3. The way a language treats modulo is related to the way a language treats integer division, by the equation a = n * b + r, where n = a // b and r = a % b.
There are essentially four options for division behavior.  What are they, and which do you think is most intuitive?

See also [Division and Modulus for Computer Scientists](https://www.microsoft.com/en-us/research/publication/division-and-modulus-for-computer-scientists)
