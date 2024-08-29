<template>
  <div class="RightSide">
    <div class="Signin">
      <label>Already have an account? <router-link to="/login">Sign in</router-link></label>
    </div>
    <div class="main text">
      <div class="JoinUs">
        <b><h2>Join Us!</h2></b>
        <br>
        <label>To begin this journey, tell us what type of account</label>
        <br>
        <span class="subtext">you’d be opening.</span>
      </div>
      <Option
        userType="manager"
       :imageSrc="require('@/assets/Images/manager.png')"
        title="Manager"
        description="Signup as a manager to manage the tasks and bugs"
      />
      <Option
        userType="developer"
        :imageSrc="require('@/assets/Images/developer.png')"
        title="Developer"
        description="Signup as a developer to work on tasks and bugs"
      />
      <Option
        userType="qa"
       :imageSrc="require('@/assets/Images/QA.png')"
        title="QA"
        description="Signup as a QA to ensure quality and manage bugs"
      />
    </div>
  </div>
</template>

<script>
import Option from './UserOptions.vue';

export default {
  name: 'RightSideOption',
  components: {
    Option
  }
}
</script>

<style scoped>
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

.Signin {
  position: absolute;
  top: 20px;
  right: 20px;
  margin: 0;
  text-align: right;
}

.main {
  width: 100%;
}

.JoinUs {
  margin-bottom: 30px;
}
</style>
