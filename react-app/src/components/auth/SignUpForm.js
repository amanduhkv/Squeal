import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux'
import { Redirect, NavLink } from 'react-router-dom';
import { signUp, login } from '../../store/session';
import { Modal } from '../../context/Modal';
import party from '../../icons/login.png';
import './SignUpForm.css';

const SignUpForm = () => {
    const [errors, setErrors] = useState([]);
    const [first_name, setFirstname] = useState('');
    const [last_name, setLastname] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [zipcode, setZipCode] = useState('');
    const [showLogModal, setShowLogModal] = useState(false);
    const [showSignModal, setShowSignModal] = useState(false);
    const user = useSelector(state => state.session.user);
    const dispatch = useDispatch();

    const onSignUp = async (e) => {
        e.preventDefault();
        if (password) {
            const data = await dispatch(signUp(first_name, last_name, email, password, zipcode));
            if (data) {
                setErrors(data)
            }
        }
    };

    const onLogin = async (e) => {
        e.preventDefault();
        const data = await dispatch(login(email, password));
        if (data) {
            setErrors(data);
        }
    };


    const updateFirstname = (e) => {
        setFirstname(e.target.value);
    };

    const updateLastname = (e) => {
        setLastname(e.target.value);
    };

    const updateEmail = (e) => {
        setEmail(e.target.value);
    };

    const updatePassword = (e) => {
        setPassword(e.target.value);
    };

    const updateZipCode = (e) => {
        setZipCode(e.target.value);
    };

    if (user) {
        return <Redirect to='/' />;
    }

    return (
        <>
    {/* -----------------------------LOG IN MODAL----------------------------- */}
            <button className='login-button session-buttons' onClick={() => { setShowLogModal(true) }}>
                <span className='session-butt-word login-word'>
                    Log In
                </span>
            </button>
            {showLogModal && (
                <Modal id='border-modal' onClose={() => {
                    // console.log('on close')
                    setShowLogModal(false)
                }}>
                    <div id="two-cols">
                        <div id='left-side'>
                            <div id="login-text">
                                <h2 id="login-title">Log in to Squeal</h2>
                                <h5 id="signup-redirect">
                                    <div className='text'>New to Squeal? </div>
                                    <div className='button' onClick={() => {
                                    setShowSignModal(true)
                                    setShowLogModal(false)
                                }}>
                                    Sign up
                                </div>
                                </h5>
                                <p id="terms">By logging in, you agree to Squeal's Terms of Service and Privacy Policy.</p>

                            </div>
                            <form id='login-form' onSubmit={onLogin}>
                                <div>
                                    {errors.map((error, ind) => (
                                        <div key={ind}>{error}</div>
                                    ))}
                                </div>
                                <button
                                    id='demo-button'
                                    type='submit'
                                    onClick={() => {
                                        setEmail('KermitFrog@user.io')
                                        setPassword('password')
                                    }}
                                >
                                    Continue with DemoUser
                                </button>

                                <div id='lines'><span className='or'>OR</span></div>
                                <div>
                                    <input
                                        id='login-input'

                                        name='email'
                                        type='text'
                                        placeholder='Email'
                                        value={email}
                                        onChange={updateEmail}
                                    />
                                </div>
                                <div>
                                    <input
                                        id='login-input'
                                        name='password'
                                        type='password'
                                        placeholder='Password'
                                        value={password}
                                        onChange={updatePassword}
                                    />
                                </div>
                                <button id='login-button' type='submit'>Log In</button>
                            </form>
                            <div id='login-fineprint'>
                                <p id='fineprint-text'>New to Squeal?</p>
                                <div id='fineprint-link' onClick={() => {
                                    setShowSignModal(true)
                                    setShowLogModal(false)
                                }}>
                                    Sign up
                                </div>
                            </div>
                        </div>
                        <div>
                            <img id='party' src={party} alt="login-party" />
                        </div>
                    </div>
                </Modal>
            )}
    {/* -----------------------------SIGN UP MODAL----------------------------- */}
            <button className='signup-button session-buttons' onClick={() => { setShowSignModal(true) }}>
                <span className='session-butt-word signup-word'>
                    Sign Up
                </span>
            </button>
            {showSignModal && (
                <Modal id='border-modal' onClose={() => {
                    setShowSignModal(false)
                }}>
                    <div id="two-cols">
                        <div id='left-side'>
                            <div id="login-text">
                                <h2 id="login-title">Sign Up for Squeal</h2>
                                <h5 id="signup-redirect">
                                    Connect with great local businesses
                                </h5>
                                <p id="terms">By continuing, you agree to Squeal's Terms of Service and acknowledge Squeal's Privacy Policy.</p>
                            </div>
                            <form onSubmit={onLogin}>
                                <button
                                    id='demo-button'
                                    type='submit'
                                    onClick={() => {
                                        setFirstname('Kermit')
                                        setLastname('Frog')
                                        setEmail('KermitFrog@user.io')
                                        setPassword('password')
                                        setZipCode('91521')
                                    }}
                                >
                                    Continue with DemoUser
                                </button>
                                <p id='terms-signup'>Don't worry, we never post without your permission.</p>
                                <div id='lines'><span className='or'>OR</span></div>
                            </form>
                            <form onSubmit={onSignUp}>
                                <div>
                                    {errors.map((error, ind) => (
                                        <div key={ind}>{error}</div>
                                    ))}
                                </div>
                                <div id='first-last-name'>
                                    <input
                                        id='login-input'
                                        type='text'
                                        name='firstname'
                                        placeholder='First Name'
                                        onChange={updateFirstname}
                                        value={first_name}
                                    ></input>
                                    <input
                                        id='login-input'
                                        type='text'
                                        name='lastname'
                                        placeholder='Last Name'
                                        onChange={updateLastname}
                                        value={last_name}
                                    ></input>
                                </div>
                                <div id='email'>
                                    <input
                                        id='login-input'
                                        type='text'
                                        name='email'
                                        placeholder='Email'
                                        onChange={updateEmail}
                                        value={email}
                                    ></input>
                                </div>
                                <div id='password'>
                                    <input
                                        id='login-input'
                                        type='password'
                                        name='password'
                                        placeholder='Password'
                                        onChange={updatePassword}
                                        value={password}
                                    ></input>
                                </div>
                                <div id='zip'>
                                    <input
                                        id='login-input'
                                        type='text'
                                        name='zipcode'
                                        placeholder='ZIP Code'
                                        onChange={updateZipCode}
                                        value={zipcode}
                                        required={true}
                                    ></input>
                                </div>
                                <button id='login-button' type='submit'>Sign Up</button>
                            </form>
                            <div id='login-fineprint'>
                                <p id='fineprint-text'>Already on Squeal?</p>
                                <div id='fineprint-link' onClick={() => {
                                    setShowSignModal(false)
                                    setShowLogModal(true)
                                }}>Log in</div>
                            </div>
                        </div>
                        <div>
                            <img id='party' src={party} alt="login-party" />
                        </div>
                    </div>
                </Modal>
            )}
        </ >
    );
};

export default SignUpForm;
