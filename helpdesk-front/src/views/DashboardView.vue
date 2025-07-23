<template>
  <div>
    <h2>Mes tickets</h2>
    <ul>
      <li v-for="ticket in tickets" :key="ticket.id">
        {{ ticket.title }} - {{ ticket.status }}
      </li>
    </ul>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const router = useRouter()
const tickets = ref([])

onMounted(async () => {
  const token = localStorage.getItem('token')
  if (!token) {
    router.push('/login')
    return
  }

  try {
    const res = await axios.get('http://127.0.0.1:8000/api/tickets/', {
      headers: {
        Authorization: `Token ${token}`
      }
    })
    tickets.value = res.data
  } catch (e) {
    console.error('Erreur :', e)
  }
})
</script>
