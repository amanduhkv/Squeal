import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { NavLink } from "react-router-dom";
import { getAllBiz } from '../../store/businesses';

import x from '../../icons/all-biz-page/x.svg';
import check from '../../icons/all-biz-page/check.svg';
import txtbub from '../../icons/all-biz-page/text-bubble.svg';
import './Biz.css';
import { getBusinessReviews } from "../../store/reviews";

export default function Biz() {
    const biz = useSelector(state => state.businesses.allBusinesses);
    const bizArr = Object.values(biz);
    const dispatch = useDispatch();

    let current_time;
    const settingTime = () => {
        const today = new Date();
        let hours = today.getHours().toString()
        let mins = today.getMinutes().toString()
        if (hours.length === 1) hours = "0" + hours;
        if (mins.length === 1) mins = "0" + mins;
        return hours + mins
    }
    current_time = settingTime()

    const time_conversion = (time) => {
        if(Number(time) > 1200) {
            time = time - 1200
        }
        let nums = time.toString().split('')

        if(nums.length === 3) return nums[0] + ':' + nums[1] + nums[2]
        if(nums.length === 4) return nums[0] + nums[1] + ':' + nums[2] + nums[3]
    }


    useEffect(() => {
        dispatch(getAllBiz())
    }, [dispatch])

    return (
        <main>
            <br></br>
            <br></br>
            <br></br>
            <h1>Best Type Near Me in City, State</h1>
            <ol>
                {bizArr.map(biz => (
                    <div className="biz-box">
                        <div className="biz-img-box" >
                            <img id='biz-img' src={biz.Business_Images[0].url} />
                        </div>
                        <div className="biz-info-box">
                            <li id='biz-title'>
                                <NavLink id='biz-title-1' to={`/biz/${biz.id}`}>
                                    {biz.name}
                                </NavLink>
                            </li>
                            <div id='biz-rev-info'>
                                <div id='rev-stars'>
                                    <div className='review-card-stars'>
                                        {/* FIRST STAR */}
                                        <svg className='first-star' width="20" height="20" viewBox="0 0 20 20">
                                            <path fill={biz.avg_rating >= 4.8 ? "rgba(251,67,60,1)" : biz.avg_rating >= 4.3 ? 'rgba(255, 100, 61, 1)' : biz.avg_rating >= 3.8 ? 'rgba(255, 100, 61, 1)' : biz.avg_rating >= 3.3 ? 'rgba(255, 135, 66, 1)' : biz.avg_rating >= 2.8 ? 'rgba(255, 135, 66, 1)' : biz.avg_rating >= 2.3 ? 'rgba(255, 173, 72, 1)' : biz.avg_rating >= 1.8 ? 'rgba(255, 173, 72, 1)' : biz.avg_rating >= 1.3 ? 'rgba(255, 204, 75, 1)' : 'rgba(255, 204, 75, 1)'}
                                                d="M0 4C0 1.79086 1.79086 0 4 0H10V20H4C1.79086 20 0 18.2091 0 16V4Z">
                                            </path>
                                            <path fill={biz.avg_rating >= 4.8 ? "rgba(251,67,60,1)" : biz.avg_rating >= 4.3 ? 'rgba(255, 100, 61, 1)' : biz.avg_rating >= 3.8 ? 'rgba(255, 100, 61, 1)' : biz.avg_rating >= 3.3 ? 'rgba(255, 135, 66, 1)' : biz.avg_rating >= 2.8 ? 'rgba(255, 135, 66, 1)' : biz.avg_rating >= 2.3 ? 'rgba(255, 173, 72, 1)' : biz.avg_rating >= 1.8 ? 'rgba(255, 173, 72, 1)' : biz.avg_rating >= 1.3 ? 'rgba(255, 204, 75, 1)' : 'rgba(255, 204, 75, 1)'}
                                                d="M20 4C20 1.79086 18.2091 0 16 0H10V20H16C18.2091 20 20 18.2091 20 16V4Z">
                                            </path>
                                            <path fill="white" fill-rule="evenodd" clip-rule="evenodd"
                                                d="M10 13.3736L12.5949 14.7111C12.7378 14.7848 12.9006 14.8106 13.0593
                                14.7847C13.4681 14.718 13.7454 14.3325 13.6787 13.9237L13.2085 11.0425L15.2824
                                8.98796C15.3967 8.8748 15.4715 8.72792 15.4959 8.569C15.5588 8.15958 15.2779
                                7.77672 14.8685 7.71384L11.983 7.2707L10.6699 4.66338C10.5975 4.51978 10.481
                                4.40322 10.3374 4.33089C9.96742 4.14458 9.51648 4.29344 9.33017 4.66338L8.01705
                                7.2707L5.13157 7.71384C4.97265 7.73825 4.82577 7.81309 4.71261 7.92731C4.42109
                                8.22158 4.42332 8.69645 4.71759 8.98796L6.79152 11.0425L6.32131 13.9237C6.29541
                                14.0824 6.3212 14.2452 6.39486 14.3881C6.58464 14.7563 7.03696 14.9009 7.40514
                                14.7111L10 13.3736Z">
                                            </path>
                                        </svg>
                                        {/* SECOND STAR */}
                                        <svg className='middle-star' width="20" height="20" viewBox="0 0 20 20">
                                            <path fill={biz.avg_rating >= 4.8 ? "rgba(251,67,60,1)" : biz.avg_rating >= 4.3 ? 'rgba(255, 100, 61, 1)' : biz.avg_rating >= 3.8 ? 'rgba(255, 100, 61, 1)' : biz.avg_rating >= 3.3 ? 'rgba(255, 135, 66, 1)' : biz.avg_rating >= 2.8 ? 'rgba(255, 135, 66, 1)' : biz.avg_rating >= 2.3 ? 'rgba(255, 173, 72, 1)' : biz.avg_rating >= 1.8 ? 'rgba(255, 173, 72, 1)' : biz.avg_rating >= 1.3 ? 'rgba(255, 204, 75, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                                d="M0 4C0 1.79086 1.79086 0 4 0H10V20H4C1.79086 20 0 18.2091 0 16V4Z">
                                            </path>
                                            <path fill={biz.avg_rating >= 4.8 ? "rgba(251,67,60,1)" : biz.avg_rating >= 4.3 ? 'rgba(255, 100, 61, 1)' : biz.avg_rating >= 3.8 ? 'rgba(255, 100, 61, 1)' : biz.avg_rating >= 3.3 ? 'rgba(255, 135, 66, 1)' : biz.avg_rating >= 2.8 ? 'rgba(255, 135, 66, 1)' : biz.avg_rating >= 2.3 ? 'rgba(255, 173, 72, 1)' : biz.avg_rating >= 1.8 ? 'rgba(255, 173, 72, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                                d="M20 4C20 1.79086 18.2091 0 16 0H10V20H16C18.2091 20 20 18.2091 20 16V4Z">
                                            </path>
                                            <path fill="white" fill-rule="evenodd" clip-rule="evenodd"
                                                d="M10 13.3736L12.5949 14.7111C12.7378 14.7848 12.9006 14.8106 13.0593
                                14.7847C13.4681 14.718 13.7454 14.3325 13.6787 13.9237L13.2085 11.0425L15.2824
                                8.98796C15.3967 8.8748 15.4715 8.72792 15.4959 8.569C15.5588 8.15958 15.2779
                                7.77672 14.8685 7.71384L11.983 7.2707L10.6699 4.66338C10.5975 4.51978 10.481
                                4.40322 10.3374 4.33089C9.96742 4.14458 9.51648 4.29344 9.33017 4.66338L8.01705
                                7.2707L5.13157 7.71384C4.97265 7.73825 4.82577 7.81309 4.71261 7.92731C4.42109
                                8.22158 4.42332 8.69645 4.71759 8.98796L6.79152 11.0425L6.32131 13.9237C6.29541
                                14.0824 6.3212 14.2452 6.39486 14.3881C6.58464 14.7563 7.03696 14.9009 7.40514
                                14.7111L10 13.3736Z">
                                            </path>
                                        </svg>
                                        {/* THIRD STAR */}
                                        <svg className='middle-star' width="20" height="20" viewBox="0 0 20 20">
                                            <path fill={biz.avg_rating >= 4.8 ? "rgba(251,67,60,1)" : biz.avg_rating >= 4.3 ? 'rgba(255, 100, 61, 1)' : biz.avg_rating >= 3.8 ? 'rgba(255, 100, 61, 1)' : biz.avg_rating >= 3.3 ? 'rgba(255, 135, 66, 1)' : biz.avg_rating >= 2.8 ? 'rgba(255, 135, 66, 1)' : biz.avg_rating >= 2.3 ? 'rgba(255, 173, 72, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                                d="M0 4C0 1.79086 1.79086 0 4 0H10V20H4C1.79086 20 0 18.2091 0 16V4Z">
                                            </path>
                                            <path fill={biz.avg_rating >= 4.8 ? "rgba(251,67,60,1)" : biz.avg_rating >= 4.3 ? 'rgba(255, 100, 61, 1)' : biz.avg_rating >= 3.8 ? 'rgba(255, 100, 61, 1)' : biz.avg_rating >= 3.3 ? 'rgba(255, 135, 66, 1)' : biz.avg_rating >= 2.8 ? 'rgba(255, 135, 66, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                                d="M20 4C20 1.79086 18.2091 0 16 0H10V20H16C18.2091 20 20 18.2091 20 16V4Z">
                                            </path>
                                            <path fill="white" fill-rule="evenodd" clip-rule="evenodd"
                                                d="M10 13.3736L12.5949 14.7111C12.7378 14.7848 12.9006 14.8106 13.0593
                                14.7847C13.4681 14.718 13.7454 14.3325 13.6787 13.9237L13.2085 11.0425L15.2824
                                8.98796C15.3967 8.8748 15.4715 8.72792 15.4959 8.569C15.5588 8.15958 15.2779
                                7.77672 14.8685 7.71384L11.983 7.2707L10.6699 4.66338C10.5975 4.51978 10.481
                                4.40322 10.3374 4.33089C9.96742 4.14458 9.51648 4.29344 9.33017 4.66338L8.01705
                                7.2707L5.13157 7.71384C4.97265 7.73825 4.82577 7.81309 4.71261 7.92731C4.42109
                                8.22158 4.42332 8.69645 4.71759 8.98796L6.79152 11.0425L6.32131 13.9237C6.29541
                                14.0824 6.3212 14.2452 6.39486 14.3881C6.58464 14.7563 7.03696 14.9009 7.40514
                                14.7111L10 13.3736Z">
                                            </path>
                                        </svg>
                                        {/* FOURTH STAR */}
                                        <svg className='middle-star' width="20" height="20" viewBox="0 0 20 20">
                                            <path fill={biz.avg_rating >= 4.8 ? "rgba(251,67,60,1)" : biz.avg_rating >= 4.3 ? 'rgba(255, 100, 61, 1)' : biz.avg_rating >= 3.8 ? 'rgba(255, 100, 61, 1)' : biz.avg_rating >= 3.3 ? 'rgba(255, 135, 66, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                                d="M0 4C0 1.79086 1.79086 0 4 0H10V20H4C1.79086 20 0 18.2091 0 16V4Z">
                                            </path>
                                            <path fill={biz.avg_rating >= 4.8 ? "rgba(251,67,60,1)" : biz.avg_rating >= 4.3 ? 'rgba(255, 100, 61, 1)' : biz.avg_rating >= 3.8 ? 'rgba(255, 100, 61, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                                d="M20 4C20 1.79086 18.2091 0 16 0H10V20H16C18.2091 20 20 18.2091 20 16V4Z">
                                            </path>
                                            <path fill="white" fill-rule="evenodd" clip-rule="evenodd"
                                                d="M10 13.3736L12.5949 14.7111C12.7378 14.7848 12.9006 14.8106 13.0593
                                14.7847C13.4681 14.718 13.7454 14.3325 13.6787 13.9237L13.2085 11.0425L15.2824
                                8.98796C15.3967 8.8748 15.4715 8.72792 15.4959 8.569C15.5588 8.15958 15.2779
                                7.77672 14.8685 7.71384L11.983 7.2707L10.6699 4.66338C10.5975 4.51978 10.481
                                4.40322 10.3374 4.33089C9.96742 4.14458 9.51648 4.29344 9.33017 4.66338L8.01705
                                7.2707L5.13157 7.71384C4.97265 7.73825 4.82577 7.81309 4.71261 7.92731C4.42109
                                8.22158 4.42332 8.69645 4.71759 8.98796L6.79152 11.0425L6.32131 13.9237C6.29541
                                14.0824 6.3212 14.2452 6.39486 14.3881C6.58464 14.7563 7.03696 14.9009 7.40514
                                14.7111L10 13.3736Z">
                                            </path>
                                        </svg>
                                        {/* FIFTH STAR */}
                                        <svg className='last-star' width="20" height="20" viewBox="0 0 20 20">
                                            <path fill={biz.avg_rating >= 4.8 ? "rgba(251,67,60,1)" : biz.avg_rating >= 4.3 ? 'rgba(255, 100, 61, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                                d="M0 4C0 1.79086 1.79086 0 4 0H10V20H4C1.79086 20 0 18.2091 0 16V4Z">
                                            </path>
                                            <path fill={biz.avg_rating >= 4.8 ? "rgba(251,67,60,1)" : 'rgba(187, 186, 192, 0.5)'}
                                                d="M20 4C20 1.79086 18.2091 0 16 0H10V20H16C18.2091 20 20 18.2091 20 16V4Z">
                                            </path>
                                            <path fill="white" fill-rule="evenodd" clip-rule="evenodd"
                                                d="M10 13.3736L12.5949 14.7111C12.7378 14.7848 12.9006 14.8106 13.0593
                                14.7847C13.4681 14.718 13.7454 14.3325 13.6787 13.9237L13.2085 11.0425L15.2824
                                8.98796C15.3967 8.8748 15.4715 8.72792 15.4959 8.569C15.5588 8.15958 15.2779
                                7.77672 14.8685 7.71384L11.983 7.2707L10.6699 4.66338C10.5975 4.51978 10.481
                                4.40322 10.3374 4.33089C9.96742 4.14458 9.51648 4.29344 9.33017 4.66338L8.01705
                                7.2707L5.13157 7.71384C4.97265 7.73825 4.82577 7.81309 4.71261 7.92731C4.42109
                                8.22158 4.42332 8.69645 4.71759 8.98796L6.79152 11.0425L6.32131 13.9237C6.29541
                                14.0824 6.3212 14.2452 6.39486 14.3881C6.58464 14.7563 7.03696 14.9009 7.40514
                                14.7111L10 13.3736Z">
                                            </path>
                                        </svg>
                                    </div>
                                </div>
                                <div id='rev-rating'>
                                    {biz.avg_rating}
                                </div>
                                <div id='biz-text-rev'>
                                    ({biz.Review.review_length} reviews)
                                </div>
                            </div>
                            <div id='biz-type-loc'>
                                <div>
                                    {Object.values(biz.types).map(type => (
                                        <button id='biz-type-butts'>
                                            {type.type}
                                        </button>
                                    ))}
                                </div>
                                <div id='biz-price'>
                                    {biz.price_range} • {biz.city}
                                </div>
                            </div>
                            <div>
                                {current_time > biz.start_time && current_time < biz.end_time ?
                                    (<div id='biz-hours'>
                                        <span id='biz-open'>Open</span>
                                        <span id='biz-hours-1'>
                                            until {time_conversion(biz.end_time)} {Number(biz.end_time) >= 1200 ? 'PM' : 'AM'}
                                        </span>
                                    </div>) :
                                    (<div id='biz-hours'>
                                        <span id='biz-closed'>Closed</span>
                                        <span id='biz-hours-1'>
                                        until {time_conversion(biz.start_time)} {Number(biz.start_time) >= 1200 ? 'PM' : 'AM'}
                                        </span>
                                    </div>)
                                }
                            </div>
                            <div id='biz-rev'>
                                <img src={txtbub} alt='txtbubble' width='16px' height='14px' />
                                <div id='biz-rev-p'>
                                    "{biz.Review.preview_review}"
                                </div>
                            </div>
                            <div id='biz-tras'>
                                <div>
                                    {Object.values(biz.transactions).map(tra => (
                                        <span id='tra-text'>
                                            <img src={check} alt='checkmark' width='16px' height='10px' />
                                            {tra.transaction}
                                        </span>
                                    ))}
                                </div>
                            </div>
                        </div>

                    </div>
                ))}
            </ol>
        </main>
    )
}
