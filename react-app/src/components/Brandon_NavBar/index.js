import React, { useState } from 'react';
import { NavLink, useLocation } from 'react-router-dom';
import squealnLogo from '../../icons/squealnLogo.png';
import squealnLogowht from '../../icons/squealnLogowht.png';
import search from '../../icons/search.svg';
import userIcon from '../../icons/githubPurple.png';
import './NavBar.css';

function NavBar(){
    const sessionUser = null;
    const url = useLocation().pathname;
    const [ query, setQuery ] = useState('');
    const [ location, setLocation ] = useState('');
    console.log('this is the url',url);
// /*
    let sessionLinks;

    if (sessionUser) {
        sessionLinks = (<>
            <div className='user-icon-container'>
                <img className='user-icon' src={userIcon} alt='user' />
            </div>
        </>)
    }
    else {
        sessionLinks = (<>
            <div className='session-buttons-sbs'>
                <button className='login-button session-buttons'>
                    <span className='session-butt-word login-word'>
                        Log In
                    </span>
                </button>
                <button className='signup-button session-buttons'>
                    <span className='session-butt-word signup-word'>
                        Sign Up
                    </span>
                </button>
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
                        {sessionLinks}
                    </div>
                </div>
            </div>
            <div className='header-bottom-portion'>

            </div>
        </div>
    )
}

export default NavBar;
