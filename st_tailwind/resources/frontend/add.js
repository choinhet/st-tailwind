let doc = parent.document;
doc.removeMargin(window);
doc.reinjectTw();

async function addTokens() {
    console.log("Appending: ", doc.appending);
    while (doc.appending) {
        await new Promise(resolve => setTimeout(resolve, 500));
    }
    doc.appending = true;
    let comp = window.frameElement.parentNode.nextSibling;
    let child = comp.querySelector("%ID%");
    let tokens = "%CLASSES%".split(" ");

    // Wait for Tailwind to load
    await new Promise(resolve => setTimeout(resolve, 1000));

    // Create temporary container and element in parent document
    const container = doc.createElement('div');
    const temp = doc.createElement('div');
    container.style.visibility = 'hidden';
    container.style.position = 'absolute';
    container.style.width = '100%';
    container.appendChild(temp);
    doc.body.appendChild(container);

    // Copy the original element's content and dimensions
    temp.innerHTML = child.innerHTML;
    temp.style.width = getComputedStyle(child).width;
    temp.style.height = getComputedStyle(child).height;

    // Log styles for each class
    const classStyles = {};
    let accumulatedStyles = {};

    // Get initial state without any classes
    const initialStyles = {};
    const initial = doc.defaultView.getComputedStyle(temp);
    for (const prop of initial) {
        initialStyles[prop] = initial.getPropertyValue(prop);
    }

    for (const token of tokens) {
        temp.className = '';

        // If this is a compound style (like flex-row), apply the previous token first
        if (token.includes('-')) {
            const baseClass = token.split('-')[0];
            if (tokens.includes(baseClass)) {
                temp.classList.add(baseClass);
                await new Promise(resolve => setTimeout(resolve, 50));
            }
        }

        // Add current token and measure changes
        temp.classList.add(token);
        await new Promise(resolve => setTimeout(resolve, 50));

        const after = doc.defaultView.getComputedStyle(temp);

        // Compare against initial state to catch all changes
        const changes = {};
        for (const prop of after) {
            const newValue = after.getPropertyValue(prop);
            if (newValue !== initialStyles[prop]) {
                changes[prop] = newValue;
            }
        }

        if (Object.keys(changes).length > 0) {
            classStyles[token] = changes;
            Object.assign(accumulatedStyles, changes);
        }
    }

    console.log("Final style changes per class:", classStyles);
    console.log("Stringified style changes:", JSON.stringify(classStyles, null, 2));
    console.log("Stringified class changes:", JSON.stringify(accumulatedStyles, null, 2));

    container.remove();

    // Apply accumulated styles
    for (const [prop, value] of Object.entries(accumulatedStyles)) {
        if (value && !prop.startsWith('perspective') && !prop.startsWith('transform-origin')) {
            child.style[prop] = value;
        }
    }
    await new Promise(resolve => setTimeout(resolve, 500));
    doc.appending = false;
}

addTokens().then(() => {
    console.log("Done");
});
