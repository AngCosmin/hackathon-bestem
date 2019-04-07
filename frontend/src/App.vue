<template>
  <div id="app">
	<div>
	  <b-navbar toggleable="lg" type="dark">
		<b-navbar-toggle target="nav_collapse"/>

		<b-navbar-brand href="#" class="m-l-3">ResQNature</b-navbar-brand>

		<b-collapse is-nav id="nav_collapse">
		  <b-navbar-nav>
			<b-nav-item active>
			  <router-link :to="{ name: 'home' }">Home</router-link>
			</b-nav-item>
			<b-nav-item v-if="isAuth">
			  <router-link :to="{ name: 'map' }">Map</router-link>
			</b-nav-item>
			<b-nav-item v-if="isAuth">
			  <router-link :to="{ name: 'calendar' }">Calendar</router-link>
			</b-nav-item>
			<b-nav-item v-if="isAuth">
			  <router-link :to="{ name: 'leaderboard' }">Leaderboard</router-link>
			</b-nav-item>
			<b-nav-item v-if="isAuth">
			  <router-link :to="{ name: 'profile' }">Profile</router-link>
			</b-nav-item>
			<b-nav-item v-if="!isAuth">
			  <router-link :to="{ name: 'login' }">Login</router-link>
			</b-nav-item>
		  </b-navbar-nav>

		  <b-navbar-nav v-if="isAuth" class="ml-auto">
			<b-navbar-nav right>
			  <b-nav-item>
				<span @click="onLogout">Logout</span>
			  </b-nav-item>
			</b-navbar-nav>
		  </b-navbar-nav>
		</b-collapse>
	  </b-navbar>
	</div>

	<router-view/>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
	name: "app",
	computed: {
		...mapGetters("auth", {
			isAuth: "isAuthenticated"
		})
	},
	created() {
		this.$store.dispatch('auth/autoLogin')
	},
	methods: {
		onLogout(evt) {
			this.$store.dispatch("auth/logout").then(() => {
				this.$router.replace("/login");
			})
		}
	}
};
</script>

<style>
/* latin */
@font-face {
  font-family: "Google Sans";
  font-style: normal;
  font-weight: 400;
  src: local("Google Sans Regular"), local("GoogleSans-Regular"),
	url(https://fonts.gstatic.com/s/googlesans/v11/4UaGrENHsxJlGDuGo1OIlL3Owp4.woff2)
	  format("woff2");
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA,
	U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215,
	U+FEFF, U+FFFD;
}

@font-face {
  font-family: "Roboto";
  font-style: normal;
  font-weight: 300;
  src: local("Roboto Light"), local("Roboto-Light"),
	url(https://fonts.gstatic.com/s/roboto/v18/KFOlCnqEu92Fr1MmSU5fBBc4.woff2)
	  format("woff2");
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA,
	U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215,
	U+FEFF, U+FFFD;
}

#app {
  font-family: "Google Sans", "Roboto", "Raleway", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.nav-item a {
  color: #fff;
}

.nav-item a:hover {
  text-decoration: none;
  color: #3498db;
}

.navbar {
  background-color: #27ae60 !important;
}

.container-fluid {
  margin: 0;
  padding-left: 0 !important;
  padding-right: 0 !important;
}

.btn-primary {
  background-color: #27ae60 !important;
  border-color: #27ae60 !important;
}
</style>
