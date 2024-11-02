#!/usr/bin/env python3

import sys
import glob
import shutil

# Check usage
if len(sys.argv) < 3:
    print("Usage: replace.py <oldname> <newname> [optional: file pattern]")
    sys.exit(1)

# Arguments
oldname = sys.argv[1]
newname = sys.argv[2]

# File list for renaming and replacing
if len(sys.argv) == 3:
    # Default file patterns
    file_list = glob.glob("*.dat") + glob.glob("*.py") + glob.glob("*.template")
else:
    file_list = []
    for pattern in sys.argv[3:]:
        file_list.extend(glob.glob(pattern))

# Replace content and rename files
for fname in file_list:
    try:
        with open(fname, "r") as f:
            content = f.read()
        
        # Write replaced content back to file
        with open(fname, "w") as f:
            f.write(content.replace(oldname, newname))
        
        # Rename file if it contains oldname in filename
        new_fname = fname.replace(oldname, newname)
        if new_fname != fname:
            shutil.move(fname, new_fname)
    
    except Exception as e:
        print(f"Failed to process file {fname}: {e}")

