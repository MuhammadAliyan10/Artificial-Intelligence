## Linear Regression

_Imagine you are trying to predict how much time you will spend praying based on how many days into ramadan you are. On day 1, you might spend 30 minute, but by day 10, you notice you're spending 40 minutes, because you are more focused. Linear regression is a way to find a straight line that best predicts one thing(`prayer time`) based on another thing(`days in ramadan`). Its about finding patterns where one number grows or shrinks as another number changes_

### Example:

_If you buy mangoes, the total cost depends on how many you buy.`1 mango = 2$`, `2 mango = 4$`, `3 mango = 6$`. Linear regression draws a line through these points to predict the cost of any number. `(cost = 2 * number of mangoes)`_

### Why we use it?

- **To predict things :** _Will you spend 50 minutes by praying day 20? How much will 5 mango cost?_
- **To understand relationships :** _Does the day of Ramadan really effect your praying time, or is it something else?_

### How does it work?

_Think of it like fitting a ruler to a bunch of dots on a graph. You have:_

- **X(input) :** _Something you know like days of ramadan or number of mangoes._
- **Y(output) :** _Something you want to predict like prayer time or cost of mangoes._
- The line is an equation. `y = mx + c`
  - **m (slope) :** _How steep the line is. If `m = 2` every extra mango adds `2$` cost._
  - **b (intercept) :** _Where the line starts when `x = 0`. If you spend `1$` on a bag before buying mangoes, `b = 1`_
- _The goal is to tweak `m` and `b` so the line gets as close as possible to all your real data points._

### When do we use it?

- _When you think two things are connected in a straight-line way (e.g., more study time = better grades)._

- _When your data isn’t too wild (if prayer time jumps randomly between 10 and 60 minutes, a straight line won’t work well)._
