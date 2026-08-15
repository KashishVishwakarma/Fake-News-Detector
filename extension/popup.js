document.getElementById("analyze-btn").addEventListener("click", async () => {
  const btn = document.getElementById("analyze-btn");
  const loader = document.getElementById("loader");
  const resultsCard = document.getElementById("results-card");
  const errorBox = document.getElementById("error-message");

  btn.classList.add("hidden");
  errorBox.classList.add("hidden");
  resultsCard.classList.add("hidden");
  loader.classList.remove("hidden");

  const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });

  if (!tab) {
    showError("No active browser tab found.");
    return;
  }

  chrome.tabs.sendMessage(tab.id, { action: "EXECUTE_PAGE_ANALYSIS" }, (response) => {
    loader.classList.add("hidden");
    btn.classList.remove("hidden");

    if (chrome.runtime.lastError) {
      showError("Unable to analyze page. Please reload the tab and try again.");
      return;
    }

    if (response && response.status === "SUCCESS") {
      renderResults(response.data);
    } else {
      showError(response?.message || "Failed to analyze page content.");
    }
  });
});

function renderResults(data) {
  const resultsCard = document.getElementById("results-card");
  const verdictTag = document.getElementById("verdict-tag");
  const confidenceVal = document.getElementById("confidence-val");
  const riskVal = document.getElementById("risk-val");
  const fakeProb = document.getElementById("fake-prob");
  const realProb = document.getElementById("real-prob");

  const isReal = data.verdict === "REAL";
  verdictTag.innerText = data.verdict;
  verdictTag.className = `tag ${isReal ? "tag-real" : "tag-fake"}`;

  confidenceVal.innerText = `${data.metrics.confidence_score}% Confident`;
  riskVal.innerText = data.risk_level;
  fakeProb.innerText = `${(data.metrics.fake_probability * 100).toFixed(1)}%`;
  realProb.innerText = `${(data.metrics.real_probability * 100).toFixed(1)}%`;

  resultsCard.classList.remove("hidden");
}

function showError(msg) {
  const btn = document.getElementById("analyze-btn");
  const loader = document.getElementById("loader");
  const errorBox = document.getElementById("error-message");

  loader.classList.add("hidden");
  btn.classList.remove("hidden");
  errorBox.innerText = msg;
  errorBox.classList.remove("hidden");
}
