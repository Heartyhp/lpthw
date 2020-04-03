from sys import argv

script, copy_from, copy_to = argv

destination = open(copy_to, 'w')
#truncate
source = open(copy_from)

txt = source.read()

destination.write(txt)


