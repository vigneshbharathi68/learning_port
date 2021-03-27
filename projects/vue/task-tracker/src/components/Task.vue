<template>
<div @click="$emit('toggle-reminder', task.id)" :class="[task.reminder ? 
'reminder': 'reminder_none', 'task']">
    <h3>{{ task.text }}
        <i @click="$emit('delete-task', task.id)" class="fas fa-times"></i>
    </h3>
    <p>{{ task.day }}</p>
</div>
</template>

<script>
export default {
    name: 'Task',
    props: {
        task: Object,
    },
}
</script>

<style scoped>
.fas {
    color: red;
}
.task {
    background: #f4f4f4;
    margin: 5px;
    padding: 10px 20px;
    cursor: pointer;
}

.task.reminder{
    background : rgb(133, 245, 133);
    border-left: 5px solid rgb(133, 245, 133);
}
.task.reminder_none{
    border-left: 5px solid #f4f4f4;
}

.task h3 {
    display: flex;
    align-items: center;
    justify-content: space-between;
}
</style>