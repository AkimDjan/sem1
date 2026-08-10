from argparse import ArgumentParser

parser = ArgumentParser(
    description=(
        "Script to create solution "
        "folder template for LeetCode"
    )
)

parser.add_argument(
    "--task-id", 
    type=str,
    required=True,
    help="folder ID for sollution for current task" 
)