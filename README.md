# CardConnect Project
## Encryption and Decryption of Data
- Encrypt
        - `openssl aes-256-cbc -a -salt -in test.pdf -out test.enc`
- Decrypt
        - `openssl aes-256-cbc -d -a -in test.enc -out test.pdf`
