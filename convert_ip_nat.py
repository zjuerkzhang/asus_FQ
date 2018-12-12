#/usr/bin/python

import sys;

g_input_file = "ips.list"
g_subnet_scope = 4

def ip_addr_convert_str_to_array(str):
    numbers = str.split('.')
    if len(numbers) != 4:
        return [0, 0, 0, 0]
    return [int(x) for x in numbers]

def ip_addr_convert_array_to_int(ip_array):
    if len(ip_array) != 4:
        return 0
    return ip_array[0]*256*256*256 + ip_array[1]*256*256 + ip_array[2]*256 + ip_array[3]

def ip_addr_convert_int_to_array(ip_int):
    return [ip_int>>24 & 0xFF, ip_int>>16 & 0xFF, ip_int>>8 & 0xFF, ip_int & 0xFF]

def convert_ip_to_nat_cmd(input_file):
    with open(input_file) as f:
        lines = f.readlines()
    lines = [x.strip() for x in lines]
    lines = sorted(lines)
    filtered_lines = reduce(lambda x, y: x + [y] if x == [] or x[-1] != y else x, lines, [])
    #filtered_lines = lines
    records = []
    for line in filtered_lines:
        num_array = ip_addr_convert_str_to_array(line)
        records.append({"str": line, "nums": num_array})
    records = sorted(records, key=lambda rec: ip_addr_convert_array_to_int(rec['nums']))
    #filter_records = reduce(lambda x, y: x + [y] if x == [] or x[-1]['str'] != y['str'] else x, records, [])
    #records = filter_records

    subnets_int = []
    for rec in records:
        #print "line: %s || %d.%d.%d.%d" % (rec['str'], rec['nums'][0], rec['nums'][1], rec['nums'][2], rec['nums'][3])
        tmp_int = ip_addr_convert_array_to_int(rec['nums']) >> g_subnet_scope << g_subnet_scope
        if tmp_int not in subnets_int:
            subnets_int.append(tmp_int)

    for subnet_int in subnets_int:
        subnet_nums = ip_addr_convert_int_to_array(subnet_int)
        print "%d.%d.%d.%d" % (subnet_nums[0], subnet_nums[1], subnet_nums[2], subnet_nums[3])

if __name__ == "__main__":
    if len(sys.argv) == 2:
        g_input_file = sys.argv[1];
    elif len(sys.argv) == 1:
        g_input_file = "ips.list"
    else:
        print "Invalid parameters";

    convert_ip_to_nat_cmd(g_input_file);