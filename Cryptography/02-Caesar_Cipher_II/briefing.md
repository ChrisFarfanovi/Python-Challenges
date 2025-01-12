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

Encrypt these words using the `Caesar Cipher`.

Take the last character of the encrypted string and encrypt it again. This will serve as a way to decrypt the message later.

Add this character to the beginning of your message.

Your solution should be all-caps and contain ***no*** spaces.

## Execution

1.
2.
3.

## Conclusion
