/**
 * Adds text to a text area given the ID of the textbox and the text added
 * @param text The text to add
 * @param textAreaId The ID of the text area
 */
const addFillInText = (text, textAreaId) => {
    const textarea = document.getElementById(textAreaId)

    if (textarea.value === '')
    {
        textarea.value += text
        return
    }

    textarea.value += ` + ${text}`;
}


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
    let textareas = document.getElementsByTagName('textarea');
    let textboxes = document.querySelectorAll('input[type="text"]');

    for (let i = 0; i < textareas.length; i++) {
        let textarea = textareas[i];
        inputsDictionary[textarea.id] = textarea.value;
    }
    
    for (let i = 0; i < textboxes.length; i++) {
        let textbox = textboxes[i];
        inputsDictionary[textbox.id] = textbox.value;
    }
    return inputsDictionary
}

document.addEventListener('DOMContentLoaded', function() { //let the document load first
    var form = document.getElementById('submit-button');
    form.onclick = function(event) {
        event.preventDefault(); // temporarily prevents reloading of the page, remove if need be

        console.log(scrapeInputs());
    }
});