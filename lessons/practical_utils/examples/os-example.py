import os

print 'working with permissions'
print 'Effective User  :', os.geteuid()
print 'Effective Group :', os.getegid()
print 'Actual User     :', os.getuid(), os.getlogin()
print 'Actual Group    :', os.getgid()
print 'Actual Groups   :', os.getgroups()

print 'process working directory'
print 'Starting:', os.getcwd()
print 'Moving up one:', os.pardir
os.chdir(os.pardir)
print 'After move:', os.getcwd()

print 'working with permissions'
print 'Testing:', __file__
print 'Exists:', os.access(__file__, os.F_OK)
print 'Readable:', os.access(__file__, os.R_OK)
print 'Writable:', os.access(__file__, os.W_OK)
print 'Executable:', os.access(__file__, os.X_OK)