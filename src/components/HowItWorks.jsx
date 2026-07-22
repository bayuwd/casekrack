import React from 'react';
import { Layout, Link, Calendar } from 'lucide-react';

export default function HowItWorks() {
  const steps = [
    {
      icon: <Layout size={32} />,
      title: 'Generate Cases',
      desc: 'Receive AI-crafted, unique design prompts daily that challenge your creativity and problem-solving skills.'
    },
    {
      icon: <Link size={32} />,
      title: 'Create & Link',
      desc: 'Design your solution, post it online, and submit the link to your case file to keep your progress documented.'
    },
    {
      icon: <Calendar size={32} />,
      title: 'Track Progress',
      desc: 'Monitor your 30-day streak, review past designs, and watch your portfolio grow into a masterpiece.'
    }
  ];

  return (
    <section className="how-it-works section container">
      <h2 className="section-title">How It <span className="gradient-text">Works</span></h2>
      <div className="steps-grid">
        {steps.map((step, idx) => (
          <div key={idx} className="step-card physical-shadow">
            <div className="step-icon">
              {step.icon}
            </div>
            <h3 className="step-title">{step.title}</h3>
            <p className="step-desc">{step.desc}</p>
          </div>
        ))}
      </div>
    </section>
  );
}
