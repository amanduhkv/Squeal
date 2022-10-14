import { csrfFetch } from './csrf';

/* ----------------------------- ACTION TYPES: ----------------------------- */

const LOAD = 'businesses/LOAD';
const ADD = 'businesses/ADD';
const DELETE = 'businesses/DELETE';
const GET_ONE = 'businesses/GET_ONE';
const UPDATE = 'businesses/UPDATE';
const ADD_IMG = '/Businesses/ADD_IMG';
const REMOVE_IMG = 'bizimages/REMOVE_IMG';
const CLEAR_DATA = '/Businesses/CLEAR_DATA';


/* ---------------------------- ACTION CREATORS: ---------------------------- */
/********************************* CREATE *************************************/

// Add a business

const addBiz = (business) => ({
    type: ADD,
    business
});

export const createBusiness = (business, previewImage) => async dispatch => {
    const response = await csrfFetch('/api/business', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(business)
    });

    if(response.ok) {
        const newBiz = await response.json();
        const res = await csrfFetch(`/api/business/${newBiz.id}/images`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                url: previewImage,
                preview: true
            })
        });

        if(res.ok) {
            const newImage = await res.json();

            dispatch(addBiz(newBiz));
            return newBiz;
        }
    }
};

const addImg = (business, img) => ({
    type: ADD_IMG,
    business,
    img
});

export const addBizImg = image => async dispatch => {
    const { businessId } = image;
    const responseGetBiz = await fetch(`/api/businesses/${businessId}`);
    let Business;

    if (responseGetBiz.ok) {
        Business = await responseGetBiz.json();

        const responseAddImg = await csrfFetch(`/api/businesses/${businessId}/images`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(image)
        });

        if (responseAddImg.ok) {
            const imgData = await responseAddImg.json();
            // console.log("JSONIFIED Business IMG DATA AFTER THUNK:", img);
            await dispatch(addImg(Business, imgData));
            return imgData;
        }
    }
};


/********************************** READ **************************************/

// Get all businesses

const load = payload => ({
    type: LOAD,
    payload
});

export const getAllBiz = () => async dispatch => {
    const response = await fetch('/api/businesses');

    if(response.ok) {
        const list = await response.json();
        dispatch(load(list));
    }
};


// Get user's businesses

export const getUsersBiz = () => async dispatch => {
    const response = await fetch(`/api/businesses/current`);

    if (response.ok) {
        const list = await response.json();
        dispatch(load(list.Businesses));
    }
};

// Get a business' details

const getOne = payload => ({
    type: GET_ONE,
    payload
});

export const getOneBiz = id => async dispatch => {
    const response  = await fetch(`/api/businesses/${id}`);

    if(response.ok) {
        const biz = await response.json();

        dispatch(getOne(biz));
        return biz;
    }
};


/********************************* UPDATE *************************************/

// Update a business

const update = payload => ({
    type: UPDATE,
    payload
});

export const updateBiz = biz => async dispatch => {
    const response = await csrfFetch(`/api/businesses/${biz.id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(biz)
    });

    if(response.ok) {
        const updatedBiz = await response.json();

        dispatch(update(updatedBiz));

        return updatedBiz;
    }
};


/********************************* DELETE *************************************/

// Delete a business

const deleteBiz = bizId => ({
    type: DELETE,
    bizId
});

export const removeBiz = id => async dispatch => {
    const response = await csrfFetch(`/api/businesses/${id}`, {
        method: 'DELETE'
    });

    if(response.ok) {
        const cool = await response.json();

        dispatch(deleteBiz(id));

        return cool;
    }
};


// Delete a business' image

const removeImg = imageId => ({
    type: REMOVE_IMG,
    imageId
});

export const deleteImg = imageId => async dispatch => {
    const response = await csrfFetch(`/api/Business-images/${imageId}`, {
        method: 'DELETE'
    });

    if (response.ok) {
        const success = await response.json();
        // console.log("THIS IS THUNK SUCCESS MSG:", successMessage, imageId);
        dispatch(removeImg(imageId));
        return success;
    }
};


/* --------------------------- BUSINESSES REDUCER: --------------------------- */

export const clearData = () => ({
    type: CLEAR_DATA
});


const initialState = { allBusinesses: {}, singleBusiness: {}};


const businessReducer = (state = initialState, action) => {
    let newState;
    switch (action.type) {
        case LOAD:
            newState = { ...state, allBusinesses: { ...state.allBusinesses }, singleBusiness: { ...state.singleBusiness } };
            // console.log("LOAD_ALL ACTION.PAYLOAD IS:", action.payload);
            const newAllBusinesses = {};
            action.payload.forEach(business => newAllBusinesses[business.id] = business);
            newState.allBusinesses = newAllBusinesses;
            // console.log("NEWSTATE AFTER LOAD_ALL ACTION:", newState);
            return newState;
        case GET_ONE:
            newState = { ...state, allBusinesses: { ...state.allBusinesses }, singleBusiness: { ...state.singleBusiness } };
            // console.log("LOAD_ONE ACTION.PAYLOAD IS:", action.payload);
            const newSingleBusiness = { ...action.payload };
            newState.singleBusiness = newSingleBusiness;
            // console.log("NEWSTATE AFTER LOAD_ONE ACTION:", newState);
            return newState;
        case ADD:
            newState = { ...state, allBusinesses: { ...state.allBusinesses }, singleBusiness: { ...state.singleBusiness } };
            const newBusiness = { ...action.payload };
            newState.allBusinesses[action.payload.id] = newBusiness;
            // console.log("NEWSTATE AFTER ADD_Business ACTION:", newState);
            return newState;
        case ADD_IMG:
            newState = { ...state, allBusinesses: { ...state.allBusinesses }, singleBusiness: { ...state.singleBusiness } };
            newState.singleBusiness = action.business;
            newState.singleBusiness.businessImages.push(action.img);
            // console.log("NEWSTATE AFTER ADD_Business ACTION:", newState);
            return newState;
        case UPDATE:
            newState = { ...state, allBusinesses: { ...state.allBusinesses }, singleBusiness: { ...state.singleBusiness } };
            const updatedBusiness = { ...action.payload };
            newState.allBusinesses[action.payload.id] = updatedBusiness;
            // console.log("NEWSTATE AFTER ADD_Business ACTION:", newState);
            return newState;
        case DELETE:
            newState = { ...state, allBusinesses: { ...state.allBusinesses }, singleBusiness: { ...state.singleBusiness } };
            delete newState.allBusinesses[action.bizId];
            newState = { ...newState };
            // console.log("NEWSTATE AFTER REMOVE_Business ACTION:", newState);
            return newState;
        case REMOVE_IMG:
            newState = { ...state, allBusinesses: { ...state.allBusinesses }, singleBusiness: { ...state.singleBusiness } };
            delete newState.singleBusiness.businessImages.find(img => img.id === action.imageId);
            newState = { ...newState };
            // console.log("NEWSTATE AFTER REMOVE_Business ACTION:", newState);
            return newState;
        case CLEAR_DATA:
            return initialState;
        default:
            return state;
    }
};

export default businessReducer;
