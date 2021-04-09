[![Vue js logo](https://hackernoon.com/hn-images/1*ACR0gj0wbx91V_xgURifWg.png)](https://vuejs.org/)https://vuejs.org/
# Vue.js
### Introduction
| Introduction | Features | Prerequisites |
| ----- | ----- | ----- |
| It a framework (javascript) | Virtual DOM | Knowledge of basic JavaScript
| Developed by google (evan you) | Two way binding | Knowledge of HTML & CSS
| Opensource and First release feb 2014 | Light Weight | Familiarity of ES6+ features and syntax
| Web application development  | MVC framework | Node.js and npm (or yarn) installed globally
| Current release version-3.0.0 | Pure Javascript | Familiarity with REST APIs would be helpful, but we'll go over it.
## Difference between react and vue
| Vue | React |
| ----- | ----- |
| Component loader fast | It's slow when comparing to vue |
| Template based (html, css, js) so, Its easy to understand | ut react.js handlig object so difficult to understand |
### installation
- For prototyping or learning purposes, you can use the latest version with:
 ```sh
            <script src="https://unpkg.com/vue@next"></script>
```
# Vue Walkthrough
We're in a golden era of JavaScript libraries and frameworks. More and more companies are building out full, dynamic web appsThis means things are constantly changing and frameworks are going in and out of vogue, but the core concepts of what we're trying to accomplish remain similar.

## Tutorials
| Name | Tutorials |
| ------ | ------ |
| Vue JS Crash Course 2021 | https://www.youtube.com/watch?v=qZXt1Aom3Cs |
| Vue 3 basics explanation / cheatsheet | https://www.wrappixel.com/vue-cheet-sheet |
| Little Intermediate tutorial | https://dev.to/adnanbabakan/vue-cheat-sheet-1-194a |

## Projects
- Task Tracker [click to redirect the project directory](https://github.com/vigneshbharathi68/learning_port/tree/main/projects/vue/task-tracker)
- Random User Generator [click to redirect the project directory](https://github.com/vigneshbharathi68/learning_port/tree/main/projects/vue/random-user-gen)

## Methods and important notes to learn
[![Vue js flow](https://v3.vuejs.org/images/lifecycle.svg?__WB_REVISION__=f4a90248bd51e5ee6261fd079b5dffb5)](https://v3.vuejs.org/guide/instance.html#lifecycle-diagram)https://v3.vuejs.org/guide/instance.html#lifecycle-diagram

### <Template>
 - ```<form @submit="onSubmit"></form>``` 
 - The below will do the toggle between two class name for border changing to give the reminder green border :
 ```<div @dblclick="$emit('toggle-reminder', task.id)" :class="[task.reminder ? 'reminder': 'reminder_none', 'task']">```
 - By clicking font x it ill delete the task listed:
 ```<i @click="$emit('delete-task', task.id)" class="fas fa-times"></i>```
 - 
```
//Components should import before use
import Header from './components/Header'
import Tasks from './components/Tasks'

//This is the structre we will be using in vue script tag
export default { 
  name: 'App',
  //Imported components should be in this component
  components: {
    Header,
    Tasks
  },
  //This is where we get the data to template
  data(){
    return {
    //Here I am getting data from created() in methods
      tasks: []
    }
  },
  //It's nothing but a function 
  //which we are going to make some function to get the data to template
  methods: {
    deleteTask(id) {
      if (confirm('Are you sure?')){
        this.tasks = this.tasks.filter((task) => task.id 
        !== id)
      }
    },
    toggleReminder(id){
      this.tasks = this.tasks.map((task) => task.id === id ? {... task, reminder: !task.reminder} : task)
    }
  },
  //I have hard coded data and pushed it to data() task array.
  created() {
    this.tasks = [
      {
        id: 1,
        text: 'Doctor Appoinment',
        day: 'March 1st at 2:30 pm',
        reminder: true,
      },
      {
        id: 2,
        text: 'Meeting at school',
        day: 'March 2nd at 10:00 am',
        reminder: true,
      },
      {
        id: 3,
        text: 'Food shopping',
        day: 'March 3rd at 11:00 am',
        reminder: false,
      }
    ]
  }
}
//There is lot more we should learn as of now I have took it while doing task tracker app.
```
## Flow of function and data in vue on submitting form 
- Two files involving in this task ```App.vue``` and ```AddTask.vue```
- In ```AddTask.vue``` we actaully designed the form as per in the below picture
![Form screen shot](https://raw.githubusercontent.com/vigneshbharathi68/learning_port/main/Screenshot_2021-03-26%20Task%20tracker.png)
```
    onSubmit(e) {
        e.preventDefault()
        if (!this.text) { alert("Please add a task") return }
        const newTask = {
            id: Math.floor(Math.random() * 100000),
            text: this.text,
            day: this.day,
            reminder: this.reminder,
        }
        this.$emit('add-task', newTask)
        this.text = '',
        this.day = '',
        this.reminder = false
    }
```
- ```this.$emit('add-task', newTask)``` - this function throws the value as json as we converted the inputs using onSumbmit function some app is vue file is ready to catch it
- ``` <AddTask @add-task="addTask" /> ``` as we use this in ```App.vue``` it actually catches that emit and throw it to some function which we declare in methods shown below:
 ```addTask(task){ this.tasks = [...this.tasks, task] },```
now its time to wrap that input form to the actual task array in ```data()``` section and it will show the value to under the value

## How To Use an API with Vue.js
#### What is Vue.js?
- ue is a progressive framework for building user interfaces. 
- It supports augmented rendering of the HTML markup through a template declaration bound to a data model.
- When the data model is updated, the browser’s HTML DOM also changes accordingly.
- Vuejs is a frontend-end [framework](https://rapidapi.com/blog/api-glossary/api-framework/), and hence it is implemented only in the view layer.

#### Vue.js Components
Each Vue.js project is composed of smaller components. These form the individual building blocks of the complete application and enable abstraction and code reuse.
Here is an example of a Vue.js component.
[![Components picture](https://rapidapi.com/blog/wp-content/uploads/2020/04/Sample-Vue-Component.png)]
A Vue.js Component consists of 3 parts;
- The HTML declaration
- The component definition
- The component style
#### The HTML Declaration

The HTML markup of the component is part of the HTML declaration. Usually, a  ```<template>``` tag defines it and contains one or more child tags.
#### The Component Definition
Every Vue.js component has an Options object. It is a JSON object containing the following properties: 
```MEDCPW``` which stands Acronyms of 
```Methods``` | ```el``` | ```Data``` | ```Computed``` | ```Props``` | ```Watch```
- ```el:``` This property contains the CSS selector of the DOM element, which is attached to the Vue component.
- ```Data:``` The data defines an object that represents the internal data of the Vue component. It can also be a function that returns the data object.
- ```Methods:``` The methods object contains a key-value pair of method names and their function definition
for example,
```
    methods: {
        created() : function (x, y){
            return x*y;
        }
    }
    
```
). These are part of the Vue component’s behavior which the other component can trigger.
- ```computed:``` This contains an object which defines the getter and setter functions for computed properties of the Vue component. Computed properties affect a reactive update on the DOM whenever their value changes.   
- ```props:``` This contains an array or object of properties specific to the Vue.js component, set at the time of invocation. 
- ```watch:``` This object keeps track of changes in the value of any of the properties defined as part of ‘data‘ by setting up functions to watch over them.
