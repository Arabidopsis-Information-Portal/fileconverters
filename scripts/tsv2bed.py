from time import localtime as lt 
import csv

def read_tsv_file():
    file_in = '/local/projects/AIP/DataProviders/noncodingRNA/snoRNA/DRSreads.snoRNA.tsv'
    file_out = '/local/projects/AIP/DataProviders/noncodingRNA/snoRNA/scripts/processed/DRSreads.snoRNA.bed'
    print('Source file location: ' + file_in)
    print('Reading tsv file has started...')
    processed_headers = ['chrom', 'chromStart','chromEnd', 'name', 'score', 'strand']
    file = open(file_out,'w')
    processed_file_writer = csv.writer(file, delimiter='\t')
    processed_file_writer.writerow(processed_headers)
    with open(file_in) as f:
        f_csv = csv.DictReader(f, delimiter='\t')
        for row in f_csv:
            process_row(f_csv, processed_file_writer, row)
    print('Reading tsv file has completed...')
    print('Processed (converted) file location: ' + file_out)
    file.flush
    file.close
    
def process_row(reader, writer,  row):
        print('Processing row...' + str(reader.line_num))
        processed_row = []
        
        name = row['Gene Name']
        score = row['DRS count']
        
        #parse location
        result = row['Location']
        print(result)
        result_list = str.split(result, ':')
        chrName = str.capitalize(result_list[0])
        
        word_strand = result_list[1]
        if word_strand == 'fwd':
            strand = '+'
        elif word_strand == 'rev':
            strand = '-'
        else:
            print 'Unknown strand'
        print ('Chromosome Name ' + chrName)
        print ('Strand ' + strand)
        
        start_chr_str = result_list[2]
        start_chr_int = int(start_chr_str) - 1        
        start_chr = str(start_chr_int)
        print('Chromosome Start ' + start_chr)
        
        end_chr = result_list[3]
        print('Chromosome End ' + end_chr)
        # end parse location
        
        processed_row.append(chrName)
        processed_row.append(start_chr)
        processed_row.append(end_chr)
        processed_row.append(name)
        processed_row.append(score)
        processed_row.append(strand)
        
        writer.writerow(processed_row)
        
    

def process_dataset():
    print('Dataset processing has started...')
    read_tsv_file()
    print('Dataset processing completed...')
    
def main():
    process_dataset();
 
if __name__ == '__main__': 
    main()
