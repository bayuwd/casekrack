import React, { useState, useEffect } from 'react';
import { Routes, Route, NavLink, useParams, Link } from 'react-router-dom';
import './index.css';
import PromptModal from './components/PromptModal';

const CATEGORIES = [
  { name: 'General', slug: '' },
  { name: 'Logo & Branding', slug: 'logo-branding' },
  { name: 'Packaging', slug: 'packaging-design' },
  { name: 'UI/UX', slug: 'ui-ux-design' },
  { name: 'Motion', slug: 'motion-design' },
  { name: 'Clothing', slug: 'clothing-design' },
  { name: 'Illustration', slug: 'illustration' },
  { name: 'Editorial', slug: 'editorial-design' },
  { name: 'Poster', slug: 'poster-design' },
];

function CategoryView({ openModal, setAutoDownload }) {
  const { categorySlug } = useParams();
  const [briefs, setBriefs] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    setLoading(true);
    const fetchPath = categorySlug ? `/data/${categorySlug}.json` : '/data/general.json';
    
    fetch(fetchPath)
      .then(res => res.json())
      .then(data => {
        setBriefs(data);
        setLoading(false);
      })
      .catch(err => {
        console.error("Error fetching briefs:", err);
        setBriefs([]);
        setLoading(false);
      });
  }, [categorySlug]);

  const displayedBriefs = briefs.slice(0, 30);
  const secretBriefs = briefs.slice(30);

  const handleGenerateRandom = () => {
    let pool = secretBriefs.length > 0 ? secretBriefs : briefs;
    if (pool.length === 0) return;
    const randomBrief = pool[Math.floor(Math.random() * pool.length)];
    setAutoDownload(true);
    openModal(randomBrief);
  };

  if (loading) {
    return (
      <div style={{ padding: '120px 24px', textAlign: 'center', color: 'var(--primary)' }}>
        <h2 style={{ fontSize: '2rem', fontFamily: 'Playfair Display, serif', fontStyle: 'italic' }}>Loading Briefs...</h2>
      </div>
    );
  }

  return (
    <>
      <div className="calendar-grid">
        {displayedBriefs.map((brief, index) => {
          const tags = brief.deliverables ? brief.deliverables.split(',').slice(0, 3).map(tag => tag.trim()) : [];
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
        <p style={{ fontSize: '1.2rem', marginBottom: '32px', opacity: 0.8, maxWidth: '600px', margin: '0 auto 32px' }}>
          Generate a randomized {categorySlug ? CATEGORIES.find(c => c.slug === categorySlug)?.name : 'General'} brief instantly.
        </p>
        <button 
          onClick={handleGenerateRandom} 
          style={{ background: 'var(--primary)', color: 'white', padding: '16px 40px', fontSize: '1.2rem', fontWeight: 'bold', border: 'none', cursor: 'pointer', transition: 'transform 0.2s, box-shadow 0.2s', boxShadow: '8px 8px 0 var(--text-primary)' }}
          onMouseEnter={(e) => { e.target.style.transform = 'translateY(-4px)'; e.target.style.boxShadow = '12px 12px 0 var(--text-primary)'; }}
          onMouseLeave={(e) => { e.target.style.transform = 'none'; e.target.style.boxShadow = '8px 8px 0 var(--text-primary)'; }}
        >
          Generate & Download PDF
        </button>
      </div>
    </>
  );
}

function App() {
  const [selectedBrief, setSelectedBrief] = useState(null);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [autoDownload, setAutoDownload] = useState(false);

  const openModal = (brief) => {
    setSelectedBrief(brief);
    setIsModalOpen(true);
    if (!autoDownload) setAutoDownload(false);
  };

  const closeModal = () => {
    setSelectedBrief(null);
    setIsModalOpen(false);
    setAutoDownload(false);
  };

  return (
    <div className="container">
      <div className="header-bar" style={{ padding: '24px', background: 'var(--bg-color)', borderBottom: '2px solid var(--text-primary)', display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
        <Link to="/" style={{ textDecoration: 'none' }}>
          <h1 className="casekrack-logo" style={{ marginBottom: '24px' }}>CaseKrack</h1>
        </Link>
        
        {/* Category Navigation */}
        <nav className="category-nav">
          {CATEGORIES.map(cat => (
            <NavLink 
              key={cat.slug} 
              to={cat.slug ? `/category/${cat.slug}` : '/'}
              end={cat.slug === ''}
              className={({ isActive }) => `category-link ${isActive ? 'active' : ''}`}
            >
              {cat.name}
            </NavLink>
          ))}
        </nav>
      </div>
      
      <Routes>
        <Route path="/" element={<CategoryView openModal={openModal} setAutoDownload={setAutoDownload} />} />
        <Route path="/category/:categorySlug" element={<CategoryView openModal={openModal} setAutoDownload={setAutoDownload} />} />
      </Routes>

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
