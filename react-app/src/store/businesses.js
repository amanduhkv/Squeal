import { csrfFetch } from './csrf';

/* ----------------------------- ACTION TYPES: ----------------------------- */

const LOAD = 'businesses/LOAD';
const SEARCH = 'businesses/SEARCH';
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
    payload: business
});

export const createBusiness = (business) => async dispatch => {
    const response = await csrfFetch('/api/biz', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(business)
    });

    if (response.ok) {
        const newBiz = await response.json();
        console.log("ANY RESPONSE AFTER CREATE BIZ THUNK ACTION:", newBiz);
        // const res = await csrfFetch(`/api/business/${newBiz.id}/images`, {
        //     method: 'POST',
        //     headers: {
        //         'Content-Type': 'application/json'
        //     },
        //     body: JSON.stringify({
        //         url: previewImage,
        //         preview: true
        //     })
        // });

        // if (res.ok) {
            // const newImage = await res.json();

            dispatch(addBiz(newBiz));
            return newBiz;
        // }
    }
};

const addImg = (business, img) => ({
    type: ADD_IMG,
    business,
    img
});

export const addBizImg = (bizId, image) => async dispatch => {
    // const { businessId } = image;
    const responseGetBiz = await fetch(`/api/biz/${bizId}`);
    let Business;

    if (responseGetBiz.ok) {
        Business = await responseGetBiz.json();

        const responseAddImg = await csrfFetch(`/api/biz/${bizId}/images`, {
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

export const search = payload => ({
    type: SEARCH,
    payload
});

export const getAllBiz = () => async dispatch => {
    const response = await csrfFetch('/api/biz');gi
    // console.log("hitting res", response)
    if (response.ok) {
        const list = await response.json();
        // console.log("hitting list", list)
        dispatch(load(list));
    }
};


// Get user's businesses

export const getUsersBiz = () => async dispatch => {
    const response = await fetch(`/api/biz/current`);

    if (response.ok) {
        const list = await response.json();
        dispatch(load(list));
    }
};

// Get a business' details

const getOne = payload => ({
    type: GET_ONE,
    payload
});

export const getOneBiz = id => async dispatch => {
    const response = await fetch(`/api/biz/${id}`);

    if (response.ok) {
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

export const updateBiz = (bizId, updatedBiz) => async dispatch => {
    const response = await fetch(`/api/biz/${bizId}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(updatedBiz)
    });

    if (response.ok) {
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
    const response = await fetch(`/api/biz/${id}`, {
        method: 'DELETE'
    });

    if (response.ok) {
        const cool = await response.json();

        dispatch(deleteBiz(id));

        return cool;
    }
};


// Delete a business' image

const removeImg = (bizId, imageId) => ({
    type: REMOVE_IMG,
    payload: {
        bizId,
        imageId
    }
});

export const deleteImg = (bizId, imageId) => async dispatch => {
    const response = await fetch(`/api/biz/images/${imageId}`, {
        method: 'DELETE'
    });

    if (response.ok) {
        const success = await response.json();
        // console.log("THIS IS THUNK SUCCESS MSG:", success, imageId);
        dispatch(removeImg(bizId, imageId));
        return success;
    }
};


/* --------------------------- BUSINESSES REDUCER: --------------------------- */

export const clearData = () => ({
    type: CLEAR_DATA
});


const initialState = { allBusinesses: {}, singleBusiness: {} };


const businessReducer = (state = initialState, action) => {
    let newState;
    switch (action.type) {
        case LOAD:
            newState = { ...state, allBusinesses: { ...state.allBusinesses }, singleBusiness: { ...state.singleBusiness } };
            // console.log("LOAD_ALL ACTION.PAYLOAD IS:", action.payload);
            const newAllBusinesses = {};
            action.payload.Businesses.forEach(business => newAllBusinesses[business.id] = business);
            newState.allBusinesses = newAllBusinesses;
            // console.log("NEWSTATE AFTER LOAD_ALL ACTION:", newState);
            return newState;
        case SEARCH:
            newState = { ...state, allBusinesses: { ...state.allBusinesses }, singleBusiness: { ...state.singleBusiness } };
            // console.log("LOAD_ALL ACTION.PAYLOAD IS:", action.payload);
            const newSearchBusinesses = {};
            action.payload.forEach(business => newSearchBusinesses[business.id] = business);
            newState.allBusinesses = newSearchBusinesses;
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
            // console.log("NEWSTATE AFTER CREATE BIZ ACTION:", newState);
            return newState;
        case ADD_IMG:
            newState = { ...state, allBusinesses: { ...state.allBusinesses }, singleBusiness: { ...state.singleBusiness } };
            newState.singleBusiness = action.business;
            newState.singleBusiness.Business_Images.push(action.img);
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

            const userBizImages = newState.allBusinesses[action.payload.bizId].Business_Images;
            for (let i = 0; i < userBizImages.length; i++) {
                const img = userBizImages[i];
                if (img.id === action.payload.imageId) userBizImages.splice(i, 1);
            }


            // delete newState.allBusinesses.Business_Images.find(img => img.id === action.imageId);
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
