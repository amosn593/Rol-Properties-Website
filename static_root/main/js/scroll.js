window.addEventListener("scroll", function () {
  let navheader = document.getElementById("scroll");
  navheader.classList.toggle("topnav-scroll", window.screenY > 0);
});
