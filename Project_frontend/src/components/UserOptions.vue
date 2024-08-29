<template>
  <div class="OptionSide">
    <div class="main text">
      <div class="containerOption" @click="setUserType(userType)">
        <div class="image">
          <img :src="imageSrc" alt="">
        </div>
        <div class="TextRight">
          <div><b>{{ title }}</b></div>
          <div>{{ description }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'UserOptions',
  props: {
    userType: {
      type: String,
      required: true
    },
    imageSrc: {
      type: String,
      required: true
    },
    title: {
      type: String,
      required: true
    },
    description: {
      type: String,
      required: true
    }
  },
  methods: {
    setUserType(type) {
      console.log(type);
      this.$router.push({ name: 'SignIn', query: { userType: type } }); // Navigate to the signin page
    }
  }
}
</script>

<style scoped>
.main {
  width: 100%;
}

.containerOption {
  display: flex;
  align-items: center;
  justify-content: flex-start;
  margin-top: 20px;
  border: 2px solid #ccc;
  padding: 10px;
  border-radius: 8px;
  padding-left: 50px;
  max-width: 400px;
  transition: background-color 0.3s;
}

.containerOption:hover {
  background-color: #007bff;
  color: white;
}

.image img {
  width: 30px;
  height: 30px;
}

.TextRight {
  text-align: left;
}

.TextRight div {
  margin-bottom: 5px;
  padding-left: 20px;
}
</style>
