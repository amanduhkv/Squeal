import React, { useEffect, useState } from 'react'
import { useLocation } from 'react-router-dom';
import search from '../../icons/search.svg';

const HomeBanner = () => {

  // ******************** Background Image Logic *******************************
  useEffect(() => {
    let timeout1;
    let timeout2;
    let timeout3;
    let timeout4;
    function bgShift_1() {
      if (!document.querySelector(".img1")) return null;
      timeout1 = setTimeout(() => {
          document.querySelector(".img1").style.opacity = 0;
          document.querySelector(".img2").style.opacity = 1;
          document.querySelector(".img3").style.opacity = 1;
          order(["-3", "-1", "-2"], () => { bgShift_2() }, 1500);
      }, 4500);
    }
    function bgShift_2() {
      if (!document.querySelector(".img1")) return null;
      timeout2 = setTimeout(() => {
          document.querySelector(".img1").style.opacity = 1;
          document.querySelector(".img2").style.opacity = 0;
          document.querySelector(".img3").style.opacity = 1;
          order(["-2", "-3", "-1"], () => { bgShift_3() }, 1500);
      }, 4500);
    }
    function bgShift_3() {
      if (!document.querySelector(".img1")) return null;
      timeout3 = setTimeout(() => {
          document.querySelector(".img1").style.opacity = 1;
          document.querySelector(".img2").style.opacity = 1;
          document.querySelector(".img3").style.opacity = 0;
          order(["-1", "-2", "-3"], () => { bgShift_1() }, 1500);
      }, 4500);
    }
    function order(arr, cb, time) {
      timeout4 = setTimeout(() => {
          document.querySelector(".img1").style.zIndex = arr[0];
          document.querySelector(".img2").style.zIndex = arr[1];
          document.querySelector(".img3").style.zIndex = arr[2];
          cb();
      }, time);
    }
    bgShift_1();
    return () => {
      clearTimeout(timeout1);
      clearTimeout(timeout2);
      clearTimeout(timeout3);
      clearTimeout(timeout4);
    }
  }, [])

  // ***************************************************************************

  return (
    <div className='homepage-banner-container'>
      <div className="bg-img img1">
        <div className='homepage-buttons'>
          <h1 className='homepage-questions'>
            Meet your soy mate
          </h1>
          <button className='homepage-button sushi-button'>
            <img src={search} className='mag-glass' />
            <span className='homepage-button-span'>Japanese</span>
          </button>
        </div>
      </div>
      <div className="bg-img img2">
        <div className='homepage-buttons'>
          <h1 className='homepage-questions'>
            Getting jjigae with it
          </h1>
          <button className='homepage-button sushi-button'>
            <img src={search} className='mag-glass' />
            <span className='homepage-button-span'>Korean</span>
          </button>
        </div>
      </div>
      <div className="bg-img img3">
        <div className='homepage-buttons'>
          <h1 className='homepage-questions'>
            Un-phở-gettable meals
          </h1>
          <button className='homepage-button sushi-button'>
            <img src={search} className='mag-glass' />
            <span className='homepage-button-span'>Vietnamese</span>
          </button>
        </div>
      </div>
    </div>
  )
}

export default HomeBanner
