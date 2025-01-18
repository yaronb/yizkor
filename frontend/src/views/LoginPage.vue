<template>
    <div>
      <h1>Login</h1>
      <form @submit.prevent="login"> 
        <input type="text" v-model="username" placeholder="Username">
        <input type="password" v-model="password" placeholder="Password">
        <button type="submit">Login</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        username: '',
        password: ''
      };
    },
    methods: {
      login() {
        // TODO: Implement login logic (send credentials to backend)
      }
    }
  };
  </script>