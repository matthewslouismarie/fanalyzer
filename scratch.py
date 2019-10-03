from os import walk

_, _, filenames = next(walk('/home/louis/notdiscardable/Dropbox/fnc3'), (None, None, []))

for f in filenames:
    