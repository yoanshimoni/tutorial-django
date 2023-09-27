import React, { useState, useEffect } from 'react';

const ItemList = () => {
  const [items, setItems] = useState([]);

  useEffect(async () => {
    const items = await fetch('http://localhost:8001/api/items')
    setItems(items)
  }, []);

  return (
    <div>
      {items.map(item => (
        <div key={item.name}>
          <h3 style={{color: item.color}}>{item.name}</h3>
          <p style={{ color: item.color }}>{item.color}</p>
        </div>
      ))}
    </div>
  );
}

export default ItemList;
