import React from 'react';

const Pentagon = () => {
  const sideLengths = [800, 400, 1200, 900, 1100]; // 오각형의 다섯 변의 길이
  const ratio = 0.75; // 찌그러짐 정도를 조절하는 비율

  const centerX = sideLengths.reduce((sum, sideLength) => sum + sideLength, 0) / 10; // 오각형의 중심 X 좌표
  const centerY = sideLengths.reduce((sum, sideLength) => sum + sideLength, 0) / 10; // 오각형의 중심 Y 좌표

  // 찌그러진 오각형의 각 꼭짓점 좌표 계산
  const points = sideLengths.map((sideLength, index) => {
    const angle = (index * (2 * Math.PI)) / 5 + Math.PI / 10; // 오각형의 각도 (10도 회전)
    const x = centerX + (sideLength * ratio * Math.cos(angle)) / 2; // X 좌표 계산
    const y = centerY - (sideLength * ratio * Math.sin(angle)) / 2; // Y 좌표 계산 (음수로 변환하여 뒤집음)
    return { x, y }; // 좌표를 객체로 반환
  });

  const exerciseNames = ["pull up", "push up", "squat", "walk", "situp"]; // 각 꼭짓점에 표시할 운동 이름

  return (
    <svg width={sideLengths.reduce((max, sideLength) => Math.max(max, sideLength), 2000)}
     height={sideLengths.reduce((max, sideLength) => Math.max(max, sideLength), 1500)} 
     
     viewBox={`0 0 ${sideLengths.reduce((sum, sideLength) => sum + sideLength, 0)} ${sideLengths.reduce((sum, sideLength) => sum + sideLength, 0)}`}>
      <polygon points={points.map(point => `${point.x},${point.y}`).join(' ')} fill="blue" />
      {points.map((point, index) => (
        <text key={index} x={point.x} y={point.y} textAnchor="middle" alignmentBaseline="central" fill="white" fontSize="80">
          {exerciseNames[index]}
        </text>
      ))}
    </svg>
  );
};

export default Pentagon;