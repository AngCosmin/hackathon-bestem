<template>
  	<div class="container">
		<h4 class="mt-3">Leaderboard</h4>

		<b-card bg-variant="white" text-variant="dark">
			<b-card-text v-for="user in users" :key="user.name" class="text-left">
				<img :src="user.avatar" width="48px">
				{{ user.name }} - {{ user.points }} points
			</b-card-text>
		</b-card>
	</div>
</template>

<script>
import axios from '@/services/api.service'
import router from "@/router";

export default {
	data() {
		return {
			users: [],
		}
	},
	watch: {
	},
	created() {
		axios.get('/account/leaderboard').then(response => {
			this.users = response.data.message
		})
	},
	methods: {
	}
}
</script>
