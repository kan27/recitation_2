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

To derive the asympottic behavior of $T(n) = aT(n/b) + n^c$, we need to analyze the recursion tree level by level.
Recursion Tree Structure:
Root:, Work = $n^c$
Level 1: $a$ ndes of size $n/b$, Work = $a*(\frac{n}{b})^c$ = $n^c * (\frac{a}{b^c})$
Level 2:, Work = $a^2*(\frac{n}{b^2})^c$ = $n^c * (\frac{a}{b^c})^2$
Level d: Work = $a^d*(\frac{n}{b^d})^c$ = $n^c * (\frac{a}{b^c})^d$
Leaf-Level ($d=\log_b n$, d is the level when $b^d = 1$): $a^(\log_b n) = n^(\log_b a)$ leaves, each performing O(1) work, so the work of all the leaves is $O(n^(\log_b a))$
Summing the work across all the levels d=0(root) to leaves:
$$T(n) = n^c \sum_{d=0}^{\log_b n - 1} \left(\frac{a}{b^c}\right)^d + \Theta(n^{\log_b a})$$
The growth factor between levels is $r=\frac{a}{b^c}$. Comparing $\log_b a$ to c determines whether $r<1, r=1, r>1$

Case 1: $log_b a < c$ (Root-dominated because the work done at each level shrinks like geometric decay, meaining the bulk of the work is at the root)
Summation: the geometric series converges
$$\sum_{d=0}^{\log_b n - 1} \left(\frac{a}{b^c}\right)^d \leq \sum_{d=0}^{\log_b n - 1} \left(r\right)^d = \frac{1}{1-r} = \Theta(1)$$
Thus total work is:
$$T(n) = n^c * \Theta(1) + \Theta(n^{\log_b a})$$
Since, the root work dominates the leaf work
$$T(n) = \Theta(n^c)$$

Case 2: $log_b a = c$ (Balanced because the work done at each level is the same)
Summation: There are $\log_b n$levels, each contributing $n^c$
$$\sum_{d=0}^{\log_b n - 1} \left(1)^d = \log_b n$$
Total work is thus:
$$T(n) = n^c * \Theta(log_b n) + \Theta(n^{\log_b a})$$
Remembering that $c = \log_b a$:
$$T(n) = \Theta(n^c\log n)$$

Case 3: $log_b a > c$ (Leaf-dominated because the work done at each level increases geometrically, meaining the bulk of the work is at the leaves)

- **7) (2 points)** Derive the asymptotic expressions for the span of the recurrences you used in problem 4 above. Confirm that everything matches up as it should. 