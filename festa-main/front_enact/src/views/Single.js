import React, { useEffect, useRef } from 'react';
import Steps from '@enact/sandstone/Steps';
import BodyText from '@enact/sandstone/BodyText';
import './css/Single.css'
import ReactPlayer from 'react-player';
import Webcam from 'react-webcam';
import {Panel, Header} from '@enact/sandstone/Panels';
import Button from '@enact/sandstone/Button';

const Single = () => {
  const videoRef = useRef(null);
  const videoId = 'tLP4k0JKI8Q'; // YouTube video ID
  const webcamRef = useRef(null);

  useEffect(() => {
    const videoElement = videoRef.current;

    // 비디오 소스 설정
    const videoSource = null; // 비디오 소스 설정
    if (videoSource) {
      videoElement.src = videoSource;
    } else {
      window.navigator.mediaDevices.getUserMedia({ video: true })
        .then((stream) => {
          videoElement.srcObject = stream;

          // 비디오 프레임 처리 및 렌더링
          const processFrame = () => {
            // 프레임 전처리 및 이미지 처리 로직

            // 화면에 프레임 렌더링
            requestAnimationFrame(processFrame);
          };

          const requestAnimationFrame =
            window.requestAnimationFrame ||
            window.webkitRequestAnimationFrame ||
            window.mozRequestAnimationFrame ||
            window.msRequestAnimationFrame;

          videoElement.addEventListener('loadeddata', () => {
            processFrame();
          });
        })
        .catch((error) => {
          console.log('Failed to access webcam:', error);
        });
    }

    return () => {
      videoElement.srcObject = null;
    };
  }, []);

  return (
    <div>
    <Header title = "Play exercise" centered />
    <h3> Single Mode: JooHyeong </h3>
    <div className="main-single-container">  
      <div className="single-temp-box single-box-one">
        <div>
          
          <ReactPlayer url={`https://www.youtube.com/watch?v=${videoId}`} playing muted controls={false} />
          </div>
      </div>
     
      <div className="single-temp-box single-box-two"> 
        <Steps total={6} current={3}/>      
        <BodyText centered>count : 3 / 15</BodyText>     
        <BodyText centered> 1 : 53 sec </BodyText>     

      </div>
      <div className="single-temp-box single-box-three">
          <p>here is the webcam</p>
          <video ref={videoRef} autoPlay playsInline />
      </div>
    </div>
    <Button id="myButton" 
                className = 'single-button'
								backgroundOpacity="transparent"
                size="small"
								icon="closex"
								>
									Finish !
							</Button>
  </div>
);
};

export default Single;
 