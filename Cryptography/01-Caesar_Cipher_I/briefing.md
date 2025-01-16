# 01-Caesar_Cipher_I

## Situation

Also know as the `Caesar Shift`, the `Caesar Cipher` simply involves 'shifting' the letters in the message up or down the alphabet by a given amount.

For Example:

In order to Encrypt the text `Hello World` with a `Caesar Shift` of 3, we would do the following:

```txt
HELLO WORLD

ABCDEFGHIJKLMNOPQRSTUVWXYZ
   ||  |   |  |  |    |   
DEFGHIJKLMNOPQRSTUVWXYZABC

KHOORZRUOG
```

Notice how we have converted the message by effectively moving each letter 3 spaces to the right in the alphabet.

We have also removed the spaces.

This technique is an extremely simple form of encryption, where the `secret` is just the number of letters shifted.

## Mission

You will be given a list of 3 random words and a random integer between 1 and 25.

Encrypt these words using the `Caesar Cipher`.

Take the last character of the encrypted string and encrypt it again. This will serve as a way to decrypt the message later.

Add this character to the beginning of your message.

Your solution should be all-caps and contain ***no*** spaces.

## Execution

1.
2.
3.

## Conclusion
