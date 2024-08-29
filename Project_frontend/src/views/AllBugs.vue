<template>
  <div class="all-bugs-container">
    <Navbar />
    <ShowBugs :project_id="projectId" />
  </div>
</template>

<script>
import Navbar from '@/components/Navbar.vue';
import ShowBugs from '@/components/ShowBugs.vue';

export default {
  name: 'AllBugs',
  components: {
    Navbar,
    ShowBugs
  },
  data() {
    return {
      projectId: this.$route.params.project_id
    };
  },
  mounted() {
    console.log('Project ID:', this.projectId);
  }
};
</script>

<style scoped>
.all-bugs-container {
  margin-left: 100px; 
  margin-right: 100px;
  background-color: #f8f8f8;
}
</style>
