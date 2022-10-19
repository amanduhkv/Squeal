import React, { useState } from 'react';
import { NavLink, useLocation } from 'react-router-dom';
import { useSelector } from 'react-redux';
import squealnLogo from '../../icons/squealnLogo.png';
import squealnLogowht from '../../icons/squealnLogowht.png';
import search from '../../icons/search.svg';
import userIcon from '../../icons/githubPurple.png';
import './NavBar.css';
import LoginForm from '../auth/LoginForm';
import SignUpForm from '../auth/SignUpForm';
import ProfileButton from '../auth/ProfileButton'
import chevron from '../../icons/chevron.svg';
import fastfood from '../../icons/fast-food.svg';
import pizza from '../../icons/pizza.svg';
import sandwich from '../../icons/sandwich.svg';
import takeout from '../../icons/takeout.svg';
import delivery from '../../icons/delivery.svg';
import burger from '../../icons/burger.svg';
import chicken from '../../icons/chicken.svg';
import donut from '../../icons/donut.svg';
import dessert from '../../icons/bakery.svg';
import icecream from '../../icons/ice-cream.svg';
import smoothie from '../../icons/juicebar.svg';
import boba from '../../icons/bubble-tea.svg';
import coffee from '../../icons/coffee.svg';
import cafe from '../../icons/cafe.svg';
import bbq from '../../icons/bbq.svg';
import bakery from '../../icons/bake.svg';
import japanese from '../../icons/japanese.svg';
import chinese from '../../icons/chinese.svg';
import korean from '../../icons/korean.svg';
import viet from '../../icons/viet.svg';
import med from '../../icons/med.svg';
import taco from '../../icons/taco.svg';
import italian from '../../icons/italian.svg';

