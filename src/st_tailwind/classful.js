SELECTOR = "%SELECTOR%"
TEXT = "%TEXT%"
CLASSES = "%CLASSES%"

function contains(selector, text) {
    let elements = parent.document.querySelectorAll(selector);
    return Array.prototype.filter.call(elements, function (element) {
        return RegExp(text).test(element.textContent);
    })[0];
}

function _contains(selector, text) {
    let elements = parent.document.querySelectorAll(selector);
    return Array.prototype.filter.call(elements, function (element) {
        return RegExp(text).test(element.srcdoc);
    })[0];
}

function checkAndInjectTailwind() {
    const isTailwindPresent = Array.from(parent.document.styleSheets).some(styleSheet =>
        styleSheet.href && styleSheet.href.includes("tailwind")
    );
    if (!isTailwindPresent) {
        const script = document.createElement('script');
        script.src = "https://cdn.tailwindcss.com";
        parent.document.head.appendChild(script);
        setTimeout(()=>{
            parent.tailwind.config = {important: true, theme: {extend: {}}}
        }, 250)
        console.log("Tailwind CSS has been injected into the document.");
    } else {
        console.log("Tailwind CSS is already present in the document.");
    }
}

function removeUnwantedMargin(selector) {
    let iframe = _contains("iframe", selector)
    let parent = iframe.parentElement.style;
    parent.display = "none";
    parent.width = "unset";
    parent.height = "unset";
}

function addClassesToElement(selector, text, classes) {
    let element = contains(selector, text)
    if (element == null) {
        console.log("Could not find element using query", selector)
        console.log("And text", text)
    } else {
        element.classList.add(classes)
    }
}

removeUnwantedMargin(SELECTOR)
checkAndInjectTailwind()
addClassesToElement(SELECTOR, TEXT, CLASSES)
