<template>
  	<div class="container-fluid">
		<div class="upcomming-events">
			<h5>Upcomming event</h5>
			<div class="event">
				<div class="title">Clean</div>
				<div class="time">
					2019-04-08 12:00 - 2019-04-08 18:00
				</div>
			</div>
		</div>

		<full-calendar :events="events" :config="config" @event-selected="eventSelected"></full-calendar>

		<b-modal ref="modal-event-details" hide-footer :title="eventDetails.title">
			<div class="d-block text-center">
				<b-button type="submit" variant="primary">Going</b-button>
			</div>
		</b-modal>

		
	</div>
</template>

<script>
import { mapGetters } from "vuex";
import axios from '@/services/api.service'
import router from "@/router";
import 'fullcalendar/dist/fullcalendar.css'

export default {
	computed: {
		...mapGetters("auth", {
			getEmail: "getEmail"
		})
	},
	data() {
		return {
			events: [
				{
					title: 'Clean',
					description: 'desc',
					start: '2019-04-07 12:00',
					end: '2019-04-07 18:00',
				},
			],
			config: {
				defaultView: 'month',
				height: 'auto',
				eventRender: function(event, element) {
					console.log(event)
				}
			},
			eventDetails: {
				title: '',
				description: '',
			}
		}
	},
	watch: {
	},
	created() {
	},
	methods: {
		eventSelected(e) {
			this.$refs['modal-event-details'].show()
			console.log(e)

			this.eventDetails.title = e.title
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
