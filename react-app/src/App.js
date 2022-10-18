import React, { useState, useEffect } from 'react';
import { BrowserRouter, Route, Switch, useLocation } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
// import LoginForm from './components/auth/LoginForm';
// import SignUpForm from './components/auth/SignUpForm';
// import NavBar from './components/NavBar';
// import ProtectedRoute from './components/auth/ProtectedRoute';
// import UsersList from './components/UsersList';
// import User from './components/User';
import { authenticate } from './store/session';
import Brandon_NavBar from './components/Brandon_NavBar';
import HomeBanner from './components/Brandon_NavBar/homeBanner';
import Footer from './components/Footer';
// import CurrentUserBiz from './components/Biz/UserBiz';
import ErrorPage from './components/ErrorPage/ErrorPage';
import UserPage from './components/User/UserPage';
import HomePage from './components/HomePage';
import Biz from './components/Biz';
import BusinessDetails from './components/BusinessDetails/BusinessDetails';

function App() {
    const [loaded, setLoaded] = useState(false);
    const dispatch = useDispatch();
    const user = useSelector(state => state.session.user);

    useEffect(() => {
        (async () => {
            await dispatch(authenticate());
            setLoaded(true);
        })();
    }, [dispatch]);

    if (!loaded) {
        return null;
    }

    return (
        <BrowserRouter>
            {/* <NavBar />
            <Switch>
                <Route path='/login' exact={true}>
                    <LoginForm />
                </Route>
                <Route path='/sign-up' exact={true}>
                    <SignUpForm />
                </Route>
                <ProtectedRoute path='/users' exact={true} >
                    <UsersList />
                </ProtectedRoute>
                <ProtectedRoute path='/users/:userId' exact={true} >
                    <User />
                </ProtectedRoute>
                <ProtectedRoute path='/' exact={true} >
                    <h1>My Home Page</h1>
                </ProtectedRoute>
            </Switch> */}
            <Brandon_NavBar />
            <Switch>
                <Route exact path='/'>
                    <HomeBanner />
                    <HomePage />
                    <Footer />
                </Route>
                <Route path='/current'>
                    {user && (
                        <UserPage />
                    )}
                    {!user && (
                        <ErrorPage />
                    )}
                    <Footer />
                </Route>
                <Route path='/biz/current'>
                    {user && (
                        <UserPage />
                    )}
                    {!user && (
                        <ErrorPage />
                    )}
                    <Footer />
                </Route>
                <Route exact path='/biz'>
                    <Biz />
                </Route>
                <Route path='/biz/:bizId'>
                    <BusinessDetails />
                </Route>
                <Route path='/reviews/current'>
                    {user && (
                        <UserPage />
                    )}
                    {!user && (
                        <ErrorPage />
                    )}
                    <Footer />
                </Route>
            </Switch>

        </BrowserRouter>
    );
}

export default App;
