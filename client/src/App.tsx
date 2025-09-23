import './App.css';
import Header from './components/Header/Header'
import Footer from './components/Footer/Footer';
import About from './components/About/About';
import { Route, Routes } from 'react-router-dom';
import Faq from './components/Faq/Faq';
import { useState } from 'react';
import Modal from './components/Modal/Modal';
import cn from 'classnames';

function App() {
  const [isModalActive, changeModalActive] = useState<boolean>(false)

  return (
    <div className="App">
      <Modal changeModalActive={changeModalActive} isActive={isModalActive} />
      <div className={cn('flex-wrapper', {'modal-active': isModalActive})}>
        <Header isActive={isModalActive} changeIsActive={changeModalActive} />
        <main className='main'>
          <Routes>
            <Route path="/" element={<About />} />
            <Route path='/faq' element={<Faq />} />
          </Routes>
        </main>
        <Footer />
      </div>
    </div>
  );
}

export default App;
