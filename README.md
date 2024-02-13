# ICS3U Your First Fork
This is a summary of the topics discussed thus far.

## Variables
A variable is something that stores information in a program so that it can be used later.

### Variable Types
We've looked at several different types of variables in Python:

| Type      | Short Form | Definition                                             | Examples            |
|-----------|------------|--------------------------------------------------------|---------------------|
| String    | str        | A sequence of characters, enclosed within quotes       | "hello", 'world'    |
| Integer   | int        | A whole number without a decimal point                 | 5, 100, -42         |
| Float     | float      | A number with a decimal point                          | 3.14, -0.5, 2.0     |

### Variable Assignment Statement
A variable is created and updated using an **assignment statement**:

![diagram01](images/diagram01.png)

### Determining Type
You can use the `type` function in Python to determine a variable's type. For example:

#### Code
```python
greeting = "Hello, world!"
pritn(type(greeting))
```

#### Output
```
<class 'str'>
```

In addition, it is good programming practice to be strict about maintaing consistency with your variables and data types. Try to avoid using the same variable for strings and integers at different points in your program.

## Best Practices
It's important to follow good variable naming conventions and style guidelines (outlined in a document called the [Python Enhancement Proposal 8](https://pep8.org/), or PEP8). This helps us write clean, readable, and maintainable code. 

Here are some good beginner variable rules based on PEP8:

### Use descriptive names
Choose variable names that are meaningful and describe their purpose or content. Avoid single-letter variable names except for loop indices or other very short-lived variables.

#### Good
```python
name = "John"
num_students = 10
```

#### Bad
```python
n = "John"
x = 10
```

### Use lowercase letters with underscores for multi-word names (i.e. snake_case)
Use underscores (_) to separate words in variable names for better readability.
#### Good
```python
max_speed = 100
user_name = "example"
```

#### Bad
```python
MaxSpeed = 100
userName = "example"
```

### Avoid using reserved words
Do not use special or reserved words as variable names.

#### Bad - 'class' is a reserved word
```python
class = "example"
```

### Be consistent
Maintain consistent naming conventions throughout your codebase.

#### Good
```python
max_speed = 100
min_speed = 50
```

#### Bad
```python
maxSpeed = 100
min_speed = 50
```

### Use meaningful prefixes for variable names in specific contexts
Use prefixes such as "is_" for Boolean variables, "num_" for counts or number variables, and "str_" for string variables.

#### Good
```python
is_valid = True
num_students = 10
str_name = "John"
```

#### Bad
```
valid = True
students = 10
name = "John"
```

### Avoid magic numbers
Assign numbers to variables with descriptive names instead of using them directly in your code.

#### Good
```python
max_speed = 100
acceleration = 9.8
```

#### Bad
```
distance = time * 9.8
```
