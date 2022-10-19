import React from 'react'
import { useState, useEffect } from 'react'
import { NavLink } from 'react-router-dom'
import { useSelector, useDispatch } from 'react-redux'
import { useParams } from 'react-router-dom'
import { getOneBiz } from '../../store/businesses'
import { getBusinessReviews } from '../../store/reviews'
import { Modal } from '../../context/Modal';
import Footer from '../Footer'

// import { getUserReviews } from '../../store/reviews'
import check from '../../icons/claimed-check.svg';
import x from '../../icons/x.svg'
import map from '../../icons/map.svg'
import phone from '../../icons/phone.svg'
import star from '../../icons/write-review-star.svg'
import Map from '../Map/map'

import './BusinessDetails.css'

const BusinessDetails = () => {
    const dispatch = useDispatch()
    const { bizId } = useParams()

    const [showPhotoModal, setShowPhotoModal] = useState(false);

    const biz = useSelector(state => state.businesses.singleBusiness)
    const bizOwner = useSelector(state => state.businesses.singleBusiness.Owner)
    const bizImages = useSelector(state => state.businesses.singleBusiness.Business_Images)
    const bizReviews = useSelector(state => state.reviews.business)
    const types = useSelector(state => state.businesses.singleBusiness.types)
    const user = useSelector(state => state.session.user);

    let numReviews;
    let numImages;
    let allReviewImages
    if (bizReviews) {
        numReviews = (Object.values(bizReviews).length)
    }
    if (bizImages) {
        numImages = (Object.values(bizImages).length)
    }
    if (bizReviews) {
        let reviews = Object.values(bizReviews).map(obj => obj.Review_Images).filter(obj => obj.url)
        allReviewImages = reviews.flat()
    }

    useEffect(() => {
        dispatch(getOneBiz(bizId))
        dispatch(getBusinessReviews(bizId))
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
            res = currentTime < open.slice(0, 2) || currentTime > close.slice(0, 2) ? "Closed" : "Open"
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
    let days = ['Mon', 'Tue', "Wed", "Thu", "Fri", "Sat", "Sun"]
    let hours
    if (biz.start_time && biz.end_time) {
        let open = openOrClosed(biz.start_time, biz.end_time)
        let today = new Date().getDay()
        hours = days.map(day => {
            return (
                <div className='single-business-hours'>{day} <span>{convertTime(biz.start_time)} - {convertTime(biz.end_time)} <span className={open ? open + "closed-red" : 'none'}>{today === days.indexOf(day) + 1 ? open + " Now" : ""}</span></span></div>
            )
        })
    }
    let location = {
        address: biz.address + ', ' + biz.city + ', ' + biz.state,
        lat: biz.lat,
        lng: biz.lng
    }

    let singleReview
    if (bizReviews) {
        let reviewsArr = Object.values(bizReviews)
        singleReview = reviewsArr.map(obj => {
            const rate = obj.rating
            return (
                <div>
                    <div className='single-business-user'>
                        <div>
                            <img height="64" width="64" src={obj.User.profile_pic} />
                        </div>
                        <div className='single-business-user-details'>
                            <div className='single-business-user-name'>

                                {obj.User.first_name} {obj.User.last_name.slice(0, 1)}.
                            </div>
                            <div className='single-business-june-cohort'>
                                Squealing since June 2022
                            </div>
                        </div>
                    </div>
                    <div className='single-business-review-subheader'>
                        <div className='single-business-star-subheader review-card-stars'>
                            {/* FIRST STAR */}
                            <svg className='first-star' width="20" height="20" viewBox="0 0 20 20">
                                <path fill={rate >= 4.8 ? "rgba(251,67,60,1)" : rate >= 4.3 ? 'rgba(255, 100, 61, 1)' : rate >= 3.8 ? 'rgba(255, 100, 61, 1)' : rate >= 3.3 ? 'rgba(255, 135, 66, 1)' : rate >= 2.8 ? 'rgba(255, 135, 66, 1)' : rate >= 2.3 ? 'rgba(255, 173, 72, 1)' : rate >= 1.8 ? 'rgba(255, 173, 72, 1)' : rate >= 1.3 ? 'rgba(255, 204, 75, 1)' : 'rgba(255, 204, 75, 1)'}
                                    d="M0 4C0 1.79086 1.79086 0 4 0H10V20H4C1.79086 20 0 18.2091 0 16V4Z">
                                </path>
                                <path fill={rate >= 4.8 ? "rgba(251,67,60,1)" : rate >= 4.3 ? 'rgba(255, 100, 61, 1)' : rate >= 3.8 ? 'rgba(255, 100, 61, 1)' : rate >= 3.3 ? 'rgba(255, 135, 66, 1)' : rate >= 2.8 ? 'rgba(255, 135, 66, 1)' : rate >= 2.3 ? 'rgba(255, 173, 72, 1)' : rate >= 1.8 ? 'rgba(255, 173, 72, 1)' : rate >= 1.3 ? 'rgba(255, 204, 75, 1)' : 'rgba(255, 204, 75, 1)'}
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
                                <path fill={rate >= 4.8 ? "rgba(251,67,60,1)" : rate >= 4.3 ? 'rgba(255, 100, 61, 1)' : rate >= 3.8 ? 'rgba(255, 100, 61, 1)' : rate >= 3.3 ? 'rgba(255, 135, 66, 1)' : rate >= 2.8 ? 'rgba(255, 135, 66, 1)' : rate >= 2.3 ? 'rgba(255, 173, 72, 1)' : rate >= 1.8 ? 'rgba(255, 173, 72, 1)' : rate >= 1.3 ? 'rgba(255, 204, 75, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                    d="M0 4C0 1.79086 1.79086 0 4 0H10V20H4C1.79086 20 0 18.2091 0 16V4Z">
                                </path>
                                <path fill={rate >= 4.8 ? "rgba(251,67,60,1)" : rate >= 4.3 ? 'rgba(255, 100, 61, 1)' : rate >= 3.8 ? 'rgba(255, 100, 61, 1)' : rate >= 3.3 ? 'rgba(255, 135, 66, 1)' : rate >= 2.8 ? 'rgba(255, 135, 66, 1)' : rate >= 2.3 ? 'rgba(255, 173, 72, 1)' : rate >= 1.8 ? 'rgba(255, 173, 72, 1)' : 'rgba(187, 186, 192, 0.5)'}
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
                                <path fill={rate >= 4.8 ? "rgba(251,67,60,1)" : rate >= 4.3 ? 'rgba(255, 100, 61, 1)' : rate >= 3.8 ? 'rgba(255, 100, 61, 1)' : rate >= 3.3 ? 'rgba(255, 135, 66, 1)' : rate >= 2.8 ? 'rgba(255, 135, 66, 1)' : rate >= 2.3 ? 'rgba(255, 173, 72, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                    d="M0 4C0 1.79086 1.79086 0 4 0H10V20H4C1.79086 20 0 18.2091 0 16V4Z">
                                </path>
                                <path fill={rate >= 4.8 ? "rgba(251,67,60,1)" : rate >= 4.3 ? 'rgba(255, 100, 61, 1)' : rate >= 3.8 ? 'rgba(255, 100, 61, 1)' : rate >= 3.3 ? 'rgba(255, 135, 66, 1)' : rate >= 2.8 ? 'rgba(255, 135, 66, 1)' : 'rgba(187, 186, 192, 0.5)'}
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
                                <path fill={rate >= 4.8 ? "rgba(251,67,60,1)" : rate >= 4.3 ? 'rgba(255, 100, 61, 1)' : rate >= 3.8 ? 'rgba(255, 100, 61, 1)' : rate >= 3.3 ? 'rgba(255, 135, 66, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                    d="M0 4C0 1.79086 1.79086 0 4 0H10V20H4C1.79086 20 0 18.2091 0 16V4Z">
                                </path>
                                <path fill={rate >= 4.8 ? "rgba(251,67,60,1)" : rate >= 4.3 ? 'rgba(255, 100, 61, 1)' : rate >= 3.8 ? 'rgba(255, 100, 61, 1)' : 'rgba(187, 186, 192, 0.5)'}
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
                                <path fill={rate >= 4.8 ? "rgba(251,67,60,1)" : rate >= 4.3 ? 'rgba(255, 100, 61, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                    d="M0 4C0 1.79086 1.79086 0 4 0H10V20H4C1.79086 20 0 18.2091 0 16V4Z">
                                </path>
                                <path fill={rate >= 4.8 ? "rgba(251,67,60,1)" : 'rgba(187, 186, 192, 0.5)'}
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
                        <div>
                            {obj.created_at.slice(5, 7) + '/' + obj.created_at.slice(8, 10) + "/" + obj.created_at.slice(0, 4)}
                        </div>
                    </div>
                    <div className='single-business-review-body'>
                        {obj.Review_Images.length > 0 && (
                            <div>{obj.Review_Images.length} photos</div>
                        )}
                        {obj.review_body}
                        {obj.Review_Images.length > 0 && obj.Review_Images.map(obj => {
                            return (
                                <div className='single-business-review-image'> <img height='300' width='300' src={obj.url} /></div>
                            )
                        }
                        )}
                    </div>
                </div>
            )
        })
    }




    return (
            <div className='single-business-details-container'>
                {/* {showPhotoModal && (
                    <>
                        <Modal id='photo-modal' onClose={() => {
                            setShowPhotoModal(false)
                        }}>
                            <div className='photo-modal-close' onClick={() => setShowPhotoModal(false)}>
                                Close <img src={x} />
                            </div>
                            <div className='single-business-modal-title'>Photos for {biz.name}</div>
                            {bizImages.length === 0 && (
                                <div>This business does not have any photos</div>
                            )}
                            <div className='single-business-modal-images'>


                                {bizImages.length > 0 && bizImages.map(obj => {
                                    return (
                                        <img className='single-business-review-image' height='300' width='300' src={obj.url} />
                                    )
                                }
                                )}
                                {allReviewImages.length > 0 && allReviewImages.map(obj => {
                                    return (
                                        <img className='single-business-review-image' height='300' width='300' src={obj.url} />
                                    )
                                })}
                            </div>
                        </Modal>
                    </>
                )} */}
                <div>
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
                                        <svg className='middle-star' width="32" height="32" viewBox="0 0 20 20">
                                            <path fill={rate >= 4.8 ? "rgba(251,67,60,1)" : rate >= 4.3 ? 'rgba(255, 100, 61, 1)' : rate >= 3.8 ? 'rgba(255, 100, 61, 1)' : rate >= 3.3 ? 'rgba(255, 135, 66, 1)' : rate >= 2.8 ? 'rgba(255, 135, 66, 1)' : rate >= 2.3 ? 'rgba(255, 173, 72, 1)' : rate >= 1.8 ? 'rgba(255, 173, 72, 1)' : rate >= 1.3 ? 'rgba(255, 204, 75, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                                d="M0 4C0 1.79086 1.79086 0 4 0H10V20H4C1.79086 20 0 18.2091 0 16V4Z">
                                            </path>
                                            <path fill={rate >= 4.8 ? "rgba(251,67,60,1)" : rate >= 4.3 ? 'rgba(255, 100, 61, 1)' : rate >= 3.8 ? 'rgba(255, 100, 61, 1)' : rate >= 3.3 ? 'rgba(255, 135, 66, 1)' : rate >= 2.8 ? 'rgba(255, 135, 66, 1)' : rate >= 2.3 ? 'rgba(255, 173, 72, 1)' : rate >= 1.8 ? 'rgba(255, 173, 72, 1)' : 'rgba(187, 186, 192, 0.5)'}
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
                                        <svg className='middle-star' width="32" height="32" viewBox="0 0 20 20">
                                            <path fill={rate >= 4.8 ? "rgba(251,67,60,1)" : rate >= 4.3 ? 'rgba(255, 100, 61, 1)' : rate >= 3.8 ? 'rgba(255, 100, 61, 1)' : rate >= 3.3 ? 'rgba(255, 135, 66, 1)' : rate >= 2.8 ? 'rgba(255, 135, 66, 1)' : rate >= 2.3 ? 'rgba(255, 173, 72, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                                d="M0 4C0 1.79086 1.79086 0 4 0H10V20H4C1.79086 20 0 18.2091 0 16V4Z">
                                            </path>
                                            <path fill={rate >= 4.8 ? "rgba(251,67,60,1)" : rate >= 4.3 ? 'rgba(255, 100, 61, 1)' : rate >= 3.8 ? 'rgba(255, 100, 61, 1)' : rate >= 3.3 ? 'rgba(255, 135, 66, 1)' : rate >= 2.8 ? 'rgba(255, 135, 66, 1)' : 'rgba(187, 186, 192, 0.5)'}
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
                                        <svg className='middle-star' width="32" height="32" viewBox="0 0 20 20">
                                            <path fill={rate >= 4.8 ? "rgba(251,67,60,1)" : rate >= 4.3 ? 'rgba(255, 100, 61, 1)' : rate >= 3.8 ? 'rgba(255, 100, 61, 1)' : rate >= 3.3 ? 'rgba(255, 135, 66, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                                d="M0 4C0 1.79086 1.79086 0 4 0H10V20H4C1.79086 20 0 18.2091 0 16V4Z">
                                            </path>
                                            <path fill={rate >= 4.8 ? "rgba(251,67,60,1)" : rate >= 4.3 ? 'rgba(255, 100, 61, 1)' : rate >= 3.8 ? 'rgba(255, 100, 61, 1)' : 'rgba(187, 186, 192, 0.5)'}
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
                                        <svg className='last-star' width="32" height="32" viewBox="0 0 20 20">
                                            <path fill={rate >= 4.8 ? "rgba(251,67,60,1)" : rate >= 4.3 ? 'rgba(255, 100, 61, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                                d="M0 4C0 1.79086 1.79086 0 4 0H10V20H4C1.79086 20 0 18.2091 0 16V4Z">
                                            </path>
                                            <path fill={rate >= 4.8 ? "rgba(251,67,60,1)" : 'rgba(187, 186, 192, 0.5)'}
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
                            <div className='single-business-see-more-photos' onClick={() => setShowPhotoModal(true)}>
                                See {numImages} photos
                            </div>
                        </div>
                        {imageHeader}
                        <div className='bottom-gradient'>
                        </div>
                    </div>

                    <div className='single-business-review-details-body'>
                        <div className='single-business-reviews-button'>
                            <div className='single-business-review-bar'>
                                <NavLink to='/'><button className='single-business-review-bar-button'>
                                    <img width='24' height='24' src={star} /> Write a review
                                </button>
                            </NavLink>
                            </div>
                            <div className='single-business-title'>Location & Hours</div>
                            <div className='single-business-location-hours'>
                                <div>
                                    <div className='map'>
                                        <Map location={location} zoomLevel={16} />
                                    </div>
                                    <div className='single-business-location-details'>
                                        <p>
                                            {biz.address}
                                        </p>
                                        <p>
                                            {biz.city}, {biz.state} {biz.zipcode}
                                        </p>
                                    </div>
                                </div>
                                <div className='single-business-hours-wrapper'>
                                    {hours}
                                </div>

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
                        <div className='single-business-reviews'>
                            <div className='single-business-title'>
                                Reviews
                            </div>
                            <div className='single-business-start-your-review'>
                                <div className='single-business-user'>
                                    <div>
                                        <img height="72" width="72" src={user.profile_pic} />
                                    </div>
                                    <div className='single-business-user-details start-review'>
                                        <div className='single-business-user-name'>

                                            {user.first_name} {user.last_name.slice(0, 1)}.
                                        </div>
                                        <div className='single-business-june-cohort'>
                                            {user.username}
                                        </div>
                                    </div>
                                </div>
                                <div className='single-business-review-link'>
                                    <NavLink style={{ color: '#007A96' }} to={`/newreview/biz/${biz.id}`}>Start your review of {biz.name}</NavLink>
                                </div>

                            </div>


                            <div>
                                <div className='single-business-overall-rating'>
                                    Overall Rating
                                </div>
                                <div className='review-card-stars'>
                                    {/* FIRST STAR */}
                                    <svg className='first-star' width="32" height="32" viewBox="0 0 20 20">
                                        <path fill={rate >= 4.8 ? "rgba(251,67,60,1)" : rate >= 4.3 ? 'rgba(255, 100, 61, 1)' : rate >= 3.8 ? 'rgba(255, 100, 61, 1)' : rate >= 3.3 ? 'rgba(255, 135, 66, 1)' : rate >= 2.8 ? 'rgba(255, 135, 66, 1)' : rate >= 2.3 ? 'rgba(255, 173, 72, 1)' : rate >= 1.8 ? 'rgba(255, 173, 72, 1)' : rate >= 1.3 ? 'rgba(255, 204, 75, 1)' : 'rgba(255, 204, 75, 1)'}
                                            d="M0 4C0 1.79086 1.79086 0 4 0H10V20H4C1.79086 20 0 18.2091 0 16V4Z">
                                        </path>
                                        <path fill={rate >= 4.8 ? "rgba(251,67,60,1)" : rate >= 4.3 ? 'rgba(255, 100, 61, 1)' : rate >= 3.8 ? 'rgba(255, 100, 61, 1)' : rate >= 3.3 ? 'rgba(255, 135, 66, 1)' : rate >= 2.8 ? 'rgba(255, 135, 66, 1)' : rate >= 2.3 ? 'rgba(255, 173, 72, 1)' : rate >= 1.8 ? 'rgba(255, 173, 72, 1)' : rate >= 1.3 ? 'rgba(255, 204, 75, 1)' : 'rgba(255, 204, 75, 1)'}
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
                                    <svg className='middle-star' width="32" height="32" viewBox="0 0 20 20">
                                        <path fill={rate >= 4.8 ? "rgba(251,67,60,1)" : rate >= 4.3 ? 'rgba(255, 100, 61, 1)' : rate >= 3.8 ? 'rgba(255, 100, 61, 1)' : rate >= 3.3 ? 'rgba(255, 135, 66, 1)' : rate >= 2.8 ? 'rgba(255, 135, 66, 1)' : rate >= 2.3 ? 'rgba(255, 173, 72, 1)' : rate >= 1.8 ? 'rgba(255, 173, 72, 1)' : rate >= 1.3 ? 'rgba(255, 204, 75, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                            d="M0 4C0 1.79086 1.79086 0 4 0H10V20H4C1.79086 20 0 18.2091 0 16V4Z">
                                        </path>
                                        <path fill={rate >= 4.8 ? "rgba(251,67,60,1)" : rate >= 4.3 ? 'rgba(255, 100, 61, 1)' : rate >= 3.8 ? 'rgba(255, 100, 61, 1)' : rate >= 3.3 ? 'rgba(255, 135, 66, 1)' : rate >= 2.8 ? 'rgba(255, 135, 66, 1)' : rate >= 2.3 ? 'rgba(255, 173, 72, 1)' : rate >= 1.8 ? 'rgba(255, 173, 72, 1)' : 'rgba(187, 186, 192, 0.5)'}
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
                                    <svg className='middle-star' width="32" height="32" viewBox="0 0 20 20">
                                        <path fill={rate >= 4.8 ? "rgba(251,67,60,1)" : rate >= 4.3 ? 'rgba(255, 100, 61, 1)' : rate >= 3.8 ? 'rgba(255, 100, 61, 1)' : rate >= 3.3 ? 'rgba(255, 135, 66, 1)' : rate >= 2.8 ? 'rgba(255, 135, 66, 1)' : rate >= 2.3 ? 'rgba(255, 173, 72, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                            d="M0 4C0 1.79086 1.79086 0 4 0H10V20H4C1.79086 20 0 18.2091 0 16V4Z">
                                        </path>
                                        <path fill={rate >= 4.8 ? "rgba(251,67,60,1)" : rate >= 4.3 ? 'rgba(255, 100, 61, 1)' : rate >= 3.8 ? 'rgba(255, 100, 61, 1)' : rate >= 3.3 ? 'rgba(255, 135, 66, 1)' : rate >= 2.8 ? 'rgba(255, 135, 66, 1)' : 'rgba(187, 186, 192, 0.5)'}
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
                                    <svg className='middle-star' width="32" height="32" viewBox="0 0 20 20">
                                        <path fill={rate >= 4.8 ? "rgba(251,67,60,1)" : rate >= 4.3 ? 'rgba(255, 100, 61, 1)' : rate >= 3.8 ? 'rgba(255, 100, 61, 1)' : rate >= 3.3 ? 'rgba(255, 135, 66, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                            d="M0 4C0 1.79086 1.79086 0 4 0H10V20H4C1.79086 20 0 18.2091 0 16V4Z">
                                        </path>
                                        <path fill={rate >= 4.8 ? "rgba(251,67,60,1)" : rate >= 4.3 ? 'rgba(255, 100, 61, 1)' : rate >= 3.8 ? 'rgba(255, 100, 61, 1)' : 'rgba(187, 186, 192, 0.5)'}
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
                                    <svg className='last-star' width="32" height="32" viewBox="0 0 20 20">
                                        <path fill={rate >= 4.8 ? "rgba(251,67,60,1)" : rate >= 4.3 ? 'rgba(255, 100, 61, 1)' : 'rgba(187, 186, 192, 0.5)'}
                                            d="M0 4C0 1.79086 1.79086 0 4 0H10V20H4C1.79086 20 0 18.2091 0 16V4Z">
                                        </path>
                                        <path fill={rate >= 4.8 ? "rgba(251,67,60,1)" : 'rgba(187, 186, 192, 0.5)'}
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
                                <div className='single-business-overall-num-rating'>
                                    {numReviews} reviews
                                </div>
                            </div>

                            <div className='single-business-single-reviews'>
                                {singleReview}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
    )
}

export default BusinessDetails
