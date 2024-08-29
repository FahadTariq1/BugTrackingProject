<template>
  <LeftBackgroundImage/>
  <SignInDetails :userType="userType"/>

</template>

<script>
import LeftBackgroundImage from '@/components/LeftBackgroundImage.vue';
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import SignInDetails from '@/components/SignInDetails.vue';
export default 
{
  name: 'SignIn',
  components:{
    LeftBackgroundImage,
    SignInDetails
  },
  setup() {
  const route = useRoute();
  const userType = ref('');  

  onMounted(() => {setTimeout(() => {
    userType.value = route.query.userType || 'No userType provided';
}, 0);
});

  return {
    userType,
  };
},
  
};
</script>

<style>
</style>
