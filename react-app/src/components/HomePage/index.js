import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import './HomePage.css';
import { getAllReviews } from '../../store/reviews';
import userpig from '../../icons/user-pig.png';
import chinese from '../../icons/category-tiles/chi.svg';
import indian from '../../icons/category-tiles/india.svg';
import italian from '../../icons/category-tiles/ital.svg';
import japanese from '../../icons/category-tiles/ja.svg';
import korean from '../../icons/category-tiles/kor.svg';
import mexican from '../../icons/category-tiles/mex.svg';
import thai from '../../icons/category-tiles/thai.svg';
import vietnamese from '../../icons/category-tiles/vietn.svg';

const HomePage = () => {
  const dispatch = useDispatch();
  const rev = useSelector(state => state.reviews.all);
  const revSlice = rev ? Object.values(rev)?.slice(-27) : null;
  console.log('these are the sliced reviews',revSlice);

  useEffect(() => {
      dispatch(getAllReviews())
  }, [dispatch])


  return (
    <div className='homepage-container'>
        <div className='recent-activity-container'>
            <h2 className='recent-activity-title'>
                Recent Activity
            </h2>
            <div className='recent-cards-container'>
            {revSlice ? revSlice.map((rev, i) => i % 3 === 0 ?
            (
                <div key={i} className='review-card'>
                    <div className='review-card-user-info'>
                    <img className='review-usericon' src={userpig} alt='user' />
                    <div className='review-userinfo'>
                        <span className='review-username'>
                            {rev.User.first_name} {rev.User.last_name[0]}.
                        </span>
                        <span className='review-written'>
                            Wrote a review
                        </span>
                    </div>
                    </div>
                    <img src={rev.Image.url} alt='review' className='review-image-prev' />
                    <div className='review-biz-name'>
                        <a className='review-biz-name-link' href={`/biz/${rev.Business.id}`}>{rev.Business.name}</a>
                    </div>
                    <div className='review-card-stars'>
                        {/* FIRST STAR */}
                        <svg className='first-star' width="20" height="20" viewBox="0 0 20 20">
                            <path fill={rev.rating >= 4.8 ? "rgba(251,67,60,1)" : rev.rating >= 4.3 ? 'rgba(255, 100, 61, 1)' : rev.rating >= 3.8 ? 'rgba(255, 100, 61, 1)' : rev.rating >= 3.3 ? 'rgba(255, 135, 66, 1)' : rev.rating >= 2.8 ? 'rgba(255, 135, 66, 1)' : rev.rating >= 2.3 ? 'rgba(255, 173, 72, 1)' : rev.rating >= 1.8 ? 'rgba(255, 173, 72, 1)' : rev.rating >= 1.3 ? 'rgba(255, 204, 75, 1)' : 'rgba(255, 204, 75, 1)'}
                                d="M0 4C0 1.79086 1.79086 0 4 0H10V20H4C1.79086 20 0 18.2091 0 16V4Z">
                            </path>
                            <path fill={rev.rating >= 4.8 ? "rgba(251,67,60,1)" : rev.rating >= 4.3 ? 'rgba(255, 100, 61, 1)' : rev.rating >= 3.8 ? 'rgba(255, 100, 61, 1)' : rev.rating >= 3.3 ? 'rgba(255, 135, 66, 1)' : rev.rating >= 2.8 ? 'rgba(255, 135, 66, 1)' : rev.rating >= 2.3 ? 'rgba(255, 173, 72, 1)' : rev.rating >= 1.8 ? 'rgba(255, 173, 72, 1)' : rev.rating >= 1.3 ? 'rgba(255, 204, 75, 1)' : 'rgba(255, 204, 75, 1)'}
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
                            <path fill={rev.rating >= 4.8 ? "rgba(251,67,60,1)" : rev.rating >= 4.3 ? 'rgba(255, 100, 61, 1)' : rev.rating >= 3.8 ? 'rgba(255, 100, 61, 1)' : rev.rating >= 3.3 ? 'rgba(255, 135, 66, 1)' : rev.rating >= 2.8 ? 'rgba(255, 135, 66, 1)' : rev.rating >= 2.3 ? 'rgba(255, 173, 72, 1)' : rev.rating >= 1.8 ? 'rgba(255, 173, 72, 1)' : rev.rating >= 1.3 ? 'rgba(255, 204, 75, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                d="M0 4C0 1.79086 1.79086 0 4 0H10V20H4C1.79086 20 0 18.2091 0 16V4Z">
                            </path>
                            <path fill={rev.rating >= 4.8 ? "rgba(251,67,60,1)" : rev.rating >= 4.3 ? 'rgba(255, 100, 61, 1)' : rev.rating >= 3.8 ? 'rgba(255, 100, 61, 1)' : rev.rating >= 3.3 ? 'rgba(255, 135, 66, 1)' : rev.rating >= 2.8 ? 'rgba(255, 135, 66, 1)' : rev.rating >= 2.3 ? 'rgba(255, 173, 72, 1)' : rev.rating >= 1.8 ? 'rgba(255, 173, 72, 1)' : 'rgba(187, 186, 192, 0.5)'}
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
                            <path fill={rev.rating >= 4.8 ? "rgba(251,67,60,1)" : rev.rating >= 4.3 ? 'rgba(255, 100, 61, 1)' : rev.rating >= 3.8 ? 'rgba(255, 100, 61, 1)' : rev.rating >= 3.3 ? 'rgba(255, 135, 66, 1)' : rev.rating >= 2.8 ? 'rgba(255, 135, 66, 1)' : rev.rating >= 2.3 ? 'rgba(255, 173, 72, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                d="M0 4C0 1.79086 1.79086 0 4 0H10V20H4C1.79086 20 0 18.2091 0 16V4Z">
                            </path>
                            <path fill={rev.rating >= 4.8 ? "rgba(251,67,60,1)" : rev.rating >= 4.3 ? 'rgba(255, 100, 61, 1)' : rev.rating >= 3.8 ? 'rgba(255, 100, 61, 1)' : rev.rating >= 3.3 ? 'rgba(255, 135, 66, 1)' : rev.rating >= 2.8 ? 'rgba(255, 135, 66, 1)' : 'rgba(187, 186, 192, 0.5)'}
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
                            <path fill={rev.rating >= 4.8 ? "rgba(251,67,60,1)" : rev.rating >= 4.3 ? 'rgba(255, 100, 61, 1)' : rev.rating >= 3.8 ? 'rgba(255, 100, 61, 1)' : rev.rating >= 3.3 ? 'rgba(255, 135, 66, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                d="M0 4C0 1.79086 1.79086 0 4 0H10V20H4C1.79086 20 0 18.2091 0 16V4Z">
                            </path>
                            <path fill={rev.rating >= 4.8 ? "rgba(251,67,60,1)" : rev.rating >= 4.3 ? 'rgba(255, 100, 61, 1)' : rev.rating >= 3.8 ? 'rgba(255, 100, 61, 1)' : 'rgba(187, 186, 192, 0.5)'}
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
                            <path fill={rev.rating >= 4.8 ? "rgba(251,67,60,1)" : rev.rating >= 4.3 ? 'rgba(255, 100, 61, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                d="M0 4C0 1.79086 1.79086 0 4 0H10V20H4C1.79086 20 0 18.2091 0 16V4Z">
                            </path>
                            <path fill={rev.rating >= 4.8 ? "rgba(251,67,60,1)" : 'rgba(187, 186, 192, 0.5)'}
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
                    <div className='review-card-text'>
                        {rev.review_body}
                    </div>
                    <div className='review-card-continue'>
                    <a className='review-card-continue-link' href={`/biz/${rev.Business.id}`}>Continue reading</a>
                    </div>
                </div>
            ) : null) : null}
            </div>
        </div>
        <div className='category-type-container'>
            <h2 className='category-type-title'>
                Categories
            </h2>
            <div className='categories-container'>
                <div className='categories-outer-container'>
                    <a className='category-link' href='/biz?type=chinese'>
                        <div className='category-tile chinese-tile'>
                            <img className='category-icon' src={chinese} alt='chinese' />
                            <p className='category-title'>
                                Chinese
                            </p>
                        </div>
                    </a>
                </div>
                <span className='categories-gap' />
                <div className='categories-outer-container'>
                    <a className='category-link' href='/biz?type=indpak'>
                        <div className='category-tile chinese-tile'>
                            <img className='category-icon' src={indian} alt='chinese' />
                            <p className='category-title'>
                                Indian
                            </p>
                        </div>
                    </a>
                </div>
                <span className='categories-gap' />
                <div className='categories-outer-container'>
                    <a className='category-link' href='/biz?type=italian'>
                        <div className='category-tile chinese-tile'>
                            <img className='category-icon' src={italian} alt='chinese' />
                            <p className='category-title'>
                                Italian
                            </p>
                        </div>
                    </a>
                </div>
                <span className='categories-gap' />
                <div className='categories-outer-container'>
                    <a className='category-link' href='/biz?type=japanese'>
                        <div className='category-tile chinese-tile'>
                            <img className='category-icon' src={japanese} alt='chinese' />
                            <p className='category-title'>
                                Japanese
                            </p>
                        </div>
                    </a>
                </div>
                </div>
                <div className='categories-container'>
                <div className='categories-outer-container'>
                    <a className='category-link' href='/biz?type=korean'>
                        <div className='category-tile chinese-tile'>
                            <img className='category-icon' src={korean} alt='chinese' />
                            <p className='category-title'>
                                Korean
                            </p>
                        </div>
                    </a>
                </div>
                <span className='categories-gap' />
                <div className='categories-outer-container'>
                    <a className='category-link' href='/biz?type=mexican'>
                        <div className='category-tile chinese-tile'>
                            <img className='category-icon' src={mexican} alt='chinese' />
                            <p className='category-title'>
                                Mexican
                            </p>
                        </div>
                    </a>
                </div>
                <span className='categories-gap' />
                <div className='categories-outer-container'>
                    <a className='category-link' href='/biz?type=thai'>
                        <div className='category-tile chinese-tile'>
                            <img className='category-icon' src={thai} alt='chinese' />
                            <p className='category-title'>
                                Thai
                            </p>
                        </div>
                    </a>
                </div>
                <span className='categories-gap' />
                <div className='categories-outer-container'>
                    <a className='category-link' href='/biz?type=vietnamese'>
                        <div className='category-tile chinese-tile'>
                            <img className='category-icon' src={vietnamese} alt='chinese' />
                            <p className='category-title'>
                                Vietnamese
                            </p>
                        </div>
                    </a>
                </div>
            </div>
        </div>
    </div>
  )
}

export default HomePage;
