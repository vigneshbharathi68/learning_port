# Javascript

## Tutorials

| name | link |
| ----- | ----- |
| Full basics | [link here](https://javascript.info/) |
| Cheat Sheet with worked out | [link here](https://htmlcheatsheet.com/) |

## Cheatsheets
| name | link/pdf here |
|-----|-----|
| Eloquent JS for learning basic | [link here](https://eloquentjavascript.net/) |

## JavaScript Object Methods
### The this Keyword
- In a function definition, this refers to the "owner" of the function.
- In the example above, this is the person object that "owns" the fullName function.
- In other words, this.firstName means the firstName property of this object.
- Read more about the this keyword at JS this Keyword.
```sh
    var person = {
        firstName: "John",
        lastName : "Doe",
        id       : 5566,
        fullName : function() {
          return this.firstName + " " + this.lastName;
        }
    };
```
Accesing object using the below code 
```
    var name = person.fullName();
    output as follows :
                John Doe
```
### JavaScript functions
- A JavaScript function can also be defined using an expression.
- A function expression can be stored in a variable:
```
    var x = function (a, b) {return a * b};
    var z = x(4, 3); 
```
From the above code You will get ```z``` value as ```12```
### Arrow function
- Arrow functions allows a short syntax for writing function expressions.
- You don't need the function keyword, the return keyword, and the curly brackets.
```sh
    // ES5
    var x = function(x, y) { return x * y; }
    // ES6
    const x = (x, y) => x * y;
```
### Function parameters
