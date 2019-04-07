<template>
	<div class="container">
		<img src="../assets/img/logo.png" class="mt-5 mb-3 w-100">

		<b-form-group label="Email address">
			<b-form-input type="email" v-model="email" required placeholder="Email"/>
		</b-form-group>

		<b-form-group label="Password">
			<b-form-input type="password" v-model="password" required placeholder="Password"/>
		</b-form-group>

		<b-button @click="onLoginPressed" variant="primary" block>Login</b-button>
		<div class="create-account-text" @click="goToRegister">Don't have an account? Create one!</div>
	</div>
</template>

<script>
import axios from "axios";
import router from "@/router";

export default {
	data() {
		return {
			email: '',
			password: '',
		}
	},
	methods: {
		onLoginPressed() {
			this.$store.dispatch("auth/login", { email: this.email, password: this.password }).then(() => {
				this.$router.replace("/map");
			})
		},
		goToRegister() {
			this.$router.replace("/register");
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

