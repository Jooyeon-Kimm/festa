import kind from '@enact/core/kind';
import {Panel, Header} from '@enact/sandstone/Panels';
import Button from '@enact/sandstone/Button';
import './css/MainPanel.css'
import Image from '@enact/sandstone/Image';
import abc from './../../image/picture1.jpeg'
import React, {Component} from 'react';
import { Link } from 'react-router-dom';

function closeWindow() {
	window.close();
  }

const MainPanel = kind({
	name: 'MainPanel',
	render: (props) => (
		
		<Panel {...props}>
				<div className="main-container">
					<div
							style={{
       							backgroundImage: "url('./../../image/picture1.jpeg')",
       							backgroundSize: 'cover',
								backgroundPosition: 'center',
        						width: '100%',
        						height: '600px'
      							}}>
						<Header title="Exercise Assistance" className='header-name' centered/>
					</div>
					<div>
						<div className='box-main'> 
							<Link to="/selectexercise/">
							<Button
								backgroundOpacity="transparent"
								icon="play"
								className='box-one'>
								START !
							</Button>
							</Link>
							<Button id="myButton" 
								onClick = "closeWindow()"
								backgroundOpacity="transparent"
								size="small"
								icon="closex"
								className='box-two'>
									EXIT !
							</Button>
						</div>
					</div>
				</div>
		</Panel>

		
	)
});

export default MainPanel;


