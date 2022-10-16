import React, { useState, useEffect } from "react";
import { useDispatch } from 'react-redux';
import { useHistory } from "react-router-dom";
import * as sessionActions from '../../store/session';
import LogoutButton from "./LogoutButton";
import userIcon from '../../icons/githubPurple.png'

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
    <button className='profile-button' onClick={openMenu}>
      <img className='user-icon' src={userIcon} alt='user' />
    </button>
      {showMenu && (
        <div className="profile-dropdown">
          <div>About Me</div>
          <div>Find Friends</div>
          <div>Account Settings</div>
          <div>
            <LogoutButton />
          </div>
        </div>
      )}
    </>
  );
}

export default ProfileButton;
