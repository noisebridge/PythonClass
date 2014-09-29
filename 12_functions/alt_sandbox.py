def fprintf(file, fmt, *args): 
    with open(file, 'w') as fp:
        fp.write(fmt % args)
# Use fprintf. args gets (42,"hello world", 3.45) 
fprintf("out.txt","%d %s %f", 42, "hello world", 3.45)

def fprintf(file, fmt, **kwargs): 
    with open(file, 'w') as fp:
        fp.write(fmt % args)
# Use fprintf. args gets (42,"hello world", 3.45) 
fprintf("out.txt","%d %s %f", num=42, greeting="hello world", almost_pi=3.45)
