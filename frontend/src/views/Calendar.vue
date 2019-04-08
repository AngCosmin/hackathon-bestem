<template>
  	<div class="container-fluid">
		<div class="upcomming-events">
			<h5>Upcomming event</h5>
			<div v-if="myEvents.length === 0" class="title">There is no upcomming events</div>
			<div v-for="event in myEvents" :key="event.title" class="event">
				<div class="title">{{ event.title }}</div>
				<div class="time">
					{{ event.time_start }} - {{ event.time_end }}
				</div>
			</div>
		</div>

		<full-calendar :events="events" :config="config" @event-selected="eventSelected"></full-calendar>

		<b-modal ref="modal-event-details" hide-footer :title="eventDetails.title">
			<div class="d-block text-center">
				{{ eventDetails.description }}
				
				<hr v-if="eventDetails.description !== null">

				<div>Starting on {{ eventDetails.start }}</div>
				<div>Ending on {{ eventDetails.end }}</div>
				<hr>

				<b-input-group class="mt-3">
					<b-form-input v-model="friendEmail" placeholder="Friend's email"></b-form-input>
					<b-input-group-append>
						<b-button variant="primary" @click="onInvitePressed">Invite</b-button>
					</b-input-group-append>
				</b-input-group>
				<hr>

				<div v-if="invitationSuccess === true" class="text-success">Invitation sent!</div>
				<div v-else-if="invitationSuccess === false" class="text-danger">Email not found!</div>
				
				<div v-if="goingSuccess === true" class="text-success">You are now going!</div>
				<div v-else-if="goingSuccess === false" class="text-danger">Already going</div>
				

				<b-button class="mt-3" variant="primary" block @click="goToEvent(eventDetails.id)">View</b-button>
				<b-button v-if="showGoingButton && !eventsToGo.includes(eventDetails.id)" class="mt-3" variant="primary" block @click="onGoingPressed(eventDetails.id)">Going</b-button>
			</div>
		</b-modal>
	</div>
</template>

<script>
import { mapGetters } from "vuex";
import axios from '@/services/api.service'
import router from "@/router";
import 'fullcalendar/dist/fullcalendar.css'
import { setTimeout } from 'timers';

export default {
	data() {
		return {
			myEvents: [],
			friendEmail: '',
			selectedEventId: null,
			invitationSuccess: null,
			goingSuccess: null,
			events: [],
			config: {
				defaultView: 'month',
				height: 'auto',
			},
			eventDetails: {
				id: '',
				title: '',
				description: null,
				start: '',
				end: '',
			},
			showGoingButton: true,
			eventsToGo: [],
		}
	},
	watch: {
	},
	created() {
		this.getEvents()
		this.getMyEvents()
	},
	methods: {
		eventSelected(e) {
			this.showGoingButton = true
			this.$refs['modal-event-details'].show()
			this.eventDetails.id = e.id
			this.eventDetails.title = e.title
			this.eventDetails.description = e.description
			this.eventDetails.start = e.start.format("DD-MM-YYYY HH:mm")
			this.eventDetails.end = e.end.format("DD-MM-YYYY HH:mm")

			this.selectedEventId = e.id
		},
		getEvents() {
			axios.get('event/all').then(response => {
				this.events = response.data.message
			})
		},
		getMyEvents() {
			axios.get('event/my_events').then(response => {
				this.myEvents = response.data.message
			})
		},
		onInvitePressed() {
			let formData = new FormData()
			formData.append('email_to', this.friendEmail)
			formData.append('event_id', this.selectedEventId)

			axios.post('/utils/send_mail', formData).then(response => {
				this.friendEmail = ''
				this.invitationSuccess = true
				setTimeout(() => {
					this.invitationSuccess = null
				}, 3000)
			}).catch((error) => {
				console.log(error)
			})
		},
		goToEvent(id) {
			this.$router.push({ name: 'event', params: { id: id } })
		},
		onGoingPressed(id) {
			let formData = new FormData()
			formData.append('event_id', this.selectedEventId)

			this.showGoingButton = false

			axios.post('/event/going', formData).then(response => {
				let success = response.data.success

				if (success === true) {
					this.goingSuccess = true
					this.getMyEvents()
					this.eventsToGo.push(id)
				}
				else {
					this.goingSuccess = false
				}

				setTimeout(() => {
					this.goingSuccess = null
				}, 3000)
				
			}).catch((error) => {
				console.log(error)
			})
		}
	}
}
</script>

<style>
body .fc {
	font-size: 0.8em;
}

#calendar {
	margin-top: 10px;
}

.fc-toolbar {
	padding-left: 10px;
	padding-right: 10px;
}

.fc-center {
	margin-top: 10px;
}

.fc-center h2 {
	font-size: 1.5em;
}

.fc-icon {
	color: #fff;
}

.fc-button {
	background-color: #27ae60 !important;
}

.fc-state-default {
	background-color: #27ae60 !important;
	background-image: linear-gradient(to bottom, #27ae60, #27ae60) !important;
	color: #fff;
	text-shadow: none;
}

.fc-unthemed td.fc-today{
	background: #96d3af !important;
}

.fc-event {
	background-color: #27ae60 !important;
	color: #FFF !important;
	border: 1px solid #27ae60 !important;
}

/* Upcomming events */
.upcomming-events {
	background-color: #27ae60;
	margin: 10px 10px;
	padding: 10px 10px;
	border-radius: 8px;
	color: #FFF;
	box-shadow: 0px 8px 12px 0px rgba(0,0,0,0.25);
}

.upcomming-events .title {
	font-weight: bold;
}

.upcomming-events .time {
	font-size: 0.8em;
}

</style>
