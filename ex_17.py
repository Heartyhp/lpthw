from sys import argv
from os.path import exists
script,copy_to,copy_from = argv 



txt_from = open(copy_from)

#print(txt_to.read())
in_data = txt_from.read()

txt_to = open(copy_to, 'a')
txt_to.truncate()
txt_to.write(in_data)



#out_data = txt_to.read()
#print(f"the value of {out_data}")

txt_to.close()
txt_from.close()



