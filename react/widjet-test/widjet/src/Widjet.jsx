import React, { useState } from "react";
import { DndProvider, useDrag, useDrop } from "react-dnd";
import { HTML5Backend } from "react-dnd-html5-backend";

// 1:1, 1:2, 2:1, 2:2 비율 크기 설정
const sizeOptions = [
  { label: "1:1", width: 1, height: 1 },
  { label: "1:2", width: 1, height: 2 },
  { label: "2:1", width: 2, height: 1 },
  { label: "2:2", width: 2, height: 2 },
];

// 위젯 컴포넌트
const Widget = ({ id, type, size, moveWidget, setSize }) => {
  const [, drag] = useDrag({
    type: "WIDGET",
    item: { id, type, size },
  });

  const handleSizeChange = (newSize) => {
    setSize(id, newSize);
  };

  const widgetStyle = {
    width: `${size.width * 100}px`,
    height: `${size.height * 100}px`,
    border: "1px solid black",
    margin: "10px",
    padding: "10px",
    cursor: "move",
  };

  return (
    <div ref={drag} style={widgetStyle}>
      <h4>{type}</h4>
      <div>
        {sizeOptions.map((option) => (
          <button key={option.label} onClick={() => handleSizeChange(option)}>
            {option.label}
          </button>
        ))}
      </div>
    </div>
  );
};

// 드롭 가능한 영역
const WidgetContainer = ({ widgets, moveWidget, setSize }) => {
  const [, drop] = useDrop({
    accept: "WIDGET",
    drop: (item) => moveWidget(item.id),
  });

  return (
    <div ref={drop} className="widget-container" style={containerStyle}>
      {widgets.map((widget) => (
        <Widget
          key={widget.id}
          id={widget.id}
          type={widget.type}
          size={widget.size}
          moveWidget={moveWidget}
          setSize={setSize}
        />
      ))}
    </div>
  );
};

// 앱 컴포넌트
const App = () => {
  const [widgets, setWidgets] = useState([
    { id: 1, type: "Widget A", size: { width: 1, height: 1 }, x: 0, y: 0 },
    { id: 2, type: "Widget B", size: { width: 1, height: 1 }, x: 1, y: 0 },
  ]);

  const moveWidget = (id) => {
    // 위치 이동 (현재는 순서를 변경하는 방식)
    setWidgets((prevWidgets) => {
      const widgetIndex = prevWidgets.findIndex((widget) => widget.id === id);
      const widget = prevWidgets[widgetIndex];
      const newWidgets = [...prevWidgets];
      newWidgets.splice(widgetIndex, 1); // 기존 위치에서 제거
      newWidgets.push(widget); // 끝으로 이동
      return newWidgets;
    });
  };

  const setSize = (id, newSize) => {
    setWidgets((prevWidgets) =>
      prevWidgets.map((widget) =>
        widget.id === id ? { ...widget, size: newSize } : widget
      )
    );
  };

  return (
    <DndProvider backend={HTML5Backend}>
      <div>
        <h1>위젯 배치 및 크기 조정</h1>
        <WidgetContainer
          widgets={widgets}
          moveWidget={moveWidget}
          setSize={setSize}
        />
      </div>
    </DndProvider>
  );
};

// 스타일 정의 (간단한 그리드 스타일)
const containerStyle = {
  display: "grid",
  gridTemplateColumns: "repeat(4, 1fr)", // 4개의 열
  gridGap: "10px",
  padding: "20px",
  width: "100%",
};

export default App;
