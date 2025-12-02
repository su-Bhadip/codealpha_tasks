async function translateText() {
    const text = document.getElementById("inputText").value.trim();
    const source = document.getElementById("sourceLang").value;
    const target = document.getElementById("targetLang").value;
    const output = document.getElementById("outputText");

    if (!text) {
        output.innerText = "Please enter text.";
        return;
    }

    output.innerText = "Translating...";

    try {
        const url = `https://api.mymemory.translated.net/get?q=${encodeURIComponent(text)}&langpair=${source}|${target}`;

        const response = await fetch(url);
        const data = await response.json();

        if (data.responseData.translatedText) {
            output.innerText = data.responseData.translatedText;
        } else {
            output.innerText = "Error: No translation found.";
        }

    } catch (error) {
        output.innerText = "Error: Unable to translate.";
        console.error(error);
    }
}

function copyOutput() {
    const text = document.getElementById("outputText").innerText;
    navigator.clipboard.writeText(text);
}

function speakOutput() {
    const text = document.getElementById("outputText").innerText;
    const speech = new SpeechSynthesisUtterance(text);
    speech.lang = "en-IN";
    speechSynthesis.speak(speech);
}
