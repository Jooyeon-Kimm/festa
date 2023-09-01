import React, { useRef } from 'react';
import ReactPlayer from 'react-player';
import Webcam from 'react-webcam';

const VideoPlayer = () => {
  const videoId = 'tLP4k0JKI8Q'; // YouTube video ID
  const webcamRef = useRef(null);

  return (
    <div>
      <h1>Multi Mode</h1>
      <div style={{ display: 'flex' }}>
        <div style={{ flex: 1 }}>
          <ReactPlayer url={`https://www.youtube.com/watch?v=${videoId}`} playing muted controls={false} />
        </div>
        <div style={{ flex: 1 }}>
          <Webcam audio={false} ref={webcamRef} />
        </div>
      </div>
    </div>
  );
};

export default VideoPlayer;
