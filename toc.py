# open README.md
# readlines
# remove everything in between <!-- START TOC --> 
#   and <!-- END TOC -->
# create list of header lines
# format into github-friendly table of contents
#   - 1 indent level per hash, starting at 0
#   - bullet list
# insert header list between <!-- START TOC --> 
#   and <!-- END TOC -->
# flatten into a single list
# write to README.md (test file first)

with open("README.md", "r") as file:
    file_lines = file.readlines()