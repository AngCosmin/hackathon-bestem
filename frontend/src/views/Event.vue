<template>
  	<div class="container">
		<h4 class="mt-3">{{ name }}</h4>
		<h6>{{ description }}</h6>

		<b-button-group size="md" class="mb-3">
			<b-button variant="outline-success">Photos<br>{{ photos.length }}</b-button>
			<b-button variant="outline-success" @click="onShareOnFacebook">Share on Facebook</b-button>
			<b-button variant="outline-success" @click="showGoing = !showGoing">Going<br>{{ usersGoing.length }}</b-button>
		</b-button-group>

		<b-carousel
			:interval="3000"
			controls
			indicators
			background="#ababab"
			img-width="1024"
			img-height="480"
			style="text-shadow: 1px 1px 2px #333;">

			<b-carousel-slide v-for="link in photos" :key="link" :img-src="link"></b-carousel-slide>
		</b-carousel>

		<b-card v-if="showGoing" bg-variant="white" text-variant="dark" title="Going">
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
			showGoing: false,
			name: '',
			description: '',
			timeStart: '',
			timeEnd: '',
			usersGoing: [],
			photos: [],
		}
	},
	created() {
		axios.get('/event/get', { params: { event_id: this.$route.params.id } }).then(response => {
			let result = response.data.message

			this.name = result.title
			this.description = result.description
			this.timeStart = result.time_start
			this.timeEnd = result.time_end
			this.usersGoing = result.users
			this.photos = result.photos
		})
	},
	methods: {
		onShareOnFacebook() {
			let host = 'http://127.0.0.1:8080/#' + this.$route.fullPath
			window.open('https://www.facebook.com/sharer.php?u=' + host + '?t=asdasdasd' + this.name, "_blank")
		}
	}
}
</script>
