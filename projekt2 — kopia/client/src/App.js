import './App.css';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import { createContext, useState, useEffect } from 'react';
import axios from 'axios';

import Profile from './pages/Profile';
import Home from "./pages/Home";
import CreatePost from "./pages/CreatePost";
import Post from "./pages/Graphic";
import Registration from "./pages/Registration";
import Login from "./pages/Login";
import PageNotFound from './pages/PageNotFound';
import Graphic from './pages/Graphic';


export const AuthContext = createContext(""); // kontekst do śledzenia czy użytkownik jest zalogowany

function App() {

  const [authState, setAuthState] = useState({
    username: "",
    id: 0,
    isLoggedIn: false
  });

  useEffect(() => {
    axios.get('http://localhost:3001/auth/users', {
      headers: {
        accessToken: localStorage.getItem('accessToken'),
      },
    })
      .then((response) => {
        if (response.data.error) {
          setAuthState({ ...authState, isLoggedIn: false });
        } else {
          setAuthState({
            username: response.data.username,
            id: response.data.id,
            isLoggedIn: true
          });
        }
      });

  }, []);


  const logout = () => {
    localStorage.removeItem("accessToken");
    setAuthState({
      username: "",
      id: 0,
      isLoggedIn: false,
    });
  }

  return (
    <div className="App">
      <AuthContext.Provider value={{ authState, setAuthState }}>
        <Router>
          <div className="menu">
            <div className="links">
              <Link to="/"> Home Page</Link>
              <Link to="/createpost"> Create A Post</Link>
            </div>
            <div className='authentication'>
              {!authState.isLoggedIn && (
                <>
                  <h3>|</h3>
                  <Link to="/login">Login</Link>
                  <Link to="/registration">Registration</Link>
                  <h3>|</h3>
                </>
              )}
            </div>
            <div className="loggedInContainer">
              <h1>
                <Link to={`/profile/${authState.id}`}>
                  {authState.username} {console.log("success")}
                </Link>
              </h1>
              {authState.isLoggedIn && <button onClick={logout}> Logout</button>}
            </div>
          </div>
          <Routes>
            <Route path="/" exact element={<Home />} />
            <Route path="/createpost" exact element={<CreatePost />} />
            <Route path="/graphic/:id" exact element={<Graphic />} />
            <Route path="/registration" exact element={<Registration />} />
            <Route path="/profile/:id" exact element={<Profile />} />
            <Route path="/login" exact element={<Login />} />
            <Route path="*" exact element={<PageNotFound />} />
          </Routes>
        </Router>
      </AuthContext.Provider>
    </div>
  );

}

export default App;
