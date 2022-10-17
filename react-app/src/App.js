import React, { useState, useEffect } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { useDispatch } from 'react-redux';
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

function App() {
    const [loaded, setLoaded] = useState(false);
    const dispatch = useDispatch();

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
                    <Footer />
                </Route>
                <Route path='/current'>
                    <UserPage />
                    <Footer />
                </Route>
                <Route path='/biz/current'>
                    <ErrorPage />
                    <Footer />
                </Route>
                <Route path='/reviews/current'>
                    <ErrorPage />
                    <Footer />
                </Route>
            </Switch>

        </BrowserRouter>
    );
}

export default App;
