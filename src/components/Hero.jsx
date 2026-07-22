import React from 'react';
import { Link } from 'react-router-dom';
import { ArrowRight } from 'lucide-react';
import dashboardImage from '../assets/dashboard.jpg';

export default function Hero() {
  return (
    <section className="hero section container">
      <div className="hero-content">
        <h1 className="hero-title">
          Master the <span className="gradient-text">30-Day Design Challenge</span>
        </h1>
        <p className="hero-subtitle">
          Elevate your design skills with daily prompts, expert feedback, and a vibrant community. Level up your portfolio in just one month.
        </p>
        <Link to="/dashboard" className="btn-primary" style={{ textDecoration: 'none', display: 'inline-flex', alignItems: 'center', gap: '8px' }}>
          Start Your Journey <ArrowRight size={20} />
        </Link>
      </div>
      <div className="hero-image-wrapper physical-shadow floating-element">
        {/* We use a placeholder div or img. The user said designer is generating dashboard.jpg */}
        <img src={dashboardImage} alt="Dashboard Preview" className="hero-image" />
      </div>
    </section>
  );
}
