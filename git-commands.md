# Git Commands and Practice Record

## 1. Configure Git

    git config --global user.name "Joshua Coutinho"
    git config --global user.email "bt25cse207@iiitn.ac.in"

Purpose: Configures the author information for commits.

## 2. Initialize a Repository

    git init -b main

Purpose: Initializes a Git repository with the main branch.

## 3. Check Repository Status

    git status

Purpose: Shows modified, staged, and untracked files.

## 4. Stage Files

    git add README.md
    git add git-commands.md
    git add exercise-01 exercise-02

Purpose: Selects files for the next commit.

## 5. Commit Changes

    git commit -m "Add assignment files"

Purpose: Records the staged changes in Git history.

## 6. View Commit History

    git log --oneline

Purpose: Displays previous commits.

## 7. Create a Branch

    git switch -c feature/input-validation

Purpose: Creates and switches to a feature branch.

## 8. Merge a Branch

    git switch main
    git merge feature/input-validation

Purpose: Merges changes from a feature branch into main.

## 9. Connect to GitHub

    git remote add origin https://github.com/zqvu/git-practice-rollnumber.git

Purpose: Connects the local repository to GitHub.

## 10. Push to GitHub

    git push -u origin main

Purpose: Uploads the main branch to GitHub.

## 11. Resolve a Merge Conflict

    git status
    git diff
    git add README.md
    git commit -m "Resolve README merge conflict"

Purpose: Inspects, stages, and commits a conflict resolution.

## Merge Conflict Record

A merge conflict occurs when two branches contain incompatible
changes to the same part of a file.

To resolve it, inspect the conflicting file, edit the conflicting
section, remove the conflict markers, save the corrected content,
and commit the resolution.

Update this record after performing the merge conflict exercise.

## 12. Verify the Repository

    git status
    git log --oneline --graph --all
    git remote -v

Purpose: Checks the working tree, commit history, and remote URLs.
