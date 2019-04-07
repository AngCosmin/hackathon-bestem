<template>
  	<div class="container">
		<h4 class="mt-3">Admin</h4>
		<hr>

		<h5>Pending users</h5>
		<table class="w-100">
			<tr>
				<th>Avatar</th>
				<th>Name</th>
				<th>Action</th>
			</tr>
			<tr v-for="user in pendingUsers" :key="user.id">
				<td><b-img :src="user.avatar" rounded="circle" width="64px"></b-img>
				<td>{{ user.name }}</td>
				<td>
					<b-button size="sm" variant="success" @click="onApproveUserPressed(user.id)">Approve</b-button>
				</td>
			</tr>
		</table>

		<hr>

		<h5>Pending pins</h5>
		<table class="w-100">
			<tr>
				<th>Title</th>
				<th>Description</th>
				<th>Action</th>
			</tr>
			<tr v-for="pin in pendingPins" :key="pin.id">
				<td>{{ pin.title }}</td>
				<td>{{ pin.description }}</td>
				<td>
					<b-button size="sm" variant="success" @click="onApprovePinPressed(pin.id)">Approve</b-button>
				</td>
			</tr>
		</table>
	</div>
</template>

<script>
import axios from '@/services/api.service'
import router from "@/router";

export default {
	data() {
		return {
			pendingUsers: [],
			pendingPins: [],
		}
	},
	watch: {
	},
	created() {
		this.getPendingUsers()
		this.getPendingPins()
	},
	methods: {
		getPendingUsers() {
			axios.get('/utils/pending_users').then(response => {
				this.pendingUsers = response.data.message
			})
		},
		getPendingPins() {
			axios.get('/utils/pending_pins').then(response => {
				this.pendingPins = response.data.message
			})
		}, 
		onApproveUserPressed(id) {
			let formData = new FormData()
			formData.append('user_id', id)
			axios.post('/utils/approve_user_profile', formData).then(response => {
				this.getPendingUsers()
			})
		},
		onApprovePinPressed(id) {
			let formData = new FormData()
			formData.append('pin_id', id)
			axios.post('/utils/approve_pin_cleaned', formData).then(response => {
				this.getPendingPins()
			})
		},
	}
}
</script>

<style>
	td {
		font-size: 0.8em;
	}
</style>
