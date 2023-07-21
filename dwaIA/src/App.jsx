import { useState,createContext } from 'react'
import './App.css'
import Container from '@mui/material/Container'
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import SendIcon from '@mui/icons-material/Send';
import Welcome from './pages/Welcome.jsx'
import { BrowserRouter,Routes, Route } from "react-router-dom";
import Recommander from './pages/Recommander'
import MyContext from './Context'





function App() {
  const [page, setPage] = useState(0)
  const [drags, setDrags] = useState([])
  const [totalPrice, setTotalPrice] = useState(0)
  const [cposition, setCposition] = useState(undefined)

  return (
   <>
    <MyContext.Provider value={{drags, setDrags, totalPrice, setTotalPrice, cposition, setCposition}}>
      <BrowserRouter>
        <Routes>
         <Route path="/welcome" element ={<Welcome/>}/>
         <Route path="/" element ={<Recommander/>}/>
        </Routes>
     </BrowserRouter>
    </MyContext.Provider>
   </>
  )
}

export default App
