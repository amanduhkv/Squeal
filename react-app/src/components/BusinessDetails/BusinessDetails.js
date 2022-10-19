import React from 'react'
import { useState, useEffect } from 'react'
import { useSelector, useDispatch } from 'react-redux'
import { useParams } from 'react-router-dom'
import { getOneBiz } from '../../store/businesses'
import { getBusinessReviews } from '../../store/reviews'
import check from '../../icons/claimed-check.svg';
import map from '../../icons/map.svg'
import phone from '../../icons/phone.svg'
import star from '../../icons/write-review-star.svg'

import './BusinessDetails.css'

const BusinessDetails = () => {
    const dispatch = useDispatch()
    const { bizId } = useParams()

    const [numImages, setNumImages] = useState('')
    const [numReviews, setNumReviews] = useState('')

    const biz = useSelector(state => state.businesses.singleBusiness)
    const bizOwner = useSelector(state => state.businesses.singleBusiness.Owner)
    const bizImages = useSelector(state => state.businesses.singleBusiness.Business_Images)
    const bizReviews = useSelector(state => state.reviews.business)
    const types = useSelector(state => state.businesses.singleBusiness.types)

    console.log(">>>>>> BIZ", biz)
    console.log(">>>>>> BIZ OWNER", bizOwner)
    console.log(">>>>>> BIZ IMAGES", bizImages)
    console.log(">>>>>> REVIEWS", numReviews)

    useEffect(() => {
        dispatch(getOneBiz(bizId))
        dispatch(getBusinessReviews(bizId))
        // setRate(biz.avg_rating)
        if (bizReviews) {
            setNumReviews(Object.values(bizReviews).length)
        }
        if (bizImages) {
            setNumImages(Object.values(bizImages).length)
        }
    }, [dispatch])

    const rate = biz.avg_rating

    let imageHeader
    if (bizImages) {
        imageHeader = bizImages.map(obj => {
            return (
                <span key={obj.id} className='single-business-one-image-wrapper' >
                    <img className='single-business-one-image' alt={obj.id} src={obj.url} />
                </span>
            )
        })
    }
    let typeStr
    if (types) {
        typeStr = types.map(obj => obj.type).join(', ')
    }

    function convertTime(str) {
        let res
        if (str) {
            str = str[0] === '0' ? str.slice(1) : str
            res = str < 1200 ? str.slice(0, -2) + ":" + str.slice(-2) + " AM" : str.slice(0, -2) - 12 + ":" + str.slice(-2) + " PM"
        }
        return res
    }
    function openOrClosed(open, close) {
        let res
        let currentTime = new Date().getHours()
        if (open && close) {
            res = currentTime < convertTime(open) || currentTime > convertTime(close) ? "Closed" : "Open"
        }
        return res
    }
    function phoneNumber(str) {
        let res
        if (str) {
            str = str.slice(2)
            res = "(" + str.slice(0, 3) + ") " + str.slice(3, 6) + '-' + str.slice(6)
        }
        return res
    }

    return (
        <div className='single-business-details-container'>
            <div className='single-business-images'>
                <div className='single-business-header-info'>
                    <div className='single-business-details'>
                        <div className='single-business-name'>
                            {biz.name}
                        </div>
                        <div className='single-business-reviews-header'>
                            <div className='review-card-stars'>
                                {/* FIRST STAR */}
                                <svg className='first-star' width="32" height="32" viewBox="0 0 20 20">
                                    <path fill={rate >= 4.8 ? "rgba(251,67,60,1)" : rate >= 4.3 ? 'rgba(255, 100, 61, 1)' : rate >= 3.8 ? 'rgba(255, 100, 61, 1)' : rate >= 3.3 ? 'rgba(255, 135, 66, 1)' : rate >= 2.8 ? 'rgba(255, 135, 66, 1)' : rate >= 2.3 ? 'rgba(255, 173, 72, 1)' : rate >= 1.8 ? 'rgba(255, 173, 72, 1)' : rate >= 1.3 ? 'rgba(255, 204, 75, 1)' : 'rgba(255, 204, 75, 1)'}
                                        d="M0 4C0 1.79086 1.79086 0 4 0H10V20H4C1.79086 20 0 18.2091 0 16V4Z">
                                    </path>
                                    <path fill={rate >= 4.8 ? "rgba(251,67,60,1)" : rate >= 4.3 ? 'rgba(255, 100, 61, 1)' : rate >= 3.8 ? 'rgba(255, 100, 61, 1)' : rate >= 3.3 ? 'rgba(255, 135, 66, 1)' : rate >= 2.8 ? 'rgba(255, 135, 66, 1)' : rate >= 2.3 ? 'rgba(255, 173, 72, 1)' : rate >= 1.8 ? 'rgba(255, 173, 72, 1)' : rate >= 1.3 ? 'rgba(255, 204, 75, 1)' : 'rgba(255, 204, 75, 1)'}
                                        d="M20 4C20 1.79086 18.2091 0 16 0H10V20H16C18.2091 20 20 18.2091 20 16V4Z">
                                    </path>
                                    <path fill="white" fill-rule="evenodd" clip-rule="evenodd"
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
                                <svg className='middle-star' width="32" height="32" viewBox="0 0 20 20">
                                    <path fill={rate >= 4.8 ? "rgba(251,67,60,1)" : rate >= 4.3 ? 'rgba(255, 100, 61, 1)' : rate >= 3.8 ? 'rgba(255, 100, 61, 1)' : rate >= 3.3 ? 'rgba(255, 135, 66, 1)' : rate >= 2.8 ? 'rgba(255, 135, 66, 1)' : rate >= 2.3 ? 'rgba(255, 173, 72, 1)' : rate >= 1.8 ? 'rgba(255, 173, 72, 1)' : rate >= 1.3 ? 'rgba(255, 204, 75, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                        d="M0 4C0 1.79086 1.79086 0 4 0H10V20H4C1.79086 20 0 18.2091 0 16V4Z">
                                    </path>
                                    <path fill={rate >= 4.8 ? "rgba(251,67,60,1)" : rate >= 4.3 ? 'rgba(255, 100, 61, 1)' : rate >= 3.8 ? 'rgba(255, 100, 61, 1)' : rate >= 3.3 ? 'rgba(255, 135, 66, 1)' : rate >= 2.8 ? 'rgba(255, 135, 66, 1)' : rate >= 2.3 ? 'rgba(255, 173, 72, 1)' : rate >= 1.8 ? 'rgba(255, 173, 72, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                        d="M20 4C20 1.79086 18.2091 0 16 0H10V20H16C18.2091 20 20 18.2091 20 16V4Z">
                                    </path>
                                    <path fill="white" fill-rule="evenodd" clip-rule="evenodd"
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
                                <svg className='middle-star' width="32" height="32" viewBox="0 0 20 20">
                                    <path fill={rate >= 4.8 ? "rgba(251,67,60,1)" : rate >= 4.3 ? 'rgba(255, 100, 61, 1)' : rate >= 3.8 ? 'rgba(255, 100, 61, 1)' : rate >= 3.3 ? 'rgba(255, 135, 66, 1)' : rate >= 2.8 ? 'rgba(255, 135, 66, 1)' : rate >= 2.3 ? 'rgba(255, 173, 72, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                        d="M0 4C0 1.79086 1.79086 0 4 0H10V20H4C1.79086 20 0 18.2091 0 16V4Z">
                                    </path>
                                    <path fill={rate >= 4.8 ? "rgba(251,67,60,1)" : rate >= 4.3 ? 'rgba(255, 100, 61, 1)' : rate >= 3.8 ? 'rgba(255, 100, 61, 1)' : rate >= 3.3 ? 'rgba(255, 135, 66, 1)' : rate >= 2.8 ? 'rgba(255, 135, 66, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                        d="M20 4C20 1.79086 18.2091 0 16 0H10V20H16C18.2091 20 20 18.2091 20 16V4Z">
                                    </path>
                                    <path fill="white" fill-rule="evenodd" clip-rule="evenodd"
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
                                <svg className='middle-star' width="32" height="32" viewBox="0 0 20 20">
                                    <path fill={rate >= 4.8 ? "rgba(251,67,60,1)" : rate >= 4.3 ? 'rgba(255, 100, 61, 1)' : rate >= 3.8 ? 'rgba(255, 100, 61, 1)' : rate >= 3.3 ? 'rgba(255, 135, 66, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                        d="M0 4C0 1.79086 1.79086 0 4 0H10V20H4C1.79086 20 0 18.2091 0 16V4Z">
                                    </path>
                                    <path fill={rate >= 4.8 ? "rgba(251,67,60,1)" : rate >= 4.3 ? 'rgba(255, 100, 61, 1)' : rate >= 3.8 ? 'rgba(255, 100, 61, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                        d="M20 4C20 1.79086 18.2091 0 16 0H10V20H16C18.2091 20 20 18.2091 20 16V4Z">
                                    </path>
                                    <path fill="white" fill-rule="evenodd" clip-rule="evenodd"
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
                                <svg className='last-star' width="32" height="32" viewBox="0 0 20 20">
                                    <path fill={rate >= 4.8 ? "rgba(251,67,60,1)" : rate >= 4.3 ? 'rgba(255, 100, 61, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                        d="M0 4C0 1.79086 1.79086 0 4 0H10V20H4C1.79086 20 0 18.2091 0 16V4Z">
                                    </path>
                                    <path fill={rate >= 4.8 ? "rgba(251,67,60,1)" : 'rgba(187, 186, 192, 0.5)'}
                                        d="M20 4C20 1.79086 18.2091 0 16 0H10V20H16C18.2091 20 20 18.2091 20 16V4Z">
                                    </path>
                                    <path fill="white" fill-rule="evenodd" clip-rule="evenodd"
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
                            <div className='single-business-reviewsnumber'>
                                {numReviews} reviews
                            </div>
                        </div>
                        <div className='single-business-claimedtypes'>
                            <img alt='check' width="16" height="16" src={check} />
                            <span>
                                <span style={{ color: '#52B4FC', fontWeight: '500' }}>Claimed</span>  ·  {biz.price_range}  ·  {typeStr}
                            </span>
                        </div>
                        <div className='single-business-open-closed'>
                            <span className={openOrClosed(biz.start_time, biz.end_time)}>{openOrClosed(biz.start_time, biz.end_time)}</span> {convertTime(biz.start_time)} - {convertTime(biz.end_time)}
                        </div>
                    </div>
                    <div className='single-business-see-more-photos'>
                        {/* <div> */}
                        See {numImages} photos
                        {/* </div> */}
                    </div>
                </div>
                {imageHeader}
                <div className='bottom-gradient'>
                </div>
            </div>

            <div className='single-business-review-details-body'>
                <div className='single-business-reviews'>
                    <div className='single-business-review-bar'>
                        <button className='single-business-review-bar-button'>
                            <img width='24' height='24' src={star} /> Write a review
                        </button>
                    </div>
                    <span className='single-business-box-divider'></span>
                    <div className='single-business-location-hours'>
                    </div>


                </div>
                <div className='single-business-contact-details'>
                    {biz.phone_number && (
                        <div className='single-business-contact'>
                            <div>{phoneNumber(biz.phone_number)}</div>
                            <img width='24' height='24' src={phone} />
                        </div>
                    )}
                    <span className='single-business-box-divider'></span>
                    {biz.address && (
                        <div className='single-business-contact'>
                            <div>{biz.address} {biz.city}, {biz.state} </div>
                            <img width='24' height='24' img src={map} />
                        </div>
                    )}
                </div>
            </div>


        </div>
    )
}

export default BusinessDetails