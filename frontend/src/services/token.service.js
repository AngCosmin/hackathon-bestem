import axios from './api.service'

const canMakeRequest = async function () {
    try {
        await axios.post('/auth/login')
        return true
    }
    catch(e) {
        return false
    }
}

export { canMakeRequest }
