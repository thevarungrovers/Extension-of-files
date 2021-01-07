# file name
fname = input("Enter Filename:")

# spliting the filename 
extname = list(fname.split("."))

#  extracting extension
lname = extname[1]

#comparing the extension 
if lname == 'py' or lname == 'PY':
    print('The extension of the file is python(py).')

elif lname == 'html' or lname == 'HTML':
    print('The extension of the file is Hyper text mark-up language (html).')

elif lname == 'css' or lname == 'CSS':
    print('The extension of the file is Cascading style sheet(css).')

elif lname == 'js' or lname == 'JS':
    print('The extension of the file is Javascript(js).')

elif lname == 'c' or lname == 'C':
    print('The extension of the file is C.')

elif lname == 'cpp' or lname == 'CPP':
    print('The extension of the file is C++.')
