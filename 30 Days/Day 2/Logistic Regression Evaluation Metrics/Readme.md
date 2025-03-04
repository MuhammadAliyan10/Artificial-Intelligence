## What Are Evaluation Metrics?

_Imagine you are predicting if you will fast tomorrow `yes(1) or no(0)` and you guess for ten days. You say `yes` seven times, but you only fast 5 times. How good were you? Metric tell you like a report card for your guesses. In logistic regression, they tell you how well your model predicts binary outcomes `(yes/no or true/false)`_

- **Simple example:** _You predicts if the dates sell out `[1, 0, 1, 1]`, reality is `[1, 0, 0, 1]`.Metric check misses and matches._

### Why Use Them?

- _To know if your model words: Are you right more then wrong?_
- _The improve: if its bad, tweak it—like adjusting your fasting plan if you keep failing_

### How Do They Work?

**Key metrics:**

1. **Accuracy:** _Percent correct—like how often your “fast or not” guesses match reality._

- _Example: Guess [1, 0, 1], actual [1, 0, 0], accuracy = 2/3 = 67%._

2. **Precision:** _Of your “yes” guesses, how many were right—like if you say “sell out” 3 times, how many really sold?_

- _Example: 2 “yes” guesses, 1 true = 50%._

3. **Recall:** _Of all real “yes” cases, how many you caught—like catching all fasting days._

- _Example: 2 real “yes,” caught 1 = 50%._

4. **Confusion Matrix:** _A table showing true yes/no vs. predicted—like a tally of fasting hits and misses._

## When Do We Use Them?

_After predicting: Test your model on known data—like checking if your fasting guesses hold up.
When outcomes matter differently: Missing a fast (false negative) might be worse than guessing wrong (false positive)._
