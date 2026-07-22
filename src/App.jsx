import React, { useState, useEffect } from 'react';
import './index.css';
import { briefs } from './data/briefs';
import PromptModal from './components/PromptModal';

function App() {
  const [selectedBrief, setSelectedBrief] = useState(null);
  const [isModalOpen, setIsModalOpen] = useState(false);

  const [autoDownload, setAutoDownload] = useState(false);

  const openModal = (brief) => {
    setSelectedBrief(brief);
    setIsModalOpen(true);
    setAutoDownload(false);
  };

  const closeModal = () => {
    setSelectedBrief(null);
    setIsModalOpen(false);
    setAutoDownload(false);
  };

  const handleGenerateRandom = () => {
    // Select randomly from the secret 50 cases (index 30 onwards)
    let randomBrief;
    if (briefs.length > 30) {
      const secretCases = briefs.slice(30);
      randomBrief = secretCases[Math.floor(Math.random() * secretCases.length)];
    } else {
      // Fallback if data hasn't merged yet
      randomBrief = briefs[Math.floor(Math.random() * briefs.length)];
    }

    setSelectedBrief(randomBrief);
    setIsModalOpen(true);
    setAutoDownload(true);
  };

  return (
    <div className="container">
      <div className="header-bar" style={{ padding: '24px', background: 'var(--bg-color)', borderBottom: '2px solid var(--text-primary)', textAlign: 'center' }}>
        <h1 className="casekrack-logo">CaseKrack</h1>
      </div>
      
      <div className="calendar-grid">
        {briefs.slice(0, 30).map((brief, index) => {
          const tags = brief.deliverables.split(',').slice(0, 3).map(tag => tag.trim());
          const isInverse = index % 2 !== 0;

          return (
            <div 
              key={brief.id} 
              className={`poster-card ${isInverse ? 'inverse' : ''}`}
              onClick={() => openModal(brief)}
            >
              <div className="poster-tag-container">
                {tags.map((tag, i) => (
                  <div key={i} className="poster-tag">{tag}</div>
                ))}
              </div>
              
              <div className="poster-bottom">
                <h3 className="poster-title">
                  {brief.title}
                </h3>
                <p className="poster-client">{brief.client}</p>
                <p style={{ marginTop: '16px', opacity: 0.6, fontSize: '0.8rem', fontWeight: 'bold' }}>
                  CASE NO. {brief.id < 10 ? `0${brief.id}` : brief.id}
                </p>
              </div>
            </div>
          );
        })}
      </div>

      {/* Endless Generator Block */}
      <div className="endless-generator-block" style={{ padding: '80px 24px', background: '#f8fafc', color: 'var(--text-primary)', textAlign: 'center', borderTop: '4px solid var(--text-primary)' }}>
        <h2 style={{ fontSize: '3rem', marginBottom: '16px', fontFamily: 'Inter, sans-serif', fontWeight: 800 }}>Need more practice?</h2>
        <p style={{ fontSize: '1.2rem', marginBottom: '32px', opacity: 0.8, maxWidth: '600px', margin: '0 auto 32px' }}>Generate an infinite amount of dynamic, randomized master briefs instantly.</p>
        <button 
          onClick={handleGenerateRandom} 
          style={{ background: 'var(--primary)', color: 'white', padding: '16px 40px', fontSize: '1.2rem', fontWeight: 'bold', border: 'none', cursor: 'pointer', transition: 'transform 0.2s, box-shadow 0.2s', boxShadow: '8px 8px 0 var(--text-primary)' }}
          onMouseEnter={(e) => { e.target.style.transform = 'translateY(-4px)'; e.target.style.boxShadow = '12px 12px 0 var(--text-primary)'; }}
          onMouseLeave={(e) => { e.target.style.transform = 'none'; e.target.style.boxShadow = '8px 8px 0 var(--text-primary)'; }}
        >
          Generate & Download PDF
        </button>
      </div>

      <footer className="footer-trademark" style={{ padding: '24px', textAlign: 'center', background: 'var(--primary)', color: 'white', borderTop: '4px solid var(--text-primary)' }}>
        <p style={{ fontWeight: 700, letterSpacing: '2px', textTransform: 'uppercase', fontSize: '0.85rem', margin: 0 }}>&copy; {new Date().getFullYear()} CaseKrack. All Rights Reserved.</p>
      </footer>

      {isModalOpen && (
        <PromptModal 
          isOpen={isModalOpen} 
          onClose={closeModal} 
          brief={selectedBrief} 
          autoDownload={autoDownload}
        />
      )}
    </div>
  );
}

export default App;
