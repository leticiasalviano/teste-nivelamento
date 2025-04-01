<template>
  <div class="container">
    <div class="header">
      <h1>Buscar Operadoras</h1>
      <div class="credits">Desenvolvido com 💖 por Leticia</div>
    </div>

    <div class="search-container">
      <div class="search-wrapper">
        <svg class="search-icon" viewBox="0 0 24 24">
          <path
            fill="#ff7aa8"
            d="M9.5,3A6.5,6.5 0 0,1 16,9.5C16,11.11 15.41,12.59 14.44,13.73L14.71,14H15.5L20.5,19L19,20.5L14,15.5V14.71L13.73,14.44C12.59,15.41 11.11,16 9.5,16A6.5,6.5 0 0,1 3,9.5A6.5,6.5 0 0,1 9.5,3M9.5,5C7,5 5,7 5,9.5C5,12 7,14 9.5,14C12,14 14,12 14,9.5C14,7 12,5 9.5,5Z"
          />
        </svg>
        <input
          v-model="query"
          @input="searchOperators"
          placeholder="Digite o nome da operadora"
          class="search-input"
        />
        <div v-if="loading" class="loading"></div>
      </div>
    </div> 

    <ul v-if="operadoras.length" class="operators-list">
      <li
        v-for="operadora in operadoras"
        :key="operadora.id"
        class="operator-item"
      >
        <span class="operator-name">{{ operadora.Nome_Fantasia }}</span>
      </li>
    </ul>

    <div v-else-if="query.length >= 1 && !loading" class="no-results">
      <svg class="no-results-icon" viewBox="0 0 24 24">
        <path
          fill="#ff7aa8"
          d="M12,2A10,10 0 0,1 22,12A10,10 0 0,1 12,22A10,10 0 0,1 2,12A10,10 0 0,1 12,2M12,4A8,8 0 0,0 4,12C4,14.4 5,16.5 6.7,18C8.1,16.7 10,16 12,16C14,16 15.8,16.7 17.3,18C19,16.5 20,14.4 20,12A8,8 0 0,0 12,4M12,6A1.5,1.5 0 0,1 13.5,7.5A1.5,1.5 0 0,1 12,9A1.5,1.5 0 0,1 10.5,7.5A1.5,1.5 0 0,1 12,6M7.5,10.5A1.5,1.5 0 0,1 9,12A1.5,1.5 0 0,1 7.5,13.5A1.5,1.5 0 0,1 6,12A1.5,1.5 0 0,1 7.5,10.5M16.5,10.5A1.5,1.5 0 0,1 18,12A1.5,1.5 0 0,1 16.5,13.5A1.5,1.5 0 0,1 15,12A1.5,1.5 0 0,1 16.5,10.5Z"
        />
      </svg>
      <p>Nenhuma operadora encontrada</p>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      query: "",
      operadoras: [],
      loading: false,
    };
  },
  methods: {
    async searchOperators() {
      if (this.query.length >= 1) {
        this.loading = true;
        try {
          const response = await axios.get(`http://localhost:8000/buscar`, {
            params: { query: this.query },
          });
          this.operadoras = response.data;
        } catch (error) {
          console.error("Erro ao buscar operadoras:", error);
        } finally {
          this.loading = false;
        }
      } else {
        this.operadoras = [];
        this.loading = false;
      }
    },
  },
};
</script>

<style scoped>
.container {
  max-width: 800px;
  margin: 0 auto;
  padding: 30px;
  font-family: "Arial", sans-serif;
  background-color: #fff5f7;
  min-height: 100vh;
}

.header {
  text-align: center;
  margin-bottom: 30px;
}

h1 {
  color: #d23669;
  font-size: 2.5rem;
  margin-bottom: 10px;
}

.credits {
  color: #ff7aa8;
  font-style: italic;
  font-size: 0.9rem;
}

.search-container {
  margin-bottom: 25px;
  text-align: center;
}

.search-wrapper {
  position: relative;
  display: inline-block;
  width: 100%;
  max-width: 500px;
}

.search-icon {
  position: absolute;
  left: 15px;
  top: 50%;
  transform: translateY(-50%);
  width: 20px;
  height: 20px;
}

.search-input {
  width: 100%;
  padding: 12px 20px 12px 45px;
  border: 2px solid #ffb8d0;
  border-radius: 30px;
  font-size: 1rem;
  outline: none;
  transition: all 0.3s;
  background-color: white;
}

.search-input:focus {
  border-color: #d23669;
  box-shadow: 0 0 8px rgba(210, 54, 105, 0.2);
}

.loading {
  position: absolute;
  right: 15px;
  top: 50%;
  transform: translateY(-50%);
  width: 20px;
  height: 20px;
  border: 3px solid rgba(255, 122, 168, 0.3);
  border-radius: 50%;
  border-top-color: #ff7aa8;
  animation: spin 1s ease-in-out infinite;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

.operators-list {
  list-style: none;
  padding: 0;
  margin: 0 auto;
  max-width: 600px;
}

.operator-item {
  background-color: white;
  margin-bottom: 10px;
  padding: 15px 20px;
  border-radius: 8px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
  transition: all 0.2s;
  border-left: 4px solid #ffb8d0;
}

.operator-item:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  border-left-color: #d23669;
}

.operator-name {
  color: #555;
  font-size: 1.1rem;
}

.no-results {
  text-align: center;
  padding: 40px;
  color: #ff7aa8;
}

.no-results-icon {
  width: 80px;
  opacity: 0.7;
  margin-bottom: 15px;
}
</style>
