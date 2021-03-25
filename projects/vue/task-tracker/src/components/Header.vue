<template>
    <header>
        <h1>{{ title }}</h1>
        <Button text="Add Task" color="green" />
        
    </header>
</template>

<script>
import Button from './Button'

export default {
    name: 'Header',
    props: {
        title: {
            type: String,
            default: 'Task Tracker',
        }
    },
    components: { 
      Button
    },
}
</script>

<style scoped>
header {
    display: flex;
    justify-content: left;
    /* align-items: left; */
    margin-bottom: 20px;
}
</style>
