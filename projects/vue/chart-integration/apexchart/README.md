# apexchart

## Project setup
```
yarn install
```

### Compiles and hot-reloads for development
```
yarn serve
```

### Compiles and minifies for production
```
yarn build
```

### Lints and fixes files
```
yarn lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

### installed packages in this project

#### Apex chart for visualizing data
```
npm install --save apexcharts
npm install --save vue3-apexcharts
```
**Usage**
```
import VueApexCharts from 'vue-apexcharts'
Vue.use(VueApexCharts)

Vue.component('apexchart', VueApexCharts)
```

**```props``` for chart**
| Prop | Description | Type | Default |
| ----- | ----- | ----- | ----- |
| [type](https://apexcharts.com/docs/options/chart/type) | The chart type which is a mandatory prop to specify | String | ‘line’ |
| [series](https://apexcharts.com/docs/options/series) | The data which you want to display in the chart | Array | 	undefined |
| [width](https://apexcharts.com/docs/options/chart/width) | Width of the chart | String-Number | ‘100%’ |
| [height](https://apexcharts.com/docs/options/chart/height) | Height of the chart | String || Number | ‘auto’ |
| [options](https://apexcharts.com/docs/options) | 	All the optional configuration of the chart goes in this property | Object | {} |
