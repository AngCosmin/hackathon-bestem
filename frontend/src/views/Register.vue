<template>
	<div class="container">
		<img src="../assets/img/logo.png" class="mt-5 mb-3" width="300px">

		<b-form-group label="Role">
			<b-form-select v-model="role">
				<option :value="1">Volunteer</option>
				<option :value="2">Collector</option>
				<option :value="3">Administrator</option>
			</b-form-select>
		</b-form-group>

		<b-form-group label="Name">
			<b-form-input type="text" v-model="name" required placeholder="Name"/>
		</b-form-group>
	
		<b-form-group label="Email address">
			<b-form-input type="email" v-model="email" required placeholder="Email"/>
		</b-form-group>

		<b-form-group label="Password">
			<b-form-input type="password" v-model="password" required placeholder="Email"/>
		</b-form-group>

		<b-form-group v-if="role === 2" label="Phone">
			<b-form-input type="text" v-model="phone" required placeholder="Phone"/>
		</b-form-group>

		<b-form-group v-if="role === 2">
			<b-form-textarea v-model="info" placeholder="Other info" rows="3" max-rows="6"></b-form-textarea>
		</b-form-group>

		<GmapMap v-if="role === 2" :options="mapOptions" :center="location" :zoom="12" map-type-id="terrain" class="mb-3" style="height: 400px">
			<GmapMarker :position="location" @drag="onLocationChange" :draggable="true">
				<gmap-info-window :opened="true">Drag me somewhere</gmap-info-window>
			</GmapMarker>
		</GmapMap>

		<b-button @click="onRegisterPressed" variant="primary" class="mb-3" block>Register</b-button>
	</div>
</template>

<script>
import axios from "axios";
import router from "@/router";

export default {
	data() {
		return {
			mapOptions: {
				fullscreenControl: false,
				streetViewControl: false,
			},
			role: 1,
			name: '',
			email: '',
			password: '',
			phone: '',
			info: '',
			location: { lat: 44.430350, lng: 26.102209 }
		}
	},
	methods: {
		onRegisterPressed() {
			this.$store.dispatch("auth/login", { email: email, password: password }).then(() => {
				this.$router.replace("/map");
			})
		},
		onLocationChange(location) {
			this.newPin.position.lat = location.latLng.lat()
			this.newPin.position.lng = location.latLng.lng()
		},
	}
};
</script>

<style>
	.create-account-text {
		margin-top: 20px;
		text-decoration: underline;
		font-size: 0.9em;
	}
</style>

