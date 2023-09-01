import kind from '@enact/core/kind';
import {Panel, Header} from '@enact/sandstone/Panels';
import Button from '@enact/sandstone/Button';
import './css/SelectExercise.css'
import Image from '@enact/sandstone/Image';
import abc from './../../image/pull-up.jpeg'
import abc1 from './../../image/sit-up.jpeg'
import abc2 from './../../image/squat.jpeg'
import abc3 from './../../image/push-up.jpeg'
import abc4 from './../../image/plank.jpeg'
import { Link } from 'react-router-dom';



const MainPanel = kind({
	name: 'SelectExercise',
	
	render: (props) => (
		<Panel {...props}>
			<Header className='abvc' centered>
				Select Exercise!
			</Header>
			
				<div className = "main-container1">
					<div>
						<Image src="./../../image/plank.jpeg" style={{height: 170, width: 260}} />						
						<Button> Plank </Button>
					</div>
					<div>
						<Image src="./../../image/push-up.jpeg" style={{height: 170, width: 260}} />						
						<Link to = "/setcountpage/">
							<Button> Push-up </Button>
						</Link>
					</div>
					<div>
						<Image src="./../../image/pull-up.jpeg" style={{height: 170, width: 260}} />						
						<Button> Pull-up </Button>
					</div>
					<div>
						<Image src="./../../image/sit-up.jpeg" style={{height: 170, width: 260}} />						
						<Button > Sit-up </Button>
					</div>
					<div>
						<Image src="./../../image/squat.jpeg" style={{height: 170, width: 260}} />						
						<Button> Squat </Button>
					</div>
				</div>
	
		</Panel>
		
	)

	
});

	



export default MainPanel;