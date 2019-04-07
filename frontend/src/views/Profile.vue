<template>
  	<div class="container">
		<b-img :src="picture !== null ? picture : 'https://i.imgur.com/JRoOWKy.jpg' " class="profile-picture" rounded="circle" width="100px" height="100px"></b-img>

		<h4>{{ name }}</h4>

		<b-button-group size="md" class="mb-3">
			<b-button variant="outline-success">Cleaned spots<br>{{ cleaned }}</b-button>
			<b-button variant="outline-success">Points<br>{{ points }}</b-button>
			<b-button variant="outline-success" @click="goToFriends">Friends<br>{{ noFriends }}</b-button>
			<b-button variant="outline-success">Reported spots<br>{{ reported }}</b-button>
		</b-button-group>

		<b-card bg-variant="white" text-variant="dark" title="Badges" class="mb-3">
			<div v-if="badges.length === 0">You have no badges</div>
			<div v-else>
				<b-card-text v-for="badge in badges" :key="badge.icon">
					<img :src="badge.icon" width="48px" @click="showDetails(badge)">
					{{ badge.name }}
				</b-card-text>
			</div>
		</b-card>

		<ve-line :data="chartData"></ve-line>

		<b-modal v-if="selectedBadge" ref="modal-details" hide-footer :title="selectedBadge.name">
			<div class="d-block text-center">
				<img :src="selectedBadge.icon" width="72px">
				<br>
				{{ selectedBadge.description }}
				<br>
				Earned at {{ selectedBadge.points }} points
			</div>
		</b-modal>
	</div>
</template>

<script>
import axios from '@/services/api.service'
import router from "@/router";

export default {
	data() {
		return {
			name: '',
			cleaned: 0,
			reported: 0,
			points: 0,
			noFriends: 0,
			picture: null,
			badges: [],
			selectedBadge: null,
			chartData: {
				columns: ['Date', 'Reported spots', 'Cleaned spots'],
				rows: [
				]
			}
		}
	},
	watch: {
	},
	created() {
		axios.get('/account/details').then(response => {
			let result = response.data.message

			this.name = result.name
			this.cleaned = result.cleaned
			this.reported = result.reported
			this.points = result.points
			this.noFriends = result.nr_friends
			this.picture = result.picture			
		})

		axios.get('/badge/get-user-badges').then(response => {
			let result = response.data.message
			this.badges = result
		})

		axios.get('/account/statistics').then(response => {
			this.chartData.rows = response.data.message
		})
	},
	methods: {
		showDetails(badge) {
			this.selectedBadge = badge

			if (this.$refs['modal-details']) {
				this.$refs['modal-details'].show()
			} 
		},
		goToFriends() {
			this.$router.push("/friends")
		}
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
