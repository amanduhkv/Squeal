import React, { useState, useEffect } from 'react'
import { useHistory } from 'react-router-dom';
import { useDispatch, useSelector } from "react-redux";
import * as bizActions from "../../store/businesses";
import './CreateBizForm.css'

export default function CreateBizForm() {
    const dispatch = useDispatch();
    const history = useHistory();
    const sessionUser = useSelector((state) => state.session.user);
    const [name, setName] = useState("");
    const [address, setAddress] = useState("");
    const [city, setCity] = useState("");
    const [state, setState] = useState("");
    const [country, setCountry] = useState("United States");
    const [zipcode, setZipcode] = useState("");
    const [lat, setLat] = useState("");
    const [lng, setLng] = useState("");
    const [priceRange, setPriceRange] = useState("$");
    const [phone, setPhone] = useState("");
    const [startTime, setStartTime] = useState("0600");
    const [endTime, setEndTime] = useState("2130");

    const [bizImgUrl, setBizImgUrl] = useState("");

    const [validationErrors, setValidationErrors] = useState([]);

    // FOR SELECT OPTIONS:
    const PRICE_RANGES = ["$", "$$", "$$$", "$$$$"];
    const BIZ_HOURS = [ ["0000", "12:00am"], ["0030", "12:30am"], ["0100", "1:00am"], ["0130", "1:30am"], ["0200", "2:00am"], ["0230", "2:30am"], ["0300", "3:00am"], ["0330", "3:30am"], ["0400", "4:00am"], ["0430", "4:30am"], ["0500", "5:00am"], ["0530", "5:30am"], ["0600", "6:00am"], ["0630", "6:30am"], ["0700", "7:00am"], ["0730", "7:30am"], ["0800", "8:00am"], ["0830", "8:30am"], ["0900", "9:00am"], ["0930", "9:30am"], ["1000", "10:00am"], ["1030", "10:30am"], ["1100", "11:00am"], ["1130", "11:30am"], ["1200", "12:00pm"], ["1230", "12:30pm"], ["1300", "1:00pm"], ["1330", "1:30pm"], ["1400", "2:00pm"], ["1430", "2:30pm"], ["1500", "3:00pm"], ["1530", "3:30pm"], ["1600", "4:00pm"], ["1630", "4:30pm"], ["1700", "5:00pm"], ["1730", "5:30pm"], ["1800", "6:00pm"], ["1830", "6:30pm"], ["1900", "7:00pm"], ["1930", "7:30pm"], ["2000", "8:00pm"], ["2030", "8:30pm"], ["2100", "9:00pm"], ["2130", "9:30pm"], ["2200", "10:00pm"], ["2230", "10:30pm"], ["2300", "11:00pm"], ["2330", "11:30pm"] ];

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
            country,
            lat: +lat,
            lng: +lng,
            price_range: priceRange,
            phone_number: phone,
            start_time: startTime,
            end_time: endTime,
            zipcode
        }

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
                        const data = await res.json();
                        if (data && data.errors) return setValidationErrors(data.errors);
                    }
                }

                setValidationErrors([]);
                history.replace(`/biz/${createdBiz.id}`);
            }
        }

        catch (res) {
            const data = await res.json();
            console.log("==>ANY ERRORS FROM CREATE BIZ:", res)
            if (data && data.errors) return setValidationErrors(data.errors);
        }
    };

    return (
        <div className='form form--create-biz'>
            <h1>Hello! Let's fill out your business details</h1>

            <form onSubmit={handleSubmit} className="form" id="form--create-spot">
                {validationErrors.length > 0 && (
                    <ul className="list list--errors">
                        {validationErrors.map((error) => <li key={error} className="li li--error">{error}</li>)}
                    </ul>
                )}

                <div className='container container--form-fields'>

                    {/* ----- NAME SECTION ----- */}
                    <div className='container container--form-fields--section container--form-fields--name-section'>
                        <label className='label--create-biz' for="form-field--name">Business Name:</label>
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
                        <label className='label--create-biz' for="form-field--address">Business Address:</label>
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
                        <label className='label--create-biz' for="form-field--phone">Phone Number:</label>
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
                            <label className='label--create-biz' for="form-field--start-time">Business Start Time:</label>
                            <select
                                value={startTime}
                                onChange={e => setStartTime(e.target.value)}
                                required
                                className='form-field'
                                id='form-field--start-time'
                                >
                                {BIZ_HOURS.map(hour => (
                                    <option value={hour[0]}>{hour[1]}</option>
                                    ))}
                            </select>
                        </div>

                        <div className='container container--form-fields--hours-section--end'>
                            <label className='label--create-biz' for="form-field--end-time">Business End Time:</label>
                            <select
                                value={endTime}
                                onChange={e => setStartTime(e.target.value)}
                                required
                                className='form-field'
                                id='form-field--end-time'
                            >
                                {BIZ_HOURS.map(hour => (
                                    <option value={hour[0]}>{hour[1]}</option>
                                ))}
                            </select>
                        </div>
                    </div>

                    {/* ----- PRICE RANGE SECTION ----- */}
                    <div className='container container--form-fields--section container--form-fields--price-range-section'>
                        <label className='label--create-biz' for="form-field--price-range">Price Range:</label>
                        <select
                            value={priceRange}
                            onChange={e => setPriceRange(e.target.value)}
                            required
                            className='form-field'
                            id='form-field--price-range'
                        >
                            {PRICE_RANGES.map(p => (
                                <option value={p}>{p}</option>
                            ))}
                        </select>
                    </div>

                    {/* ----- BIZ IMG SECTION ----- */}
                    <div className='container container--form-fields--section container--form-fields--img-section'>
                        <label className='label--create-biz' for="form-field--img">Business Preview Image:</label>
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
