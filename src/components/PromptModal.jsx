import React, { useEffect } from 'react';
import { X, Download, CheckCircle, Circle } from 'lucide-react';
import html2pdf from 'html2pdf.js';
import './PromptModal.css';

export default function PromptModal({ isOpen, onClose, brief, autoDownload }) {
  if (!isOpen || !brief) return null;

  const handleDownloadPDF = async () => {
    const element = document.getElementById('pdf-content');
    
    // Temporarily add class to condense spacing slightly and prevent awkward page breaks
    element.classList.add('pdf-export-mode');

    const opt = {
      margin:       10,
      filename:     `CaseKrack_Brief_${brief.id < 10 ? '0' + brief.id : brief.id}.pdf`,
      image:        { type: 'jpeg', quality: 0.98 },
      html2canvas:  { scale: 2 },
      jsPDF:        { unit: 'mm', format: 'a4', orientation: 'portrait' },
      pagebreak:    { mode: 'css' }
    };
    
    await html2pdf().set(opt).from(element).save();
    
    // Remove the class so the UI returns to normal
    element.classList.remove('pdf-export-mode');
  };

  useEffect(() => {
    if (autoDownload) {
      // Small timeout to allow DOM layout to render fully before taking the snapshot
      const timer = setTimeout(() => {
        handleDownloadPDF();
      }, 300);
      return () => clearTimeout(timer);
    }
  }, [autoDownload]);

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content" onClick={(e) => e.stopPropagation()}>
        <button className="modal-close" onClick={onClose}>
          <X size={24} />
        </button>
        
        <div className="modal-scroll-wrapper" style={{ flex: 1, overflowY: 'auto', padding: '20px', textAlign: 'left' }}>
          <div id="pdf-content" style={{ padding: '20px' }}>
            <div className="brief-header" style={{ marginBottom: '40px', borderBottom: '2px solid var(--text-primary)', paddingBottom: '24px' }}>
              {brief.title && (
                <div style={{ fontSize: '1.2rem', fontWeight: 'bold', textTransform: 'uppercase', letterSpacing: '1px', opacity: 0.7, marginBottom: '8px' }}>
                  Project: {brief.title} &nbsp; | &nbsp; {brief.client}
                </div>
              )}
              <h2 className="modal-title brand-heading">
                {brief.brandName || brief.client}
              </h2>
              {brief.tagline && (
                <h3 className="modal-tagline">
                  "{brief.tagline}"
                </h3>
              )}
            </div>
            
            <div className="prompt-result-container" style={{ overflowY: 'visible', margin: 0 }}>
              <div className="prompt-result">
                
                {/* The Twist - Hero Block */}
                <div className="prompt-section twist-box">
                  <div className="prompt-label twist-label">The Wildcard Twist</div>
                  <div className="prompt-value twist-value">{brief.theTwist}</div>
                </div>

                {/* Narrative Block */}
                <div className="prompt-section">
                  <div className="prompt-label">Background</div>
                  <div className="prompt-value description">{brief.background}</div>
                </div>
                
                <div className="prompt-section">
                  <div className="prompt-label">The Problem</div>
                  <div className="prompt-value description">{brief.problem}</div>
                </div>

                <div className="prompt-section">
                  <div className="prompt-label">Why Now?</div>
                  <div className="prompt-value description">{brief.whyNow || "N/A - Original Brief"}</div>
                </div>

                <div className="prompt-section">
                  <div className="prompt-label">Purpose</div>
                  <div className="prompt-value description">{brief.purpose}</div>
                </div>

                {/* Strategy & Metrics Subgrid */}
                <div className="prompt-subgrid metrics-grid" style={{ gridColumn: '1 / -1', display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '24px', background: '#0f172a', padding: '32px', color: 'white', marginBottom: '8px', border: 'none' }}>
                  <div className="prompt-section" style={{ marginBottom: 0 }}>
                    <div className="prompt-label" style={{ color: '#cbd5e1', borderBottomColor: '#cbd5e1' }}>KPIs & Metrics</div>
                    <div className="prompt-value" style={{ color: 'white' }}>{brief.kpis || "TBD"}</div>
                  </div>
                  <div className="prompt-section" style={{ marginBottom: 0 }}>
                    <div className="prompt-label" style={{ color: '#cbd5e1', borderBottomColor: '#cbd5e1' }}>Budget & Timeline</div>
                    <div className="prompt-value" style={{ color: 'white' }}>{brief.budgetTimeline || "TBD"}</div>
                  </div>
                  <div className="prompt-section" style={{ marginBottom: 0 }}>
                    <div className="prompt-label" style={{ color: '#cbd5e1', borderBottomColor: '#cbd5e1' }}>Brand Archetype</div>
                    <div className="prompt-value" style={{ color: 'white' }}>{brief.brandArchetype}</div>
                  </div>
                  <div className="prompt-section" style={{ marginBottom: 0 }}>
                    <div className="prompt-label" style={{ color: '#cbd5e1', borderBottomColor: '#cbd5e1' }}>Tone of Voice</div>
                    <div className="prompt-value" style={{ color: 'white' }}>{brief.toneOfVoice}</div>
                  </div>
                </div>

                {/* User Persona */}
                <div className="prompt-section" style={{ gridColumn: '1 / -1', padding: '24px', borderLeft: '6px solid var(--primary)', background: '#f8fafc', marginBottom: '8px' }}>
                  <div className="prompt-label">Primary User Persona</div>
                  <div className="prompt-value description" style={{ fontStyle: 'italic', fontSize: '1.4rem', fontWeight: '500' }}>"{brief.userPersona || brief.targetAudience}"</div>
                </div>

                {/* Features & Restrictions */}
                <div className="prompt-section">
                  <div className="prompt-label">Key UX/UI Features</div>
                  <div className="prompt-value description">{brief.keyFeatures || "Standard deliverables apply."}</div>
                </div>

                <div className="prompt-section restriction-box" style={{ gridColumn: 'auto', marginTop: 0, marginBottom: 0 }}>
                  <div className="prompt-label restriction-label">Mandatory Restrictions</div>
                  <div className="prompt-value restriction-value">{brief.mandatoryRestrictions}</div>
                </div>

                {/* Visual Direction Subgrid */}
                <div className="prompt-subgrid visual-grid" style={{ gridColumn: '1 / -1', display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '24px', borderTop: '4px solid var(--text-primary)', paddingTop: '24px', background: 'transparent', borderLeft: 'none', borderRight: 'none', borderBottom: 'none' }}>
                  <div className="prompt-section">
                    <div className="prompt-label">Palette</div>
                    <div className="prompt-value">{brief.palette}</div>
                  </div>
                  <div className="prompt-section">
                    <div className="prompt-label">Typography Direction</div>
                    <div className="prompt-value">{brief.typography || "TBD"}</div>
                  </div>
                  <div className="prompt-section">
                    <div className="prompt-label">Competitors</div>
                    <div className="prompt-value">{brief.competitors}</div>
                  </div>
                  <div className="prompt-section">
                    <div className="prompt-label">References</div>
                    <div className="prompt-value">{brief.references}</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        {/* Action Buttons (Excluded from PDF) */}
        <div className="modal-actions" style={{ display: 'flex', flexWrap: 'wrap', gap: '16px', marginTop: '16px', paddingTop: '24px', borderTop: '2px solid var(--text-primary)', justifyContent: 'space-between' }}>
          <button 
            className="action-btn"
            onClick={handleDownloadPDF}
            style={{ display: 'flex', alignItems: 'center', gap: '8px', padding: '12px 24px', background: 'var(--primary)', color: 'white', border: 'none', fontWeight: 'bold', cursor: 'pointer', transition: 'all 0.2s', flex: 1, justifyContent: 'center' }}
          >
            <Download size={20} />
            Download PDF
          </button>
        </div>

      </div>
    </div>
  );
}
