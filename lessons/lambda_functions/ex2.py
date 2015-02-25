def a_func()
  ...
  if some_conditon:
     ...
     call_some_big_func(arg1, arg2, arg3, arg4...)
  else
     ...
     call_some_big_func(arg1, arg2, arg3, arg4...)

#I replace that with a temp lambda

def a_func()
  ...
  call_big_f = lambda args_that_change: call_some_big_func(arg1, arg2, arg3, args_that_change)
  if some_conditon:
     ...
     call_big_f(argX)
  else
     ...
     call_big_f(argY)