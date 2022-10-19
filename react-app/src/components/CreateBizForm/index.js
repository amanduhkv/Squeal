import React, { useState, useEffect } from 'react'
import { useHistory } from 'react-router-dom';
import { useDispatch, useSelector } from "react-redux";
import * as bizActions from "../../store/businesses";
import './CreateBizForm.css'

export default function CreateBizForm() {
    const dispatch = useDispatch();
    const history = useHistory();
    const sessionUser = useSelector(state => state.session.user);
    const [name, setName] = useState("");
    const [address, setAddress] = useState("");
    const [city, setCity] = useState("");
    const [state, setState] = useState("");
    const [zipcode, setZipcode] = useState("");
    const [lat, setLat] = useState("");
    const [lng, setLng] = useState("");
    const [country, setCountry] = useState("United States");
    const [phone, setPhone] = useState("");
    const [startTime, setStartTime] = useState("0600");
    const [endTime, setEndTime] = useState("2130");
    const [priceRange, setPriceRange] = useState("$");
    const [types, setTypes] = useState([]);
    const [transactions, setTransactions] = useState([]);

    const [bizImgUrl, setBizImgUrl] = useState("");

    const [validationErrors, setValidationErrors] = useState([]);

    // FOR SELECT OPTIONS:
    const PRICE_RANGES = ["$", "$$", "$$$", "$$$$"];
    const BIZ_HOURS = [ ["0000", "12:00am"], ["0030", "12:30am"], ["0100", "1:00am"], ["0130", "1:30am"], ["0200", "2:00am"], ["0230", "2:30am"], ["0300", "3:00am"], ["0330", "3:30am"], ["0400", "4:00am"], ["0430", "4:30am"], ["0500", "5:00am"], ["0530", "5:30am"], ["0600", "6:00am"], ["0630", "6:30am"], ["0700", "7:00am"], ["0730", "7:30am"], ["0800", "8:00am"], ["0830", "8:30am"], ["0900", "9:00am"], ["0930", "9:30am"], ["1000", "10:00am"], ["1030", "10:30am"], ["1100", "11:00am"], ["1130", "11:30am"], ["1200", "12:00pm"], ["1230", "12:30pm"], ["1300", "1:00pm"], ["1330", "1:30pm"], ["1400", "2:00pm"], ["1430", "2:30pm"], ["1500", "3:00pm"], ["1530", "3:30pm"], ["1600", "4:00pm"], ["1630", "4:30pm"], ["1700", "5:00pm"], ["1730", "5:30pm"], ["1800", "6:00pm"], ["1830", "6:30pm"], ["1900", "7:00pm"], ["1930", "7:30pm"], ["2000", "8:00pm"], ["2030", "8:30pm"], ["2100", "9:00pm"], ["2130", "9:30pm"], ["2200", "10:00pm"], ["2230", "10:30pm"], ["2300", "11:00pm"], ["2330", "11:30pm"] ];
    const TYPES = [ { 'alias': 'bakeries', 'title': 'Bakeries' }, { 'alias': 'bubbletea', 'title': 'Bubble Tea' }, { 'alias': 'cocktailbars', 'title': 'Cocktails' }, { 'alias': 'bars', 'title': 'Bars' }, { 'alias': 'brazilian', 'title': 'Brazilian' }, { 'alias': 'coffee', 'title': 'Coffee & Tea' }, { 'alias': 'chickenshop', 'title': 'Chicken Shop' }, { 'alias': 'desserts', 'title': 'Desserts' }, { 'alias': 'donuts', 'title': 'Donuts' }, { 'alias': 'dimsum', 'title': 'Dim Sum' }, { 'alias': 'ethiopian', 'title': 'Ethiopian' }, { 'alias': 'icecream', 'title': 'Ice Cream & Froyo' }, { 'alias': 'juicebars', 'title': 'Juice Bars & Smoothies' }, { 'alias': 'bbq', 'title': 'Barbeque' }, { 'alias': 'breakfast_brunch', 'title': 'Breakfast & Brunch' }, { 'alias': 'burgers', 'title': 'Burgers' }, { 'alias': 'cafes', 'title': 'Cafes' }, { 'alias': 'chicken_wings', 'title': 'Chicken Wings' }, { 'alias': 'chinese', 'title': 'Chinese' }, { 'alias': 'gluten_free', 'title': 'Gluten-Free' }, { 'alias': 'german', 'title': 'German' }, { 'alias': 'gastropubs', 'title': 'Gastropubs' }, { 'alias': 'french', 'title': 'French' }, { 'alias': 'hotdogs', 'title': 'Fast Food' }, { 'alias': 'indpak', 'title': 'Indian' }, { 'alias': 'latin', 'title': 'Latin' }, { 'alias': 'italian', 'title': 'Italian' }, { 'alias': 'japanese', 'title': 'Japanese' }, { 'alias': 'korean', 'title': 'Korean' }, { 'alias': 'newamerican', 'title': 'American (New)' }, { 'alias': 'mediterranean', 'title': 'Mediterranean' }, { 'alias': 'mexican', 'title': 'Mexican' }, { 'alias': 'pizza', 'title': 'Pizza' }, { 'alias': 'ramen', 'title': 'Ramen' }, { 'alias': 'noodles', 'title': 'Noodles' }, { 'alias': 'raw_food', 'title': 'Raw Food' }, { 'alias': 'salad', 'title': 'Salad' }, { 'alias': 'sandwiches', 'title': 'Sandwiches' }, { 'alias': 'soulfood', 'title': 'Soul Food' }, { 'alias': 'soup', 'title': 'Soup' }, { 'alias': 'seafood', 'title': 'Seafood' }, { 'alias': 'steak', 'title': 'Steakhouses' }, { 'alias': 'sushi', 'title': 'Sushi Bars' }, { 'alias': 'tacos', 'title': 'Tacos' }, { 'alias': 'tradamerican', 'title': 'American (Traditional)' }, { 'alias': 'taiwanese', 'title': 'Taiwanese' }, { 'alias': 'thai', 'title': 'Thai' }, { 'alias': 'tapasmallplates', 'title': 'Tapas/Small Plates' }, { 'alias': 'vegetarian', 'title': 'Vegetarian' }, { 'alias': 'vegan', 'title': 'Vegan' }, { 'alias': 'vietnamese', 'title': 'Vietnamese' }, {'alias': 'waffles', 'title': 'Waffles' } ]
    const TRANSACTIONS = [['pickup', 'Pickup'], ['delivery', 'Deliver'], ['restaurant_reservation', 'Restaurant Reservation']]

    if (!sessionUser) {
        alert("Please log in or create an account to create a business.");
        history.push("/");
    }

    // TODO: ADD MORE VALIDATION ERROR HANDLING
    useEffect(() => {
        const errors = [];

        if (Number.isNaN(Number(lat)) ||
            (Number(lat)) > 90 ||
            (Number(lat)) < -90)
            errors.push("Latitude must be a number between -90.0 and 90.0");

        if (Number.isNaN(Number(lng)) ||
            (Number(lng)) > 180 ||
            (Number(lng)) < -180)
            errors.push("Longitude must be a number between -180.0 and 180.0");

        setValidationErrors(errors);
    }, [lat, lng]);

    const handleSubmit = async (e) => {
        e.preventDefault();

        const newBiz = {
            name,
            address,
            city,
            state,
            zipcode,
            lat: +lat,
            lng: +lng,
            country,
            phone_number: phone,
            start_time: startTime,
            end_time: endTime,
            price_range: priceRange,
            transactions,
            types
        }

        console.log("NEW BIZ AFTER SUBMIT:", newBiz);

        try {
            const createdBiz = await dispatch(bizActions.createBusiness(newBiz));
            if (createdBiz) {
                if (bizImgUrl.length) {
                    const newImg = { url: bizImgUrl }
                    try {
                        const createdImg = await dispatch(bizActions.addBizImg(createdBiz.id, newImg));
                        if (createdImg) setValidationErrors([]);
                    }
                    catch (res) {
                        console.log("==>ANY ERRORS FROM CREATE BIZ IMG:", res)
                        // const data = await res.json();
                        // if (data && data.errors) return setValidationErrors(data.errors);
                    }
                }

                setValidationErrors([]);
                history.replace(`/biz/${createdBiz.id}`);
            }
        }

        catch (res) {
            console.log("==>ANY ERRORS FROM CREATE BIZ:", res)
            // const data = await res.json();
            // if (data && data.errors) return setValidationErrors(data.errors);
        }
    };

    return (
        <div className='form form--create-biz'>
            <h1 className='header header--create-biz'>Hello! Let's fill out your business details</h1>

            <form onSubmit={handleSubmit} className="form" id="form--create-biz">
                {validationErrors.length > 0 && (
                    <ul className="list list--errors">
                        {validationErrors.map((error) => <li key={error} className="li li--error">{error}</li>)}
                    </ul>
                )}

                <div className='container container--form-fields'>

                    {/* ----- NAME SECTION ----- */}
                    <div className='container container--form-fields--section container--form-fields--name-section'>
                        <label className='label--create-biz' htmlFor="form-field--name">Business Name:</label>
                        <input
                            type="text"
                            value={name}
                            onChange={(e) => setName(e.target.value)}
                            required
                            placeholder='Business name'
                            className='form-field'
                            id='form-field--name'
                        />
                    </div>

                    {/* ----- ADDRESS SECTION ----- */}
                    <div className='container container--form-fields--section container--form-fields--address-info-section'>
                        <label className='label--create-biz' htmlFor="form-field--address">Business Address:</label>
                        <div className='container container--form-fields--address-info-section--address'>
                            <input
                                type="text"
                                value={address}
                                onChange={(e) => setAddress(e.target.value)}
                                required
                                placeholder='Address'
                                className='form-field'
                                id='form-field--address'
                            />
                        </div>

                        <div className='container container--form-fields--address-info-section--city-state-zip'>
                            <input
                                type="text"
                                value={city}
                                onChange={(e) => setCity(e.target.value)}
                                required
                                placeholder='City'
                                className='form-field'
                                id='form-field--city'
                            />

                            <input
                                type="text"
                                value={state}
                                onChange={(e) => setState(e.target.value)}
                                required
                                placeholder='State'
                                className='form-field'
                                id='form-field--state'
                            />

                            <input
                                type="text"
                                value={zipcode}
                                onChange={(e) => setZipcode(e.target.value)}
                                required
                                placeholder='Zipcode'
                                className='form-field'
                                id='form-field--zipcode'
                            />
                        </div>

                        <div className='container container--form-fields--address-info-section--country-lat-lng'>
                            <input
                                type="text"
                                value={lat}
                                onChange={(e) => setLat(e.target.value)}
                                required
                                placeholder='Latitude'
                                className='form-field'
                                id='form-field--lat'
                            />

                            <input
                                type="text"
                                value={lng}
                                onChange={(e) => setLng(e.target.value)}
                                required
                                placeholder='Longitude'
                                className='form-field'
                                id='form-field--lng'
                            />

                            <input
                                type="text"
                                value={country}
                                onChange={(e) => setCountry(e.target.value)}
                                required
                                placeholder='Country'
                                className='form-field'
                                id='form-field--country'
                            />
                        </div>
                    </div>

                    {/* ----- NAME SECTION ----- */}
                    <div className='container container--form-fields--section container--form-fields--phone-section'>
                        <label className='label--create-biz' htmlFor="form-field--phone">Phone Number:</label>
                        <input
                            type="tel"
                            value={phone}
                            onChange={(e) => setPhone(e.target.value)}
                            required
                            placeholder='(123) 456-7890'
                            className='form-field'
                            id='form-field--phone'
                        />
                    </div>


                    {/* ----- HOURS SECTION ----- */}
                    <div className='container container--form-fields--section container--form-fields--hours-section'>
                        <div className='container container--form-fields--hours-section--start'>
                            <label className='label--create-biz' htmlFor="form-field--start-time">Business Start Time:</label>
                            <select
                                value={startTime}
                                onChange={e => setStartTime(e.target.value)}
                                required
                                className='form-field'
                                id='form-field--start-time'
                                >
                                {BIZ_HOURS.map(hour => (
                                    <option value={hour[0]} key={hour}>{hour[1]}</option>
                                ))}
                            </select>
                        </div>

                        <div className='container container--form-fields--hours-section--end'>
                            <label className='label--create-biz' htmlFor="form-field--end-time">Business End Time:</label>
                            <select
                                value={endTime}
                                onChange={e => setEndTime(e.target.value)}
                                required
                                className='form-field'
                                id='form-field--end-time'
                            >
                                {BIZ_HOURS.map(hour => (
                                    <option value={hour[0]} key={hour}>{hour[1]}</option>
                                ))}
                            </select>
                        </div>
                    </div>

                    {/* ----- PRICE RANGE SECTION ----- */}
                    <div className='container container--form-fields--section container--form-fields--price-range-section'>
                        <label className='label--create-biz' htmlFor="form-field--price-range">Price Range:</label>
                        <select
                            value={priceRange}
                            onChange={e => setPriceRange(e.target.value)}
                            required
                            className='form-field'
                            id='form-field--price-range'
                        >
                            {PRICE_RANGES.map(p => (
                                <option value={p} key={p}>{p}</option>
                            ))}
                        </select>
                    </div>

                    {/* ----- TYPES & TRANSACTIONS SECTION ----- */}
                    <div className='container container--form-fields--section container--form-fields--types-transactions-section'>

                        <div className='container container--form-fields--types-transactions-section--transactions'>
                            <label className='label--create-biz label--create-biz-transactions' htmlFor="form-field--transactions">Transactions:</label>
                            <div className='container container--form-fields--transactions-checkboxes-section'>
                                {TRANSACTIONS.map(transaction => (
                                    <div id='single-transaction' key={transaction[0]}>
                                        <input
                                            type="checkbox"
                                            className='form-field--checkbox'
                                            id='form-field--transactions'
                                            onChange={
                                                (e) => {
                                                    const transactionsList = transactions;
                                                    if (e.target.checked) {
                                                        // console.log("ADDING TO TRANSACTIONS LIST!");
                                                        transactionsList.push(e.target.value);
                                                        // console.log("TRANSACTIONS IS NOW:", transactionsList);
                                                    }
                                                    else {
                                                        // console.log("REMOVING FROM TRANSACTIONS LIST");
                                                        const i = transactionsList.indexOf(e.target.value);
                                                        transactionsList.splice(i, 1);
                                                        // console.log("TRANSACTIONS IS NOW:", transactionsList);
                                                    }

                                                    setTransactions(transactionsList);
                                                }
                                            }
                                            value={transaction[0]}
                                            name={transaction[0]}
                                        />
                                        <label
                                            htmlFor={transaction[0]}
                                            className='label--create-biz-transaction'
                                        >
                                            {transaction[1]}
                                        </label>
                                    </div>
                                ))}
                            </div>
                        </div>

                        <div className='container container--form-fields--types-transactions-section--types'>
                            <label className='label--create-biz label--create-biz-types' htmlFor="form-field--transactions">Types:</label>
                            <div className='container container--form-fields--types-checkboxes-section'>
                            {TYPES.map(type => (
                                <div id='single-type' key={type.alias}>
                                    <input
                                        type="checkbox"
                                        className='form-field--checkbox'
                                        id='form-field--types'
                                        onChange={
                                            (e) => {
                                                const typesList = types;
                                                if (e.target.checked) {
                                                    // console.log("ADDING TO TYPES LIST!");
                                                    typesList.push(e.target.value);
                                                    // console.log("TYPESLIST IS NOW:", typesList);
                                                }
                                                else {
                                                    // console.log("REMOVING FROM TYPES LIST");
                                                    const i = typesList.indexOf(e.target.value);
                                                    typesList.splice(i, 1);
                                                    // console.log("TYPESLIST IS NOW:", typesList);
                                                }

                                                setTypes(typesList);
                                            }
                                        }
                                        value={type.alias}
                                        name={type.alias}
                                        />
                                    <label
                                        htmlFor={type.alias}
                                        className='label--create-biz-type'
                                    >
                                        {type.title}
                                    </label>
                                </div>
                            ))}
                            </div>
                        </div>
                    </div>

                    {/* ----- BIZ IMG SECTION ----- */}
                    <div className='container container--form-fields--section container--form-fields--img-section'>
                        <label className='label--create-biz' htmlFor="form-field--img">Business Preview Image:</label>
                        <input
                            type="text"
                            value={bizImgUrl}
                            onChange={(e) => setBizImgUrl(e.target.value)}
                            required
                            placeholder='Business Image url'
                            className='form-field'
                            id='form-field--img'
                        />
                        {bizImgUrl && <img className='img img--create-biz-url-preview' src={bizImgUrl} alt={bizImgUrl} />}
                    </div>
                </div>

                <button
                    type="submit"
                    disabled={validationErrors.length}
                    className='button button--submit'
                    id='create-biz-submit-button'
                >
                    Submit
                </button>
            </form>
        </div>
    );
}
