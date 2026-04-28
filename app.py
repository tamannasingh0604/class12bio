<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Sexual Reproduction in Flowering Plants | Class 12 Bio Ch.1</title>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=Outfit:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
:root {
  --emerald: #0d6e4a;
  --emerald-mid: #16a06a;
  --emerald-light: #d0f5e5;
  --emerald-glow: #1ecc87;
  --amber: #d97706;
  --amber-light: #fef3c7;
  --rose: #be123c;
  --rose-light: #ffe4ec;
  --sky: #0369a1;
  --sky-light: #e0f2fe;
  --violet: #6d28d9;
  --violet-light: #ede9fe;
  --orange: #c2410c;
  --orange-light: #ffedd5;
  --teal: #0f766e;
  --teal-light: #ccfbf1;
  --bg: #f0fdf4;
  --surface: #ffffff;
  --border: #d1fae5;
  --text: #0f1a0f;
  --muted: #4b6857;
  --card-shadow: 0 4px 24px rgba(13,110,74,0.10);
}

* { box-sizing: border-box; margin: 0; padding: 0; }

body {
  font-family: 'Outfit', sans-serif;
  background: var(--bg);
  color: var(--text);
  line-height: 1.7;
  overflow-x: hidden;
}

/* ─── HERO ─── */
.hero {
  background: linear-gradient(135deg, #064e2c 0%, #0d6e4a 40%, #0f9960 70%, #1ecc87 100%);
  color: #fff;
  padding: 4rem 2rem 5rem;
  text-align: center;
  position: relative;
  overflow: hidden;
}
.hero::before {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(ellipse at 30% 60%, rgba(30,204,135,0.18) 0%, transparent 60%),
              radial-gradient(ellipse at 80% 20%, rgba(255,255,255,0.07) 0%, transparent 50%);
}
.hero::after {
  content: '';
  position: absolute;
  bottom: -1px;
  left: 0;
  right: 0;
  height: 60px;
  background: var(--bg);
  clip-path: ellipse(55% 100% at 50% 100%);
}
.hero-tag {
  display: inline-block;
  background: rgba(255,255,255,0.15);
  border: 1px solid rgba(255,255,255,0.3);
  color: #b9ffd9;
  font-size: 0.7rem;
  font-weight: 700;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  padding: 5px 18px;
  border-radius: 30px;
  margin-bottom: 1.2rem;
  position: relative;
}
.hero h1 {
  font-family: 'Playfair Display', serif;
  font-size: clamp(2rem, 5vw, 3.5rem);
  font-weight: 700;
  line-height: 1.15;
  margin-bottom: 0.8rem;
  position: relative;
  text-shadow: 0 2px 20px rgba(0,0,0,0.2);
}
.hero p {
  color: rgba(255,255,255,0.8);
  font-size: 1rem;
  position: relative;
}
.hero-badges {
  display: flex;
  gap: 8px;
  justify-content: center;
  flex-wrap: wrap;
  margin-top: 1.8rem;
  position: relative;
}
.badge {
  background: rgba(255,255,255,0.13);
  border: 1px solid rgba(255,255,255,0.25);
  color: #fff;
  font-size: 0.75rem;
  font-weight: 600;
  padding: 5px 16px;
  border-radius: 20px;
  backdrop-filter: blur(4px);
}

/* ─── TOPIC NAV ─── */
.topic-nav {
  background: var(--surface);
  border-bottom: 2px solid var(--border);
  padding: 0;
  position: sticky;
  top: 0;
  z-index: 200;
  display: flex;
  overflow-x: auto;
  scrollbar-width: none;
  box-shadow: 0 2px 12px rgba(13,110,74,0.08);
}
.topic-nav::-webkit-scrollbar { display: none; }
.topic-btn {
  padding: 14px 20px;
  font-family: 'Outfit', sans-serif;
  font-size: 0.78rem;
  font-weight: 600;
  color: var(--muted);
  background: none;
  border: none;
  border-bottom: 3px solid transparent;
  cursor: pointer;
  white-space: nowrap;
  transition: all 0.2s;
  letter-spacing: 0.03em;
}
.topic-btn:hover { color: var(--emerald); background: var(--emerald-light); }
.topic-btn.active { color: var(--emerald); border-bottom-color: var(--emerald-glow); background: var(--emerald-light); }

/* ─── PAGES ─── */
.page {
  display: none;
  animation: fadeSlide 0.35s ease;
}
.page.active { display: block; }
@keyframes fadeSlide {
  from { opacity: 0; transform: translateY(16px); }
  to { opacity: 1; transform: translateY(0); }
}

/* ─── PAGE HEADER ─── */
.page-header {
  padding: 3rem 0 2rem;
  text-align: center;
  position: relative;
}
.page-num {
  display: inline-block;
  font-size: 0.68rem;
  font-weight: 800;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: var(--emerald-mid);
  background: var(--emerald-light);
  border: 1.5px solid var(--emerald-mid);
  padding: 4px 16px;
  border-radius: 20px;
  margin-bottom: 0.8rem;
}
.page-title {
  font-family: 'Playfair Display', serif;
  font-size: clamp(1.8rem, 4vw, 2.8rem);
  font-weight: 700;
  color: var(--emerald);
  line-height: 1.2;
}
.page-subtitle {
  color: var(--muted);
  font-size: 0.95rem;
  margin-top: 0.5rem;
}

/* ─── CONTAINER ─── */
.container {
  max-width: 1000px;
  margin: 0 auto;
  padding: 0 1.5rem 4rem;
}

/* ─── SECTION TITLE ─── */
.section-title {
  font-family: 'Playfair Display', serif;
  font-size: 1.4rem;
  font-weight: 700;
  color: var(--emerald);
  display: flex;
  align-items: center;
  gap: 10px;
  margin: 2rem 0 1rem;
}
.section-title::before {
  content: '';
  display: inline-block;
  width: 5px;
  height: 28px;
  background: linear-gradient(180deg, var(--emerald-glow), var(--emerald));
  border-radius: 3px;
  flex-shrink: 0;
}

/* ─── CARDS ─── */
.card {
  background: var(--surface);
  border: 1.5px solid var(--border);
  border-radius: 16px;
  padding: 1.5rem 1.8rem;
  margin-bottom: 1.2rem;
  box-shadow: var(--card-shadow);
}

/* ─── COLORED INFO BOXES ─── */
.info-box {
  border-radius: 14px;
  padding: 1.2rem 1.4rem;
  margin: 1rem 0;
  font-size: 0.92rem;
  border-left: 5px solid;
}
.info-box.green { background: var(--emerald-light); border-color: var(--emerald-mid); color: #0a3d22; }
.info-box.blue  { background: var(--sky-light); border-color: var(--sky); color: #0a2a45; }
.info-box.amber { background: var(--amber-light); border-color: var(--amber); color: #5a2d00; }
.info-box.violet{ background: var(--violet-light); border-color: var(--violet); color: #2d1260; }
.info-box.teal  { background: var(--teal-light); border-color: var(--teal); color: #053b36; }
.info-box.rose  { background: var(--rose-light); border-color: var(--rose); color: #5c0820; }
.info-box.orange{ background: var(--orange-light); border-color: var(--orange); color: #5c1a00; }
.info-box strong { display: block; margin-bottom: 6px; font-size: 0.88rem; letter-spacing: 0.04em; }

/* ─── BULB TRIVIA DROPDOWN ─── */
.bulb-trivia {
  margin: 1.2rem 0;
  border-radius: 14px;
  overflow: hidden;
  border: 2px solid #fbbf24;
  box-shadow: 0 2px 12px rgba(251,191,36,0.15);
}
.bulb-header {
  background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
  padding: 0.9rem 1.4rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 12px;
  user-select: none;
  transition: background 0.2s;
}
.bulb-header:hover { background: linear-gradient(135deg, #fde68a 0%, #fbbf24 100%); }
.bulb-icon {
  width: 36px;
  height: 36px;
  flex-shrink: 0;
  position: relative;
}
.bulb-icon svg { width: 100%; height: 100%; }
.bulb-label {
  font-size: 0.72rem;
  font-weight: 800;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: #92400e;
  flex: 1;
}
.bulb-label span {
  display: block;
  font-size: 0.85rem;
  font-weight: 600;
  letter-spacing: 0;
  text-transform: none;
  color: #78350f;
  margin-top: 1px;
}
.bulb-arrow {
  font-size: 1.1rem;
  color: #92400e;
  transition: transform 0.3s;
  font-weight: 700;
}
.bulb-trivia.open .bulb-arrow { transform: rotate(180deg); }
.bulb-body {
  background: #fffbeb;
  padding: 0;
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.4s ease, padding 0.3s;
}
.bulb-trivia.open .bulb-body {
  max-height: 1000px;
  padding: 1.2rem 1.5rem;
}
.bulb-body ul { padding-left: 1.4rem; }
.bulb-body li {
  font-size: 0.88rem;
  color: #44200a;
  margin-bottom: 0.5rem;
  line-height: 1.6;
}
.bulb-body li strong { color: #7c2d12; }
.neet-tag {
  display: inline-block;
  background: #dc2626;
  color: #fff;
  font-size: 0.6rem;
  font-weight: 800;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  padding: 1px 7px;
  border-radius: 10px;
  margin-left: 4px;
  vertical-align: middle;
}

/* ─── SVG DIAGRAM BOX ─── */
.diagram-box {
  background: linear-gradient(135deg, #f0fdf4 0%, #d1fae5 100%);
  border: 2px dashed var(--emerald-mid);
  border-radius: 16px;
  padding: 1.5rem;
  margin: 1.2rem 0;
  overflow-x: auto;
}
.diagram-box svg { display: block; margin: 0 auto; max-width: 100%; }
.diagram-label {
  text-align: center;
  font-size: 0.75rem;
  font-weight: 700;
  color: var(--emerald);
  letter-spacing: 0.1em;
  text-transform: uppercase;
  margin-bottom: 1rem;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
}
.diagram-label::before, .diagram-label::after {
  content: '';
  display: block;
  height: 1px;
  width: 40px;
  background: var(--emerald-mid);
}

/* ─── TABLES ─── */
.table-wrap { overflow-x: auto; margin: 1rem 0; border-radius: 14px; box-shadow: var(--card-shadow); }
table { width: 100%; border-collapse: collapse; font-size: 0.86rem; }
th { background: var(--emerald); color: #fff; padding: 11px 14px; text-align: left; font-weight: 700; font-size: 0.82rem; letter-spacing: 0.04em; }
th:first-child { border-radius: 12px 0 0 0; }
th:last-child { border-radius: 0 12px 0 0; }
td { padding: 9px 14px; border-bottom: 1px solid var(--border); vertical-align: top; }
tr:nth-child(even) td { background: #f0fdf9; }
tr:hover td { background: var(--emerald-light); }

/* ─── GRID ─── */
.grid-2 { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1rem; margin: 1rem 0; }
.grid-3 { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin: 1rem 0; }

.mini-card {
  background: var(--surface);
  border: 1.5px solid var(--border);
  border-radius: 14px;
  padding: 1.1rem 1.3rem;
  position: relative;
  overflow: hidden;
  transition: transform 0.2s, box-shadow 0.2s;
}
.mini-card:hover { transform: translateY(-2px); box-shadow: 0 8px 24px rgba(13,110,74,0.13); }
.mini-card h4 { font-size: 0.88rem; font-weight: 700; color: var(--emerald); margin-bottom: 8px; }
.mini-card p, .mini-card li { font-size: 0.82rem; color: var(--muted); line-height: 1.6; }
.mini-card ul { padding-left: 1rem; }
.mini-card .accent-bar {
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 4px;
}

/* ─── STEPS ─── */
.steps { list-style: none; padding-left: 0; counter-reset: step; }
.steps li {
  position: relative;
  padding: 0.85rem 1rem 0.85rem 3.2rem;
  margin-bottom: 0.7rem;
  background: var(--surface);
  border: 1.5px solid var(--border);
  border-radius: 12px;
  font-size: 0.92rem;
  counter-increment: step;
  transition: border-color 0.2s;
}
.steps li:hover { border-color: var(--emerald-mid); }
.steps li::before {
  content: counter(step);
  position: absolute;
  left: 0.8rem;
  top: 50%;
  transform: translateY(-50%);
  width: 28px;
  height: 28px;
  background: linear-gradient(135deg, var(--emerald-glow), var(--emerald));
  color: #fff;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.78rem;
  font-weight: 800;
}

/* ─── KEY TERM ─── */
.key { color: var(--emerald); font-weight: 700; }
.formula {
  font-family: 'JetBrains Mono', monospace;
  background: #e8fdf3;
  border: 1px solid #6ee7b7;
  border-radius: 5px;
  padding: 1px 7px;
  font-size: 0.84rem;
  color: var(--emerald);
}

/* ─── MCQ SECTION ─── */
.mcq-section {
  margin-top: 2.5rem;
  padding-top: 2rem;
  border-top: 2px solid var(--border);
}
.mcq-section-header {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 1.5rem;
}
.mcq-section-header h3 {
  font-family: 'Playfair Display', serif;
  font-size: 1.3rem;
  color: var(--violet);
}
.mcq-badge {
  background: var(--violet-light);
  color: var(--violet);
  font-size: 0.7rem;
  font-weight: 800;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  padding: 4px 12px;
  border-radius: 20px;
  border: 1.5px solid var(--violet);
}
.mcq-item {
  background: var(--surface);
  border: 1.5px solid #e8e0fa;
  border-radius: 14px;
  padding: 1.2rem 1.4rem;
  margin-bottom: 1rem;
  box-shadow: 0 2px 10px rgba(109,40,217,0.06);
}
.mcq-item .q-num {
  font-size: 0.68rem;
  font-weight: 800;
  color: var(--violet);
  letter-spacing: 0.1em;
  text-transform: uppercase;
  margin-bottom: 4px;
}
.mcq-item .q {
  font-weight: 600;
  font-size: 0.93rem;
  margin-bottom: 0.8rem;
  color: var(--text);
  line-height: 1.5;
}
.pyq-tag {
  display: inline-block;
  background: #fce7f3;
  color: #9d174d;
  font-size: 0.6rem;
  font-weight: 800;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  padding: 2px 8px;
  border-radius: 10px;
  margin-left: 6px;
  vertical-align: middle;
  border: 1px solid #fbcfe8;
}
.mcq-options { display: flex; flex-direction: column; gap: 6px; margin-bottom: 10px; }
.mcq-opt {
  padding: 8px 16px;
  border-radius: 25px;
  background: #f5f3ff;
  font-size: 0.84rem;
  border: 1.5px solid #ddd6fe;
  cursor: pointer;
  transition: all 0.15s;
  text-align: left;
  font-family: 'Outfit', sans-serif;
  color: var(--text);
}
.mcq-opt:hover { background: var(--violet-light); border-color: var(--violet); color: var(--violet); }
.mcq-opt.correct { background: var(--emerald-light); border-color: var(--emerald-mid); color: var(--emerald); font-weight: 600; }
.mcq-opt.wrong { background: var(--rose-light); border-color: var(--rose); color: var(--rose); }
.mcq-opt:disabled { cursor: default; }
.mcq-ans {
  display: none;
  font-size: 0.83rem;
  color: #0a3d22;
  background: var(--emerald-light);
  border-radius: 8px;
  padding: 8px 12px;
  margin-top: 6px;
  border-left: 3px solid var(--emerald-glow);
}
.mcq-item.revealed .mcq-ans { display: block; }

/* ─── QUICK NUMBERS ─── */
.numbers-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
  gap: 10px;
  margin: 1rem 0;
}
.num-card {
  background: var(--surface);
  border-radius: 14px;
  padding: 1rem;
  text-align: center;
  border: 2px solid var(--border);
  transition: transform 0.2s;
}
.num-card:hover { transform: scale(1.03); }
.num-card .num { font-family: 'Playfair Display', serif; font-size: 2rem; font-weight: 700; line-height: 1; }
.num-card .lbl { font-size: 0.72rem; font-weight: 600; color: var(--muted); margin-top: 4px; }

/* ─── PROCESS FLOW ─── */
.flow {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 0;
  margin: 1rem 0;
}
.flow-step {
  background: var(--emerald);
  color: #fff;
  padding: 8px 18px;
  border-radius: 8px;
  font-size: 0.82rem;
  font-weight: 600;
  white-space: nowrap;
}
.flow-arrow {
  font-size: 1.2rem;
  color: var(--emerald-mid);
  padding: 0 6px;
  font-weight: 700;
}
.flow-step.amber { background: var(--amber); }
.flow-step.sky { background: var(--sky); }
.flow-step.violet { background: var(--violet); }
.flow-step.teal { background: var(--teal); }
.flow-step.rose { background: var(--rose); }

/* ─── COLOR ACCENT MINIS ─── */
.mini-card.amber { border-color: #fed7aa; }
.mini-card.amber h4 { color: var(--orange); }
.mini-card.sky h4 { color: var(--sky); }
.mini-card.sky { border-color: #bae6fd; }
.mini-card.violet h4 { color: var(--violet); }
.mini-card.violet { border-color: #ddd6fe; }
.mini-card.rose h4 { color: var(--rose); }
.mini-card.rose { border-color: #fecdd3; }
.mini-card.teal h4 { color: var(--teal); }
.mini-card.teal { border-color: #99f6e4; }

/* ─── HR ─── */
hr.wave { border: none; height: 2px; background: linear-gradient(90deg, transparent, var(--emerald-light), var(--emerald-mid), var(--emerald-light), transparent); margin: 2rem 0; }

/* ─── REVISION PANEL ─── */
.revision-panel {
  background: linear-gradient(135deg, #064e2c 0%, #0d6e4a 100%);
  border-radius: 18px;
  padding: 2rem;
  color: #fff;
  margin: 2rem 0;
}
.revision-panel h3 {
  font-family: 'Playfair Display', serif;
  font-size: 1.2rem;
  margin-bottom: 1rem;
  color: #b9ffd9;
}
.revision-panel .rev-item {
  display: flex;
  align-items: flex-start;
  gap: 10px;
  margin-bottom: 0.6rem;
  font-size: 0.88rem;
  color: rgba(255,255,255,0.88);
}
.revision-panel .rev-item::before { content: '→'; color: var(--emerald-glow); font-weight: 700; flex-shrink: 0; }

/* ─── FOOTER ─── */
footer {
  background: var(--emerald);
  color: rgba(255,255,255,0.7);
  text-align: center;
  padding: 2rem;
  font-size: 0.8rem;
  margin-top: 2rem;
}
footer strong { color: #fff; }

/* ─── SCROLLBAR ─── */
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: var(--bg); }
::-webkit-scrollbar-thumb { background: var(--emerald-mid); border-radius: 3px; }

/* ─── RESPONSIVE ─── */
@media(max-width:600px){
  .hero { padding: 2.5rem 1rem 4rem; }
  .container { padding: 0 1rem 3rem; }
  .flow { flex-direction: column; align-items: flex-start; }
  .flow-arrow { transform: rotate(90deg); }
}

/* ─── TAG ─── */
.tag {
  display: inline-block;
  font-size: 0.7rem;
  font-weight: 700;
  padding: 2px 10px;
  border-radius: 20px;
  margin: 2px 3px 2px 0;
}
.tag.g { background: var(--emerald-light); color: var(--emerald); }
.tag.a { background: var(--amber-light); color: var(--amber); }
.tag.b { background: var(--sky-light); color: var(--sky); }
.tag.r { background: var(--rose-light); color: var(--rose); }
.tag.v { background: var(--violet-light); color: var(--violet); }
</style>
</head>
<body>

<!-- HERO -->
<div class="hero">
  <div class="hero-tag">NCERT Class 12 · Biology · Chapter 1</div>
  <h1>Sexual Reproduction in<br>Flowering Plants</h1>
  <p>Complete study guide · NEET & Boards focused · Allen module trivia included</p>
  <div class="hero-badges">
    <span class="badge">Angiosperm Reproduction</span>
    <span class="badge">Microsporogenesis</span>
    <span class="badge">Megasporogenesis</span>
    <span class="badge">Double Fertilisation</span>
    <span class="badge">Embryology</span>
    <span class="badge">Apomixis</span>
  </div>
</div>

<!-- NAV -->
<nav class="topic-nav" id="topicNav">
  <button class="topic-btn active" onclick="showPage('intro',this)">🌿 Introduction</button>
  <button class="topic-btn" onclick="showPage('flower',this)">🌸 The Flower</button>
  <button class="topic-btn" onclick="showPage('stamen',this)">🌾 Stamen & Pollen</button>
  <button class="topic-btn" onclick="showPage('pistil',this)">🌼 Pistil & Ovule</button>
  <button class="topic-btn" onclick="showPage('pollination',this)">🐝 Pollination</button>
  <button class="topic-btn" onclick="showPage('fertilisation',this)">⚗️ Fertilisation</button>
  <button class="topic-btn" onclick="showPage('seed',this)">🌱 Seed & Embryo</button>
  <button class="topic-btn" onclick="showPage('apomixis',this)">🔬 Apomixis</button>
  <button class="topic-btn" onclick="showPage('revision',this)">📋 Quick Revision</button>
</nav>

<!-- ══════════════════════════════════════
     PAGE 1: INTRODUCTION
═══════════════════════════════════════ -->
<div class="page active" id="page-intro">
  <div class="page-header">
    <div class="page-num">Topic 1 of 8</div>
    <div class="page-title">Introduction to Angiosperm Reproduction</div>
    <div class="page-subtitle">Flowers, Sexual Reproduction & Key Concepts</div>
  </div>
  <div class="container">

    <div class="card">
      <p><span class="key">Angiosperms</span> (flowering plants) are the most dominant group of land plants on Earth. They reproduce sexually via formation of male & female gametes, pollination, fertilisation, and seed/fruit development.</p>
      <br>
      <p><strong>Sexual reproduction</strong> in angiosperms involves fusion of male (pollen) and female (ovule) gametes → zygote → seed. The <span class="key">flower</span> is the reproductive unit — it is a <em>modified shoot</em>.</p>
    </div>

    <!-- DIAGRAM: Flower position in Plant Life Cycle -->
    <div class="diagram-box">
      <div class="diagram-label">NCERT Diagram — Life Cycle Overview (Angiosperm)</div>
      <svg viewBox="0 0 700 260" xmlns="http://www.w3.org/2000/svg" font-family="Outfit,sans-serif">
        <!-- Boxes -->
        <rect x="10" y="100" width="110" height="50" rx="10" fill="#0d6e4a"/>
        <text x="65" y="121" fill="#fff" text-anchor="middle" font-size="12" font-weight="700">Sporophyte</text>
        <text x="65" y="138" fill="#c9ffe8" text-anchor="middle" font-size="10">(2n) — Plant Body</text>

        <rect x="160" y="100" width="110" height="50" rx="10" fill="#16a06a"/>
        <text x="215" y="121" fill="#fff" text-anchor="middle" font-size="12" font-weight="700">Flower</text>
        <text x="215" y="138" fill="#c9ffe8" text-anchor="middle" font-size="10">Reproductive organ</text>

        <rect x="310" y="40" width="120" height="50" rx="10" fill="#1ecc87"/>
        <text x="370" y="61" fill="#fff" text-anchor="middle" font-size="12" font-weight="700">Pollen Grain</text>
        <text x="370" y="78" fill="#e0fff5" text-anchor="middle" font-size="10">(n) — ♂ gametophyte</text>

        <rect x="310" y="160" width="120" height="50" rx="10" fill="#0f766e"/>
        <text x="370" y="181" fill="#fff" text-anchor="middle" font-size="12" font-weight="700">Embryo Sac</text>
        <text x="370" y="198" fill="#ccfbf1" text-anchor="middle" font-size="10">(n) — ♀ gametophyte</text>

        <rect x="480" y="100" width="110" height="50" rx="10" fill="#d97706"/>
        <text x="535" y="121" fill="#fff" text-anchor="middle" font-size="12" font-weight="700">Fertilisation</text>
        <text x="535" y="138" fill="#fef3c7" text-anchor="middle" font-size="10">Syngamy + Triple fusion</text>

        <rect x="600" y="100" width="90" height="50" rx="10" fill="#6d28d9"/>
        <text x="645" y="121" fill="#fff" text-anchor="middle" font-size="12" font-weight="700">Seed</text>
        <text x="645" y="138" fill="#ede9fe" text-anchor="middle" font-size="10">(2n embryo)</text>

        <!-- Arrows -->
        <line x1="120" y1="125" x2="155" y2="125" stroke="#0d6e4a" stroke-width="2.5" marker-end="url(#arr)"/>
        <line x1="270" y1="115" x2="305" y2="75" stroke="#16a06a" stroke-width="2" marker-end="url(#arr)"/>
        <line x1="270" y1="135" x2="305" y2="175" stroke="#16a06a" stroke-width="2" marker-end="url(#arr)"/>
        <line x1="430" y1="65" x2="475" y2="110" stroke="#1ecc87" stroke-width="2" marker-end="url(#arr)"/>
        <line x1="430" y1="185" x2="475" y2="145" stroke="#0f766e" stroke-width="2" marker-end="url(#arr)"/>
        <line x1="590" y1="125" x2="597" y2="125" stroke="#d97706" stroke-width="2.5" marker-end="url(#arr)"/>

        <!-- MEIOSIS label -->
        <text x="240" y="85" fill="#6d28d9" font-size="10" font-weight="700">Meiosis</text>
        <!-- MITOSIS label -->
        <text x="240" y="165" fill="#6d28d9" font-size="10" font-weight="700">Meiosis</text>

        <defs>
          <marker id="arr" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
            <path d="M0,0 L0,6 L8,3 z" fill="#0d6e4a"/>
          </marker>
        </defs>
      </svg>
    </div>

    <div class="info-box green">
      <strong>Key Definition</strong>
      <strong>Angiosperm</strong> = Greek <em>angeion</em> (vessel) + <em>sperma</em> (seed) → seed enclosed in a fruit. The flower is a modified shoot acting as the reproductive unit.
    </div>

    <!-- BULB TRIVIA -->
    <div class="bulb-trivia" onclick="toggleBulb(this)">
      <div class="bulb-header">
        <div class="bulb-icon">
          <svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg">
            <circle cx="20" cy="16" r="11" fill="#fbbf24" opacity="0.3"/>
            <path d="M20 5 C13 5 8 10 8 17 C8 22 11 25 14 27 L14 31 C14 32.1 14.9 33 16 33 L24 33 C25.1 33 26 32.1 26 31 L26 27 C29 25 32 22 32 17 C32 10 27 5 20 5 Z" fill="#f59e0b" stroke="#d97706" stroke-width="1.5"/>
            <rect x="16" y="33" width="8" height="3" rx="1.5" fill="#92400e"/>
            <line x1="20" y1="28" x2="20" y2="30" stroke="#fff" stroke-width="2" opacity="0.6"/>
            <circle cx="20" cy="3" r="2" fill="#fde68a"/>
            <line x1="7" y1="17" x2="4" y2="17" stroke="#fde68a" stroke-width="2"/>
            <line x1="33" y1="17" x2="36" y2="17" stroke="#fde68a" stroke-width="2"/>
            <line x1="9.5" y1="8.5" x2="7" y2="6" stroke="#fde68a" stroke-width="2"/>
            <line x1="30.5" y1="8.5" x2="33" y2="6" stroke="#fde68a" stroke-width="2"/>
          </svg>
        </div>
        <div class="bulb-label">
          NEET + Allen Trivia
          <span>High-yield facts for Introduction</span>
        </div>
        <div class="bulb-arrow">▼</div>
      </div>
      <div class="bulb-body">
        <ul>
          <li>Angiosperms are the <strong>only group showing double fertilisation</strong> — first discovered by <strong>Nawaschin (1898)</strong> in <em>Lilium</em> and <em>Fritillaria</em>. <span class="neet-tag">NEET</span></li>
          <li>Flower = <strong>modified shoot</strong> with determinate growth on a receptacle (thalamus).</li>
          <li>Gymnosperms: <strong>NO double fertilisation</strong>, seeds naked (not enclosed in fruit).</li>
          <li>Sexual reproduction → genetic variation; promotes evolution and adaptability.</li>
          <li>Asexual reproduction in plants = vegetative propagation (no fusion of gametes).</li>
          <li>Term <em>Angiosperm</em> coined by <strong>Paul Hermann (1690)</strong>.</li>
        </ul>
      </div>
    </div>

    <!-- MCQ Section -->
    <div class="mcq-section">
      <div class="mcq-section-header">
        <h3>Practice Questions</h3>
        <span class="mcq-badge">3 MCQs · Boards + NEET</span>
      </div>

      <div class="mcq-item" id="i-q1">
        <div class="q-num">Q 1 · Introduction</div>
        <div class="q">Double fertilisation is a unique feature of: <span class="pyq-tag">NEET 2016</span></div>
        <div class="mcq-options">
          <button class="mcq-opt" onclick="answerMCQ('i-q1',this,false)">A. Gymnosperms</button>
          <button class="mcq-opt" onclick="answerMCQ('i-q1',this,true)">B. Angiosperms</button>
          <button class="mcq-opt" onclick="answerMCQ('i-q1',this,false)">C. Pteridophytes</button>
          <button class="mcq-opt" onclick="answerMCQ('i-q1',this,false)">D. Bryophytes</button>
        </div>
        <div class="mcq-ans">✓ Angiosperms — Double fertilisation (syngamy + triple fusion) is unique to angiosperms, first reported by Nawaschin (1898).</div>
      </div>

      <div class="mcq-item" id="i-q2">
        <div class="q-num">Q 2 · Introduction</div>
        <div class="q">A flower is considered a modified: <span class="pyq-tag">Boards 2019</span></div>
        <div class="mcq-options">
          <button class="mcq-opt" onclick="answerMCQ('i-q2',this,false)">A. Root</button>
          <button class="mcq-opt" onclick="answerMCQ('i-q2',this,false)">B. Leaf</button>
          <button class="mcq-opt" onclick="answerMCQ('i-q2',this,true)">C. Shoot</button>
          <button class="mcq-opt" onclick="answerMCQ('i-q2',this,false)">D. Bud</button>
        </div>
        <div class="mcq-ans">✓ Shoot — The flower is a modified shoot; it bears whorls of sepals, petals, stamens, and carpels on the receptacle (thalamus).</div>
      </div>

      <div class="mcq-item" id="i-q3">
        <div class="q-num">Q 3 · Introduction</div>
        <div class="q">The term 'Angiosperm' comes from Greek words meaning:</div>
        <div class="mcq-options">
          <button class="mcq-opt" onclick="answerMCQ('i-q3',this,false)">A. Naked seed</button>
          <button class="mcq-opt" onclick="answerMCQ('i-q3',this,true)">B. Enclosed seed (vessel + seed)</button>
          <button class="mcq-opt" onclick="answerMCQ('i-q3',this,false)">C. Double seed</button>
          <button class="mcq-opt" onclick="answerMCQ('i-q3',this,false)">D. Flowering plant</button>
        </div>
        <div class="mcq-ans">✓ Enclosed seed — Greek: angeion (vessel) + sperma (seed) = seed enclosed in a vessel (fruit). Gymnosperm = naked seed (gymno = naked).</div>
      </div>
    </div>

  </div>
</div>

<!-- ══════════════════════════════════════
     PAGE 2: THE FLOWER
═══════════════════════════════════════ -->
<div class="page" id="page-flower">
  <div class="page-header">
    <div class="page-num">Topic 2 of 8</div>
    <div class="page-title">The Flower — Structure & Parts</div>
    <div class="page-subtitle">Whorls, Symmetry & Sexual Types</div>
  </div>
  <div class="container">

    <!-- DIAGRAM: Flower Parts -->
    <div class="diagram-box">
      <div class="diagram-label">NCERT Diagram — Parts of a Typical Flower</div>
      <svg viewBox="0 0 680 320" xmlns="http://www.w3.org/2000/svg" font-family="Outfit,sans-serif">
        <!-- Receptacle / Stem -->
        <rect x="320" y="270" width="40" height="50" rx="5" fill="#5a3e28"/>
        <text x="340" y="310" fill="#fff" text-anchor="middle" font-size="10" font-weight="600">Peduncle</text>

        <!-- Thalamus -->
        <ellipse cx="340" cy="265" rx="30" ry="12" fill="#7c5c3a"/>
        <text x="390" y="269" fill="#7c5c3a" font-size="10" font-weight="700">Thalamus/Receptacle</text>

        <!-- Sepals (calyx) -->
        <path d="M340,260 Q310,240 300,210 Q330,225 340,255" fill="#2d7a3a" stroke="#1a5c28" stroke-width="1"/>
        <path d="M340,260 Q370,240 380,210 Q350,225 340,255" fill="#2d7a3a" stroke="#1a5c28" stroke-width="1"/>
        <path d="M340,260 Q315,248 305,220 Q328,233 340,255" fill="#3a8c47"/>
        <text x="285" y="205" fill="#1a5c28" font-size="11" font-weight="700">Sepals (Calyx)</text>

        <!-- Petals (corolla) -->
        <path d="M340,255 Q295,220 290,170 Q325,195 340,250" fill="#ff9eb5" stroke="#d63060" stroke-width="1" opacity="0.9"/>
        <path d="M340,255 Q385,220 390,170 Q355,195 340,250" fill="#ff9eb5" stroke="#d63060" stroke-width="1" opacity="0.9"/>
        <path d="M340,255 Q300,215 295,165 Q328,188 340,250" fill="#ffb3c6" opacity="0.85"/>
        <path d="M340,255 Q380,215 385,165 Q352,188 340,250" fill="#ffb3c6" opacity="0.85"/>
        <text x="420" y="168" fill="#be123c" font-size="11" font-weight="700">Petals (Corolla)</text>

        <!-- Stamens (androecium) -->
        <line x1="325" y1="250" x2="310" y2="190" stroke="#d97706" stroke-width="2.5"/>
        <ellipse cx="309" cy="186" rx="7" ry="5" fill="#fbbf24" stroke="#d97706" stroke-width="1.5"/>
        <line x1="340" y1="248" x2="338" y2="185" stroke="#d97706" stroke-width="2.5"/>
        <ellipse cx="337" cy="181" rx="7" ry="5" fill="#fbbf24" stroke="#d97706" stroke-width="1.5"/>
        <line x1="355" y1="250" x2="368" y2="190" stroke="#d97706" stroke-width="2.5"/>
        <ellipse cx="369" cy="186" rx="7" ry="5" fill="#fbbf24" stroke="#d97706" stroke-width="1.5"/>
        <text x="200" y="192" fill="#d97706" font-size="11" font-weight="700">Stamen (Androecium)</text>
        <text x="200" y="205" fill="#d97706" font-size="9">Filament + Anther</text>

        <!-- Pistil (gynoecium) -->
        <!-- Stigma -->
        <ellipse cx="340" cy="155" rx="12" ry="6" fill="#6d28d9"/>
        <text x="420" y="158" fill="#6d28d9" font-size="11" font-weight="700">Stigma</text>
        <!-- Style -->
        <rect x="336" y="161" width="8" height="35" rx="4" fill="#7c3aed"/>
        <text x="420" y="185" fill="#7c3aed" font-size="10">Style</text>
        <!-- Ovary -->
        <ellipse cx="340" cy="206" rx="16" ry="12" fill="#4c1d95" stroke="#6d28d9" stroke-width="1.5"/>
        <text x="420" y="210" fill="#4c1d95" font-size="10" font-weight="700">Ovary (Gynoecium)</text>
        <!-- Ovules inside -->
        <ellipse cx="336" cy="206" rx="4" ry="3" fill="#c4b5fd"/>
        <ellipse cx="344" cy="210" rx="4" ry="3" fill="#c4b5fd"/>
        <text x="420" y="222" fill="#6d28d9" font-size="9">Contains ovules (♀)</text>

        <!-- Labels left -->
        <line x1="293" y1="258" x2="275" y2="270" stroke="#1a5c28" stroke-width="1" stroke-dasharray="3"/>
        <line x1="200" y1="188" x2="295" y2="240" stroke="#d97706" stroke-width="1" stroke-dasharray="3"/>
        <line x1="419" y1="155" x2="355" y2="158" stroke="#6d28d9" stroke-width="1" stroke-dasharray="3"/>
        <line x1="419" y1="168" x2="395" y2="175" stroke="#be123c" stroke-width="1" stroke-dasharray="3"/>
        <line x1="419" y1="208" x2="360" y2="208" stroke="#4c1d95" stroke-width="1" stroke-dasharray="3"/>

        <text x="10" y="250" fill="#0d6e4a" font-size="10" font-style="italic">♀ Pistil = Stigma + Style + Ovary</text>
        <text x="10" y="265" fill="#d97706" font-size="10" font-style="italic">♂ Stamen = Filament + Anther</text>
      </svg>
    </div>

    <div class="section-title">Whorls of a Flower</div>
    <div class="table-wrap">
      <table>
        <tr><th>Whorl</th><th>Parts</th><th>Function</th><th>Type</th></tr>
        <tr><td><span class="tag g">Calyx</span></td><td>Sepals</td><td>Protect bud</td><td>Accessory</td></tr>
        <tr><td><span class="tag r">Corolla</span></td><td>Petals</td><td>Attract pollinators</td><td>Accessory</td></tr>
        <tr><td><span class="tag a">Androecium</span></td><td>Stamens ♂</td><td>Produces pollen</td><td>Essential</td></tr>
        <tr><td><span class="tag v">Gynoecium</span></td><td>Carpels/Pistil ♀</td><td>Contains ovules</td><td>Essential</td></tr>
      </table>
    </div>

    <div class="section-title">Types of Flowers</div>
    <div class="grid-2">
      <div class="mini-card">
        <div class="accent-bar" style="background:linear-gradient(90deg,#0d6e4a,#1ecc87)"></div>
        <h4>Bisexual (Hermaphrodite)</h4>
        <p>Both androecium + gynoecium present</p>
        <p style="margin-top:6px"><strong>Eg:</strong> Mustard, Rose, China rose, Lily</p>
      </div>
      <div class="mini-card amber">
        <div class="accent-bar" style="background:linear-gradient(90deg,#d97706,#fbbf24)"></div>
        <h4>Unisexual</h4>
        <p>Either staminate (♂) OR pistillate (♀)</p>
        <p style="margin-top:6px"><strong>Eg:</strong> Papaya, Coconut, Maize, Cucumber</p>
      </div>
      <div class="mini-card sky">
        <div class="accent-bar" style="background:linear-gradient(90deg,#0369a1,#38bdf8)"></div>
        <h4>Monoecious</h4>
        <p>Both ♂ & ♀ flowers on <strong>same plant</strong></p>
        <p style="margin-top:6px"><strong>Eg:</strong> Maize (corn), Coconut, Castor</p>
      </div>
      <div class="mini-card violet">
        <div class="accent-bar" style="background:linear-gradient(90deg,#6d28d9,#a78bfa)"></div>
        <h4>Dioecious</h4>
        <p>♂ & ♀ flowers on <strong>different plants</strong></p>
        <p style="margin-top:6px"><strong>Eg:</strong> Papaya, Date palm, Cannabis, Hemp</p>
      </div>
    </div>

    <div class="info-box amber">
      <strong>Symmetry Types (NCERT)</strong>
      <strong>Actinomorphic</strong> = radial symmetry (can be divided in multiple planes) → Rose, Mustard | <strong>Zygomorphic</strong> = bilateral symmetry (only one plane) → Pea, Gulmohar, Bean | <strong>Asymmetric</strong> = no plane of symmetry → Canna
    </div>

    <!-- BULB TRIVIA -->
    <div class="bulb-trivia" onclick="toggleBulb(this)">
      <div class="bulb-header">
        <div class="bulb-icon">
          <svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg">
            <circle cx="20" cy="16" r="11" fill="#fbbf24" opacity="0.3"/>
            <path d="M20 5 C13 5 8 10 8 17 C8 22 11 25 14 27 L14 31 C14 32.1 14.9 33 16 33 L24 33 C25.1 33 26 32.1 26 31 L26 27 C29 25 32 22 32 17 C32 10 27 5 20 5 Z" fill="#f59e0b" stroke="#d97706" stroke-width="1.5"/>
            <rect x="16" y="33" width="8" height="3" rx="1.5" fill="#92400e"/>
          </svg>
        </div>
        <div class="bulb-label">NEET + Allen Trivia<span>High-yield facts for The Flower</span></div>
        <div class="bulb-arrow">▼</div>
      </div>
      <div class="bulb-body">
        <ul>
          <li><strong>Ebracteate</strong> = no bract; <strong>Bracteate</strong> = bract present. Bract = leaf-like structure at base of flower. <span class="neet-tag">Allen</span></li>
          <li>Flowers with both whorls (calyx + corolla) = <strong>complete</strong>; missing one = <strong>incomplete</strong>.</li>
          <li><strong>Epigynous flower</strong>: ovary inferior (thalamus grows around ovary) — apple, guava, cucumber. <span class="neet-tag">NEET</span></li>
          <li><strong>Hypogynous</strong>: ovary superior (most flowers) — mustard, brinjal.</li>
          <li><strong>Perigynous</strong>: ovary half-inferior — rose, plum.</li>
          <li>When sepals are fused = <strong>gamosepalous</strong>; free = <strong>polysepalous</strong>. Petals fused = <strong>gamopetalous</strong>; free = <strong>polypetalous</strong>. <span class="neet-tag">Boards</span></li>
          <li><strong>Dioecy</strong> is an outbreeding device — ensures cross-pollination, promotes genetic variation.</li>
        </ul>
      </div>
    </div>

    <!-- MCQ Section -->
    <div class="mcq-section">
      <div class="mcq-section-header">
        <h3>Practice Questions</h3>
        <span class="mcq-badge">3 MCQs · Boards + NEET</span>
      </div>

      <div class="mcq-item" id="f-q1">
        <div class="q-num">Q 1 · The Flower</div>
        <div class="q">Which of the following plants is dioecious? <span class="pyq-tag">Boards 2017</span></div>
        <div class="mcq-options">
          <button class="mcq-opt" onclick="answerMCQ('f-q1',this,false)">A. Maize</button>
          <button class="mcq-opt" onclick="answerMCQ('f-q1',this,false)">B. Coconut</button>
          <button class="mcq-opt" onclick="answerMCQ('f-q1',this,true)">C. Papaya</button>
          <button class="mcq-opt" onclick="answerMCQ('f-q1',this,false)">D. Castor</button>
        </div>
        <div class="mcq-ans">✓ Papaya is dioecious — male and female flowers on different plants. Maize and coconut are monoecious (both sexes on same plant).</div>
      </div>

      <div class="mcq-item" id="f-q2">
        <div class="q-num">Q 2 · The Flower</div>
        <div class="q">A flower that can be divided into two equal halves in only one plane is called: <span class="pyq-tag">NEET 2018</span></div>
        <div class="mcq-options">
          <button class="mcq-opt" onclick="answerMCQ('f-q2',this,false)">A. Actinomorphic</button>
          <button class="mcq-opt" onclick="answerMCQ('f-q2',this,true)">B. Zygomorphic</button>
          <button class="mcq-opt" onclick="answerMCQ('f-q2',this,false)">C. Asymmetric</button>
          <button class="mcq-opt" onclick="answerMCQ('f-q2',this,false)">D. Trimerous</button>
        </div>
        <div class="mcq-ans">✓ Zygomorphic = bilateral symmetry (one plane only). Examples: Pea, Gulmohar, Bean. Actinomorphic = radial symmetry (multiple planes).</div>
      </div>

      <div class="mcq-item" id="f-q3">
        <div class="q-num">Q 3 · The Flower</div>
        <div class="q">The essential whorls of a flower are: <span class="pyq-tag">Boards 2020</span></div>
        <div class="mcq-options">
          <button class="mcq-opt" onclick="answerMCQ('f-q3',this,false)">A. Calyx and Corolla</button>
          <button class="mcq-opt" onclick="answerMCQ('f-q3',this,false)">B. Calyx and Androecium</button>
          <button class="mcq-opt" onclick="answerMCQ('f-q3',this,true)">C. Androecium and Gynoecium</button>
          <button class="mcq-opt" onclick="answerMCQ('f-q3',this,false)">D. Corolla and Gynoecium</button>
        </div>
        <div class="mcq-ans">✓ Androecium (♂) and Gynoecium (♀) are essential whorls — directly involved in reproduction. Calyx and Corolla are accessory whorls.</div>
      </div>
    </div>

  </div>
</div>

<!-- ══════════════════════════════════════
     PAGE 3: STAMEN & POLLEN
═══════════════════════════════════════ -->
<div class="page" id="page-stamen">
  <div class="page-header">
    <div class="page-num">Topic 3 of 8</div>
    <div class="page-title">Stamen, Microsporogenesis & Pollen Grain</div>
    <div class="page-subtitle">Anther Wall · Tapetum · Pollen Structure · Male Gametophyte</div>
  </div>
  <div class="container">

    <!-- Anther Diagram -->
    <div class="diagram-box">
      <div class="diagram-label">NCERT + Allen Diagram — T.S. of Anther (Microsporangium)</div>
      <svg viewBox="0 0 700 310" xmlns="http://www.w3.org/2000/svg" font-family="Outfit,sans-serif">
        <!-- Anther shape -->
        <ellipse cx="200" cy="160" rx="130" ry="95" fill="#e8f5ee" stroke="#0d6e4a" stroke-width="2"/>
        <!-- Vascular bundle (connective) -->
        <rect x="185" y="80" width="30" height="160" rx="8" fill="#a7f3d0" stroke="#16a06a" stroke-width="1.5"/>
        <text x="200" y="168" fill="#065f46" text-anchor="middle" font-size="9" font-weight="700">Connective</text>

        <!-- Left lobe - microsporangia -->
        <ellipse cx="130" cy="130" rx="45" ry="35" fill="#d0f5e5" stroke="#16a06a" stroke-width="1.5"/>
        <ellipse cx="130" cy="190" rx="45" ry="35" fill="#d0f5e5" stroke="#16a06a" stroke-width="1.5"/>
        <!-- Right lobe -->
        <ellipse cx="270" cy="130" rx="45" ry="35" fill="#d0f5e5" stroke="#16a06a" stroke-width="1.5"/>
        <ellipse cx="270" cy="190" rx="45" ry="35" fill="#d0f5e5" stroke="#16a06a" stroke-width="1.5"/>

        <!-- Sporogenous tissue (pollen) -->
        <circle cx="130" cy="130" r="22" fill="#fbbf24" opacity="0.5"/>
        <circle cx="130" cy="190" r="22" fill="#fbbf24" opacity="0.5"/>
        <circle cx="270" cy="130" r="22" fill="#fbbf24" opacity="0.5"/>
        <circle cx="270" cy="190" r="22" fill="#fbbf24" opacity="0.5"/>

        <!-- Small pollen circles -->
        <circle cx="125" cy="125" r="5" fill="#d97706"/>
        <circle cx="137" cy="132" r="5" fill="#d97706"/>
        <circle cx="128" cy="140" r="5" fill="#d97706"/>
        <circle cx="265" cy="125" r="5" fill="#d97706"/>
        <circle cx="277" cy="132" r="5" fill="#d97706"/>

        <!-- Wall layers label area -->
        <!-- Epidermis -->
        <line x1="90" y1="130" x2="60" y2="100" stroke="#be123c" stroke-width="1.5" stroke-dasharray="3"/>
        <text x="5" y="95" fill="#be123c" font-size="10" font-weight="700">Epidermis</text>

        <!-- Endothecium -->
        <line x1="92" y1="140" x2="50" y2="150" stroke="#0369a1" stroke-width="1.5" stroke-dasharray="3"/>
        <text x="0" y="148" fill="#0369a1" font-size="10" font-weight="700">Endothecium</text>

        <!-- Middle layers -->
        <line x1="93" y1="155" x2="50" y2="178" stroke="#6d28d9" stroke-width="1.5" stroke-dasharray="3"/>
        <text x="0" y="176" fill="#6d28d9" font-size="10" font-weight="700">Middle Layer(s)</text>

        <!-- Tapetum -->
        <line x1="105" y1="165" x2="55" y2="200" stroke="#d97706" stroke-width="2" stroke-dasharray="3"/>
        <text x="0" y="200" fill="#d97706" font-size="10" font-weight="800">Tapetum ★</text>
        <text x="0" y="212" fill="#d97706" font-size="8">(innermost, nutritive)</text>

        <!-- Sporogenous tissue -->
        <line x1="142" y1="130" x2="330" y2="80" stroke="#065f46" stroke-width="1.5" stroke-dasharray="3"/>
        <text x="335" y="78" fill="#065f46" font-size="10" font-weight="700">Sporogenous Tissue (MMC)</text>
        <text x="335" y="92" fill="#065f46" font-size="9">→ Microspores by Meiosis</text>

        <!-- Filament -->
        <rect x="185" y="255" width="30" height="45" rx="5" fill="#5a3e28"/>
        <text x="200" y="286" fill="#fff" text-anchor="middle" font-size="9" font-weight="700">Filament</text>

        <!-- Labels -->
        <text x="340" y="120" fill="#16a06a" font-size="10" font-weight="700">Left Lobe</text>
        <text x="340" y="135" fill="#16a06a" font-size="9">2 microsporangia</text>
        <text x="340" y="160" fill="#d97706" font-size="10" font-weight="700">Anther = Bilobed</text>
        <text x="340" y="175" fill="#d97706" font-size="9">4 microsporangia total</text>
        <text x="340" y="195" fill="#6d28d9" font-size="10" font-weight="700">= Tetrasporangiate</text>

        <line x1="270" y1="235" x2="340" y2="220" stroke="#16a06a" stroke-width="1" stroke-dasharray="3"/>
        <line x1="270" y1="90" x2="340" y2="120" stroke="#16a06a" stroke-width="1" stroke-dasharray="3"/>
      </svg>
    </div>

    <div class="info-box green">
      <strong>Anther Wall Layers (Outside → Inside)</strong>
      <div class="flow" style="margin-top:8px">
        <span class="flow-step rose">Epidermis</span><span class="flow-arrow">→</span>
        <span class="flow-step sky">Endothecium</span><span class="flow-arrow">→</span>
        <span class="flow-step violet">Middle Layers (2-3)</span><span class="flow-arrow">→</span>
        <span class="flow-step amber">Tapetum ★</span>
      </div>
    </div>

    <div class="section-title">Microsporogenesis — Process</div>
    <div class="diagram-box">
      <div class="diagram-label">NCERT Diagram — Microsporogenesis Flow</div>
      <svg viewBox="0 0 680 120" xmlns="http://www.w3.org/2000/svg" font-family="Outfit,sans-serif">
        <rect x="10" y="35" width="130" height="50" rx="10" fill="#0d6e4a"/>
        <text x="75" y="57" fill="#fff" text-anchor="middle" font-size="12" font-weight="700">MMC (2n)</text>
        <text x="75" y="74" fill="#c9ffe8" text-anchor="middle" font-size="10">Microspore Mother Cell</text>

        <text x="155" y="62" fill="#d97706" text-anchor="middle" font-size="11" font-weight="700">Meiosis I</text>
        <line x1="145" y1="60" x2="175" y2="60" stroke="#d97706" stroke-width="2" marker-end="url(#a2)"/>

        <rect x="180" y="35" width="120" height="50" rx="10" fill="#16a06a"/>
        <text x="240" y="57" fill="#fff" text-anchor="middle" font-size="12" font-weight="700">Dyad (n+n)</text>
        <text x="240" y="74" fill="#c9ffe8" text-anchor="middle" font-size="10">2 haploid cells</text>

        <text x="315" y="62" fill="#d97706" text-anchor="middle" font-size="11" font-weight="700">Meiosis II</text>
        <line x1="305" y1="60" x2="335" y2="60" stroke="#d97706" stroke-width="2" marker-end="url(#a2)"/>

        <rect x="340" y="25" width="130" height="70" rx="10" fill="#1ecc87"/>
        <text x="405" y="52" fill="#fff" text-anchor="middle" font-size="12" font-weight="700">Tetrad (n each)</text>
        <text x="405" y="68" fill="#e0fff5" text-anchor="middle" font-size="10">4 microspores</text>
        <text x="405" y="84" fill="#e0fff5" text-anchor="middle" font-size="9">Isobilateral / Tetrahedral</text>

        <line x1="475" y1="60" x2="505" y2="60" stroke="#6d28d9" stroke-width="2" marker-end="url(#a2)"/>
        <text x="487" y="52" fill="#6d28d9" font-size="9">develops</text>

        <rect x="510" y="30" width="150" height="60" rx="10" fill="#6d28d9"/>
        <text x="585" y="57" fill="#fff" text-anchor="middle" font-size="11" font-weight="700">Pollen Grain (n)</text>
        <text x="585" y="72" fill="#e9d5ff" text-anchor="middle" font-size="9">Male Gametophyte</text>
        <text x="585" y="84" fill="#e9d5ff" text-anchor="middle" font-size="9">2-celled or 3-celled</text>

        <defs>
          <marker id="a2" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
            <path d="M0,0 L0,6 L8,3 z" fill="#0d6e4a"/>
          </marker>
        </defs>
      </svg>
    </div>

    <div class="section-title">Structure of Pollen Grain</div>
    <div class="diagram-box">
      <div class="diagram-label">Allen Diagram — Pollen Grain (L.S. / 2-celled stage)</div>
      <svg viewBox="0 0 500 220" xmlns="http://www.w3.org/2000/svg" font-family="Outfit,sans-serif">
        <!-- Outer Exine -->
        <ellipse cx="200" cy="110" rx="100" ry="80" fill="none" stroke="#d97706" stroke-width="8" opacity="0.4"/>
        <ellipse cx="200" cy="110" rx="100" ry="80" fill="none" stroke="#d97706" stroke-width="3"/>
        <!-- Intine -->
        <ellipse cx="200" cy="110" rx="85" ry="68" fill="#fffbeb" stroke="#16a06a" stroke-width="2"/>
        <!-- Cytoplasm/Vegetative cell -->
        <ellipse cx="200" cy="115" rx="78" ry="62" fill="#d0f5e5" opacity="0.7"/>
        <!-- Generative cell -->
        <ellipse cx="200" cy="100" rx="28" ry="20" fill="#0d6e4a" opacity="0.85"/>
        <text x="200" y="104" fill="#fff" text-anchor="middle" font-size="9" font-weight="700">Generative</text>
        <text x="200" y="115" fill="#fff" text-anchor="middle" font-size="8">cell (n)</text>

        <!-- Aperture (pore/colpus) -->
        <ellipse cx="295" cy="110" rx="8" ry="20" fill="#fbbf24" stroke="#d97706" stroke-width="1.5"/>

        <!-- Vegetative nucleus -->
        <circle cx="185" cy="140" r="12" fill="#16a06a" opacity="0.7"/>
        <text x="185" y="144" fill="#fff" text-anchor="middle" font-size="8">V.N.</text>

        <!-- Labels -->
        <line x1="300" y1="60" x2="370" y2="40" stroke="#d97706" stroke-width="1.5" stroke-dasharray="3"/>
        <text x="373" y="38" fill="#d97706" font-size="10" font-weight="700">Exine</text>
        <text x="373" y="50" fill="#92400e" font-size="9">(Sporopollenin)</text>

        <line x1="285" y1="80" x2="370" y2="70" stroke="#16a06a" stroke-width="1.5" stroke-dasharray="3"/>
        <text x="373" y="72" fill="#16a06a" font-size="10" font-weight="700">Intine</text>
        <text x="373" y="84" fill="#065f46" font-size="9">(Cellulose + Pectin)</text>

        <line x1="225" y1="100" x2="370" y2="100" stroke="#0d6e4a" stroke-width="1.5" stroke-dasharray="3"/>
        <text x="373" y="104" fill="#0d6e4a" font-size="10" font-weight="700">Generative Cell (n)</text>
        <text x="373" y="116" fill="#0d6e4a" font-size="9">Divides → 2 male gametes</text>

        <line x1="225" y1="138" x2="373" y2="135" stroke="#16a06a" stroke-width="1.5" stroke-dasharray="3"/>
        <text x="376" y="138" fill="#16a06a" font-size="10" font-weight="700">Vegetative Nucleus</text>
        <text x="376" y="150" fill="#16a06a" font-size="9">Large; food reserve</text>

        <line x1="295" y1="120" x2="373" y2="170" stroke="#d97706" stroke-width="1.5" stroke-dasharray="3"/>
        <text x="376" y="172" fill="#d97706" font-size="10" font-weight="700">Aperture (Colpus/Pore)</text>
        <text x="376" y="184" fill="#92400e" font-size="9">Sporopollenin absent here</text>

        <text x="10" y="200" fill="#6d28d9" font-size="10" font-style="italic" font-weight="600">★ In grasses/composites: 3-celled pollen (generative cell divides before shedding → 2 male gametes)</text>
      </svg>
    </div>

    <!-- BULB TRIVIA -->
    <div class="bulb-trivia" onclick="toggleBulb(this)">
      <div class="bulb-header">
        <div class="bulb-icon">
          <svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg">
            <path d="M20 5 C13 5 8 10 8 17 C8 22 11 25 14 27 L14 31 C14 32.1 14.9 33 16 33 L24 33 C25.1 33 26 32.1 26 31 L26 27 C29 25 32 22 32 17 C32 10 27 5 20 5 Z" fill="#f59e0b" stroke="#d97706" stroke-width="1.5"/>
            <rect x="16" y="33" width="8" height="3" rx="1.5" fill="#92400e"/>
          </svg>
        </div>
        <div class="bulb-label">NEET + Allen Trivia<span>High-yield facts for Stamen & Pollen</span></div>
        <div class="bulb-arrow">▼</div>
      </div>
      <div class="bulb-body">
        <ul>
          <li><strong>Tapetum</strong>: innermost anther wall; nutritive; multinucleate/polyploid (2n or 4n); provides sporopollenin precursors, pollenkitt, ubisch bodies. <span class="neet-tag">NEET</span></li>
          <li><strong>Endothecium</strong>: fibrous thickenings (hygroscopic) → helps in anther dehiscence (opening). <span class="neet-tag">Allen</span></li>
          <li><strong>Sporopollenin</strong>: most resistant organic compound known; found in exine of pollen; not degraded by any enzyme; absent at apertures (colpi/pores). <span class="neet-tag">NEET</span></li>
          <li>Pollen viability: <strong>30 min</strong> (rice, wheat) vs <strong>months</strong> (Rosaceae, Leguminosae). Pollen stored in <strong>liquid nitrogen at −196°C</strong> (pollen banks). <span class="neet-tag">NEET</span></li>
          <li><strong>Pollenkitt</strong> = lipid-rich sticky coat → secreted by tapetum → aids insect pollination.</li>
          <li>Pollen allergy → <strong>pollinosis</strong>. Highly allergenic: <em>Parthenium</em> (carrot grass), <em>Amaranthus</em>, <em>Chenopodium</em>. <span class="neet-tag">Allen</span></li>
          <li>1 MMC → 4 microspores (meiosis). 1 microsporangium → many MMCs → many pollen grains.</li>
          <li><strong>Ubisch bodies</strong> (orbicules): small sporopollenin bodies secreted by tapetum onto inner anther wall.</li>
        </ul>
      </div>
    </div>

    <div class="mcq-section">
      <div class="mcq-section-header">
        <h3>Practice Questions</h3>
        <span class="mcq-badge">3 MCQs · Boards + NEET</span>
      </div>

      <div class="mcq-item" id="s-q1">
        <div class="q-num">Q 1 · Stamen & Pollen</div>
        <div class="q">The innermost layer of the anther wall, which nourishes the developing pollen grains, is: <span class="pyq-tag">NEET 2019</span></div>
        <div class="mcq-options">
          <button class="mcq-opt" onclick="answerMCQ('s-q1',this,false)">A. Epidermis</button>
          <button class="mcq-opt" onclick="answerMCQ('s-q1',this,false)">B. Endothecium</button>
          <button class="mcq-opt" onclick="answerMCQ('s-q1',this,false)">C. Middle layers</button>
          <button class="mcq-opt" onclick="answerMCQ('s-q1',this,true)">D. Tapetum</button>
        </div>
        <div class="mcq-ans">✓ Tapetum — Innermost nutritive layer; cells are multinucleate/polyploid; secretes sporopollenin precursors, pollenkitt & ubisch bodies. Highest metabolic activity in anther.</div>
      </div>

      <div class="mcq-item" id="s-q2">
        <div class="q-num">Q 2 · Stamen & Pollen</div>
        <div class="q">Sporopollenin is a constituent of: <span class="pyq-tag">NEET 2014</span></div>
        <div class="mcq-options">
          <button class="mcq-opt" onclick="answerMCQ('s-q2',this,true)">A. Exine of pollen grain</button>
          <button class="mcq-opt" onclick="answerMCQ('s-q2',this,false)">B. Intine of pollen grain</button>
          <button class="mcq-opt" onclick="answerMCQ('s-q2',this,false)">C. Pollen tube wall</button>
          <button class="mcq-opt" onclick="answerMCQ('s-q2',this,false)">D. Testa of seed</button>
        </div>
        <div class="mcq-ans">✓ Exine — The outer wall of the pollen grain is made of sporopollenin, the most resistant organic compound. It cannot be degraded by any enzyme and is absent at apertures (colpi/pores).</div>
      </div>

      <div class="mcq-item" id="s-q3">
        <div class="q-num">Q 3 · Stamen & Pollen</div>
        <div class="q">A typical anther is called tetrasporangiate because it has: <span class="pyq-tag">Boards 2015</span></div>
        <div class="mcq-options">
          <button class="mcq-opt" onclick="answerMCQ('s-q3',this,false)">A. 2 microsporangia</button>
          <button class="mcq-opt" onclick="answerMCQ('s-q3',this,true)">B. 4 microsporangia</button>
          <button class="mcq-opt" onclick="answerMCQ('s-q3',this,false)">C. 4 microspores</button>
          <button class="mcq-opt" onclick="answerMCQ('s-q3',this,false)">D. 4 pollen grains</button>
        </div>
        <div class="mcq-ans">✓ 4 microsporangia — Anther is bilobed (2 lobes × 2 microsporangia per lobe = 4 total). Hence called tetrasporangiate. Each microsporangium contains MMCs that form pollen grains by meiosis.</div>
      </div>
    </div>

  </div>
</div>

<!-- ══════════════════════════════════════
     PAGE 4: PISTIL & OVULE
═══════════════════════════════════════ -->
<div class="page" id="page-pistil">
  <div class="page-header">
    <div class="page-num">Topic 4 of 8</div>
    <div class="page-title">Pistil, Ovule & Megasporogenesis</div>
    <div class="page-subtitle">Female Reproductive Organs · Embryo Sac (7-celled, 8-nucleate)</div>
  </div>
  <div class="container">

    <!-- Ovule Diagram -->
    <div class="diagram-box">
      <div class="diagram-label">NCERT Diagram — Anatropous Ovule (L.S.) + Embryo Sac</div>
      <svg viewBox="0 0 700 300" xmlns="http://www.w3.org/2000/svg" font-family="Outfit,sans-serif">
        <!-- Outer integument -->
        <ellipse cx="250" cy="140" rx="90" ry="115" fill="none" stroke="#16a06a" stroke-width="3"/>
        <!-- Inner integument -->
        <ellipse cx="250" cy="145" rx="70" ry="95" fill="none" stroke="#0d6e4a" stroke-width="2.5"/>
        <!-- Nucellus -->
        <ellipse cx="250" cy="150" rx="52" ry="75" fill="#d0f5e5" stroke="#065f46" stroke-width="2"/>
        <!-- Embryo sac inside -->
        <ellipse cx="250" cy="135" rx="32" ry="55" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>

        <!-- Antipodal cells (chalazal) -->
        <circle cx="238" cy="85" r="8" fill="#6d28d9"/>
        <circle cx="252" cy="80" r="8" fill="#6d28d9"/>
        <circle cx="266" cy="87" r="8" fill="#6d28d9"/>
        <text x="250" y="72" fill="#6d28d9" text-anchor="middle" font-size="8" font-weight="700">Antipodal cells (3)</text>

        <!-- Polar nuclei (central cell) -->
        <circle cx="245" cy="125" r="7" fill="#0369a1"/>
        <circle cx="258" cy="133" r="7" fill="#0369a1"/>
        <text x="250" y="148" fill="#0369a1" text-anchor="middle" font-size="8" font-weight="700">Polar nuclei (2)</text>

        <!-- Egg apparatus -->
        <circle cx="250" cy="165" r="9" fill="#be123c" stroke="#9f1239" stroke-width="1.5"/>
        <circle cx="238" cy="177" r="7" fill="#f87171"/>
        <circle cx="262" cy="177" r="7" fill="#f87171"/>
        <text x="250" y="193" fill="#be123c" text-anchor="middle" font-size="8" font-weight="700">Egg apparatus (3)</text>

        <!-- Micropyle -->
        <path d="M230,220 Q250,230 270,220" stroke="#0d6e4a" stroke-width="2" fill="none"/>
        <text x="250" y="244" fill="#0d6e4a" text-anchor="middle" font-size="10" font-weight="700">Micropyle</text>

        <!-- Funicle -->
        <line x1="250" y1="255" x2="250" y2="290" stroke="#5a3e28" stroke-width="4"/>
        <text x="275" y="280" fill="#5a3e28" font-size="10" font-weight="600">Funicle</text>

        <!-- Hilum -->
        <ellipse cx="250" cy="255" rx="15" ry="6" fill="#8b5e3c"/>
        <text x="285" y="258" fill="#8b5e3c" font-size="9" font-weight="600">Hilum</text>

        <!-- Chalaza -->
        <ellipse cx="250" cy="50" rx="20" ry="8" fill="#15803d" opacity="0.7"/>
        <text x="250" y="53" fill="#fff" text-anchor="middle" font-size="8" font-weight="700">Chalaza</text>

        <!-- Labels right -->
        <line x1="340" y1="50" x2="268" y2="50" stroke="#15803d" stroke-width="1" stroke-dasharray="3"/>
        <text x="343" y="53" fill="#15803d" font-size="10" font-weight="700">Chalazal end</text>

        <line x1="340" y1="90" x2="310" y2="88" stroke="#0d6e4a" stroke-width="1" stroke-dasharray="3"/>
        <text x="343" y="93" fill="#0d6e4a" font-size="10" font-weight="700">Outer integument</text>

        <line x1="340" y1="110" x2="316" y2="118" stroke="#065f46" stroke-width="1" stroke-dasharray="3"/>
        <text x="343" y="113" fill="#065f46" font-size="10" font-weight="700">Inner integument</text>

        <line x1="340" y1="135" x2="302" y2="152" stroke="#065f46" stroke-width="1" stroke-dasharray="3"/>
        <text x="343" y="138" fill="#065f46" font-size="10" font-weight="700">Nucellus (2n)</text>

        <line x1="340" y1="158" x2="282" y2="138" stroke="#d97706" stroke-width="1" stroke-dasharray="3"/>
        <text x="343" y="161" fill="#d97706" font-size="10" font-weight="700">Embryo Sac (♀ gametophyte)</text>
        <text x="343" y="174" fill="#d97706" font-size="9">7 cells · 8 nuclei</text>

        <!-- Embryo sac detail right -->
        <rect x="430" y="20" width="250" height="200" rx="14" fill="#fffbeb" stroke="#fbbf24" stroke-width="2"/>
        <text x="555" y="42" fill="#92400e" text-anchor="middle" font-size="11" font-weight="800">Embryo Sac Structure</text>
        <text x="555" y="58" fill="#78350f" text-anchor="middle" font-size="9" font-weight="600">(Polygonum type — most common)</text>

        <circle cx="555" cy="80" r="6" fill="#6d28d9"/><circle cx="543" cy="80" r="6" fill="#6d28d9"/><circle cx="567" cy="80" r="6" fill="#6d28d9"/>
        <text x="555" y="100" fill="#6d28d9" text-anchor="middle" font-size="9" font-weight="700">3 Antipodal cells</text>
        <text x="555" y="111" fill="#6d28d9" text-anchor="middle" font-size="8">(chalazal end; degenerate)</text>

        <circle cx="548" cy="130" r="8" fill="#0369a1"/><circle cx="562" cy="130" r="8" fill="#0369a1"/>
        <text x="555" y="152" fill="#0369a1" text-anchor="middle" font-size="9" font-weight="700">2 Polar nuclei = Central cell</text>
        <text x="555" y="163" fill="#0369a1" text-anchor="middle" font-size="8">→ fuse → Secondary nucleus (2n)</text>

        <circle cx="555" cy="180" r="10" fill="#be123c" stroke="#9f1239" stroke-width="1.5"/>
        <circle cx="543" cy="190" r="7" fill="#f87171"/>
        <circle cx="567" cy="190" r="7" fill="#f87171"/>
        <text x="555" y="210" fill="#be123c" text-anchor="middle" font-size="9" font-weight="700">Egg (1) + Synergids (2)</text>
        <text x="555" y="222" fill="#9f1239" text-anchor="middle" font-size="8">= Egg apparatus; micropylar end</text>
      </svg>
    </div>

    <div class="section-title">Megasporogenesis</div>

    <div class="diagram-box">
      <div class="diagram-label">NCERT Diagram — Megasporogenesis → Embryo Sac Development</div>
      <svg viewBox="0 0 700 150" xmlns="http://www.w3.org/2000/svg" font-family="Outfit,sans-serif">
        <rect x="10" y="45" width="100" height="50" rx="10" fill="#0d6e4a"/>
        <text x="60" y="67" fill="#fff" text-anchor="middle" font-size="11" font-weight="700">MMC (2n)</text>
        <text x="60" y="82" fill="#c9ffe8" text-anchor="middle" font-size="9">in nucellus</text>

        <line x1="115" y1="70" x2="145" y2="70" stroke="#d97706" stroke-width="2" marker-end="url(#a3)"/>
        <text x="130" y="63" fill="#d97706" font-size="9" font-weight="700">Meiosis</text>

        <rect x="150" y="35" width="110" height="70" rx="10" fill="#16a06a"/>
        <text x="205" y="58" fill="#fff" text-anchor="middle" font-size="10" font-weight="700">Linear Tetrad</text>
        <text x="205" y="72" fill="#c9ffe8" text-anchor="middle" font-size="9">4 megaspores (n)</text>
        <text x="205" y="87" fill="#fde68a" text-anchor="middle" font-size="9">3 degenerate ✗</text>
        <text x="205" y="100" fill="#b9ffd9" text-anchor="middle" font-size="9">1 functional ★ (chalazal)</text>

        <line x1="265" y1="70" x2="295" y2="70" stroke="#6d28d9" stroke-width="2" marker-end="url(#a3)"/>
        <text x="280" y="63" fill="#6d28d9" font-size="9">3 mitosis</text>

        <rect x="300" y="30" width="130" height="80" rx="10" fill="#6d28d9"/>
        <text x="365" y="55" fill="#fff" text-anchor="middle" font-size="10" font-weight="700">Embryo Sac</text>
        <text x="365" y="70" fill="#e9d5ff" text-anchor="middle" font-size="9">7 cells, 8 nuclei</text>
        <text x="365" y="85" fill="#e9d5ff" text-anchor="middle" font-size="9">Monosporic development</text>
        <text x="365" y="100" fill="#fde68a" text-anchor="middle" font-size="9">(Polygonum type)</text>

        <line x1="435" y1="70" x2="465" y2="70" stroke="#0d6e4a" stroke-width="2" marker-end="url(#a3)"/>

        <rect x="468" y="25" width="210" height="90" rx="10" fill="#0f766e"/>
        <text x="573" y="48" fill="#fff" text-anchor="middle" font-size="10" font-weight="700">3 Antipodals + 2 Polars +</text>
        <text x="573" y="62" fill="#ccfbf1" text-anchor="middle" font-size="10">1 Egg + 2 Synergids</text>
        <text x="573" y="78" fill="#fde68a" text-anchor="middle" font-size="10">= 7 cells | 8 nuclei</text>
        <text x="573" y="96" fill="#ccfbf1" text-anchor="middle" font-size="9">(central cell has 2 polar nuclei)</text>

        <defs>
          <marker id="a3" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
            <path d="M0,0 L0,6 L8,3 z" fill="#0d6e4a"/>
          </marker>
        </defs>
      </svg>
    </div>

    <div class="info-box amber">
      <strong>Types of Ovules (Allen Module Favourite)</strong>
      <strong>Anatropous</strong> (most common in angiosperms — inverted, micropyle near funicle) | <strong>Orthotropous</strong> (erect, hilum-micropyle-chalaza in line; Polygonum) | <strong>Campylotropous</strong> (curved body) | <strong>Amphitropous</strong> (half-inverted) | <strong>Circinotropous</strong> (funicle coils around ovule)
    </div>

    <!-- BULB TRIVIA -->
    <div class="bulb-trivia" onclick="toggleBulb(this)">
      <div class="bulb-header">
        <div class="bulb-icon">
          <svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg">
            <path d="M20 5 C13 5 8 10 8 17 C8 22 11 25 14 27 L14 31 C14 32.1 14.9 33 16 33 L24 33 C25.1 33 26 32.1 26 31 L26 27 C29 25 32 22 32 17 C32 10 27 5 20 5 Z" fill="#f59e0b" stroke="#d97706" stroke-width="1.5"/>
            <rect x="16" y="33" width="8" height="3" rx="1.5" fill="#92400e"/>
          </svg>
        </div>
        <div class="bulb-label">NEET + Allen Trivia<span>High-yield facts for Pistil, Ovule & Embryo Sac</span></div>
        <div class="bulb-arrow">▼</div>
      </div>
      <div class="bulb-body">
        <ul>
          <li>Embryo sac = <strong>7 cells, 8 nuclei</strong> — most repeated NEET fact ever. <span class="neet-tag">NEET</span></li>
          <li><strong>Synergids</strong> have <strong>filiform apparatus</strong> at micropylar end → guides pollen tube by secreting chemotropic substances. <span class="neet-tag">NEET</span></li>
          <li>Polar nuclei: 2 (one from each pole) fuse → <strong>secondary nucleus (2n)</strong>; secondary nucleus + male gamete = PEN (3n).</li>
          <li><strong>Antipodal cells</strong>: ephemeral (degenerate after fertilisation); no direct role in fertilisation. <span class="neet-tag">Allen</span></li>
          <li>Most common ovule = <strong>anatropous</strong>. Orthotropous found in Polygonum, Piperaceae.</li>
          <li><strong>Perisperm</strong> = persistent nucellus → found in: beet, black pepper (<em>Piper nigrum</em>), coffee. <span class="neet-tag">NEET</span></li>
          <li>Bitegmic ovule = 2 integuments (most angiosperms). Unitegmic = 1 integument (Asteraceae, Gamopetalae).</li>
          <li>Megasporogenesis: Functional megaspore = <strong>always chalazal</strong>. 3 mitotic divisions → 8-nucleate embryo sac.</li>
          <li><strong>Bisporic</strong> (Allium type); <strong>Tetrasporic</strong> (Peperomia/Drusa type) — Allen module asked these!</li>
        </ul>
      </div>
    </div>

    <div class="mcq-section">
      <div class="mcq-section-header">
        <h3>Practice Questions</h3>
        <span class="mcq-badge">3 MCQs · Boards + NEET</span>
      </div>

      <div class="mcq-item" id="p-q1">
        <div class="q-num">Q 1 · Pistil & Ovule</div>
        <div class="q">The number of cells and nuclei in a mature embryo sac of angiosperm are respectively: <span class="pyq-tag">NEET 2013</span></div>
        <div class="mcq-options">
          <button class="mcq-opt" onclick="answerMCQ('p-q1',this,true)">A. 7 cells, 8 nuclei</button>
          <button class="mcq-opt" onclick="answerMCQ('p-q1',this,false)">B. 8 cells, 8 nuclei</button>
          <button class="mcq-opt" onclick="answerMCQ('p-q1',this,false)">C. 7 cells, 7 nuclei</button>
          <button class="mcq-opt" onclick="answerMCQ('p-q1',this,false)">D. 6 cells, 8 nuclei</button>
        </div>
        <div class="mcq-ans">✓ 7 cells, 8 nuclei — 3 egg apparatus + 1 central cell (with 2 polar nuclei) + 3 antipodals = 7 cells. Central cell has 2 nuclei → total 8 nuclei.</div>
      </div>

      <div class="mcq-item" id="p-q2">
        <div class="q-num">Q 2 · Pistil & Ovule</div>
        <div class="q">The most common type of ovule found in angiosperms is: <span class="pyq-tag">Boards 2016</span></div>
        <div class="mcq-options">
          <button class="mcq-opt" onclick="answerMCQ('p-q2',this,false)">A. Orthotropous</button>
          <button class="mcq-opt" onclick="answerMCQ('p-q2',this,true)">B. Anatropous</button>
          <button class="mcq-opt" onclick="answerMCQ('p-q2',this,false)">C. Campylotropous</button>
          <button class="mcq-opt" onclick="answerMCQ('p-q2',this,false)">D. Amphitropous</button>
        </div>
        <div class="mcq-ans">✓ Anatropous — The inverted ovule where the micropyle lies close to the funicle (hilum). It is the most common type of ovule in angiosperms.</div>
      </div>

      <div class="mcq-item" id="p-q3">
        <div class="q-num">Q 3 · Pistil & Ovule</div>
        <div class="q">Filiform apparatus is a characteristic feature of: <span class="pyq-tag">NEET 2017</span></div>
        <div class="mcq-options">
          <button class="mcq-opt" onclick="answerMCQ('p-q3',this,false)">A. Antipodal cells</button>
          <button class="mcq-opt" onclick="answerMCQ('p-q3',this,false)">B. Egg cell</button>
          <button class="mcq-opt" onclick="answerMCQ('p-q3',this,true)">C. Synergids</button>
          <button class="mcq-opt" onclick="answerMCQ('p-q3',this,false)">D. Central cell</button>
        </div>
        <div class="mcq-ans">✓ Synergids — The filiform apparatus at the micropylar end of synergids guides the pollen tube by secreting chemotropic substances. One synergid degenerates after pollen tube entry.</div>
      </div>
    </div>

  </div>
</div>

<!-- ══════════════════════════════════════
     PAGE 5: POLLINATION
═══════════════════════════════════════ -->
<div class="page" id="page-pollination">
  <div class="page-header">
    <div class="page-num">Topic 5 of 8</div>
    <div class="page-title">Pollination</div>
    <div class="page-subtitle">Types of Pollination · Agents · Outbreeding Devices</div>
  </div>
  <div class="container">

    <div class="card">
      <p><span class="key">Pollination</span> = Transfer of pollen grains from the <strong>anther</strong> to the <strong>stigma</strong> of a flower. It is <strong>NOT fertilisation</strong>. Pollination is a prerequisite for fertilisation in most angiosperms.</p>
    </div>

    <div class="section-title">Types of Pollination</div>
    <div class="grid-3">
      <div class="mini-card">
        <div class="accent-bar" style="background:linear-gradient(90deg,#0d6e4a,#1ecc87)"></div>
        <h4>Autogamy (Self)</h4>
        <p>Pollen transfers to stigma of <strong>same flower</strong>. Requires bisexual flower. Cleistogamous flowers = obligate autogamy (Viola, Oxalis, Commelina).</p>
      </div>
      <div class="mini-card sky">
        <div class="accent-bar" style="background:linear-gradient(90deg,#0369a1,#38bdf8)"></div>
        <h4>Geitonogamy</h4>
        <p>Pollen to <strong>another flower</strong> of <strong>same plant</strong>. Functionally cross-pollination (needs pollinator). Genetically = self-pollination (same genome).</p>
      </div>
      <div class="mini-card rose">
        <div class="accent-bar" style="background:linear-gradient(90deg,#be123c,#fb7185)"></div>
        <h4>Xenogamy (Cross)</h4>
        <p>Pollen to <strong>different plant</strong> (same species). True cross-pollination. Promotes genetic variation — evolutionarily beneficial.</p>
      </div>
    </div>

    <!-- Pollination Agents Diagram -->
    <div class="diagram-box">
      <div class="diagram-label">Allen Diagram — Agents of Pollination & Their Flower Features</div>
      <svg viewBox="0 0 700 220" xmlns="http://www.w3.org/2000/svg" font-family="Outfit,sans-serif">
        <!-- Central hub -->
        <circle cx="350" cy="110" r="45" fill="#0d6e4a"/>
        <text x="350" y="105" fill="#fff" text-anchor="middle" font-size="12" font-weight="800">Agents of</text>
        <text x="350" y="122" fill="#b9ffd9" text-anchor="middle" font-size="11" font-weight="700">Pollination</text>

        <!-- Wind -->
        <rect x="20" y="15" width="130" height="80" rx="12" fill="#bae6fd" stroke="#0369a1" stroke-width="2"/>
        <text x="85" y="38" fill="#0369a1" text-anchor="middle" font-size="12" font-weight="800">💨 Wind</text>
        <text x="85" y="53" fill="#0c4a6e" text-anchor="middle" font-size="9" font-weight="600">Anemophily</text>
        <text x="85" y="67" fill="#075985" text-anchor="middle" font-size="8">Light, non-sticky pollen</text>
        <text x="85" y="79" fill="#075985" text-anchor="middle" font-size="8">Feathery stigma; no nectar</text>
        <text x="85" y="91" fill="#0369a1" text-anchor="middle" font-size="8" font-weight="700">Maize, Date palm, Grasses</text>
        <line x1="150" y1="55" x2="308" y2="90" stroke="#0369a1" stroke-width="1.5" stroke-dasharray="4"/>

        <!-- Insects -->
        <rect x="20" y="125" width="130" height="85" rx="12" fill="#fef9c3" stroke="#d97706" stroke-width="2"/>
        <text x="85" y="148" fill="#d97706" text-anchor="middle" font-size="12" font-weight="800">🐝 Insect</text>
        <text x="85" y="163" fill="#92400e" text-anchor="middle" font-size="9" font-weight="600">Entomophily</text>
        <text x="85" y="177" fill="#78350f" text-anchor="middle" font-size="8">Sticky, spiny pollen</text>
        <text x="85" y="189" fill="#78350f" text-anchor="middle" font-size="8">Bright, fragrant; nectar</text>
        <text x="85" y="201" fill="#d97706" text-anchor="middle" font-size="8" font-weight="700">Rose, Salvia, most angiosperms</text>
        <line x1="150" y1="168" x2="308" y2="130" stroke="#d97706" stroke-width="1.5" stroke-dasharray="4"/>

        <!-- Water -->
        <rect x="555" y="15" width="135" height="80" rx="12" fill="#ccfbf1" stroke="#0f766e" stroke-width="2"/>
        <text x="622" y="38" fill="#0f766e" text-anchor="middle" font-size="12" font-weight="800">💧 Water</text>
        <text x="622" y="53" fill="#065f46" text-anchor="middle" font-size="9" font-weight="600">Hydrophily</text>
        <text x="622" y="67" fill="#065f46" text-anchor="middle" font-size="8">Pollen protected by mucilage</text>
        <text x="622" y="79" fill="#065f46" text-anchor="middle" font-size="8">Ribbon-like pollen; no exine</text>
        <text x="622" y="91" fill="#0f766e" text-anchor="middle" font-size="8" font-weight="700">Zostera, Vallisneria, Hydrilla</text>
        <line x1="555" y1="55" x2="392" y2="90" stroke="#0f766e" stroke-width="1.5" stroke-dasharray="4"/>

        <!-- Birds -->
        <rect x="555" y="125" width="135" height="85" rx="12" fill="#ffe4ec" stroke="#be123c" stroke-width="2"/>
        <text x="622" y="148" fill="#be123c" text-anchor="middle" font-size="12" font-weight="800">🦜 Bird</text>
        <text x="622" y="163" fill="#9f1239" text-anchor="middle" font-size="9" font-weight="600">Ornithophily</text>
        <text x="622" y="177" fill="#9f1239" text-anchor="middle" font-size="8">Bright red/orange; tubular</text>
        <text x="622" y="189" fill="#9f1239" text-anchor="middle" font-size="8">Nectar at base; odourless</text>
        <text x="622" y="201" fill="#be123c" text-anchor="middle" font-size="8" font-weight="700">Bignonia, Bombax, Erythrina</text>
        <line x1="555" y1="168" x2="392" y2="130" stroke="#be123c" stroke-width="1.5" stroke-dasharray="4"/>
      </svg>
    </div>

    <div class="section-title">Outbreeding Devices</div>
    <div class="grid-2">
      <div class="mini-card teal">
        <h4>Dichogamy</h4>
        <p><strong>Protandry</strong>: anthers mature before stigma (sunflower, Salvia, maize) | <strong>Protogyny</strong>: stigma matures before anthers (Mirabilis, magnolia)</p>
      </div>
      <div class="mini-card violet">
        <h4>Self-Incompatibility (SI)</h4>
        <p>Genetic mechanism — prevents pollen from same plant germinating on stigma. Most common outbreeding device. Prevents inbreeding.</p>
      </div>
      <div class="mini-card amber">
        <h4>Herkogamy</h4>
        <p>Physical barrier between anther & stigma prevents self-pollination. E.g., long style in some flowers.</p>
      </div>
      <div class="mini-card rose">
        <h4>Dioecy</h4>
        <p>♂ & ♀ on different plants — ensures cross-pollination. Eg: Papaya, Date palm, Hemp (Cannabis).</p>
      </div>
    </div>

    <div class="info-box teal">
      <strong>Artificial Hybridisation (Boards — Important)</strong>
      Steps: <strong>Emasculation</strong> (removal of anthers from bisexual flower before pollen maturity) → <strong>Bagging</strong> (covering with butter-paper bag to prevent contamination) → collect desired pollen → dust on bagged emasculated flower → re-bag. Used in plant breeding to create new varieties.
    </div>

    <!-- BULB TRIVIA -->
    <div class="bulb-trivia" onclick="toggleBulb(this)">
      <div class="bulb-header">
        <div class="bulb-icon">
          <svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg">
            <path d="M20 5 C13 5 8 10 8 17 C8 22 11 25 14 27 L14 31 C14 32.1 14.9 33 16 33 L24 33 C25.1 33 26 32.1 26 31 L26 27 C29 25 32 22 32 17 C32 10 27 5 20 5 Z" fill="#f59e0b" stroke="#d97706" stroke-width="1.5"/>
            <rect x="16" y="33" width="8" height="3" rx="1.5" fill="#92400e"/>
          </svg>
        </div>
        <div class="bulb-label">NEET + Allen Trivia<span>High-yield facts for Pollination</span></div>
        <div class="bulb-arrow">▼</div>
      </div>
      <div class="bulb-body">
        <ul>
          <li><strong>Cleistogamy</strong> = obligate autogamy; flowers never open. Eg: <em>Viola</em> (pansy), <em>Oxalis</em>, <em>Commelina</em>. Advantage: seed production even without pollinators. <span class="neet-tag">NEET</span></li>
          <li><strong>Chasmogamous</strong> = open flowers (normal); can undergo cross or self-pollination.</li>
          <li><strong>Vallisneria</strong> = epihydrophily (surface water pollination) — ♀ flower floats, ♂ pollen floats to it.</li>
          <li><strong>Zostera</strong> = hypohydrophily (submerged); pollen ribbon-like, no sporopollenin in exine. <span class="neet-tag">NEET</span></li>
          <li><strong>Salvia</strong> uses lever mechanism (modification of stamens) for insect pollination — a classic Allen module example. <span class="neet-tag">Allen</span></li>
          <li><strong>Yucca moth</strong> (<em>Pronuba</em>) & <em>Yucca</em> plant — obligate mutualism; neither can reproduce without the other. <span class="neet-tag">Allen</span></li>
          <li>Most wind-pollinated flowers: small, inconspicuous, no nectar/fragrance, large amounts of pollen (compensate for wastage).</li>
          <li><strong>Heterostyly</strong>: different style lengths in same species (Primrose) — promotes cross-pollination.</li>
        </ul>
      </div>
    </div>

    <div class="mcq-section">
      <div class="mcq-section-header">
        <h3>Practice Questions</h3>
        <span class="mcq-badge">3 MCQs · Boards + NEET</span>
      </div>

      <div class="mcq-item" id="po-q1">
        <div class="q-num">Q 1 · Pollination</div>
        <div class="q">Which of the following flowers shows cleistogamy? <span class="pyq-tag">NEET 2020</span></div>
        <div class="mcq-options">
          <button class="mcq-opt" onclick="answerMCQ('po-q1',this,false)">A. Salvia</button>
          <button class="mcq-opt" onclick="answerMCQ('po-q1',this,true)">B. Viola</button>
          <button class="mcq-opt" onclick="answerMCQ('po-q1',this,false)">C. Vallisneria</button>
          <button class="mcq-opt" onclick="answerMCQ('po-q1',this,false)">D. Maize</button>
        </div>
        <div class="mcq-ans">✓ Viola — Also Oxalis and Commelina. Cleistogamous flowers never open, ensuring obligate self-pollination. Advantage: seed production even in absence of pollinators.</div>
      </div>

      <div class="mcq-item" id="po-q2">
        <div class="q-num">Q 2 · Pollination</div>
        <div class="q">In Zostera, pollination occurs by: <span class="pyq-tag">Boards 2018</span></div>
        <div class="mcq-options">
          <button class="mcq-opt" onclick="answerMCQ('po-q2',this,false)">A. Wind</button>
          <button class="mcq-opt" onclick="answerMCQ('po-q2',this,false)">B. Insects</button>
          <button class="mcq-opt" onclick="answerMCQ('po-q2',this,true)">C. Submerged water (hypohydrophily)</button>
          <button class="mcq-opt" onclick="answerMCQ('po-q2',this,false)">D. Surface water (epihydrophily)</button>
        </div>
        <div class="mcq-ans">✓ Hypohydrophily — Zostera is a sea grass; pollination occurs underwater. Pollen grains are elongated ribbon-like, with no exine (sporopollenin absent). Vallisneria shows epihydrophily (surface).</div>
      </div>

      <div class="mcq-item" id="po-q3">
        <div class="q-num">Q 3 · Pollination</div>
        <div class="q">Artificial hybridisation involves the following two steps in correct order: <span class="pyq-tag">Boards 2021</span></div>
        <div class="mcq-options">
          <button class="mcq-opt" onclick="answerMCQ('po-q3',this,false)">A. Bagging → Emasculation</button>
          <button class="mcq-opt" onclick="answerMCQ('po-q3',this,true)">B. Emasculation → Bagging</button>
          <button class="mcq-opt" onclick="answerMCQ('po-q3',this,false)">C. Bagging → Crossing only</button>
          <button class="mcq-opt" onclick="answerMCQ('po-q3',this,false)">D. Pollination → Emasculation</button>
        </div>
        <div class="mcq-ans">✓ Emasculation first, then Bagging — First remove stamens (emasculation) before pollen matures, then bag the flower to prevent contamination. Later apply desired pollen and re-bag.</div>
      </div>
    </div>

  </div>
</div>

<!-- ══════════════════════════════════════
     PAGE 6: FERTILISATION
═══════════════════════════════════════ -->
<div class="page" id="page-fertilisation">
  <div class="page-header">
    <div class="page-num">Topic 6 of 8</div>
    <div class="page-title">Pollen–Pistil Interaction & Double Fertilisation</div>
    <div class="page-subtitle">Pollen Tube Growth · Syngamy · Triple Fusion · Post-Fertilisation</div>
  </div>
  <div class="container">

    <!-- Double Fertilisation Diagram -->
    <div class="diagram-box">
      <div class="diagram-label">NCERT Diagram — Double Fertilisation in Angiosperm</div>
      <svg viewBox="0 0 700 280" xmlns="http://www.w3.org/2000/svg" font-family="Outfit,sans-serif">
        <!-- Embryo Sac outline -->
        <ellipse cx="400" cy="140" rx="150" ry="110" fill="#fffbeb" stroke="#d97706" stroke-width="2.5"/>
        <text x="400" y="22" fill="#d97706" text-anchor="middle" font-size="10" font-weight="700">EMBRYO SAC</text>

        <!-- Synergids -->
        <circle cx="370" cy="195" r="15" fill="#fb923c" stroke="#d97706" stroke-width="1.5"/>
        <circle cx="400" cy="205" r="15" fill="#fb923c" stroke="#d97706" stroke-width="1.5"/>
        <text x="385" y="228" fill="#c2410c" text-anchor="middle" font-size="9" font-weight="700">Synergids</text>

        <!-- Egg cell -->
        <circle cx="435" cy="195" r="18" fill="#be123c" stroke="#9f1239" stroke-width="2"/>
        <text x="435" y="198" fill="#fff" text-anchor="middle" font-size="9" font-weight="700">Egg (n)</text>

        <!-- Polar nuclei -->
        <circle cx="388" cy="140" r="13" fill="#0369a1"/>
        <circle cx="413" cy="135" r="13" fill="#0369a1"/>
        <text x="400" y="120" fill="#0369a1" text-anchor="middle" font-size="9" font-weight="700">2 Polar nuclei</text>
        <text x="400" y="167" fill="#0369a1" text-anchor="middle" font-size="9">Secondary nucleus (2n)</text>

        <!-- Antipodals -->
        <circle cx="380" cy="80" r="9" fill="#6d28d9"/>
        <circle cx="400" cy="72" r="9" fill="#6d28d9"/>
        <circle cx="420" cy="80" r="9" fill="#6d28d9"/>
        <text x="400" y="60" fill="#6d28d9" text-anchor="middle" font-size="9" font-weight="700">Antipodals (3)</text>

        <!-- Pollen tube entering -->
        <line x1="100" y1="200" x2="340" y2="200" stroke="#16a06a" stroke-width="4" stroke-dasharray="6"/>
        <text x="200" y="192" fill="#16a06a" text-anchor="middle" font-size="10" font-weight="700">Pollen Tube</text>
        <text x="200" y="210" fill="#065f46" text-anchor="middle" font-size="9">through micropyle</text>

        <!-- Male gametes -->
        <circle cx="340" cy="200" r="10" fill="#1ecc87" stroke="#0d6e4a" stroke-width="2"/>
        <text x="340" y="204" fill="#fff" text-anchor="middle" font-size="8" font-weight="700">♂1</text>
        <circle cx="315" cy="200" r="10" fill="#0f766e" stroke="#0d6e4a" stroke-width="2"/>
        <text x="315" y="204" fill="#fff" text-anchor="middle" font-size="8" font-weight="700">♂2</text>

        <!-- Syngamy arrow -->
        <path d="M350,200 Q380,195 418,195" stroke="#be123c" stroke-width="2.5" fill="none" marker-end="url(#a4)"/>
        <text x="390" y="185" fill="#be123c" text-anchor="middle" font-size="9" font-weight="800">SYNGAMY</text>
        <text x="390" y="245" fill="#be123c" text-anchor="middle" font-size="8">♂1(n) + Egg(n) = Zygote(2n)</text>

        <!-- Triple fusion arrow -->
        <path d="M325,195 Q350,160 380,145" stroke="#0369a1" stroke-width="2.5" fill="none" marker-end="url(#a4)"/>
        <text x="320" y="165" fill="#0369a1" text-anchor="middle" font-size="9" font-weight="800">TRIPLE FUSION</text>
        <text x="320" y="180" fill="#0369a1" text-anchor="middle" font-size="8">♂2(n) + 2 polar(n+n) = PEN(3n)</text>

        <!-- Products -->
        <rect x="480" y="175" width="120" height="40" rx="8" fill="#be123c"/>
        <text x="540" y="193" fill="#fff" text-anchor="middle" font-size="9" font-weight="700">Zygote (2n)</text>
        <text x="540" y="208" fill="#fecdd3" text-anchor="middle" font-size="8">→ Embryo</text>

        <rect x="480" y="110" width="120" height="40" rx="8" fill="#0369a1"/>
        <text x="540" y="128" fill="#fff" text-anchor="middle" font-size="9" font-weight="700">PEN (3n)</text>
        <text x="540" y="143" fill="#bae6fd" text-anchor="middle" font-size="8">→ Endosperm</text>

        <line x1="455" y1="193" x2="478" y2="193" stroke="#be123c" stroke-width="1.5" marker-end="url(#a4)"/>
        <line x1="425" y1="138" x2="478" y2="130" stroke="#0369a1" stroke-width="1.5" marker-end="url(#a4)"/>

        <!-- Double fertilisation label -->
        <text x="540" y="260" fill="#d97706" text-anchor="middle" font-size="10" font-weight="800">= DOUBLE FERTILISATION</text>
        <text x="540" y="274" fill="#92400e" text-anchor="middle" font-size="8">(Syngamy + Triple Fusion together)</text>

        <!-- Micropyle label -->
        <text x="130" y="225" fill="#0d6e4a" font-size="9">← Micropyle end</text>

        <defs>
          <marker id="a4" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
            <path d="M0,0 L0,6 L8,3 z" fill="#0d6e4a"/>
          </marker>
        </defs>
      </svg>
    </div>

    <div class="section-title">Post-Fertilisation: What becomes What?</div>
    <div class="table-wrap">
      <table>
        <tr><th>Structure Before</th><th>Develops Into</th><th>Ploidy</th></tr>
        <tr><td>Zygote (syngamy)</td><td><strong>Embryo</strong></td><td>2n</td></tr>
        <tr><td>PEN (triple fusion)</td><td><strong>Endosperm</strong></td><td>3n (mostly)</td></tr>
        <tr><td>Ovule</td><td><strong>Seed</strong></td><td>—</td></tr>
        <tr><td>Ovary</td><td><strong>Fruit</strong></td><td>—</td></tr>
        <tr><td>Outer integument</td><td><strong>Testa</strong></td><td>2n</td></tr>
        <tr><td>Inner integument</td><td><strong>Tegmen</strong></td><td>2n</td></tr>
        <tr><td>Nucellus (if persistent)</td><td><strong>Perisperm</strong></td><td>2n</td></tr>
      </table>
    </div>

    <div class="info-box blue">
      <strong>Pollen Tube Entry into Ovule</strong>
      <strong>Porogamy</strong> (through micropyle — most common in angiosperms) | <strong>Chalazogamy</strong> (through chalaza) → Casuarina, Betula | <strong>Mesogamy</strong> (through integument) → Cucurbita (pumpkin)
    </div>

    <!-- BULB TRIVIA -->
    <div class="bulb-trivia" onclick="toggleBulb(this)">
      <div class="bulb-header">
        <div class="bulb-icon">
          <svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg">
            <path d="M20 5 C13 5 8 10 8 17 C8 22 11 25 14 27 L14 31 C14 32.1 14.9 33 16 33 L24 33 C25.1 33 26 32.1 26 31 L26 27 C29 25 32 22 32 17 C32 10 27 5 20 5 Z" fill="#f59e0b" stroke="#d97706" stroke-width="1.5"/>
            <rect x="16" y="33" width="8" height="3" rx="1.5" fill="#92400e"/>
          </svg>
        </div>
        <div class="bulb-label">NEET + Allen Trivia<span>High-yield facts for Fertilisation</span></div>
        <div class="bulb-arrow">▼</div>
      </div>
      <div class="bulb-body">
        <ul>
          <li>Double fertilisation discovered by <strong>S.G. Nawaschin, 1898</strong> in <em>Lilium</em> and <em>Fritillaria</em>. <span class="neet-tag">NEET</span></li>
          <li><strong>Syngamy</strong> = karyogamy = fusion of male gamete (n) + egg (n) → Zygote (2n) → Embryo.</li>
          <li><strong>Triple fusion</strong>: male gamete (n) + 2 polar nuclei (n+n) = PEN (3n) → Endosperm (triploid in most). <span class="neet-tag">NEET</span></li>
          <li>Gymnosperms: <strong>NO double fertilisation</strong>. Endosperm in gymnosperms = haploid (pre-fertilisation female gametophyte). <span class="neet-tag">Allen</span></li>
          <li>Pollen tube contents entering embryo sac: <strong>vegetative nucleus + 2 male gametes</strong>; enters through 1 degenerated synergid.</li>
          <li><strong>Vegetative nucleus</strong> disintegrates after guiding the pollen tube to embryo sac.</li>
          <li>Chalazogamy was first discovered in <strong>Casuarina</strong> by Treub (1891). <span class="neet-tag">Allen</span></li>
        </ul>
      </div>
    </div>

    <div class="mcq-section">
      <div class="mcq-section-header">
        <h3>Practice Questions</h3>
        <span class="mcq-badge">3 MCQs · Boards + NEET</span>
      </div>

      <div class="mcq-item" id="fe-q1">
        <div class="q-num">Q 1 · Fertilisation</div>
        <div class="q">Double fertilisation was first observed by Nawaschin in: <span class="pyq-tag">NEET 2015</span></div>
        <div class="mcq-options">
          <button class="mcq-opt" onclick="answerMCQ('fe-q1',this,false)">A. Lilium and Rosa</button>
          <button class="mcq-opt" onclick="answerMCQ('fe-q1',this,true)">B. Lilium and Fritillaria</button>
          <button class="mcq-opt" onclick="answerMCQ('fe-q1',this,false)">C. Triticum and Oryza</button>
          <button class="mcq-opt" onclick="answerMCQ('fe-q1',this,false)">D. Capsella and Lilium</button>
        </div>
        <div class="mcq-ans">✓ Lilium and Fritillaria — S.G. Nawaschin in 1898 first observed double fertilisation in these two plants. It is a landmark discovery unique to angiosperms.</div>
      </div>

      <div class="mcq-item" id="fe-q2">
        <div class="q-num">Q 2 · Fertilisation</div>
        <div class="q">The ploidy of endosperm in a typical angiosperm is: <span class="pyq-tag">Boards 2022</span></div>
        <div class="mcq-options">
          <button class="mcq-opt" onclick="answerMCQ('fe-q2',this,false)">A. Haploid (n)</button>
          <button class="mcq-opt" onclick="answerMCQ('fe-q2',this,false)">B. Diploid (2n)</button>
          <button class="mcq-opt" onclick="answerMCQ('fe-q2',this,true)">C. Triploid (3n)</button>
          <button class="mcq-opt" onclick="answerMCQ('fe-q2',this,false)">D. Tetraploid (4n)</button>
        </div>
        <div class="mcq-ans">✓ Triploid (3n) — PEN = ♂ gamete (n) + 2 polar nuclei (n+n) = 3n. Therefore endosperm is triploid. Exception: Gymnosperms have haploid (n) endosperm.</div>
      </div>

      <div class="mcq-item" id="fe-q3">
        <div class="q-num">Q 3 · Fertilisation</div>
        <div class="q">Pollen tube entry through the integuments is known as: <span class="pyq-tag">NEET 2021</span></div>
        <div class="mcq-options">
          <button class="mcq-opt" onclick="answerMCQ('fe-q3',this,false)">A. Porogamy</button>
          <button class="mcq-opt" onclick="answerMCQ('fe-q3',this,false)">B. Chalazogamy</button>
          <button class="mcq-opt" onclick="answerMCQ('fe-q3',this,true)">C. Mesogamy</button>
          <button class="mcq-opt" onclick="answerMCQ('fe-q3',this,false)">D. Syngamy</button>
        </div>
        <div class="mcq-ans">✓ Mesogamy — Pollen tube enters through the integuments (Cucurbita/pumpkin). Porogamy = through micropyle (most common). Chalazogamy = through chalaza (Casuarina).</div>
      </div>
    </div>

  </div>
</div>

<!-- ══════════════════════════════════════
     PAGE 7: SEED & EMBRYO
═══════════════════════════════════════ -->
<div class="page" id="page-seed">
  <div class="page-header">
    <div class="page-num">Topic 7 of 8</div>
    <div class="page-title">Endosperm, Embryo Development & Seed</div>
    <div class="page-subtitle">Endosperm Types · Dicot vs Monocot Embryo · Fruit</div>
  </div>
  <div class="container">

    <!-- Embryo Diagram -->
    <div class="diagram-box">
      <div class="diagram-label">NCERT Diagram — Dicot vs Monocot Embryo Comparison</div>
      <svg viewBox="0 0 700 260" xmlns="http://www.w3.org/2000/svg" font-family="Outfit,sans-serif">
        <!-- Dicot -->
        <text x="170" y="22" fill="#0d6e4a" text-anchor="middle" font-size="13" font-weight="800">Dicot Embryo (e.g., Capsella)</text>

        <!-- Suspensor -->
        <rect x="153" y="220" width="34" height="30" rx="5" fill="#a3e635" stroke="#65a30d" stroke-width="1.5"/>
        <text x="170" y="240" fill="#365314" text-anchor="middle" font-size="8" font-weight="600">Suspensor</text>

        <!-- Hypocotyl -->
        <rect x="153" y="175" width="34" height="40" rx="5" fill="#4ade80" stroke="#16a34a" stroke-width="1.5"/>
        <text x="170" y="199" fill="#14532d" text-anchor="middle" font-size="8" font-weight="600">Hypocotyl</text>

        <!-- Radicle -->
        <ellipse cx="170" cy="165" rx="20" ry="9" fill="#fb923c" stroke="#ea580c" stroke-width="1.5"/>
        <text x="170" y="168" fill="#fff" text-anchor="middle" font-size="8" font-weight="700">Radicle</text>

        <!-- Cotyledons -->
        <ellipse cx="145" cy="115" rx="28" ry="20" fill="#22c55e" stroke="#15803d" stroke-width="1.5"/>
        <ellipse cx="195" cy="115" rx="28" ry="20" fill="#22c55e" stroke="#15803d" stroke-width="1.5"/>
        <text x="145" y="118" fill="#fff" text-anchor="middle" font-size="8" font-weight="700">Cot. 1</text>
        <text x="195" y="118" fill="#fff" text-anchor="middle" font-size="8" font-weight="700">Cot. 2</text>

        <!-- Epicotyl -->
        <rect x="158" y="85" width="24" height="25" rx="4" fill="#0d6e4a" stroke="#065f46" stroke-width="1.5"/>
        <text x="170" y="101" fill="#fff" text-anchor="middle" font-size="8" font-weight="600">Epicotyl</text>

        <!-- Plumule -->
        <ellipse cx="170" cy="78" rx="16" ry="9" fill="#be123c" stroke="#9f1239" stroke-width="1.5"/>
        <text x="170" y="81" fill="#fff" text-anchor="middle" font-size="8" font-weight="700">Plumule</text>

        <!-- labels -->
        <text x="30" y="100" fill="#0d6e4a" font-size="9">2 Cotyledons</text>
        <text x="30" y="115" fill="#6b7280" font-size="8">(seed leaves)</text>
        <text x="30" y="165" fill="#ea580c" font-size="9">Radicle</text>
        <text x="30" y="195" fill="#16a34a" font-size="9">Hypocotyl</text>
        <text x="30" y="240" fill="#65a30d" font-size="9">Suspensor</text>

        <!-- Divider -->
        <line x1="350" y1="20" x2="350" y2="260" stroke="#d1fae5" stroke-width="2" stroke-dasharray="6"/>

        <!-- Monocot -->
        <text x="530" y="22" fill="#0369a1" text-anchor="middle" font-size="13" font-weight="800">Monocot Embryo (e.g., Maize)</text>

        <!-- Coleorhiza -->
        <rect x="510" y="220" width="40" height="28" rx="5" fill="#fed7aa" stroke="#d97706" stroke-width="1.5"/>
        <text x="530" y="237" fill="#92400e" text-anchor="middle" font-size="8" font-weight="600">Coleorhiza</text>

        <!-- Radicle -->
        <ellipse cx="530" cy="213" rx="16" ry="7" fill="#fb923c" stroke="#ea580c" stroke-width="1.5"/>
        <text x="530" y="216" fill="#fff" text-anchor="middle" font-size="7" font-weight="700">Radicle</text>

        <!-- Scutellum (cotyledon) -->
        <ellipse cx="555" cy="150" rx="40" ry="55" fill="#22c55e" stroke="#15803d" stroke-width="2" opacity="0.85"/>
        <text x="555" y="147" fill="#fff" text-anchor="middle" font-size="10" font-weight="800">Scutellum</text>
        <text x="555" y="162" fill="#d0fce8" text-anchor="middle" font-size="8">(1 cotyledon)</text>

        <!-- Coleoptile -->
        <rect x="507" y="145" width="28" height="45" rx="5" fill="#0369a1" stroke="#0c4a6e" stroke-width="1.5"/>
        <text x="521" y="162" fill="#fff" text-anchor="middle" font-size="8" font-weight="600">Coleo-</text>
        <text x="521" y="174" fill="#fff" text-anchor="middle" font-size="8" font-weight="600">ptile</text>

        <!-- Plumule -->
        <ellipse cx="521" cy="138" rx="14" ry="8" fill="#be123c" stroke="#9f1239" stroke-width="1.5"/>
        <text x="521" y="141" fill="#fff" text-anchor="middle" font-size="7" font-weight="700">Plumule</text>

        <!-- Right labels -->
        <text x="620" y="148" fill="#22c55e" font-size="9">1 Cotyledon</text>
        <text x="620" y="163" fill="#6b7280" font-size="8">(Scutellum)</text>
        <text x="620" y="178" fill="#0369a1" font-size="9">Coleoptile</text>
        <text x="620" y="215" fill="#ea580c" font-size="9">Coleorhiza</text>
      </svg>
    </div>

    <div class="section-title">Types of Endosperm Development</div>
    <div class="grid-2">
      <div class="mini-card">
        <div class="accent-bar" style="background:linear-gradient(90deg,#0d6e4a,#1ecc87)"></div>
        <h4>Nuclear (Most common)</h4>
        <p>Free-nuclear divisions first, cell walls formed later. Eg: <strong>Coconut</strong> — liquid endosperm (coconut water) = free nuclear stage; coconut meat = cellular stage.</p>
      </div>
      <div class="mini-card sky">
        <div class="accent-bar" style="background:linear-gradient(90deg,#0369a1,#38bdf8)"></div>
        <h4>Cellular</h4>
        <p>Cell wall formed after every nuclear division. Eg: <strong>Petunia</strong>, Adoxa. Less common than nuclear type.</p>
      </div>
      <div class="mini-card amber">
        <div class="accent-bar" style="background:linear-gradient(90deg,#d97706,#fbbf24)"></div>
        <h4>Helobial</h4>
        <p>Intermediate type — first division cellular, rest nuclear. Common in <strong>monocots</strong>.</p>
      </div>
      <div class="mini-card rose">
        <div class="accent-bar" style="background:linear-gradient(90deg,#be123c,#fb7185)"></div>
        <h4>Ruminate Endosperm</h4>
        <p>Irregular, chewed-up appearance. Eg: <strong>Areca nut</strong> (betel nut), <em>Annona</em>, nutmeg.</p>
      </div>
    </div>

    <div class="table-wrap">
      <table>
        <tr><th>Feature</th><th>Dicot Embryo</th><th>Monocot Embryo (Maize)</th></tr>
        <tr><td>Cotyledons</td><td>2 (seed leaves)</td><td>1 (Scutellum)</td></tr>
        <tr><td>Plumule cover</td><td>Absent</td><td><strong>Coleoptile</strong></td></tr>
        <tr><td>Radicle cover</td><td>Absent</td><td><strong>Coleorhiza</strong></td></tr>
        <tr><td>Epiblast</td><td>Absent</td><td>Present (vestigial 2nd cotyledon)</td></tr>
        <tr><td>Eg.</td><td>Pea, Bean, Mustard, Capsella</td><td>Maize, Wheat, Grass</td></tr>
      </table>
    </div>

    <!-- BULB TRIVIA -->
    <div class="bulb-trivia" onclick="toggleBulb(this)">
      <div class="bulb-header">
        <div class="bulb-icon">
          <svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg">
            <path d="M20 5 C13 5 8 10 8 17 C8 22 11 25 14 27 L14 31 C14 32.1 14.9 33 16 33 L24 33 C25.1 33 26 32.1 26 31 L26 27 C29 25 32 22 32 17 C32 10 27 5 20 5 Z" fill="#f59e0b" stroke="#d97706" stroke-width="1.5"/>
            <rect x="16" y="33" width="8" height="3" rx="1.5" fill="#92400e"/>
          </svg>
        </div>
        <div class="bulb-label">NEET + Allen Trivia<span>High-yield facts for Seed & Embryo</span></div>
        <div class="bulb-arrow">▼</div>
      </div>
      <div class="bulb-body">
        <ul>
          <li><strong>Scutellum</strong> = single cotyledon of monocot (shield-shaped); secretes amylase to digest starchy endosperm in germination. <span class="neet-tag">Allen</span></li>
          <li>Coconut water = <strong>free-nuclear endosperm</strong>; coconut meat = cellular endosperm. <span class="neet-tag">NEET</span></li>
          <li><strong>Albuminous seeds</strong> (endosperm persistent): wheat, maize, castor, coconut, barley.</li>
          <li><strong>Ex-albuminous seeds</strong> (endosperm consumed during development): pea, bean, groundnut, orchid. <span class="neet-tag">NEET</span></li>
          <li><strong>False fruit</strong> (thalamus → fruit): apple (edible part = thalamus), strawberry, cashew (accessory fruit). <span class="neet-tag">Boards</span></li>
          <li><strong>True fruit</strong>: pericarp develops from ovary wall only. Eg: mango, tomato, date.</li>
          <li><strong>Parthenocarpy</strong> = fruit without fertilisation → seedless fruits. Eg: banana, seedless grapes. Can be induced by auxins (IAA). <span class="neet-tag">NEET</span></li>
          <li>Hypophysis = first cell of suspensor → gives rise to radicle tip and root cap.</li>
        </ul>
      </div>
    </div>

    <div class="mcq-section">
      <div class="mcq-section-header">
        <h3>Practice Questions</h3>
        <span class="mcq-badge">3 MCQs · Boards + NEET</span>
      </div>

      <div class="mcq-item" id="se-q1">
        <div class="q-num">Q 1 · Seed & Embryo</div>
        <div class="q">Coconut water represents which type of endosperm? <span class="pyq-tag">NEET 2018</span></div>
        <div class="mcq-options">
          <button class="mcq-opt" onclick="answerMCQ('se-q1',this,true)">A. Free-nuclear endosperm</button>
          <button class="mcq-opt" onclick="answerMCQ('se-q1',this,false)">B. Cellular endosperm</button>
          <button class="mcq-opt" onclick="answerMCQ('se-q1',this,false)">C. Helobial endosperm</button>
          <button class="mcq-opt" onclick="answerMCQ('se-q1',this,false)">D. Ruminate endosperm</button>
        </div>
        <div class="mcq-ans">✓ Free-nuclear endosperm — Coconut water is the free-nuclear (liquid) stage. The coconut meat (solid white part) represents the cellular stage where cell walls have formed around the nuclei.</div>
      </div>

      <div class="mcq-item" id="se-q2">
        <div class="q-num">Q 2 · Seed & Embryo</div>
        <div class="q">In a monocot seed, the radicle is enclosed in: <span class="pyq-tag">Boards 2019</span></div>
        <div class="mcq-options">
          <button class="mcq-opt" onclick="answerMCQ('se-q2',this,false)">A. Coleoptile</button>
          <button class="mcq-opt" onclick="answerMCQ('se-q2',this,true)">B. Coleorhiza</button>
          <button class="mcq-opt" onclick="answerMCQ('se-q2',this,false)">C. Scutellum</button>
          <button class="mcq-opt" onclick="answerMCQ('se-q2',this,false)">D. Epiblast</button>
        </div>
        <div class="mcq-ans">✓ Coleorhiza — In monocot embryo (e.g., maize), the radicle is covered by coleorhiza. The plumule is covered by coleoptile. Scutellum is the single cotyledon; epiblast is the vestigial 2nd cotyledon.</div>
      </div>

      <div class="mcq-item" id="se-q3">
        <div class="q-num">Q 3 · Seed & Embryo</div>
        <div class="q">Parthenocarpy (seedless fruit) can be induced by: <span class="pyq-tag">NEET 2016</span></div>
        <div class="mcq-options">
          <button class="mcq-opt" onclick="answerMCQ('se-q3',this,false)">A. Gibberellins only</button>
          <button class="mcq-opt" onclick="answerMCQ('se-q3',this,true)">B. Auxins (IAA)</button>
          <button class="mcq-opt" onclick="answerMCQ('se-q3',this,false)">C. Cytokinins</button>
          <button class="mcq-opt" onclick="answerMCQ('se-q3',this,false)">D. Abscisic acid</button>
        </div>
        <div class="mcq-ans">✓ Auxins (IAA) — Parthenocarpy = fruit without fertilisation (seedless). Can be induced artificially by applying auxins. Natural examples: banana, seedless grapes, some citrus varieties.</div>
      </div>
    </div>

  </div>
</div>

<!-- ══════════════════════════════════════
     PAGE 8: APOMIXIS
═══════════════════════════════════════ -->
<div class="page" id="page-apomixis">
  <div class="page-header">
    <div class="page-num">Topic 8 of 8</div>
    <div class="page-title">Apomixis & Polyembryony</div>
    <div class="page-subtitle">Seed Formation Without Fertilisation · Agricultural Significance</div>
  </div>
  <div class="container">

    <div class="card">
      <p><span class="key">Apomixis</span> = Production of seeds <strong>without fertilisation</strong>. It is a form of asexual reproduction that mimics sexual reproduction (agamospermy). No genetic recombination occurs → clonal offspring identical to mother plant.</p>
    </div>

    <!-- Apomixis diagram -->
    <div class="diagram-box">
      <div class="diagram-label">Allen Diagram — Types of Apomixis</div>
      <svg viewBox="0 0 700 220" xmlns="http://www.w3.org/2000/svg" font-family="Outfit,sans-serif">
        <!-- Central -->
        <circle cx="350" cy="110" r="50" fill="#0d6e4a"/>
        <text x="350" y="105" fill="#fff" text-anchor="middle" font-size="12" font-weight="800">Apomixis</text>
        <text x="350" y="122" fill="#b9ffd9" text-anchor="middle" font-size="10">Seed without</text>
        <text x="350" y="135" fill="#b9ffd9" text-anchor="middle" font-size="10">fertilisation</text>

        <!-- Diplospory -->
        <rect x="20" y="20" width="145" height="75" rx="12" fill="#ede9fe" stroke="#6d28d9" stroke-width="2"/>
        <text x="92" y="42" fill="#6d28d9" text-anchor="middle" font-size="11" font-weight="800">Diplospory</text>
        <text x="92" y="58" fill="#4c1d95" text-anchor="middle" font-size="9">MMC → embryo sac</text>
        <text x="92" y="71" fill="#4c1d95" text-anchor="middle" font-size="9">without meiosis (2n)</text>
        <text x="92" y="86" fill="#6d28d9" text-anchor="middle" font-size="9" font-weight="700">Eg: Taraxacum (dandelion)</text>
        <line x1="165" y1="58" x2="302" y2="90" stroke="#6d28d9" stroke-width="1.5" stroke-dasharray="4"/>

        <!-- Apospory -->
        <rect x="20" y="125" width="145" height="75" rx="12" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
        <text x="92" y="147" fill="#d97706" text-anchor="middle" font-size="11" font-weight="800">Apospory</text>
        <text x="92" y="163" fill="#92400e" text-anchor="middle" font-size="9">Nucellus/integument</text>
        <text x="92" y="176" fill="#92400e" text-anchor="middle" font-size="9">cell → embryo sac</text>
        <text x="92" y="189" fill="#d97706" text-anchor="middle" font-size="9" font-weight="700">(somatic cells, no meiosis)</text>
        <line x1="165" y1="163" x2="302" y2="130" stroke="#d97706" stroke-width="1.5" stroke-dasharray="4"/>

        <!-- Adventive embryony -->
        <rect x="535" y="20" width="155" height="75" rx="12" fill="#fce7f3" stroke="#be123c" stroke-width="2"/>
        <text x="612" y="42" fill="#be123c" text-anchor="middle" font-size="11" font-weight="800">Adventive Embryony</text>
        <text x="612" y="58" fill="#9f1239" text-anchor="middle" font-size="9">Sporophytic embryos from</text>
        <text x="612" y="71" fill="#9f1239" text-anchor="middle" font-size="9">nucellus / integument</text>
        <text x="612" y="86" fill="#be123c" text-anchor="middle" font-size="9" font-weight="700">Eg: Citrus, Mango → Polyembryony</text>
        <line x1="535" y1="58" x2="398" y2="90" stroke="#be123c" stroke-width="1.5" stroke-dasharray="4"/>

        <!-- Vegetative apomixis -->
        <rect x="535" y="125" width="155" height="75" rx="12" fill="#d1fae5" stroke="#16a06a" stroke-width="2"/>
        <text x="612" y="147" fill="#16a06a" text-anchor="middle" font-size="11" font-weight="800">Vegetative Apomixis</text>
        <text x="612" y="163" fill="#065f46" text-anchor="middle" font-size="9">Vegetative buds form</text>
        <text x="612" y="176" fill="#065f46" text-anchor="middle" font-size="9">instead of flowers/seeds</text>
        <text x="612" y="189" fill="#16a06a" text-anchor="middle" font-size="9" font-weight="700">Eg: Agave, Allium</text>
        <line x1="535" y1="163" x2="398" y2="130" stroke="#16a06a" stroke-width="1.5" stroke-dasharray="4"/>
      </svg>
    </div>

    <div class="section-title">Polyembryony</div>
    <div class="card">
      <p><span class="key">Polyembryony</span> = Presence of <strong>more than one embryo</strong> in a seed. First reported by <strong>Leeuwenhoek</strong> in Citrus (orange) seeds.</p>
      <p style="margin-top:0.6rem">Types: <strong>Nucellar polyembryony</strong> (adventive embryony from nucellus) → Citrus, Mangifera | Simple polyembryony (cleavage of zygote) | Eg: Opuntia, Orchids.</p>
    </div>

    <div class="info-box violet">
      <strong>Agricultural Significance of Apomixis (Allen Module — Very Important)</strong>
      Apomixis helps maintain <strong>hybrid vigour</strong> (heterosis) year after year without loss of genetic combination. Traditional hybrid seeds must be produced every season (costly); apomictic hybrids would produce clonal seeds true to parent. Major agricultural research goal. Eg: apomictic sugarcane, wheat, rice varieties under development.
    </div>

    <!-- BULB TRIVIA -->
    <div class="bulb-trivia" onclick="toggleBulb(this)">
      <div class="bulb-header">
        <div class="bulb-icon">
          <svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg">
            <path d="M20 5 C13 5 8 10 8 17 C8 22 11 25 14 27 L14 31 C14 32.1 14.9 33 16 33 L24 33 C25.1 33 26 32.1 26 31 L26 27 C29 25 32 22 32 17 C32 10 27 5 20 5 Z" fill="#f59e0b" stroke="#d97706" stroke-width="1.5"/>
            <rect x="16" y="33" width="8" height="3" rx="1.5" fill="#92400e"/>
          </svg>
        </div>
        <div class="bulb-label">NEET + Allen Trivia<span>High-yield facts for Apomixis & Polyembryony</span></div>
        <div class="bulb-arrow">▼</div>
      </div>
      <div class="bulb-body">
        <ul>
          <li>Apomixis = agamospermy = <strong>seed without sex</strong>; offspring are genetically identical to mother (clonal). <span class="neet-tag">NEET</span></li>
          <li><strong>Polyembryony in Citrus</strong> → nucellar polyembryony (adventive embryony from nucellus). First discovered by <strong>Leeuwenhoek</strong> in orange. <span class="neet-tag">NEET</span></li>
          <li>Orchid seeds are the <strong>smallest, most numerous</strong> seeds; lack endosperm; up to 10 million per plant (Asparagus fern). <span class="neet-tag">Allen</span></li>
          <li>Smallest seeds overall = orchids; heaviest seed = Lodoicea maldivica (Double coconut, Coco de Mer) up to 25 kg.</li>
          <li>Apomixis avoids: meiosis, fertilisation, and genetic recombination. Offspring are <strong>diploid</strong> (not haploid).</li>
          <li>In India: <strong>ICAR, IARI</strong> research ongoing for apomictic crop varieties (especially sorghum, millets). <span class="neet-tag">Allen</span></li>
          <li><strong>Vegetative apomixis</strong> (Agave, Allium) → bulbils/vegetative propagules replace normal flowers.</li>
        </ul>
      </div>
    </div>

    <div class="mcq-section">
      <div class="mcq-section-header">
        <h3>Practice Questions</h3>
        <span class="mcq-badge">3 MCQs · Boards + NEET</span>
      </div>

      <div class="mcq-item" id="ap-q1">
        <div class="q-num">Q 1 · Apomixis</div>
        <div class="q">Polyembryony through adventive embryony is most commonly seen in: <span class="pyq-tag">NEET 2014</span></div>
        <div class="mcq-options">
          <button class="mcq-opt" onclick="answerMCQ('ap-q1',this,false)">A. Wheat</button>
          <button class="mcq-opt" onclick="answerMCQ('ap-q1',this,false)">B. Orchids</button>
          <button class="mcq-opt" onclick="answerMCQ('ap-q1',this,true)">C. Citrus</button>
          <button class="mcq-opt" onclick="answerMCQ('ap-q1',this,false)">D. Pea</button>
        </div>
        <div class="mcq-ans">✓ Citrus — Nucellar polyembryony (adventive embryony from nucellus). First reported by Leeuwenhoek in orange. Each orange seed may contain 2-3 embryos of nucellar origin + 1 sexual embryo.</div>
      </div>

      <div class="mcq-item" id="ap-q2">
        <div class="q-num">Q 2 · Apomixis</div>
        <div class="q">Apomixis in plants is a type of: <span class="pyq-tag">Boards 2020</span></div>
        <div class="mcq-options">
          <button class="mcq-opt" onclick="answerMCQ('ap-q2',this,false)">A. Sexual reproduction</button>
          <button class="mcq-opt" onclick="answerMCQ('ap-q2',this,true)">B. Asexual reproduction</button>
          <button class="mcq-opt" onclick="answerMCQ('ap-q2',this,false)">C. Vegetative propagation only</button>
          <button class="mcq-opt" onclick="answerMCQ('ap-q2',this,false)">D. Cross-pollination</button>
        </div>
        <div class="mcq-ans">✓ Asexual reproduction — Apomixis produces seeds without fertilisation. Offspring are genetically identical to the mother (clonal). It mimics sexual reproduction but does not involve fusion of gametes.</div>
      </div>

      <div class="mcq-item" id="ap-q3">
        <div class="q-num">Q 3 · Apomixis</div>
        <div class="q">What is the agricultural significance of apomixis? <span class="pyq-tag">Boards 2022</span></div>
        <div class="mcq-options">
          <button class="mcq-opt" onclick="answerMCQ('ap-q3',this,false)">A. Increases genetic variation</button>
          <button class="mcq-opt" onclick="answerMCQ('ap-q3',this,true)">B. Maintains hybrid vigour across generations</button>
          <button class="mcq-opt" onclick="answerMCQ('ap-q3',this,false)">C. Produces polyploid plants</button>
          <button class="mcq-opt" onclick="answerMCQ('ap-q3',this,false)">D. Promotes cross-pollination</button>
        </div>
        <div class="mcq-ans">✓ Maintains hybrid vigour — Apomixis helps fix hybrid characteristics across generations without costly hybrid seed production each season. This is a major agricultural research goal for crops like wheat, rice, sorghum.</div>
      </div>
    </div>

  </div>
</div>

<!-- ══════════════════════════════════════
     PAGE 9: QUICK REVISION
═══════════════════════════════════════ -->
<div class="page" id="page-revision">
  <div class="page-header">
    <div class="page-num">Revision Summary</div>
    <div class="page-title">Quick Revision</div>
    <div class="page-subtitle">Key Numbers · Glossary · One-liner Facts</div>
  </div>
  <div class="container">

    <div class="section-title">🔢 Numbers to Remember (NEET Loves These!)</div>
    <div class="numbers-grid">
      <div class="num-card">
        <div class="num" style="color:#0d6e4a">4</div>
        <div class="lbl">Microsporangia per anther</div>
      </div>
      <div class="num-card">
        <div class="num" style="color:#d97706">4</div>
        <div class="lbl">Microspores per MMC (meiosis)</div>
      </div>
      <div class="num-card">
        <div class="num" style="color:#6d28d9">7</div>
        <div class="lbl">Cells in embryo sac</div>
      </div>
      <div class="num-card">
        <div class="num" style="color:#be123c">8</div>
        <div class="lbl">Nuclei in embryo sac</div>
      </div>
      <div class="num-card">
        <div class="num" style="color:#0369a1">3</div>
        <div class="lbl">Egg apparatus cells</div>
      </div>
      <div class="num-card">
        <div class="num" style="color:#0f766e">3</div>
        <div class="lbl">Antipodal cells</div>
      </div>
      <div class="num-card">
        <div class="num" style="color:#d97706">2</div>
        <div class="lbl">Polar nuclei (central cell)</div>
      </div>
      <div class="num-card">
        <div class="num" style="color:#6d28d9">3n</div>
        <div class="lbl">Endosperm ploidy</div>
      </div>
      <div class="num-card">
        <div class="num" style="color:#0d6e4a">2n</div>
        <div class="lbl">Embryo ploidy</div>
      </div>
      <div class="num-card">
        <div class="num" style="color:#be123c">2/3</div>
        <div class="lbl">Pollen grain cells</div>
      </div>
    </div>

    <div class="section-title">📖 Key Terms Glossary</div>
    <div class="table-wrap">
      <table>
        <tr><th>Term</th><th>One-Line Definition</th><th>Example</th></tr>
        <tr><td>Sporopollenin</td><td>Most resistant organic compound; forms pollen exine</td><td>All pollen grains</td></tr>
        <tr><td>Tapetum</td><td>Innermost nutritive anther wall layer; multinucleate</td><td>All angiosperms</td></tr>
        <tr><td>Filiform apparatus</td><td>In synergids; guides pollen tube to egg</td><td>Embryo sac</td></tr>
        <tr><td>Double fertilisation</td><td>Syngamy + Triple fusion; unique to angiosperms</td><td>All angiosperms</td></tr>
        <tr><td>Perisperm</td><td>Persistent residual nucellus</td><td>Black pepper, coffee, beet</td></tr>
        <tr><td>Parthenocarpy</td><td>Fruit without fertilisation (seedless)</td><td>Banana, seedless grapes</td></tr>
        <tr><td>Apomixis</td><td>Seed formation without fertilisation</td><td>Citrus, Taraxacum</td></tr>
        <tr><td>Polyembryony</td><td>More than 1 embryo per seed</td><td>Citrus, Mango</td></tr>
        <tr><td>Cleistogamy</td><td>Flowers never open; obligate autogamy</td><td>Viola, Oxalis, Commelina</td></tr>
        <tr><td>Chalazogamy</td><td>Pollen tube enters through chalaza</td><td>Casuarina</td></tr>
        <tr><td>Scutellum</td><td>Single cotyledon of monocot embryo</td><td>Maize, Wheat</td></tr>
        <tr><td>Epiblast</td><td>Vestigial second cotyledon in monocots</td><td>Maize</td></tr>
      </table>
    </div>

    <div class="section-title">⚡ One-Liner Facts for Last-Minute Revision</div>
    <div class="revision-panel">
      <h3>NEET & Boards Must-Remember Facts</h3>
      <div class="rev-item">Anther wall (outside→in): Epidermis → Endothecium → Middle layers → <strong>Tapetum</strong></div>
      <div class="rev-item">Tapetum = innermost, nutritive, polyploid (2n/4n), secretes pollenkitt + ubisch bodies</div>
      <div class="rev-item">1 MMC (2n) →[Meiosis]→ 4 microspores (n) = tetrad</div>
      <div class="rev-item">Embryo sac = 7 cells, 8 nuclei (Polygonum type = monosporic, most common)</div>
      <div class="rev-item">Chalazal megaspore = functional megaspore (always!)</div>
      <div class="rev-item">3 mitotic divisions of functional megaspore → 8-nucleate embryo sac</div>
      <div class="rev-item">Double fertilisation: Syngamy (♂ + egg → 2n zygote) + Triple fusion (♂ + 2 polar → 3n PEN)</div>
      <div class="rev-item">Nawaschin (1898): double fertilisation in Lilium & Fritillaria</div>
      <div class="rev-item">Porogamy (most common) | Chalazogamy (Casuarina) | Mesogamy (Cucurbita)</div>
      <div class="rev-item">Coconut water = free-nuclear endosperm; coconut meat = cellular endosperm</div>
      <div class="rev-item">Apple, strawberry, cashew = false fruits (thalamus → edible part)</div>
      <div class="rev-item">Nucellar polyembryony first reported by Leeuwenhoek in Citrus (orange)</div>
    </div>

    <div class="info-box green" style="margin-top:2rem">
      <strong>🎯 Common Mistakes to Avoid</strong>
      ❌ Pollination ≠ Fertilisation | ❌ Geitonogamy = genetically self-pollination, not cross | ❌ Gymnosperms do NOT have double fertilisation | ❌ Endosperm is 3n (not 2n) | ❌ Antipodal cells are at chalazal end (not micropylar) | ❌ Egg apparatus is at micropylar end | ❌ Coconut water = FREE nuclear (not cellular) endosperm
    </div>

  </div>
</div>

<footer>
  <strong>Sexual Reproduction in Flowering Plants</strong> — Class 12 NCERT Biology Chapter 1<br>
  Reference: NCERT Class 12 Biology Textbook · Allen Kota Module (NEET UG) · CBSE Board PYQs<br>
  <span style="opacity:0.5">For educational purposes only</span>
</footer>

<script>
// Page navigation
function showPage(id, btn) {
  document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
  document.querySelectorAll('.topic-btn').forEach(b => b.classList.remove('active'));
  document.getElementById('page-' + id).classList.add('active');
  btn.classList.add('active');
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

// Bulb trivia toggle
function toggleBulb(el) {
  el.classList.toggle('open');
}

// MCQ answer
function answerMCQ(id, btn, isCorrect) {
  const item = document.getElementById(id);
  if (item.classList.contains('revealed')) return;
  item.classList.add('revealed');
  const opts = item.querySelectorAll('.mcq-opt');
  opts.forEach(o => { o.disabled = true; });
  if (isCorrect) {
    btn.classList.add('correct');
  } else {
    btn.classList.add('wrong');
    // Show correct answer
    opts.forEach(o => {
      if (o.onclick.toString().includes('true')) o.classList.add('correct');
    });
  }
}
</script>

</body>
</html>
