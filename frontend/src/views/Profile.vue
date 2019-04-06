<template>
  	<div class="container">
		<b-img :src="'https://i.imgur.com/JRoOWKy.jpg'" class="profile-picture" rounded="circle" width="100px" height="100px"></b-img>

		<b-card bg-variant="white" text-variant="dark" title="Badges">
			<b-card-text>
				<img src="https://i.imgur.com/dZO8Oe2.png" width="75px" title="First place cleaned">
				<img src="https://i.imgur.com/enAo5hV.png" width="75px" title="First place cleaned">
				<img src="https://i.imgur.com/GrluEyU.png" width="75px" title="First place cleaned">
				<img src="https://i.imgur.com/C8NRv16.png" width="75px" title="First place cleaned">
				<img src="https://i.imgur.com/xVzReTJ.png" width="75px" title="First place cleaned">
			</b-card-text>
		</b-card>
	</div>
</template>

<script>
import { mapGetters } from "vuex";
import axios from '@/services/api.service'
import router from "@/router";

export default {
	computed: {
		...mapGetters("auth", {
			getEmail: "getEmail"
		})
	},
	data() {
		return {
		}
	},
	watch: {
	},
	created() {
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
