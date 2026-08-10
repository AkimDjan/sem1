import os
import re

"""
регулярные выражения - для проверки строки на параметры
1 правило ^[re] - строка должна начинаться с re
2 правило (re)$ - строка заканчивается на re
3 правило (re)* - строка может повторяться 0 и более раз 
4 правило [a-zA-Z0-9_]- указание что текущий символ может быть в диапазоне от a до z
от A до Z и от 0 до 9, включая _
"""

class InvalidTaskIDError(Exception):
    """Raises when task ID is not unique or task ID is invalid"""


class FolderCreator:
    TASK_ID_PATTERN: str = r"^[a-zA-Z0-9][a-zA-Z0-9_]*[a-zA-Z0-9]$"
    PATH_TO_TASKS_FOLDER: str = "tasks"
    INDENT: int = " " * 4
    SOLUTION_TEMPLATE: str = (
        f"class solution:\n{INDENT}# your code here"
        f"{INDENT}pass\n\n\nif __name__ == \"__main__\":\n"
        f"{INDENT}solution = Solution()\n{INDENT}# testcases\n"
    )

    @staticmethod
    def create(task_id: str) -> None:
        path_to_folder=FolderCreator._create_path_to_task_folder(
            task_id=task_id
        )
        os.makedirs(path_to_folder)

        path_to_solution = os.path.join(path_to_folder, "solution.py")
        with open(path_to_solution, "w") as file:
            file.write(FolderCreator.SOLUTION_TEMPLATE)
        
        readme_handler = " ".join(map(str.capitalize, task_id.split('_')))
        readme_handler = f'# {readme_handler}\n'
        path_to_readme = os.path.join(path_to_folder, "README.md")

        with open(path_to_readme, "w") as file:
            file.write(readme_handler)

    @staticmethod
    def _create_path_to_task_folder(task_id: str) -> str:
        if not re.match(FolderCreator.TASK_ID_PATTERN,task_id):
            raise InvalidTaskIDError(
                f"Task ID must match next pattern: {FolderCreator.TASK_ID_PATTERN}"
            )
        
        path_to_folder = os.path.join(FolderCreator.PATH_TO_TASKS_FOLDER, task_id)
        if os.path.exists(path_to_folder):
            raise InvalidTaskIDError(f"folder with task ID {task_id} already exists")
        return path_to_folder


