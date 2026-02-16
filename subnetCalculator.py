ip = "192.168.1.0"
parts = ip.split(".")
binary_parts = [format(int(p), '08b') for p in parts]
def cidr_to_mask(prefix):
    mask_bits = ('1' * prefix).ljust(32, '0')
    octets = [mask_bits[i:i+8] for i in range(0, 32, 8)]
    return [int(octet, 2) for octet in octets]  # return as list of ints now

def subnet_info(ip, prefix):
    # Convert IP to list of ints
    ip_parts = [int(p) for p in ip.split('.')]
    mask_parts = cidr_to_mask(prefix)

    # Network address = IP AND mask
    network = [ip_parts[i] & mask_parts[i] for i in range(4)]

    # Broadcast = network OR inverted mask
    broadcast = [network[i] | (255 - mask_parts[i]) for i in range(4)]

    # First usable host = network + 1
    first_host = network[:3] + [network[3] + 1]

    # Last usable host = broadcast - 1
    last_host = broadcast[:3] + [broadcast[3] - 1]

    # Total usable hosts = 2^(host bits) - 2
    host_bits = 32 - prefix
    total_hosts = (2 ** host_bits) - 2

    print(f"IP Address:    {ip}")
    print(f"Subnet Mask:   {'.'.join(map(str, mask_parts))}")
    print(f"Network:       {'.'.join(map(str, network))}")
    print(f"Broadcast:     {'.'.join(map(str, broadcast))}")
    print(f"First Host:    {'.'.join(map(str, first_host))}")
    print(f"Last Host:     {'.'.join(map(str, last_host))}")
    print(f"Total Hosts:   {total_hosts}")

# Example usage
# Get input from user
user_input = input("Enter IP/CIDR (e.g. 192.168.1.50/24): ")

# Split on the slash
ip, prefix = user_input.split('/')

# Convert prefix to int and run
subnet_info(ip, int(prefix))
