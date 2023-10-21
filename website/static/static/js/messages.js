document.addEventListener("DOMContentLoaded", function () {
  const flashes = document.querySelectorAll(
    ".flashes .error, .flashes .success"
  );

  flashes.forEach(function (flash) {
    setTimeout(function () {
      flash.style.display = "none";
    }, 5000);
  });
});
