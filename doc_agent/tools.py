


import os


def write_doc(documentation: str, filename: str) -> dict:
    """save the clojure vector of maps to a .clj file"""
    mode = "w" if not os.path.exists(filename) else "a"
    with open( filename, mode) as f:
        f.write(documentation)
    return {"status": "success"}