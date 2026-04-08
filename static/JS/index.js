// Simple button feedback
document.querySelector(".btn").addEventListener("click", () => {
  console.log("Get Started clicked");
});
window.addEventListener("load", () => {
  const el = document.querySelector(".hero-text");
  if (el) {
    // thoda delay taaki page paint ho jaaye
    setTimeout(() => el.classList.add("animate"), 100);
  }
});
// JS/index.js
const text = "Kothiwal Institute of Technologies & Professional Studies";
const el = document.getElementById("typeText");
let i = 0;

if (el) {
  el.textContent = "";
  const timer = setInterval(() => {
    el.textContent += text.charAt(i);
    i++;
    if (i >= text.length) clearInterval(timer);
  }, 40); // speed control
}

document.getElementById("searchInput").addEventListener("keypress", function(e) {
  if (e.key === "Enter") {
    console.log("Searching:", this.value);
  }
});