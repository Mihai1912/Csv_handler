import re
import IPython.display as display

def detect_delimitator(header):
    if ',' in header:
        return ','
    elif ';' in header:
        return ';'
    
def replace_escape_quotes(line):
    return line.replace('\\"', "'")

def replace_delimitator_inside_quotes(line, delimitator):
    inside_quotes = False
    for i in range(0, len(line)):
        if line[i] == '"':
            inside_quotes = not inside_quotes
        elif line[i] == delimitator and inside_quotes:
            line = line[:i] + "Mihai19" + line[i+1:]
    return line

def nureplace_delimitator_inside_quotes(line, delimitator):
    return re.sub(r'(?<!")' + "Mihai19" + r'(?<!")', delimitator, line)
    

def pars_csv(filename):
    list = []
    file = open(filename, 'r')
    line = file.readline()
    delimitator = detect_delimitator(line)
    header = line.split(delimitator)

    if (filename == 'website_dataset.csv'):
        header[0] = 'domain'

    header[-1] = header[-1].replace('\n', '')

    while True:
        dict = {}
        line = file.readline()
        if not line:
            break
        line = replace_escape_quotes(line)
        line = replace_delimitator_inside_quotes(line, delimitator)
        line = line.split(delimitator)
        line[-1] = line[-1].replace('\n', '')
        for i in range(0, len(line)):
            line[i] = line[i].replace("Mihai19", delimitator)

        if len(line) != len(header):
            continue

        for i in range(0, len(header)):
            dict[header[i]] = line[i]
        list.append(dict)

    return list , header

def join (list1, list2, key):
    dict2 = {item[key]: item for item in list2}

    result = []
    for item in list1:
        if item[key] in dict2:
            result.append({**item, **dict2[item[key]]})

    return result

def main():
    facebook_data, facebook_header = pars_csv('facebook_dataset.csv')
    google_data, google_header = pars_csv('google_dataset.csv')
    website_data, website_header = pars_csv('website_dataset.csv')

    joined_data = join(facebook_data, google_data, 'domain')
    fin_joined_data = join(joined_data, website_data, 'domain')

    output = open('output.csv', 'w')
    output.write(','.join(facebook_header + google_header + website_header) + '\n')
    for item in fin_joined_data:
        output.write(','.join([item[header] for header in facebook_header + google_header + website_header]) + '\n')
    output.close()

if __name__ == '__main__':
    main()
    