<template>
  	<div class="container">
		<h5 v-if="friends !== null && friends.length === 0" class="mt-3">
			You are not following someone :(
			<img src="http://www.reactiongifs.com/r/sbbn.gif" class="mt-5 w-100">
		</h5>

		<b-card v-if="friends.length > 0" class="mt-3" bg-variant="white" text-variant="dark" title="Follows">
			<b-card-text v-for="user in friends" :key="user.name" class="text-left">
				<img :src="user.avatar" width="48px">
				{{ user.name }}
			</b-card-text>
		</b-card>

		<b-card v-if="suggestions.length > 0" class="mt-3" bg-variant="white" text-variant="dark" title="Suggestions">
			<b-card-text v-for="user in suggestions" :key="user.name" class="text-left">
				<img :src="user.avatar" width="48px" height="48px">
				{{ user.name }}
				<b-badge variant="success" @click="onFollowPressed(user.id)">Follow</b-badge>
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
			friends: null,
			suggestions: [],
		}
	},
	watch: {
	},
	created() {
		this.getData()
	},
	methods: {
		onFollowPressed(id) {
			let formData = new FormData()
			formData.append('user_id', id)

			axios.post('/account/follow', formData).then(response => {
				this.getData()
			})
		},
		getData() {
			axios.get('/account/friends').then(response => {
				this.friends = response.data.message.friends
				this.suggestions = response.data.message.suggestions
			})
		}
	}
}
</script>
