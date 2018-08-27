#/usr/bin/python

import sys;

g_input_file = "ips.list"

def convert_ip_to_nat_cmd(input_file):
    with open(input_file) as f:
        lines = f.readlines()
    lines = [x.strip() for x in lines]
    records = []
    for line in lines:
        numbers = line.split(".");
        if len(numbers) == 4:
            num_array = [int(x) for x in numbers]
            records.append({"str": line, "nums": num_array})
    records = sorted(records, key=lambda rec: rec['nums'][0]*256*256*256 + rec['nums'][1]*256*256 + rec['nums'][2]*256 + rec['nums'][3])
    
    for rec in records:
        print "line: %s || %d.%d.%d.%d" % (rec['str'], rec['nums'][0], rec['nums'][1], rec['nums'][2], rec['nums'][3])


if __name__ == "__main__":
    if len(sys.argv) == 2:
        g_input_file = sys.argv[1];
    elif len(sys.argv) == 1:
        g_input_file = "ips.list"
    else:
        print "Invalid parameters";

    convert_ip_to_nat_cmd(g_input_file);