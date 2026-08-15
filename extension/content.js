/**
 * Content script running within active web pages.
 * Parses DOM paragraphs and injects floating verification badges onto the page.
 */

(function () {
  if (window.hasTruthShieldInjected) return;
  window.hasTruthShieldInjected = true;

  function extractArticleContent() {
    const headline = document.querySelector("h1")?.innerText || document.title || "";
    
    const paragraphs = Array.from(document.querySelectorAll("article p, main p, p"))
      .map(p => p.innerText.trim())
      .filter(text => text.length > 30);

    const fullText = paragraphs.join("\n\n");
    return { title: headline, text: fullText, url: window.location.href };
  }

  function injectBadgeOverlay(data) {
    const existingBadge = document.getElementById("truthshield-floating-badge");
    if (existingBadge) existingBadge.remove();

    const badge = document.createElement("div");
    badge.id = "truthshield-floating-badge";
    
    const isReal = data.verdict === "REAL";
    const badgeColor = isReal ? "#10B981" : "#EF4444";
    const statusText = isReal ? "Likely Authentic" : "Potential Misinformation";

    badge.style.backgroundColor = badgeColor;
    badge.innerHTML = `
      <div class="ts-badge-content">
        <span class="ts-icon">${isReal ? "✓" : "⚠"}</span>
        <span class="ts-text">${statusText} (${data.metrics.confidence_score}%)</span>
        <button class="ts-close-btn" id="ts-close">&times;</button>
      </div>
    `;

    document.body.appendChild(badge);

    document.getElementById("ts-close").addEventListener("click", () => {
      badge.remove();
    });
  }

  chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === "EXECUTE_PAGE_ANALYSIS") {
      const payload = extractArticleContent();

      if (!payload.text || payload.text.length < 50) {
        sendResponse({ status: "ERROR", message: "Insufficient main body text found on this page." });
        return true;
      }

      chrome.runtime.sendMessage(
        { action: "ANALYZE_TEXT", payload: payload },
        (response) => {
          if (response && response.status === "SUCCESS") {
            injectBadgeOverlay(response.data);
            sendResponse({ status: "SUCCESS", data: response.data });
          } else {
            sendResponse({ status: "ERROR", message: response?.error || "Page analysis failed." });
          }
        }
      );
      return true;
    }
  });
})();
