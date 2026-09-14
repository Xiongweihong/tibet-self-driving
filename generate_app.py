import json

with open('regions_data.json', 'r', encoding='utf-8') as f:
    regions = json.load(f)

html_template = r'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CHRONO-LOOP 5.0 | 46天西藏全境动态可视化路书与全域纯玩指挥舱</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700;900&family=Noto+Sans+SC:wght@300;400;500;700;900&family=Outfit:wght@300;400;600;700;800&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg-dark: #05080e;
      --bg-surface: #0a0f1d;
      --bg-panel: rgba(13, 20, 36, 0.82);
      --bg-card: rgba(18, 28, 50, 0.65);
      --border-color: rgba(255, 255, 255, 0.08);
      --border-glow: rgba(56, 189, 248, 0.35);
      --cyan-glow: #06b6d4;
      --emerald-glow: #10b981;
      --amber-glow: #f59e0b;
      --rose-glow: #f43f5e;
      --purple-glow: #a855f7;
      --text-primary: #f8fafc;
      --text-secondary: #94a3b8;
      --text-muted: #64748b;
      --font-display: 'Outfit', 'Noto Sans SC', sans-serif;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      background-color: var(--bg-dark);
      color: var(--text-primary);
      font-family: var(--font-display);
      line-height: 1.6;
      overflow-x: hidden;
      background-image: 
        radial-gradient(circle at 10% 15%, rgba(6, 182, 212, 0.12) 0%, transparent 45%),
        radial-gradient(circle at 90% 25%, rgba(245, 158, 11, 0.10) 0%, transparent 45%),
        radial-gradient(circle at 50% 85%, rgba(16, 185, 129, 0.08) 0%, transparent 50%);
      background-attachment: fixed;
    }

    ::-webkit-scrollbar { width: 8px; height: 8px; }
    ::-webkit-scrollbar-track { background: rgba(0,0,0,0.3); }
    ::-webkit-scrollbar-thumb { background: rgba(255,255,255,0.18); border-radius: 4px; }
    ::-webkit-scrollbar-thumb:hover { background: rgba(255,255,255,0.35); }

    /* Top Master HUD */
    header {
      padding: 1.6rem 2rem;
      border-bottom: 1px solid var(--border-color);
      background: linear-gradient(180deg, rgba(10, 15, 29, 0.96) 0%, rgba(10, 15, 29, 0.85) 100%);
      position: sticky;
      top: 0;
      z-index: 1000;
      backdrop-filter: blur(20px);
    }

    .header-inner {
      max-width: 1520px;
      margin: 0 auto;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 1.2rem;
    }

    .brand-title-wrap {
      display: flex;
      flex-direction: column;
      gap: 0.25rem;
    }

    .protocol-badge {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      color: var(--emerald-glow);
      font-size: 0.72rem;
      font-weight: 700;
      letter-spacing: 0.14em;
      text-transform: uppercase;
    }

    .pulse-dot {
      width: 8px;
      height: 8px;
      background: var(--emerald-glow);
      border-radius: 50%;
      box-shadow: 0 0 10px var(--emerald-glow);
      animation: pulseAnim 2s infinite;
    }
    @keyframes pulseAnim {
      0%, 100% { opacity: 1; transform: scale(1); }
      50% { opacity: 0.35; transform: scale(0.85); }
    }

    h1 {
      font-size: clamp(1.3rem, 2.2vw, 1.95rem);
      font-weight: 800;
      letter-spacing: -0.02em;
      background: linear-gradient(135deg, #ffffff 30%, #38bdf8 65%, #fbbf24 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    /* Tab Switcher */
    .view-tabs {
      display: flex;
      background: rgba(255, 255, 255, 0.05);
      padding: 4px;
      border-radius: 12px;
      border: 1px solid var(--border-color);
      gap: 4px;
    }

    .tab-btn {
      background: transparent;
      border: none;
      color: var(--text-secondary);
      font-family: inherit;
      font-size: 0.86rem;
      font-weight: 600;
      padding: 0.55rem 1.1rem;
      border-radius: 8px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.45rem;
      transition: all 0.2s ease;
    }
    .tab-btn:hover {
      color: #fff;
      background: rgba(255, 255, 255, 0.06);
    }
    .tab-btn.active {
      background: linear-gradient(135deg, rgba(6, 182, 212, 0.25) 0%, rgba(59, 130, 246, 0.25) 100%);
      color: #fff;
      border: 1px solid var(--border-glow);
      box-shadow: 0 0 15px rgba(6, 182, 212, 0.25);
    }

    /* Live Telemetry Pills */
    .hud-telemetry {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      flex-wrap: wrap;
    }

    .telemetry-pill {
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--border-color);
      border-radius: 10px;
      padding: 0.4rem 0.85rem;
      display: flex;
      flex-direction: column;
      min-width: 95px;
    }
    .tel-label {
      font-size: 0.68rem;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }
    .tel-val {
      font-size: 0.98rem;
      font-weight: 700;
      color: #fff;
      font-family: monospace;
    }

    /* Main Container */
    .main-container {
      max-width: 1520px;
      margin: 0 auto;
      padding: 1.8rem 1.5rem 3rem;
    }

    /* TAB CONTENT WRAPPERS */
    .tab-pane {
      display: none;
      animation: tabFadeIn 0.3s ease;
    }
    .tab-pane.active {
      display: block;
    }
    @keyframes tabFadeIn {
      from { opacity: 0; transform: translateY(8px); }
      to { opacity: 1; transform: translateY(0); }
    }

    /* --- TAB 1: COCKPIT STYLES --- */
    .playback-bar {
      background: var(--bg-panel);
      border: 1px solid var(--border-color);
      border-radius: 16px;
      padding: 1.1rem 1.5rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1.5rem;
      margin-bottom: 1.8rem;
      backdrop-filter: blur(16px);
      box-shadow: 0 15px 35px rgba(0, 0, 0, 0.4);
      flex-wrap: wrap;
    }

    .playback-controls {
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }

    .btn-ctrl {
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--border-color);
      color: #fff;
      padding: 0.55rem 1.1rem;
      border-radius: 10px;
      cursor: pointer;
      font-family: inherit;
      font-weight: 600;
      font-size: 0.85rem;
      display: inline-flex;
      align-items: center;
      gap: 0.45rem;
      transition: all 0.2s;
    }
    .btn-ctrl:hover {
      background: rgba(255, 255, 255, 0.1);
      border-color: var(--cyan-glow);
    }

    .btn-play-hero {
      background: linear-gradient(135deg, #06b6d4 0%, #3b82f6 100%);
      color: #000;
      font-weight: 700;
      border: none;
      box-shadow: 0 0 20px rgba(6, 182, 212, 0.4);
    }
    .btn-play-hero:hover {
      transform: translateY(-1px);
      box-shadow: 0 0 25px rgba(6, 182, 212, 0.6);
    }

    .speed-pills {
      display: flex;
      background: rgba(0, 0, 0, 0.35);
      border-radius: 8px;
      padding: 2px;
      border: 1px solid var(--border-color);
    }
    .speed-chip {
      padding: 0.3rem 0.65rem;
      font-size: 0.75rem;
      color: var(--text-muted);
      cursor: pointer;
      border-radius: 6px;
      transition: all 0.2s;
    }
    .speed-chip.active {
      background: var(--cyan-glow);
      color: #000;
      font-weight: 700;
    }

    .scrubber-zone {
      flex: 1;
      display: flex;
      align-items: center;
      gap: 1rem;
      min-width: 280px;
    }

    .timeline-range {
      flex: 1;
      -webkit-appearance: none;
      height: 6px;
      border-radius: 3px;
      background: rgba(255, 255, 255, 0.12);
      outline: none;
      cursor: pointer;
    }
    .timeline-range::-webkit-slider-thumb {
      -webkit-appearance: none;
      width: 18px;
      height: 18px;
      border-radius: 50%;
      background: var(--cyan-glow);
      box-shadow: 0 0 12px var(--cyan-glow);
      cursor: pointer;
      border: 2px solid #fff;
      transition: transform 0.15s;
    }
    .timeline-range::-webkit-slider-thumb:hover { transform: scale(1.3); }

    /* Dual Stage */
    .cockpit-stage {
      display: grid;
      grid-template-columns: 1.45fr 1fr;
      gap: 1.8rem;
      margin-bottom: 2rem;
    }

    .map-pod {
      background: var(--bg-panel);
      border: 1px solid var(--border-color);
      border-radius: 18px;
      padding: 1.5rem;
      backdrop-filter: blur(16px);
      box-shadow: 0 20px 40px rgba(0, 0, 0, 0.45);
      position: relative;
      display: flex;
      flex-direction: column;
    }

    .pod-header {
      display: flex;
      justify-content: space-between;
      align-items: baseline;
      margin-bottom: 0.9rem;
    }
    .pod-title {
      font-size: 1.15rem;
      font-weight: 700;
      color: #fff;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .svg-viewport {
      position: relative;
      width: 100%;
      background: radial-gradient(circle at center, rgba(16, 25, 42, 0.98) 0%, rgba(5, 9, 15, 0.98) 100%);
      border-radius: 14px;
      overflow: hidden;
      border: 1px solid rgba(255,255,255,0.06);
    }

    /* Spotlight Card */
    .spotlight-pod {
      background: linear-gradient(180deg, rgba(20, 32, 56, 0.88) 0%, rgba(10, 16, 28, 0.95) 100%);
      border: 1px solid var(--border-glow);
      border-radius: 18px;
      padding: 1.8rem;
      backdrop-filter: blur(16px);
      box-shadow: 0 20px 40px rgba(0, 0, 0, 0.5);
      display: flex;
      flex-direction: column;
      position: relative;
      overflow: hidden;
    }
    .spotlight-pod::before {
      content: '';
      position: absolute;
      top: 0; left: 0; right: 0; height: 4px;
      background: linear-gradient(90deg, var(--cyan-glow), var(--purple-glow), var(--amber-glow), var(--emerald-glow));
    }

    .spot-top {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 0.8rem;
    }
    .spot-day-badge {
      font-size: 1.85rem;
      font-weight: 900;
      letter-spacing: -0.02em;
      color: #fff;
      display: flex;
      align-items: baseline;
      gap: 0.6rem;
    }
    .spot-stage-chip {
      font-size: 0.8rem;
      color: var(--cyan-glow);
      font-weight: 600;
      background: rgba(6, 182, 212, 0.12);
      padding: 0.2rem 0.65rem;
      border-radius: 6px;
      border: 1px solid rgba(6, 182, 212, 0.25);
    }

    .spot-alt-chip {
      font-size: 0.9rem;
      padding: 0.35rem 0.85rem;
      border-radius: 8px;
      font-weight: 700;
      background: rgba(16, 185, 129, 0.15);
      color: var(--emerald-glow);
      border: 1px solid rgba(16, 185, 129, 0.35);
    }
    .alt-warn { background: rgba(245, 158, 11, 0.15); color: var(--amber-glow); border-color: rgba(245, 158, 11, 0.35); }
    .alt-high { background: rgba(244, 63, 94, 0.15); color: var(--rose-glow); border-color: rgba(244, 63, 94, 0.35); }

    .spot-route-name {
      font-size: 1.25rem;
      font-weight: 800;
      color: #fff;
      margin-bottom: 1rem;
      line-height: 1.4;
    }

    .spot-metrics-grid {
      display: flex;
      gap: 0.75rem;
      margin-bottom: 1.2rem;
      flex-wrap: wrap;
    }
    .spot-metric-tag {
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--border-color);
      padding: 0.35rem 0.75rem;
      border-radius: 8px;
      font-size: 0.82rem;
      color: var(--text-secondary);
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }

    .spot-block {
      background: rgba(0, 0, 0, 0.28);
      border: 1px solid rgba(255, 255, 255, 0.05);
      border-radius: 12px;
      padding: 0.9rem 1.1rem;
      margin-bottom: 0.85rem;
    }
    .spot-block-title {
      font-size: 0.78rem;
      font-weight: 700;
      color: var(--cyan-glow);
      margin-bottom: 0.35rem;
      display: flex;
      align-items: center;
      gap: 0.4rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }
    .title-food { color: var(--amber-glow); }
    .title-warn { color: var(--rose-glow); }

    .spot-block-body {
      font-size: 0.88rem;
      color: var(--text-secondary);
      line-height: 1.5;
    }

    .spot-nav-action {
      margin-top: auto;
      background: rgba(0, 0, 0, 0.45);
      border: 1px solid var(--border-color);
      border-radius: 10px;
      padding: 0.75rem 1rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 0.8rem;
    }
    .nav-str {
      font-family: monospace;
      font-size: 0.8rem;
      color: var(--text-muted);
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
    }
    .btn-copy-nav {
      background: var(--cyan-glow);
      color: #000;
      font-weight: 700;
      border: none;
      padding: 0.45rem 0.95rem;
      border-radius: 6px;
      font-size: 0.8rem;
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.2s;
    }
    .btn-copy-nav:hover {
      box-shadow: 0 0 15px var(--cyan-glow);
      transform: translateY(-1px);
    }

    /* Altitude Chart */
    .alt-panel {
      background: var(--bg-panel);
      border: 1px solid var(--border-color);
      border-radius: 18px;
      padding: 1.5rem;
      backdrop-filter: blur(16px);
      box-shadow: 0 20px 40px rgba(0, 0, 0, 0.45);
      margin-bottom: 2rem;
    }
    .alt-svg-wrap {
      width: 100%;
      height: 240px;
      position: relative;
    }

    /* Days Scroller */
    .days-scroller-wrap {
      margin-bottom: 2.5rem;
    }
    .scroller-head {
      font-size: 1.1rem;
      font-weight: 700;
      color: #fff;
      margin-bottom: 0.9rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }
    .days-tray {
      display: flex;
      gap: 0.85rem;
      overflow-x: auto;
      padding-bottom: 0.8rem;
      scroll-behavior: smooth;
    }
    .tray-card {
      flex: 0 0 160px;
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 0.9rem;
      cursor: pointer;
      transition: all 0.2s;
    }
    .tray-card:hover {
      background: rgba(255, 255, 255, 0.08);
      border-color: var(--cyan-glow);
      transform: translateY(-3px);
    }
    .tray-card.active {
      background: rgba(6, 182, 212, 0.15);
      border-color: var(--cyan-glow);
      box-shadow: 0 0 15px rgba(6, 182, 212, 0.3);
    }
    .tray-day-tag { font-size: 1.1rem; font-weight: 800; color: #fff; }
    .tray-alt { font-size: 0.75rem; color: var(--emerald-glow); font-weight: 600; }
    .tray-route { font-size: 0.74rem; color: var(--text-secondary); margin-top: 0.4rem; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }

    /* --- TAB 2: 49 REGIONS EXPLORER STYLES --- */
    .filter-deck {
      background: var(--bg-panel);
      border: 1px solid var(--border-color);
      border-radius: 16px;
      padding: 1.2rem 1.6rem;
      margin-bottom: 2rem;
      backdrop-filter: blur(16px);
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }

    .search-row {
      display: flex;
      gap: 1rem;
      align-items: center;
    }
    .search-input {
      flex: 1;
      background: rgba(0, 0, 0, 0.4);
      border: 1px solid var(--border-color);
      border-radius: 10px;
      padding: 0.65rem 1.2rem;
      color: #fff;
      font-size: 0.92rem;
      font-family: inherit;
      outline: none;
      transition: border-color 0.2s;
    }
    .search-input:focus { border-color: var(--cyan-glow); box-shadow: 0 0 10px rgba(6, 182, 212, 0.3); }

    .category-chips {
      display: flex;
      flex-wrap: wrap;
      gap: 0.6rem;
    }
    .cat-chip {
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--border-color);
      color: var(--text-secondary);
      font-size: 0.8rem;
      font-weight: 600;
      padding: 0.35rem 0.85rem;
      border-radius: 20px;
      cursor: pointer;
      transition: all 0.2s;
    }
    .cat-chip:hover { color: #fff; background: rgba(255, 255, 255, 0.08); }
    .cat-chip.active {
      background: var(--cyan-glow);
      color: #000;
      border-color: var(--cyan-glow);
      font-weight: 700;
      box-shadow: 0 0 12px rgba(6, 182, 212, 0.4);
    }

    .regions-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
      gap: 1.5rem;
      margin-bottom: 3rem;
    }

    .region-card {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 16px;
      padding: 1.4rem;
      backdrop-filter: blur(12px);
      box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
      display: flex;
      flex-direction: column;
      gap: 0.9rem;
      transition: all 0.25s ease;
      position: relative;
      overflow: hidden;
    }
    .region-card:hover {
      border-color: var(--cyan-glow);
      transform: translateY(-4px);
      box-shadow: 0 15px 35px rgba(6, 182, 212, 0.2);
    }
    .region-card::before {
      content: '';
      position: absolute;
      top: 0; left: 0; right: 0; height: 3px;
      background: linear-gradient(90deg, var(--cyan-glow), transparent);
    }

    .region-card-top {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
    }
    .reg-id-badge {
      font-size: 0.72rem;
      font-family: monospace;
      color: var(--text-muted);
      background: rgba(255, 255, 255, 0.05);
      padding: 0.2rem 0.5rem;
      border-radius: 6px;
    }
    .reg-name {
      font-size: 1.25rem;
      font-weight: 800;
      color: #fff;
    }
    .reg-pref {
      font-size: 0.82rem;
      color: var(--cyan-glow);
      font-weight: 600;
    }
    .reg-stage-pill {
      font-size: 0.75rem;
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid var(--border-color);
      padding: 0.25rem 0.6rem;
      border-radius: 6px;
      color: var(--text-secondary);
    }

    .reg-item-box {
      background: rgba(0, 0, 0, 0.25);
      border-radius: 10px;
      padding: 0.7rem 0.9rem;
      border: 1px solid rgba(255, 255, 255, 0.03);
    }
    .reg-item-label {
      font-size: 0.72rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 0.25rem;
      display: flex;
      align-items: center;
      gap: 0.35rem;
    }
    .lbl-spots { color: #38bdf8; }
    .lbl-food { color: #fbbf24; }
    .lbl-hotel { color: #34d399; }
    .lbl-pet { color: #f472b6; }
    .lbl-weather { color: #a78bfa; }

    .reg-item-val {
      font-size: 0.84rem;
      color: var(--text-secondary);
      line-height: 1.45;
    }

    /* --- TAB 3: SAFETY & PROTOCOL STYLES --- */
    .protocol-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(460px, 1fr));
      gap: 1.8rem;
      margin-bottom: 3rem;
    }

    .proto-box {
      background: var(--bg-panel);
      border: 1px solid var(--border-color);
      border-radius: 18px;
      padding: 1.8rem;
      backdrop-filter: blur(16px);
      box-shadow: 0 15px 35px rgba(0, 0, 0, 0.4);
    }
    .proto-box-title {
      font-size: 1.2rem;
      font-weight: 800;
      color: #fff;
      display: flex;
      align-items: center;
      gap: 0.6rem;
      margin-bottom: 1.2rem;
      padding-bottom: 0.6rem;
      border-bottom: 1px solid var(--border-color);
    }
    .proto-list {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 0.9rem;
    }
    .proto-list li {
      background: rgba(0, 0, 0, 0.25);
      border-radius: 10px;
      padding: 0.85rem 1rem;
      border: 1px solid rgba(255, 255, 255, 0.04);
      font-size: 0.88rem;
      color: var(--text-secondary);
      line-height: 1.5;
    }
    .proto-list strong { color: #fff; }

    /* Toast */
    #toast {
      position: fixed;
      bottom: 2rem;
      right: 2rem;
      background: #10b981;
      color: #000;
      padding: 0.8rem 1.4rem;
      border-radius: 10px;
      font-weight: 700;
      box-shadow: 0 10px 25px rgba(0,0,0,0.5);
      display: none;
      z-index: 9999;
      animation: fadeIn 0.3s;
    }
    @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }

    footer {
      text-align: center;
      padding: 2.5rem 1rem;
      color: var(--text-muted);
      font-size: 0.85rem;
      border-top: 1px solid var(--border-color);
    }

    @media (max-width: 1080px) {
      .cockpit-stage { grid-template-columns: 1fr; }
      .protocol-grid { grid-template-columns: 1fr; }
    }
  </style>
</head>
<body>

  <!-- Top Header HUD -->
  <header>
    <div class="header-inner">
      <div class="brand-title-wrap">
        <div class="protocol-badge">
          <div class="pulse-dot"></div>
          <span>CHRONO-LOOP 5.0 · 西藏自驾数字孪生全景指挥舱</span>
        </div>
        <h1>46天西藏全境全疆域动态可视化路书</h1>
      </div>

      <!-- Navigation Tabs -->
      <div class="view-tabs">
        <button class="tab-btn active" onclick="switchTab('cockpit', this)">
          <span>🛰️</span>
          <span>动态巡航大屏</span>
        </button>
        <button class="tab-btn" onclick="switchTab('regions', this)">
          <span>🗺️</span>
          <span>49行政区纯玩图鉴</span>
        </button>
        <button class="tab-btn" onclick="switchTab('safety', this)">
          <span>🛡️</span>
          <span>棋手防御与银发中枢</span>
        </button>
      </div>

      <!-- Telemetry Pills -->
      <div class="hud-telemetry">
        <div class="telemetry-pill">
          <span class="tel-label">巡航天数</span>
          <span class="tel-val" id="hud-day">D01 / 46</span>
        </div>
        <div class="telemetry-pill">
          <span class="tel-label">睡眠海拔</span>
          <span class="tel-val" id="hud-alt" style="color: var(--emerald-glow);">1500m</span>
        </div>
        <div class="telemetry-pill">
          <span class="tel-label">累计里程</span>
          <span class="tel-val" id="hud-km">190 km</span>
        </div>
        <div class="telemetry-pill">
          <span class="tel-label">边防合规校验</span>
          <span class="tel-val" style="color: #34d399; font-size: 0.82rem;">✅ 规避日喀则</span>
        </div>
      </div>
    </div>
  </header>

  <div class="main-container">

    <!-- ================= TAB 1: COCKPIT ================= -->
    <div class="tab-pane active" id="pane-cockpit">

      <!-- Playback Bar -->
      <div class="playback-bar">
        <div class="playback-controls">
          <button class="btn-ctrl btn-play-hero" id="btn-play" onclick="togglePlay()">
            <span id="play-icon">▶</span>
            <span id="play-text">启动巡航动效</span>
          </button>
          <button class="btn-ctrl" onclick="stepDay(-1)">◀ 上一日</button>
          <button class="btn-ctrl" onclick="stepDay(1)">下一日 ▶</button>
          
          <div class="speed-pills">
            <div class="speed-chip active" onclick="setSpeed(1, this)">1x</div>
            <div class="speed-chip" onclick="setSpeed(2, this)">2x</div>
            <div class="speed-chip" onclick="setSpeed(4, this)">4x</div>
          </div>
        </div>

        <div class="scrubber-zone">
          <span style="font-size: 0.8rem; color: var(--text-muted); font-family: monospace;">D01</span>
          <input type="range" class="timeline-range" id="timeline-slider" min="1" max="46" value="1" oninput="onSliderMove(this.value)">
          <span style="font-size: 0.8rem; color: var(--text-muted); font-family: monospace;">D46</span>
        </div>
      </div>

      <!-- Split Stage: Map + Spotlight -->
      <div class="cockpit-stage">
        
        <!-- Interactive Vector Map -->
        <div class="map-pod">
          <div class="pod-header">
            <div class="pod-title">
              <span>🗺️</span>
              <span>全闭环巡航动态轨迹图 (Live Vehicle Tracking)</span>
            </div>
            <span style="font-size: 0.8rem; color: var(--text-muted);">点击任意节点即可瞬时巡航</span>
          </div>

          <div class="svg-viewport">
            <svg viewBox="0 0 1100 500" width="100%" height="auto" id="main-map-svg">
              <defs>
                <linearGradient id="trailG318" x1="0%" y1="100%" x2="100%" y2="0%">
                  <stop offset="0%" stop-color="#06b6d4" /><stop offset="100%" stop-color="#3b82f6" />
                </linearGradient>
                <linearGradient id="trailShannan" x1="0%" y1="0%" x2="100%" y2="100%">
                  <stop offset="0%" stop-color="#a855f7" /><stop offset="100%" stop-color="#ec4899" />
                </linearGradient>
                <linearGradient id="trailAli" x1="0%" y1="100%" x2="100%" y2="0%">
                  <stop offset="0%" stop-color="#f59e0b" /><stop offset="100%" stop-color="#fbbf24" />
                </linearGradient>
                <linearGradient id="trailG317" x1="0%" y1="0%" x2="100%" y2="100%">
                  <stop offset="0%" stop-color="#10b981" /><stop offset="100%" stop-color="#059669" />
                </linearGradient>
                <filter id="glowEffect">
                  <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
                  <feMerge><feMergeNode in="coloredBlur"/><feMergeNode in="SourceGraphic"/></feMerge>
                </filter>
              </defs>

              <!-- Grid Lines -->
              <line x1="50" y1="90" x2="1050" y2="90" stroke="rgba(255,255,255,0.03)" stroke-dasharray="4" />
              <line x1="50" y1="210" x2="1050" y2="210" stroke="rgba(255,255,255,0.03)" stroke-dasharray="4" />
              <line x1="50" y1="360" x2="1050" y2="360" stroke="rgba(255,255,255,0.03)" stroke-dasharray="4" />

              <!-- Region Watermarks -->
              <text x="40" y="45" fill="rgba(255,255,255,0.18)" font-size="12" font-weight="700">【阿里全境 / 持阿里边防证】</text>
              <text x="380" y="45" fill="rgba(255,255,255,0.18)" font-size="12" font-weight="700">【藏北内陆 / 免边防证走廊】</text>
              <text x="820" y="45" fill="rgba(255,255,255,0.18)" font-size="12" font-weight="700">【川西雅安·大渡河与攀西】</text>

              <!-- Trail 1: G318 Outbound -->
              <path d="M 980 440 L 950 360 L 900 240 L 830 250 L 750 280 L 670 290 L 610 290 L 550 270 L 490 270 L 450 280" 
                    fill="none" stroke="url(#trailG318)" stroke-width="4.5" stroke-linecap="round" opacity="0.65" />

              <!-- Trail 2: Nyingchi -> Shannan -> Yamdrok -> Lhasa -->
              <path d="M 450 280 L 410 330 L 370 340 L 390 260" 
                    fill="none" stroke="url(#trailShannan)" stroke-width="4.5" stroke-linecap="round" opacity="0.65" />

              <!-- Trail 3: Lhasa -> Damxung -> Baingoin -> Nyima -> Gerze -> Shiquanhe -->
              <path d="M 390 260 L 340 200 L 260 190 L 170 200 L 90 230" 
                    fill="none" stroke="url(#trailAli)" stroke-width="4.5" stroke-linecap="round" opacity="0.65" />

              <!-- Trail 3B: Ali internal (Zanda -> Burang -> Pangong) -->
              <path d="M 90 230 L 65 310 L 105 370 L 90 230 L 70 140 L 90 230" 
                    fill="none" stroke="#fbbf24" stroke-width="2.5" stroke-dasharray="4 3" opacity="0.7" />

              <!-- Trail 4: G317 Return -->
              <path d="M 90 230 L 170 200 L 260 190 L 380 170 L 520 170 L 620 170 L 710 180 L 810 220 L 900 310 L 950 360 L 980 440" 
                    fill="none" stroke="url(#trailG317)" stroke-width="4.5" stroke-dasharray="8 4" stroke-linecap="round" opacity="0.65" />

              <!-- Waypoint Anchors -->
              <g id="svg-nodes-group"></g>

              <!-- Moving Active Vehicle Beacon -->
              <g id="vehicle-beacon" transform="translate(980, 440)">
                <circle cx="0" cy="0" r="18" fill="rgba(6, 182, 212, 0.25)">
                  <animate attributeName="r" values="10;26;10" dur="1.8s" repeatCount="indefinite"/>
                  <animate attributeName="opacity" values="0.8;0;0.8" dur="1.8s" repeatCount="indefinite"/>
                </circle>
                <circle cx="0" cy="0" r="8" fill="#06b6d4" stroke="#fff" stroke-width="2.5" filter="url(#glowEffect)"/>
                <text x="14" y="-12" fill="#38bdf8" font-size="11" font-weight="bold" id="vehicle-tag">🚙 当前车队</text>
              </g>
            </svg>
          </div>
        </div>

        <!-- Spotlight Card -->
        <div class="spotlight-pod" id="spotlight-card">
          <div class="spot-top">
            <div class="spot-day-badge">
              <span id="spot-day">DAY 01</span>
              <span class="spot-stage-chip" id="spot-stage">攀西走廊</span>
            </div>
            <div class="spot-alt-chip" id="spot-alt">🌙 宿: 1500m</div>
          </div>

          <div class="spot-route-name" id="spot-route">攀枝花 ➔ 德昌风车 ➔ 西昌邛海</div>

          <div class="spot-metrics-grid">
            <div class="spot-metric-tag" id="spot-time">⏱️ 纯驾 3.5h</div>
            <div class="spot-metric-tag" id="spot-km">🛣️ 190 km</div>
            <div class="spot-metric-tag" id="spot-safe">🛡️ 边防证免检</div>
          </div>

          <div class="spot-block">
            <div class="spot-block-title">✨ 今日核心纯玩视界 (无台阶/免门票)</div>
            <div class="spot-block-body" id="spot-scenic">安宁河谷平原、德昌白色风机群、邛海环湖平坦绿道。</div>
          </div>

          <div class="spot-block">
            <div class="spot-block-title title-food">🍲 农夫适老真滋味 (温润高能)</div>
            <div class="spot-block-body" id="spot-food">西昌鲜菌土鸡清汤锅、邛海清蒸银鱼、现蒸杂粮软糕。</div>
          </div>

          <div class="spot-block">
            <div class="spot-block-title title-warn">🚫 棋手红线避坑指南</div>
            <div class="spot-block-body" id="spot-warn">避免进西昌过于重油重辣的火盆烧烤街以防肠胃失调。</div>
          </div>

          <div class="spot-nav-action">
            <span class="nav-str" id="spot-nav">攀枝花市区 -> 德昌县风电场 -> 邛海湿地</span>
            <button class="btn-copy-nav" onclick="copyActiveNav()">一键复制手机导航</button>
          </div>
        </div>

      </div>

      <!-- Synchronized Altitude Chart -->
      <div class="alt-panel">
        <div class="pod-header">
          <div class="pod-title">
            <span>📈</span>
            <span>全程静息睡眠海拔动效相图 (Elevation Synchronizer)</span>
          </div>
          <span style="font-size: 0.8rem; color: var(--text-muted);">首周夜宿严格压制在3000m以下 · 动态黄光标指引当前日</span>
        </div>

        <div class="alt-svg-wrap">
          <svg viewBox="0 0 1050 240" width="100%" height="100%" preserveAspectRatio="none" id="alt-chart-svg">
            <defs>
              <linearGradient id="chartFillGrad" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" stop-color="rgba(6, 182, 212, 0.38)" />
                <stop offset="100%" stop-color="rgba(16, 185, 129, 0.0)" />
              </linearGradient>
            </defs>

            <!-- Warning bands -->
            <line x1="40" y1="40" x2="1020" y2="40" stroke="rgba(244, 63, 94, 0.35)" stroke-dasharray="4" />
            <text x="50" y="32" fill="#f43f5e" font-size="10">⛔ 4200m 高原无供氧红线</text>

            <line x1="40" y1="90" x2="1020" y2="90" stroke="rgba(245, 158, 11, 0.35)" stroke-dasharray="4" />
            <text x="50" y="82" fill="#f59e0b" font-size="10">⚠️ 3000m 高原过渡线 (林芝2900m/波密2700m/天全750m安全保障)</text>

            <!-- Chart Polygon -->
            <polygon points="
              55,220
              55,185 90,215 125,120 160,120 195,122 230,115 265,75 300,120 335,95 370,95
              405,62 440,55 475,55 510,20 545,20 580,30 615,55 650,45 685,30 720,30
              755,20 790,40 825,80 860,82 895,70 930,165 965,210 1000,200
              1000,220
            " fill="url(#chartFillGrad)" />

            <!-- Chart Polyline -->
            <polyline points="
              55,185 90,215 125,120 160,120 195,122 230,115 265,75 300,120 335,95 370,95
              405,62 440,55 475,55 510,20 545,20 580,30 615,55 650,45 685,30 720,30
              755,20 790,40 825,80 860,82 895,70 930,165 965,210 1000,200
            " fill="none" stroke="#06b6d4" stroke-width="3" stroke-linecap="round" />

            <!-- Dynamic Indicator -->
            <g id="alt-tracker" transform="translate(55, 0)">
              <line x1="0" y1="10" x2="0" y2="220" stroke="#f59e0b" stroke-width="2" stroke-dasharray="2" />
              <circle cx="0" cy="185" r="5.5" fill="#f59e0b" stroke="#fff" stroke-width="1.5" id="alt-tracker-dot" />
            </g>
          </svg>
        </div>
      </div>

      <!-- Quick Days Tray -->
      <div class="days-scroller-wrap">
        <div class="scroller-head">
          <span>🗓️</span>
          <span>46天全域行程节点盘 (点击快速载入对应天数)</span>
        </div>
        <div class="days-tray" id="days-scroller"></div>
      </div>

    </div>

    <!-- ================= TAB 2: 49 REGIONS EXPLORER ================= -->
    <div class="tab-pane" id="pane-regions">
      
      <!-- Filter Deck -->
      <div class="filter-deck">
        <div class="search-row">
          <input type="text" class="search-input" id="region-search" placeholder="🔍 搜索49行政区、景点、冷水鱼、松茸、古格王朝、土林、免票..." oninput="filterRegions()">
          <span style="font-size: 0.85rem; color: var(--text-muted); font-family: monospace;" id="match-counter">显示 49 / 49 地区</span>
        </div>
        <div class="category-chips" id="cat-chips">
          <div class="cat-chip active" onclick="selectCategory('ALL', this)">全部 49 行政区</div>
          <div class="cat-chip" onclick="selectCategory('川西雅安·大渡河', this)">川西雅安与大渡河</div>
          <div class="cat-chip" onclick="selectCategory('川西甘孜G318', this)">甘孜G318翡翠阶梯</div>
          <div class="cat-chip" onclick="selectCategory('藏东昌都G318', this)">藏东昌都南线</div>
          <div class="cat-chip" onclick="selectCategory('林芝雪域江南', this)">林芝雪域江南</div>
          <div class="cat-chip" onclick="selectCategory('藏南雅江摇篮', this)">藏南山南文明摇篮</div>
          <div class="cat-chip" onclick="selectCategory('拉萨圣城及周边', this)">拉萨圣城平原</div>
          <div class="cat-chip" onclick="selectCategory('藏北内陆湖泊', this)">藏北一错再错</div>
          <div class="cat-chip" onclick="selectCategory('西极阿里全境', this)">西极阿里秘境</div>
          <div class="cat-chip" onclick="selectCategory('川藏北线G317', this)">川藏北线G317</div>
        </div>
      </div>

      <!-- 49 Regions Grid -->
      <div class="regions-grid" id="regions-grid"></div>

    </div>

    <!-- ================= TAB 3: SAFETY & PROTOCOL ================= -->
    <div class="tab-pane" id="pane-safety">
      <div class="protocol-grid">
        
        <!-- Box 1: Single Driver Pacing -->
        <div class="proto-box">
          <div class="proto-box-title">
            <span>🛡️</span>
            <span>单人驾驶（35岁男独驾）防疲劳防御法</span>
          </div>
          <ul class="proto-list">
            <li><strong>2-2-2 巡航节奏律：</strong>每连续驾驶 2 小时，强制熄火 20 分钟；车上全员下车在安全开阔地做扩胸深呼吸与下肢拉伸。</li>
            <li><strong>神经与体温抗昏睡：</strong>车内备足云南薄荷脑鼻通吸入棒、冷萃纯苦丁茶、柠檬水；阿里路段紫外线极强，驾驶员全天佩戴防眩偏光镜。</li>
            <li><strong>碳水节制法：</strong>午餐严禁大量摄入高升糖米面或油炸食物，以防胰岛素骤升导致餐后昏睡；以清炖牛肉、蒸南瓜、坚果为主。</li>
            <li><strong>下坡制动铁律：</strong>觉巴山、怒江72拐、东达山下坡，必须挂入低速挡（M2/L挡）利用发动机制动，严禁全程踩刹车导致热衰退。</li>
          </ul>
        </div>

        <!-- Box 2: Elderly Cardiovascular & Altitude Care -->
        <div class="proto-box">
          <div class="proto-box-title">
            <span>❤️</span>
            <span>两位长辈（60+岁）心脑血管与低反四维红线</span>
          </div>
          <ul class="proto-list">
            <li><strong>前7天绝对控高律：</strong>入藏前7晚严格住宿于海拔 3000m 以下（天全750m ➔ 雅江2600m ➔ 巴塘2580m ➔ 波密2700m ➔ 林芝2900m），使得骨髓平稳合成红细胞。</li>
            <li><strong>早晚血氧雷达监测：</strong>随身配备2台医用指夹式血氧仪；早起与晚间各测一次，静息血氧需稳定在 80% 以上；低于 75% 立即用车载 10L 医用氧气瓶供氧。</li>
            <li><strong>极境高海拔开氧策略：</strong>藏北班戈（4700m）、尼玛（4500m）、改则（4500m）夜间酒店必须强制开启中央弥散供氧系统，使客房等效海拔降至2800m。</li>
            <li><strong>高海拔四不动作：</strong>不高声说话、不疾步快走上台阶、不洗过烫淋浴（洗澡易缺氧且易感冒）、不饮冰凉水。</li>
          </ul>
        </div>

        <!-- Box 3: Pet Safety Shield -->
        <div class="proto-box">
          <div class="proto-box-title">
            <span>🐕</span>
            <span>携宠（家庭爱犬）全地形安全护甲指南</span>
          </div>
          <ul class="proto-list">
            <li><strong>防烈犬与猛禽铁律：</strong>阿里与藏北无人区常有流浪藏獒与金雕猛禽，爱犬下车必须全程拴紧防爆冲胸背带，严禁让其独自追逐旱獭。</li>
            <li><strong>肉垫护理与粗糙碎石：</strong>札达土林、班公湖碎石滩地表干硬尖锐，每天归寝用温水清洁脚垫并涂抹凡士林滋润，防干裂出血。</li>
            <li><strong>水源安全防线：</strong>藏北色林错、拉昂错多为高盐碱、高矿化度水质，严禁犬只饮用湖水以免引起急性肾衰；全程只喂白开水。</li>
            <li><strong>低温保暖防护：</strong>阿里与藏北夜间气温降至零度以下，犬只必须睡在客房内防风窝垫中，加穿宠物防风保暖马甲。</li>
          </ul>
        </div>

        <!-- Box 4: Border Pass Clearance Matrix -->
        <div class="proto-box">
          <div class="proto-box-title">
            <span>📑</span>
            <span>边防证合规验证走廊（零违约闭环通关）</span>
          </div>
          <ul class="proto-list">
            <li><strong>持证合法覆盖区：</strong>林芝市全境（米林/朗县/工布江达）、山南市全境（浪卡子/乃东/加查）、阿里地区全境（改则/革吉/噶尔/日土/札达/普兰）100%通关。</li>
            <li><strong>日喀则边检避开策略：</strong>因无日喀则边防证，由山南经拉萨直接北上当雄-班戈-尼玛内陆免检走廊（属于那曲市非边控区），完全绕开萨嘎、仲巴等日喀则边控卡点。</li>
            <li><strong>喜马拉雅极高雪峰远眺方案：</strong>珠峰大本营因在定日边控区无法实入；我们在普兰孔雀河谷与岗底斯山口设立远眺平台，近观冈仁波齐、纳木那尼雪峰群，合规且视觉震撼。</li>
            <li><strong>随车证件随时抽查：</strong>边防证纸质原件与身份证放在主驾手套箱最外层，过卡前由主驾一人携带全员身份证与边防证下车核验，长辈无需吹冷风。</li>
          </ul>
        </div>

      </div>
    </div>

  </div>

  <div id="toast">✅ 路线经纬导航点已复制到剪贴板！可在手机高德/百度地图中直接粘贴</div>

  <footer>
    <p>CHRONO-LOOP 5.0 动态路书全息指挥舱 · 攀枝花自驾大本营 · 49行政区纯玩闭环合规典范</p>
  </footer>

  <script>
    // 1. Injected 49 Regions Dataset from Excel
    const rawRegions = ''' + json.dumps(regions, ensure_ascii=False) + r''';

    // 2. 28-Day Cruise Dataset
    const itinerary = [
      {
            "day": 1,
            "tag": "D01",
            "stage": "千里奔袭",
            "route": "攀枝花 ➔ G5京昆高速直达 ➔ 雅安天全318大本营",
            "alt": "750m",
            "altNum": 750,
            "time": "6.5h",
            "km": "520km",
            "safe": "免边防证",
            "scenic": "【纯赶路坚决不观景】沿G5京昆高速一路北上，中途服务区休整换气，直插川藏318起点天全县，为翻山养精蓄锐。",
            "food": "天全思经高山冷水鱼（清汤滚沸极鲜嫩，优质蛋白易消化）、温热土鸡汤，温和养胃。",
            "warn": "今日以安全赶路为唯一目标，途中各大风景区坚决不进；天全海拔仅750m，超富氧让全员深度安睡。",
            "nav": "起点: 攀枝花市政府 ➔ 途经点1: 西昌服务区 ➔ 途经点2: 石棉服务区 ➔ 途经点3: 雅安西收费站 ➔ 终点: 天全318自驾大本营",
            "x": 980,
            "y": 440,
            "chartX": 40,
            "chartY": 215
      },
      {
            "day": 2,
            "tag": "D02",
            "stage": "川西翡翠梯",
            "route": "雅安天全 ➔ 二郎山特长隧道 ➔ 泸定 ➔ 康定情歌城",
            "alt": "2560m",
            "altNum": 2560,
            "time": "3.5h",
            "km": "140km",
            "safe": "免边防证",
            "scenic": "穿越气候分界线二郎山特长隧道、大渡河铁索桥远眺、抵达康定情歌广场与跑马山脚。",
            "food": "康定老字号清炖牦牛杂汤锅、蒸热青稞饼、热红糖水，迅速补充爬升糖原。",
            "warn": "【CAS-α安全阶梯开启】今夜宿康定2560m，不急于翻折多山，为心脑血管留出充分代偿时间。",
            "nav": "起点: 天全318大本营 ➔ 途经点1: 二郎山特长隧道天全端 ➔ 途经点2: 泸定桥南广场 ➔ 终点: 康定岷山太阳部落酒店",
            "x": 910,
            "y": 240,
            "chartX": 62,
            "chartY": 120
      },
      {
            "day": 3,
            "tag": "D03",
            "stage": "康定代偿",
            "route": "康定市 ➔ 木格措清凉木栈道慢步 ➔ 康定连宿",
            "alt": "2560m",
            "altNum": 2560,
            "time": "1.5h",
            "km": "60km",
            "safe": "免边防证",
            "scenic": "木格措（野人海）纯平无障碍木栈道吸氧慢步、高山杜鹃花海与雪山倒影，折多山前的生理驯化。",
            "food": "热酥油茶配青稞糌粑薄饼、清炖高山土鸡汤，温和滋补。",
            "warn": "康定连宿第二晚！全员血氧稳定在85%以上方可解锁明日翻山；全车检查轮胎与刹车皮。",
            "nav": "起点: 康定市区 ➔ 途经点1: 木格措景区停车场 ➔ 途经点2: 雅拉雪山远眺台 ➔ 终点: 康定岷山太阳部落酒店",
            "x": 900,
            "y": 240,
            "chartX": 84,
            "chartY": 120
      },
      {
            "day": 4,
            "tag": "D04",
            "stage": "翻山直降",
            "route": "康定 ➔ 折多山4298(车览不停) ➔ 新都桥 ➔ 雅江 ➔ 巴塘",
            "alt": "2580m",
            "altNum": 2580,
            "time": "6.0h",
            "km": "305km",
            "safe": "免边防证",
            "scenic": "折多山垭口车内打卡不停留、新都桥光影十里长廊、天路十八弯盘旋路、毛垭草原与姊妹湖，直降金沙江畔巴塘。",
            "food": "巴塘传统团结包子（蒸满一整屉，土豆鲜肉软嫩多汁）、高山雪梨银耳羹润燥。",
            "warn": "理塘海拔4014m胃肠动力弱，坚决不在理塘留宿也不吃重油火锅；直降巴塘2580m果乡保命安睡。",
            "nav": "起点: 康定市区 ➔ 途经点1: 折多山垭口观雪台 ➔ 途经点2: 天路十八弯观景台 ➔ 途经点3: 海子山姊妹湖 ➔ 终点: 巴塘君悦假日酒店",
            "x": 780,
            "y": 270,
            "chartX": 106,
            "chartY": 122
      },
      {
            "day": 5,
            "tag": "D05",
            "stage": "金沙江蓄力",
            "route": "巴塘县城 ➔ 竹巴笼湿地漫步 ➔ 巴塘苹果园慢游",
            "alt": "2580m",
            "altNum": 2580,
            "time": "1.0h",
            "km": "40km",
            "safe": "免边防证",
            "scenic": "【农夫等天晴·海通沟天气观测日】金沙江畔竹巴笼湿地散步，爱犬在果园绿荫自由奔跑，全家养精蓄锐。",
            "food": "巴塘高山生态苹果汁、清蒸金沙江江鱼、现蒸杂粮糕，清淡少油好吸收。",
            "warn": "海通沟入藏咽喉若遇雨顺延，今日在巴塘确认前方路况与通关检查站；全员测血氧与血压。",
            "nav": "起点: 巴塘君悦假日酒店 ➔ 途经点1: 竹巴笼湿地观景台 ➔ 途经点2: 巴塘弦子广场 ➔ 终点: 巴塘君悦假日酒店",
            "x": 770,
            "y": 275,
            "chartX": 128,
            "chartY": 122
      },
      {
            "day": 6,
            "tag": "D06",
            "stage": "跨江入藏",
            "route": "巴塘 ➔ 竹巴笼金沙江大桥(入藏) ➔ 芒康 ➔ 澜沧江如美",
            "alt": "2640m",
            "altNum": 2640,
            "time": "3.5h",
            "km": "160km",
            "safe": "身份证核验",
            "scenic": "跨金沙江大桥正式入藏！跨越海通沟绝壁公路、翻拉乌山高山草甸，落宿澜沧江深切暖谷如美镇。",
            "food": "如美镇澜沧江特色石板豆腐、清炖萝卜土鸡汤，口感清润暖胃。",
            "warn": "芒康县城海拔3875m易引发长辈头痛，午后翻过拉乌山必须直接落宿如美(2640m)避寒。",
            "nav": "起点: 巴塘迎宾大道 ➔ 途经点1: 竹巴笼金沙江大桥检查站 ➔ 途经点2: 芒康县中石化 ➔ 终点: 如美镇竹卡村客栈",
            "x": 700,
            "y": 285,
            "chartX": 150,
            "chartY": 115
      },
      {
            "day": 7,
            "tag": "D07",
            "stage": "高飞低宿",
            "route": "如美 ➔ 觉巴山绝壁 ➔ 东达山5130 ➔ 左贡车览 ➔ 八宿",
            "alt": "3260m",
            "altNum": 3260,
            "time": "6.0h",
            "km": "270km",
            "safe": "身份证核验",
            "scenic": "觉巴山30公里绝壁盘山天路、东达山5130m垭口车内打卡、怒江72拐大地奇观天台，直下八宿河谷。",
            "food": "八宿原汁清炖羊肉排（青盐白煮无膻味）、热糌粑糊配高山甜茶。",
            "warn": "【棋手高飞低宿妙招】左贡(3750m)过境不停宿，直降海拔更低、气候更温和的八宿(3260m)安寝！",
            "nav": "起点: 如美镇 ➔ 途经点1: 觉巴山观景台 ➔ 途经点2: 东达山垭口纪念碑 ➔ 途经点3: 怒江72拐全景天台 ➔ 终点: 八宿海螺国际大酒店",
            "x": 610,
            "y": 290,
            "chartX": 172,
            "chartY": 75
      },
      {
            "day": 8,
            "tag": "D08",
            "stage": "冰川林海",
            "route": "八宿 ➔ 安久拉山4468 ➔ 然乌湖北岸 ➔ 米堆观光车 ➔ 波密古乡",
            "alt": "2600m",
            "altNum": 2600,
            "time": "5.0h",
            "km": "230km",
            "safe": "身份证核验",
            "scenic": "然乌湖晨雾倒影、米堆冰川乘舒适观光车远眺冰瀑、松宗盔甲山岩层，扎进波密原始云杉森林。",
            "food": "波密野生天麻炖土鸡、手撕高山黑木耳拌热时蔬，在超高负氧离子中饱餐一顿。",
            "warn": "米堆冰川只乘观光车到观景平台，长辈严禁徒步上冰舌；夜宿波密2600m，心肺彻底放松。",
            "nav": "起点: 八宿海螺大酒店 ➔ 途经点1: 然乌湖观景台 ➔ 途经点2: 米堆冰川景区售票处 ➔ 途经点3: 松宗镇盔甲山 ➔ 终点: 波密古乡湖精品客栈",
            "x": 550,
            "y": 270,
            "chartX": 194,
            "chartY": 120
      },
      {
            "day": 9,
            "tag": "D09",
            "stage": "波密休耕",
            "route": "波密古乡 ➔ 岗云杉林纯平草湖步道 ➔ 古乡湖连宿",
            "alt": "2600m",
            "altNum": 2600,
            "time": "1.0h",
            "km": "30km",
            "safe": "持林芝证",
            "scenic": "【农夫48h休耕枢纽】岗云杉林草湖纯平步道漫步，古乡湖冰川倒影，全员深度安眠修复。",
            "food": "波密高山藏香猪清炖萝卜汤、热苹果茶，为进藏腹地蓄满维生素储备。",
            "warn": "全天严禁剧烈爬坡，享受林海纯氧漫步；主驾彻底深度睡眠消除前段盘山神经疲劳。",
            "nav": "起点: 波密古乡客栈 ➔ 途经点1: 岗云杉林景区大门 ➔ 途经点2: 古乡湖环湖木栈道 ➔ 终点: 波密古乡湖精品客栈",
            "x": 540,
            "y": 270,
            "chartX": 216,
            "chartY": 120
      },
      {
            "day": 10,
            "tag": "D10",
            "stage": "南迦双窗",
            "route": "波密 ➔ 通麦大桥 ➔ 鲁朗石锅鸡 ➔ 色季拉山口 ➔ 米林索松村",
            "alt": "2950m",
            "altNum": 2950,
            "time": "4.5h",
            "km": "210km",
            "safe": "持林芝证",
            "scenic": "通麦特大桥天险变通途、鲁朗扎西岗村田园高山牧场、色季拉山口远眺，抵索松村直面南迦巴瓦峰。",
            "food": "正宗鲁朗墨脱石锅鸡（富锌皂石锅微火慢煨，手掌参配野生黄菇），鲜美绝伦滋养气血。",
            "warn": "夜宿索松村（2950m）客栈推窗看雪山金顶！索松村连住两晚，南迦巴瓦晨昏开窗概率翻倍。",
            "nav": "起点: 古乡客栈 ➔ 途经点1: 通麦特大桥 ➔ 途经点2: 鲁朗镇扎西岗村 ➔ 途经点3: 色季拉山口 ➔ 终点: 米林市索松村观景民宿",
            "x": 480,
            "y": 275,
            "chartX": 238,
            "chartY": 95
      },
      {
            "day": 11,
            "tag": "D11",
            "stage": "索松秘境",
            "route": "索松村 ➔ 雅鲁藏布大峡谷大渡卡遗址 ➔ 索松连宿",
            "alt": "2950m",
            "altNum": 2950,
            "time": "1.0h",
            "km": "30km",
            "safe": "持林芝证",
            "scenic": "南迦巴瓦峰日出晨曦倒影、大渡卡古堡遗址、雅鲁藏布江大峡谷深切江湾与佛掌沙丘奇观。",
            "food": "索松村藏家风干牦牛肉煲、清炒高原芥蓝、热甜茶。",
            "warn": "今日零长途驾驶，爱犬在峡谷草甸尽情奔跑；全员在海拔3000m以下完成最后一道生理储备。",
            "nav": "起点: 索松村客栈 ➔ 途经点1: 大渡卡遗址 ➔ 途经点2: 佛掌沙丘观景点 ➔ 终点: 索松村观景民宿",
            "x": 470,
            "y": 275,
            "chartX": 260,
            "chartY": 95
      },
      {
            "day": 12,
            "tag": "D12",
            "stage": "藏南沿江",
            "route": "索松村 ➔ G219沿江生态道 ➔ 朗县冲康核桃林 ➔ 加查",
            "alt": "3200m",
            "altNum": 3200,
            "time": "4.5h",
            "km": "230km",
            "safe": "持山南证",
            "scenic": "沿G219雅江沿江风情道西行，穿行冲康千年古核桃林、达布大峡谷开阔水系，抵达加查县。",
            "food": "加查核桃清蒸蛋、山南清炖冷水鱼豆腐汤、热青稞糌粑粥暖胃强心。",
            "warn": "沿江峡谷野生猕猴较多，严禁开窗投喂以防抓伤；路况极佳全柏油，车速控制在60km/h。",
            "nav": "起点: 索松村民宿 ➔ 途经点1: 朗县冲康庄园古核桃林 ➔ 途经点2: 加查达布峡谷观景台 ➔ 终点: 加查县天海宾馆",
            "x": 430,
            "y": 320,
            "chartX": 282,
            "chartY": 80
      },
      {
            "day": 13,
            "tag": "D13",
            "stage": "雅江摇篮",
            "route": "加查 ➔ 桑日马鹿保护区 ➔ 乃东区山南泽当",
            "alt": "3560m",
            "altNum": 3560,
            "time": "3.5h",
            "km": "160km",
            "safe": "持山南证",
            "scenic": "藏木水电高峡平湖、桑日沿江马鹿保护区、山南乃东西藏第一座宫殿雍布拉康山脚原野。",
            "food": "乃东荞麦煎粑、山南清炖牦牛骨汤配高山萝卜，滋补补钙。",
            "warn": "山南泽当海拔3560m，为山南行政医疗核心，三甲医院近在咫尺，安全感极强。",
            "nav": "起点: 加查天海宾馆 ➔ 途经点1: 桑日县雅江特大桥 ➔ 途经点2: 雍布拉康山脚观景台 ➔ 终点: 山南市泽当饭店",
            "x": 400,
            "y": 330,
            "chartX": 304,
            "chartY": 62
      },
      {
            "day": 14,
            "tag": "D14",
            "stage": "圣湖无返",
            "route": "山南泽当 ➔ 扎囊沙丘 ➔ 浪卡子(羊湖东拉乡水际) ➔ 曲水 ➔ 拉萨",
            "alt": "3650m",
            "altNum": 3650,
            "time": "5.0h",
            "km": "240km",
            "safe": "持山南证",
            "scenic": "【消灭拉萨回头路·顺道穿越】扎囊沙丘、浪卡子羊卓雍措南岸东拉乡水际公路（免票亲水、车轮贴水草）、拉萨河谷。",
            "food": "拉萨阿可丁传统藏面（牦牛骨清汤爽滑面条，易嚼好消化）、微甜酥油茶润肠燥。",
            "warn": "避开岗巴拉高收费观景台刺骨强风，顺路穿越羊湖水际线直达拉萨，省去原案260km折返空耗！",
            "nav": "起点: 山南泽当饭店 ➔ 途经点1: 扎囊沙丘生态公园 ➔ 途经点2: 羊卓雍措东拉乡水际公路 ➔ 途经点3: 曲水雅江大桥 ➔ 终点: 拉萨圣地天堂洲际大饭店",
            "x": 370,
            "y": 340,
            "chartX": 326,
            "chartY": 55
      },
      {
            "day": 15,
            "tag": "D15",
            "stage": "圣城修养",
            "route": "拉萨圣城沉浸慢游（布达拉宫预约参观/八廓街甜茶）",
            "alt": "3650m",
            "altNum": 3650,
            "time": "0.5h",
            "km": "15km",
            "safe": "市内自由",
            "scenic": "【王翼迟攻兑现】第15天全员血氧处于巅峰，从容完成布达拉宫缓行参观；午后仓姑寺露天庭院喝甜茶。",
            "food": "仓姑寺老甜茶馆清茶一壶、热蒸素包、清淡藏式炖牛蹄筋（胶原蛋白丰富，软糯无骨）。",
            "warn": "布宫台阶慢行，心率超80%即在平台静息；晚间入住洲际中央弥散供氧客房。",
            "nav": "起点: 洲际大饭店 ➔ 途经点1: 布达拉宫东门 ➔ 途经点2: 仓姑寺甜茶馆 ➔ 途经点3: 药王山观景台 ➔ 终点: 酒店地下车库",
            "x": 390,
            "y": 260,
            "chartX": 348,
            "chartY": 55
      },
      {
            "day": 16,
            "tag": "D16",
            "stage": "拉萨轻环",
            "route": "拉萨 ➔ 堆龙德庆生态步道 ➔ 墨竹工卡日多温泉 ➔ 拉萨",
            "alt": "3650m",
            "altNum": 3650,
            "time": "2.5h",
            "km": "90km",
            "safe": "市内自由",
            "scenic": "堆龙德庆滨河生态步道遛狗漫步、墨竹工卡日多地热天然温泉小憩泡脚，采购进阿里物资。",
            "food": "墨竹工卡清炖放养藏香鸡、手工荞麦冷糕、高山热甜茶。",
            "warn": "今日下午做进阿里前的关键整备：换新空气滤芯、复检刹车油液位、采购车载饮用水4箱与氧气罐。",
            "nav": "起点: 拉萨市区 ➔ 途经点1: 堆龙德庆滨河公园 ➔ 途经点2: 墨竹工卡日多温泉 ➔ 终点: 拉萨圣地天堂洲际",
            "x": 390,
            "y": 260,
            "chartX": 370,
            "chartY": 55
      },
      {
            "day": 17,
            "tag": "D17",
            "stage": "藏北试金",
            "route": "拉萨 ➔ 当雄念青唐古拉山 ➔ 纳木错北岸 ➔ 班戈",
            "alt": "4700m",
            "altNum": 4700,
            "time": "5.5h",
            "km": "330km",
            "safe": "免边防证",
            "scenic": "【G2门关键试金夜】直面念青唐古拉雪山主峰金字塔峰、穿行藏北草原S301、巴木错晚霞，抵班戈县。",
            "food": "藏北高原清炖羊排汤（加少许青盐萝卜白煮，汤清肉嫩驱寒气）、热酥油红糖水。",
            "warn": "【全程最高睡眠海拔4700m】中信大酒店已锁死中央弥散供氧客房，进房立即开氧，夜测血氧必须≥85%。",
            "nav": "起点: 拉萨市区 ➔ 途经点1: 当雄服务区 ➔ 途经点2: 念青唐古拉山观景台 ➔ 途经点3: 巴木错观湖点 ➔ 终点: 班戈中信大酒店(中央供氧)",
            "x": 340,
            "y": 200,
            "chartX": 392,
            "chartY": 20
      },
      {
            "day": 18,
            "tag": "D18",
            "stage": "一错再错",
            "route": "班戈 ➔ G317 ➔ 色林错自然保护区 ➔ 达则错 ➔ 尼玛",
            "alt": "4500m",
            "altNum": 4500,
            "time": "5.0h",
            "km": "330km",
            "safe": "免边防证",
            "scenic": "全新平整柏油路，西藏第一大湖色林错如浩瀚大海、达则错纯净倒影、藏羚羊与藏野驴沿路奔腾。",
            "food": "尼玛热牛肉汤细粉、蒸热南瓜软馍、热开水泡西洋参片，饱腹暖身。",
            "warn": "严禁在湖畔碎石滩下车急跑追逐动物；随车制氧机保持常开，长辈随时深呼吸。",
            "nav": "起点: 班戈县城 ➔ 途经点1: 色林错国家级自然保护区观景天台 ➔ 途经点2: 达则错湖畔停车港湾 ➔ 终点: 尼玛福森大酒店(中央供氧)",
            "x": 260,
            "y": 190,
            "chartX": 414,
            "chartY": 20
      },
      {
            "day": 19,
            "tag": "D19",
            "stage": "当惹雍错",
            "route": "尼玛 ➔ 当惹雍错纯净湖畔 ➔ 文布南村世外桃源 ➔ 尼玛连宿",
            "alt": "4500m",
            "altNum": 4500,
            "time": "2.5h",
            "km": "220km",
            "safe": "免边防证",
            "scenic": "【藏地顶流神湖】探秘当惹雍错蓝与古象雄文明发源地文布南村，湖水深邃湛蓝，雪山倒映如镜。",
            "food": "文布藏家热土豆浓汤、高原风干羊肉麦片粥、热甜茶。",
            "warn": "文布南村海拔4600m，白日短暂停留拍照，下午返回尼玛县城供氧酒店连宿，不增加行李搬运内耗。",
            "nav": "起点: 尼玛福森大酒店 ➔ 途经点1: 当惹雍错观景天台 ➔ 途经点2: 文布南村湖岸 ➔ 终点: 尼玛福森大酒店",
            "x": 250,
            "y": 195,
            "chartX": 436,
            "chartY": 20
      },
      {
            "day": 20,
            "tag": "D20",
            "stage": "挺进阿里",
            "route": "尼玛 ➔ 洞错 ➔ 阿里改则 (持阿里边防证无阻通关)",
            "alt": "4500m",
            "altNum": 4500,
            "time": "6.0h",
            "km": "340km",
            "safe": "持阿里证",
            "scenic": "洞错蓝绿渐变湖岸、正式跨入阿里地区边界（持阿里边防证秒过检查站）、先遣连纪念碑、羌塘旷野。",
            "food": "改则清真牛肉软烂热拉面、高山原汁羊肉骨汤，清爽易嚼好吸收。",
            "warn": "检查站由主驾一人下车持全员身份证及阿里边防证核验；夜宿改则供氧酒店。",
            "nav": "起点: 尼玛县城 ➔ 途经点1: 洞错观景台 ➔ 途经点2: 改则东检查站 ➔ 终点: 改则先遣大酒店(中央供氧)",
            "x": 170,
            "y": 200,
            "chartX": 458,
            "chartY": 20
      },
      {
            "day": 21,
            "tag": "D21",
            "stage": "西极大本营",
            "route": "改则 ➔ G317 ➔ 盐湖乡 ➔ 革吉草原 ➔ 阿里首府狮泉河",
            "alt": "4280m",
            "altNum": 4280,
            "time": "5.5h",
            "km": "360km",
            "safe": "持阿里证",
            "scenic": "【消灭革吉换宿】全平整国道一路畅行，避开革吉4515m简陋住宿，直降狮泉河绿洲大本营！",
            "food": "狮泉河正规川菜馆清汤土鸡汤、手撕高山白菜、清蒸水蛋，温润补给。",
            "warn": "狮泉河配备阿里地区人民医院（全线西极最强医疗点），全楼中央供氧地暖，长辈极度安心。",
            "nav": "起点: 改则先遣大酒店 ➔ 途经点1: 盐湖乡 ➔ 途经点2: 革吉县中石化 ➔ 终点: 阿里大酒店(中央供氧/医疗保障点)",
            "x": 90,
            "y": 230,
            "chartX": 480,
            "chartY": 30
      },
      {
            "day": 22,
            "tag": "D22",
            "stage": "狮泉河整备",
            "route": "阿里狮泉河 48h 深度整备日（车辆例检/暗夜星空）",
            "alt": "4280m",
            "altNum": 4280,
            "time": "0.5h",
            "km": "20km",
            "safe": "持阿里证",
            "scenic": "狮泉河高原盆地绿洲湿地漫步、暗夜星空公园远眺、全车底盘悬挂排查与换机油。",
            "food": "清汤羊肉暖锅、蒸热杂粮窝头、新鲜苹果雪梨汤。",
            "warn": "零长途驾驶休耕日，主驾体能彻底满血复活；采购后续神山圣湖段补给品。",
            "nav": "起点: 阿里大酒店 ➔ 途经点1: 狮泉河水上公园 ➔ 途经点2: 阿里天文台暗夜公园 ➔ 终点: 阿里大酒店",
            "x": 90,
            "y": 230,
            "chartX": 502,
            "chartY": 30
      },
      {
            "day": 23,
            "tag": "D23",
            "stage": "界湖班公",
            "route": "狮泉河 ➔ G219新藏线 ➔ 日土 ➔ 班公湖水鸟乐园 ➔ 狮泉河",
            "alt": "4280m",
            "altNum": 4280,
            "time": "4.0h",
            "km": "240km",
            "safe": "持阿里证",
            "scenic": "中印界湖班公湖东段清甜淡水区（红嘴鸥漫天飞舞、水清见底）、湖畔平坦草甸爱犬欢跃撒欢。",
            "food": "日土热砂锅豆腐丸子煲、西红柿炒蛋配软米饭，温润平实。",
            "warn": "轻车日归无需搬运行李；班公湖边湿地泥泞，车停在硬化观景台慢行，严禁涉水踩陷。",
            "nav": "起点: 狮泉河镇 ➔ 途经点1: 日土县中心广场 ➔ 途经点2: 班公湖国家湿地公园外湖岸 ➔ 终点: 阿里大酒店",
            "x": 70,
            "y": 140,
            "chartX": 524,
            "chartY": 30
      },
      {
            "day": 24,
            "tag": "D24",
            "stage": "象雄土林",
            "route": "狮泉河 ➔ 札达土林地质公园 ➔ 象泉河谷 ➔ 札达县城",
            "alt": "3700m",
            "altNum": 3700,
            "time": "4.5h",
            "km": "230km",
            "safe": "持阿里证",
            "scenic": "穿行世界最大札达土林万壑千峰壮丽峡谷（公路穿行纯免费）、象泉河谷绿洲、古格王朝崖壁古刹遥望。",
            "food": "札达象泉河黄土豆炖风干牛肉（土豆久炖沙绵软烂，牛肉香酥无渣，高能量好消化）。",
            "warn": "【海拔暴降至3700m！】全员宛如进入高原纯氧吧，彻底深睡安眠；古格王朝在山脚仰拍即可。",
            "nav": "起点: 阿里大酒店 ➔ 途经点1: 那木如村 ➔ 途经点2: 札达土林观景台 ➔ 途经点3: 古格王朝山脚 ➔ 终点: 札达土林城堡酒店",
            "x": 65,
            "y": 310,
            "chartX": 546,
            "chartY": 55
      },
      {
            "day": 25,
            "tag": "D25",
            "stage": "札达连宿",
            "route": "札达县城 ➔ 托林寺外围千年古柏 ➔ 象泉河日落金山",
            "alt": "3700m",
            "altNum": 3700,
            "time": "0.5h",
            "km": "20km",
            "safe": "持阿里证",
            "scenic": "【氧吧轮作休整】托林寺红墙古柏转经道缓步、象泉河岸观土林千峰在夕阳下化作赤金宫殿。",
            "food": "札达温室大棚新鲜青椒炒肉、热清汤面条、蒸南瓜软包。",
            "warn": "札达连宿第二晚！避开颠簸烂路霞义沟，保全全家精力与车胎，为明日翻越冈仁波齐蓄满能量。",
            "nav": "起点: 札达城堡酒店 ➔ 途经点1: 托林寺广场 ➔ 途经点2: 象泉河滨河湿地 ➔ 终点: 札达土林城堡酒店",
            "x": 65,
            "y": 310,
            "chartX": 568,
            "chartY": 55
      },
      {
            "day": 26,
            "tag": "D26",
            "stage": "神山圣湖",
            "route": "札达 ➔ 巴尔兵站 ➔ 冈仁波齐远眺 ➔ 玛旁雍错 ➔ 普兰",
            "alt": "3900m",
            "altNum": 3900,
            "time": "5.0h",
            "km": "260km",
            "safe": "持阿里证",
            "scenic": "神山之王冈仁波齐金字塔形标志性十字冰阶、圣湖玛旁雍错碧蓝如镜、鬼湖拉昂错玄石幽蓝，入住孔雀河谷。",
            "food": "普兰孔雀河谷温室新鲜时蔬大棚现摘炒菜、清炖高山小羊排（补充天然维生素C）。",
            "warn": "拉昂错湖边风大浪急，车辆停在平缓红礁石滩边开窗平视神山倒影，老人注意避风防着凉。",
            "nav": "起点: 札达城堡酒店 ➔ 途经点1: 巴尔兵站中石油 ➔ 途经点2: 冈仁波齐外围公路远眺台 ➔ 途经点3: 玛旁雍错环湖道 ➔ 终点: 普兰县三峡大酒店",
            "x": 105,
            "y": 370,
            "chartX": 590,
            "chartY": 45
      },
      {
            "day": 27,
            "tag": "D27",
            "stage": "普兰温谷",
            "route": "普兰 ➔ 孔雀河谷边贸田园 ➔ 纳木那尼峰日落 ➔ 普兰连宿",
            "alt": "3900m",
            "altNum": 3900,
            "time": "0.5h",
            "km": "20km",
            "safe": "持阿里证",
            "scenic": "普兰孔雀河谷田园农耕景观、纳木那尼雪峰庞大冰川群在晚霞中如粉金玉屏。",
            "food": "热玉米青稞浓汤、热馒头蘸蜂蜜、清炖藏羊骨汤。",
            "warn": "普兰连宿第二晚！在气候温润的河谷深度蓄力，迎接明日 G219 南线东出长坡。",
            "nav": "起点: 普兰三峡大酒店 ➔ 途经点1: 普兰国际边贸市场 ➔ 途经点2: 纳木那尼峰远眺天台 ➔ 终点: 普兰三峡大酒店",
            "x": 105,
            "y": 370,
            "chartX": 612,
            "chartY": 45
      },
      {
            "day": 28,
            "tag": "D28",
            "stage": "219东出",
            "route": "普兰 ➔ 公珠错 ➔ 帕羊草原 ➔ 避开仲巴 ➔ 萨嘎",
            "alt": "4500m",
            "altNum": 4500,
            "time": "6.5h",
            "km": "475km",
            "safe": "持日喀则证",
            "scenic": "伴行公珠错水天一色、马泉河源头湿地沙丘、帕羊高寒草原牧群，抵萨嘎县城。",
            "food": "萨嘎热清汤牦牛肉面、现蒸热素包、热白开水配西洋参片。",
            "warn": "【消灭仲巴恶劣住宿】仲巴(4570m)风沙极大住宿简陋，车队直接平稳开进萨嘎(4500m)供氧酒店。",
            "nav": "起点: 普兰三峡大酒店 ➔ 途经点1: 公珠错观景点 ➔ 途经点2: 帕羊镇加油站 ➔ 途经点3: 仲巴县外环 ➔ 终点: 萨嘎吉诺大酒店(供氧房)",
            "x": 180,
            "y": 380,
            "chartX": 634,
            "chartY": 20
      },
      {
            "day": 29,
            "tag": "D29",
            "stage": "珠峰期权",
            "route": "萨嘎 ➔ 桑桑草原 ➔ 拉孜 ➔ 定日白坝 (激活G3门)",
            "alt": "4330m",
            "altNum": 4330,
            "time": "6.0h",
            "km": "360km",
            "safe": "持日喀则证",
            "scenic": "桑桑高原湿地黑颈鹤、拉孜青稞之乡、抵达珠峰门户定日白坝镇，直面喜马拉雅主脊。",
            "food": "白坝热气腾腾土鸡汤锅、清炒高原白菜、热馒头，为明日登临加乌拉山储热储糖。",
            "warn": "【G3珠峰门激活】第29天全员适应资本极度雄厚；若晴率>60%明日启程看珠峰，若阴则改远眺。",
            "nav": "起点: 萨嘎吉诺大酒店 ➔ 途经点1: 桑桑草原观景台 ➔ 途经点2: 拉孜县城中石化 ➔ 终点: 定日白坝珠峰迎宾馆(供氧客房)",
            "x": 260,
            "y": 380,
            "chartX": 656,
            "chartY": 30
      },
      {
            "day": 30,
            "tag": "D30",
            "stage": "群峰朝圣",
            "route": "定日白坝 ➔ 加乌拉山口5210 ➔ 绒布寺珠峰近观 ➔ 日喀则",
            "alt": "3836m",
            "altNum": 3836,
            "time": "6.5h",
            "km": "320km",
            "safe": "持日喀则证",
            "scenic": "【人生高光视界】加乌拉山口五座8000m级雪峰一字排开同框盛景！绒布寺平视珠峰北壁雪瀑；下午直降日喀则。",
            "food": "日喀则藏家手工藏包子、清炖羊排汤、高山热甜茶。",
            "warn": "加乌拉山口风大低温，下车拍照严控15分钟内；绒布寺只乘环保车平视，下午降至日喀则3836m舒适安睡。",
            "nav": "起点: 定日白坝迎宾馆 ➔ 途经点1: 加乌拉山口观景台 ➔ 途经点2: 绒布寺停车场 ➔ 途经点3: 拉孜县 ➔ 终点: 日喀则希尔顿酒店",
            "x": 320,
            "y": 360,
            "chartX": 678,
            "chartY": 50
      },
      {
            "day": 31,
            "tag": "D31",
            "stage": "后藏扎寺",
            "route": "日喀则扎什伦布寺 ➔ 雅叶高速直达 ➔ 拉萨洲际",
            "alt": "3650m",
            "altNum": 3650,
            "time": "3.5h",
            "km": "270km",
            "safe": "市内自由",
            "scenic": "后藏格鲁圣地扎什伦布寺红墙慢步转经、展佛台俯瞰日喀则古城；走全新拉日高速顺雅江直达拉萨。",
            "food": "光明港琼甜茶馆清茶一壶、热藏饺配番茄汁、清淡藏式炖牛蹄筋。",
            "warn": "【消灭拉萨多余滞留】全程高等级高速顺畅无阻，车机直接导航至拉萨洲际地下车库。",
            "nav": "起点: 日喀则希尔顿 ➔ 途经点1: 扎什伦布寺南门 ➔ 途经点2: 仁布收费站(拉日高速) ➔ 终点: 拉萨圣地天堂洲际大饭店",
            "x": 370,
            "y": 340,
            "chartX": 700,
            "chartY": 55
      },
      {
            "day": 32,
            "tag": "D32",
            "stage": "拉萨大休耕",
            "route": "拉萨圣地天堂洲际大饭店 48h 远征大休整日",
            "alt": "3650m",
            "altNum": 3650,
            "time": "0.0h",
            "km": "0km",
            "safe": "市内自由",
            "scenic": "【农夫大休耕】罗布林卡古树林荫慢步、全车精细洗车与深度机修保养、全员体能生化指标复测。",
            "food": "拉萨天然素食养生菌汤锅、现蒸杂粮软糕、新鲜热苹果茶。",
            "warn": "全员零长途驾驶，行李彻底重整；明日正式向北踏上川藏北线 G317 史诗归途！",
            "nav": "起点: 洲际大饭店 ➔ 途经点1: 罗布林卡南门 ➔ 途经点2: 途虎养车拉萨工场店 ➔ 终点: 酒店地下车库",
            "x": 390,
            "y": 260,
            "chartX": 722,
            "chartY": 55
      },
      {
            "day": 33,
            "tag": "D33",
            "stage": "北线启程",
            "route": "拉萨 ➔ 京藏高速G6直飞 ➔ 当雄念青唐古拉 ➔ 那曲",
            "alt": "4500m",
            "altNum": 4500,
            "time": "4.0h",
            "km": "330km",
            "safe": "非边控区",
            "scenic": "【消灭当雄碎段】全程高速平稳直达藏北门户那曲市！车览念青唐古拉雪山群、孝登寺老街转经道。",
            "food": "那曲高寒原汁清炖小羊排汤（鲜美驱寒）、热酥油茶润肺。",
            "warn": "全平直高速长途，主驾严控100km/h内；那曲维也纳酒店中央供氧房，夜间持续开氧。",
            "nav": "起点: 洲际大饭店 ➔ 途经点1: 当雄收费站(G6) ➔ 途经点2: 念青唐古拉山观景台 ➔ 终点: 那曲维也纳国际酒店(弥散供氧客房)",
            "x": 380,
            "y": 190,
            "chartX": 744,
            "chartY": 20
      },
      {
            "day": 34,
            "tag": "D34",
            "stage": "藏北小布宫",
            "route": "那曲 ➔ G317 ➔ 索曲河湿地 ➔ 索县赞丹寺",
            "alt": "4000m",
            "altNum": 4000,
            "time": "4.0h",
            "km": "230km",
            "safe": "非边控区",
            "scenic": "沿G317向东，在索县远眺建在雅拉多晓山顶的“藏北小布达拉宫”赞丹寺（零商业免门票，气势磅礴）。",
            "food": "索县热气腾腾牦牛排炖高山土豆汤、清炒木耳高山包菜，暖意融融。",
            "warn": "海拔开始从4500m阶梯下降至4000m；赞丹寺在山下平地仰拍全景即可，长辈无需爬高陡台阶。",
            "nav": "起点: 那曲酒店 ➔ 途经点1: 索曲特大桥 ➔ 途经点2: 索县赞丹寺山脚广场 ➔ 终点: 索县赞丹大酒店(供氧房)",
            "x": 440,
            "y": 180,
            "chartX": 766,
            "chartY": 40
      },
      {
            "day": 35,
            "tag": "D35",
            "stage": "峡谷丹霞",
            "route": "索县 ➔ 巴青大草原 ➔ 斜拉山4900 ➔ 丁青县",
            "alt": "3870m",
            "altNum": 3870,
            "time": "5.0h",
            "km": "250km",
            "safe": "非边控区",
            "scenic": "藏东红层丹霞奇峰林立、斜拉山垭口车览不停留、丁青怒江峡谷雄奇地貌。",
            "food": "丁青手撕黄牛肉面、热甜茶配青稞饼，热腾腾暖胃。",
            "warn": "斜拉山垭口4900m为过境暴露点，不停留直接下坡；丁青县城海拔回落至3870m。",
            "nav": "起点: 索县大酒店 ➔ 途经点1: 巴青县城 ➔ 途经点2: 斜拉山垭口 ➔ 终点: 丁青雪域明珠大酒店(供氧房)",
            "x": 500,
            "y": 175,
            "chartX": 788,
            "chartY": 45
      },
      {
            "day": 36,
            "tag": "D36",
            "stage": "康巴小瑞士",
            "route": "丁青 ➔ 孜珠寺峡谷平视 ➔ 类乌齐查杰玛大殿 ➔ 昌都",
            "alt": "3240m",
            "altNum": 3240,
            "time": "5.5h",
            "km": "270km",
            "safe": "非边控区",
            "scenic": "【消灭类乌齐碎段】孜珠山天空之城峡谷平视、类乌齐国家森林公园高山针叶林、查杰玛大殿红白黑三色条纹，抵昌都。",
            "food": "昌都老城名小吃“加加面”（精炼骨汤爽口一口面，鲜美清淡不油腻）、酸奶饭。",
            "warn": "孜珠寺山顶土路陡峭严禁贸然冲顶，峡谷平视天空之城最壮阔；昌都海拔降至3240m，三甲医院近在咫尺。",
            "nav": "起点: 丁青酒店 ➔ 途经点1: 孜珠寺山脚峡谷观景台 ➔ 途经点2: 类乌齐查杰玛大殿 ➔ 途经点3: 昌都澜沧江特大桥 ➔ 终点: 昌都国际大酒店",
            "x": 560,
            "y": 170,
            "chartX": 810,
            "chartY": 80
      },
      {
            "day": 37,
            "tag": "D37",
            "stage": "茶马咽喉",
            "route": "昌都卡若区 ➔ 强巴林寺晨课 ➔ 澜沧江两江汇流漫步",
            "alt": "3240m",
            "altNum": 3240,
            "time": "0.5h",
            "km": "20km",
            "safe": "非边控区",
            "scenic": "【东归休耕日】强巴林寺外围古柏石林转经道缓步、昌都两江交汇茶马广场慢步，爱犬江畔漫步。",
            "food": "清汤牦牛肉煲、清炒高原娃娃菜、温热甜茶。",
            "warn": "昌都海拔仅3240m，湿润温暖，主驾全天充足睡眠，为明日翻越江达入川蓄满精力。",
            "nav": "起点: 昌都国际大酒店 ➔ 途经点1: 强巴林寺广场 ➔ 途经点2: 茶马广场步行街 ➔ 终点: 昌都国际大酒店",
            "x": 560,
            "y": 170,
            "chartX": 832,
            "chartY": 80
      },
      {
            "day": 38,
            "tag": "D38",
            "stage": "离藏入川",
            "route": "昌都 ➔ 妥坝草原 ➔ 江达同普 ➔ 岗妥大桥 ➔ 甘孜德格",
            "alt": "3240m",
            "altNum": 3240,
            "time": "5.5h",
            "km": "250km",
            "safe": "出藏入川",
            "scenic": "【消灭江达碎段】妥坝高山草甸、江达同普藏寨田园、跨金沙江岗妥大桥（“西藏”红字摩崖告别西藏），抵德格印经院。",
            "food": "德格纯手工藏包子（皮薄馅足多汁，清香不膻）、热酥油藏茶配青稞薄饼。",
            "warn": "江达出藏检查站减速慢行通过；德格印经院老门槛高，慢步搀扶老人。",
            "nav": "起点: 昌都酒店 ➔ 途经点1: 妥坝草甸观景点 ➔ 途经点2: 江达岗妥金沙江大桥 ➔ 终点: 德格印经院停车场",
            "x": 620,
            "y": 170,
            "chartX": 854,
            "chartY": 80
      },
      {
            "day": 39,
            "tag": "D39",
            "stage": "瑶池白塔",
            "route": "德格 ➔ 雀儿山特长隧道 ➔ 玉隆拉措车览 ➔ 甘孜县",
            "alt": "3390m",
            "altNum": 3390,
            "time": "3.5h",
            "km": "180km",
            "safe": "川西非控",
            "scenic": "穿雀儿山特长隧道避开往日风雪天险、玉隆拉措（新路海）冰川巨石玛尼堆、甘孜大白塔金色穹顶与雪山同框。",
            "food": "甘孜水淘糌粑、原汁清炖生康乡牦牛肉汤锅、高山热甜茶。",
            "warn": "玉隆拉措车览即可，湖边巨石较滑不建议老人徒步深入湖滩；甘孜县城地势平坦物价亲民。",
            "nav": "起点: 德格酒店 ➔ 途经点1: 雀儿山特长隧道德格端 ➔ 途经点2: 新路海大门外公路观景区 ➔ 终点: 甘孜县格萨尔王城大酒店",
            "x": 660,
            "y": 175,
            "chartX": 876,
            "chartY": 70
      },
      {
            "day": 40,
            "tag": "D40",
            "stage": "纯氧大换气",
            "route": "甘孜 ➔ 炉霍卡萨湖 ➔ 道孚崩科藏居 ➔ 丹巴中路藏寨",
            "alt": "1860m",
            "altNum": 1860,
            "time": "5.5h",
            "km": "260km",
            "safe": "嘉绒超富氧",
            "scenic": "【消灭道孚碎段】卡萨湖水鸟群倒映群山、道孚雕梁画栋棕白藏居、大金川峡谷千碉之国，直降丹巴中路藏寨（免票清幽古碉）。",
            "food": "嘉绒生态素席（高山鲜竹笋、有机南瓜、时蔬拌木耳）、香猪老腊肉薄片、温热自酿青稞果酒。",
            "warn": "【海拔断崖式暴跌至1860m！】全员彻底脱离高原缺氧负荷！晚间在丹巴藏家享受超强纯氧深度安睡，一扫旅途疲倦。",
            "nav": "起点: 甘孜酒店 ➔ 途经点1: 炉霍卡萨湖观景台 ➔ 途经点2: 道孚县城中心 ➔ 终点: 丹巴中路藏寨景区大门停车场",
            "x": 720,
            "y": 180,
            "chartX": 898,
            "chartY": 165
      },
      {
            "day": 41,
            "tag": "D41",
            "stage": "美人谷休耕",
            "route": "丹巴中路藏寨 48h 纯氧休耕日（古碉群与梨树林晨光）",
            "alt": "1860m",
            "altNum": 1860,
            "time": "0.5h",
            "km": "15km",
            "safe": "嘉绒超富氧",
            "scenic": "中路古碉群与梨树林晨曦光影、甲居藏寨外围全景台远眺、大金川峡谷微风，爱犬自由奔跑。",
            "food": "嘉绒农家现摘高山时蔬、现炒腊肉片、热玉米南瓜粥，温润清甜。",
            "warn": "全天平路慢行深呼吸，高负氧离子修复全员心肺红细胞，彻底洗脱高原旅途劳顿。",
            "nav": "起点: 丹巴中路民宿 ➔ 途经点1: 中路一号观景台 ➔ 途经点2: 甲居藏寨大门外全景台 ➔ 终点: 丹巴中路藏寨民宿",
            "x": 720,
            "y": 180,
            "chartX": 920,
            "chartY": 165
      },
      {
            "day": 42,
            "tag": "D42",
            "stage": "大渡河温泉",
            "route": "丹巴 ➔ S211大渡河沿江绝壁风情道 ➔ 泸定 ➔ 雅安石棉县",
            "alt": "850m",
            "altNum": 850,
            "time": "4.0h",
            "km": "190km",
            "safe": "零回头路",
            "scenic": "【不走回头路·走沿江绝壁风情道】全程贴着大渡河右岸S211顺流而下，车览泸定强渡纪念渡口，抵石棉天然温泉之乡。",
            "food": "石棉特色铁板清烤脆香鱼片、石棉贡椒拌土鸡、高山清甜黄果柑。",
            "warn": "S211大渡河沿岸平缓顺行，车速控制在40km/h；全家晚间泡草科地热温泉，彻底消除疲乏。",
            "nav": "起点: 丹巴中路藏寨 ➔ 途经点1: S211大渡河大桥 ➔ 途经点2: 泸定县滨江路 ➔ 终点: 石棉草科温泉假日酒店",
            "x": 810,
            "y": 220,
            "chartX": 942,
            "chartY": 210
      },
      {
            "day": 43,
            "tag": "D43",
            "stage": "千米绝壁",
            "route": "石棉 ➔ S66/G245 ➔ 乐山金口大峡谷 ➔ 乌斯河 ➔ 冕宁/西昌",
            "alt": "1500m",
            "altNum": 1500,
            "time": "4.5h",
            "km": "210km",
            "safe": "零回头路",
            "scenic": "【不走回头路·探秘旷世奇绝】穿行乐山金口大峡谷绝壁公路（中国唯一准驾进入的千米大绝壁）、铁道兵博物馆，抵西昌邛海。",
            "food": "金口河高山腊肉炖竹笋、大渡河高山豆花、西昌邛海清蒸南沼银鱼锅。",
            "warn": "绝壁公路视野开阔安全，慢速通行即可；避开去程的高速干线，换走山水秘境国道，体验感翻倍。",
            "nav": "起点: 石棉草科温泉酒店 ➔ 途经点1: 乐山金口大峡谷铁道兵博物馆 ➔ 途经点2: 乌斯河火车站旧址 ➔ 终点: 西昌邛海湾柏樾酒店",
            "x": 900,
            "y": 320,
            "chartX": 964,
            "chartY": 185
      },
      {
            "day": 44,
            "tag": "D44",
            "stage": "月城邛海",
            "route": "西昌邛海国家湿地公园慢步 ➔ 泸山林荫 ➔ 西昌连宿",
            "alt": "1500m",
            "altNum": 1500,
            "time": "1.0h",
            "km": "30km",
            "safe": "休闲养生",
            "scenic": "【邛海湖滨休整】西昌邛海国家湿地公园纯平无障碍湖滨绿道漫步、爱犬湖畔畅跑、清风拂柳白鹭戏水。",
            "food": "西昌鲜菌土鸡清汤锅、现蒸荞麦软糕、邛海银鱼滑蛋，清淡养胃。",
            "warn": "全天无长途驾驶，为全家提供从容的归程心理过渡，收拾全车行李物资。",
            "nav": "起点: 西昌邛海湾柏樾酒店 ➔ 途经点1: 邛海湿地三期梦里水乡 ➔ 途经点2: 泸山景区大门外广场 ➔ 终点: 西昌邛海湾柏樾酒店",
            "x": 950,
            "y": 380,
            "chartX": 980,
            "chartY": 185
      },
      {
            "day": 45,
            "tag": "D45",
            "stage": "风电长廊",
            "route": "西昌 ➔ 德昌安宁河风电长廊 ➔ 米易阳光绿道 ➔ 攀枝花市区",
            "alt": "1100m",
            "altNum": 1100,
            "time": "3.5h",
            "km": "220km",
            "safe": "荣耀凯旋",
            "scenic": "德昌白色巨型风力发电机群、米易热带水果长廊、安宁河谷阳光大道，午后荣耀返抵攀枝花家中！",
            "food": "米易阳光热带芒果沙拉、攀枝花正宗羊肉米线（鲜薄荷清香高汤，回味悠长）。",
            "warn": "【46天史诗自驾圆满凯旋！】7200公里横跨西藏全疆域，全员零高反、零事故、零违控，成就人生壮阔传奇！",
            "nav": "起点: 西昌邛海湾柏樾酒店 ➔ 途经点1: 德昌安宁河风电场 ➔ 途经点2: 米易阳光绿道观景台 ➔ 终点: 攀枝花市政府",
            "x": 980,
            "y": 440,
            "chartX": 996,
            "chartY": 200
      },
      {
            "day": 46,
            "tag": "D46",
            "stage": "凯旋复盘",
            "route": "攀枝花大本营（全车精洗复盘/全家体检/数据归档）",
            "alt": "1100m",
            "altNum": 1100,
            "time": "0.0h",
            "km": "0km",
            "safe": "平安收官",
            "scenic": "【大闭环圆满终章】全家生理指标全面体检复查、爱犬洗澡除菌、全车底盘悬挂清洗保养、摄影照片数据归档。",
            "food": "攀枝花家常滋补鸡汤、清炒时蔬、新鲜芒果拼盘。",
            "warn": "46天完美避开7月横断山脉暴雨汛期，零险阻凯旋收官！",
            "nav": "起点: 攀枝花市区 ➔ 途经点1: 攀枝花市中心医院健康管理中心 ➔ 途经点2: 汽车美容工场 ➔ 终点: 攀枝花温馨家中",
            "x": 980,
            "y": 440,
            "chartX": 1005,
            "chartY": 200
      }
];
    let currentDayIdx = 0;
    let isPlaying = false;
    let playTimer = null;
    let playSpeed = 1;
    let currentCategory = "ALL";

    // Tab Switching
    function switchTab(tabId, btn) {
      document.querySelectorAll(".tab-btn").forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      document.querySelectorAll(".tab-pane").forEach(p => p.classList.remove("active"));
      document.getElementById(`pane-${tabId}`).classList.add("active");
    }

    // Render Scroller
    function renderScroller() {
      const container = document.getElementById("days-scroller");
      container.innerHTML = "";
      itinerary.forEach((item, idx) => {
        const card = document.createElement("div");
        card.className = `tray-card ${idx === currentDayIdx ? 'active' : ''}`;
        card.id = `mini-card-${idx}`;
        card.onclick = () => jumpToDay(idx);
        card.innerHTML = `
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <span class="tray-day-tag">${item.tag}</span>
            <span class="tray-alt">${item.alt}</span>
          </div>
          <div class="tray-route">${item.route}</div>
        `;
        container.appendChild(card);
      });
    }

    // Render Waypoints on SVG Map
    function renderSvgNodes() {
      const group = document.getElementById("svg-nodes-group");
      group.innerHTML = "";
      itinerary.forEach((item, idx) => {
        const g = document.createElementNS("http://www.w3.org/2000/svg", "g");
        g.setAttribute("transform", `translate(${item.x}, ${item.y})`);
        g.style.cursor = "pointer";
        g.onclick = () => jumpToDay(idx);

        const circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
        circle.setAttribute("cx", "0");
        circle.setAttribute("cy", "0");
        circle.setAttribute("r", "4");
        circle.setAttribute("fill", "#38bdf8");
        circle.setAttribute("stroke", "#ffffff");
        circle.setAttribute("stroke-width", "1");

        const text = document.createElementNS("http://www.w3.org/2000/svg", "text");
        text.setAttribute("x", "6");
        text.setAttribute("y", "3");
        text.setAttribute("fill", "rgba(255,255,255,0.7)");
        text.setAttribute("font-size", "9");
        text.textContent = item.tag;

        g.appendChild(circle);
        g.appendChild(text);
        group.appendChild(g);
      });
    }

    // Update Live State
    function updateState(idx) {
      currentDayIdx = idx;
      const data = itinerary[idx];

      // HUD
      document.getElementById("hud-day").innerText = `${data.tag} / 28`;
      const hudAlt = document.getElementById("hud-alt");
      hudAlt.innerText = data.alt;
      if (data.altNum > 4200) hudAlt.style.color = "var(--rose-glow)";
      else if (data.altNum > 3000) hudAlt.style.color = "var(--amber-glow)";
      else hudAlt.style.color = "var(--emerald-glow)";
      document.getElementById("hud-km").innerText = data.km;

      // Range Slider
      document.getElementById("timeline-slider").value = idx + 1;

      // Map Vehicle
      const beacon = document.getElementById("vehicle-beacon");
      beacon.setAttribute("transform", `translate(${data.x}, ${data.y})`);
      document.getElementById("vehicle-tag").textContent = `🚙 ${data.tag} ${data.stage}`;

      // Altitude Tracker
      const tracker = document.getElementById("alt-tracker");
      tracker.setAttribute("transform", `translate(${data.chartX}, 0)`);
      const dot = document.getElementById("alt-tracker-dot");
      dot.setAttribute("cy", data.chartY);

      // Spotlight Card
      document.getElementById("spot-day").innerText = `DAY ${data.day < 10 ? '0'+data.day : data.day}`;
      document.getElementById("spot-stage").innerText = data.stage;
      
      const altBadge = document.getElementById("spot-alt");
      altBadge.className = "spot-alt-chip";
      if (data.altNum > 4200) altBadge.classList.add("alt-high");
      else if (data.altNum > 3000) altBadge.classList.add("alt-warn");
      altBadge.innerText = `🌙 宿: ${data.alt}`;

      document.getElementById("spot-route").innerText = data.route;
      document.getElementById("spot-time").innerText = `⏱️ 纯驾 ${data.time}`;
      document.getElementById("spot-km").innerText = `🛣️ ${data.km}`;
      document.getElementById("spot-safe").innerText = `🛡️ ${data.safe}`;
      document.getElementById("spot-scenic").innerText = data.scenic;
      document.getElementById("spot-food").innerText = data.food;
      document.getElementById("spot-warn").innerText = data.warn;
      document.getElementById("spot-nav").innerText = data.nav;

      // Scroller sync
      document.querySelectorAll(".tray-card").forEach((c, i) => {
        if (i === idx) c.classList.add("active");
        else c.classList.remove("active");
      });
      const activeMini = document.getElementById(`mini-card-${idx}`);
      if (activeMini) {
        activeMini.scrollIntoView({ behavior: 'smooth', inline: 'center', block: 'nearest' });
      }
    }

    // Playback Engine
    function togglePlay() {
      isPlaying = !isPlaying;
      const btn = document.getElementById("btn-play");
      const icon = document.getElementById("play-icon");
      const text = document.getElementById("play-text");

      if (isPlaying) {
        icon.innerText = "❚❚";
        text.innerText = "暂停巡航";
        btn.style.background = "var(--rose-glow)";
        btn.style.color = "#fff";
        startLoop();
      } else {
        icon.innerText = "▶";
        text.innerText = "启动巡航动效";
        btn.style.background = "";
        btn.style.color = "";
        stopLoop();
      }
    }

    function startLoop() {
      stopLoop();
      const interval = 2200 / playSpeed;
      playTimer = setInterval(() => {
        if (currentDayIdx >= itinerary.length - 1) {
          currentDayIdx = 0;
        } else {
          currentDayIdx++;
        }
        updateState(currentDayIdx);
      }, interval);
    }

    function stopLoop() {
      if (playTimer) clearInterval(playTimer);
    }

    function setSpeed(sp, el) {
      playSpeed = sp;
      document.querySelectorAll(".speed-chip").forEach(o => o.classList.remove("active"));
      el.classList.add("active");
      if (isPlaying) startLoop();
    }

    function stepDay(delta) {
      stopLoop();
      isPlaying = false;
      document.getElementById("play-icon").innerText = "▶";
      document.getElementById("play-text").innerText = "启动巡航动效";
      document.getElementById("btn-play").style.background = "";

      let next = currentDayIdx + delta;
      if (next < 0) next = 0;
      if (next > itinerary.length - 1) next = itinerary.length - 1;
      updateState(next);
    }

    function jumpToDay(idx) {
      stopLoop();
      isPlaying = false;
      document.getElementById("play-icon").innerText = "▶";
      document.getElementById("play-text").innerText = "启动巡航动效";
      document.getElementById("btn-play").style.background = "";
      updateState(idx);
    }

    function onSliderMove(val) {
      jumpToDay(parseInt(val) - 1);
    }

    function copyActiveNav() {
      const text = itinerary[currentDayIdx].nav;
      navigator.clipboard.writeText(text).then(() => {
        const toast = document.getElementById("toast");
        toast.style.display = "block";
        setTimeout(() => { toast.style.display = "none"; }, 2500);
      });
    }

    // 49 Regions Rendering and Filtering
    function renderRegions(list) {
      const grid = document.getElementById("regions-grid");
      grid.innerHTML = "";
      document.getElementById("match-counter").innerText = `显示 ${list.length} / 49 地区`;

      list.forEach(r => {
        const card = document.createElement("div");
        card.className = "region-card";
        card.innerHTML = `
          <div class="region-card-top">
            <div>
              <div class="reg-pref">${r.pref}</div>
              <div class="reg-name">${r.cty}</div>
            </div>
            <div style="display:flex; flex-direction:column; align-items:flex-end; gap:0.3rem;">
              <span class="reg-id-badge">#${r.id < 10 ? '0'+r.id : r.id}</span>
              <span class="reg-stage-pill">${r.stage}</span>
            </div>
          </div>

          <div class="reg-item-box">
            <div class="reg-item-label lbl-spots">📸 纯玩打卡景点 (免票/原生态推荐)</div>
            <div class="reg-item-val">${r.spots}</div>
          </div>

          <div class="reg-item-box">
            <div class="reg-item-label lbl-food">🍲 农夫适老养生美食</div>
            <div class="reg-item-val">${r.food}</div>
          </div>

          <div class="reg-item-box">
            <div class="reg-item-label lbl-hotel">🏨 极境舒适住宿推荐</div>
            <div class="reg-item-val">${r.hotel}</div>
          </div>

          <div style="display:grid; grid-template-columns: 1fr 1fr; gap:0.6rem;">
            <div class="reg-item-box">
              <div class="reg-item-label lbl-weather">⛅ 气候与温差</div>
              <div class="reg-item-val" style="font-size:0.78rem;">${r.weather}</div>
            </div>
            <div class="reg-item-box">
              <div class="reg-item-label lbl-pet">🐕 宠物友好度</div>
              <div class="reg-item-val" style="font-size:0.78rem;">${r.pet}</div>
            </div>
          </div>
        `;
        grid.appendChild(card);
      });
    }

    function selectCategory(cat, el) {
      currentCategory = cat;
      document.querySelectorAll(".cat-chip").forEach(c => c.classList.remove("active"));
      el.classList.add("active");
      filterRegions();
    }

    function filterRegions() {
      const q = document.getElementById("region-search").value.trim().toLowerCase();
      const filtered = rawRegions.filter(r => {
        const matchesCat = (currentCategory === "ALL" || r.stage === currentCategory);
        const text = `${r.pref} ${r.cty} ${r.stage} ${r.spots} ${r.food} ${r.hotel} ${r.weather} ${r.pet}`.toLowerCase();
        const matchesQuery = !q || text.includes(q);
        return matchesCat && matchesQuery;
      });
      renderRegions(filtered);
    }

    // Init
    document.addEventListener("DOMContentLoaded", () => {
      renderScroller();
      renderSvgNodes();
      updateState(0);
      renderRegions(rawRegions);
    });
  </script>
</body>
</html>
'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

print("Successfully generated ultra-premium index.html with all 3 tabs and 49 regions!")
