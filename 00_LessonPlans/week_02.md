# Week 02: Interactive Script (Age Calculator)

## Goals
- Learn user input (`input()`), type conversion, and error handling.
- Practice functions and conditionals.
- Create your first **interactive script**.
- Strengthen Git commit/push habits.

---

## Steps

### 1. Set up
- In `01_Code/Week_02/`, create `age100.py`.

---

### 2. Build the script
Write code that:
1. Asks the user for their **name** and **age** with `input()`.
2. Calculates the year they will turn 100.
   - Hint: `from datetime import date` → `date.today().year`
3. Prints a friendly message with the result.

---

### 3. Add error handling
- Use `try/except` to catch if the user enters a non-integer age.
- Add a check: if age <= 0 or > 120 → print an error message.

---

### 4. Wrap in a function
- Define `year_when_100(age: int, today_year: int) -> int`.
- Add a short docstring explaining what it does.
- Call the function in your script.

---

### 5. Run and test
- Run the script in the VS Code terminal (`py age100.py`) OR in Interactive Window.
- Test with valid and invalid inputs:
  - Normal (e.g., age 25).
  - Edge cases (negative numbers, 200, or “banana”).

---

### 6. Commit + Push
- Stage and commit after making it work:
  ```powershell
  git add 01_Code/Week_02/age100.py
  git commit -m "Add interactive age100 script"
  git push
  ```

---

### 7. README Update
- Edit `README.md` at the repo root to add a new section:
  ```markdown
  ## Week 2
  - `01_Code/Week_02/age100.py` → Interactive script (calculates year user turns 100)
  ```

- Commit and push the updated README.

---

### 8. Reflection Notes
- In `02_Notes/wins_and_frustrations.md`, add your Week 2 notes.
- In `02_Notes/ideas.md`, jot any ideas for scripts that take input and automate tasks.

---

## Deliverables
- `01_Code/Week_02/age100.py` in GitHub.
- README updated with Week 2 section.
- Notes updated with wins, frustrations, and ideas.

---

## Stretch Goal (optional)
- Modify the script to also ask for the user’s **birth year** and cross-check it against their stated age. If mismatch → print a warning.
