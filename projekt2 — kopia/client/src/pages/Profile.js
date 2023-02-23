import React, { useEffect, useState } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import axios from 'axios';

function Profile() {
  let { id } = useParams();
  const [username, setUsername] = useState("");
  const [listOfGraphics, setListOfGraphics] = useState([]);
  let navigate = useNavigate();

  useEffect(() => {
    axios.get(`http://localhost:3001/auth/basicinfo/${id}`).then((response) => {
      setUsername(response.data.username);
    });

    axios.get(`http://localhost:3001/graphics/byUserId/${id}`).then((response) => {
      setListOfGraphics(response.data);
    });
  }, []);

  return (
    <div className='profilePageContainer'>
      <div className='basicInfo'><h1>@{username}</h1></div>

      <div className='gallery'>
        {listOfGraphics.map((value, key) => {
          return (
            <div key={key} className="graphics" onClick={() => { navigate(`/graphic/${value.id}`) }}>
              <img className='individualImg' src={value.graphics} alt="graphics" />
            </div>
          );
        })}

      </div>
    </div>
  );
}

export default Profile
