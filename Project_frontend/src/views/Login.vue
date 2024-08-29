<template>
    <LeftBackgroundImage/>
    <LoginDetails/>
 
</template>
  
  <script>
import LeftBackgroundImage from '@/components/LeftBackgroundImage.vue';
import LoginDetails from '@/components/LoginDetails.vue';

  export default 
  {
    name: 'LogIn',
    components:{
      LeftBackgroundImage,
      LoginDetails
    }
  }
  </script>
  
  <style>
  </style>
  