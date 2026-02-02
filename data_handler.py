
data = "database\etfs.json"
access_data = open(data, 'r')

print(access_data.read())


class DataHandler(object):
    '''
    Docstring for DataHandler
    

"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

    '''
    # The coding will be layered based, therefore 1st we define sketch of functinality, 2nd we integrate with other parts, 3rd we add defensive programming practices, test and edge cases
    # add an assertion file_path should only work with json files.
    def __init__(self, file_path):
        self.file_path = file_path
        
    def read_data(self):
        r = open(self.file_path, 'r')
        return r
    
    def write_data(self):
        w = open(self.file_path, 'w')
        return w
        
    def create_data(self, archive_name):
        c = open(archive_name, 'x')
        return c
    
    def appending_data(self):
        a = open(self.write_data, 'a')
        return a
        
        
        
        
import json

class Graph:
    def __init__(self):
        # Let's assume an adjacency list: { node_id: [neighbor_id1, neighbor_id2] }
        self.adj_list = {}

    def save_to_json(self, filename):
        try:
            with open(filename, 'w') as f:
                # We need to use the json library here
                # Your logic goes here
                pass
            print(f"Successfully saved to {filename}")
        except Exception as e:
            print(f"Error saving file: {e}")
        
