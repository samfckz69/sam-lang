# Sam Programming Language

Sam is a friendly programming language that wraps Python with more intuitive command names and syntax. It's perfect for beginners and those who prefer more readable command names.

## Installation

```bash
pip install sam-lang
```

## Usage

After installation, you can use Sam in three ways:

1. Run a Sam file:
```bash
sam run example.sam
```

2. Start the interactive shell:
```bash
sam shell
```

3. Use it in Python code:
```python
from sam_lang import SamInterpreter

interpreter = SamInterpreter()
interpreter.run('say "Hello, World!"')
```

## Example Sam Code

```
# This is a Sam program
make greet(name):
    give "Hello, " + name + "!"

when yes:
    say greet("World")

my_array = array([1, 2, 3])
repeat item inside my_array:
    say item
```

## Command Reference

Sam provides intuitive alternatives to Python commands:

- `say` instead of `print`
- `when` instead of `if`
- `repeat` instead of `for`
- `make` instead of `def`
- `thing` instead of `class`
- And many more!

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
