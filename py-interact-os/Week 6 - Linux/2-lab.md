# Editing Files using Substrings

Search for all lines that contain "jane"

Find files from list.txt that are present within the system.

```bash
#!/bin/bash

> oldFiles.txt

files=$(grep " jane " ../data/list.txt | cut -d ' ' -f 3)

for file in $files; do
  if test -e /home/student-03-03352af5f976$file; then 
    echo "File exists"; 
    echo /home/student-03-03352af5f976$file >> oldFiles.txt 
else 
    echo "File doesn't exist"; 
  fi
done

echo $files
```

![](images/20230616134313.png)

---

Change names to required format of `jdoe`

```python

import sys
import subprocess

# Get the file name from command line argument
file_name = sys.argv[1]

# Open the file and read its contents
with open(file_name, 'r') as file:
    lines = file.readlines()

# Process each line in the file
for line in lines:
    old_name = line.strip()
    new_name = old_name.replace("jane", "jdoe")
    print(old_name)
    print(new_name)
```

![](images/20230616134236.png)