<template>
  <div class="RightSide">
    <div class="main text">
      <div class="Signin">
        <b><h2>Sign Up</h2></b>
        <label>Please fill in the information below</label>
      </div>
      <div class="form">
        <form @submit.prevent="handleSubmit">
          <div v-if="successMessage" class="success-message">{{ successMessage }}</div>
          <div v-if="errorMessage" class="error-message">{{ errorMessage }}</div>
          <div class="form-group">
            <div class="input-container">
              <i class="fas fa-user icon"></i>
              <input type="text" id="name" v-model="form.name" placeholder="Enter your name" />
            </div>
          </div>
          <div class="form-group">
            <div class="input-container">
              <i class="fas fa-mobile-alt icon"></i>
              <input type="tel" id="mobile" v-model="form.mobile" placeholder="Enter your mobile number" />
            </div>
          </div>
          <div class="form-group">
            <div class="input-container">
              <i class="fas fa-envelope icon"></i>
              <input type="email" id="email" v-model="form.email" placeholder="Enter your email" />
            </div>
          </div>
          <div class="form-group">
            <div class="input-container">
              <i class="fas fa-lock icon"></i>
              <input type="password" id="password" v-model="form.password" placeholder="Enter your password" />
            </div>
          </div>
          <button type="submit"><b>Sign Up</b> <i class="fas fa-arrow-right"></i></button>
          <hr class="dotted-line" />
        </form>
      </div>
      <div class="AlreadyAccount"></div>
      <label>Already have an account?</label> <router-link to="/Login" class="login-link"> Log in to your account</router-link>
    </div>
  </div>
</template>

<script>
import { signupUser }  from '../servicesfile/loginfile';

export default {
  name: 'RightSideSignup',
  props: {
    userType: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      form: {
        name: '',
        mobile: '',
        email: '',
        password: '',
      },
      successMessage: '',
      errorMessage: '',
    };
  },
  methods: {
    async handleSubmit() {
      this.successMessage = '';
      this.errorMessage = '';

      if (!this.form.name || !this.form.mobile || !this.form.email || !this.form.password) {
        this.errorMessage = 'Please fill in all required fields.';
        return;
      }

      try {
        const userData = {
          name: this.form.name,
          email: this.form.email,
          password: this.form.password,
          type: this.userType,
        };
        const response = await signupUser(userData);
        this.successMessage = 'You have successfully signed up!';
        console.log('Response:', response);
      } 
      catch (error) 
      {
        if (error.response) 
        {
          if (error.response.status === 400) {
            this.errorMessage = 'User with this email exists';
          } else 
          {
            this.errorMessage = 'Error: ' + (error.response.data.user_email ? error.response.data.user_email[0] : 'An error occurred');
          }
          console.error('Error response data:', error.response.data);
          console.error('Error response status:', error.response.status);
          console.error('Error response headers:', error.response.headers);
        } else if (error.request) 
        {
          console.error('Error request data:', error.request);
          this.errorMessage = 'Error: No response received from server';
        } else 
        {
          console.error('Error message:', error.message);
          this.errorMessage = 'Error: ' + error.message;
        }
      }
    }
  }
}

</script>

<style scoped>
.success-message {
  color: green;
  margin-bottom: 15px;
  font-weight: bold;
}

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
  width: 50%; 
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

.Signin {
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
  width: 80%; 
  max-width: 500px; 
}

input {
  width: 100%;
  padding: 10px; 
  padding-left: 40px; 
  font-size: 16px; 
  box-sizing: border-box;
  border-radius: 4px; 
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

.login-link {
  color: #007BFF;
  text-decoration: none;
}

.login-link:hover {
  text-decoration: underline;
}
</style>
