# Fix a Slow System with Python

At a media production company, a Python script is used to backup data daily from the production NAS (mounted at /data/prod) to the backup NAS (mounted at /data/prod_backup). With increasing data volumes, the backup now takes over 20 hours to complete using the original sequential code.

To optimize the script, multiprocessing can be implemented to leverage all available CPUs and parallelize the file copying. The script is modified to use Python's multiprocessing module and determine the CPU count with cpu_count(). A process pool is created with this count and rsync copy commands are spawned across worker processes.

The directory walking code is also optimized to only backup relevant directories under /data/prod by filtering the paths. The full file paths are passed to rsync to retain the original directory structures.

With these changes, the backup runtime is significantly reduced by distributing work across multiple CPUs. The script is now more efficient and performs the daily backup well within the required time window. Multiprocessing allows computationally intensive tasks like large file copies to be parallelized easily with Python.

```python
#!/usr/bin/env python3

import os
import subprocess
from multiprocessing import cpu_count, Pool

src = "/home/student-03-660bb01d2245/data/prod/"
dest = "/home/student-03-660bb01d2245/data/prod_backup/"

def backup(dirpath):
    subprocess.call(["rsync", "-arq", dirpath, dest])

if __name__ == "__main__":
    src_depth = src.count(os.path.sep)

    with Pool(processes=cpu_count()) as pool:
        for dirpath, dirs, files in os.walk(src):
            if dirpath.count(os.path.sep) == src_depth:
                pool.apply_async(backup, [dirpath])

        pool.close()
        pool.join()
```