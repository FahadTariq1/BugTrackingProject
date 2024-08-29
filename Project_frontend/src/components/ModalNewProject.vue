<template>
  <div class="modal" v-if="isVisible" @click.self="closeModal">
    <div class="modal-content">
      <span class="close" @click="closeModal">&times;</span>
      <h2>Add New Project</h2>
      <form @submit.prevent="submitForm">
        <div class="form-group">
          <label for="project-name">Project Name</label>
          <input 
            type="text" 
            id="project-name" 
            v-model="projectName" 
            placeholder="Enter project name" 
            required
          />
        </div>
        <div class="form-group">
          <label for="project-description">Description</label>
          <textarea 
            id="project-description" 
            v-model="projectDescription" 
            placeholder="Enter project description" 
            required
          ></textarea>
        </div>
        <div class="file-upload-container">
          <FileUpload ref="fileupload" mode="basic" name="file" url="/api/upload" accept="image/png, image/gif" :maxFileSize="1000000"/>
        </div>
        <div class="button-container">
          <Button label="Remove" @click="remove" severity="secondary" />
          <button type="submit">Submit</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import { createProject } from '../servicesfile/service'; 
import FileUpload from 'primevue/fileupload';
import Button from 'primevue/button';
import { jwtDecode } from 'jwt-decode'; // Correct import for jwtDecode

export default {
  name: 'PopUpNewProject',
  components: {
    FileUpload,
    Button
  },
  props: {
    isVisible: {
      type: Boolean,
      required: true
    }
  },
  data() {
    return {
      projectName: '',
      projectDescription: ''
    };
  },
  methods: {
    closeModal() {
      this.$emit('update:isVisible', false);
    },
    async submitForm() {
      const formData = new FormData();
      formData.append('name', this.projectName);
      formData.append('description', this.projectDescription);

      if (this.$refs.fileupload.files.length > 0) {
        formData.append('image', this.$refs.fileupload.files[0]);
      }

      const authToken = localStorage.getItem('authToken');
      let userId = null;

      if (authToken) {
        try {
          const decodedToken = jwtDecode(authToken);
          userId = decodedToken.user_id;
          formData.append('manager_id', userId);
        } catch (error) {
          console.error('Error decoding token:', error);
        }
      }

      try {
        console.log('Form data:', Array.from(formData.entries()));
        const response = await createProject(formData);
        console.log('Project added successfully:', response);
        this.closeModal();
        this.$emit('project-added');
      } catch (error) {
        console.error('Error adding project:', error);
      }
    },
    remove() {
      this.file = null; // Reset the file property
      this.$refs.fileupload.clear(); // Clear the FileUpload input
      console.log("File removed");
    },
  }
};
</script>

<style scoped>
.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
}

.modal-content {
  background-color: white;
  padding: 20px;
  border-radius: 5px;
  width: 400px;
  max-width: 90%;
  position: relative;
}

.close {
  position: absolute;
  top: 10px;
  right: 10px;
  font-size: 20px;
  cursor: pointer;
}

h2 {
  margin: 0;
  font-size: 18px;
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  margin-bottom: 5px;
}

input, textarea {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

button {
  padding: 10px 20px;
  font-size: 16px;
  color: #fff;
  background-color: #007bff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}

.file-upload-container {
  margin-bottom: 15px;
}

.button-container 
{
  display: flex;
  justify-content: flex-end;
  gap: 10px;
}

.button-container button 
{
  margin-left: 10px;
}
</style>
