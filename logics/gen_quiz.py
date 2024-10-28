import json, os, random
from pathlib import Path

FOLDER_1 = 'data'
FOLDER_2= 'new'

##one random preprocessed json file in folder "new"
def random_file():

    # Specify the directory
    # Current script directory
    current_directory = Path(__file__).resolve()
    # Parent directory
    parent_directory = current_directory.parent.parent

    # # Get the directory of the current script
    # base_dir = os.path.dirname(os.path.abspath(__file__))
    directory = os.path.join(parent_directory, FOLDER_1 )
    directory = os.path.join(directory, FOLDER_2 )


    # List all files in the directory
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    # Check if there are any files in the directory
    if files:
        # Randomly select a file
        selected_file = random.choice(files)
        print(f'Selected file: {selected_file}')
        return os.path.join(directory , selected_file)
    else:
        print('No files found in the directory.')

## 10 random mcq 
def gen_quiz():
  
    file_path = random_file() 
    
    #load json
    with open(file_path , 'r',encoding='utf-8', errors='ignore') as f:
        o = json.load(f ) 

    print(len(o))
    #pick 10 q
    q = random.sample(o, random.randint(10, 10))
    print(len(q))
    return(q)


if __name__ == "__main__":

    print( gen_quiz() )