# Portfolio Part 2 - Knowledge Question

1. Describe what is hashing is in general?

  - Hashing is the process that we used to create or convert a unique sequence
 from an input,it can be a string or a file, this sequence normally use letters and numbers,
 and this function is used to protect and secure the data.

2. Describe advantages and disadvantages for at least three different
   hashing algorithms.

  - Sha256 = Is a cryptographic hash function that converts a text input to an almost-unique alphanumeric string,
    the hash value will always be 256 bits.
    - Advantages: it can be useful to compare files or codes to identify unintentional only corruptions, and it is
      useful for storing password hashes as it slows down brute force attacks.
    - Disadvantages: it can be slower than other algorithms, is less secure, the collisions are easy to find, and the
      key length is too short to resist to attacks.
  
  - Message-Digest Algorithm 5 (MD5) = Is a one-way cryptographic function that converts messages of any length and 
    return them into a string output of a fixed length of 32 characters.
    - Advantages: is useful to compare between files or codes to identify any type of changes, and is easy to store
      smaller hashes.
    - Disadvantages: is slower than other algorithms, is more vulnerable to collisions, and it is easy to get the same
      hash function for two distinct inputs.
    
  - Blake2 = Is a cryptographic hash function designed to be fast, secure and versatile.
    - Advantages: is faster than some sha algorithms, is more resistance to collision, and support variable-length
      outputs.
    - Disadvantages: this algorithm is relative new compare to others so is not supported in some
      systems or old software and compatibility issues.

3. Provide a stepwise description of how can you store a password safely using a hashing technique and how
   you can verify that some string is the right password?

  - A) first of all we need the input from the user, after that we need a method to storage the password in this case
       I'm gonna use the salt method, so we need to create a random string with characters, so the input can be
       'password123' and the random string 'Kj7@ImwY0n8', after this we need to combine both passwords, so the salt
       method gonna convert the combine the two password into a fixed-length string, follow we need a hash function for
       which in can be Argon2 or other cryptographic hash function, so this can generate something
       like 'aDf89dFcv23', after having this we need to store the salt password because if is not store we can't 
       verificate. So after doing this the random string which is the salt and the new generate password which is the
       hashed password gonna be together in the user's record.
  - B) When the user provide the password which is the 'password123', we retrieve the salt password with the password to
       get the has password, we use the dame hash function to join the salt and the user password and have to produce
       the same hash password, after that we compare the hash password with the one that we have stored
       to verificate if they match or not, to give the correspond permission to access.

4. What is the purpose of a "salt" when hashing a password? what are the two most important properties of a "salt"?

  - The purpose of salt when we want to hashing a password is to enhance the security of it, so for example if two
    different users have the same password the salt method will create a different hash password for the two users.
    And the two most important properties I think are the uniqueness and randomness, because of this
    method going to generate a unique password every time, so we are never going to have the same password and the
    randomness because using a random number is going to give us an unpredictable result every time, make more difficult
   to hackers to access or try to guess the salt.

# References:

What Is SHA-256 Algorithm: How it Works and Applications [2022 Edition] | Simplilearn n.d., Simplilearn.com.

Hash Algorithm Comparison: MD5, SHA-1, SHA-2 & SHA-3 (codesigningstore.com)

BLAKE2 n.d., www.blake2.net.

Password Storage - OWASP Cheat Sheet Series 2015, Owasp.org.

Arias, D 2021, Adding Salt to Hashing: A Better Way to Store Passwords, Auth0.

Adding Salt to Hashing: A Better Way to Store Passwords n.d., www.youtube.com.

