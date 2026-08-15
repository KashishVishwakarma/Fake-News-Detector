/**
 * Service Worker script managing API communications between content scripts,
 * popup interfaces, and the external FastAPI inference server.
 */

const API_ENDPOINT = "http://localhost:8000/predict";

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
        throw new Error(`HTTP network error: status ${response.status}`);
      }
      return response.json();
    })
    .then(data => {
      sendResponse({ status: "SUCCESS", data: data });
    })
    .catch(error => {
      console.error("Background service worker fetch error:", error);
      sendResponse({ status: "ERROR", error: error.message });
    });

    return true;
  }
});
