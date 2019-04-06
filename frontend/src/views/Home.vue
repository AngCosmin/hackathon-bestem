<template>
  	<div class="container-fluid">
		<GmapMap :options="mapOptions" :center="{ lat: 44.430350, lng: 26.102209 }" :zoom="12" map-type-id="terrain" style="width: 100vw; height: 100vh;">
			<GmapMarker v-for="pin in mapRecyclePins" :key="pin.id" 
						:position="pin.position" 
						:clickable="true" 
						:icon="pin.icon"
						@click="onMarkerClicked"/>

			<GmapMarker v-for="pin in mapForCleaningPins" :key="pin.id" 
						:position="pin.position" 
						:clickable="true" 
						:icon="pin.icon"
						@click="onMarkerClicked"/>
			
			<GmapMarker v-if="newPin.show" :position="newPin.position" :draggable="true" :icon="newPin.icon">
				<gmap-info-window :opened="true">Place me somewhere</gmap-info-window>
			</GmapMarker>
		</GmapMap>

		<b-modal ref="my-modal" hide-footer title="Create new spot to clean">
			<div class="d-block text-center">
				<div class="form-group">
					<input v-model="newPin.form.title" type="text" class="form-control" placeholder="Title">
				</div>
				<div class="form-group">
					<textarea v-model="newPin.form.description" class="form-control" placeholder="Description"></textarea>
				</div>
				<div class="form-group">
					<label>Select photo before cleaning</label>
					<b-form-file v-model="newPin.form.photo" drop-placeholder="Drop file here..."></b-form-file>
				</div>

				{{ newPin.form.photo }}

				<b-button type="submit" variant="primary" @click="onSaveNewSpot">Save</b-button>
			</div>
		</b-modal>

		<button v-if="newPin.show" class="bubbly-button" @click="onPlacePressed">Place</button>
		<button v-else class="bubbly-button" @click="onAddPressed">Add</button>
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
			mapOptions: {
				fullscreenControl: false,
				streetViewControl: false,
			},
			mapRecyclePins: [
				{ id: 1, position: { lat: 44.429147, lng: 26.026514 }, icon: { url: 'https://i.imgur.com/wOgSiQU.png' } },
				{ id: 2, position: { lat: 44.417551, lng: 26.156501 }, icon: { url: 'https://i.imgur.com/wOgSiQU.png' } },
				{ id: 3, position: { lat: 44.470105, lng: 26.091612 }, icon: { url: 'https://i.imgur.com/wOgSiQU.png' } },
			],
			mapForCleaningPins: [
				{ id: 4, position: { lat: 44.435951, lng: 26.099595 }, icon: { url: 'https://i.imgur.com/uKscO2W.png' } },
				{ id: 5, position: { lat: 44.402239, lng: 26.116448 }, icon: { url: 'https://i.imgur.com/uKscO2W.png' } },
				{ id: 6, position: { lat: 44.392550, lng: 26.172245 }, icon: { url: 'https://i.imgur.com/uKscO2W.png' } },
			],
			newPin: {
				show: false,
				position: {
					lat: 44.430350, 
					lng: 26.102209,
				},
				icon: {
					url:'http://icons.iconarchive.com/icons/icons-land/vista-map-markers/32/Map-Marker-Marker-Outside-Chartreuse-icon.png'
				},
				form: {
					title: '',
					description: '',
					photo: null,
				}
			}
		};
	},
	watch: {
	},
	methods: {
		onMarkerClicked() {
			console.log('asd')
		},
		onSaveNewSpot() {
			let formData = new FormData()
			formData.append('title', this.newPin.form.title)
			formData.append('description', this.newPin.form.description)
			formData.append('lat', this.newPin.position.lat)
			formData.append('lng', this.newPin.position.lng)
			formData.append('file', this.newPin.form.photo)

			axios.post("/pin/create", formData, { 
				headers: { 
					'Content-Type': 'multipart/form-data',
					'Authorization': 'Bearer 123'
				}
			}).then(response => {
				console.log(response)
			}).catch(error => {
				console.error(error);
			});
		},
		onAddPressed(e) {
			this.makeAnimation(e)

			this.newPin.show = true
		},
		onPlacePressed(e) {
			this.makeAnimation(e)

			this.$refs['my-modal'].show()
		},
		makeAnimation(e) {
			e.preventDefault
			e.target.classList.remove('animate')
			e.target.classList.add('animate')
			setTimeout(function(){
				e.target.classList.remove('animate')
			}, 700)
		}
	}
}
</script>

