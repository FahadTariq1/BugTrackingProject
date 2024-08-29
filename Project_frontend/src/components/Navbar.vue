<template>
  <div class="navbar">
    <div class="logo-image">
      <img src="../assets/Images/buglogo.png" alt="Logo" class="logo" />
      <span style="padding-left: 20px;">Manage Bug</span>
    </div>
    <div class="nav-items">
      <div class="nav-links">
        <div class="nav-item">
          <i class="icon-projects">
            <img src="../assets/Images/project-icon.png" alt="Projects" />
          </i>
          <span>Projects</span>
        </div>
        <div class="nav-item">
          <i class="icon-tasks">
            <img src="../assets/Images/tasks.png" alt="Tasks" />
          </i>
          <span>Tasks</span>
        </div>
        <div class="nav-item">
          <i class="icon-manage">
            <img src="../assets/Images/manage.png" alt="Manage" />
          </i>
          <span>Manage</span>
        </div>
        <div class="nav-item">
          <i class="icon-users">
            <img src="../assets/Images/users.png" alt="Users" />
          </i>
          <span>Users</span>
        </div>
      </div>
      <div class="dev-items">
        <div class="dev-item">
          <i class="icon-dev1">
            <img src="../assets/Images/notification.jpeg" alt="Dev1" />
          </i>
        </div>
        <div class="dev-item">
          <i class="icon-dev2">
            <img src="../assets/Images/messages.png" alt="Dev2" />
          </i>
        </div>
        <div class="dev-item">
          <i class="icon-dev3">
            <img src="../assets/Images/v.png" alt="Dev3" />
          </i>
          <span>{{ userRole }}</span> <!-- Display the user role -->
        </div>
        <div class="dev-item" @click="handleLogout">
          <i class="icon-dev4">
            <img src="../assets/Images/Logout.png" alt="Dev4" />
          </i>
          <span>Logout</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {jwtDecode} from 'jwt-decode';

export default {
  name: 'NavbarMenu',
  data() {
    return {
      userRole: '',
    };
  },
  methods: {
    handleLogout() {
      localStorage.removeItem('authToken');
      this.$router.push('/');
    },
    decodeToken() {
      const token = localStorage.getItem('authToken');
      if (token) {
        const decoded = jwtDecode(token);
        this.userRole = decoded.user_type.charAt(0).toUpperCase() + decoded.user_type.slice(1);
      }
    },
  },
  mounted() {
    this.decodeToken(); // Decode the token when the component mounts
  },
};
</script>

  <style scoped>
  .navbar {
    display: flex;
    justify-content: space-between; /* Space between logo and nav items */
    align-items: center;
    padding: 0 20px;
    height: 60px;
    background-color: #f8f8f8;
  }
  
  .logo-image {
    display: flex;
    align-items: center;
  }
  
  .logo {
    width: 40px;
    height: auto;
  }
  
  .nav-items {
    display: flex;
    flex-grow: 1;
    justify-content: center;
  }
  
  .nav-links {
    display: flex;
    align-items: center;
    flex-grow: 1; /* Allow nav links to take up available space */
    justify-content: center; /* Center the nav items */
  }
  
  .nav-item {
    display: flex;
    align-items: center;
    margin-right: 20px; /* Space between each nav item */
  }
  
  .nav-item i {
    margin-right: 8px;
  }
  
  .nav-item i img {
    width: 16px; /* Adjust icon size */
    height: auto;
  }
  
  .nav-item span {
    font-size: 14px; /* Adjust text size */
    color: #333;
  }
  
  .dev-items {
    display: flex;
    align-items: center;
  }
  
  .dev-item {
    display: flex;
    align-items: center;
    margin-left: 20px; /* Space between each dev item */
  }
  
  .dev-item i {
    margin-right: 8px;
  }
  
  .dev-item i img {
    width: 16px; /* Adjust icon size */
    height: auto;
  }
  
  .dev-item span {
    font-size: 14px; /* Adjust text size */
    color: #333;
  }
  </style>
  