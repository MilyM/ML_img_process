import os
import pandas as pd

folder_path = 'data/train/' 
 
csv_file = 'data/train_ship_segmentations_v2.csv'  
df = pd.read_csv(csv_file)
 
def file_exists(image_name, folder):
    return os.path.isfile(os.path.join(folder, image_name))
 
df = df[df['ImageId'].apply(lambda x: file_exists(x, folder_path))]
 
updated_csv_path = 'data/train_ship_segmentations.csv'
df.to_csv(updated_csv_path, index=False)
 
print(f'Zaktualizowany plik CSV został zapisany jako {updated_csv_path}')
 
 