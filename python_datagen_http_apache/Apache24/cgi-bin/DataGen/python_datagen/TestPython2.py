#!C:\Users\Administrator\AppData\Local\Programs\Python\Python310\python.exe

# ==================================================
# = File:	    TestPython2.py
# = Purpose:	Super-simple HTML response
# ==================================================

# ---
# - Define this procedure's name
# ---
v_current_procedure_name = 'TestPython2.py'


# ---
# - Adding HTML to our AI/ML python code
# ---
print('Content-type: text/html\n')
print('<html>')
print('<title>' + v_current_procedure_name + '</title>')
print('<body bgcolor=#B5CDE1>')
print('<br>')
print('<table border=1 cellspacing=0 cellpadding=8 width=432>')
print(' <tr>')
print('  <td align=center bgcolor=white>')
print('	<b><font size=3>' + v_current_procedure_name + '</font></b>')
print('  </td>')
print(' </tr>')
print('</table>')
print('<br>')
print('<br>')
print('<pre>')


# ---
# - Display a simple greeting
# ---
# print('\n', 10)
print('==================================================')
print('= ' + v_current_procedure_name + ': START')
print('==================================================')
print('\n'*2)


# # Get the current working directory
# cwd = os.getcwd()

# # Print the current working directory
# print('... current working directory: {0}'.format(cwd))
# print('\n')

# ---
# - Display exit message
# ---
print('==================================================')
print('= ' + v_current_procedure_name + ': END')
print('==================================================')
print('\n'*2)



# ---
# - A bunch 'o newbies adding HTML to our AI/ML python code
# ---
print('</pre>')
print('<br>')
print('<br>')
print('</body>')
print('</html>')

