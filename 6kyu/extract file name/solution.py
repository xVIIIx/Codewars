class FileNameExtractor:
    def extract_file_name(dirty_file_name):
        #your code here
        x = dirty_file_name.split('_',1)
        y = ''.join(x[1]).split('.')
      
        
        return y[0]+'.'+y[1]
