import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { NavLink } from "react-router-dom";
import { getAllBiz } from '../../store/businesses';
import ReactPaginate from 'react-paginate';

import x from '../../icons/all-biz-page/x.svg';
import check from '../../icons/all-biz-page/check.svg';
import txtbub from '../../icons/all-biz-page/text-bubble.svg';
import './Biz.css';

import { types, types_alias } from '../../assets/types';
import Search from "../Search/search";
import { BizToFront } from "../../assets/bizNames";

export default function Biz() {
    const biz = useSelector(state => state.businesses.allBusinesses);
    const bizArr = Object.values(biz);
    const dispatch = useDispatch();



    const [activePrice, setActivePrice] = useState(false);
    const [activeOpen, setActiveOpen] = useState(false);
    const [activeDel, setActiveDel] = useState(false);
    const [activeTakeout, setActiveTakeout] = useState(false);
    const [activeRes, setActiveRes] = useState(false);

    const [query, setQuery] = useState('');
    const [showBizTypes, setShowBizTypes] = useState([]);

    // console.log('types to the front', types)


    /* ------------SEARCH FXNS/LOGIC------------ */
    const searchType = (data) => {
        return data.filter(biz => biz.types.some(type => type.type.toLowerCase().includes(query)))
    }
    const searchTra = (data) => {
        return data.filter(biz => biz.transactions.some(tra => tra.transaction.toLowerCase().includes(query)))
    }





    /* ------------TOGGLE FXNS/LOGIC------------ */
    const toggleIdPrice = () => {
        setActivePrice(!activePrice);
    }
    const toggleIdOpen = () => {
        setActiveOpen(!activeOpen);
    }
    const toggleIdDel = () => {
        setActiveDel(!activeDel);
    }
    const toggleIdTakeout = () => {
        setActiveTakeout(!activeTakeout);
    }
    const toggleIdRes = () => {
        setActiveRes(!activeRes);
    }


    /* -------USE EFFECT:get all bizzies------- */
    useEffect(() => {
        dispatch(getAllBiz())
    }, [dispatch])


    return (
        <main className="main">
            <div>
                <input
                    type='search'
                    value={query}
                    onChange={e => setQuery(e.target.value.toLowerCase())}
                />
            </div>
            <h1 className="allbiz-title">Best Food Near Me in City, State</h1>
            <div className="types-buttons">
                <button
                    id={activePrice ? 'type-butt-price-act' : 'type-butt'}
                    onClick={ e => {
                        toggleIdPrice()
                        setQuery(e.target.value)
                    }
                    }
                >
                    Price
                    <svg width='12' height='12'><path d="M 8 10.25 a 0.746 0.746 0 0 1 -0.525 -0.215 l -3.055 -3 a 0.75 0.75 0 0 1 1.05 -1.07 L 8 8.449 l 2.53 -2.484 a 0.75 0.75 0 0 1 1.05 1.07 l -3.055 3 A 0.746 0.746 0 0 1 8 10.25 Z"></path></svg>
                </button>
                <button
                    id={activeOpen ? 'type-butt-act' : 'type-butt'}
                    value={query}
                    onClick={ e => {
                        toggleIdOpen()
                        setQuery('open')
                        console.log(setQuery(e.target.value))
                    }
                    }
                >
                    Open Now
                </button>
                <button
                    id={activeDel ? 'type-butt-act' : 'type-butt'}
                    onClick={toggleIdDel}
                >
                    Offers Delivery
                </button>
                <button
                    id={activeTakeout ? 'type-butt-act' : 'type-butt'}
                    onClick={toggleIdTakeout}
                >
                    Offers Takeout
                </button>
                <button
                    id={activeRes ? 'type-butt-act' : 'type-butt'}
                    onClick={toggleIdRes}
                >
                    Reservations
                </button>
                {/* <button
                    id={active ? 'type-butt-act-4' : 'type-butt'}
                    onClick={toggleId}
                    >
                    Breakfast & Brunch
                </button> */}
            </div>
            <Search data={searchTra(bizArr) && searchType(bizArr)} />
            
        </main>

    )
}
