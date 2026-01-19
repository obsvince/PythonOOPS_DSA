"""
Class is the blueprint, from which we create objects.



-> Inheritance offers us a mechanism for creating new classes that modify or extend the behavior of existing classes.
-> establishes hierarchy between classes
-> well-designed inheritance defines a "is-a" relationships between classes.


All classes in python inherit from object type. ( object )

-> object is callable because its type implements a __call__ method.

Method Resolution Order ( MRO)
-> checks in ClassName.__dict__ -> then parent classes and so on.
ClassName.__mro__ to get the order.
"""
