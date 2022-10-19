import { csrfFetch } from './csrf';

/* ----------------------------- ACTION TYPES: ----------------------------- */
const LOAD_USER_REVIEWS = '/reviews/LOAD_USER_REVIEWS';
const LOAD_BUSINESS_REVIEWS = '/reviews/LOAD_BUSINESS_REVIEWS';
const ADD_REVIEW = '/reviews/ADD_REVIEW';
const ADD_REVIEW_IMG = '/reviews/ADD_REVIEW_IMG';
const EDIT_REVIEW = '/reviews/EDIT_REVIEW';
const REMOVE_REVIEW = '/reviews/REMOVE_REVIEW';
const REMOVE_REVIEW_IMG = '/reviews/REMOVE_REVIEW_IMG';
const CLEAR_DATA = '/reviews/CLEAR_DATA';


/* ---------------------------- ACTION CREATORS: ---------------------------- */
const loadUserReviews = (reviews) => ({
    type: LOAD_USER_REVIEWS,
    payload: reviews
});

const loadBusinessReviews = (reviews) => ({
    type: LOAD_BUSINESS_REVIEWS,
    payload: reviews
});

const addReview = (reviewData, userData, businessData) => ({
    type: ADD_REVIEW,
    payload: {
        reviewData,
        userData,
        businessData
    }
});

const addReviewImg = (reviewId, reviewImgData) => ({
    type: ADD_REVIEW_IMG,
    payload: {
        reviewId,
        reviewImgData
    }
});

const editReview = (reviewData, userData, businessData) => ({
    type: EDIT_REVIEW,
    payload: {
        reviewData,
        userData,
        businessData
    }
})

const removeReview = (reviewId) => ({
    type: REMOVE_REVIEW,
    payload: reviewId
});

const removeReviewImg = (reviewId, reviewImgId) => ({
    type: REMOVE_REVIEW_IMG,
    payload: {
        reviewId,
        reviewImgId
    }
});

export const clearData = () => ({
    type: CLEAR_DATA
});



/* ------------------------- THUNK ACTION CREATORS: ------------------------- */
export const getUserReviews = () => async dispatch => {
    const response = await csrfFetch(`/api/reviews/current`);

    if (response.ok) {
        const userReviews = await response.json();
        // console.log("JSONIFIED Reviews DATA AFTER THUNK:", userReviews);
        dispatch(loadUserReviews(userReviews));
        return userReviews;
    }
}

export const getBusinessReviews = (businessId) => async dispatch => {
    const response = await fetch(`/api/biz/${businessId}/reviews`);

    if (response.ok) {
        const businessReviews = await response.json();
        // console.log("JSONIFIED BUSINESS REVIEWS DATA AFTER THUNK:", businessReviews);
        dispatch(loadBusinessReviews(businessReviews));
        return businessReviews;
    }
}

export const createReview = (businessId, reviewData, userData, businessData) => async dispatch => {
    const response = await csrfFetch(`/api/biz/${businessId}/reviews`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(reviewData)
    });

    if (response.ok) {
        const newReview = await response.json();
        // console.log("JSONIFIED NEW-SPOT DATA AFTER THUNK:", newReview);
        dispatch(addReview(newReview, userData, businessData));
        return newReview;
    }
}

export const createReviewImg = (reviewId, reviewImgData) => async dispatch => {
    const response = await csrfFetch(`/api/reviews/${reviewId}/images`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(reviewImgData)
    });

    if (response.ok) {
        const newReviewImg = await response.json();
        // console.log("JSONIFIED NEW-BUSINESS DATA AFTER THUNK:", newReviewImg);
        dispatch(addReviewImg(reviewId, newReviewImg));
        return newReviewImg;
    }
}

