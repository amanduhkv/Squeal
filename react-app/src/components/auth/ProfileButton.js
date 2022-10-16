import React, { useState, useEffect } from "react";
import { useDispatch } from 'react-redux';
import { useHistory } from "react-router-dom";
import * as sessionActions from '../../store/session';
import LogoutButton from "./LogoutButton";
import userIcon from '../../icons/user-pig.png'
import aboutPig from '../../icons/about-pig.png'
import bizPig from '../../icons/biz-pig.png'
import reviewPig from '../../icons/review-pig.png'
import './ProfileButton.css'

function ProfileButton({ user }) {
  const dispatch = useDispatch();
  const [showMenu, setShowMenu] = useState(false);
  const history = useHistory();

  const openMenu = () => {
    if (showMenu) return;
    setShowMenu(true);
  };

  useEffect(() => {
    if (!showMenu) return;

    const closeMenu = () => {
      setShowMenu(false);
    };

    document.addEventListener('click', closeMenu);

    return () => document.removeEventListener("click", closeMenu);
  }, [showMenu]);


  return (
    <>
    <div className='profile-button' onClick={openMenu}>
      <img className='user-icon' src={userIcon} alt='user' />
    </div>
      {showMenu && (
        <div className="profile-dropdown">
          <div id='dropdown-text'>
            <img src={aboutPig} width='25px'/>
            About Me
          </div>
          <div id='dropdown-text'>
            <img src={bizPig} width='30px' />
            My Businesses
          </div>
          <div id='dropdown-text'>
            <img src={reviewPig} width='30px' />
            My Reviews
          </div>
          <div id='logout'>
            <LogoutButton />
          </div>
        </div>
      )}
    </>
  );
}

export default ProfileButton;
