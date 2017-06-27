from collections import Counter


def read_file(filename):
    with open(filename + '.txt') as file:
        content = file.readlines()
    return content

def group_hostnames_by_request(content):
    host_requests_counter = Counter()
    for line in content:
        hostname = line.split(' - - ')[0]
        host_requests_counter.update({hostname: 1})
    return host_requests_counter

def write_to_file(host_requests_counter, filename):
    records_path = 'records_' + filename + '.txt'
    records = open(records_path,'w')

    for hostname, total_requests in host_requests_counter.items():
        records.write(hostname + ' ' + str(total_requests) + '\n')
    records.close()


filename = input()
content = read_file(filename)
host_requests_counter = group_hostnames_by_request(content)
write_to_file(host_requests_counter, filename)

