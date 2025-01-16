# 02-Caesar_Cipher_I

## Situation

As explored in the [previous challenge](/Cryptography/02-Caesar_Cipher_II/briefing.md), the `Caesar Cipher` is one of the simplest forms of encryption (and is very easily broken).

In the last challenge, we added our key to the message so that we can use a random shift every time we use the cipher.

This time we are going to be deciphering the message using the key.

For Example:

In order to Encrypt the text `Hello World` with a `Caesar Shift` of 3, we would do the following:

```txt
JKHOORZRUOG

Our key was just our last character, shifted; so let's unshift it.

G->H->I->J = 3 jumps

So now we know that in order to decipher our message we have to shift our letters by 3.

ABCDEFGHIJKLMNOPQRSTUVWXYZ
      ||  |   |  |  |    |   
   ABCDEFGHIJKLMNOPQRSTUVWXYZ

Which gives us:

HELLOWORLD
```

## Mission

You will be given a `Caesar Cipher` to decrypt.

Find the key by finding the difference between the first and last characters.

Use this key to decrypt the message

Your solution should be ***all-caps*** and contain ***no spaces***.

## Execution

1. Take the encrypted message from the `.data` attribute of the challenge.
2. Calculate the shift between the first and last characters (see [Part 1](/Cryptography/01-Caesar_Cipher_I/briefing.md))
3. Use this information to decrypt the rest of the message
4. Ensure your message is in ***all-caps*** and contains ***no spaces***, then return it.

## Conclusion

Make sure you've at least *read* [Part 1](/Cryptography/01-Caesar_Cipher_I/briefing.md) before you give this a go.

If you're sure you're doing everything right, make sure your data is all in the right format and that you are only supplying uppercase ***letters*** as part of your solution.
