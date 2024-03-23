Design problems occur more frequently than algorithmic ones.

Are you the kind of person that’s well aware that the actual act of coding itself is easy.

What’s hard is producing software that’s:
• Simple
• Clean
• Satisfies the needs of its users today
• Can be changed to satisfy the needs of its users tomorrow
That’s hard. That’s also the primary goal of software.

Goal #1 of software: Satisfy the users’ needs.
Goal #2 of software: Consistently accomplish Goal #1, with as minimal development effort
as possible.

System quality attributes (SQAs):
Metrics like:
speed, reliability, availability, and scalability.

What is architecture:
Architecture is about identifying the software system quality attributes that are most related to the success or failure of a system. e.g mvc, DDD, micro-service arch

What is software design:
Software architecture & design is the structure of a system, the elements it contains, and the relationship between those elements.


The point I’m trying to make is that you can’t be a high-level designer (software architect),without knowledge of the low-level details (writing clean code, using a programming paradigm effectively, adhering to design principles). The devil is in the details.

Step 1:
Clean Code ('image on the side)
My definitive explanation of clean code consists of:
• 􀀀 Your developer mindset (empathy, craftsmanship, growth mindset, design thinking)
• 􀀀 Your coding conventions (naming things, refactoring, testing, etc)
• 􀀀􀀀 Your skills & knowledge (of patterns, principles, and how to avoid code smells and
anti-patterns)
So much of what makes

One requirement is that you should care enough to learn about the business you’re writing code within. If we don’t care about the domain enough to understand it, then how can we be sure we’re using good names to represent domain concepts?

We often think that code is solely written to serve the needs of the end user, but we forget the other people we write code for: us, our teammates, and the project’s future maintainers.
Having an understanding of the principles of design and how human psychology decides
what is good and bad design.

Step 2: Programming paradigms ('image in the side')
Object-Oriented Programming is the tool best suited for defining how we cross architectural
boundaries with polymorphism and plugins
• Functional programming is the tool we use to push data to the edges of our applications
and elegantly handle program flow
• and Structured programming is the tool we use to compose algorithms.

Step 3: Object Oriented Programming and Domain Modeling: ('image in the side')
Not only does Object-Oriented programming enable us to create a plugin architecture and build flexibility into our projects, OOP comes with the 4 principles of OOP (encapsulation, inheritance, polymorphism, and abstraction) that helps us create rich domain models

Step 4: Design Principles:
When should I use extends and inheritance?
When should I use an interface?
When should I use an abstract class?

Design Principles are well-established and battle-tested object-oriented best practices that we can use as guardrails.

Examples of common design principles we will familiarize ourselves with are:
• Composition over inheritance
• Encapsulate what varies
• Program against abstractions, not concretions
• The Hollywood principle: “Don’t call us, we’ll call you.”
• The SOLID principles, especially the Single responsibility principle
• DRY (Do Not Repeat Yourself)
• YAGNI (You Aren’t Gonna Need It)

Step 5: Design patterns
There are 3 categories of design patterns: creational, structural, and behavioral.
Creational Design Patterns
Creational patterns are patterns that control how objects are created.

Examples of creational patterns include:
• The Singleton pattern* for ensuring only a single instance of a class can exist
• The Abstract Factory pattern, for creating an instance of several families of classes
• The Prototype pattern, for starting out with an instance that is cloned from an existing one

Structural Design Patterns
Structural patterns are patterns that simplify how we define relationships between components.
Examples of structural design patterns include:
• The Adapter pattern, for creating an interface to enable classes that generally can’t
work together, to work together.
• The Bridge pattern, for splitting a class that should actually be one or more, into a set
of classes that belong to a hierarchy, enabling the implementations to be developed
independently of each other.
• The Decorator pattern, for adding responsibilities to objects dynamically.

Behavioral Design Patterns
Behavioral patterns are common patterns for facilitating elegant communication between
objects.
Examples of behavioral patterns are:
• The Template pattern, for deferring the exact steps of an algorithm to a subclass.
• The Mediator pattern, for defining the exact communication channels allowed between
classes.
• The Observer pattern, for enabling classes to subscribe to something of interest and
to be notified when a change occurred.

Step 6 Architectural Principles:
• Component design principles: The Stable Abstraction Principle), The Stable Dependency
Principle, and The Acyclic Dependency Principle, for how to organize components,
their dependencies, when to couple them, and the implications of accidentally
creating dependency cycles and relying on unstable components.
• Policy vs. Detail, for understanding how to separate the rules of your application
from the implementation details.
• Boundaries, and how to identify the subdomains that the features of your application belongs within.

Step 7: Architectural Styles:
Architectural styles are groupings of all the different types of architectures that you can employ. Each of these styles has uniquely positive effects on maintaining the health of one or more SQAs.

Here are a few examples:
• Component-based architectures emphasize separation of concerns between the individual
components within a system. Think Google for a sec. Consider how many applications
they have within their enterprise (Google Docs, Google Drive, Google Maps,
etc). For platforms with lots of functionality, component-based architectures divide
the concerns into loosely coupled independent components. This is a horizontal separation.
• Monolithic means that the application is combined into a single platform or program,
deployed all together. Note: You can have a component-based AND monolithic architecture if
you separate your applications properly, yet deploy it all as one piece.
• Layered architectures separate the concerns by cutting software into infrastructure,
application, and domain layers. This is a vertical separation.

Step 8: Architectural Patterns:

Step 9: Enterprise patterns

