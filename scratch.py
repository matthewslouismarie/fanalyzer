from os import walk

filenames = []

_, _, filenames = next(walk('/home/louis/notdiscardable/Dropbox/fnc3'), (None, None, []))
print(filenames)