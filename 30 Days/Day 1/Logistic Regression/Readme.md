## Logistic Regression

_Imagine you’re deciding whether to fast tomorrow based on how tired you feel today. If you’re exhausted (say, 8/10 tiredness), you might skip fasting; if you’re fresh (2/10), you’ll fast. Logistic regression predicts a yes/no outcome (fast or not) based on inputs (like tiredness). Instead of a straight line like linear regression, it gives a probability (0 to 1) and picks a category (e.g., >0.5 = yes)._

- **Simple Example:** _Will you buy dates for iftar? If they cost $2, probably yes; if $10, maybe no. Logistic regression finds the tipping point._

### Why Use It?

- **To classify:** _Will you fast? Will dates sell out? Will a delivery arrive on time?_
- **When the outcome is binary (yes/no, true/false), not a number.**

### How Does It Work?

_It uses a `sigmoid` curve: a squashed S-shape that turns numbers into probabilities between 0 and 1._

- **Inputs (X):** _Things like tiredness, date price, or weather._
- **Output (y):** _0 (no) or 1 (yes)._
- `Probability = 1 / (1 + e^-(m1*X1 + m2*X2 + b))`
  - _`m1, m2: `Weights for each input (e.g., tiredness matters more than weather)._
  - _`b:` Bias (baseline chance)._
  - _`e:` Math constant (~2.718)._
- _If probability > 0.5, predict 1; else, 0._

### When Do We Use It?

- _When you need a yes/no answer: Will it rain during taraweeh? Will you oversleep suhoor?_
- _When inputs affect a decision but don’t scale linearly (e.g., $5 vs. $10 dates might flip your choice)._
