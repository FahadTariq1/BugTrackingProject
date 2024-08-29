<template>
  <div class="modal" v-if="isVisible" @click.self="closeModal">
    <div class="modal-content">
      <span class="close" @click="closeModal">&times;</span>
      <div class="topheadergray">
        <div class="header-content">
          <h2>Add new bug</h2>
          <i class="fas fa-ellipsis-h"></i>
        </div>
      </div>
      <hr>
      <div class="form-container">
        <div class="assign-container">
          <p class="assign-text">Assign to</p>
          <div class="dropdown">
            <select v-model="selectedDeveloper" @change="onDeveloperChange">
              <option value="" disabled>Select Developer</option>
              <option v-for="developer in developers" :key="developer.id" :value="developer.id">
                {{ developer.name }}
              </option>
            </select>
          </div>
        </div>
        <div class="due-date-container">
          <p class="due-date-text">Add Due Date</p>
          <input type="date" v-model="dueDate" />
        </div>
        <div class="title-container">
          <input type="text" v-model="title" placeholder="Add title here" />
        </div>
        <div class="bug-details-container">
          <h4>Bug Details</h4>
          <input type="text" v-model="bugDetails" placeholder="Enter details here" />
        </div>
        <div class="file-upload-container">
          <FileUpload ref="fileupload" mode="basic" name="file" url="/api/upload" accept="image/png, image/gif" :maxFileSize="1000000" @select="onSelect" />
          <div class="file-upload-container2">
            <Button label="Remove" @click="remove" severity="secondary" />
          </div>
        </div>
      </div>
      <div class="submit-container">
        <Button label="Submit" @click="submitForm" />
      </div>
    </div>
  </div>
</template>

<script>
import FileUpload from 'primevue/fileupload';
import Button from 'primevue/button';
import { fetchDevelopers, createBug } from '../servicesfile/service'; 
export default 
{
  name: 'PopUpNewTask',
  props: {
    isVisible: {
      type: Boolean,
      required: true
    }
  },
  components: {
    FileUpload,
    Button
  },
  data() {
    return {
      developers: [],
      selectedDeveloper: null,
      dueDate: '',
      title: '',
      bugDetails: '',
      file: null,
      bug_screenshot_type: '',
      bug_project: '',
      bug_user_id: '',
      bug_type: 'inprogress',
      bug_date: ''
    };
  },
  methods: {
    closeModal() {
      this.$emit('update:isVisible', false);
    },
    async fetchDevelopers() {
      try {
        this.developers = await fetchDevelopers();
        console.log(this.developers);
      } catch (error) {
        console.error('Error fetching developers:', error);
      }
    },
    onDeveloperChange() {
      console.log('Selected developer ID:', this.selectedDeveloper);
    },
    onSelect(event) {
      this.file = event.files[0];
      const mimeType = this.file.type;
      this.bug_screenshot_type = mimeType.split('/')[1];
      console.log('File selected:', this.file.name);
      console.log('File type:', this.bug_screenshot_type);
    },
    remove() {
      this.file = null;
      this.$refs.fileupload.clear();
      console.log("File removed");
    },
    async submitForm() {
      try {
        const formData = new FormData();
        formData.append('title', this.title);
        formData.append('description', this.bugDetails);
        formData.append('screenshot_type', this.bug_screenshot_type);
        formData.append('status', this.bug_type);
        formData.append('assignedproject_id', this.bug_project);
        formData.append('assigneduser_id', this.selectedDeveloper);
        formData.append('due_date', this.dueDate);

        if (this.file) {
          formData.append('image', this.file);
        }

        console.log('Form data to be sent:', Array.from(formData.entries()));
        await createBug(formData);
        console.log('Form submitted successfully');

        this.$emit('form-submitted'); // Emit event on successful form submission
        this.closeModal();
      } catch (error) {
        console.error('Error submitting form:', error);
      }
    }
  },
  watch: {
    isVisible(newVal) {
      if (newVal) {
        this.fetchDevelopers();
      }
    }
  },
  created() {
    let bugProjectIdInt = this.$route.params.project_id;
    this.bug_project = parseInt(bugProjectIdInt, 10);
    console.log('Project ID from URL:', this.bug_project);
  }
};
</script>


  
  <style scoped>
  .submit-container {
    margin-top: 20px;
    display: flex;
    justify-content: center;
  }
  .file-upload-container2 {
    margin-top: 20px;
    display: flex;
    justify-content: center;
    gap: 10px;
  }
  
  .modal {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    overflow: auto;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    align-items: center;
    justify-content: center;
  }
  
  .modal-content {
    background-color: white;
    padding: 20px;
    border-radius: 5px;
    width: 50%;
    max-width: 600px;
    position: relative;
  }
  
  .close {
    border: 2px solid black;
    background-color: black;
    color: white;
    position: absolute;
    top: 10px;
    right: 10px;
    font-size: 30px;
    cursor: pointer;
  }
  
  .topheadergray {
    margin-top: 20px;
    border-radius: 5px 5px 0 0;
    margin-bottom: 10px;
    position: relative;
  }
  
  .header-content {
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  
  .header-content i {
    font-size: 20px;
    color: gray;
  }
  
  hr {
    border: 0;
    height: 1px;
    background: gray;
    width: 100%;
  }
  
  .form-container {
    margin-top: 10px;
  }
  
  .assign-container {
    display: flex;
    align-items: center;
    margin-bottom: 10px;
  }
  
  .assign-text {
    margin-right: 10px;
  }
  
  .dropdown select {
    padding: 5px;
    border-radius: 5px;
    border: 1px solid #ddd;
    font-size: 14px;
    width: 150px;
  }
  
  .due-date-container {
    display: flex;
    align-items: center;
    margin-bottom: 10px;
  }
  
  .due-date-text {
    margin-right: 10px;
  }
  
  input[type="date"] {
    padding: 5px;
    border-radius: 5px;
    border: 1px solid #ddd;
    font-size: 14px;
  }
  
  .title-container {
    display: flex;
    align-items: center;
  }
  
  input[type="text"] {
    padding: 10px;
    border-radius: 5px;
    border: 1px solid #ddd;
    font-size: 16px;
    width: 100%;
    box-sizing: border-box;
  }
  
  .bug-details-container {
    margin-top: 20px;
  }
  
  .bug-details-container h4 {
    margin-bottom: 10px;
    font-size: 18px;
  }
  
  .bug-details-container input[type="text"] {
    padding: 10px;
    border-radius: 5px;
    border: 1px solid #ddd;
    font-size: 16px;
    width: 100%;
    box-sizing: border-box;
  }
  .file-upload-container{
    margin-top: 20px;
  }
  </style>
