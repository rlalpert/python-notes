import itertools

# create table of contents container
toc = []

# open README.md
# readlines
with open("README.md", "r") as file:
    lines = file.readlines()

# get the index of START TOC and END TOC
start_toc_index = lines.index('<!-- START TOC -->\n')
end_toc_index = lines.index('<!-- END TOC -->\n')

# remove everything in between <!-- START TOC --> 
#   and <!-- END TOC -->
for i in range(end_toc_index - start_toc_index - 1):
    del lines[start_toc_index+1]

# create list of toc lines
for line in lines:
    if line.startswith("#"):
        toc.append(line)

# format into github-friendly table of contents
# for line in toc:
    # formatting here
#   - 1 indent level per hash, starting at 0
#   - bullet list

# insert toc list between <!-- START TOC -->
lines.insert(start_toc_index+1, toc) 
#   and <!-- END TOC -->

# flatten into a single list
lines = list(itertools.chain.from_iterable(lines))

# write to README.md (test file first)
with open('README_test.md', 'w') as file:
    for line in lines:
        file.write(line)