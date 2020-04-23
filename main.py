from flask import Request
# from child_project_module import print_child
from root_project_module import print_parent


def process_request(request: Request) -> str:
    """HTTP Cloud Function entry point."""

    print_parent()
    # print_child()

    return "Done"
