document.addEventListener("DOMContentLoaded", function () {
  const slider = document.querySelector(".slides");
  let currentIndex = 0;
  const slideCount = slider.children.length;
  const slideWidth = 400;
  const slideInterval = 1500;

  setInterval(function () {
    currentIndex = (currentIndex + 1) % slideCount;
    slider.style.transform = `translateX(-${currentIndex * slideWidth}px)`;
  }, slideInterval);
});

document.addEventListener("DOMContentLoaded", function () {
  const slider2 = document.querySelector(".slides2");
  let currentIndex = 0;
  const slideCount = slider2.children.length;
  const slideWidth = 380;
  const slideInterval = 1500;

  setInterval(function () {
    currentIndex = (currentIndex + 1) % slideCount;
    slider2.style.transform = `translateX(-${currentIndex * slideWidth}px)`;
  }, slideInterval);
});
