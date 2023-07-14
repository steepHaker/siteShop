document.addEventListener("DOMContentLoaded", function() {
    const enlargeImages = document.querySelectorAll(".enlarge-image");
    enlargeImages.forEach(function(image) {
      image.addEventListener("click", function(event) {
        event.preventDefault();
        const enlargedImage = document.createElement("img");
        enlargedImage.src = this.href;
        enlargedImage.classList.add("enlarged-image");
        const closeOverlay = document.createElement("div");
        closeOverlay.classList.add("close-overlay");
        closeOverlay.addEventListener("click", function() {
          document.body.removeChild(enlargedImage);
          document.body.removeChild(closeOverlay);
        });
        document.body.appendChild(enlargedImage);
        document.body.appendChild(closeOverlay);
      });
    });
  });

  