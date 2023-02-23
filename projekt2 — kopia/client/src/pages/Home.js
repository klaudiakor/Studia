import React from 'react'
import axios from "axios";
import { useEffect, useState } from "react";
import { Link } from 'react-router-dom';

function Home() {
  const [listOfGraphics, setListOfGraphics] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:3001/graphics").then((response) => {
      setListOfGraphics(response.data);
    });
  }, []);

  return (
    <div className='gallery'>
      {listOfGraphics.map((value, key) => {
        return (
          <div key={key} className="post" >
            <div className="graphics">
              <Link to={`/graphic/${value.id}`}>
                <img className='individualImg' src={value.graphics} alt="graphics" />
              </Link>
            </div>
            <div className='footer'>
              <div className="username">
                <Link to={`/profile/${value.UserId}`}> @{value.username} </Link>
              </div>
            </div>
          </div>
        );
      })}
    </div>
  );
}

export default Home
