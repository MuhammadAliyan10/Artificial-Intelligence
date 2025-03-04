## What Is Cross-Validation?

_Imagine you’re testing your fasting prediction model on 30 days of Ramadan data. You split it—20 days to train, 10 to test—and get 90% accuracy. Great, right? But what if those 10 test days were easy ones? Cross-validation (CV) is like running multiple tests, swapping different days as “test” each time, to see if your model’s good across all scenarios—not just lucky once. It’s like tasting your iftar dish from different batches to ensure it’s consistently delicious._

- **Simple Example: Split 10 days into 5 parts, test on each part—average the results.**

### Why Use It?

- _To trust your model: One test might over- or underestimate—like guessing fasting only on cool days._
- _To avoid overfitting: Training too well on one split might fail on new data—like memorizing one Ramadan’s weather._
- _To handle small data: Your 100-day fasting set needs robust checks._

### How Does It Work?

- **K-Fold CV:** _Split data into K parts (e.g., 5 folds). Train on K-1 parts, test on 1, repeat K times, average scores._
  - _Example: 30 days, 5 folds = 6 days per fold. Train on 24, test on 6, rotate 5 times._
- **Metrics** _Average accuracy, precision, recall, etc., across folds—gives a stable score._
- **Types**
  - **K-Fold:** _Standard, like above._
  - **Stratified K-Fold:** _Keeps yes/no balance—crucial for your rare failures/dropouts._

### When Do We Use It?

- _Small datasets: Your 100-day fasting data—don’t waste it on one split._
- _Imbalanced data: Your charity dropouts (5% 1s)—ensure rare cases aren’t missed._
- _Before deployment: Confirm your model works broadly—like prepping charity plans for all cities._
