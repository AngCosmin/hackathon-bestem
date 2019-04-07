import axios from '@/services/api.service'
import router from '@/router'

const state = {
	token: null,
	role: null,
}

const mutations = {
	authUser(state, data) {
		state.token = data.token
		state.role = data.role
	},
	clearAuthData(state) {
		state.token = null
		state.role = null
	}
}

const getters = {
	isAuthenticated(state) {
		return state.token !== null
	},
	isVolunteer(state) {
		return parseInt(state.role) === 1
	},
	isCollector(state) {
		return parseInt(state.role) === 2
	},
	isAdmin(state) {
		return parseInt(state.role) === 3
	}
}

const actions = {
	login: ({ commit }, authData) => {
		let formData = new FormData()

		formData.append('email', authData.email)
		formData.append('password', authData.password)

		axios.post('/auth/login', authData).then(response => {
			commit('authUser', { token: response.data.token, role: response.data.role })
			localStorage.setItem('token', response.data.token)
			localStorage.setItem('role', response.data.role)
			router.replace('/map');
		}).catch(error => {
			console.error(error);
		})
	},
	autoLogin({ commit, dispatch }) {
		let token = localStorage.getItem('token')
		let role = localStorage.getItem('role')

		if (!token) {
			dispatch('logout')
			return
		}

		commit('authUser', {token: token, role: role})
	},
	logout: ({ commit }) => {
		commit('clearAuthData');
		localStorage.removeItem('token');
		localStorage.removeItem('role');
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

