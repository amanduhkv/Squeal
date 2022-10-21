import React, { useState, useRef, useLayoutEffect } from 'react';
import { NavLink, useLocation, useHistory } from 'react-router-dom';
import { useSelector } from 'react-redux';
import squealnLogo from '../../icons/squealnLogo.png';
import squealnLogowht from '../../icons/squealnLogowht.png';
import search from '../../icons/search.svg';
import './NavBar.css';
import SignUpForm from '../auth/SignUpForm';
import ProfileButton from '../auth/ProfileButton'
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

function NavBar() {
    const history = useHistory();
    const ref = useRef(null);
    const [width, setWidth] = useState(0);
    const sessionUser = useSelector(state => state.session.user);
    const url = useLocation().pathname;
    const [query, setQuery] = useState('');
    const [location, setLocation] = useState('LA and the BAY, CA');
    const [loc, setLoc] = useState('CA');
    let sessionLinks;

    useLayoutEffect(() => {
        if (ref.current) {
            const updateWidth = () => {
                setWidth(ref.current.offsetWidth);
            }
            updateWidth();
            window.addEventListener('resize', updateWidth);

            return () => window.removeEventListener('resize', updateWidth)
        }
    }, [url]);
    // Hello world

    const onSubmit = (e) => {
        e.preventDefault();
        const tempQuery = query;
        setQuery('');
        history.push(`/biz?type=${tempQuery}&loc=${loc}`)
    }

    function changeLocLAandBAY() {
        setLocation('LA and the BAY, CA');
        setLoc('CA');
    }
    function changeLocLA() {
        setLocation('Los Angeles, CA');
        setLoc('Los Angeles');
    }
    function changeLocOAK() {
        setLocation('Oakland, CA');
        setLoc('Oakland');
    }
    function changeLocSF() {
        setLocation('San Francisco, CA');
        setLoc('San Francisco');
    }
    function changeLocSJ() {
        setLocation('San Jose, CA');
        setLoc('San Jose');
    }

    if (sessionUser) {
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
        <div className={url === '/' ? 'header-container gradient' : url.includes('new') || url.includes('update') || url.includes('write') ? 'header-container-sm header-container-fixed' : 'header-container header-container-fixed'}>
            <div className={sessionUser ? 'header-top-portion-user' : 'header-top-portion-sl'}>
                <div className={sessionUser ? 'logo-left-section-user' : 'logo-left-section-sl'}>
                    <NavLink className='logo' exact to="/">
                        <img src={url === '/' ? squealnLogowht : squealnLogo}
                            alt='logo' className='squeal-logo' />
                    </NavLink>
                </div>
                <div className={sessionUser ? 'search-and-buttons-right-section-user' : 'search-and-buttons-right-section-sl'}>
                    {url.includes('new') || url.includes('update') || url.includes('write') ? <div></div> : <div className='nav-search-section'>
                        <form className='search-query-section' onSubmit={onSubmit}>
                            <label className='search-input-label search-input-label-left'>
                                <input className='search-query-input search-input'
                                    placeholder="noodles, pizza, donuts"
                                    type='text'
                                    value={query}
                                    onChange={(e) => setQuery(e.target.value)}
                                    onKeyPress={(e) => e.key === "Enter" ? history.push(`/biz?type=${query}&loc=${loc}`) : null}
                                    />
                            </label>
                            <span className='inbetween-inputs' />
                            <label ref={ref} className='search-input-label search-input-label-right'>
                                <input className='search-location-input search-input'
                                    // placeholder='Los Angeles, CA'
                                    value={location}
                                    readOnly
                                />
                                <div className='tooltip-location' style={{ width: `${width}px` }}>
                                    <button id='LAbay' className='dropdown-location' onClick={(e) => {
                                        e.preventDefault();
                                        changeLocLAandBAY();
                                    }}>
                                        LA & the BAY
                                    </button>
                                    <button id='LA' className='dropdown-location' onClick={(e) => {
                                        e.preventDefault();
                                        changeLocLA();
                                    }}>
                                        Los Angeles, CA
                                    </button>
                                    <button id='OAK' className='dropdown-location' onClick={(e) => {
                                        e.preventDefault();
                                        changeLocOAK();
                                    }}>
                                        Oakland, CA
                                    </button>
                                    <button id='SF' className='dropdown-location' onClick={(e) => {
                                        e.preventDefault();
                                        changeLocSF();
                                    }}>
                                        San Francisco, CA
                                    </button>
                                    <button id='SJ' className='dropdown-location' onClick={(e) => {
                                        e.preventDefault();
                                        changeLocSJ();
                                    }}>
                                        San Jose, CA
                                    </button>
                                </div>
                            </label>
                            <button type='submit' className='search-button'>
                                <img src={search} alt='icon' className='search-icon' />
                            </button>
                        </form>
                    </div>}
                    {sessionUser ? <span className='header-gap-search-buttons' /> : null}
                    <div className={url.includes('new') || url.includes('update') || url.includes('write') ? 'buttons-form-stuff' : sessionUser ? 'buttons-user-stuff' : 'buttons-sl-stuff'}>
                        {url.includes('new') || url.includes('update') || url.includes('write') ? <div></div> : <><NavLink to='/biz/new' className={sessionUser ? 'navbar-button-left' : 'navbar-button-left-sl'}>
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
            {url.includes('new') || url.includes('update') || url.includes('write') ? null :
                <div className={sessionUser ? 'header-bottom-portion-user' : 'header-bottom-portion-sl'}>
                    <div className='empty-below-icon' />
                    <div className='buttons-under-search'>
                        <div className='tooltip-under-search'>
                            <button className={url === '/' ? 'header-bottom-buttons fast-food-button' : 'header-bottom-buttons ff-button-blk'}>
                                Quick Meals <svg width="24" height="24" className={url === '/' ? "chevron-svg" : "chevron-svg-blk"}><path d="M12 15.25a1 1 0 01-.7-.29l-4.58-4.5A1.011 1.011 0 018.12 9L12 12.85 15.88 9a1 1 0 111.4 1.42L12.7 15a1 1 0 01-.7.25z"></path></svg>
                            </button>
                            <div className='tooltiptext tooltip-ff'>
                                <a className='category-link' href='/biz?type=hotdogs'><button className='dropdown-display-text top-dropdown left-ffdropdown'>
                                    <img className='tooltip-icons' src={fastfood} alt='icon' />Fast Food
                                </button></a>
                                <a className='category-link' href='/biz?type=pizza'><button className='dropdown-display-text top-dropdown right-ffdropdown'>
                                    <img className='tooltip-icons' src={pizza} alt='icon' />Pizza
                                </button></a>
                                <a className='category-link' href='/biz?type=delivery'><button className='dropdown-display-text left-ffdropdown'>
                                    <img className='tooltip-icons' src={delivery} alt='icon' />Delivery
                                </button></a>
                                <a className='category-link' href='/biz?type=burgers'><button className='dropdown-display-text right-ffdropdown'>
                                    <img className='tooltip-icons' src={burger} alt='icon' />Burgers
                                </button></a>
                                <a className='category-link' href='/biz?type=sandwiches'><button className='dropdown-display-text left-ffdropdown'>
                                    <img className='tooltip-icons' src={sandwich} alt='icon' />Sandwiches
                                </button></a>
                                <a className='category-link' href='/biz?type=chicken_wings'><button className='dropdown-display-text right-ffdropdown'>
                                    <img className='tooltip-icons' src={chicken} alt='icon' />Chicken Wings
                                </button></a>
                                <a className='category-link' href='/biz?type=pickup'><button className='dropdown-display-text bottom-dropdown left-ffdropdown'>
                                    <img className='tooltip-icons' src={takeout} alt='icon' />Takeout
                                </button></a>
                                <a className='category-link' href='/biz?type=donuts'><button className='dropdown-display-text bottom-dropdown right-ffdropdown'>
                                    <img className='tooltip-icons' src={donut} alt='icon' />Donuts
                                </button></a>
                            </div>
                        </div>
                        <div className='tooltip-under-search dessert-under'>
                            <button className={url === '/' ? 'header-bottom-buttons dessert-button' : 'header-bottom-buttons dessert-button-blk'}>
                                Dessert <svg width="24" height="24" className={url === '/' ? "chevron-svg" : "chevron-svg-blk"}><path d="M12 15.25a1 1 0 01-.7-.29l-4.58-4.5A1.011 1.011 0 018.12 9L12 12.85 15.88 9a1 1 0 111.4 1.42L12.7 15a1 1 0 01-.7.25z"></path></svg>
                            </button>
                            <div className='tooltiptext tooltip-ff'>
                                <a className='category-link' href='/biz?type=bakeries'><button className='dropdown-display-text top-dropdown left-ffdropdown'>
                                    <img className='tooltip-icons' src={bakery} alt='icon' />Bakeries
                                </button></a>
                                <a className='category-link' href='/biz?type=bubbletea'><button className='dropdown-display-text top-dropdown right-ffdropdown'>
                                    <img className='tooltip-icons' src={boba} alt='icon' />Bubble Tea
                                </button></a>
                                <a className='category-link' href='/biz?type=desserts'><button className='dropdown-display-text left-ffdropdown'>
                                    <img className='tooltip-icons' src={dessert} alt='icon' />Desserts
                                </button></a>
                                <a className='category-link' href='/biz?type=coffee'><button className='dropdown-display-text right-ffdropdown'>
                                    <img className='tooltip-icons' src={coffee} alt='icon' />Coffee & Tea
                                </button></a>
                                <a className='category-link' href='/biz?type=icecream'><button className='dropdown-display-text left-ffdropdown'>
                                    <img className='tooltip-icons' src={icecream} alt='icon' />Ice Cream
                                </button></a>
                                <a className='category-link' href='/biz?type=donuts'><button className='dropdown-display-text right-ffdropdown'>
                                    <img className='tooltip-icons' src={donut} alt='icon' />Donuts
                                </button></a>
                                <a className='category-link' href='/biz?type=juicebars'><button className='dropdown-display-text bottom-dropdown left-ffdropdown'>
                                    <img className='tooltip-icons' src={smoothie} alt='icon' />Smoothies
                                </button></a>
                                <a className='category-link' href='/biz?type=cafes'><button className='dropdown-display-text bottom-dropdown right-ffdropdown'>
                                    <img className='tooltip-icons' src={cafe} alt='icon' />Cafes
                                </button></a>
                            </div>
                        </div>
                        <div className='tooltip-under-search'>
                            <button className={url === '/' ? 'header-bottom-buttons coffee-tea-button' : 'header-bottom-buttons popular-button-blk'}>
                                Popular <svg width="24" height="24" className={url === '/' ? "chevron-svg" : "chevron-svg-blk"}><path d="M12 15.25a1 1 0 01-.7-.29l-4.58-4.5A1.011 1.011 0 018.12 9L12 12.85 15.88 9a1 1 0 111.4 1.42L12.7 15a1 1 0 01-.7.25z"></path></svg>
                            </button>
                            <div className='tooltiptext tooltip-ff'>
                                <a className='category-link' href='/biz?type=bbq'><button className='dropdown-display-text top-dropdown left-ffdropdown'>
                                    <img className='tooltip-icons' src={bbq} alt='icon' />Barbeque
                                </button></a>
                                <a className='category-link' href='/biz?type=korean'><button className='dropdown-display-text top-dropdown right-ffdropdown'>
                                    <img className='tooltip-icons' src={korean} alt='icon' />Korean
                                </button></a>
                                <a className='category-link' href='/biz?type=chinese'><button className='dropdown-display-text left-ffdropdown'>
                                    <img className='tooltip-icons' src={chinese} alt='icon' />Chinese
                                </button></a>
                                <a className='category-link' href='/biz?type=mexican'><button className='dropdown-display-text right-ffdropdown'>
                                    <img className='tooltip-icons' src={taco} alt='icon' />Mexican
                                </button></a>
                                <a className='category-link' href='/biz?type=italian'><button className='dropdown-display-text left-ffdropdown'>
                                    <img className='tooltip-icons' src={italian} alt='icon' />Italian
                                </button></a>
                                <a className='category-link' href='/biz?type=vietnamese'><button className='dropdown-display-text right-ffdropdown'>
                                    <img className='tooltip-icons' src={viet} alt='icon' />Vietnamese
                                </button></a>
                                <a className='category-link' href='/biz?type=japanese'><button className='dropdown-display-text bottom-dropdown left-ffdropdown'>
                                    <img className='tooltip-icons' src={japanese} alt='icon' />Japanese
                                </button></a>
                                <a className='category-link' href='/biz?type=mediterranean'><button className='dropdown-display-text bottom-dropdown right-ffdropdown'>
                                    <img className='tooltip-icons' src={med} alt='icon' />Mediterranean
                                </button></a>
                            </div>
                        </div>

                    </div>
                </div>}
        </div>
    )
}

export default NavBar;
