<template>
  	<div class="container-fluid">
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