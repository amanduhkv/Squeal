import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getAllBiz } from '../../store/businesses';


export default function Biz() {
    const biz = useSelector(state => state.businesses.allBusinesses);

    const bizArr = Object.values(biz);
    const dispatch = useDispatch();

    useEffect(() => {
        dispatch(getAllBiz())
    }, [dispatch])

    return (
        <main>
            <br></br>
            <br></br>
            <br></br>
            <h1>Testing the splash page</h1>
            {bizArr.map(biz => (
                <div>{biz.name}</div>
            ))}
        </main>
    )
}