<style>
.bubbly-button {
  position: fixed !important;
  bottom: 25px;
  left: 25px;
  display: block;
 
  font-family: 'Helvetica', 'Arial', sans-serif;
  display: inline-block;
  font-size: 1em;
  padding: 1em 2em;
  -webkit-appearance: none;
  appearance: none;
  background-color: #27ae60;
  color: #fff;
  border-radius: 4px;
  border: none;
  cursor: pointer;
  position: relative;
  transition: transform ease-in 0.1s, box-shadow ease-in 0.25s;
  box-shadow: 0 2px 25px #27ae5f81;
}
.bubbly-button:focus {
  outline: 0;
}
.bubbly-button:before, .bubbly-button:after {
  position: absolute;
  content: '';
  display: block;
  width: 140%;
  height: 100%;
  left: -20%;
  z-index: -1000;
  transition: all ease-in-out 0.5s;
  background-repeat: no-repeat;
}
.bubbly-button:before {
  display: none;
  top: -75%;
  background-image: radial-gradient(circle, #27ae60 20%, transparent 20%), radial-gradient(circle, transparent 20%, #27ae60 20%, transparent 30%), radial-gradient(circle, #27ae60 20%, transparent 20%), radial-gradient(circle, #27ae60 20%, transparent 20%), radial-gradient(circle, transparent 10%, #27ae60 15%, transparent 20%), radial-gradient(circle, #27ae60 20%, transparent 20%), radial-gradient(circle, #27ae60 20%, transparent 20%), radial-gradient(circle, #27ae60 20%, transparent 20%), radial-gradient(circle, #27ae60 20%, transparent 20%);
  background-size: 10% 10%, 20% 20%, 15% 15%, 20% 20%, 18% 18%, 10% 10%, 15% 15%, 10% 10%, 18% 18%;
}
.bubbly-button:after {
  display: none;
  bottom: -75%;
  background-image: radial-gradient(circle, #27ae60 20%, transparent 20%), radial-gradient(circle, #27ae60 20%, transparent 20%), radial-gradient(circle, transparent 10%, #27ae60 15%, transparent 20%), radial-gradient(circle, #27ae60 20%, transparent 20%), radial-gradient(circle, #27ae60 20%, transparent 20%), radial-gradient(circle, #27ae60 20%, transparent 20%), radial-gradient(circle, #27ae60 20%, transparent 20%);
  background-size: 15% 15%, 20% 20%, 18% 18%, 20% 20%, 15% 15%, 10% 10%, 20% 20%;
}
.bubbly-button:active {
  transform: scale(0.9);
  background-color: #1f8d4d;
  box-shadow: 0 2px 25px #1f8d4d81;
}
.bubbly-button.animate:before {
  display: block;
  animation: topBubbles ease-in-out 0.75s forwards;
}
.bubbly-button.animate:after {
  display: block;
  animation: bottomBubbles ease-in-out 0.75s forwards;
}
@keyframes topBubbles {
  0% {
    background-position: 5% 90%, 10% 90%, 10% 90%, 15% 90%, 25% 90%, 25% 90%, 40% 90%, 55% 90%, 70% 90%;
  }
  50% {
    background-position: 0% 80%, 0% 20%, 10% 40%, 20% 0%, 30% 30%, 22% 50%, 50% 50%, 65% 20%, 90% 30%;
  }
  100% {
    background-position: 0% 70%, 0% 10%, 10% 30%, 20% -10%, 30% 20%, 22% 40%, 50% 40%, 65% 10%, 90% 20%;
    background-size: 0% 0%, 0% 0%, 0% 0%, 0% 0%, 0% 0%, 0% 0%;
  }
}
@keyframes bottomBubbles {
  0% {
    background-position: 10% -10%, 30% 10%, 55% -10%, 70% -10%, 85% -10%, 70% -10%, 70% 0%;
  }
  50% {
    background-position: 0% 80%, 20% 80%, 45% 60%, 60% 100%, 75% 70%, 95% 60%, 105% 0%;
  }
  100% {
    background-position: 0% 90%, 20% 90%, 45% 70%, 60% 110%, 75% 80%, 95% 70%, 110% 10%;
    background-size: 0% 0%, 0% 0%, 0% 0%, 0% 0%, 0% 0%, 0% 0%;
  }
}

</style>