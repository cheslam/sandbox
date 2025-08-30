# Week 01: Setup & Hello World

## Goals
- Install Python, VS Code, Git
- Create GitHub account & repo
- Run your first Python script
- Push code to GitHub

## Steps
1. Install Python 3.x from https://www.python.org/downloads/  
   - During install, check "Add Python to PATH"  
   - Confirm install: `python --version` in terminal  

2. Install VS Code from https://code.visualstudio.com/  
   - Install Python extension  

3. Install Git from https://git-scm.com/downloads  
   - Confirm install: `git --version`  

4. Create a GitHub account (if you don’t have one)  
   - Create one repo named `sandbox`  

5. In VS Code, make a new folder `Week_01` inside `01_Code/`  
   - Add file `hello.py` with:  
     ```python
     print("Hello, world!")
     ```  

6. Run script:  
   - Open terminal in VS Code → `python hello.py`  

7. Push code to GitHub:  
   - `git init`  
   - `git add hello.py`  
   - `git commit -m "week 01 hello world"`  
   - `git branch -M main`  
   - `git remote add origin <your_repo_url>`  
   - `git push -u origin main`  

## Deliverable
- Repo `sandbox` with `hello.py` inside
