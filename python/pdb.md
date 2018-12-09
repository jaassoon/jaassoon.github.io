#### display contxt sources by l (list)
```shell
ipdb> l
```
b 02_logistic_regression.py:44,start>54500  to add condition break point;
#### add break point
```shell
ipdb> b /usr/lib64/python3.6/site-packages/keras/engine/training.py:142
```
continue c
#### step into
```shell
ipdb> s
```
#### exit debug mode
```shell
ipdb> q
```
return r  
quit q  >maybe restart debug  
#### forward to next line
```shell
ipdb> n
```
#### dump var by print
```shell
ipdb> p array.size()
ipdb> p len(tuple)
```
pprint pp  
!var_name to change var value  
r >continue until return, use after setp into
help  
w where >Print a stack trace, 
u up
d down >Move the current frame count (default one) levels down in the stack trace (to a newer frame).
locals()
tbreak >Temporary breakpoint,
cl(ear) >clear breakpoint
disable >Disable the breakpoints 
enable
ignore
condition
unt(il) [lineno]> continue until lineno
#### jump to specified line
```shell
ipdb> j 142
```
whatis Print the type of the expression.
source >show src
display [expression]
undisplay
interact
alias
unalias
restart
#### continue to run
```shell
ipdb> run
```

python3.5 -m pdb myscript.py
#### enter key
If you press ENTER without entering anything, pdb will re-execute the last command that you gave it.  

break fib.py:4
break fib.main >when main() executed
break fib.py:4, high > 10  >condition break point
