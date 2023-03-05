import {createBrowserRouter,Route, createRoutesFromElements, RouterProvider} from "react-router-dom";
import HomePage from "./pages/HomePage";
import './index.css'
import LoginPage from "./pages/LoginPage";
import NavBar from "./components/NavBar";
import axios from "axios";


function App() {
  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
          }
        }
      }
    return cookieValue;
  }
  const csrfToken = getCookie('csrftoken');

  axios.defaults.headers.common["X-CSRFToken"] = csrfToken;
const router = createBrowserRouter(
  createRoutesFromElements(
    <Route path="/" element={<NavBar/>}>
        <Route index element={<HomePage/>}></Route>
        <Route path="/login" element={<LoginPage/>}></Route>
      </Route>
      )
)
  return (
      <RouterProvider router={router}/>
  )
}

export default App
