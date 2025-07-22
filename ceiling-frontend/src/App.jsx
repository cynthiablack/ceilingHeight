import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <header>
      <h1>Ceiling Height Prediction Tool</h1>
      <p>Please choose a date to display a prediction for Ted Stevens Anchorage International Airport (PANC)</p>
      </header>
      <main>
      {/* interactive inputs */}
        <section>
          {/* TODO: date picker here */}
        </section>
        {/* visualizations */}
        <section>
          {/* TODO: graphs from PyMC here */}
        </section>
      </main>
      <footer>
        <p>Bayesian regression learning model created by Cynthia Black using PyMC &copy; 2025</p>
      </footer>
    </>
  )
}

export default App
