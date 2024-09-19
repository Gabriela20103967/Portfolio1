# Portfolio 2 - Knowledge Question  

1. Describe what is hashing is in general?
- Hashing is the process that we used to create or convert a unique sequence from an input, it can be a string or a file,
  this sequence normally uses letters and numbers, and this function is used to protect and secure the data.

2. Describe advantages and disadvantages for at least three different hashing algorithms.
- Sha256 = Is a cryptographic hash function that converts a text input an almost-unique alphanumeric string, the hash
  value will always be 256 bits.
  - Advantages: It can be useful to compare files or codes to identify unintentional only corruptions, and it is useful
    for storing password hashes as it slows down brute force attacks.
  - Disadvantages: It can be slower than other algorithms, is less secure, the collisions are easy to find, and the key
    length is too short to resist to attacks.
  
- Message-Digest Algorithm 5 (MD5) = Is a one-way cryptographic function that converts messages of any length and return
  them into a string output of a fixed length of 32 characters.
  - Advantages: Is useful to compare between files or codes to identify any type of changes and is easy to store smaller
    hashes.
  - Disadvantages: Is slower than other algorithms, is more vulnerable to collisions, and it is easy to get the same
    hash functions for two distinct inputs.
  
- Blake2 = Is a cryptographic hash function designed to be fast, secure and versatile
- Advantages: Is faster than some sha algorithm, is more resistance to collision, and support variable-length outputs.
- Disadvantages: This algorithm is relative new compare to others so is not supported in some systems or old software
  and compatibility issues.

3. Provide a stepwise description of how can you store a password safely using a hashing technique and how you can
   verify that some string is the right password?

- A)First we need to create a unique, random salt for each password, after that we need to combine the password and the
     salt, use a secure hashing algorithm to hash the combined password and salt, and save the hash and the salt in the
     database.
- B)To verify the right password we need first get the user's stored salt, combine the input password with the stored
     salt, to hash the combined input password and salt and compare the new hash with the stored hash. So, if they match.

4. What is the purpose of "salt" when hashing a password? what are the two most important properties of a "salt"?

- The purpose of "salt" when hashing a password is to ensure the security and uniqueness for identical password. And
  the two most important properties are randomness and uniqueness.


# References 
What Is SHA-256 Algorithm:How it Works and Applications [2022 Edition] Simplilearn n.d.,Simplilearn.com.

Hash Algorithm Comparison: MD5, SHA-1, SHA-2 & SHA-3 (codesigningstore.com)

BLAKE2 n.d., www.blake2.net.

Arias,D 2021, Adding Salt to Hashing: A Better Way to Store Password, Auth0.

Adding Salt to Hashing:A Better Way to Store Password n.d., www.youtube.com.
