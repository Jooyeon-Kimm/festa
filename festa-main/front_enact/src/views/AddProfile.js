import React from 'react';
import kind from '@enact/core/kind';
import { Panel, Header } from '@enact/sandstone/Panels';
import Image from '@enact/sandstone/Image';
import { Link } from 'react-router-dom'
import Button from '@enact/sandstone/Button';
import { InputBase, InputField, InputFieldBase } from '@enact/sandstone/Input';
import './css/AddProfile.css'


const AddProfile = kind({
	name: 'AddProfile',

	render: (props) => (
		<Panel {...props}>
			<Header title="Add your profile" centered/>
			<div className='main-container-addprofile'>
				<div>
					Name
					<InputField>
					</InputField>
				</div>
				<div>
					<br></br>
					<br></br>
						Height
					<InputField>
					</InputField>
					<br></br>
				</div>
					<br></br>
					<br></br>
				<div>
					Weight
					<InputField>
					</InputField>
					<br></br>
					<br></br>
					<br></br>
				</div>
				<div className='box1-addprofile'>
					<p>Target weight</p>
					<InputField>

					</InputField>
				</div>

				<Link to="/mypage/">
					<Button 
						backgroundOpacity="transparent"
						size="small"
						icon="home">
						MY PAGE !
					</Button>
				</Link>
			</div>





		</Panel>
	)

});

export default AddProfile;