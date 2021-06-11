import os
import os.path

def get_matching_paths_recursively(rootdir, extension, verbose=0):
    "Returns a list of full paths. Searches 'rootdir' recursively for all files with 'extension'."
    if not rootdir.endswith(os.sep):
        rootdir+=os.sep
        
    if verbose:
        print(
            "Getting filenames for files with extension \"%s\" at:\n%s" %
            (extension, rootdir))
    results = []
    for root, subFolders, filenames in os.walk(rootdir):
        for filename in filenames:
            if filename.find(extension) == len(filename) - len(extension):
                path = os.path.join(root, filename)
                results.append(path)
    return results
