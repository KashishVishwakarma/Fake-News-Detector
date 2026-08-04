// Wait until the page is fully loaded
document.addEventListener("DOMContentLoaded", function () {

    const form = document.getElementById("newsForm");
    const button = document.getElementById("predictBtn");
    const loading = document.getElementById("loading");
    const textarea = document.getElementById("news");

    form.addEventListener("submit", function (event) {

        const news = textarea.value.trim();

        // Prevent empty submission
        if (news.length === 0) {
            event.preventDefault();
            alert("Please enter a news article.");
            return;
        }

        // Show loading animation
        loading.style.display = "block";

        // Disable button
        button.disabled = true;
        button.innerHTML = "Analyzing...";

    });

    // Character counter (optional)
    const counter = document.createElement("p");
    counter.style.textAlign = "right";
    counter.style.marginTop = "8px";
    counter.style.color = "#666";
    counter.innerHTML = "Characters: 0";

    textarea.parentNode.insertBefore(counter, textarea.nextSibling);

    textarea.addEventListener("input", function () {
        counter.innerHTML = "Characters: " + textarea.value.length;
    });

});
