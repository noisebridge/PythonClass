import keyword

keywords = keyword.kwlist

control_flow_keywords = ['while', 'if', 'elif', 'raise', 'for', 'break', 'continue', 'else', 'pass', 'try', 'except', 'finally', 'with', 'as']

special_keywords = ['del', 'assert', 'class', 'def', 'return', 'yield', 'lambda', 'exec', 'import', 'from', 'global', 'print']

not_control_flow_keywords = []
for word in keywords:
    if word not in control_flow_keywords:
        not_control_flow_keywords.append(word)

comparison_keywords = []
for word in not_control_flow_keywords:
    if word not in special_keywords:
        comparison_keywords.append(word)


print "There are three categories of keywords:"

print "Control Flow keywords:", control_flow_keywords

print "Comparison Keywords", comparison_keywords

print "Specialized Keywords:", special_keywords

print
print "Inside Specialized Keywords:"
print "Global level:", ['del', 'global']
print "User Feedback:", ['assert','print']
print "Classes:", ['class']
print "Functions", ['def', 'return', 'yield', 'lambda']
print "Module level:", ['import', 'from', 'exec']
print 
