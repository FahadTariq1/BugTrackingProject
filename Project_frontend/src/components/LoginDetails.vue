<template>
  <div class="RightSide">
    <div class="main text">
      <div class="Login">
        <b><h2>Login</h2></b>
        <label>Please enter your login details</label>
      </div>
      <div class="form">
        <form @submit.prevent="handleSubmit">
          <div v-if="errorMessage" class="error-message">{{ errorMessage }}</div>
          <div class="form-group">
            <div class="input-container">
              <i class="fas fa-envelope icon"></i>
              <input type="email" id="email" v-model="form.email" placeholder="Enter your email" required />
            </div>
          </div>
          <div class="form-group">
            <div class="input-container">
              <i class="fas fa-lock icon"></i>
              <input type="password" id="password" v-model="form.password" placeholder="Enter your password" required />
            </div>
          </div>
          <button type="submit"><b>Login</b> <i class="fas fa-arrow-right"></i></button>
          <hr class="dotted-line" />
        </form>
      </div>
      <div class="Noaccount"></div>
      <label>Don't have an account</label> <router-link to="/" class="signup-link"> Create account</router-link>
    </div>
  </div>
</template>

<script>
import { loginUser } from '../servicesfile/loginfile';

export default {
  name: 'RightSideLogin',
  data() {
    return {
      form: {
        email: '',
        password: ''
      },
      errorMessage: ''
    };
  },
  methods: {
    async handleSubmit() {
      this.errorMessage = ''; // Clear previous error message
      try {
        const userData = {
          email: this.form.email,
          password: this.form.password
        };
        const response = await loginUser(userData);
        const token = response.token;
        localStorage.setItem('authToken', token);
        console.log('Login successful:', response);
        this.$router.push('/allprojects'); // Redirect to AllProjects.vue
      } catch (error) {
        if (error.response && error.response.status === 400) {
          this.errorMessage = 'Invalid email or password. Please try again.';
        } else {
          this.errorMessage = 'An error occurred during login. Please try again later.';
        }
        console.error('Login error:', error.response ? error.response.data : error.message);
      }
    }
  }
}
</script>
  <style scoped>
  .error-message {
    color: red;
    margin-bottom: 15px;
    font-weight: bold;
  }
.RightSide {
  position: absolute;
  right: 0;
  top: 0;
  bottom: 0;
  width: 50%; /* Cover 50% of the viewport width */
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 20px;
  box-sizing: border-box;
  background-color: #f9f9f9; 
}

.main {
  width: 100%;
}

.Login {
  margin-bottom: 20px;
}

.form {
  width: 100%;
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  margin-bottom: 5px;
}

.input-container {
  position: relative;
  display: flex;
  align-items: center;
  width: 80%; /* Adjust width as needed */
  max-width: 500px; /* Optional: Set a maximum width */
}

input {
  width: 100%;
  padding: 10px; /* Increase padding for height */
  padding-left: 40px; /* Space for the icon */
  font-size: 16px; /* Increase font size if needed */
  box-sizing: border-box;
  border-radius: 4px; /* Optional: Add rounded corners */
}

.icon {
  position: absolute;
  left: 10px;
  top: 50%;
  transform: translateY(-50%);
  color: #aaa; /* Adjust color as needed */
}

button {
  padding: 10px 15px;
  border: none;
  background-color: #007BFF;
  color: white;
  cursor: pointer;
  border-radius: 4px; /* Optional: Add rounded corners */
  display: flex;
  align-items: center;
}

button i {
  margin-left: 10px; /* Add space between text and arrow icon */
}

button:hover {
  background-color: #0056b3;
}
.dotted-line {
    width: 80%; /* Same width as the input fields */
    max-width: 500px; /* Match the maximum width of the input fields */
    border: none;
    border-top: 1px dotted #ccc; /* Dotted line style */
    margin: 20px 0; /* Space above and below the line */
  }
  .signup-link {
    color: #007BFF;
    text-decoration: none;
  }
  
  .signup-link:hover {
    text-decoration: underline;
  }

</style>