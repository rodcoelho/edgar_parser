import json, os, time,re


def write_out_to_log(payload, cik_id):
    unix = str(int(time.time()))
    file_name = '/Users/rodrigocoelho/projects/edgar_parser/selenium_parser/output/' + cik_id + '-' + unix + '.txt'
    with open(file_name, 'a') as f:
        f.write(payload)

