# Best Time to Buy and Sell Stock Problems

## Leetcode 121: buy one sell one
- brute-force
  - 在所有元素中取兩個元素，前為買後為賣，所有可能： $C^n_2 = O(n)$
- Transformation
  - 因為重要的其實不是 stock price 而是每天的變化值，因此我們將 array 由每天的股價轉化為每天的股價變化
  - 由此，解決問題的方向變成了去尋找總合為最大的連續區間，也就是所謂的 maximum subarray
- A solution using divide-and-conquer
  - 假設我們要找 A[low .. high] 的 maximum subarray
  - 由於 Divide-and-conquer 方法建議我們盡量將一個陣列分為同等長度的兩個陣列，故我們可先找到中間點 mid，則陣列被一分為二成 A[low .. mid] 和 A[mid+1 .. high] 兩者
  - 任何連續的陣列 A[i .. j] 都會落入以下三種情況
    - i, j 皆在 A[low .. mid] 內
    - i, j 皆在 A[mid+1 .. high] 內
    - i 在 A[low .. mid] 內，j 在 [mid+1 .. high] 內
    - 