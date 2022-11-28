import React, { useState, useEffect } from 'react'
import { useHistory, useParams } from 'react-router-dom';
import { useDispatch, useSelector } from "react-redux";
import * as bizActions from "../../store/businesses";
import './CreateBizImgForm.css'
import brokenImgPig from '../../icons/broken-img-pig.png';

export default function CreateBizImgForm() {
    const dispatch = useDispatch();
    const history = useHistory();
    const { bizId } = useParams();
    const sessionUser = useSelector(state => state.session.user);
    const biz = useSelector(state => state.businesses.singleBusiness);

    // const [bizImgUrl, setBizImgUrl] = useState(null);
    const [image, setImage] = useState(null);
    const [imageLoading, setImageLoading] = useState(false);

    const [validationErrors, setValidationErrors] = useState([]);

    if (!sessionUser) {
        alert("Please log in or create an account to add an image to your business.");
        history.push("/");
    }

    // LOAD BIZ BY PARAMETER BIZ ID
    useEffect(() => {
        dispatch(bizActions.getOneBiz(bizId));

        return () => dispatch(bizActions.clearData());
    }, [dispatch, bizId]);

    // TODO: ADD MORE VALIDATION ERROR HANDLING
    useEffect(() => {
        const errors = [];

        setValidationErrors(errors);
    }, [image]);

    const handleSubmit = async (e) => {
        e.preventDefault();

        const formData = new FormData();
        formData.append("image", image);

        setImageLoading(true);


        // HANDLING FOR USERS WHO HARDCODE ADD BIZ IMG PAGE:
        if (sessionUser && biz) {
            if ((sessionUser.id !== biz.owner_id)) {
                alert("Only the business owner can update his or her business.");
                history.push("/");
                return;
            }
        }

        try {
            const responseAddImg = await fetch(`/api/biz/${bizId}/images`, {
                method: 'POST',
                body: formData
            });

            if (responseAddImg.json()) {
                setImageLoading(false);
                setValidationErrors([]);
                history.push(`/biz/current`);
            }
        }
        catch (res) {
            console.log("==>ANY ERRORS FROM CREATE BIZ IMG:", res);
            setImageLoading(false);
            // const data = await res.json();
            // if (data && data.errors) return setValidationErrors(data.errors);
        }
    };

    return (
        <div className='form form--add-biz-img'>
            <h1 className='header header--add-biz-img'>Hello! Let's add an image to your business</h1>

            <form onSubmit={handleSubmit} className="form" id="form--add-biz-img">
                {validationErrors.length > 0 && (
                    <ul className="list list--errors">
                        {validationErrors.map((error) => <li key={error} className="li li--error">{error}</li>)}
                    </ul>
                )}

                <div className='container--form-fields'>
                    {/* ----- BIZ IMG SECTION ----- */}
                    <div className='container--form-fields--section container--form-fields--img-section'>
                        <label className='label--add-biz-img' htmlFor="form-field--img">Business Preview Image:</label>
                        <input
                            type="file"
                            name="image"
                            // value={image}
                            onChange={(e) => setImage(e.target.files[0])}
                            required
                            // placeholder='Business Image url'
                            className='form-field'
                            id='form-field--img'
                        />
                        {/* {image && <img className='img img--add-biz-img-url-preview' src={image} alt={image} onError={e => e.target.src=brokenImgPig} />} */}
                    </div>
                </div>

                <button
                    type="submit"
                    disabled={validationErrors.length}
                    className='button button--submit'
                    id='add-biz-img-submit-button'
                >
                    Submit
                </button>
                {(imageLoading)&& <p>Loading...</p>}
            </form>
        </div>
    );
}
