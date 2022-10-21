import React, { useState, useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import FuzzySearch from 'fuzzy-search';
import { getAllBiz, clearData } from '../../store/businesses';
import './ReviewForm.css';
import searchicon from '../../icons/search.svg';

const WriteAReview = () => {
    const dispatch = useDispatch();
    const biz = useSelector(state => state.businesses.allBusinesses);
    const bizArr = Object.values(biz);
    const [bizName, setBizName] = useState('');

    useEffect(() => {
        dispatch(getAllBiz());

        return () => dispatch(clearData());
    }, [dispatch])


    const search = new FuzzySearch(bizArr, ['name']);

    const result = search.search(bizName)

    return (
        <div className='writeareview-container'>
            <div className='write-review-inner'>
                <div className='review-biz-search'>
                    <h1 className='find-a-biz-rev'>Find a business to review</h1>
                    <p className='review-anything-text'>Review anything from your favorite steakhouse to your local coffee shop.</p>
                    <form className='review-biz-search-section'>
                        <label className='review-biz-search-label'>
                            <input className='search-query-input search-input'
                                placeholder="Restaurant name"
                                type='text' value={bizName} onChange={(e) => setBizName(e.target.value)} />
                        </label>
                        <button type='submit' className='search-button'>
                            <img src={searchicon} alt='icon' className='search-icon' />
                        </button>
                    </form>
                </div>
                <div className='review-biz-list-container'>
                    <div className='review-biz-card'>
                        <ul className='review-biz-list'>
                            {result.map((biz, i) => (
                                <a className='review-biz-list-a' href={`/newreview/biz/${biz.id}`}><li key={i} className='review-biz-list-item'>
                                    {biz.name}
                                </li></a>
                            ))}</ul>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default WriteAReview
