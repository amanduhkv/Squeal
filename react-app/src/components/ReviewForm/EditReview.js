import React, { useEffect, useState, useRef } from 'react'
import './ReviewForm.css';
import { useParams, useHistory } from 'react-router-dom';
import { useSelector, useDispatch } from 'react-redux';
import * as bizActions from '../../store/businesses';
// import { getOneBiz } from '../../store/businesses';
import * as reviewActions from '../../store/reviews';
// import { getUserReviews, updateReview } from '../../store/reviews';

const EditReview = () => {
    const history = useHistory();
    const dispatch = useDispatch();
    const { bizId, reviewId } = useParams();
    const reviews = useSelector(state => state.reviews.user);
    let review;
    if (reviews) review = reviews[reviewId];
    const biz = useSelector(state => state.businesses.singleBusiness);
    const user = useSelector(state => state.session.user);
    const [hover1, isHover1] = useHover();
    const [hover2, isHover2] = useHover();
    const [hover3, isHover3] = useHover();
    const [hover4, isHover4] = useHover();
    const [hover5, isHover5] = useHover();
    const [revRate, setRevRate] = useState(review?.rating ?? 0);
    const [revBody, setRevBody] = useState(review?.review_body ?? '');
    const [validationErrors, setValidationErrors] = useState([]);

    useEffect(() => {
        dispatch(bizActions.getOneBiz(bizId));
        dispatch(reviewActions.getUserReviews(reviewId));

        return () => {
            dispatch(bizActions.clearData());
            dispatch(reviewActions.clearData());
        }
    }, [dispatch, bizId, reviewId]);

    if (!user) {
        alert("Please log in or create an account to edit a review.");
        history.push(`/biz/${bizId}`);
    }

    const handleSubmit = async (e) => {
        e.preventDefault();

        const updatedRev = {
            rating: revRate,
            review_body: revBody
        };

        const newRev = await dispatch(reviewActions.updateReview(reviewId, updatedRev, user, biz));

        if (newRev) {
            setValidationErrors([]);
            history.push(`/biz/${bizId}`)
        }
    }

    // ERROR HANDLING:
    useEffect(() => {
        const errors = [];

        if (revRate < 1) {
            errors.push("Please provide a rating");
        }

        if (revBody.length < 1) {
            errors.push("Please provide a review");
        }

        setValidationErrors(errors);
    }, [revRate, revBody]);

    return (
        <div className='editreview-page-container'>
            <div className='editreview-container'>
                <div className='new-review-inner'>
                    <h1 className='new-review-title'>{biz.name}</h1>
                    <form className='new-review-form' onSubmit={handleSubmit}>
                        <div className='new-review-form-inner'>
                            <div className='new-review-stars'>
                                {/* FIRST STAR */}
                                <svg ref={hover1} onClick={() => setRevRate(1)}
                                    id={isHover1 ? 'one' : isHover2 ? 'two' : isHover3 ? 'three' : isHover4 ? 'four' : isHover5 ? 'five' : ''}
                                    className={revRate > 4 ? 'big-first-star new-star star1 five' : revRate > 3 ? 'big-first-star new-star star1 four' : revRate > 2 ? 'big-first-star new-star star1 three' : revRate > 1 ? 'big-first-star new-star star1 two' : revRate > 0 ? 'big-first-star new-star star1 one' : 'big-first-star new-star star1'}
                                    width="32" height="32" viewBox="0 0 20 20">
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
                                    onClick={() => setRevRate(2)}
                                    className={revRate > 4 ? 'big-middle-star new-star star2 five' : revRate > 3 ? 'big-middle-star new-star star2 four' : revRate > 2 ? 'big-middle-star new-star star2 three' : revRate > 1 ? 'big-middle-star new-star star2 two' : 'big-middle-star new-star star2'}
                                    width="32" height="32" viewBox="0 0 20 20">
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
                                <svg ref={hover3} id={isHover1 ? 'grey' : isHover2 ? 'grey' : isHover3 ? 'three' : isHover4 ? 'four' : isHover5 ? 'five' : ''}
                                    onClick={() => setRevRate(3)}
                                    className={revRate > 4 ? 'big-middle-star new-star star3 five' : revRate > 3 ? 'big-middle-star new-star star3 four' : revRate > 2 ? 'big-middle-star new-star star3 three' : 'big-middle-star new-star star3'}
                                    width="32" height="32" viewBox="0 0 20 20">
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
                                <svg ref={hover4} id={isHover1 ? 'grey' : isHover2 ? 'grey' : isHover3 ? 'grey' : isHover4 ? 'four' : isHover5 ? 'five' : ''}
                                    onClick={() => setRevRate(4)}
                                    className={revRate > 4 ? 'big-middle-star new-star star4 five' : revRate > 3 ? 'big-middle-star new-star star4 four' : 'big-middle-star new-star star4'}
                                    width="32" height="32" viewBox="0 0 20 20">
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
                                <svg ref={hover5} id={isHover1 ? 'grey' : isHover2 ? 'grey' : isHover3 ? 'grey' : isHover4 ? 'grey' : isHover5 ? 'five' : ''}
                                    onClick={() => setRevRate(5)}
                                    className={revRate > 4 ? 'big-last-star new-star star5 five' : 'big-last-star new-star star5'}
                                    width="32" height="32" viewBox="0 0 20 20">
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

                        {validationErrors.length > 0 && (
                            <ul id="list-errors-review" className="list--errors">
                                {validationErrors.map((error) => <li key={error} className="li li--error">{error}</li>)}
                            </ul>
                        )}

                        <button type='submit' className='new-review-submit'>Update Review</button>
                    </form>
                </div>
            </div>
        </div>
    )
}

export default EditReview;

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
