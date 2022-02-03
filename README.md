## Command-line version of [Wordle](https://www.powerlanguage.co.uk/wordle/)

Run with `python3 my_wordle.py`
Guess a 5 letter word!
* Note: My algorithm for giving hints (e.g., the `*` characters in my_wordle) differs slightly from the original Wordle's, but is still correct
* E.g., for the secret word `moist` and guess word `tests`, the following examples both hint for the letters `t` and `s`, but in different locations of `tests` :

**Wordle:**
<img src="./images/eg_wordle.png" alt="Wordle example" width="400"/>

**my_wordle:**

<img src="./images/eg_my_wordle.png" alt="my wordle example" width="175"/> &nbsp;

where `⏟` indicates gray boxes, `*` indicates yellow boxes, and the actual letters (e.g., `s`) indicate green boxes.


For copying results to Twitter (or other social media), `□` represents correct characters (hidden for others)

* E.g.,

<img src="./images/wordle_twitter.png" alt="Wordle example" width="200"/>
&emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp;
<img src="./images/my_wordle_twitter.png" alt="Wordle example" width="200"/>
