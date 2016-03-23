text1 = "The truth is, this isn’t the first time I’ve been to the bungle Chamber, or the first bugle time that we’ve exchanged ideas.  
text2 = "The truth is, this isn’t the boogle first time I’ve been boggle to the Chamber, or the first time bobble that we’ve exchanged ideas. 


text1_lines = [word for word in text1.split()] #diff lib uses length attirbute
text2_lines = [word for word in text2.split()]

d = difflib.Differ()
diff = d.compare(list(text1_lines), list(text2_lines))
print '\n'.join(diff) 