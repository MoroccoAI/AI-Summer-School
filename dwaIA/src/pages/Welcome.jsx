import Logo from '../assets/PhamacieLogo.svg'
import Button from '@mui/material/Button';
import SendIcon from '@mui/icons-material/Send';
function Welcome(){
    return (
     <div style={{display:"flex", flexDirection:"column",borderRadius:"50px",alignItems:"center",rowGap:"30px", backgroundColor:"#EEEEEE" }}>
       <img src={Logo} style={{width:"200px"}}/>
       <p style={{width:"500px",fontWeight:"bold"}}>
          The proposed app addresses the challenges of illegible medical transcriptions and the inconvenience of finding available medications. By utilizing optical character recognition (OCR) and natural language processing (NLP), the app converts handwritten transcriptions into readable text and extracts crucial information. It then searches for pharmacies based on drug availability, location, and price, recommending the best option to patients. This streamlined approach enhances patient comprehension, eliminates the need for multiple pharmacy visits, and improves overall convenience in accessing prescribed medications.
          an app</p>
        <Button variant="contained" endIcon={<SendIcon />}>
          Let's started
        </Button>
      </div>
    )
}
export default Welcome
