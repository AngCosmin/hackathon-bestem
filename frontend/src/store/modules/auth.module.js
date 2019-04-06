import axios from '@/services/api.service'
import router from '@/router'

const state = {
	token: null
}

const mutations = {
	authUser(state, token) {
		state.token = token
	},
	clearAuthData(state) {
		state.token = null
	}
}

const getters = {
	isAuthenticated(state) {
		return state.token !== null
	},
}

const actions = {
	login: ({ commit }, authData) => {
		let formData = new FormData()

		formData.append('email', authData.email)
		formData.append('password', authData.password)

		axios.post('/auth/login', authData).then(response => {
			commit('authUser', response.data.token);
			localStorage.setItem('token', response.data.token)
			router.replace('/map');
		}).catch(error => {
			console.error(error);
		})
	},
	autoLogin({ commit, dispatch }) {
		let token = localStorage.getItem('token')

		if (!token) {
			dispatch('logout')
			return
		}

		commit('authUser', token)
	},
	logout: ({ commit }) => {
		commit('clearAuthData');
		localStorage.removeItem('token');
		router.push('/login')
	},
}

export default {
	namespaced: true,
	state,
	mutations,
	getters,
	actions,
};

