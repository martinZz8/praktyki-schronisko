<template>
  <v-card class="ma-4">
    <v-form ref="form">
      <v-container>
        <p>Tutaj będzie treść strony głównej.</p>
        <div class="image">
          <a href="https://media.tenor.com/images/7287cd13acf63ccfa11c00aabee30e7f/tenor.png">
            <img src="https://media.tenor.com/images/7287cd13acf63ccfa11c00aabee30e7f/tenor.png" style="width: 1500px;">
          </a>
        </div>
      </v-container>
    </v-form>
  </v-card>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Home',
  components: {
  }
}
</script>

<style scoped>
.image {
  text-align: center;
}
</style>
