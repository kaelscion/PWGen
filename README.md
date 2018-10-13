# PWGen
A dead-simple script for generating strong passwords for use in password resets, single sign-on, or initial password set for web applications.

Easy to implement, easy to use, and uses the python standard library's randint module so no dependencies. Simply import the pw_gen module, and initialize the PWGen() class, override the pw_len property should use desire a password longer than the default 25 characters. The generate function is set to run on initialization and will create a password that will assemble, at random, a string of characters of the specified length by randomly choosing them one at a time from a list of all 26 en-US alphabet letters, numbers 0-9, and special characters located above the number keys on an en-US keyboard. During generation, the script will also psuedo-randomly decide whether or not to capitalize a letter character.

Sample Usage

Print 30 character password to console:

```python
from pw_gen import PWGen:

temp_password = PWGen(pw_len=30, print_to_console=True)

FvD(o5GUz##9&V9m^N6W&8FjJ#l(n0
```
PWGen assumes it will be used to generate a value that is NOT printed to the console and defaults to False so override this property at your own risk as the password it generates will be saved to your console history.
