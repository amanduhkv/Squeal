import React, { useEffect, useState, useRef } from 'react'
import './ReviewForm.css';
import {useParams, Redirect, useHistory} from 'react-router-dom';
import { useSelector, useDispatch } from 'react-redux';
// import { signUp, login } from '../../store/session';
// import { Modal } from '../../context/Modal';
// import party from '../../icons/login.png';
import { getOneBiz } from '../../store/businesses';
import userpig from '../../icons/user-pig.png';
import { createReview } from '../../store/reviews';
import { getBusinessReviews } from '../../store/reviews';

const ReviewForm = () => {
    const history = useHistory();
    const [ hover1, isHover1 ] = useHover();
    const [ hover2, isHover2 ] = useHover();
    const [ hover3, isHover3 ] = useHover();
    const [ hover4, isHover4 ] = useHover();
    const [ hover5, isHover5 ] = useHover();
    const rate = 4.5;
    const rate2 = 5;
    const rate3 = 5;
    const [ revRate, setRevRate ] = useState(0);
    const [ revBody, setRevBody ] = useState('');
    const [ showSidebar, setShowSidebar ] = useState(true);
    const [ read1, setRead1 ] = useState(false);
    const [ read2, setRead2 ] = useState(false);
    const [ read3, setRead3 ] = useState(false);
    const dispatch = useDispatch();
    const { bizId } = useParams();
    const biz = useSelector(state => state.businesses.singleBusiness);
    const user = useSelector(state => state.session.user);
    const revs = useSelector(state => state.reviews.business);
    const reviews = Object.values(revs);

    console.log(biz);

    useEffect(() => {
        dispatch(getOneBiz(bizId));
    }, [dispatch, bizId]);

    const handleSubmit = async (e) => {
        e.preventDefault();

        if (!user) {
            alert("Please log in or create an account to write a review.");
            return;
        }

        if (reviews.filter(rev => rev.user_id === user.id).length) {
            alert("You have already submitted a review for this restaurant.");
            history.replace(`/biz/${bizId}`);
        }

        const newReview = {
            rating: revRate,
            review_body: revBody
        };

        const newRev = await dispatch(createReview(bizId, newReview, user, biz));

        if(newRev) {
            history.push(`/biz/${bizId}`)
        }
    }


  return (
    <div className='reviewform-page-container'>
        <div className='review-sidebar' style={showSidebar ? { transform: 'translateX(-100%)' } : {}}>
            <button className='sidebar-arrow' onClick={() => setShowSidebar(!showSidebar)}>
              <svg width="16" height="16" className={showSidebar ? "sidebar-svg" : "sidebar-svg-flipped"}><path d="M6.5 11.805a.75.75 0 01-.535-1.276L8.449 8 5.965 5.47a.75.75 0 011.07-1.05l3 3.055a.75.75 0 010 1.05l-3 3.055a.749.749 0 01-.535.225z"></path></svg>
            </button>
            <div className='sidebar-inner-container'>
            <h2 className='review-sidebar-title'>Recent Reviews</h2>
            <div className='sidebar-cards-container'>
                {/* First review start */}
                <div className='sidebar-review-card'>
                    <div className='review-card-user-info sidebar-review-user'>
                    <img className='review-usericon' src={userpig} alt='user' />
                    <div className='review-userinfo'>
                        <span className='review-username'>
                            Jae Young H.
                        </span>
                        <span className='review-written'>
                            Wrote a review
                        </span>
                    </div>
                    </div>
                    <div className='review-card-stars'>
                        {/* FIRST STAR */}
                        <svg className='first-star' width="20" height="20" viewBox="0 0 20 20">
                            <path fill={rate >= 4.8 ? "rgba(251,67,60,1)" : rate >= 4.3 ? 'rgba(255, 100, 61, 1)' : rate >= 3.8 ? 'rgba(255, 100, 61, 1)' : rate >= 3.3 ? 'rgba(255, 135, 66, 1)' : rate >= 2.8 ? 'rgba(255, 135, 66, 1)' : rate >= 2.3 ? 'rgba(255, 173, 72, 1)' : rate >= 1.8 ? 'rgba(255, 173, 72, 1)' : rate >= 1.3 ? 'rgba(255, 204, 75, 1)' : 'rgba(255, 204, 75, 1)'}
                                d="M0 4C0 1.79086 1.79086 0 4 0H10V20H4C1.79086 20 0 18.2091 0 16V4Z">
                            </path>
                            <path fill={rate >= 4.8 ? "rgba(251,67,60,1)" : rate >= 4.3 ? 'rgba(255, 100, 61, 1)' : rate >= 3.8 ? 'rgba(255, 100, 61, 1)' : rate >= 3.3 ? 'rgba(255, 135, 66, 1)' : rate >= 2.8 ? 'rgba(255, 135, 66, 1)' : rate >= 2.3 ? 'rgba(255, 173, 72, 1)' : rate >= 1.8 ? 'rgba(255, 173, 72, 1)' : rate >= 1.3 ? 'rgba(255, 204, 75, 1)' : 'rgba(255, 204, 75, 1)'}
                                d="M20 4C20 1.79086 18.2091 0 16 0H10V20H16C18.2091 20 20 18.2091 20 16V4Z">
                            </path>
                            <path fill="white" fillRule="evenodd" clipRule="evenodd"
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
                            <path fill={rate >= 4.8 ? "rgba(251,67,60,1)" : rate >= 4.3 ? 'rgba(255, 100, 61, 1)' : rate >= 3.8 ? 'rgba(255, 100, 61, 1)' : rate >= 3.3 ? 'rgba(255, 135, 66, 1)' : rate >= 2.8 ? 'rgba(255, 135, 66, 1)' : rate >= 2.3 ? 'rgba(255, 173, 72, 1)' : rate >= 1.8 ? 'rgba(255, 173, 72, 1)' : rate >= 1.3 ? 'rgba(255, 204, 75, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                d="M0 4C0 1.79086 1.79086 0 4 0H10V20H4C1.79086 20 0 18.2091 0 16V4Z">
                            </path>
                            <path fill={rate >= 4.8 ? "rgba(251,67,60,1)" : rate >= 4.3 ? 'rgba(255, 100, 61, 1)' : rate >= 3.8 ? 'rgba(255, 100, 61, 1)' : rate >= 3.3 ? 'rgba(255, 135, 66, 1)' : rate >= 2.8 ? 'rgba(255, 135, 66, 1)' : rate >= 2.3 ? 'rgba(255, 173, 72, 1)' : rate >= 1.8 ? 'rgba(255, 173, 72, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                d="M20 4C20 1.79086 18.2091 0 16 0H10V20H16C18.2091 20 20 18.2091 20 16V4Z">
                            </path>
                            <path fill="white" fillRule="evenodd" clipRule="evenodd"
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
                            <path fill={rate >= 4.8 ? "rgba(251,67,60,1)" : rate >= 4.3 ? 'rgba(255, 100, 61, 1)' : rate >= 3.8 ? 'rgba(255, 100, 61, 1)' : rate >= 3.3 ? 'rgba(255, 135, 66, 1)' : rate >= 2.8 ? 'rgba(255, 135, 66, 1)' : rate >= 2.3 ? 'rgba(255, 173, 72, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                d="M0 4C0 1.79086 1.79086 0 4 0H10V20H4C1.79086 20 0 18.2091 0 16V4Z">
                            </path>
                            <path fill={rate >= 4.8 ? "rgba(251,67,60,1)" : rate >= 4.3 ? 'rgba(255, 100, 61, 1)' : rate >= 3.8 ? 'rgba(255, 100, 61, 1)' : rate >= 3.3 ? 'rgba(255, 135, 66, 1)' : rate >= 2.8 ? 'rgba(255, 135, 66, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                d="M20 4C20 1.79086 18.2091 0 16 0H10V20H16C18.2091 20 20 18.2091 20 16V4Z">
                            </path>
                            <path fill="white" fillRule="evenodd" clipRule="evenodd"
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
                            <path fill={rate >= 4.8 ? "rgba(251,67,60,1)" : rate >= 4.3 ? 'rgba(255, 100, 61, 1)' : rate >= 3.8 ? 'rgba(255, 100, 61, 1)' : rate >= 3.3 ? 'rgba(255, 135, 66, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                d="M0 4C0 1.79086 1.79086 0 4 0H10V20H4C1.79086 20 0 18.2091 0 16V4Z">
                            </path>
                            <path fill={rate >= 4.8 ? "rgba(251,67,60,1)" : rate >= 4.3 ? 'rgba(255, 100, 61, 1)' : rate >= 3.8 ? 'rgba(255, 100, 61, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                d="M20 4C20 1.79086 18.2091 0 16 0H10V20H16C18.2091 20 20 18.2091 20 16V4Z">
                            </path>
                            <path fill="white" fillRule="evenodd" clipRule="evenodd"
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
                            <path fill={rate >= 4.8 ? "rgba(251,67,60,1)" : rate >= 4.3 ? 'rgba(255, 100, 61, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                d="M0 4C0 1.79086 1.79086 0 4 0H10V20H4C1.79086 20 0 18.2091 0 16V4Z">
                            </path>
                            <path fill={rate >= 4.8 ? "rgba(251,67,60,1)" : 'rgba(187, 186, 192, 0.5)'}
                                d="M20 4C20 1.79086 18.2091 0 16 0H10V20H16C18.2091 20 20 18.2091 20 16V4Z">
                            </path>
                            <path fill="white" fillRule="evenodd" clipRule="evenodd"
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
                    <div className={read1 ? 'sidebar-text sidebar-review-card-text' : 'sidebar-text sidebar-review-card-text-sh'}>
                    I've tried a handful of Korean fried chicken joints, and they all kind of blend together. But for me, CM chicken is one of those places that really stand out!
                    <br /><br />
                    Super convenient online ordering and very unique flavors. I also like how when you order to-go, they separate all the sauces into different containers so it doesn't get soggy. The chicken still tasted really good and crispy after the 45-minute drive home.
                    <br /><br />
                    After watching Korean mukbangs, I've been really interested in trying snow chicken (4.5/5) and this place has it! If you're a fan of the refreshing crunch of onions, you'll really like this combo.
                    <br /><br />
                    This place scratched an itch that I didn't even know I had! Will undoubtedly be back in the future if I have more late-night cravings.
                    </div>
                    <div className='sidebar-review-card-continue' onClick={() => setRead1(!read1)}>
                        {read1 ? 'Collapse' : 'Continue reading'}
                    </div>
                </div>
                {/* First review end */}
                {/* First review start */}
                <div className='sidebar-review-card'>
                    <div className='review-card-user-info sidebar-review-user'>
                    <img className='review-usericon' src={userpig} alt='user' />
                    <div className='review-userinfo'>
                        <span className='review-username'>
                            Amanda V.
                        </span>
                        <span className='review-written'>
                            Wrote a review
                        </span>
                    </div>
                    </div>
                    <div className='review-card-stars'>
                        {/* FIRST STAR */}
                        <svg className='first-star' width="20" height="20" viewBox="0 0 20 20">
                            <path fill={rate2 >= 4.8 ? "rgba(251,67,60,1)" : rate2 >= 4.3 ? 'rgba(255, 100, 61, 1)' : rate2 >= 3.8 ? 'rgba(255, 100, 61, 1)' : rate2 >= 3.3 ? 'rgba(255, 135, 66, 1)' : rate2 >= 2.8 ? 'rgba(255, 135, 66, 1)' : rate2 >= 2.3 ? 'rgba(255, 173, 72, 1)' : rate2 >= 1.8 ? 'rgba(255, 173, 72, 1)' : rate2 >= 1.3 ? 'rgba(255, 204, 75, 1)' : 'rgba(255, 204, 75, 1)'}
                                d="M0 4C0 1.79086 1.79086 0 4 0H10V20H4C1.79086 20 0 18.2091 0 16V4Z">
                            </path>
                            <path fill={rate2 >= 4.8 ? "rgba(251,67,60,1)" : rate2 >= 4.3 ? 'rgba(255, 100, 61, 1)' : rate2 >= 3.8 ? 'rgba(255, 100, 61, 1)' : rate2 >= 3.3 ? 'rgba(255, 135, 66, 1)' : rate2 >= 2.8 ? 'rgba(255, 135, 66, 1)' : rate2 >= 2.3 ? 'rgba(255, 173, 72, 1)' : rate2 >= 1.8 ? 'rgba(255, 173, 72, 1)' : rate2 >= 1.3 ? 'rgba(255, 204, 75, 1)' : 'rgba(255, 204, 75, 1)'}
                                d="M20 4C20 1.79086 18.2091 0 16 0H10V20H16C18.2091 20 20 18.2091 20 16V4Z">
                            </path>
                            <path fill="white" fillRule="evenodd" clipRule="evenodd"
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
                            <path fill={rate2 >= 4.8 ? "rgba(251,67,60,1)" : rate2 >= 4.3 ? 'rgba(255, 100, 61, 1)' : rate2 >= 3.8 ? 'rgba(255, 100, 61, 1)' : rate2 >= 3.3 ? 'rgba(255, 135, 66, 1)' : rate2 >= 2.8 ? 'rgba(255, 135, 66, 1)' : rate2 >= 2.3 ? 'rgba(255, 173, 72, 1)' : rate2 >= 1.8 ? 'rgba(255, 173, 72, 1)' : rate2 >= 1.3 ? 'rgba(255, 204, 75, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                d="M0 4C0 1.79086 1.79086 0 4 0H10V20H4C1.79086 20 0 18.2091 0 16V4Z">
                            </path>
                            <path fill={rate2 >= 4.8 ? "rgba(251,67,60,1)" : rate2 >= 4.3 ? 'rgba(255, 100, 61, 1)' : rate2 >= 3.8 ? 'rgba(255, 100, 61, 1)' : rate2 >= 3.3 ? 'rgba(255, 135, 66, 1)' : rate2 >= 2.8 ? 'rgba(255, 135, 66, 1)' : rate2 >= 2.3 ? 'rgba(255, 173, 72, 1)' : rate2 >= 1.8 ? 'rgba(255, 173, 72, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                d="M20 4C20 1.79086 18.2091 0 16 0H10V20H16C18.2091 20 20 18.2091 20 16V4Z">
                            </path>
                            <path fill="white" fillRule="evenodd" clipRule="evenodd"
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
                            <path fill={rate2 >= 4.8 ? "rgba(251,67,60,1)" : rate2 >= 4.3 ? 'rgba(255, 100, 61, 1)' : rate2 >= 3.8 ? 'rgba(255, 100, 61, 1)' : rate2 >= 3.3 ? 'rgba(255, 135, 66, 1)' : rate2 >= 2.8 ? 'rgba(255, 135, 66, 1)' : rate2 >= 2.3 ? 'rgba(255, 173, 72, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                d="M0 4C0 1.79086 1.79086 0 4 0H10V20H4C1.79086 20 0 18.2091 0 16V4Z">
                            </path>
                            <path fill={rate2 >= 4.8 ? "rgba(251,67,60,1)" : rate2 >= 4.3 ? 'rgba(255, 100, 61, 1)' : rate2 >= 3.8 ? 'rgba(255, 100, 61, 1)' : rate2 >= 3.3 ? 'rgba(255, 135, 66, 1)' : rate2 >= 2.8 ? 'rgba(255, 135, 66, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                d="M20 4C20 1.79086 18.2091 0 16 0H10V20H16C18.2091 20 20 18.2091 20 16V4Z">
                            </path>
                            <path fill="white" fillRule="evenodd" clipRule="evenodd"
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
                            <path fill={rate2 >= 4.8 ? "rgba(251,67,60,1)" : rate2 >= 4.3 ? 'rgba(255, 100, 61, 1)' : rate2 >= 3.8 ? 'rgba(255, 100, 61, 1)' : rate2 >= 3.3 ? 'rgba(255, 135, 66, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                d="M0 4C0 1.79086 1.79086 0 4 0H10V20H4C1.79086 20 0 18.2091 0 16V4Z">
                            </path>
                            <path fill={rate2 >= 4.8 ? "rgba(251,67,60,1)" : rate2 >= 4.3 ? 'rgba(255, 100, 61, 1)' : rate2 >= 3.8 ? 'rgba(255, 100, 61, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                d="M20 4C20 1.79086 18.2091 0 16 0H10V20H16C18.2091 20 20 18.2091 20 16V4Z">
                            </path>
                            <path fill="white" fillRule="evenodd" clipRule="evenodd"
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
                            <path fill={rate2 >= 4.8 ? "rgba(251,67,60,1)" : rate2 >= 4.3 ? 'rgba(255, 100, 61, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                d="M0 4C0 1.79086 1.79086 0 4 0H10V20H4C1.79086 20 0 18.2091 0 16V4Z">
                            </path>
                            <path fill={rate2 >= 4.8 ? "rgba(251,67,60,1)" : 'rgba(187, 186, 192, 0.5)'}
                                d="M20 4C20 1.79086 18.2091 0 16 0H10V20H16C18.2091 20 20 18.2091 20 16V4Z">
                            </path>
                            <path fill="white" fillRule="evenodd" clipRule="evenodd"
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
                    <div className={read2 ? 'sidebar-text sidebar-review-card-text' : 'sidebar-text sidebar-review-card-text-sh'}>
                    This place is a little gem tucked in a corner you probably drive by on your daily commute.
                    <br /><br />
                    I love that it feels like you're in the production of some YouTubers kitchen or something. Everyone's in motion and there's wonders behind every counter.
                    <br /><br />
                    The food here is fresh and of high quality. It's made with such mastery and I am glad they have such a affordable menu. Everyone on the west coast must come here to try the closest thing to Italian food there is. (West coast isn't as blessed with Italian food as the east).
                    <br /><br />
                    I had the porcini mushroom pasta with chicken. It was house made pasta  with a light cream sauce. The chicken was so moist and beautifully cut up to still allow the mushrooms to be the star of the show.
                    <br /><br />
                    The service, food and price point is such a perfect score. Would come back here again.
                    </div>
                    <div className='sidebar-review-card-continue' onClick={() => setRead2(!read2)}>
                        {read2 ? 'Collapse' : 'Continue reading'}
                    </div>
                </div>
                {/* First review end */}
                {/* First review start */}
                <div className='sidebar-review-card'>
                    <div className='review-card-user-info sidebar-review-user'>
                    <img className='review-usericon' src={userpig} alt='user' />
                    <div className='review-userinfo'>
                        <span className='review-username'>
                            Michael J.
                        </span>
                        <span className='review-written'>
                            Wrote a review
                        </span>
                    </div>
                    </div>
                    <div className='review-card-stars'>
                        {/* FIRST STAR */}
                        <svg className='first-star' width="20" height="20" viewBox="0 0 20 20">
                            <path fill={rate3 >= 4.8 ? "rgba(251,67,60,1)" : rate3 >= 4.3 ? 'rgba(255, 100, 61, 1)' : rate3 >= 3.8 ? 'rgba(255, 100, 61, 1)' : rate3 >= 3.3 ? 'rgba(255, 135, 66, 1)' : rate3 >= 2.8 ? 'rgba(255, 135, 66, 1)' : rate3 >= 2.3 ? 'rgba(255, 173, 72, 1)' : rate3 >= 1.8 ? 'rgba(255, 173, 72, 1)' : rate3 >= 1.3 ? 'rgba(255, 204, 75, 1)' : 'rgba(255, 204, 75, 1)'}
                                d="M0 4C0 1.79086 1.79086 0 4 0H10V20H4C1.79086 20 0 18.2091 0 16V4Z">
                            </path>
                            <path fill={rate3 >= 4.8 ? "rgba(251,67,60,1)" : rate3 >= 4.3 ? 'rgba(255, 100, 61, 1)' : rate3 >= 3.8 ? 'rgba(255, 100, 61, 1)' : rate3 >= 3.3 ? 'rgba(255, 135, 66, 1)' : rate3 >= 2.8 ? 'rgba(255, 135, 66, 1)' : rate3 >= 2.3 ? 'rgba(255, 173, 72, 1)' : rate3 >= 1.8 ? 'rgba(255, 173, 72, 1)' : rate3 >= 1.3 ? 'rgba(255, 204, 75, 1)' : 'rgba(255, 204, 75, 1)'}
                                d="M20 4C20 1.79086 18.2091 0 16 0H10V20H16C18.2091 20 20 18.2091 20 16V4Z">
                            </path>
                            <path fill="white" fillRule="evenodd" clipRule="evenodd"
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
                            <path fill={rate3 >= 4.8 ? "rgba(251,67,60,1)" : rate3 >= 4.3 ? 'rgba(255, 100, 61, 1)' : rate3 >= 3.8 ? 'rgba(255, 100, 61, 1)' : rate3 >= 3.3 ? 'rgba(255, 135, 66, 1)' : rate3 >= 2.8 ? 'rgba(255, 135, 66, 1)' : rate3 >= 2.3 ? 'rgba(255, 173, 72, 1)' : rate3 >= 1.8 ? 'rgba(255, 173, 72, 1)' : rate3 >= 1.3 ? 'rgba(255, 204, 75, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                d="M0 4C0 1.79086 1.79086 0 4 0H10V20H4C1.79086 20 0 18.2091 0 16V4Z">
                            </path>
                            <path fill={rate3 >= 4.8 ? "rgba(251,67,60,1)" : rate3 >= 4.3 ? 'rgba(255, 100, 61, 1)' : rate3 >= 3.8 ? 'rgba(255, 100, 61, 1)' : rate3 >= 3.3 ? 'rgba(255, 135, 66, 1)' : rate3 >= 2.8 ? 'rgba(255, 135, 66, 1)' : rate3 >= 2.3 ? 'rgba(255, 173, 72, 1)' : rate3 >= 1.8 ? 'rgba(255, 173, 72, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                d="M20 4C20 1.79086 18.2091 0 16 0H10V20H16C18.2091 20 20 18.2091 20 16V4Z">
                            </path>
                            <path fill="white" fillRule="evenodd" clipRule="evenodd"
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
                            <path fill={rate3 >= 4.8 ? "rgba(251,67,60,1)" : rate3 >= 4.3 ? 'rgba(255, 100, 61, 1)' : rate3 >= 3.8 ? 'rgba(255, 100, 61, 1)' : rate3 >= 3.3 ? 'rgba(255, 135, 66, 1)' : rate3 >= 2.8 ? 'rgba(255, 135, 66, 1)' : rate3 >= 2.3 ? 'rgba(255, 173, 72, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                d="M0 4C0 1.79086 1.79086 0 4 0H10V20H4C1.79086 20 0 18.2091 0 16V4Z">
                            </path>
                            <path fill={rate3 >= 4.8 ? "rgba(251,67,60,1)" : rate3 >= 4.3 ? 'rgba(255, 100, 61, 1)' : rate3 >= 3.8 ? 'rgba(255, 100, 61, 1)' : rate3 >= 3.3 ? 'rgba(255, 135, 66, 1)' : rate3 >= 2.8 ? 'rgba(255, 135, 66, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                d="M20 4C20 1.79086 18.2091 0 16 0H10V20H16C18.2091 20 20 18.2091 20 16V4Z">
                            </path>
                            <path fill="white" fillRule="evenodd" clipRule="evenodd"
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
                            <path fill={rate3 >= 4.8 ? "rgba(251,67,60,1)" : rate3 >= 4.3 ? 'rgba(255, 100, 61, 1)' : rate3 >= 3.8 ? 'rgba(255, 100, 61, 1)' : rate3 >= 3.3 ? 'rgba(255, 135, 66, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                d="M0 4C0 1.79086 1.79086 0 4 0H10V20H4C1.79086 20 0 18.2091 0 16V4Z">
                            </path>
                            <path fill={rate3 >= 4.8 ? "rgba(251,67,60,1)" : rate3 >= 4.3 ? 'rgba(255, 100, 61, 1)' : rate3 >= 3.8 ? 'rgba(255, 100, 61, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                d="M20 4C20 1.79086 18.2091 0 16 0H10V20H16C18.2091 20 20 18.2091 20 16V4Z">
                            </path>
                            <path fill="white" fillRule="evenodd" clipRule="evenodd"
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
                            <path fill={rate3 >= 4.8 ? "rgba(251,67,60,1)" : rate3 >= 4.3 ? 'rgba(255, 100, 61, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                d="M0 4C0 1.79086 1.79086 0 4 0H10V20H4C1.79086 20 0 18.2091 0 16V4Z">
                            </path>
                            <path fill={rate3 >= 4.8 ? "rgba(251,67,60,1)" : 'rgba(187, 186, 192, 0.5)'}
                                d="M20 4C20 1.79086 18.2091 0 16 0H10V20H16C18.2091 20 20 18.2091 20 16V4Z">
                            </path>
                            <path fill="white" fillRule="evenodd" clipRule="evenodd"
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
                    <div className={read3 ? 'sidebar-text sidebar-review-card-text' : 'sidebar-text sidebar-review-card-text-sh'}>
                    I love this place! The authenticity of it is unbeatable. This is my wife and her best friend's go to, and when she decided to take me it became my go to as well.
                    <br /><br />
                    This place isn't your typical fake sushi restaurant. This is genuine and authentic Japanese food that people commonly eat for breakfast. The food is a 10/10, the atmosphere is phenomenal, and the service is the cherry on top.
                    <br /><br />
                    I recommend this place 10000%. A bonus is that there are restaurants around so you can get boba or dessert after your meal :)</div>
                    <div className='sidebar-review-card-continue' onClick={() => setRead3(!read3)}>
                        {read3 ? 'Collapse' : 'Continue reading'}
                    </div>
                </div>
                {/* First review end */}
              </div>
            </div>
        </div>
        <div className='new-review-container'>
          <div className='new-review-inner'>
            <h1 className='new-review-title'>{biz.name}</h1>
            <form className='new-review-form' onSubmit={handleSubmit}>
              <div className='new-review-form-inner'>
              <div className='new-review-stars'>
                        {/* FIRST STAR */}
                        <svg ref={hover1} onClick={() => setRevRate(1)}
                            id={isHover1 ? 'one' : isHover2 ? 'two' : isHover3 ? 'three' : isHover4 ? 'four' : isHover5 ? 'five' : ''} className={revRate > 4 ? 'big-first-star new-star star1 five' : revRate > 3 ? 'big-first-star new-star star1 four' : revRate > 2 ? 'big-first-star new-star star1 three' : revRate > 1 ? 'big-first-star new-star star1 two' : revRate > 0 ? 'big-first-star new-star star1 one' : 'big-first-star new-star star1'} width="32" height="32" viewBox="0 0 20 20">
                            <path className='star-1l'
                            // fill={rate >= 4.8 ? "rgba(251,67,60,1)" : rate >= 4.3 ? 'rgba(255, 100, 61, 1)' : rate >= 3.8 ? 'rgba(255, 100, 61, 1)' : rate >= 3.3 ? 'rgba(255, 135, 66, 1)' : rate >= 2.8 ? 'rgba(255, 135, 66, 1)' : rate >= 2.3 ? 'rgba(255, 173, 72, 1)' : rate >= 1.8 ? 'rgba(255, 173, 72, 1)' : rate >= 1.3 ? 'rgba(255, 204, 75, 1)' : 'rgba(255, 204, 75, 1)'}
                                d="M0 4C0 1.79086 1.79086 0 4 0H10V20H4C1.79086 20 0 18.2091 0 16V4Z">
                            </path>
                            <path className='star-1r'
                            // fill={rate >= 4.8 ? "rgba(251,67,60,1)" : rate >= 4.3 ? 'rgba(255, 100, 61, 1)' : rate >= 3.8 ? 'rgba(255, 100, 61, 1)' : rate >= 3.3 ? 'rgba(255, 135, 66, 1)' : rate >= 2.8 ? 'rgba(255, 135, 66, 1)' : rate >= 2.3 ? 'rgba(255, 173, 72, 1)' : rate >= 1.8 ? 'rgba(255, 173, 72, 1)' : rate >= 1.3 ? 'rgba(255, 204, 75, 1)' : 'rgba(255, 204, 75, 1)'}
                                d="M20 4C20 1.79086 18.2091 0 16 0H10V20H16C18.2091 20 20 18.2091 20 16V4Z">
                            </path>
                            <path fill="white" fillRule="evenodd" clipRule="evenodd"
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
                        <svg ref={hover2} id={isHover1 ? 'grey' : isHover2 ? 'two' : isHover3 ? 'three' : isHover4 ? 'four' : isHover5 ? 'five' : ''}
                             onClick={() => setRevRate(2)} className={revRate > 4 ? 'big-middle-star new-star star2 five' : revRate > 3 ? 'big-middle-star new-star star2 four' : revRate > 2 ? 'big-middle-star new-star star2 three' : revRate > 1 ? 'big-middle-star new-star star2 two' : 'big-middle-star new-star star2'} width="32" height="32" viewBox="0 0 20 20">
                            <path className='star-2l'
                            // fill={rate >= 4.8 ? "rgba(251,67,60,1)" : rate >= 4.3 ? 'rgba(255, 100, 61, 1)' : rate >= 3.8 ? 'rgba(255, 100, 61, 1)' : rate >= 3.3 ? 'rgba(255, 135, 66, 1)' : rate >= 2.8 ? 'rgba(255, 135, 66, 1)' : rate >= 2.3 ? 'rgba(255, 173, 72, 1)' : rate >= 1.8 ? 'rgba(255, 173, 72, 1)' : rate >= 1.3 ? 'rgba(255, 204, 75, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                d="M0 4C0 1.79086 1.79086 0 4 0H10V20H4C1.79086 20 0 18.2091 0 16V4Z">
                            </path>
                            <path className='star-2r'
                            // fill={rate >= 4.8 ? "rgba(251,67,60,1)" : rate >= 4.3 ? 'rgba(255, 100, 61, 1)' : rate >= 3.8 ? 'rgba(255, 100, 61, 1)' : rate >= 3.3 ? 'rgba(255, 135, 66, 1)' : rate >= 2.8 ? 'rgba(255, 135, 66, 1)' : rate >= 2.3 ? 'rgba(255, 173, 72, 1)' : rate >= 1.8 ? 'rgba(255, 173, 72, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                d="M20 4C20 1.79086 18.2091 0 16 0H10V20H16C18.2091 20 20 18.2091 20 16V4Z">
                            </path>
                            <path fill="white" fillRule="evenodd" clipRule="evenodd"
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
                        <svg ref={hover3} id={isHover1 ? 'grey' : isHover2 ? 'grey' : isHover3 ? 'three' : isHover4 ? 'four' : isHover5 ? 'five' : ''} onClick={() => setRevRate(3)}
                            className={revRate > 4 ? 'big-middle-star new-star star3 five' : revRate > 3 ? 'big-middle-star new-star star3 four' : revRate > 2 ? 'big-middle-star new-star star3 three' : 'big-middle-star new-star star3'} width="32" height="32" viewBox="0 0 20 20">
                            <path className='star-3l'
                            // fill={rate >= 4.8 ? "rgba(251,67,60,1)" : rate >= 4.3 ? 'rgba(255, 100, 61, 1)' : rate >= 3.8 ? 'rgba(255, 100, 61, 1)' : rate >= 3.3 ? 'rgba(255, 135, 66, 1)' : rate >= 2.8 ? 'rgba(255, 135, 66, 1)' : rate >= 2.3 ? 'rgba(255, 173, 72, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                d="M0 4C0 1.79086 1.79086 0 4 0H10V20H4C1.79086 20 0 18.2091 0 16V4Z">
                            </path>
                            <path className='star-3r'
                            // fill={rate >= 4.8 ? "rgba(251,67,60,1)" : rate >= 4.3 ? 'rgba(255, 100, 61, 1)' : rate >= 3.8 ? 'rgba(255, 100, 61, 1)' : rate >= 3.3 ? 'rgba(255, 135, 66, 1)' : rate >= 2.8 ? 'rgba(255, 135, 66, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                d="M20 4C20 1.79086 18.2091 0 16 0H10V20H16C18.2091 20 20 18.2091 20 16V4Z">
                            </path>
                            <path fill="white" fillRule="evenodd" clipRule="evenodd"
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
                        <svg ref={hover4} id={isHover1 ? 'grey' : isHover2 ? 'grey' : isHover3 ? 'grey' : isHover4 ? 'four' : isHover5 ? 'five' : ''} onClick={() => setRevRate(4)}
                            className={revRate > 4 ? 'big-middle-star new-star star4 five' : revRate > 3 ? 'big-middle-star new-star star4 four' : 'big-middle-star new-star star4'} width="32" height="32" viewBox="0 0 20 20">
                            <path className='star-4l'
                            // fill={rate >= 4.8 ? "rgba(251,67,60,1)" : rate >= 4.3 ? 'rgba(255, 100, 61, 1)' : rate >= 3.8 ? 'rgba(255, 100, 61, 1)' : rate >= 3.3 ? 'rgba(255, 135, 66, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                d="M0 4C0 1.79086 1.79086 0 4 0H10V20H4C1.79086 20 0 18.2091 0 16V4Z">
                            </path>
                            <path className='star-4r'
                            // fill={rate >= 4.8 ? "rgba(251,67,60,1)" : rate >= 4.3 ? 'rgba(255, 100, 61, 1)' : rate >= 3.8 ? 'rgba(255, 100, 61, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                d="M20 4C20 1.79086 18.2091 0 16 0H10V20H16C18.2091 20 20 18.2091 20 16V4Z">
                            </path>
                            <path fill="white" fillRule="evenodd" clipRule="evenodd"
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
                        <svg ref={hover5} id={isHover1 ? 'grey' : isHover2 ? 'grey' : isHover3 ? 'grey' : isHover4 ? 'grey' : isHover5 ? 'five' : ''} onClick={() => setRevRate(5)}
                              className={revRate > 4 ? 'big-last-star new-star star5 five' : 'big-last-star new-star star5'} width="32" height="32" viewBox="0 0 20 20">
                            <path className='star-5l'
                            // fill={rate >= 4.8 ? "rgba(251,67,60,1)" : rate >= 4.3 ? 'rgba(255, 100, 61, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                d="M0 4C0 1.79086 1.79086 0 4 0H10V20H4C1.79086 20 0 18.2091 0 16V4Z">
                            </path>
                            <path className='star-5r'
                            // fill={rate >= 4.8 ? "rgba(251,67,60,1)" : 'rgba(187, 186, 192, 0.5)'}
                                d="M20 4C20 1.79086 18.2091 0 16 0H10V20H16C18.2091 20 20 18.2091 20 16V4Z">
                            </path>
                            <path fill="white" fillRule="evenodd" clipRule="evenodd"
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
                        <div className='new-review-blob'>
                          {isHover5 ? 'Great' : isHover4 ? 'Good' : isHover3 ? 'Ok' : isHover2 ? "Could've been better" : isHover1 ? 'Not good' : revRate === 5 ? 'Great' : revRate === 4 ? 'Good' : revRate === 3 ? 'Ok' : revRate === 2 ? "Could've been better" : revRate === 1 ? 'Not good' : ''}
                        </div>
                    </div>
                <textarea className='new-review-body'
                          value={revBody}
                          onChange={(e) => setRevBody(e.target.value)}
                          required
                          placeholder="I’ve been coming to this place for 3 years now and it’s all you can ask for in a pub with TVs, a jukebox and an outdoor patio. It’s a great spot to catch a Warriors game or just grab drinks with friends. Never been a huge Bloody Mary fan, but after watching the bartender make a few here I had to try one and... wow. They’re legit. The Spicy Mule also gets the job done. Tons of beer on tap, which just adds to the appeal. Head to the back deck and you can kill a whole day before you even realize it."
                           />
              </div>
              <button type='submit' className='new-review-submit'>Post Review</button>
            </form>
          </div>
        </div>
    </div>
  )
}

export default ReviewForm;

function useHover() {
  const [value, setValue] = useState(false);

  const ref = useRef(null);

  const handleMouseOver = () => setValue(true);
  const handleMouseOut = () => setValue(false);

  useEffect(
    () => {
      const node = ref.current;
      if (node) {
        node.addEventListener('mouseover', handleMouseOver);
        node.addEventListener('mouseout', handleMouseOut);

        return () => {
          node.removeEventListener('mouseover', handleMouseOver);
          node.removeEventListener('mouseout', handleMouseOut);
        };
      }
    },
    [ref.current] // Recall only if ref changes
  );

  return [ref, value];
}
