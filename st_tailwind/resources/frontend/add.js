let doc = parent.document;
doc.removeMargin(window);
doc.reinjectTw();
let comp = window.frameElement.parentNode.nextSibling;
let child = comp.querySelector("%ID%");
let tokens = "%CLASSES%".split(" ");
child.classList.add(...tokens)
