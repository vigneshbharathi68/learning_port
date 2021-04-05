<template>
    <div id="App">
        <h1>Fetch data with API</h1>
        <h1>Employee List</h1>
    </div>

</template>
<script>
import axios from 'axios'

export default {
    name:'FetchApiAxios',
    mounted() {
        axios.get('http://dummy.restapiexample.com/api/v1/employees')
        .then((resp)=>{
            console.warn(resp);
        })
    }
}
</script>
<style scoped>

</style>