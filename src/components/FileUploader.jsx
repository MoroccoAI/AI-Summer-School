import Logo from '../assets/PhamacieLogo.svg'
import Button from '@mui/material/Button';
import { useEffect, useState } from 'react'
import MyContext from '../Context'
import {useContext} from 'react'
import axios from 'axios';
function FileUploader(){
    const [file, setFile] = useState();
    const {drags, setDrags, totalPrice, setTotalPrice} = useContext(MyContext)
    setTotalPrice(0)
    function handleChange(e) {
        var formData = new FormData();
        setFile(URL.createObjectURL(e.target.files[0]));
        formData.append("image", e.target.files[0]);
        axios.post("/api/predict",formData ,{
                headers:{
                  'Content-Type': 'multipart/form-data'
        }
        }).then((response)=>{
          console.log(response.data)
        setDrags(response.data)
        })
    }
  return (
    <>
       <img src={Logo} style={{width:"200px"}}/>
       <p>Upload You Photo</p>
        {file? (
          <img style={{width:"300px"}} src={file}/>
        ):(<></>)}
       <Button
            variant="contained"
            component="label"
       >
                Upload File
            <input
            type="file"
            onChange={handleChange}
            /*onSubmit={()=>{
              axios.post("http://localhost:5000/predict", file,{
                headers:{
                  'Content-Type': 'multipart/form-data'
                }
              }).then((response)=>{
                setDrags(response.data)
              })
            }}*/
            hidden
            />
       </Button>
    </>
  )
}
export default FileUploader;
