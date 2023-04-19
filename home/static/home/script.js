const slider = document.querySelector(".slider");
const form = document.getElementById('survey-form');
const moodImages = document.querySelectorAll(".slider-images-container img[data-position='mood']");
const graspImages = document.querySelectorAll(".slider-images-container img[data-position='grasp']");
const moodInput = document.getElementById('id_mood');
const graspInput = document.getElementById('id_grasp');
window.onload = function() {
  if(slider && form){
    slider.addEventListener("input", function () {
      let moodValue = 0;
      let graspValue = 0;
      const sliderValue = this.value;

      // Calculate mood value
      if (sliderValue === 1) {
        moodValue = -10;
      } else if (sliderValue === 2) {
        moodValue = -5;
      } else if (sliderValue === 3) {
        moodValue = 0;
      } else if (sliderValue === 4) {
        moodValue = 5;
      } else if (sliderValue === 5) {
        moodValue = 10;
      }

      // Calculate grasp value
      if (sliderValue === 1) {
        graspValue = -10;
      } else if (sliderValue === 2) {
        graspValue = -5;
      } else if (sliderValue === 3) {
        graspValue = 0;
      } else if (sliderValue === 4) {
        graspValue = 5;
      } else if (sliderValue === 5) {
        graspValue = 10;
      }

      // Set mood and grasp values to inputs



      moodInput.value = parseInt(moodInput.value) + moodValue;
      graspInput.value = parseInt(graspInput.value) + graspValue;
      
    });

    $.ajax({
      type: "POST",
      url: '/survey',
      data: {
        "mood": 5,
        "grasp": 10
      },
      dataType: "json",
      success: function(data) {
        alert("successfull")
      },
      failure: function(error) {
        alert("failure");
      }

    });


  }

};