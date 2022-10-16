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

function NavBar(){
    const sessionUser = useSelector(state => state.session.user);
    const url = useLocation().pathname;
    const [ query, setQuery ] = useState('');
    const [ location, setLocation ] = useState('');
    console.log('this is the url',url);
// /*
    let sessionLinks;

    if (sessionUser) {
        console.log('hereeee')
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
        <div className={url === '/' ? 'header-container gradient' : 'header-container header-container-fixed'}>
            <div className={sessionUser ? 'header-top-portion-user' : 'header-top-portion-sl'}>
                <div className={sessionUser ? 'logo-left-section-user' : 'logo-left-section-sl'}>
                    <NavLink className='logo' exact to="/">
                        <img src={url === '/' ? squealnLogowht : squealnLogo}
                                            alt='logo' className='squeal-logo'/>
                    </NavLink>
                </div>
                <div className={sessionUser ? 'search-and-buttons-right-section-user' : 'search-and-buttons-right-section-sl'}>
                    <div className='nav-search-section'>
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
                    </div>
                    {sessionUser ? <span className='header-gap-search-buttons' /> : null}
                    <div className={sessionUser ? 'buttons-user-stuff' : 'buttons-sl-stuff'}>
                        <NavLink to='/businesses/new' className={sessionUser ? 'navbar-button-left' : 'navbar-button-left-sl'}>
                            <button className={url === '/' ? 'top-button-wht header-right-button' : 'top-button-blk header-right-button'}>
                                List a Business
                            </button>
                        </NavLink>
                        <NavLink to='/writeareview' className={sessionUser ? 'navbar-button-right' : 'navbar-button-right-sl'}>
                            <button className={url === '/' ? 'top-button-wht header-right-button' : 'top-button-blk header-right-button'}>
                                Write a Review
                            </button>
                        </NavLink>
                        <div>
                        {sessionLinks}
                        </div>
                    </div>
                </div>
            </div>
            <div className='header-bottom-portion'>

            </div>
        </div>
    )
}

export default NavBar;
