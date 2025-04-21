# 📦 Stack Implementation Using Linked Lists

This project is developed for **Assignment #3** of the Data Structures course. The objective is to implement a **Stack** using **Linked Lists** in Python and manage the development using **Git and GitHub**.

---

## ✅ Task Summary

- Transfer files from the template repository  
- Create a new branch for development  
- Implement the `ds.py` module with:
  - `LLNode`, `LinkedList`, `Stack` classes
- Ensure `main_LL.py` runs successfully  
- Make at least 2 commits  
- Merge the branch when completed

---

## 🔧 Class Overview

| Class        | Description                                           |
|--------------|--------------------------------------------------------|
| `Node`       | Basic data holder with ID, coordinates, and name      |
| `LLNode`     | Inherits from `Node`, adds `next` for linked list     |
| `LinkedList` | Adds/removes nodes at specific positions              |
| `Stack`      | Uses `LinkedList` to implement `push`, `pop`, `peek`  |

---

## 🔀 Git Workflow

```bash
git clone <repo-url>
git checkout -b stack-implementation
# work and commit at least twice
git add .
git commit -m "Implemented Stack using Linked List"
git checkout main
git merge stack-implementation
