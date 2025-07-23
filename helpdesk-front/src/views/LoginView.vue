<template>
  <div>
    <h2>Connexion</h2>
    <form @submit.prevent="login">
      <input v-model="email" type="email" placeholder="Email" required />
      <input v-model="password" type="password" placeholder="Mot de passe" required />
      <button type="submit">Se connecter</button>
    </form>
    <p v-if="error" style="color: red;">{{ error }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const email = ref('')
const password = ref('')
const error = ref('')
const router = useRouter()

const login = async () => {
  try {
    const response = await axios.post('http://127.0.0.1:8000/api/users/auth/token/login/', {
      email: email.value,
      password: password.value
    })

    const token = response.data.auth_token
    localStorage.setItem('token', token)
    router.push('/dashboard')
  } catch (err) {
    error.value = "Identifiants invalides"
  }
}
</script>
