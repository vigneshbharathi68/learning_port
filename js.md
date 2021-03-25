# Javascript

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
