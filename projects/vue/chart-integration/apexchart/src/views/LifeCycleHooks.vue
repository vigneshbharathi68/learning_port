<template>
  <h1>Life cycle hooks</h1>
  <p>Here I am actually going to show the life cyle hooks example</p>
</template>

<script>
export default {
    name:"LifeCycleHooks",
    props: {
    },
    methods: {

    },
    computed: {

    },
    created(){
        console.log("created")
    },
    mounted(){
        console.log("mounted")
    },
    unmounted(){
        console.log("Unmounted")
    },
    
}
</script>

<style>

</style>