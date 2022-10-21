import React, { useState, useEffect } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import { authenticate } from './store/session';
import Navbar from './components/Navbar';
import HomeBanner from './components/Navbar/homeBanner';
import Footer from './components/Footer';
import ErrorPage from './components/ErrorPage/ErrorPage';
import UserPage from './components/User/UserPage';
import HomePage from './components/HomePage';
import BusinessDetails from './components/BusinessDetails/BusinessDetails';
import CreateBizForm from './components/CreateBizForm';
import UpdateBizForm from './components/UpdateBizForm';
import CreateBizImgForm from './components/CreateBizImgForm';
import ReviewForm from './components/ReviewForm';
import CreateReviewImgForm from './components/CreateReviewImgForm';
import Search from './components/Biz/search';
import EditReview from './components/ReviewForm/EditReview';
import WriteAReview from './components/ReviewForm/WriteAReview';


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
            <Navbar />

            <Switch>
                <Route exact path='/'>
                    <HomeBanner />
                    <HomePage />
                    <Footer />
                </Route>
                <Route exact path='/current'>
                    {user && (
                        <UserPage />
                    )}
                    {!user && (
                        <ErrorPage />
                    )}
                    <Footer />
                </Route>
                <Route exact path='/biz/current'>
                    {user && (
                        <UserPage />
                    )}
                    {!user && (
                        <ErrorPage />
                    )}
                    <Footer />
                </Route>

                <Route exact path='/biz/new'>
                    <CreateBizForm />
                </Route>

                <Route exact path='/biz/:bizId/images/new'>
                    <CreateBizImgForm />
                </Route>

                <Route exact path='/biz/:bizId/update'>
                    <UpdateBizForm />
                </Route>

                <Route exact path='/biz/:bizId/review/:reviewId'>
                    <EditReview />
                </Route>

                <Route exact path='/biz/:bizId'>
                    <BusinessDetails />
                    <Footer />
                </Route>

                <Route exact path='/biz'>
                    <Search />
                    <Footer />
                </Route>

                <Route exact path='/reviews/current'>
                    {user && (
                        <UserPage />
                    )}
                    {!user && (
                        <ErrorPage />
                    )}
                    <Footer />
                </Route>

                <Route exact path='/review/:reviewId/images/new'>
                    <CreateReviewImgForm />
                </Route>

                <Route exact path='/newreview/biz/:bizId'>
                    <ReviewForm />
                </Route>
                <Route exact path='/writeareview'>
                    <WriteAReview />
                </Route>
            </Switch>

        </BrowserRouter>
    );
}

export default App;
