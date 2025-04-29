"""
===============================
🔑 CORE OBJECT-ORIENTED CONCEPTS
===============================

Concept         | Description
----------------|----------------------------------------------------------
Class           | Blueprint for creating objects (instances).
Object          | Instance of a class.
Encapsulation   | Hiding internal data and methods; controlling access.
Abstraction     | Hiding complex implementation details and exposing only essential features.
Inheritance     | A class can inherit behavior and properties from another class.
Polymorphism    | The ability to present the same interface for different data types.
Composition     | A class contains instances of other classes to reuse code.
Association     | General relationship between two classes.
Aggregation     | A special form of association: "has-a" but both can exist independently.
Delegation      | One object relies on another to perform a task.

=====================================
🐍 PYTHON-SPECIFIC OOP KEYWORDS & TOOLS
=====================================

Keyword/Tool          | Purpose
----------------------|-----------------------------------------------------
class                 | Defines a class.
self                  | Refers to the current instance (like this in Java/C++).
__init__()            | Constructor method, called when object is created.
super()               | Calls parent class methods or constructor.
@property                | Creates getter methods that behave like attributes.
@classmethod          | Defines a method bound to the class, not instance.
@staticmethod         | Defines a method that doesn’t access instance or class data.
@abstractmethod       | Declares a method that must be implemented in subclass.
from abc import ABC   | Used to define abstract base classes (like interfaces).
_single_underscore    | Naming convention for protected (internal use only).
__double_underscore   | Name mangling; simulates private access.
__str__ / __repr__    | Magic methods for string representation of objects.
isinstance()          | Checks if an object is an instance of a class.
issubclass()          | Checks if a class is a subclass of another.
hasattr() / getattr() / setattr() | Dynamic attribute access.
del                   | Deletes objects or object attributes.
__del__()             | Destructor method (rarely used).
__dict__              | Holds an object’s writable attributes in a dictionary.
__slots__             | Restricts object to fixed attributes, improves memory usage.

==================================================
⚖️ ACCESS MODIFIERS: PYTHON VS JAVA EQUIVALENTS
==================================================

Modifier    | Python Syntax     | Java Equivalent | Meaning
------------|-------------------|-----------------|-----------------------------------------
Public      | my_var            | public          | Accessible everywhere
Protected   | _my_var (convention) | protected     | Intended for internal or subclass use
Private     | __my_var          | private         | Not accessible directly outside

=================================
🎯 ADDITIONAL OOP CONCEPTS TO KNOW
=================================

Concept              | Python Tool or Explanation
---------------------|------------------------------------------------------
Method Overriding    | Redefining a method in a subclass.
Method Overloading   | Not directly supported in Python (simulate with default arguments or *args).
Duck Typing          | "If it walks like a duck..." — behavior-based typing.
Multiple Inheritance | Supported natively in Python (unlike Java).
Mixins               | Small classes used to add functionality via multiple inheritance.
Operator Overloading | Use magic methods like __add__, __eq__, __lt__, etc.
Inner/Nested Class   | Class defined inside another class.
Metaclass            | Class of a class; controls class creation (using type or __new__).

"""
