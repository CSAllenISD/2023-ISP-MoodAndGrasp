
(function () {
let currentQuestion = 0;
let questions;

function createQuestionElements(parent, surveyQuestionsData) {
    surveyQuestionsData.forEach((questionData, index) => {
        const questionElement = document.createElement('div');
        questionElement.classList.add('question');
        if (index === 0) questionElement.classList.add('active');

        const h3 = document.createElement('h3');
        h3.textContent = `Question ${index + 1}:`;
        questionElement.appendChild(h3);

        const p = document.createElement('p');
        p.textContent = questionData.question;
        questionElement.appendChild(p);

        const sliderContainer = document.createElement('div');
        sliderContainer.classList.add('slider-container');
        questionElement.appendChild(sliderContainer);

        const input = document.createElement('input');
        input.type = 'range';
        input.min = '1';
        input.max = '5';
        input.value = '1';
        input.classList.add('slider');
        input.id = `answerSlider${index + 1}`;
        sliderContainer.appendChild(input);

        const ul = document.createElement('ul');
        ul.classList.add('slider-labels');
        sliderContainer.appendChild(ul);

        questionData.dummyText.forEach((text, i) => {
            const li = document.createElement('li');
            li.setAttribute('data-text', text);
            li.textContent = `Image ${i + 1}`;
            ul.appendChild(li);
        });

        parent.appendChild(questionElement);
    });
    questions = document.querySelectorAll('.question');
    showQuestion(currentQuestion, questions);
}
const surveyQuestionsData = [
    {   
        type: 'emotional',
        question: 'How do you feel about our website design?',
        dummyText: ['Very Unhappy', 'Unhappy', 'Neutral', 'Happy', 'Very Happy']
    },
    {   
        type: 'emotional',
        question: 'How satisfied are you with our customer service?',
        dummyText: ['Very Unsatisfied', 'Unsatisfied', 'Neutral', 'Satisfied', 'Very Satisfied']
    },
    {   
        type: 'emotional',
        question: 'How likely are you to recommend our services to a friend?',
        dummyText: ['Not Likely', 'Unlikely', 'Neutral', 'Likely', 'Very Likely']
    },
    {   
        type: 'emotional',
        question: 'How would you rate your overall experience with us?',
        dummyText: ['Very Poor', 'Poor', 'Average', 'Good', 'Excellent']
    },
    {   
        type: 'statistical',
        question: 'How many times have you visited our website in the past month?',
        dummyText: ['0-1', '2-5', '6-10', '11-20', '21+']
    },
    {   
        type: 'statistical',
        question: 'How many products or services have you purchased from us?',
        dummyText: ['0', '1-2', '3-4', '5-6', '7+']
    },
    {   
        type: 'statistical',
        question: 'How long did it take for you to find what you were looking for on our website?',
        dummyText: ['< 1 min', '1-5 min', '6-15 min', '16-30 min', '> 30 min']
    },
    {   
        type: 'statistical',
        question: 'On a scale of 1-5, how would you rate the ease of navigation on our website?',
        dummyText: ['1', '2', '3', '4', '5']
    },
];
const questionsContainer = document.querySelector('.questions');
createQuestionElements(questionsContainer, surveyQuestionsData, questions);

function showQuestion(index, questions) {
    questions.forEach((question, i) => {
        if (i === index) {
            question.classList.add('active');
        } else {
            question.classList.remove('active');
        }
    });
}

function nextQuestion(questions) {
    if (currentQuestion < questions.length - 1) {
        currentQuestion++;
        showQuestion(currentQuestion, questions);
    }
}

function prevQuestion(questions) {
    if (currentQuestion > 0) {
        currentQuestion--;
        showQuestion(currentQuestion, questions);
    }
}

const nextBtn = document.querySelector("#nextBtn");
const prevBtn = document.querySelector("#prevBtn");
nextBtn.addEventListener("click", () => nextQuestion(questions));
prevBtn.addEventListener("click", () => prevQuestion(questions));


function updateSliderColor(slider) {
    let percentage = ((slider.value - slider.min) / (slider.max - slider.min)) * 100;
    let colorLeft = "#ff69b4";
    let colorRight = "#ffb6c1";
    let background = `linear-gradient(90deg, ${colorLeft} ${percentage}%, ${colorRight} ${percentage}%)`;
    slider.style.background = background;
}

document.querySelectorAll('.slider').forEach(slider => {
    updateSliderColor(slider);
    slider.addEventListener('input', () => updateSliderColor(slider));
});

function submitSliderData(surveyQuestionsData) {
    const sliderValues = [];

    document.querySelectorAll('.slider').forEach((slider, index) => {
        sliderValues.push({
            question: surveyQuestionsData[index].question,
            value: slider.value,
        });
    });

    // Replace this URL with the appropriate URL for your Django backend
    const url = '/submit_slider_data/';

    fetch(url, {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        // Add any required Django CSRF headers or authentication headers
    },
    body: JSON.stringify(sliderValues),
})
.then(response => response.json())
.then(data => {
    if (data.status === 'success') {
        console.log('Data saved successfully');
        // Redirect to a success page or show a success message
    } else {
        console.error('Error saving data');
            // Show an error message
        }
    })
    .catch((error) => {
        console.error('Error:', error);
        // Show an error message
    });
}
const submitBtn = document.querySelector('#submitBtn');
submitBtn.addEventListener('click', () => submitSliderData(surveyQuestionsData));

})();
