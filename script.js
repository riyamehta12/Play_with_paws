const form = document.getElementById("contact-form");
const successMessage = document.getElementById("success-message");

form.addEventListener("submit", function(event) {
  event.preventDefault(); // Prevent default form submission behavior

  // Simulate form submission (replace with actual submission logic if needed)
  console.log("Form submitted!");

  // Display the "Thank You" message
  successMessage.style.display = "block";
  form.reset(); // Reset the form after successful submission
});