export const updateReview = (reviewId, reviewData, userData, businessData) => async dispatch => {
    const response = await csrfFetch(`/api/reviews/${reviewId}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(reviewData)
    });

    if (response.ok) {
        const updatedReviewData = await response.json();
        // console.log("JSONIFIED UPDATED BUSINESS DATA AFTER THUNK:", updatedReviewData);
        dispatch(editReview(updatedReviewData, userData, businessData));
        return updatedReviewData;
    }
}

export const deleteReview = (reviewId) => async dispatch => {
    const response = await csrfFetch(`/api/reviews/${reviewId}`, {
        method: 'DELETE'
    });

    if (response.ok) {
        const successMessage = await response.json();
        // console.log("THIS IS THUNK SUCCESS MSG:", successMessage, ReviewId);
        dispatch(removeReview(reviewId));
        return successMessage;
    }
}

export const deleteReviewImg = (reviewId, reviewImgId) => async dispatch => {
    const response = await csrfFetch(`/api/review-images/${reviewImgId}`, {
        method: 'DELETE'
    });

    if (response.ok) {
        const successMessage = await response.json();
        // console.log("THIS IS THUNK SUCCESS MSG:", successMessage, ReviewId);
        dispatch(removeReviewImg(reviewId, reviewImgId));
        return successMessage;
    }
}


/* ---------------------------- REVIEWS REDUCER: ---------------------------- */
const initialState = { user: null, business: null };

const reviewsReducer = (state = initialState, action) => {
    let newState;
    switch (action.type) {
        case LOAD_USER_REVIEWS:
            newState = { ...state, user: { ...state.user } };
            // console.log("LOAD_USER_REVIEWS ACTION.PAYLOAD IS:", action.payload);
            const newUserReviews = {};
            action.payload.Reviews.forEach(review => newUserReviews[review.id] = review);
            newState.user = newUserReviews;
            // console.log("NEWSTATE AFTER LOAD_USER_REVIEWS ACTION:", newState);
            return newState;
        case LOAD_BUSINESS_REVIEWS:
            newState = { ...state, business: { ...state.business } };
            // console.log("LOAD_BUSINESS_REVIEWS ACTION.PAYLOAD IS:", action.payload);
            const newBusinessReviews = {};
            action.payload.Reviews.forEach(review => newBusinessReviews[review.id] = review);
            newState.business = newBusinessReviews;
            // console.log("NEWSTATE AFTER LOAD_BUSINESS_REVIEWS ACTION:", newState);
            return newState;
        case ADD_REVIEW:
            newState = { ...state, user: { ...state.user }, business: { ...state.business } };
            const newUserReview = { ...action.payload.reviewData, User: { ...action.payload.userData }, Spot: { ...action.payload.businessData } };
            const newBusinessReview = { ...action.payload.reviewData, User: { ...action.payload.userData } };
            newState.user[action.payload.reviewData.id] = newUserReview;
            newState.business[action.payload.reviewData.id] = newBusinessReview;
            // console.log("NEWSTATE AFTER ADD_REVIEW ACTION:", newState);
            return newState;
        case ADD_REVIEW_IMG:
            newState = { ...state, user: { ...state.user }, business: { ...state.business } };
            newState.user[action.payload.reviewId].ReviewImages ? newState.user[action.payload.reviewId].ReviewImages = [...state.user[action.payload.reviewId].ReviewImages] : newState.user[action.payload.reviewId].ReviewImages = []

            const newReviewImg = { ...action.payload.reviewImgData };

            newState.user[action.payload.reviewId].ReviewImages.push(newReviewImg);
            // console.log("NEWSTATE AFTER ADD_REVIEW_IMG ACTION:", newState);
            return newState;
        case EDIT_REVIEW:
            newState = { ...state, user: { ...state.user }, business: { ...state.business } };
            const updatedUserReview = { ...action.payload.reviewData, User: { ...action.payload.userData }, Spot: { ...action.payload.businessData } };
            const updatedBusinessReview = { ...action.payload.reviewData, User: { ...action.payload.userData } };
            newState.user[action.payload.reviewData.id] = updatedUserReview;
            newState.business[action.payload.reviewData.id] = updatedBusinessReview;
            // console.log("NEWSTATE AFTER EDIT_REVIEW ACTION:", newState);
            return newState;
        case REMOVE_REVIEW:
            newState = { ...state, user: { ...state.user }, business: { ...state.business } };
            delete newState.user[action.payload];
            delete newState.business[action.payload];
            newState = { ...newState };
            // console.log("NEWSTATE AFTER REMOVE_REVIEW ACTION:", newState);
            return newState;
        case REMOVE_REVIEW_IMG:
            newState = { ...state, user: { ...state.user }, business: { ...state.business } };
            newState.user[action.payload.reviewId].ReviewImages = [...state.user[action.payload.reviewId].ReviewImages]

            const userReviewImages = newState.user[action.payload.reviewId].ReviewImages;
            for (let i = 0; i < userReviewImages.length; i++) {
                const img = userReviewImages[i];
                if (img.id === action.payload.reviewImgId) userReviewImages.splice(i, 1);
            }

            newState = { ...newState };
            // console.log("NEWSTATE AFTER REMOVE_REVIEW_IMG ACTION:", newState);
            return newState;
        case CLEAR_DATA:
            return initialState;
        default:
            return state;
    }
};

export default reviewsReducer;
