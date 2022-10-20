import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { NavLink } from "react-router-dom";
import { getAllBiz } from '../../store/businesses';
import ReactPaginate from 'react-paginate';
import FuzzySearch from 'fuzzy-search';
import { search, clearData } from "../../store/businesses";

import x from '../../icons/all-biz-page/x.svg';
import check from '../../icons/all-biz-page/check.svg';
import txtbub from '../../icons/all-biz-page/text-bubble.svg';
import './Biz.css';

import { types, types_alias } from '../../assets/types';
import Search from "./search";
import { BizToFront } from "../../assets/bizNames";

export default function Biz() {
    const biz = useSelector(state => state.businesses.allBusinesses);
    const bizArr = Object.values(biz);

    const dispatch = useDispatch();

    const [pageNum, setPageNum] = useState(0);

    const [activePrice, setActivePrice] = useState(false);
    const [activeOpen, setActiveOpen] = useState(false);
    const [activeDel, setActiveDel] = useState(false);
    const [activeTakeout, setActiveTakeout] = useState(false);
    const [activeRes, setActiveRes] = useState(false);

    const [query, setQuery] = useState('');
    const [showBizTypes, setShowBizTypes] = useState([]);

    // console.log('types to the front', types)


    /* ------------SEARCH FXNS/LOGIC------------ */
    const searchFunc = new FuzzySearch(bizArr, ['transactions.transaction', 'types.type', 'name'])

    const res = searchFunc.search(query)
    console.log('using search', res)

    const handleSubmit = (e) => {
        e.preventDefault();
        dispatch(search(res))
        clearData()
        // console.log('SUCCESS')
    }



    /* ----------PAGINATION FXNS/LOGIC---------- */
    const bizPerPage = 10;
    const visitedPages = pageNum * bizPerPage;
    const pageCount = Math.ceil(res.length / bizPerPage);
    const pageChange = ({ selected }) => {
        setPageNum(selected);
    }

    const bizzies = res.slice(visitedPages, visitedPages + bizPerPage)
    // console.log('this the bizzies', bizzies)


    /* -------------TIME FXNS/LOGIC------------- */
    let current_time;
    const settingTime = () => {
        const today = new Date();
        let hours = today.getHours().toString()
        let mins = today.getMinutes().toString()
        if (hours.length === 1) hours = "0" + hours;
        if (mins.length === 1) mins = "0" + mins;
        return hours + mins
    }
    current_time = settingTime()

    const time_conversion = (time) => {
        if (Number(time) > 1200) {
            time = time - 1200
        }
        let nums = time.toString().split('')

        if (nums.length === 3) return nums[0] + ':' + nums[1] + nums[2]
        if (nums.length === 4) return nums[0] + nums[1] + ':' + nums[2] + nums[3]
    }


    /* ------------TOGGLE FXNS/LOGIC------------ */
    const toggleIdPrice = () => {
        setActivePrice(!activePrice);
    }
    const toggleIdOpen = () => {
        setActiveOpen(!activeOpen);
        setQuery(query ? 'open' : '')
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
            <form id='search-form' onSubmit={handleSubmit}>
                <input
                    type='search'
                    value={query}
                    onChange={e => setQuery(e.target.value.toLowerCase())}
                />
                <button type='submit'>Submit</button>
            </form>

            <h1 className="allbiz-title">Best {query ? query[0].toUpperCase() + query.substring(1) : "Food"} Near Me</h1>
            <div className="types-buttons">
                <button
                    id={activePrice ? 'type-butt-price-act' : 'type-butt'}
                    onClick={() => {
                        toggleIdPrice()
                    }
                    }
                >
                    Price
                    <svg width='12' height='12'><path d="M 8 10.25 a 0.746 0.746 0 0 1 -0.525 -0.215 l -3.055 -3 a 0.75 0.75 0 0 1 1.05 -1.07 L 8 8.449 l 2.53 -2.484 a 0.75 0.75 0 0 1 1.05 1.07 l -3.055 3 A 0.746 0.746 0 0 1 8 10.25 Z"></path></svg>
                </button>
                <button
                    id={activeOpen ? 'type-butt-act' : 'type-butt'}
                    value={query}
                    type='submit'
                    onClick={() => {
                        toggleIdOpen()
                    }
                    }
                >
                    Open Now
                </button>
                <button
                    id={activeDel ? 'type-butt-act' : 'type-butt'}
                    value={query}
                    type='submit'
                    onClick={() => {
                        toggleIdDel()
                        setQuery('delivery')
                    }
                    }
                >
                    Offers Delivery
                </button>
                <button
                    id={activeTakeout ? 'type-butt-act' : 'type-butt'}
                    value={query}
                    type='submit'
                    onClick={() => {
                        toggleIdTakeout()
                        setQuery('pickup')
                    }
                    }
                >
                    Offers Takeout
                </button>
                <button
                    id={activeRes ? 'type-butt-act' : 'type-butt'}
                    value={query}
                    type='submit'
                    onClick={() => {
                        toggleIdRes()
                        setQuery('restaurant_reservation')
                    }
                    }
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
            <Search data={res}/>
            {/* <div>
                <ReactPaginate
                    // breakLabel='...'
                    previousLabel="<"
                    nextLabel='>'
                    pageRangeDisplayed='5'
                    pageCount={pageCount}
                    onPageChange={pageChange}
                    containerClassName='pagination-container'
                    activeClassName="pagination-active"
                    pageClassName="pag-num"
                    pageLinkClassName='pag-txt'
                    disabledLinkClassName='pag-hide'
                />
            </div> */}
        </main>
    )
}
