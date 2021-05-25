<template>
  <h1>Bar chartasdfasdf</h1>
  <center>
    <Suspense>
        <template #default>
            <div class="example">
                <apexchart width="50%" height="400" :options="options" :series="series"></apexchart>
            </div>
        </template>
        <template #fallback>
            <div>Loading......</div>
        </template>
    </Suspense>
  </center>
  
</template>

<script>
import VueApexCharts from 'vue3-apexcharts';
import axios from 'axios';

export default {
    name: 'BarChart',
    components: {
        apexchart: VueApexCharts,
    },
    data(){
        return{
            options: {
                chart: {
                    id: 'basic-bar'
                },
            },
            series:[{
                type:'bar',
                name: 'series-1',
                data: [30, 40, 45, 50, 49, 60, 70, 91]
            },
            {
                type:'line',
                name:'series-2',
                data: [30, 40, 45, 50, 49, 60, 70, 91]
            }]
        }
    },
    async created(){
        alert(`While created ${this.series[0].data}`)
        this.cleanUpArray(); //this keyword looking up outside the current objects
        const { data } = await axios.get(`https://api.zealbots.com/api/v1/download/month/2021/03/18/2021/08/02/?Key=8742022d140fd0554e0e9fa27cc13835adb8e342&format=json`);
        console.log("asdfasdfasdfasdf",data.Date)
        
        
    },
    mounted(){
        alert(`While mounted ${this.series[0].data}`)
    },
    unmounted(){
        alert(this.series[0].data)
    },
    methods: {
        cleanUpArray(){
            const barSeries = this.series[0].data;
            const columnSeries = this.series[1].data;
            //Setting array empty here
            barSeries.length = 0; columnSeries.length = 0; 
        }
    }

}
</script>

<style>

</style>