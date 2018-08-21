import React, { Component } from 'react'
import Header from '../components/Header'
import Footer from '../components/Footer'
import CardContainer from './CardContainer'
import '../css/App.css'

class App extends Component {
  render () {
    return (
      <div className='wrapper'>
        <Header />
        <div className='content-wrapper'>
          <CardContainer />
        </div>
        <Footer />
      </div>
    )
  }
}

export default App
