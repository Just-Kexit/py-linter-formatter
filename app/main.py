def format_linter_error(error: dict) -> dict:
    return { "line": key[2],
        "column": key[3],
        "message": key[4],
        "name": key[0],
        "source": "flake8"
        for key in error
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": [format_linter_error(argument)],
        "path": file_path
        for argument in errors
        if errors "status": "failed"
        else "status": "passed"
    }



def format_linter_report(linter_report: dict) -> list:
    return [
        {
        "errors": [format_linter_error(desc)],
        "path": way
        for way, desc in argument
        if "errors" "status": "failed"
        else "status": "passed"
        }
        for argument in linter_report
        ]
return