function NavBar(){
    const sessionUser = useSelector(state => state.session.user);
    const url = useLocation().pathname;
    const [ query, setQuery ] = useState('');
    const [ location, setLocation ] = useState('');
    // console.log('this is the url',url);
// /*
    let sessionLinks;

    if (sessionUser) {
        // console.log('hereeee')
        sessionLinks = (<>
            <div className='user-icon-container'>
                <ProfileButton />
            </div>
        </>)
    }
    else {
        sessionLinks = (<>
            <div className='session-buttons-sbs'>
                {/* <LoginForm /> */}
                <SignUpForm />
            </div>
        </>)
    }
// */
    return (
        <div className={url === '/' ? 'header-container gradient' : url.includes('new') ? 'header-container-sm header-container-fixed' : 'header-container header-container-fixed'}>
            <div className={sessionUser ? 'header-top-portion-user' : 'header-top-portion-sl'}>
                <div className={sessionUser ? 'logo-left-section-user' : 'logo-left-section-sl'}>
                    <NavLink className='logo' exact to="/">
                        <img src={url === '/' ? squealnLogowht : squealnLogo}
                                            alt='logo' className='squeal-logo'/>
                    </NavLink>
                </div>
                <div className={sessionUser ? 'search-and-buttons-right-section-user' : 'search-and-buttons-right-section-sl'}>
                    {url.includes('new') ? <div></div> : <div className='nav-search-section'>
                        <form className='search-query-section' action='/search'>
                            <label className='search-input-label search-input-label-left'>
                                <input className='search-query-input search-input'
                                    placeholder="tacos, cheap dinner, Max's"
                                    type='text' value={query} onChange={(e) => setQuery(e.target.value)} />
                            </label>
                            <span className='inbetween-inputs' />
                            <label className='search-input-label search-input-label-right'>
                                <input className='search-location-input search-input'
                                    placeholder='Los Angeles, CA'
                                    type='text' value={location} onChange={(e) => setLocation(e.target.value)} />
                            </label>
                            <button type='submit' className='search-button'>
                                <img src={search} alt='icon' className='search-icon' />
                            </button>
                        </form>
                    </div>}
                    {sessionUser ? <span className='header-gap-search-buttons' /> : null}
                    <div className={url.includes('new') ? 'buttons-form-stuff' : sessionUser ? 'buttons-user-stuff' : 'buttons-sl-stuff'}>
                        {url.includes('new') ? <div></div> : <><NavLink to='/businesses/new' className={sessionUser ? 'navbar-button-left' : 'navbar-button-left-sl'}>
                            <button className={url === '/' ? 'top-button-wht header-right-button' : 'top-button-blk header-right-button'}>
                                List a Business
                            </button>
                        </NavLink>
                        <NavLink to='/writeareview' className={sessionUser ? 'navbar-button-right' : 'navbar-button-right-sl'}>
                            <button className={url === '/' ? 'top-button-wht header-right-button' : 'top-button-blk header-right-button'}>
                                Write a Review
                            </button>
                        </NavLink></>}
                        <div>
                        {sessionLinks}
                        </div>
                    </div>
                </div>
            </div>
            {url.includes('new') ? null :
            <div className={sessionUser ? 'header-bottom-portion-user' : 'header-bottom-portion-sl'}>
                <div className='empty-below-icon' />
                <div className='buttons-under-search'>
                    <div className='tooltip-under-search'>
                        <button className={url === '/' ? 'header-bottom-buttons fast-food-button' : 'header-bottom-buttons ff-button-blk'}>
                            Quick Meals <svg width="24" height="24" className={url === '/' ? "chevron-svg" : "chevron-svg-blk"}><path d="M12 15.25a1 1 0 01-.7-.29l-4.58-4.5A1.011 1.011 0 018.12 9L12 12.85 15.88 9a1 1 0 111.4 1.42L12.7 15a1 1 0 01-.7.25z"></path></svg>
                        </button>
                        <div className='tooltiptext tooltip-ff'>
                            <button className='dropdown-display-text top-dropdown left-ffdropdown'>
                                <img className='tooltip-icons' src={fastfood} alt='icon' />Fast Food
                            </button>
                            <button className='dropdown-display-text top-dropdown right-ffdropdown'>
                                <img className='tooltip-icons' src={pizza} alt='icon' />Pizza
                            </button>
                            <button className='dropdown-display-text left-ffdropdown'>
                                <img className='tooltip-icons' src={delivery} alt='icon' />Delivery
                            </button>
                            <button className='dropdown-display-text right-ffdropdown'>
                                <img className='tooltip-icons' src={burger} alt='icon' />Burgers
                            </button>
                            <button className='dropdown-display-text left-ffdropdown'>
                                <img className='tooltip-icons' src={sandwich} alt='icon' />Sandwiches
                            </button>
                            <button className='dropdown-display-text right-ffdropdown'>
                                <img className='tooltip-icons' src={chicken} alt='icon' />Chicken Wings
                            </button>
                            <button className='dropdown-display-text bottom-dropdown left-ffdropdown'>
                                <img className='tooltip-icons' src={takeout} alt='icon' />Takeout
                            </button>
                            <button className='dropdown-display-text bottom-dropdown right-ffdropdown'>
                                <img className='tooltip-icons' src={donut} alt='icon' />Donuts
                            </button>
                        </div>
                    </div>
                    <div className='tooltip-under-search'>
                        <button className={url === '/' ? 'header-bottom-buttons dessert-button' : 'header-bottom-buttons dessert-button-blk'}>
                            Dessert <svg width="24" height="24" className={url === '/' ? "chevron-svg" : "chevron-svg-blk"}><path d="M12 15.25a1 1 0 01-.7-.29l-4.58-4.5A1.011 1.011 0 018.12 9L12 12.85 15.88 9a1 1 0 111.4 1.42L12.7 15a1 1 0 01-.7.25z"></path></svg>
                        </button>
                        <div className='tooltiptext tooltip-ff'>
                            <button className='dropdown-display-text top-dropdown left-ffdropdown'>
                                <img className='tooltip-icons' src={bakery} alt='icon' />Bakeries
                            </button>
                            <button className='dropdown-display-text top-dropdown right-ffdropdown'>
                                <img className='tooltip-icons' src={boba} alt='icon' />Bubble Tea
                            </button>
                            <button className='dropdown-display-text left-ffdropdown'>
                                <img className='tooltip-icons' src={dessert} alt='icon' />Desserts
                            </button>
                            <button className='dropdown-display-text right-ffdropdown'>
                                <img className='tooltip-icons' src={coffee} alt='icon' />Coffee & Tea
                            </button>
                            <button className='dropdown-display-text left-ffdropdown'>
                                <img className='tooltip-icons' src={icecream} alt='icon' />Ice Cream
                            </button>
                            <button className='dropdown-display-text right-ffdropdown'>
                                <img className='tooltip-icons' src={donut} alt='icon' />Donuts
                            </button>
                            <button className='dropdown-display-text bottom-dropdown left-ffdropdown'>
                                <img className='tooltip-icons' src={smoothie} alt='icon' />Smoothies
                            </button>
                            <button className='dropdown-display-text bottom-dropdown right-ffdropdown'>
                                <img className='tooltip-icons' src={cafe} alt='icon' />Cafes
                            </button>
                        </div>
                    </div>
                    <div className='tooltip-under-search'>
                        <button className={url === '/' ? 'header-bottom-buttons coffee-tea-button' : 'header-bottom-buttons popular-button-blk'}>
                            Popular <svg width="24" height="24" className={url === '/' ? "chevron-svg" : "chevron-svg-blk"}><path d="M12 15.25a1 1 0 01-.7-.29l-4.58-4.5A1.011 1.011 0 018.12 9L12 12.85 15.88 9a1 1 0 111.4 1.42L12.7 15a1 1 0 01-.7.25z"></path></svg>
                        </button>
                        <div className='tooltiptext tooltip-ff'>
                            <button className='dropdown-display-text top-dropdown left-ffdropdown'>
                                <img className='tooltip-icons' src={bbq} alt='icon' />Barbeque
                            </button>
                            <button className='dropdown-display-text top-dropdown right-ffdropdown'>
                                <img className='tooltip-icons' src={korean} alt='icon' />Korean
                            </button>
                            <button className='dropdown-display-text left-ffdropdown'>
                                <img className='tooltip-icons' src={chinese} alt='icon' />Chinese
                            </button>
                            <button className='dropdown-display-text right-ffdropdown'>
                                <img className='tooltip-icons' src={taco} alt='icon' />Mexican
                            </button>
                            <button className='dropdown-display-text left-ffdropdown'>
                                <img className='tooltip-icons' src={italian} alt='icon' />Italian
                            </button>
                            <button className='dropdown-display-text right-ffdropdown'>
                                <img className='tooltip-icons' src={viet} alt='icon' />Vietnamese
                            </button>
                            <button className='dropdown-display-text bottom-dropdown left-ffdropdown'>
                                <img className='tooltip-icons' src={japanese} alt='icon' />Japanese
                            </button>
                            <button className='dropdown-display-text bottom-dropdown right-ffdropdown'>
                                <img className='tooltip-icons' src={med} alt='icon' />Mediterranean
                            </button>
                        </div>
                    </div>

                </div>
            </div>}
        </div>
    )
}

export default NavBar;
