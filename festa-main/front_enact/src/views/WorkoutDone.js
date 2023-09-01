import Button from '@enact/sandstone/Button';
import kind from '@enact/core/kind';
import {Panel, Header} from '@enact/sandstone/Panels';
import {InputField} from '@enact/sandstone/Input';
import './css/WorkoutDone.css'

const WorkoutDone = kind({
	name: 'WorkoutDone',

	render: (props) => (
		<Panel {...props}>
            
                <Header title="Oh Woon Wan!" centered />
                <div className='main-container-workoutdone'>
                <div className='workoutdone-box1'>Exercise time :
                <InputField defaultValue='16:03'></InputField>
                </div>
                <br></br>
                <div className='workoutdone-box2'>Sets :
                <InputField defaultValue='5'></InputField>
                </div>
                <br></br>
                <div className='workoutdone-box3'>Counts :
                <InputField defaultValue='150'></InputField>
                </div>
                <br></br>
                <div className='workoutdone-box4'>Feedback :
                <InputField defaultValue='great'></InputField>
                </div>
                <br></br>
                <Button className='workoutdone-button'
                            backgroundOpacity="transparent"
                            size="small"
                            icon="home">
                                MY PAGE !
                            </Button>
                            
            </div>

		</Panel>
	)
});

export default WorkoutDone;