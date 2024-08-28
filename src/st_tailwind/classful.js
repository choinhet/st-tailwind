function checkAndInjectTailwind() {
    const isTailwindPresent = Array
        .from(parent.document.scripts)
        .some(script => script.src && script.src.includes("tailwind")
        );

    if (!isTailwindPresent) {
        const script = document.createElement('script');
        script.src = "https://cdn.tailwindcss.com";
        parent.document.head.appendChild(script);
        setTimeout(() => {
            parent.tailwind.config = {important: true, theme: {extend: {}}}
        }, 250)
    } else {
    }
}

function removeUnwantedMargin() {
    let iframe_parent = window.frameElement.parentNode
    iframe_parent.style.display = "none";
    iframe_parent.style.width = "unset";
    iframe_parent.style.height = "unset";
}

function addClassesToElement() {
    let element = [...parent.document.querySelectorAll("%SELECTOR%")]["%POS%"];
    if (element == null) {
    } else {
        let tokens = "%CLASSES%".split(" ");
        element.classList.add(...tokens)
    }
}

setTimeout(() => {
    removeUnwantedMargin()
    checkAndInjectTailwind()
    addClassesToElement()
}, 350)
