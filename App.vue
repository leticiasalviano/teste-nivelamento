<template>
  <div id="app">
    <SearchOperators />
  </div>
</template>

<script>
import SearchOperators from "./components/SearchOperators.vue";

export default {
  components: {
    SearchOperators,
  },
};
</script>

<style>
#app {
  font-family: "Arial", sans-serif;
  text-align: center;
  margin: 0;
  padding: 0;
  min-height: 100vh;
  background: linear-gradient(135deg, #fff5f7 0%, #ffecef 100%);
}

/* Estilos globais opcionais para manter a consistência */
body {
  margin: 0;
  padding: 0;
  color: #555;
}

/* Você pode adicionar estilos globais para outros elementos se necessário */
button {
  background-color: #d23669;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 30px;
  cursor: pointer;
  transition: all 0.3s;
}

button:hover {
  background-color: #ff7aa8;
  transform: translateY(-2px);
}
</style>
