# Variable Scope
def test_scope():
  local_var = "I am Local"
  print(local_var)

test_scope()

global_var = "I am Global"

def modify_global():
  global global_var
  global_var = "Modified Global"

modify_global()
print(global_var)
