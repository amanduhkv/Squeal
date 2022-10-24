import React, { useEffect, useState } from 'react'
import search from '../../icons/search.svg';
import './NavBar.css';
import brokenImgPig from '../../icons/broken-img-pig.png';

const HomeBanner = () => {
    const [isLoaded, setIsLoaded] = useState(false);

    // ******************** Background Image Logic *******************************
    useEffect(() => {
        let timeout1;
        let timeout2;
        let timeout3;
        let timeout4;

        function bgShift_1() {
            timeout1 = setTimeout(() => {
                if (document.querySelector(".img1")) {
                    document.querySelector(".img1").style.opacity = 0;
                    document.querySelector(".img2").style.opacity = 1;
                    document.querySelector(".img3").style.opacity = 1;
                    order(["-3", "-1", "-2"], () => { bgShift_2() }, 1500);
                }
            }, 4500);
        }
        function bgShift_2() {
            timeout2 = setTimeout(() => {
                if (document.querySelector(".img1")) {
                    document.querySelector(".img1").style.opacity = 1;
                    document.querySelector(".img2").style.opacity = 0;
                    document.querySelector(".img3").style.opacity = 1;
                    order(["-2", "-3", "-1"], () => { bgShift_3() }, 1500);
                }
            }, 4500);
        }
        function bgShift_3() {
            timeout3 = setTimeout(() => {
                if (document.querySelector(".img1")) {
                    document.querySelector(".img1").style.opacity = 1;
                    document.querySelector(".img2").style.opacity = 1;
                    document.querySelector(".img3").style.opacity = 0;
                    order(["-1", "-2", "-3"], () => { bgShift_1() }, 1500);
                }
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
        setIsLoaded(true);
        return () => {
            clearTimeout(timeout1);
            clearTimeout(timeout2);
            clearTimeout(timeout3);
            clearTimeout(timeout4);
        }
    }, [])

    // ***************************************************************************
    if (!isLoaded) return (
        <div className='loading-container'>
            <img className='squeal-loading' src='https://i.imgur.com/NoEXVTv.gif' alt='loading' onError={e => e.target.src=brokenImgPig} />
        </div>
    );
    return (
        <div className='homepage-banner-container'>
            <div className="bg-img img1">
                <div className='homepage-buttons'>
                    <h1 className='homepage-questions'>
                        Meet your soy mate
                    </h1>
                    <a className='homeBanner-link' href='/biz?type=japanese'>
                        <button className='homepage-button sushi-button'>
                            <img src={search} alt='search' className='mag-glass' onError={e => e.target.src=brokenImgPig} />
                            <span className='homepage-button-span'>Japanese</span>
                        </button></a>
                </div>
            </div>
            <div className="bg-img img2">
                <div className='homepage-buttons'>
                    <h1 className='homepage-questions'>
                        Getting jjigae with it
                    </h1>
                    <a className='homeBanner-link' href='/biz?type=korean'>
                        <button className='homepage-button sushi-button'>
                            <img src={search} alt='search' className='mag-glass' onError={e => e.target.src=brokenImgPig} />
                            <span className='homepage-button-span'>Korean</span>
                        </button></a>
                </div>
            </div>
            <div className="bg-img img3">
                <div className='homepage-buttons'>
                    <h1 className='homepage-questions'>
                        Un-phở-gettable meals
                    </h1>
                    <a className='homeBanner-link' href='/biz?type=vietnamese'>
                        <button className='homepage-button sushi-button'>
                            <img src={search} alt='search' className='mag-glass' onError={e => e.target.src=brokenImgPig} />
                            <span className='homepage-button-span'>Vietnamese</span>
                        </button></a>
                </div>
            </div>
        </div>
    )
}

export default HomeBanner;
