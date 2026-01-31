# python-optimization-algorithm

Find the maximum number of packet each agent can carry to distribute most packets among a given number of agents.

Each packet can be divided into smaller packets, but packets cannot be merged.

All agents must carry the same number of packet.

## Examples

1) Example 1
packets = [7, 10, 4]
agents = 4
=> packets = [3 + 4, 4 + 4 + 2, 4]
=> packets = [3, 4, 4, 4, 2, 4]
Output = 4

2) Example 2
packets = [3, 1]
agents = 10
Output = 0

3) Example 3
packets = [7, 2]
agents = 4
=> packets = [2 + 2 + 2 + 1, 2]
=> packets = [2, 2, 2, 1, 2]
Output = 2
