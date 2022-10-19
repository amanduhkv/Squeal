import React, { useState, useEffect } from 'react'
import { useHistory, useParams } from 'react-router-dom';
import { useDispatch, useSelector } from "react-redux";
import * as reviewActions from "../../store/reviews";
import './CreateReviewImgForm.css'

export default function CreateReviewImgForm() {
    const dispatch = useDispatch();
    const history = useHistory();
    const { reviewId } = useParams();
    const sessionUser = useSelector(state => state.session.user);
    const userReviews = useSelector(state => state.reviews.user);
    let review;
    console.log("USER REVIEWS:", userReviews)
    // if (userReviews) review = userReviews

    const [reviewImgUrl, setreviewImgUrl] = useState("");

    const [validationErrors, setValidationErrors] = useState([]);

    if (!sessionUser) {
        alert("Please log in or create an account to add an image to your review.");
        history.push("/");
    }

    // LOAD review BY PARAMETER review ID
    useEffect(() => {
        dispatch(reviewActions.getUserReviews());

        return () => dispatch(reviewActions.clearData());
    }, [dispatch, reviewId]);

    // TODO: ADD MORE VALIDATION ERROR HANDLING
    useEffect(() => {
        const errors = [];

        setValidationErrors(errors);
    }, [reviewImgUrl]);

    const handleSubmit = async (e) => {
        e.preventDefault();

        // HANDLING FOR USERS WHO HARDCODE ADD review IMG PAGE:
        if (sessionUser && review) {
            if ((sessionUser.id !== review.owner_id)) {
                alert("Only the review owner can update his or her review.");
                history.push("/");
                return;
            }
        }

        const newImg = { url: reviewImgUrl }
        try {
            const createdImg = await dispatch(reviewActions.createReviewImg(reviewId, newImg));
            if (createdImg) setValidationErrors([]);
            history.push(`/review/${reviewId}`);
        }
        catch (res) {
            console.log("==>ANY ERRORS FROM CREATE REVIEW IMG:", res)
            // const data = await res.json();
            // if (data && data.errors) return setValidationErrors(data.errors);
        }
    };

    return (
        <div className='form form--add-review-img'>
            <h1 className='header header--add-review-img'>Hello! Let's add an image to your review</h1>

            <form onSubmit={handleSubmit} className="form" id="form--add-review-img">
                {validationErrors.length > 0 && (
                    <ul className="list list--errors">
                        {validationErrors.map((error) => <li key={error} className="li li--error">{error}</li>)}
                    </ul>
                )}

                <div className='container container--form-fields'>
                    {/* ----- review IMG SECTION ----- */}
                    <div className='container container--form-fields--section container--form-fields--img-section'>
                        <label className='label--add-review-img' htmlFor="form-field--img">Review Preview Image:</label>
                        <input
                            type="text"
                            value={reviewImgUrl}
                            onChange={(e) => setreviewImgUrl(e.target.value)}
                            required
                            placeholder='Business Image url'
                            className='form-field'
                            id='form-field--img'
                        />
                        {reviewImgUrl && <img className='img img--add-review-img-url-preview' src={reviewImgUrl} alt={reviewImgUrl} />}
                    </div>
                </div>

                <button
                    type="submit"
                    disabled={validationErrors.length}
                    className='button button--submit'
                    id='add-review-img-submit-button'
                >
                    Submit
                </button>
            </form>
        </div>
    );
}
