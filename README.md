# Assessment 3.2: Linear Data Structure

**Name:** RESUJENTO
**Section:** IT2B
**Letters used:** R, E, S, U, J, E, N, T, O

## Purpose
This project turns the six algorithms from Assessment 3.1 into dynamic Python programs.
Each program adds the nine letters of RESUJENTO one at a time, displays the structure,
then removes one element at a time, displaying the updated structure after every step
until it is empty. Each program is in its own file and runs on its own.

## The six data structures
| File | Data structure | Insert | Remove | Removal order |
|---|---|---|---|---|
| `array.py` | Array (Python list) | append at end | remove LAST element | O, T, N, E, J, U, S, E, R |
| `linked_list.py` | Linked list (nodes + references) | insert at end | remove FIRST node, update head | R, E, S, U, J, E, N, T, O |
| `singly_linked_list.py` | Singly linked list (data + next) | insert at end | remove FIRST node, update head | R, E, S, U, J, E, N, T, O |
| `doubly_linked_list.py` | Doubly linked list (data + next + prev) | insert at end | remove LAST node, update tail, set new tail's next to None | O, T, N, E, J, U, S, E, R |
| `stack.py` | Stack (LIFO) | push | pop top | O, T, N, E, J, U, S, E, R |
| `queue.py` | Queue (FIFO, `collections.deque`) | enqueue (`append`) | dequeue (`popleft`) | R, E, S, U, J, E, N, T, O |

`None` is used wherever the algorithm says NULL.

## Open the project in PyCharm
1. Unzip `RESUJENTO_IT2B_Assessment_3.2.zip`.
2. In PyCharm choose **File > Open** and select the folder `RESUJENTO_IT2B_Assessment_3.2`.
3. If asked, choose **Trust Project**. Use any Python 3 interpreter.

## Run each file
1. Open the file in the Project panel (for example `array.py`).
2. Right-click inside the editor and choose **Run 'array'**, or click the green play button.
3. Compare the console with the matching file in the `outputs/` folder.
4. Repeat for the other five files.

Note: `array.py` and `queue.py` share names with Python standard library modules.
They run fine here because no file imports those modules. Use **Run** (not Debug).
Click **uploading an existing file**, drag in the six `.py` files, `README.md` and the `outputs`
folder, then click **Commit changes**. Copy the repository link from the address bar and submit it.

**PyCharm:** **Git > Create Git Repository**, add the files, **Commit**, then
**Git > GitHub > Share Project on GitHub**.
