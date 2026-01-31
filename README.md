# python-optimization-algorithm

Find the maximum number of packet each agent can carry to distribute most packets among a given number of agents.

Each packet can be divided into smaller packets, but packets cannot be merged.

All agents must carry the same number of packet.

## Examples

### Example 1

```python
packets = [7, 10, 4]
agents = 4
# packets = [3 + 4, 4 + 4 + 2, 4]
# packets = [3, 4, 4, 4, 2, 4]
output = 4
```

### Example 2

```python
packets = [3, 1]
agents = 10
output = 0
```

### Example 3

```python
packets = [7, 2]
agents = 4
# packets = [2 + 2 + 2 + 1, 2]
# packets = [2, 2, 2, 1, 2]
output = 2
```
