<template>
    <div>
      <PersonCard v-for="person in persons" :key="person.id" :person="person" /> 
    </div>
  </template>
  
  <script>
  import PersonCard from '../components/PersonCard.vue'; // Import from components/
  
  export default {
    components: {
      PersonCard 
    },
    // ... other logic ...
  };
  </script>