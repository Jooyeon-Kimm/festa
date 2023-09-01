import React, { useState } from 'react';
import Calendar from 'react-calendar';
import 'react-calendar/dist/Calendar.css';
import './css/MyPage.css';
import Button from '@enact/sandstone/Button';
import Pentagon from './Pentagon.js';
import { ToastContainer, toast } from 'react-toastify';
import { useNavigate } from 'react-router-dom';


const MyPage = () => {
  const [selectedDate, setSelectedDate] = useState(new Date());
  const navigate = useNavigate();

  const redirectToMainPanel = () => {
    navigate('/');
  };

  const handleDateSelection = (date) => {
    setSelectedDate(date);

    //new Notification('Selected date: ${date.toDateString()}');
  };
  
  const handleDateChange = (date) => {
    console.log('Selected Date:', date);
  };

  return (
    <div className='mypage-main-container'>
      <div className='mypage-box1'>
      <Button id="myButton" 
          backgroundOpacity="transparent"
          size="small"
          icon="playcircle">
          Play Exercise !
        </Button>
        </div>
      <div className='mypage-container'>
        <h1>My Page: _</h1>
        
        <h2>Calendar</h2>
        <div>
        <Calendar className='calendar-container'
          onChange={handleDateSelection} 
          value={selectedDate}
          tileClassName="custom-calendar-tile"
        />
        </div>
      </div>
      <div className='mypage-box2'>
        <Button id="myButton" 
          backgroundOpacity="transparent"
          size="small"
          icon="closex"
          onClick={redirectToMainPanel}
          >
          EXIT !
        </Button>
      </div>
      
    </div>
    
  );
};

export default MyPage;
