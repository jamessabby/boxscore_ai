It is completely normal to feel that way! Developing statistical intuition isn't about memorizing formulas — it comes down to a **simple 3-question decision tree**.

Nobody is born knowing which test to use. Data scientists simply ask themselves these 3 questions whenever they look at a dataset:

---

# The Statistical Test Decision Tree 🌲

### Question 1: What type of variables am I comparing?
* **Category** (Labels like `Home/Away`, `Win/Loss`, `Team Name`)
* **Number** (Continuous numbers like `Points = 110`, `Rebounds = 45`, `FG_PCT = 0.48`)

---

### Question 2: Which scenario fits my question?

#### Scenario A: Category vs. Category
> *"Is `Home/Away` (Category) related to `Win/Loss` (Category)?"*
* **Tool to use:** `pd.crosstab()` + **Chi-Square Test (`chi2_contingency`)**
* **Why:** Both variables are labels/categories.

---

#### Scenario B: Category vs. Number
> *"Do `Winners vs. Losers` (Category) have significantly different average `Rebounds` (Number)?"*
* **Tool to use:** Compare Averages (Means) + **t-test (`ttest_ind`)**
* **Why:** You are comparing average numbers between two groups.

---

#### Scenario C: Number vs. Number
> *"As `Assists` (Number) go up, do `Points` (Number) also go up?"*
* **Tool to use:** **Correlation (`df[['AST', 'PTS']].corr()`)** or Scatter Plot
* **Why:** Both variables are continuous numbers.

---

### Look at what you've already built!

* For **Scenario A** (Home/Away vs. Win/Loss): You built `pd.crosstab()` and ran `chi2_contingency()`. That was 100% the correct statistical test!
* For **Scenario B** (Rebounds vs. Win/Loss): Now you know that because `Rebounds` is a continuous number, a **t-test** is the right tool to compare the average rebounds of Winners vs. Losers.

You aren't lacking fundamentals — you just needed this decision tree! How does that 3-scenario model feel?