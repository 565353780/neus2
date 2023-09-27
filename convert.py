import sys
sys.path.append('../colmap-manage/')

from colmap_manage.Module.colmap_manager import COLMAPManager
from colmap_manage.Module.dataset_manager import DatasetManager

data_folder_path = '/home/chli/chLi/Dataset/NeRF/3vjia_simple/'
video_file_path = '/home/chli/chLi/Dataset/NeRF/3vjia_person_2/1.mp41'
down_sample_scale = 4

scale = 1
show_image = False
print_progress = True
remove_old = False
valid_percentage = 0.8
dataset_folder_path = '../colmap-manage/output/3vjia_simple/'
method_dict = {
    'aabb_scale': 2,
}

COLMAPManager(data_folder_path).autoGenerateData(remove_old, valid_percentage)
DatasetManager().generateDataset('ns2', data_folder_path, dataset_folder_path,
                                 method_dict)
