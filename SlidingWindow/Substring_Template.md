# 10-line template for 'substring' problems
## Template
```python
def findSubString(s: str)
    map = [0] * 128
    count
    begin = 0
    end = 0
    d

    # Map initialize
    for ()

    while end < len(s):
        if map[ord(s[end])] ?:
            # Modify count
        map[ord(s[end])] += 1
        end += 1

        while # count condition
            # update d here if finding minimum

            # increase begin to make it invalid/valid again

            if map[ord(s[begin])] ?:
                # Modify count
            map[ord(s[begin])] += 1
            begin += 1
        
        # update d here if finding maximum
    return d
```

## Example:
### 1. Minumum Window Substring:
```python
def minWindow(self, s: str, t: str) -> str:
        map = [0] * 128
        count = len(t)
        begin = 0
        end = 0
        d = float('inf')
        start_index = 0

        for char in t:
            map[ord(char)] += 1

        while end < len(s):
            if map[ord(s[end])] > 0:
                count -= 1
            map[ord(s[end])] -= 1
            end += 1
            while count == 0:
                if end - begin < d:
                    start_index = begin
                    d = end - begin

                if map[ord(s[begin])] == 0:
                    count += 1
                map[ord(s[begin])] += 1
                begin += 1
        return "" if d == float('inf') else s[start_index:start_index + d]
```

### 2. Longest Substring with At Most Two Distinct Characters:
```python
def lengthOfLongestSubstringTwoDistinct (s: str):
    map = [0] * 128
    count = 0
    begin = 0
    end = 0
    d = 0

    while end < len(s):
        if map[ord(s[end])] == 0:
                count += 1
            map[ord(s[end])] += 1
            end += 1
        
        while count > 2:
            if map[ord(s[begin])] == 1:
                count -= 1
            map[ord(s[begin])] -= 1
            begin += 1
        d = max(d, end - begin)
    return d
```
### 3. Longest Substring Without Repeating Characters:
```python
def lengthOfLongestSubstringWithoutRepeatingCharacters (s: str):
    map = [0] * 128
    count = 0
    begin = 0
    end = 0
    d = 0

    while end < len(s):
        if map[ord(s[end])] > 0:
                count += 1
            map[ord(s[end])] += 1
            end += 1
        
        while count > 2:
            if map[ord(s[begin])] > 1:
                count -= 1
            map[ord(s[begin])] -= 1
            begin += 1
        d = max(d, end - begin)
    return d
```