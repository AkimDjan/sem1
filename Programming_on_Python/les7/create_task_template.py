from parser import parser
from folder_creater import FolderCreator

if __name__ == "__main__":
    args = parser.parse_args()
    FolderCreator.create(args.task_id)

    
    