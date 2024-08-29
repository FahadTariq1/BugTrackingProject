<template>
    <div class="all-projects-container">
      <NavbarMenu />
      <ProjectListing/>
    </div>
  </template>
  
  <script>
import ProjectListing from '@/components/ProjectListing.vue';
import NavbarMenu from '../components/Navbar.vue'
  export default 
  {
    name: 'AllProjects',
    components: 
    {
      NavbarMenu,
      ProjectListing
    }
  }
  </script>
  
  <style scoped>
  .all-projects-container 
  {
    margin-left: 100px;
    margin-right: 100px;
    margin-top: 50px;
    background-color: #f8f8f8;
    min-height: 700px
  }
  </style>
  