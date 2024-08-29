<template>
  <div class="allbugscontainer">
    <hr>
    <span class="breadcrumb">Projects → </span>
    <span class="breadcrumb">Android UI System</span>
    <div class="header-container">
      <div class="bugs-header">
        <h1>All Bugs Listing</h1>
        <span class="bugsbox">Bugs</span>
      </div>
      <div class="actions-container">
        <div v-if="userType === 'manager' || userType === 'qa'" class="dropdown">
          <button class="dropbtn">Assignees</button>
          <div class="dropdown-content">
            <a href="#">Assignee</a>
            <a href="#">Me</a>
          </div>
        </div>
        <button v-if="userType === 'manager' || userType === 'qa'" class="new-task-button" @click="showModal = true">
          <span class="plus-sign">+</span>
          New Task Bug
        </button>
      </div>
    </div>
    <hr>
    <div class="search-container">
      <div class="search-input-container">
        <i class="fas fa-search search-icon"></i>
        <input 
          type="text" 
          class="search-input" 
          placeholder="Search..." 
          v-model="searchQuery" 
          @input="search"
        >
      </div>
    </div>
    <hr>
    <BugDetails :project_id="project_id" :bugs="filteredBugs" @update-bugs="search" />
    <ModalNewBug :isVisible="showModal" @update:isVisible="showModal = $event" @form-submitted="search" />
  </div>
</template>

<script>
import { jwtDecode } from 'jwt-decode';
import { searchBugs } from '../servicesfile/service';
import ModalNewBug from './ModalNewBug.vue';
import BugDetails from './BugDetails.vue';

export default {
  name: "ShowBugs",
  components: {
    BugDetails,
    ModalNewBug
  },
  props: {
    project_id: {
      type: String,
      required: true
    
    }
  }
  ,
  data() {
    return {
      showModal: false,
      authToken: '',
      userType: '',
      searchQuery: '',
      bugs: []
    };
  },
  computed: {
    filteredBugs() {
      return this.bugs.filter(bug => 
        bug.description.toLowerCase().includes(this.searchQuery.toLowerCase())
      );
    }
  },
  mounted() {
    this.printAuthToken();
    this.search();
    console.log('asndkansjs')
  },
  methods: {
    printAuthToken() {
      this.authToken = localStorage.getItem('authToken');
      if (this.authToken) {
        try {
          const decoded = jwtDecode(this.authToken);
          this.userType = decoded.user_type;
        } catch (error) {
          console.error('Error decoding token:', error);
        }
      }
    },
    async search() {
      try {
        const response = await searchBugs(this.searchQuery, this.project_id);
        this.bugs = response;
      } catch (error) {
        console.error('Error fetching bugs:', error);
      }
    }
  }
};
</script>

<style scoped>
.allbugscontainer {
    margin-top: 20px;
    margin-left: 20px;
    margin-right: 20px;
}

.breadcrumb {
    margin-left: 10px;
    margin-top: 10px;
    font-size: 14px;
    color: lightgray;
    margin-right: 5px; 
}

.header-container {
    display: flex;
    align-items: center; 
    margin-top: 20px; 
    justify-content: space-between; 
}

.bugs-header {
    display: flex;
    align-items: center;
}

.bugsbox {
    font-size: 12px;
    background-color: pink;
    width: 60px; /* Adjust width as needed */
    height: 30px; /* Adjust height as needed */
    color: red;
    display: flex;
    align-items: center; /* Center text vertically */
    justify-content: center; /* Center text horizontally */
    border-radius: 5px; /* Optional: rounded corners */
    margin-left: 10px; /* Space between the "Bugs" label and heading */
}

h1 {
    font-size: 36px; /* Adjust font size as needed */
    font-weight: bold; /* Make the text bold */
    margin: 0; /* Remove default margin */
}

.actions-container {
    display: flex;
    align-items: center;
}

.actions-container i {
    font-size: 20px; /* Adjust icon size as needed */
    width: 40px; /* Fixed width for the icon container */
    height: 40px; /* Fixed height for the icon container */
    margin-left: 15px; /* Space between icons */
    color: gray; /* Icon color */
    border: 1px solid gray; /* Fixed width gray border */
    border-radius: 10%; /* Make the border circular */
    display: flex;
    align-items: center; /* Center icon vertically */
    justify-content: center; /* Center icon horizontally */
    box-sizing: border-box; /* Ensure border and padding are included in the element's total width and height */
}

.vertical-icon {
    display: flex;
    align-items: center; /* Center the vertical dots */
    transform: rotate(90deg); /* Rotate the icon to make it vertical */
}

.new-task-button {
    display: flex;
    align-items: center;
    margin-left: 20px;
    padding: 10px 20px;
    font-size: 14px;
    background-color: #007bff; /* Button background color */
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

.new-task-button .plus-sign {
    font-size: 16px; /* Adjust font size for the "+" sign as needed */
    margin-right: 10px; /* Space between the button text and the "+" sign */
}

.new-task-button:hover {
    background-color: #0056b3; /* Darker button background on hover */
}

hr {
    border: 0; /* Remove default border */
    border-top: 1px solid gray; /* Set a thinner top border for less boldness */
    margin-top: 20px; /* Ensure spacing for hr elements */
}

/* Search Bar Styling */
.search-container {
    margin-top: 20px; /* Spacing from previous elements */
}

.search-input-container {
    position: relative; /* Positioning context for the search icon */
    display: flex;
    align-items: center;
}

.search-icon {
    position: absolute;
    left: 10px; /* Space between the icon and the left edge of the input field */
    font-size: 16px; /* Adjust icon size as needed */
    color: gray; /* Icon color */
}

.search-input {
    padding: 10px 10px 10px 35px; /* Add padding on the left to accommodate the icon */
    font-size: 14px;
    border: 1px solid #ccc; /* Light gray border for the input field */
    border-radius: 5px; /* Optional: rounded corners */
    box-sizing: border-box; /* Include padding in element's total width and height */
    width: 25%; /* Make the input field take the available width */
}
.dropdown {
    position: relative; /* Ensure dropdown content is positioned relative to the button */
}

.dropbtn {
    background-color: #007bff; /* Button background color */
    color: white;
    border: none;
    padding: 10px 20px;
    font-size: 14px;
    border-radius: 5px;
    cursor: pointer;
}

.dropdown-content {
    display: none; /* Hide dropdown content by default */
    position: absolute; /* Position dropdown content relative to the dropdown button */
    top: 100%; /* Position directly below the button */
    left: 0;
    background-color: white; /* Background color for dropdown items */
    min-width: 160px; /* Minimum width of the dropdown */
    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2); /* Optional: shadow for dropdown */
    z-index: 1000; /* Ensure dropdown is on top of other content */
    padding: 0; /* Remove default padding to avoid shifting */
    margin: 0; /* Remove default margin */
}

.dropdown-content a {
    color: black; 
    padding: 12px 16px; 
    text-decoration: none;
    display: block; 
    box-sizing: border-box; 
}

.dropdown-content a:hover {
    background-color: #f1f1f1;
}

.dropdown:hover .dropdown-content {
    display: block;
}

.dropdown:hover .dropbtn {
    background-color: #0056b3;
}

</style>