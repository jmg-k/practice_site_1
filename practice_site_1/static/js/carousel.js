let slideIndex = 1;
let autoSlide = true;

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function goToSlide(n, el) {
  el.preventDefault()
  slideIndex = n;
  autoSlide = false;
  showSlides(slideIndex);
}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("dot");
  if (n == undefined) {n = slideIndex}

  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";

  if(autoSlide == true) {
    slideIndex++;
    setTimeout(showSlides, 3000);
  }
} 


function ready(callback){
  // in case the document is already rendered
  if (document.readyState!='loading') callback();
  // modern browsers
  else if (document.addEventListener) document.addEventListener('DOMContentLoaded', callback);
  // IE <= 8
  else document.attachEvent('onreadystatechange', function(){
      if (document.readyState=='complete') callback();
  });
}

ready(function(){
  showSlides(slideIndex);
  var slide_objs = document.querySelectorAll('.dots .dot');
  for (i = 0; i < slide_objs.length; ++i) {
    slide_objs[i].addEventListener('click', function(e){ goToSlide(e.target.getAttribute('data-slide'), e);});
  }

  var prev_btn = document.querySelector('.carousel .prev');
  prev_btn.addEventListener('click', function(e) { goToSlide(slideIndex-1, e)})

  var next_btn = document.querySelector('.carousel .next');
  next_btn.addEventListener('click', function(e) { goToSlide(slideIndex+1, e)})

});