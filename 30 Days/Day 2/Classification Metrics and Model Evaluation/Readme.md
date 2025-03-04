## What Are Classification Metrics and Model Evaluation?

_Imagine you’re predicting whether you’ll fast tomorrow—yes (1) or no (0)—for 30 days. You guess each day, then check how often you’re right, how often you miss a “no,” or guess “yes” wrongly. Classification metrics are numbers that tell you how good your guesses are, beyond just “percent correct.” Model evaluation is the process of using these numbers to judge and improve your prediction system—like a coach reviewing your Ramadan fasting plan._

_Simple Example: You predict taraweeh attendance: [1, 0, 1], reality: [1, 0, 0]. Metrics show where you succeed or fail._

### Why Use Them?

_To measure success: Are you catching rare fasting failures (like your extreme weather case)?_
_To compare: Is one model better than another for charity dropouts?_
_To fix: If you miss too many “no’s,” tweak your approach—like adjusting suhoor to boost fasting._

### How Do They Work?\_

**Key metrics:**

- **Accuracy:** _Percent correct—e.g., 8/10 days right = 80%. Simple, but tricky if “yes” dominates (imbalanced data)._
- **Precision:** _Of your “yes” guesses, how many were right—e.g., 3 “yes” predictions, 2 true = 67%. Good when false positives (wrong “yes”) hurt._
- **Recall:** _Of real “yes” cases, how many you caught—e.g., 4 real “yes,” caught 3 = 75%. Key when missing “yes” (false negatives) is bad._
- **F1 Score:** _Balances precision and recall—e.g., harmonic mean of 67% and 75% ≈ 71%. Useful when both matter._
- **Confusion Matrix:** _Table of true vs. predicted—e.g., [[True No, False Yes], [False No, True Yes]]—shows all hits/misses._
- **ROC Curve & AUC:** _Plots true positives vs. false positives—like how well you trade off fasting guesses. AUC (0–1) summarizes it—1 is perfect._

### When Do We Use Them?

- _After training: Test on known data—like your 100-day fasting set._
- _When data’s messy: Imbalanced (few failures), noisy (random flips)—like your hard examples._
- _To decide: Pick the best model for real-world use—e.g., charity planning._
