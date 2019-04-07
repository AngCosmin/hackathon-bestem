<template>
  	<div class="container">
		<h4>{{ name }}</h4>

		<b-card bg-variant="white" text-variant="dark" title="Going">
			<b-card-text v-for="user in usersGoing" :key="user.id" class="text-left">
				<img :src="user.avatar" width="48px">
				{{ user.name }}
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
			name: '',
			description: '',
		}
	},
	watch: {
	},
	created() {
		console.log(this.$route.params.id)
		axios.get('/event/get').then(response => {
			
		})
	},
	methods: {
	}
}
</script>

<style>
	.profile-picture {
		margin-top: 10px;
		margin-bottom: 30px;
		border: 3px solid #27ae60;
		box-shadow: 0 2px 30px #27ae5f81;
	}
</style>
