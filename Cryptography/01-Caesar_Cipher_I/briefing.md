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

Your solution should be ***all-caps*** and contain ***no spaces***.

## Execution

1. Take your 3 words and shift-value from the `.data` attribute of the challenge.
2. Join the 3 words together to make your message for encryption.
3. Encrypt your message.
4. Encrypt the last letter again and put this value at the beginning of your message.
5. Ensure your message is in ***all-caps*** and contains ***no spaces***, then return it.

## Conclusion

Working out how to `shift` characters can be hard if you're new to Python, but if you are struggling for direction; look into the `ord()` and `chr()` functions.

Don't be afraid to fail a bunch of tasks or pull up and online

If you're sure you're doing everything right, make sure your data is all in the right format and that you are only supplying uppercase ***letters*** as part of your solution.
