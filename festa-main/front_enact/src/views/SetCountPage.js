import kind from '@enact/core/kind';
import {Panel, Header} from '@enact/sandstone/Panels';
import Dropdown from '@enact/sandstone/Dropdown';
import Button from '@enact/sandstone/Button';
import './css/SetCountPage.css'
import Input from '@enact/sandstone/Input';
import {InputField} from '@enact/sandstone/Input';
import { Link } from 'react-router-dom'


const MainPanel = kind({
	name: 'MainPanel',
	
	render: (props) => (
		<Panel {...props}>
				<Header title="Exercise Assistance" centered/>
				<div className="main-container3">				
					<div>
						<Dropdown
							className = "down"
							defaultSelected={0}
							inline
							title="Select the goal of set">
							{['3','4', '5', '6']}
						</Dropdown>

					</div>
						<div>
						<Input
							id='set_count'
							placeholder="count"
  							subtitle="count"
 							title="Goal of count"
							onClick="getValue_set_count"
							/>
						</div>
						<div>
						<Input
							placeholder="rest time"
  							subtitle="rest time"
 							title="rest time"
							/>
						</div>
					<Link to="/selectmode/">
						<Button
							backgroundOpacity="transparent"
							icon="forward">
								go!
						</Button>
					</Link>
				</div>
		</Panel>
		
	)

	
});

	



export default MainPanel;