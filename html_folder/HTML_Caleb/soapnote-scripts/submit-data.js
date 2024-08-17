/*
TextAreas for Physical Exam, Assessment section, & Subjective
Inputs for Vital Signs & test results

Instructions:
- call ScrapeInputs to scrape all data from text boxes/text areas/text controllers
- have the listener function below that to detect when the submit button is clicked
- call scrape inputs for the returned dictionary
- send dictionary off to databse

Future directions:
- retrieve dictionary from database for every unique ID of each user
*/

function scrapeInputs() {
    let inputsDictionary = {};

    const textInputs = document.querySelectorAll('textarea, input[type="text"]');

    for (const input of textInputs) {
        inputsDictionary[input.id] = input.value;
    }

    return inputsDictionary;
}

document.addEventListener("DOMContentLoaded", function () {
    // let the document load first
    const formButton = document.getElementById("submit-button");

    formButton.onclick = function (event) {
        event.preventDefault(); // temporarily prevents reloading of the page, remove if need be        

        const emrData = scrapeInputs();

        console.log(emrData);
        // TODO submit data to api endpoint
    };
});
