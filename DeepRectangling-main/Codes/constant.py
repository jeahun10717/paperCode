#training dataset path
# TRAIN_FOLDER = '/data/cylin/nl/Data/DIR-D-fusion/training' # original source
TRAIN_FOLDER = '/home/pllab/Desktop/jeahun/paper_code/DeepRectangling-main/Codes/DIR-D/training'

#testing dataset path
# TEST_FOLDER = '/data/cylin/nl/Data/DIR-D-fusion/testing' # original source
TEST_FOLDER = '/home/pllab/Desktop/jeahun/paper_code/DeepRectangling-main/Codes/DIR-D/testing'

#GPU index
GPU = '0'

#batch size for training
TRAIN_BATCH_SIZE = 4

#batch size for testing
TEST_BATCH_SIZE = 1

#num of iters
ITERATIONS = 100000

# checkpoints path
SNAPSHOT_DIR = "./checkpoints"

#sumary path
SUMMARY_DIR = "./summary"

# define the mesh resolution
GRID_W = 8
GRID_H = 6
