import React, { useEffect, useState, useContext } from 'react'
import { useParams, Link } from 'react-router-dom';
import axios from 'axios';

import { AuthContext } from "../App";

function Graphic() {
    let { id } = useParams();
    const [graphicObject, setGraphicObject] = useState({});
    const [comments, setComments] = useState([]);
    const [newComment, setNewComment] = useState("")
    const { authState } = useContext(AuthContext);


    useEffect(() => {
        axios.get(`http://localhost:3001/graphics/byId/${id}`).then((response) => {
            setGraphicObject(response.data);
        });
        axios.get(`http://localhost:3001/comments/${id}`).then((response) => {
            setComments(response.data);
        });
    }, []);

    const addComment = () => {
        axios
            .post("http://localhost:3001/comments", {
                commentText: newComment,
                GraphicId: id,
            },
                {
                    headers: {
                        accessToken: localStorage.getItem("accessToken"),
                    },
                }
            )
            .then((response) => {
                if (response.data.error) {
                    alert(response.data.error);
                } else {
                    const commentToAdd = {
                        commentText: newComment,
                        username: response.data.username,
                        id: response.data.id
                    };
                    setComments([...comments, commentToAdd]); // dodaje na koniec nowy komentarz, żeby wyświetliło się bez odświeżania strony
                    setNewComment(""); //żeby wyczyścić input
                }
            });
    };

    const deleteComment = (id) => {
        axios
            .delete(`http://localhost:3001/comments/${id}`, {
                headers: { accessToken: localStorage.getItem("accessToken") },
            })
            .then(() => {
                setComments(
                    comments.filter((val) => {
                        return val.id !== id;
                    })
                );
            });
    };

    return (
        <div className="graphicPage">
            <div className="post">
                <div className="graphics">
                    <img className="individualImg" src={graphicObject.graphics} alt="graphics" />
                </div>
                <div className='description'>
                    <div className="title"> {graphicObject.title} </div>
                    <div className="body">{graphicObject.description}</div>
                    <div className="footer">
                        <Link to={`/profile/${graphicObject.UserId}`}> @{graphicObject.username} </Link>
                    </div>
                </div>
            </div>
            <div className='addCommentContainer'>
                <input
                    type="text"
                    placeholder=' Comment ...'
                    autoComplete='off'
                    value={newComment}
                    onChange={(event) => {
                        setNewComment(event.target.value)
                    }} />
                <button onClick={addComment}> Add Comment </button>
            </div>
            <div className='listOfComments'>
                {comments.map((comment, key) => {
                    return (
                        <div key={key} className='comment'>
                            <div className='commentHeader'>
                                <div className='commentUsername'> @{comment.username} </div>
                                {authState.username === comment.username &&
                                    <button onClick={() => {
                                        deleteComment(comment.id);
                                    }}>X</button>}
                            </div>
                            <div className='commentBody'>
                                {comment.commentText}
                            </div>
                        </div>);
                })}
            </div>
        </div>
    );
}

export default Graphic;
