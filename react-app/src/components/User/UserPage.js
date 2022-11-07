import { useEffect } from "react";
import { NavLink, useLocation } from 'react-router-dom';
import { useSelector, useDispatch } from 'react-redux';

import pigOutline from '../../icons/pig-outline.png'
import upProf from '../../icons/user-page-icons/prof-up.png'
import pig from '../../icons/user-page-icons/pig-head.png';
import starGrey from '../../icons/user-page-icons/star-grey.png';
import starOran from '../../icons/user-page-icons/star-oran.png';
import savedBiz from '../../icons/user-page-icons/save.png';
import brokenImgPig from '../../icons/broken-img-pig.png';

import './UserPage.css';
import UserReviews from './UserReviews';
import UserBiz from "./UserBiz";
import * as reviewActions from "../../store/reviews";
import * as bizActions from "../../store/businesses";



const UserPage = () => {
    const url = useLocation().pathname;
    const dispatch = useDispatch();
    const user = useSelector(state => state.session.user);
    const userReviews = useSelector(state => state.reviews.user);
    const userBizzes = useSelector(state => state.businesses.allBusinesses);

    let lastName = user.last_name.split('')
    let lastInitial = lastName[0];


    const GREETING_LIST = [
        "Hello!",
        "Hola!",
        "Zdravstvuyte!",
        "Nǐ hǎo!",
        "Salve!",
        "Kon'nichiwa!",
        "Guten Tag!",
        "Olá!",
        "Anyoung haseyo!",
        "Asalaam alaikum!",
        "Goddag!",
        "Shikamoo!",
        "Goedendag!",
        "Yassas!",
        "Dzień dobry!",
        "Selamat siang!",
        "Namaste!",
        "Merhaba!",
        "Shalom!",
        "Ciao!",
        "G'day!",
        "Zdravo!",
        "Ciao!",
        "Hallo!",
        "Xin Chào!",
    ];

    const pickRandomGreeting = () => {
        return GREETING_LIST[Math.floor(Math.random() * GREETING_LIST.length)];
    }


    useEffect(() => {
        dispatch(reviewActions.getUserReviews());
        dispatch(bizActions.getUsersBiz());

        return () => {
            dispatch(bizActions.clearData());
            dispatch(reviewActions.clearData());
        }
    }, [dispatch]);

    return (
        <>
            <div id='bckgrd'></div>
            <div className='user-prof'>
                <div id='left-col'>
                    <button id='user-img'>
                        <img id='pig-outline' src={user.profile_pic ? user.profile_pic : pigOutline} alt='pig-outline' width='100%' height='100%' objectFit='cover' onError={e => e.target.src=brokenImgPig} />
                    </button>
                    <h3 id='bar-name'>{user.first_name}'s Profile</h3>
                    <div className='side-bar'>
                        {/* -----------------------OVERVIEW--------------------- */}
                        <NavLink to='/current' id='bar-row'>
                            <img id='bar-img' src={pig} alt='pig' width='25px' onError={e => e.target.src=brokenImgPig} />
                            <div id='bar-txt'>Profile Overview</div>
                        </NavLink>
                        {/* -----------------------REVIEWS--------------------- */}
                        <NavLink to='/reviews/current' id='bar-row'>
                            <img id='bar-img' src={starGrey} alt='star-grey' width='25px' onError={e => e.target.src=brokenImgPig} />
                            <div id='bar-txt'>
                                {/* <span>{userReviews && Object.keys(userReviews).length}</span> */}
                                Reviews
                            </div>
                        </NavLink>
                        {/* -----------------------BIZ--------------------- */}
                        <NavLink to='/biz/current' id='bar-row'>
                            <img id='bar-img' src={savedBiz} alt='star-grey' width='25px' onError={e => e.target.src=brokenImgPig} />
                            <div id='bar-txt'>My Businesses</div>
                        </NavLink>
                    </div>
                </div>
                <div id='mid-col'>
                    <div className='user-info'>
                        <h1 id='user-name'>{user.first_name} {lastInitial}.</h1>
                        <p id='user-greeting'>{pickRandomGreeting()}</p>
                        <div className='user-icons'>
                            <div id='user-rev'>
                                <img src={starOran} alt='star' onError={e => e.target.src=brokenImgPig} />
                                <p id='user-txt'>
                                    <span className="user-review-count">{userReviews && Object.keys(userReviews).length}</span>
                                    {userReviews && Object.keys(userReviews).length === 1 ? "Review" : "Reviews"}
                                </p>
                            </div>
                            {/* <div id='user-pht'>
                                <img src={cam} alt='cam' width='24px' onError={e => e.target.src=brokenImgPig} />
                                <p id='user-txt'>Photos</p>
                            </div> */}
                        </div>
                    </div>
                    <br></br>
                    <br></br>
                    {url === '/current' && (
                        <div>
                            <h2 id='mid-title-over'>Hello, {user.username}</h2>
                            <div>Access your businesses and reviews using the tabs on the left.</div>
                            {/* <div>
              <button to='/current' id='recent-act-user-container'>
                <img id='recent-act-user-pic' src={user.profile_pic ? user.profile_pic : pigOutline} onError={e => e.target.src=brokenImgPig} />
              </button>
            </div> */}
                        </div>
                    )}
                    {url === '/reviews/current' && (
                        <UserReviews user={user} userReviews={userReviews} />
                    )}
                    {url === '/biz/current' && (
                        <UserBiz user={user} userBizzes={userBizzes} />
                    )}
                </div>
                <div id='right-col'>
                    <div id='top-rc'>
                        {/* <h5 id='top-rc-text'>
                            <img src={cam} alt='add-prof-img' width='15px' onError={e => e.target.src=brokenImgPig} />
                            Add Profile Photo
                        </h5> */}
                        <h5 id='top-rc-text'>
                            <img src={upProf} alt='up-prof' width='15px' onError={e => e.target.src=brokenImgPig} />
                            Update Your Profile
                        </h5>
                    </div>
                    {url === '/current' && (
                        <div id='bot-rc'>
                            <div id='title-bot'>About {user.first_name} {lastInitial}.</div>
                            <h5 id='bot-rc-title'>Stats</h5>
                            <div id='bot-rc-1'>
                                <img src={savedBiz} alt='save' width='16px' height='16px' onError={e => e.target.src=brokenImgPig} />
                                <p id='bot-rc-txt'>
                                    My Businesses ({userBizzes && Object.keys(userBizzes).length})
                                </p>
                            </div>
                            {/* <h5 id='bot-rc-title'>Location</h5> */}
                            <div id='bot-rc-1'>
                            </div>
                            <h5 id='bot-rc-title'>Squealing Since 2022</h5>
                            <div id='bot-rc-1'>
                            </div>
                        </div>
                    )}
                </div>
            </div>
        </>
    )
}

export default UserPage
