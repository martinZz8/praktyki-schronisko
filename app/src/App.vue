<template>
  <div id="app">
    <v-app>
      <v-app-bar app color="rgba(57,200,67,1)">
        <div class="d-flex align-center">
          <router-link to="/">
            <v-img :src="require('@/assets/logo.png')" alt="logo" contain height="100" width="50"/>
          </router-link>
        </div>
        <v-toolbar-title class="ml-5"><span style="color: white">Schronisko dla zwierząt</span></v-toolbar-title>
        <!-- Tutaj dodajemy elementy app baru -->
      </v-app-bar>
      <!-- Nie zmieniać zawartości tagu <v-main> -->
      <v-main><router-view/></v-main>
    </v-app>
  </div>
</template>

<script>

export default {
  name: 'App',

  components: {
  },

  data: () => ({
    //
  }),
};
</script>
