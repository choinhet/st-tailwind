// noinspection JSUnresolvedReference

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
    }
}

function removeUnwantedMargin() {
    let iframe_parent = window.frameElement.parentNode
    iframe_parent.style.display = "none";
    iframe_parent.style.width = "unset";
    iframe_parent.style.height = "unset";
}

function addClassesToElement() {
    let child = window.frameElement.parentNode.previousSibling.previousSibling;
    let element = Array.from(child.getElementsByTagName("*")).toSpliced(0, 0, child)[Number("%IDX%")]
    let tokens = "%CLASSES%".split(" ");
    element.classList.add(...tokens)
}

setTimeout(() => {
    removeUnwantedMargin()
    checkAndInjectTailwind()
    addClassesToElement()
}, 350)
