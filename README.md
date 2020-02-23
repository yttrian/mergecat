# mergecat

Semi-automatic voice line clip extractor

## How to use

1. Install the package via `pip install mergecat` and make sure you have `ffmpeg`
2. Create a timing file in a format like this (using seconds)  
   Example:
   ```
   2 24
   60 75
   92 103
   128 135
   ```
3. Run mergecat via `mergecat video_file timing_file`  
   Example: `mergecat something.mp4 timing.txt`
   
## Goals

- [x] Handle temporary file cleanup
- [ ] Automate the process instead of requiring timing files
- [ ] Be more flexible than just using seconds
- [ ] Add input error checking
- [ ] Allow batch processing
