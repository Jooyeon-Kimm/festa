import React from 'react';
import kind from '@enact/core/kind';
import { Panel, Header } from '@enact/sandstone/Panels';
import Image from '@enact/sandstone/Image';
import Button from '@enact/sandstone/Button';
import './css/Profile.css'
import IconItem from '@enact/sandstone/IconItem';
import { useState } from 'react';
import { useCallback } from 'react';
import { Routable,Route,Link } from '@enact/ui/Routable';
import selectMode from './SelectMode'
import AddProfile from './AddProfile';

const Views = Routable({navigate: 'onNavigate'}, ({children}) => <div>{children}</div>);


const Sample = (props) => {
    // use 'main' for the default path
    const [path, nav] = useState('main');
    // if onNavigate is called with a new path, update the state
    const handleNavigate = useCallback((ev) => nav(ev.path), [nav]);
  
    return (
        <Views {...props} path={path} onNavigate={handleNavigate}>
          <Route path="main" component={Profiles}/>
          <Route path="selectMode" component={selectMode} />
          <Route path="addProfile" component={AddProfile} />
        </Views>
    );
  };


const Profiles = (props) => {
    const [path, nav] = useState('main');
	// if onNavigate is called with a new path, update the state
	const handleNavigate = useCallback((ev) => nav(ev.path), [nav]);
    return (
<Panel {...props}>
         <Header title="Profiles" centered/>
         <div className='main-container-profile'>    
         <div>
            <Image src="https://dummyimage.com/400x200/54d7d9/fff.png&text=SW" style={{ height: 200, width: 260 }} />
            <Image src="https://dummyimage.com/400x200/deba71/fff.png&text=JH" style={{ height: 200, width: 260 }} />
            <Image src="https://dummyimage.com/400x200/84f565/fff.png&text=JY" style={{ height: 200, width: 260 }} />
            <Image src="https://dummyimage.com/400x200/808275/fff.png&text=	₊" style={{ height: 200, width: 260 }} />
         </div>

         <div>
            {/* <Link to="/selectmode/"> */}
               <Button
                  backgroundOpacity="transparent">
                  _
               </Button>
            {/* </Link> */}

            {/* <Link to="/selectmode/"> */}
            <Link path="/selectMode">
               <Button
                  backgroundOpacity="transparent">
                  _
               </Button>
               </Link>
            {/* </Link> */}

            {/* <Link to="/selectmode/"> */}
               <Button
                  backgroundOpacity="transparent">
                  _
               </Button>
            {/* </Link> */}


            <Link path="/addProfile">
            {/* <Link to="/addprofile/"> */}
               <Button
                  backgroundOpacity="transparent">
                  Add
               </Button>
               </Link>
            {/* </Link> */}
         </div>
         </div>
      </Panel>
    );
}


const profiles = kind({
   name: 'Profile',

   render: (props) => (
      <Panel {...props}>
         <Header title="Profile" centered/>


         <div>
            <Image src="https://dummyimage.com/400x200/54d7d9/fff.png&text=SW" style={{ height: 200, width: 260 }} />
            <Image src="https://dummyimage.com/400x200/deba71/fff.png&text=JH" style={{ height: 200, width: 260 }} />
            <Image src="https://dummyimage.com/400x200/84f565/fff.png&text=JY" style={{ height: 200, width: 260 }} />
            <Image src="https://dummyimage.com/400x200/808275/fff.png&text=†" style={{ height: 200, width: 260 }} />
         </div>

         <div>
            {/* <Link to="/selectmode/"> */}
               <Button
                  backgroundOpacity="transparent">
                  _
               </Button>
            {/* </Link> */}

            {/* <Link to="/selectmode/"> */}
               <Button
                  backgroundOpacity="transparent">
                  _
               </Button>
            {/* </Link> */}

            {/* <Link to="/selectmode/"> */}
               <Button
                  backgroundOpacity="transparent">
                  _
               </Button>
            {/* </Link> */}


            {/* <Link to="/addprofile/"> */}
               <Button
                  backgroundOpacity="transparent">
                  Add
               </Button>
            {/* </Link> */}
         </div>

      </Panel>
   )

});

export default Sample;
