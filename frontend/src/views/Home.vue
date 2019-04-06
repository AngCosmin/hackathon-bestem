<template>
  	<div class="container-fluid">
		<h1> Welcome to the City Green! </h1>
		<h2> We'll handle it from here. </h2>

		<p> Our application facilitates the process of marking and cleaning the polutted 
			areas from your town! 9 out of 10 people said they would recycle if it were “easier”. 
			You came up with the solution! Follow the steps bellow in order to help us make a 
			better future for our planet! </p>
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