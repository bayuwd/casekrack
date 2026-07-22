import React from 'react';
import { CheckCircle, Globe, ArrowRight } from 'lucide-react';

export default function Features() {
  const features = [
    {
      title: 'Expert Feedback',
      desc: 'Get actionable critique from industry veterans on your submitted cases.'
    },
    {
      title: 'Global Community',
      desc: 'Join thousands of designers from around the world participating in the challenge.'
    },
    {
      title: 'Portfolio Ready',
      desc: 'End the month with 30 diverse, high-quality pieces ready for your portfolio.'
    }
  ];

  return (
    <section className="features section container">
      <div className="features-grid">
        <div className="features-intro">
          <h2 className="section-title" style={{ marginBottom: '24px', textAlign: 'left' }}>
            Why Join <span className="gradient-text">CaseKrack?</span>
          </h2>
          <p className="hero-subtitle" style={{ marginLeft: 0, textAlign: 'left' }}>
            We provide everything you need to succeed, stay motivated, and improve your design skills consistently over 30 days.
          </p>
        </div>
        <div>
          {features.map((feature, idx) => (
            <div key={idx} className="feature-item physical-shadow" style={{ marginBottom: '16px' }}>
              <div className="icon">
                {idx === 1 ? <Globe size={28} /> : <CheckCircle size={28} />}
              </div>
              <div>
                <h3 className="step-title" style={{ marginBottom: '8px' }}>{feature.title}</h3>
                <p className="step-desc">{feature.desc}</p>
              </div>
            </div>
          ))}
        </div>
      </div>

      <div className="cta-section physical-shadow">
        <h2 className="section-title" style={{ marginBottom: '24px' }}>Ready for the Challenge?</h2>
        <p className="step-desc" style={{ marginBottom: '32px', fontSize: '1.25rem' }}>
          Commit to 30 days of growth. Start your first case today.
        </p>
        <button className="btn-primary">
          Begin Challenge <ArrowRight size={20} />
        </button>
      </div>
    </section>
  );
}
