import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import * as reviewActions from "../../store/reviews";

export default function UserReviews({ user }) {
    const dispatch = useDispatch();
    const userReviews = useSelector(state => state.reviews.user);
    console.log("USER REVIEWS:", userReviews);

    useEffect(() => {
        dispatch(reviewActions.getUserReviews());

        return () => dispatch(reviewActions.clearData());
    }, [dispatch]);

    if (!userReviews || !Object.values(userReviews).length) {
        return (
            <div>
                <h2 id='mid-title'>Reviews</h2>
                <div>You haven't made any reviews yet.</div>
            </div>
        )
    }

    else return (
        <div>
            <h2 id='mid-title'>Reviews</h2>
            <div className="all-user-reviews">
                {userReviews && Object.values(userReviews).map(review => (
                    <div className="single-user-review-card" key={review.id}>
                        <div className="user-review-biz-info">
                            <div>{review.Business.name}</div>
                            <div>{review.Business.address}</div>
                            <div>
                                <span>{review.Business.city}</span>
                                <span>{review.Business.state}</span>
                                <span>{review.Business.zipcode}</span>
                            </div>
                        </div>
                        <div className="user-review-review-info">
                            <div className="user-review-rating">{review.rating}</div>
                            <p className="user-review-review-body">{review.review_body}</p>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    )

}
