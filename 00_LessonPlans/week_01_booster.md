# Week 01 – Mid-Week Booster (1 Hour)

This booster session is designed to keep your coding muscle active between Saturday blocks.  
Keep it short and focused — ~1 hour total.

---

## 🔹 Drills (15 min)
- Create a new file: `01_Code/Week_01/drills.py`.
- Implement a few small practice functions:
  ```python
  def is_even(n: int) -> bool:
      """Return True if n is even, False otherwise."""
      return n % 2 == 0

  def reverse_string(s: str) -> str:
      """Return the reverse of a string."""
      return s[::-1]

  def max_of_list(lst: list) -> int:
      """Return the largest element in a list."""
      return max(lst)
  ```
- Run each function with test inputs to confirm results.

---

## 🔹 Refactor Practice (20 min)
- Open `01_Code/Week_01/hello.py`.
- Add comments and a docstring:
  ```python
  """Week 1 hello world script for Git + Python practice."""

  # Print a simple message to confirm environment setup
  print("Hello, world!")
  print("Week 1 branch test.")
  ```
- Commit and push:
  ```powershell
  git add 01_Code/Week_01/hello.py
  git commit -m "Refactor hello.py with comments and docstring"
  git push
  ```

---

## 🔹 Repo Reading & Notes (25 min)
- Visit GitHub and skim a small Python repo (can even be your own sandbox).
- Look at:
  - How they organize folders.
  - How their README is structured.
  - How often they commit and how clear their messages are.
- In `02_Notes/questions.md`, jot down **2–3 takeaways** (what you’d like to emulate or avoid).

---

## ✅ Deliverables
- `01_Code/Week_01/drills.py` with 2–3 working functions.
- Updated `hello.py` with comments/docstring.
- Notes in `02_Notes/questions.md` reflecting on repo reading.
- All changes committed and pushed to GitHub.
