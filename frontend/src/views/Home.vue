<template>
  	<div class="container">
		<h2 class="mt-3"> Welcome to the ResQNature! </h2>
		<h4> We'll handle it from here. </h4>

		<p> Our application facilitates the process of marking and cleaning the polutted 
			areas from your town! 9 out of 10 people said they would recycle if it were “easier”. 
			You came up with the solution! Follow the steps bellow in order to help us make a 
			better future for our planet!
		</p>

		<b-carousel
			id="carousel-fade"
			style="text-shadow: 0px 0px 2px #000"
			fade
			indicators
			img-width="1024"
			img-height="480"
		>
			<b-carousel-slide
			caption="Mark the polutted places form your town!"
			img-src="https://i.imgur.com/NEUnh7o.jpg"
			></b-carousel-slide>
			<b-carousel-slide
			caption="Attend events where you clean some areas!"
			img-src="https://i.imgur.com/aXSnhQc.jpg"
			></b-carousel-slide>
			<b-carousel-slide
			caption="Live in a clean city!"
			img-src="https://i.imgur.com/vSEvTRl.jpg"
			></b-carousel-slide>
		</b-carousel>
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