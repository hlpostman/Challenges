# Add without Arithmetic Operators

#### The Challenge
The challenge here is to add two unsigned integers without the use of arithmetic operators (e.g. +, -, /, \*).  While it may seem that all our tools have been taken from us, our hands are far from tied.  Sure, we have to forego the use of arithmetic operators, but we can still use bitwise operators.  This [implementation](https://github.com/hlpostman/challenges/blob/master/add_without_arithmetic_operators/add_without_arithmetic_operators.py) relies on that fact, using bit manipulation to find and return the sum of the two numbers passed.  The every-day objects (whether mathematical or otherwise) represented in code are just that - *represented*, not purely occurring. What is more, the representation is constructed is by our own design: computer scientists imagined a way of representing all kinds of information with bits that could take on only the two values 0 and 1, and to this day we can manipulate what a given bit or string of bits represents by toggling the bit or bits from 0 to 1 or visa versa in strategic ways.  The bitwise solution to this problem serves as a friendly PSA to computer scientists: think creatively, and play to your strengths - there is always a way!

#### The Simple Case: No Common Bits Set *or* No Carrying Required
Suppose that you have the numbers 1 and 4 and you want to add them by using binary operators.  Well, the binary representation of 1 is `0001` and the binary representation of 4 is `0100`.  We could just use the bitwise OR, |, and return `1|4` which is  `0101`, or 5.  That gives us the right answer.  In cases like this where there are no common set bits between the addends (i.e. for any bit *n* that is set in addend *a*, then bit *n* is NOT set in addend *b*), we can also use the bitwise exclusive or, XOR, ^, with the same effect.

#### The Likely Case: Common Bits Set *or* Carrying Required
This time, suppose that you want to add the numbers 1 and 5 using binary operators.  We know that the correct answer is 6.  But if we use either of the methods suggested above for adding 1 and 4, we get the wrong answer.  Why?  It's because our addends have common set bits.  Another way of saying this is that carrying is required.  Both our addends have the first bit, or the 1's place (i.e. 2\*\*0), set. Using the bitwise OR, we get 5 back as our result.  That's because the OR operator sees a 1 in the 1's place of at least one operand and accordingly sets the 1's place in our result - but does nothing to account for the fact that the 1's place is set in both addends.  We effectively *subtracted* the other 2\*\*0 from our result!  On the other hand, using the bitwise XOR gives us 4, which is even worse!  The bitwise XOR gives us 4 because it sees that the 1's place is set in both addends, and unsets the 1's place in the result accordingly.  This has the effect of subtracting *both* 2\*\*0's from the result.  

So you might wonder, what should we do?  How about a bitwise AND?  Nope - 1&5 is 1.  The AND returns only the common set bits - the OR is better than this.  What we need is a clever combination of all these operators.  The algorithm uses the XOR, the AND, and a *left shift* to modify the two addends and incrementally work towards the correct result.  The "too easy to be true" example given in the section **The Simple Case - No Common Bits Set *or* No Carrying Required** actually has quite a lot relevance however.  As we manipulate the addends, the "no common bits" or "no carrying required" case is the goal state; it is ultimately what tells us that our sum is ready to return.

#### Handling Carry *or* Getting from The Likely Case to The Simple Case
For certain addends, we enter the goal state immediately, as seen with the example of adding 1 and 4 in the section **The Simple Case - No Common Bits Set *or* No Carrying Required** above.  We get this behavior whenever the two addends passed have no common set bits, because no carrying is required.  We need a way to handle addends that do have one or more bit settings in common, such as 1 and 5 as seen in the section **The Likely Case: Common Bits Set *or* Carrying Required** above.  Let's look at what carrying really is for a moment, so we have a clear vision of what our solution will need to achieve. Since base 10 is analogous to, and usually more intuitive than, base 2, we'll start by considering what it means to carry in base 10.

For a given number *n* in a given base *b*, the digit *d* in a given place *p* indicates, loosely speaking that *n* contains *d* copies of *b*\*\**p*.  I say "loosely speaking" because

In any base *b* (whether it be 2 or 10 or something else)

In base 10, every "place" after the 1's place (i.e. "the 10's place", "the 100's place", etc. - "the 10\*\**p* place" where *p* is a positive integer)



continue to inspect the 1 and 5 example.

\* Common set bits iff carrying required - a note and explain bidirectional but consequential implication.  If you like this stuff, check out formal logic.



This question is a good reminder of the options available to us as computer scientists, and


 says "too much of a party here", and

Note this implementation does not do anything to protect against overflow, since Python 3 uses infinite precision and therefore does not "have" overflow.

serves as a polite PSA:

while b != 0:
    carry = a & b # Mask of the bits that will necessitate carrying  --> zero when no more carrying is required (no set bits coincide)
    a ^= b # Mask of the bits that, at this iteration, can be added into a from b without carrying
    b = carry << 1 # Mask of the

    The next iteration will take care of any  


    """
  i = 0
  x = 7 = 0111
  y = 3 = 0011
  carry = 7&3 = 0011
  x ^= y = 0100
  y = carry << 1 = 0110 = 6

  i = 1
  x = 4 = 0100
  y = 6 = 0110
  carry = 4&6 = 0100
  x ^= y = 0010
  y = carry << 1 = 1000 = 8

  i = 2
  x = 2
  y = 8
  carry = 2&8 = 0000
  x ^= y = 1010 = 10 <-- BINGO
  y = carry << 1 = 0000

  i = 3
  x = 10
  y = 0 --> don't run

      """

      address playground thing 7, 10 , 7, refernce vs value vs immutable int
