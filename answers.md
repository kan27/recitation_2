# CMPS 2200 Recitation 02
## Answers

**Name:**_Srikanya Balaji Garuda__
**Name:**_________________________


Place all written answers from `recitation-02.md` here for easier grading.

- **4) (3 points)** Now, derive the asymptotic behavior of $W(n)$ using $f(n) = 1$, $f(n) = n$, and $f(n) = n^2$  with $a=2$ and $b=2$. Then, generate actual values for $W(n)$ for your code and confirm that the trends match your derivations.
  1. W(n) = 2*W(n/2) + 1
    Cost is asymptotically-dominated by the leaves, only need to consider their costs. Cost of each leave is 1, number of leaves in a binary tree is n. Final cost is $W(n) \in O(n)$
  2. W(n) = 2*W(n/2) + n
    Cost is constant across all levels in the tree (C(0) = n, C(1) = n). Total levels in the tree is $\lg n + 1$, Cost per level is n. Total cost across all levels is $n*(\lg n + 1)$. Final cost is $W(n) \in O(n\lg n)$
  3. W(n) = 2*W(n/2) + n^2
    Cost is asymptotically dominated by the root, we only need to consider the root's cost. Thus, final cost is $W(n) \in O(n^2)$

    --- f(n)=1 vs f(n)=n ---
|   n |   W_1 |   W_2 |
|-----|-------|-------|
|   1 |     1 |     1 |
|   2 |     3 |     4 |
|   4 |     7 |    12 |
|   8 |    15 |    32 |
|  16 |    31 |    80 |
|  32 |    63 |   192 |
|  64 |   127 |   448 |
| 128 |   255 |  1024 |

--- f(n)=n vs f(n)=n^2 ---
|   n |   W_1 |   W_2 |
|-----|-------|-------|
|   1 |     1 |     1 |
|   2 |     4 |     6 |
|   4 |    12 |    28 |
|   8 |    32 |   120 |
|  16 |    80 |   496 |
|  32 |   192 |  2016 |
|  64 |   448 |  8128 |
| 128 |  1024 | 32640 |

- **5) (4 points)** Now that you have a nice way to empirically 
  generate values of $W(n)$, we can look at the relationship 
  between $a$, $b$, and $f(n)$. If $f(n) = n^c$, we can derive 
  a very nice result.
  
  The Master Method gives an easy formula for solving general 
  recurrences of the form: 

    $$T(n) = aT(n/b) + n^c$$

  Its three cases correspond to the relationship between $\log_b a$ 
  and $c$. Derive the asymptotic behavior of $T(n)$ by solving its 
  general recursion tree for each of the three cases. Show your 
  recursion tree and derivations from it.

  1. $\log_b a < c$

  2. $\log_b a = c$

  3. $\log_b a > c$ 

- **7) (2 points)** Derive the asymptotic expressions for the span of the recurrences you used in problem 4 above. Confirm that everything matches up as it should. 