<template>
  <div class="single-project-container" @click="handleClick">
    <img class="project-image" src="../assets/Images/Videoicon.png" alt="Project Icon">
    <div class="heading-project">
      <b>{{ truncatedProjectName }}</b>
    </div>
    <div class="description-project">
      <span>{{ project_description }}</span>
    </div>
    <div class="task-done"><span>Task done : </span> <b>{{ closed_bug_count }} / {{ bug_count}}</b></div>
  </div>
</template>

<script>
export default {
  name: 'ProjectDetails',
  props: {
    project_id: {
      type: Number,
      required: true,
    },
    bug_count: {
      type: Number,
      required: true,
    },
    closed_bug_count: {
      type: Number,
      required: true,
    },
    project_name: {
      type: String,
      required: true,
    },
    project_description: {
      type: String,
      required: true,
    },
  },
  computed: {

    truncatedProjectName() {
      return this.project_name.length > 30 
        ? this.project_name.substring(0, 30) + '...' 
        : this.project_name;
    }
  },
  methods: {
    handleClick() {
      this.$emit('project-clicked', this.project_id);
    },
  },
};
</script>

<style scoped>
.single-project-container {
  background-color: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  width: 340px;
  cursor: pointer; 
}

.project-image {
  width: 50px;
  height: auto;
}

.heading-project {
  padding-top: 10px;
  white-space: nowrap;
  overflow: hidden; 
  text-overflow: ellipsis; 
}

.description-project {
  padding-top: 10px;
}

.task-done {
  padding-top: 10px;
}

span {
  color: gray;
}
</style>
