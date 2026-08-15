/**
 * Background Service Worker
 * Routes text analysis requests to the live Render backend API.
 */

// Replace the placeholder below with your exact Render URL from Step 1
const API_ENDPOINT = "https://fake-news-detector-2-1jco.onrender.com/predict";

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === "ANALYZE_TEXT") {
    fetch(API_ENDPOINT, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        title: request.payload.title,
        text: request.payload.text,
        url: request.payload.url
      })
    })
    .then(response => {
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return response.json();
    })
    .then(data => {
      sendResponse({ status: "SUCCESS", data: data });
    })
    .catch(error => {
      console.error("Fetch error in background script:", error);
      sendResponse({ status: "ERROR", error: error.message });
    });

    return true; // Keeps the message channel open for async response
  }
});
