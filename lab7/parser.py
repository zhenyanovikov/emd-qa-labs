import re


def parse(out):
    receiver_line = re.search(r'([\d.]+-[\d.]+)\s+sec\s+([\d.]+\s+\w?Bytes)\s+([\d.])+\s+\w?bits/sec\s+receiver',
                              out.decode())
    interval, transfer, bandwidth = receiver_line.groups()
    result = {'Interval': interval, 'Transfer': transfer, 'Bitrate': bandwidth}
    return result
