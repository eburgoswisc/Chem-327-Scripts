import argparse
import csv
import statistics
from time import sleep

def parse_chunks(chunks: list) -> None:
    
    new_chunks = []
    for c in chunks:
        filtered_chunk = list(filter(lambda x: x != [''], c))
        new_chunks.append(filtered_chunk)
    
    mode_chunks = statistics.mode([len(i) for i in new_chunks])
    new_chunks = list(filter(lambda x: len(x) == mode_chunks, new_chunks))

    zipped_chunks = zip(*new_chunks)
    
    # Get filename
    filename = next(zipped_chunks)[0]

    samples = [i[0] for i in next(zipped_chunks)]

    header = next(zipped_chunks)
    
    new_header = []
    for s,h in zip(samples, header):
        for i in h:
            new_header.append(f"{s} {i}")
    data = []
    for values in list(zipped_chunks)[3:]:
        new_values = []
        try:
            for t,v in values:
                new_values.append(t)
                new_values.append(v)
        except ValueError:
            continue
        dict_writer = dict()
        for key, v in zip(new_header,new_values):
            dict_writer[key] = v
        data.append(dict_writer)
    return data, new_header

def write_to_file(data: list, header:list, output:str) -> None:
    with open(output, 'w') as out:
        writer = csv.DictWriter(out, header)
        writer.writeheader()
        # Write data 
        writer.writerows(data)
    return

def get_chunks(filename: str) -> list:
    with open(filename, 'r') as f:
        chunks = []
        i = -1
        for line in f:
            if line.rstrip().startswith('Vernier'):
                i += 1
                chunks.append([])
            else:
                chunks[i].append(line.rstrip().split('\t'))

        return chunks

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='LabQuestParser')

    
    parser.add_argument('-i', '--spect-files', help='Path to text file with spect data.')
    parser.add_argument('-o', '--output', help='Name for output csv file', default='output.csv')

    args = parser.parse_args()

    chunks = get_chunks(args.spect_files)
    data, header = parse_chunks(chunks)
    write_to_file(data, header, args.output)

