let doc = parent.document;
doc.appending = false;

doc.removeMargin = function (currentWindow) {
    let iframe_parent = currentWindow.frameElement.parentNode
    iframe_parent.style.display = "none";
    iframe_parent.style.width = "unset";
    iframe_parent.style.height = "unset";
}

doc.removeMargin(window);

doc.addTokens = async function (id, classes, currentWindow) {
    doc.removeMargin(currentWindow);
    while (doc.appending) {
        await new Promise(resolve => setTimeout(resolve, 50));
    }

    doc.appending = true;
    let comp = currentWindow.frameElement.parentNode.nextSibling;
    let child = comp.querySelector(id);

    const script = document.createElement('script');
    script.src = 'https://unpkg.com/tw-to-css';
    document.head.appendChild(script);

    if (typeof twi === 'undefined') {
        await new Promise(resolve => script.onload = resolve);
    }

    let inlineCss = twi(classes);
    inlineCss = inlineCss.replaceAll(";", " !important;");
    child.style.cssText = inlineCss;
    doc.appending = false;
}