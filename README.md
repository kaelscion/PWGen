# PWGen
A dead-simple script for generating strong passwords for use in password resets, single sign-on, or initial password set

Easy to implement, easy to use, and uses the python standard library's randint module. Simply import the pw_gen module, and 
initialize the PWGen() class, override the pw_len property should use desire (default length of the password is 25 characters).The generate function is set to run on initialization.

Sample Usage

Print 30 character password to console:

```python
from pw_gen import PWGen():

temp_password = PWGen(pw_len=30, print_to_console=True)

FvD(o5GUz##9&V9m^N6W&8FjJ#l(n0
```
PWGen assumes it will be used to generate a value that is NOT printed to the console and defaults to False so override this property at your own risk as the password it generates will be saved to your console history.
