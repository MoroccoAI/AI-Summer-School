
import Logo from '../assets/PhamacieLogo.svg'
import Button from '@mui/material/Button';
import { useEffect, useState, useContext} from 'react'
//import { MapContainer, TileLayer } from 'react-leaflet'
import { MapContainer, Marker, Popup, TileLayer,  useMap } from "react-leaflet";

import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemText from '@mui/material/ListItemText';
import { FixedSizeList} from 'react-window';
import LocalPharmacyIcon from '../assets/local_pharmacy.png'
import pharmacies from '../models/pharmacies.jsx'


import 'leaflet/dist/leaflet.css';
import MyContext from '../Context';
const my_pos = [33.5396, -5.1066]
function RenderRow({ name, price, remise, position }) {
  const {cposition, setCposition} = useContext(MyContext)
  useEffect(()=>{
    console.log(cposition)
  },[cposition])
  return (
    <ListItem  component="div" disablePadding>
      <ListItemButton onClick={()=>{
            setCposition(position)
        }}>
        <div style={{display:"flex",flexDirection:"row",width:"100%",justifyContent:"space-between", alignItems:"space-between"}}>
          <p>{name}</p>
          <div  style={{display:"flex", flexDirection:"column"}}>
            <p style={{fontSize:"10px", color:"red", textDecoration: "line-through"}}><b>{price} DH</b></p>
            <p style={{fontSize:"10px", color:"green"}}><b>{(Math.round((price * remise)* 100) / 100).toFixed(2)}DH</b></p>
          </div>
        </div>
      </ListItemButton>
    </ListItem>
  );
}



function FileUploader(){
  const {totalPrice} = useContext(MyContext)
  const position = [51.505, -0.09]
  const {cposition, setCposition} = useContext(MyContext)
   return (
    <>
    <img src={Logo} style={{width:"235px"}}/>
      <div style={{display: "flex",flexDirection:"row", rowGap:"10px"}}>
        <div style ={{padding: "10px",display:"flex", flexDirection:"column",width:"235px", height:"400px"}}>
                <div style={{display:"flex", flexDirection:"row"}}>
                <div style={{flex:1}}>
                  <p className="recommander_btn" >Best Prices</p>
                </div>
                  <div className="recommander_btn" onClick={()=>{}} style={{flex:1}}>
                    <p>Closed</p>
                  </div>
                </div>
                <div style={{width:"255px", height: "250px"}}>
                  {
                    pharmacies.map((pha, index)=>{
                      return (
                        <RenderRow name={pha.name} price ={totalPrice} remise ={pha.remise} position={pha.position}/>
                      )
                    })
                  }
                </div>
              </div>
    <div style={{width:"400", height:"400"}}>
      <MapContainer style={{width:"400", height:"400"}}  center={position} zoom={13} scrollWheelZoom={false}>
            <TileLayer
              attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
              url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            />
             <PharmacieMarker latlong={pharmacies[0].position}/>
            {
              pharmacies.map((pha)=>{
                return (
                  <Marker
                    position={pha.position}
                    //draggable
                    icon={iconPharmacie}
                    //ondragend={handleDragEnd}
                  >
                  </Marker>
                )
              })
            }

            <LocationMarker/>
            {cposition?(<GoCPosition/>):(<></>)}
          </MapContainer>
      </div>
    </div>
    </>
  )
}
function GoCPosition(){
            const {cposition, setCposition} = useContext(MyContext)
            const map = useMap();
            map.flyTo(cposition, map.getZoom(10));
}

const iconPharmacie = new L.Icon({
    iconUrl: LocalPharmacyIcon,
    iconAnchor: null,
    popupAnchor: null,
    shadowUrl: null,
    shadowSize: null,
    shadowAnchor: null,
    iconSize: new L.Point(5, 5),
});

function PharmacieMarker({latlong}){
   const [position, setPosition] = useState(null);
   const [cposition, setCposition] = useState(null);
   const [bbox, setBbox] = useState([]);
  /*
  const map = useMap()
    useEffect(() => {
    console.log(map)
    const circle = L.circle(latlong, 10);
    circle.addTo(map);
    setBbox(['-10.000010221868283', '28.49999101684723', '-9.999989778131717', '28.50000898315277']);
    },[map])
    */
}
 function LocationMarker() {
   const [position, setPosition] = useState(my_pos);
    const [bbox, setBbox] = useState([]);
    const map = useMap();

   /*
    useEffect(() => {
      map.locate().on("locationfound", function (e) {
        setPosition(e.latlng);
        map.flyTo(e.latlng, map.getZoom());
        console.log(e.latlng)
        const radius = e.accuracy;
        const circle = L.circle(e.latlng, radius);
        circle.addTo(map);
        console.log(e.bounds.toBBoxString().split(","))
        setBbox(e.bounds.toBBoxString().split(","));
      });
    }, [map]);
    */
    /*return (
      <Marker position={position} >
        <Popup>
          You are here. <br />
          Map bbox: <br />
          <b>Southwest lng</b>: {bbox[0]} <br />
          <b>Southwest lat</b>: {bbox[1]} <br />
          <b>Northeast lng</b>: {bbox[2]} <br />
          <b>Northeast lat</b>: {bbox[3]}
        </Popup>
      </Marker>
    );*/
   console.log(position,"SS")
    map.flyTo(position,50);
    return (
      <Marker position={position} >
      </Marker>
    );
   return (<></>)
  }
export default FileUploader;
