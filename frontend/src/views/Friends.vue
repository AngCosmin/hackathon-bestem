<template>
  	<div class="container">
		<h4 class="mt-3">Friends</h4>

		<h5 v-if="users.length === 0">
			You have no friends :(
			<img src="http://www.reactiongifs.com/r/sbbn.gif" class="mt-5 w-100">
		</h5>

		<b-card v-if="users.length > 0" bg-variant="white" text-variant="dark">
			<b-card-text v-for="user in users" :key="user.name" class="text-left">
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
			users: [],
		}
	},
	watch: {
	},
	created() {
		axios.get('/account/friends').then(response => {
			this.users = response.data.message
		})
	},
	methods: {
	}
}
</script>
