/*
===============================
🔑 CORE OBJECT-ORIENTED CONCEPTS
===============================

Concept         | Description
----------------|----------------------------------------------------------
Class           | Blueprint for creating objects (instances).
Object          | Instance of a class.
Encapsulation   | Bundling data and methods that operate on that data.
Abstraction     | Hiding complex implementation and exposing essential details.
Inheritance     | One class (child) derives properties/methods from another (parent).
Polymorphism    | Functions/objects behave differently based on context.
Composition     | A class contains objects of other classes (has-a relationship).
Association     | General relationship between two independent classes.
Aggregation     | A special form of association: whole and part can exist independently.
Delegation      | One object delegates responsibility to another helper object.

=========================================
🔧 C++-SPECIFIC OOP FEATURES & KEYWORDS
=========================================

Keyword/Feature       | Purpose
----------------------|----------------------------------------------------------
class                 | Defines a class (members default to private).
struct                | Similar to class, but members default to public.
public / private / protected | Access specifiers controlling member access.
constructor           | Special method for object initialization.
destructor            | Special method called on object destruction (~ClassName()).
this                  | Pointer to the current object.
virtual               | Allows method to be overridden in derived class.
override              | (C++11+) Indicates a method overrides a base class method.
final                 | (C++11+) Prevents method or class from being overridden/inherited.
friend                | Grants another class/function access to private/protected members.
explicit              | Prevents implicit constructor conversions.
mutable               | Allows member to be modified even if object is const.
static                | Shared among all instances; belongs to the class.
const                 | Prevents modification of data or function.
new / delete          | Dynamic memory management.
operator overloading  | Redefines built-in operator behavior (e.g. operator+).
template              | Enables generic programming (classes and functions).
namespace             | Avoids naming conflicts.

==================================
⚖️ ACCESS MODIFIERS IN C++
==================================

Access Modifier | Description
----------------|----------------------------------------------------------
public           | Accessible from anywhere the object is visible.
protected        | Accessible in the class and its derived classes.
private          | Accessible only within the class or friends.

=================================
🎯 ADDITIONAL OOP CONCEPTS IN C++
=================================

Concept              | C++ Feature or Explanation
---------------------|------------------------------------------------------
Method Overriding    | Done via virtual methods and overriding in derived class.
Method Overloading   | Supported natively (same method name, different signatures).
Polymorphism         | Achieved using virtual functions and inheritance.
Multiple Inheritance | Fully supported, but can lead to diamond problem (solved via virtual inheritance).
Templates            | Enables writing generic and reusable code.
STL Classes          | C++ Standard Template Library provides ready-to-use generic containers.
RTTI                 | Run-Time Type Information (typeid, dynamic_cast).
Operator Overloading | Supported for most operators.
Nested Class         | Class defined inside another class.
Friend Class/Function| Can access private/protected members of the class.
*/

