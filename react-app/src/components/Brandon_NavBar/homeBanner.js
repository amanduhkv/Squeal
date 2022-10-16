import React, { useState } from 'react'

const HomeBanner = () => {

  // ******************** Background Image Logic *******************************
  function bgShift_1() {
    setTimeout(() => {
        document.querySelector(".img1").style.opacity = 0;
        document.querySelector(".img2").style.opacity = 1;
        document.querySelector(".img3").style.opacity = 1;
        order(["-3", "-1", "-2"], () => { bgShift_2() }, 1500);
    }, 4500);
  }
  function bgShift_2() {
    setTimeout(() => {
        document.querySelector(".img1").style.opacity = 1;
        document.querySelector(".img2").style.opacity = 0;
        document.querySelector(".img3").style.opacity = 1;
        order(["-2", "-3", "-1"], () => { bgShift_3() }, 1500);
    }, 4500);
  }
  function bgShift_3() {
    setTimeout(() => {
        document.querySelector(".img1").style.opacity = 1;
        document.querySelector(".img2").style.opacity = 1;
        document.querySelector(".img3").style.opacity = 0;
        order(["-1", "-2", "-3"], () => { bgShift_1() }, 1500);
    }, 4500);
  }
  function order(arr, cb, time) {
    setTimeout(() => {
        document.querySelector(".img1").style.zIndex = arr[0];
        document.querySelector(".img2").style.zIndex = arr[1];
        document.querySelector(".img3").style.zIndex = arr[2];
        cb();
    }, time);
  }
  bgShift_1();
  // ***************************************************************************

  return (
    <div className='homepage-banner-container'>
      <img class="bg-img img1" src="https://i.imgur.com/pQ50uP5.jpg" />
      <img class="bg-img img2" src="https://i.imgur.com/LLEGfPN.jpg" />
      <img class="bg-img img3" src="https://i.imgur.com/UOv3X1b.jpg" />
    </div>
  )
}

export default HomeBanner
