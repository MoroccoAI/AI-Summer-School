import Logo from '../assets/PhamacieLogo.svg'
import Button from '@mui/material/Button';
import { useContext, useEffect, useState } from 'react'
import KeyboardArrowDownIcon from '@mui/icons-material/KeyboardArrowDown';
import MyContext from '../Context';
const drags = [
  {name:"Medcine1", price:100,reimbursement:10.1, description:null},
  {name:"Medcine1", price:100,reimbursement:10.1, description:null},
]
function DrugsScanned(){
  const {drags, setDrags, totalPrice, setTotalPrice} = useContext(MyContext)
  const [drugs, setDrugs] = useState(new Array(drags.length).fill(0))
  useEffect(()=>{
    console.log(drugs)
  },[drugs])
  return (
    <>
       <img src={Logo} style={{width:"200px"}}/>
       <p>Drugs Scanned</p>
    <div style={{width:"100%"}}>
      <div style = {{width:"100%",padding:"10px", display:"flex",rowGap:"10px",flexDirection:"column"}}>
            {
              drags.map((item, index)=>{
                return (
                  <div style={{display:"flex",flexDirection:"column"}}>
                    <div key={index} style={{display:"flex",columnGap:"10px"}}>
                      <KeyboardArrowDownIcon onClick={()=>{
                        const new_drugs = drugs.map((item_, index_)=>{
                          if(index_ == index){
                            if (drugs[index] == 0){
                              return 1
                            }
                            return 0
                          }
                          else{
                            return drugs[index_]
                          }
                        })
                        setDrugs(new_drugs)
                        setTotalPrice(totalPrice + item.price)
                      }}/>
                      <p>{item.name}</p>
                    </div>
                  {
                    drugs[index] == 1 ? (
                  <div style={{display:"flex",flexDirection:"column", paddingLeft:"34px"}}>
                  <p style={{textAlign:"start",maximumWidth:"400px"}}><b>Price:</b> {item.price}</p>
                  <p style={{textAlign:"start",maximumWidth:"400px"}}><b>Reimbursement:</b> {item.reimbursement}</p>
                    </div>
                    ):(<></>)
                  }
                  </div>
                )
              })
            }
         </div>
       </div>
    </>
  )
}
export default DrugsScanned;
