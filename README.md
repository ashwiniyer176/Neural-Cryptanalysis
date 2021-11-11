# Neural Cryptanalysis on Classic Ciphers

## Aim
Cryptanalysis identifies weaknesses of ciphers and investigates methods to exploit them in order to compute the plaintext and/or the secret cipher key. Exploitation is nontrivial and, in many cases, weaknesses have been shown to be effective only on reduced versions of the cipher. The goal is to perform Cryptanalysis on Classical Ciphers using Neural Networks.

## Dataset

The dataset was created using the [Common Passwords List](https://www.kaggle.com/wjburns/common-password-list-rockyoutxt) from Kaggle. While this can be done with any NLP Dataset, using this particular dataset gives a twofold advantage:

1. Passwords can often be random. 
2. Passwords are limited by length, so the computation required is lower.
3. Passwords are one single word, so sequence dependency will not be a problem.
4. The dataset is large (14 million passwords) and thus can be cut short to speed up the training process.


## Usage

1. Open Anaconda Prompt
2. Run `setup.bat`
3. Check if `data/CaesarCipher.csv` exists.
4. If the above condition is done, you're good to go 

### Steps to change the encryption algorithm

1. Go to `utils/encryption.py` and make a function for your algorithm
2. Open `utils/dataset_creation.py` and import your function
3. Go to the `__main__` block of code.
4. Call `createDataset(df,encryption.your_algorithm,'YourFileName')`

## Contributors

<a href="https://github.com/ashwiniyer176/Neural-Cryptanalysis/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=ashwiniyer176/Neural-Cryptanalysis" />
</a>