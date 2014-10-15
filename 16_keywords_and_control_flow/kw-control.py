import keyword

keywords = keyword.kwlist

control_flow_keywords = ['if', 'elif', 'else', 'while', 'for', 'pass', 'break', 'continue', 'raise', 'try', 'except', 'finally', 'with', 'as']

special_keywords = ['del', 'assert', 'class', 'def', 'return', 'yield', 'lambda', 'exec', 'import', 'from', 'global', 'print']

not_control_flow_keywords = []
for word in keywords:
    if word not in control_flow_keywords:
        not_control_flow_keywords.append(word)

comparison_keywords = []
for word in not_control_flow_keywords:
    if word not in special_keywords:
        # Truly the remainder after removing control flow and 'special'
        comparison_keywords.append(word)

print "There are %s keywords: %s" % (len(keywords), keywords)
print
print "Lets break them into 3 categories:"

print "Control Flow keywords:", control_flow_keywords

print "Comparison Keywords", comparison_keywords

print "Specialized Keywords:", special_keywords

print
print "Inside Specialized Keywords:"
print "Namespace:", ['del', 'global', 'exec']
print "Import:", ['import', 'from']
print "User Feedback:", ['assert','print']
print "Classes:", ['class']
print "Functions", ['def', 'return', 'yield', 'lambda']
print 
