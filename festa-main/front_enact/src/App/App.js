import React, { Component } from 'react';
import kind from '@enact/core/kind';
import css from './App.module.less';
import ThemeDecorator from '@enact/sandstone/ThemeDecorator';
import Panels from '@enact/sandstone/Panels';
import { BrowserRouter, Routes, Route} from 'react-router-dom';
import SelectMode from './../views/SelectMode';
import AddProfile from '../views/AddProfile'
import MainPanel from '../views/MainPanel';
import Multi from '../views/Multi';
import Single from '../views/Single';
import MyPage from '../views/MyPage';
import SelectExercise from '../views/SelectExercise'
import SetCountPage from '../views/SetCountPage'
import WorkoutDone from '../views/WorkoutDone';
import Profile from '../views/Profile';

const App = kind({
	name: 'App',

	styles: {
		css,
		className: 'app'
	},

	render: (props) => (
	/*	<Panels {...props}>
			<MainPanel />
		</Panels>*/
		<BrowserRouter>
		<Routes>
		  <Route path="/" element={<Panels {...props}><MainPanel /></Panels>}></Route>
		  <Route path="/selectmode" element={<Panels {...props}><SelectMode /></Panels>}></Route>
		  <Route path="/mainpanel" element={<Panels {...props}><MainPanel /></Panels>}></Route>
		  <Route path="/addprofile" element={<Panels {...props}><AddProfile /></Panels>}></Route>
		  <Route path="/multi" element={<Panels {...props}><Multi /></Panels>}></Route>
		  <Route path="/single" element={<Panels {...props}><Single /></Panels>}></Route>
		  <Route path="/mypage" element={<Panels {...props}><MyPage /></Panels>}></Route>
		  <Route path="/selectexercise" element={<Panels {...props}><SelectExercise /></Panels>}></Route>
		  <Route path="/setcountpage" element={<Panels {...props}><SetCountPage /></Panels>}></Route>
		  <Route path="/workoutdone" element={<Panels {...props}><WorkoutDone /></Panels>}></Route>
		  <Route path="/profile" element={<Panels {...props}><Profile /></Panels>}></Route>


		  {/* 엘리먼트의 상단에 위치하는 라우트들의 규칙을 모두 확인하고, 일치하는 라우트가 없다면 이 라우트가 화면에 나타나게 됩니다. */}
	 
		</Routes>
	</BrowserRouter>
	)
});

export default ThemeDecorator(App);
