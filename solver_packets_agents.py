def sum_packets(packets : list) -> int:
    '''
    Sum all packets in the list.
    '''
    total = 0
    for p in packets:
        total += p
    return total


def get_max_packets_recursively(packets : list, agents : int, max_packet : int) -> int:
    '''
    Recursive function to get the max packets each agent can carry.
    '''
    max_packets = 0
    #print(f'Agents : {agents} -- Max Packet : {max_packet}')
    for p in packets:
        divided_packets = p // max_packet
        #print(f'Packet : {p} -- Divide packet : {divided_packets}')
        if (divided_packets > 0):
            max_packets += divided_packets
    #print(f'Max packet : {max_packets}')
    if max_packets >= agents:
        return max_packet
    return get_max_packets_recursively(packets, agents, max_packet-1)


def get_max_packets_iteratively(packets : list, agents : int, max_packet : int) -> int:
    '''
    Iterative function to get the max packets each agent can carry.
    '''
    packet_max = int(max_packet)
    while True:
        max_packets = 0
        #print(f'Agents : {agents} -- Max Packet : {packet_max}')
        for p in packets:
            divided_packets = p // packet_max
            #print(f'Packet : {p} -- Divide packet : {divided_packets}')
            if (divided_packets > 0):
                max_packets += divided_packets
        #print(f'Max packet : {max_packets}')
        if max_packets >= agents:
            return packet_max
        packet_max -= 1


def solve_packets_per_agent_problem(packets : list, agents : int) -> int:
    '''
    Return the max unit of packets each agent can carry.
    Each packet can be divided into smaller units, but none can be merged.
    Each agent must carry the same amount of packets.
    '''

    print(f'Packets : {packets} -- Agents : {agents}')

    if agents < 1:
        print('No agent')
        return 0

    size_packets = len(packets)
    if size_packets < 1:
        print('No packet to share')
        return 0
    
    total_packets = sum_packets(packets)
    if total_packets < agents:
        print('Less than one packet per agent')
        return 0
    if total_packets == agents:
        print('Exactly one packet per agent')
        return 1

    packets.sort(reverse=True)
    max_packet = packets[0]
    #print(f'Max Number : {max_packet} -- Sorted packets : {packets}')
    if agents == 1:
        print(f'Exactly one agent, so takes the biggest packet : {max_packet}')
        return max_packet
    result = get_max_packets_iteratively(packets, agents, max_packet)
    print(f'Result : {result}')
    return result

def main():
    packets = [7, 10, 4]
    agents = 4
    result = solve_packets_per_agent_problem(packets, agents)
    print(f'Max unit of packets each agent can carry: {result}')
   

if __name__ == '__main__':
    main()
