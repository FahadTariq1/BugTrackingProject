<template>
  <div class="container">
    <div class="show-project-container">
      <div class="heading-of-project">
        <h4>Projects</h4>
        <span class="welcome-message">Hi Devisnext, Welcome to ManageBug</span>
      </div>
      <div class="right-container">
        <div class="search-container">
          <div class="search-input-wrapper">
            <i class="search-icon">🔍</i>
            <input 
              type="text" 
              v-model="searchQuery" 
              placeholder="Search for the project here" 
              class="search-input" 
              @input="fetchAllProjects(currentPage, projectsPerPage, searchQuery)"
            />
          </div>
          <button 
            v-if="userType === 'manager'" 
            class="add-bug-button" 
            @click="showAddProjectModal"
          >
            <span class="plus-sign">+</span> Add New Project
          </button>
          <select class="manage-dropdown">
            <option value="manage">Manage by</option>
          </select>
          <select class="sort-dropdown">
            <option value="name">Sort by</option>
          </select>
          <img src="../assets/Images/buglogo.png" alt="Logo" class="logo-icon" />
        </div>
      </div>
    </div>

    <div class="multiple-projects-container">
      <div :class="['project-grid', projects.length > 6 ? 'grid-row' : 'grid-column']">
        <ProjectDetails
          v-for="(project, index) in paginatedProjects"
          :key="index"
          :project_id="project.id"
          :project_name="project.name"
          :project_description="project.description"
          :bug_count="project.total_bugs"
          :closed_bug_count="project.closed_bugs"
          @project-clicked="handleProjectClick"
        />
      </div>
      <div v-if="totalPages > 1" class="pagination-controls">
        <button @click="prevPage" :disabled="currentPage === 1">Previous</button>
        <span>Page {{ currentPage }} of {{ totalPages }}</span>
        <button @click="nextPage" :disabled="currentPage === totalPages">Next</button>
      </div>
    </div>

    <ModalNewProject 
      :isVisible="isModalVisible" 
      @update:isVisible="isModalVisible = $event" 
      @project-added="fetchAllProjects(currentPage, projectsPerPage, searchQuery)"
    />
  </div>
</template>

<script>
import { jwtDecode } from 'jwt-decode';
import { fetchAllProjects } from '../servicesfile/service';
import ProjectDetails from './ProjectDetails.vue';
import ModalNewProject from './ModalNewProject.vue';

export default {
  name: 'ProjectListing',
  components: {
    ProjectDetails,
    ModalNewProject
  },
  data() {
    return {
      projects: [],
      searchQuery: '',
      currentPage: 1,
      projectsPerPage: 6,
      totalPages: 1,
      isModalVisible: false,
      authToken: '',
      userType: ''
    };
  },
  computed: {
    paginatedProjects() {
      return this.projects;
    },
  },
  methods: {
    async fetchAllProjects(page = 1, pageSize = 6, description_search = '') {
      try {
        const data = await fetchAllProjects(page, pageSize, description_search);
        console.log('Projects data:', data);
        
        this.projects = data.results;
        this.totalPages = Math.ceil(data.count / this.projectsPerPage); 
        this.currentPage = page;
        localStorage.setItem('currentPage', page);
      } catch (error) {
        console.error('Error fetching projects data:', error);
      }
    },
    prevPage() {
      if (this.currentPage > 1) {
        this.fetchAllProjects(this.currentPage - 1, this.projectsPerPage, this.searchQuery);
      }
    },
    nextPage() {
      if (this.currentPage < this.totalPages) {
        this.fetchAllProjects(this.currentPage + 1, this.projectsPerPage, this.searchQuery);
      }
    },
    handleProjectClick(project_id) {
      this.$router.push({ name: 'AllBugs', params: { project_id } });
    },
    showAddProjectModal() {
      this.isModalVisible = true;
    },
    printAuthToken() {
      this.authToken = localStorage.getItem('authToken');
      if (this.authToken) {
        try {
          const decoded = jwtDecode(this.authToken);
          this.userType = decoded.user_type;
          console.log('Decoded Token:', decoded);
        } catch (error) {
          console.error('Error decoding token:', error);
        }
      } else {
        console.log('No auth token found in local storage.');
      }
    }
  },
  beforeMount() {
    this.printAuthToken();
    const storedPage = parseInt(localStorage.getItem('currentPage'), 10);
    if (storedPage) {
      this.currentPage = storedPage;
    }
  },
  mounted() {
    this.fetchAllProjects(this.currentPage, this.projectsPerPage, this.searchQuery);
  }
};
</script>
<style scoped>
.container {
  display: flex;
  flex-direction: column;
  margin: 50px 20px;
}

.show-project-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.right-container {
  display: flex;
  align-items: center;
}

.heading-of-project {
  display: flex;
  flex-direction: column;
}

.heading-of-project h4 {
  margin-bottom: 5px;
}

.welcome-message {
  font-size: 12px;
  color: #808080;
}

.search-container {
  display: flex;
  align-items: center;
  margin-left: 20px; /* Space between the search container and heading */
}

.search-input-wrapper {
  position: relative;
}

.search-icon {
  position: absolute;
  left: 10px;
  top: 50%;
  transform: translateY(-50%);
  font-size: 18px;
  color: #aaa;

}

.search-input {
  width: 300px;
  padding: 10px 15px 10px 35px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 4px;
  background-color: #f0f0f0;
}

.add-bug-button {
  display: flex;
  align-items: center;
  margin-left: 20px;
  padding: 10px 15px;
  font-size: 16px;
  color: #fff;
  background-color: #007bff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.add-bug-button:hover {
  background-color: #0056b3;
}

.plus-sign {
  margin-right: 8px;
  font-weight: bold;
}

.manage-dropdown,
.sort-dropdown {
  margin-left: 20px;
  padding: 10px 15px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 4px;
  background-color: #fff;
  cursor: pointer;
}

.logo-icon {
  margin-left: 10px;
  height: 50px;
}

.multiple-projects-container {
  margin-top: 20px;
}

.project-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
}

.grid-row {
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
}

.grid-column {
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
}

.pagination-controls {
  margin-top: 20px;
  display: flex;
  justify-content: center;
  gap: 10px;
}
.pagination-controls button {
  padding: 5px 10px;
}
</style>