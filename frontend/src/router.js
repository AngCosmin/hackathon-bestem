import Vue from 'vue'
import Router from 'vue-router'
import { canMakeRequest } from '@/services/token.service'

Vue.use(Router)

function loadView(view) {
    return () => import(/* webpackChunkName: "view-[request]" */ `@/views/${view}.vue`)
}

let routes = [
    {
        path: '/',
        component: loadView('Home'),
        meta: { requiresAuth: false },
        name: 'home',
    },
    {
        path: '/login',
        component: loadView('Login'),
        meta: { requiresAuth: false },
        name: 'login',
    },
    {
        path: '/register',
        component: loadView('Register'),
        meta: { requiresAuth: false },
        name: 'register',
    },
    {
        path: '/map',
        component: loadView('Map'),
        meta: { requiresAuth: true },
        name: 'map',
    },
    {
        path: '/calendar',
        component: loadView('Calendar'),
        meta: { requiresAuth: true },
        name: 'calendar',
    },
    {
        path: '/profile',
        component: loadView('Profile'),
        meta: { requiresAuth: true },
        name: 'profile',
    },
    {
        path: '/friends',
        component: loadView('Friends'),
        meta: { requiresAuth: true },
        name: 'friends',
    },
    {
        path: '/leaderboard',
        component: loadView('Leaderboard'),
        meta: { requiresAuth: true },
        name: 'leaderboard',
    },
]

const router = new Router({
    routes: routes,
})

router.beforeEach((to, from, next) => {
    let token = localStorage.getItem('token')
    let requireAuth = to.matched.some(record => record.meta.requiresAuth)

    if (to.path === '/login' && token) {
        next('/map') 
    }

    if (!requireAuth) {
        next()
    }
    else {
        if (token) { 
            next() 
        }
        else {
            next('/login')                 
        }
    }
});


export default router