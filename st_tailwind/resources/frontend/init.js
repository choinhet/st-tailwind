let doc = parent.document;

doc.injectTw = function() {
    let head = doc.getElementsByTagName("head")[0];

    let cdn = doc.createElement("script");
    cdn.src = "https://cdn.tailwindcss.com";

    let twConfig = doc.createElement("script");
    twConfig.innerHMTL = "tailwind.config = {important: true, theme: {extend: {}}}";

    head.appendChild(cdn);
    head.appendChild(twConfig);
}


doc.reinjectTw = function () {
    const isTailwindPresent = Array
        .from(parent.document.scripts)
        .some(script => script.src && script.src.includes("tailwind")
        );

    if (!isTailwindPresent) {
        doc.injectTw();
    }
}

doc.removeMargin = function(currentWindow) {
    let iframe_parent = currentWindow.frameElement.parentNode
    iframe_parent.style.display = "none";
    iframe_parent.style.width = "unset";
    iframe_parent.style.height = "unset";
}

doc.injectTw();
setTimeout(doc.reinjectTw, timeout=50);
doc.removeMargin(window);
