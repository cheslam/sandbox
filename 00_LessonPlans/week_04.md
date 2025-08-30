# Week 04: Git Basics + First Automation

## Goals
- Practice Git branching
- Write your first real automation script
- Automate file renaming in a folder

## Steps
1. In `01_Code/Week_04/`, create `file_renamer.py`  

2. Script tasks:  
   - Take all `.txt` files in a folder  
   - Rename them sequentially: `file_1.txt`, `file_2.txt`, etc.  

3. Practice Git branching:  
   - Create new branch: `git checkout -b dev`  
   - Write your script on this branch  
   - Merge into main when working:  
     ```
     git checkout main
     git merge dev
     ```  

4. Push finished code to GitHub  

## Deliverable
- `file_renamer.py` in GitHub with before/after demo folder
