function toggleText(button) {
    // get preview and full text elements
    const textPreview = button.previousElementSibling.previousElementSibling;
    const textFull = button.previousElementSibling;
  
    // check if full text is hidden or not
    const isHidden = textFull.style.display === "none";
  
    //toggle visibility for preview and full texts, also change text of button
    textPreview.style.display = isHidden ? "none" : "inline";
    textFull.style.display = isHidden ? "inline" : "none";
    button.innerHTML = isHidden ? "Show Less" : "Show More";
 }