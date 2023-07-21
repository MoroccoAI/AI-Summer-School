import Logo from '../assets/PhamacieLogo.svg'
import Button from '@mui/material/Button';
import SendIcon from '@mui/icons-material/Send';
import Welcome from './Welcome';
import FileUploader from '../components/FileUploader';
import DrugsScanned from '../components/DrugsScanned';
import Map from '../components/Map'
import ArrowBackIosNewIcon from '@mui/icons-material/ArrowBackIosNew';
import ArrowForwardIosIcon from '@mui/icons-material/ArrowForwardIos';
import { useState, useEffect } from 'react';
import { drawerClasses } from '@mui/material';
const medcince = ["Medcine 1", "Medcine 2", "Medcine 3"]
function Recommander(){
    let items = [ FileUploader, DrugsScanned, Map]
    let [index, setIndex] = useState(0)
  useEffect(()=>{
    console.log(index)
  },[index])
    return (
     <div style={{display:"flex", flexDirection:"column",borderRadius:"50px",alignItems:"center",padding:"50px",rowGap:"30px", backgroundColor:"#EEEEEE" }}>
            {
              index == 0?(
                <FileUploader/>
              ):index == 1?(
                <DrugsScanned/>
              ):index == 2?(
                <Map/>
              ):(
                <></>)
            }
       <div style={{width:"100%",display:"flex", flexDirection:"row",columnGap:"20px", justifyContent:"space-between"}}>
         <Button  onClick = {()=>{
           console.log(index)
           setIndex(index-1)
         }} style={index == 0 ? {visibility:"hidden"}:{}} variant="contained" startIcon={<ArrowBackIosNewIcon/>}>
           Previous
         </Button>
        <div>
          <div style={{width:"100%",display:"flex", columnGap:"10px", flexDirection:"row"}}>
          {
            items.map((item, index)=>{
              return (
                <SlideNumber value={index}/>
              )
            })
          }
          </div>
        </div>
         <Button style={index == items.length - 1 ? {visibility:"hidden"}:{}} onClick={()=>{
           setIndex(index + 1)
         }
         } variant="contained" endIcon={<ArrowForwardIosIcon />}>
           Next
        </Button>
      </div>
      </div>
    )
}

function SlideNumber({value,active}){
          var style = {display:"flex",alignItems:"center", justifyContent:"center",borderRadius: "60px",backgroundColor:"#1976D2", width:"50px",height:"50px"}
          return (
          <div
                  style={style}
                onClick={()=>{
          }}>
          <p style={{color:"white"}}>{value}</p>
          </div>
          )
}
export default Recommander
