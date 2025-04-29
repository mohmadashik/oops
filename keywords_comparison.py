"""
======================
🐍 PYTHON vs JAVA vs C++: OOP FEATURES COMPARISON
======================

Concept/Feature       | Python                      | Java                      | C++
----------------------|-----------------------------|---------------------------|-----------------------------
Class                 | class                       | class                     | class
Object                | Instance of a class         | Instance of a class       | Instance of a class
Constructor           | __init__()                  | Constructor method        | Constructor method
Destructor            | __del__()                   | Finalize method           | Destructor (~ClassName())
Inheritance           | Inherits with class name    | Inherits using 'extends'  | Inherits using ':'
Method Overriding     | Redefine method in subclass | Redefine method in subclass | Redefine method in subclass
Method Overloading    | Not directly supported      | Supported (same name, different parameters) | Supported (same name, different parameters)
Polymorphism          | Achieved with inheritance   | Achieved with inheritance | Achieved with inheritance
Access Modifiers     | _ (protected), __ (private) | public, protected, private | public, protected, private
Abstract Class        | abc, @abstractmethod        | abstract class, interface | pure virtual class (abstract)
Interface             | abc (abstract base class)   | interface                 | Not available (use abstract classes)
Static Methods        | @staticmethod                | static                    | static
Class Method          | @classmethod                 | static                    | static
Private Methods       | __ (name mangling)          | private                   | private
Protected Methods    | _ (convention)              | protected                 | protected
Friendship (Friend)   | Not available               | Not available             | friend
Multiple Inheritance  | Supported                   | Supported, but via interfaces | Supported (with potential for diamond problem)
Composition           | Achieved with instance of other class | Achieved with instance of other class | Achieved with instance of other class
Delegation            | Not explicitly available    | Not explicitly available  | Achieved by using objects as class members
Operator Overloading  | Supported via magic methods (e.g., __add__) | Supported                 | Supported
Encapsulation         | Public, _protected, __private | public, private, protected | public, private, protected
Abstract Methods      | @abstractmethod in abc      | abstract methods in abstract classes or interfaces | Pure virtual functions in abstract classes
Property (getter/setter) | @property, @setter/getter | get/set methods            | get/set methods
Type Checking         | isinstance(), issubclass()  | instanceof, ClassName.class | typeid, dynamic_cast
Garbage Collection    | Automatic (via reference counting and GC) | Automatic (via garbage collector) | Manual (using delete or smart pointers)
"""

