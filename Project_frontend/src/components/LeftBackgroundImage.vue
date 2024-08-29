<template>
  <div class="left-side">
    <img src="../assets/Images/Frontend.avif" alt="">
  </div>
</template>

<script>
export default {
  name: 'LeftBackgroundImage',
};
</script>

<style scoped>
.left-side {
  flex: 0 0 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  height: 100vh;
  width: 40vw; 
}

.left-side img {
  width: 100%;
  height: 100%;
  object-fit: cover; 
}
</style>
