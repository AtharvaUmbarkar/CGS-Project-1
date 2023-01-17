import React from 'react'

import './App.css'

const CaptchaGrid = () => {

  const rand = (min, max) => {
    return Math.floor(Math.random() * (max - min + 1) + min)
  }

  const currCell = rand(0, 8)
  const cells = [...Array(9).keys()]
  // console.log(cells);

  return (
    <ul className='h-full w-full grid grid-cols-3 grid-rows-3 gap-x-1 gap-y-1 bg-sky-600'>
      {cells.map((cell) => {
        return (
          <li key={cell} className=' bg-primary grid place-content-center'>
            {(cell === currCell) &&
              <div className="g-recaptcha h-1/2" data-sitekey="6LdumQYkAAAAAMpuve5V58awLSqCnQQ6NgQ-7ne1"></div>
            }
          </li>
        )
      })}
    </ul>
  )
}



function App() {
  return (
    <div className="App">

      <CaptchaGrid />
    </div>
  );
}

export default App;
