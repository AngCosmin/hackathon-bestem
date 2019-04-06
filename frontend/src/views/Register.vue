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
			<b-form-input type="password" v-model="password" required placeholder="Password"/>
		</b-form-group>

		<b-form-group v-if="role === 2" label="Phone">
			<b-form-input type="text" v-model="phone" required placeholder="Phone"/>
		</b-form-group>

		<b-form-group v-if="role === 2">
			<b-form-textarea v-model="info" placeholder="Other info" rows="3" max-rows="6"></b-form-textarea>
		</b-form-group>

		<GmapMap v-if="role === 2" :options="mapOptions" :center="{ lat: 44.430350, lng: 26.102209 }" :zoom="12" map-type-id="terrain" class="mb-3" style="height: 400px">
			<GmapMarker :position="location" @drag="onLocationChange" :draggable="true">
				<gmap-info-window :opened="true">Drag me somewhere</gmap-info-window>
			</GmapMarker>
		</GmapMap>

		<div :class="{ 'text-success': registrationSuccess, 'text-danger': !registrationSuccess }" class="mt-3 mb-3">
			<span v-if="registrationSuccess === true">
				You have successfully registered! <br> 
				Go to <span class="go-to-login" @click="goToLogin">login</span>
			</span>
			<span v-else-if="registrationSuccess === false">There was an error</span>
		</div>

		<b-button @click="onRegisterPressed" variant="primary" class="mb-3" block>Register</b-button>
	</div>
</template>

<script>
import axios from "axios";
import router from "@/router";

export default {
	data() {
		return {
			registrationSuccess: null,
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
			let formData = new FormData()

			formData.append('role', this.role)
			formData.append('name', this.name)
			formData.append('email', this.email)
			formData.append('password', this.password)

			if (this.role === 2) {
				formData.append('phone', this.phone)
				formData.append('info', this.info)
				formData.append('lat', this.location.lat)
				formData.append('lng', this.location.lng)
			}

			axios.post('/auth/register', formData).then(response => {
				this.registrationSuccess = true
			})
		},
		onLocationChange(location) {
			this.location.lat = location.latLng.lat()
			this.location.lng = location.latLng.lng()
		},
		goToLogin() {
			this.$router.replace("/login");
		}
	}
};
</script>

<style>
	.go-to-login {
		text-decoration: underline;
	}
</style>

