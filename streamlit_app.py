import streamlit as st

st.set_page_config(
    page_title="이주훈 | 수학을 더 가깝게",
    page_icon="📐",
    layout="wide",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Gowun+Dodum&family=Space+Grotesk:wght@400;500;600;700&display=swap');

    :root {
        --ink: #172326;
        --paper: #f3f5ef;
        --blue: #3158ed;
        --lime: #d7f45b;
        --coral: #ff755d;
        --muted: #627073;
    }

    html { scroll-behavior: smooth; }
    [data-testid="stAppViewContainer"] {
        background:
            linear-gradient(rgba(23, 35, 38, .035) 1px, transparent 1px),
            linear-gradient(90deg, rgba(23, 35, 38, .035) 1px, transparent 1px),
            var(--paper);
        background-size: 32px 32px;
        color: var(--ink);
    }
    [data-testid="stHeader"], [data-testid="stToolbar"], footer { visibility: hidden; }
    .block-container { max-width: 1160px; padding: 1.4rem 2rem 5rem; }
    .site-nav {
        display: flex; justify-content: space-between; align-items: center;
        padding: 8px 0 22px; border-bottom: 1px solid rgba(23,35,38,.22);
        font-family: 'DM Mono', monospace; font-size: 12px; letter-spacing: .04em;
    }
    .nav-mark { font-weight: 500; }
    .nav-links { display: flex; gap: 28px; }
    .nav-links a { color: var(--ink); text-decoration: none; }
    .hero {
        min-height: 490px; display: grid; grid-template-columns: 1.15fr .85fr;
        gap: 42px; align-items: center; padding: 56px 0 58px;
    }
    .eyebrow, .section-kicker {
        font-family: 'DM Mono', monospace; font-size: 12px; letter-spacing: .08em;
        text-transform: uppercase;
    }
    .eyebrow { color: var(--blue); margin-bottom: 22px; }
    h1, h2, p { margin-top: 0; }
    .hero h1 {
        margin: 0; font-family: 'Space Grotesk', 'Gowun Dodum', sans-serif;
        font-size: 82px; line-height: .98; letter-spacing: 0; font-weight: 700;
    }
    .hero h1 span { color: var(--blue); }
    .hero-copy {
        max-width: 460px; margin: 24px 0 0; color: #435154;
        font-family: 'Gowun Dodum', sans-serif; font-size: 18px; line-height: 1.8;
    }
    .hero-art {
        min-height: 350px; position: relative; overflow: hidden;
        background: var(--blue); color: white; padding: 28px;
        display: flex; flex-direction: column; justify-content: space-between;
    }
    .art-label { font: 12px 'DM Mono', monospace; opacity: .8; }
    .equation {
        position: relative; z-index: 1; align-self: center; margin: 0;
        font: 500 42px 'DM Mono', monospace; letter-spacing: 0;
    }
    .orbit {
        position: absolute; width: 230px; height: 230px; border-radius: 50%;
        border: 1px solid rgba(255,255,255,.55); top: 72px; left: 50%;
        transform: translateX(-50%);
    }
    .orbit::before, .orbit::after {
        content: ''; position: absolute; border: 1px solid rgba(255,255,255,.34);
        border-radius: 50%; inset: 25px;
    }
    .orbit::after { inset: 55px; }
    .art-dot {
        position: absolute; width: 18px; height: 18px; border-radius: 50%;
        background: var(--lime); top: 99px; right: 17%;
    }
    .art-index { align-self: flex-end; color: var(--lime); font: 12px 'DM Mono', monospace; }
    .intro-band {
        display: grid; grid-template-columns: 1fr 2fr; gap: 40px;
        padding: 28px 0 34px; border-top: 1px solid rgba(23,35,38,.22);
        border-bottom: 1px solid rgba(23,35,38,.22);
    }
    .section-kicker { color: var(--blue); padding-top: 5px; }
    .intro-band h2 {
        margin-bottom: 12px; font: 600 30px 'Gowun Dodum', sans-serif; letter-spacing: 0;
    }
    .intro-band p {
        margin: 0; max-width: 680px; color: #435154;
        font: 16px/1.85 'Gowun Dodum', sans-serif;
    }
    .details {
        display: grid; grid-template-columns: 1fr 1fr; gap: 0 48px;
        padding: 54px 0 44px;
    }
    .detail {
        display: grid; grid-template-columns: 110px 1fr; gap: 18px;
        padding: 20px 0; border-bottom: 1px solid rgba(23,35,38,.22);
    }
    .detail-label { color: var(--muted); font: 12px 'DM Mono', monospace; padding-top: 5px; }
    .detail-value { font: 17px 'Gowun Dodum', sans-serif; line-height: 1.6; }
    .dream {
        position: relative; display: grid; grid-template-columns: 1fr auto; gap: 24px;
        align-items: end; padding: 32px; background: var(--lime); margin: 8px 0 56px;
    }
    .dream .section-kicker { color: #405000; }
    .dream h2 {
        max-width: 720px; margin: 18px 0 0; font: 600 30px/1.45 'Gowun Dodum', sans-serif;
    }
    .dream-symbol { color: var(--blue); font: 68px 'DM Mono', monospace; line-height: .9; }
    .footer {
        display: flex; justify-content: space-between; gap: 18px;
        padding-top: 18px; border-top: 1px solid rgba(23,35,38,.22);
        color: var(--muted); font: 11px 'DM Mono', monospace;
    }
    @media (max-width: 720px) {
        .block-container { padding: 1rem 1.15rem 3rem; }
        .nav-links { gap: 14px; }
        .hero { grid-template-columns: 1fr; gap: 30px; padding: 48px 0; }
        .hero h1 { font-size: 58px; }
        .hero-art { min-height: 290px; }
        .intro-band { grid-template-columns: 1fr; gap: 14px; }
        .details { grid-template-columns: 1fr; padding: 32px 0; }
        .dream { grid-template-columns: 1fr; padding: 24px; }
        .dream h2 { font-size: 24px; }
        .dream-symbol { position: absolute; right: 20px; bottom: 20px; opacity: .22; }
        .footer { flex-direction: column; }
    }
    </style>

    <div class="site-nav">
      <div class="nav-mark">JH / MATH EDUCATION</div>
      <div class="nav-links">
        <a href="#about">ABOUT</a>
        <a href="#dream">DREAM</a>
      </div>
    </div>

    <main>
      <section class="hero">
        <div>
          <div class="eyebrow">A future mathematics educator · 2026</div>
          <h1>안녕하세요,<br><span>이주훈</span>입니다.</h1>
          <p class="hero-copy">수학의 즐거움을 발견하고, 그 즐거움을 더 많은 사람과 나누는 선생님을 꿈꿉니다.</p>
        </div>
        <div class="hero-art" aria-label="수학 기호로 꾸민 그래픽">
          <div class="art-label">A LITTLE MATH, A BIG IDEA</div>
          <div class="orbit"></div>
          <div class="art-dot"></div>
          <div class="equation">x² + y²</div>
          <div class="art-index">01 — KEEP ASKING</div>
        </div>
      </section>

      <section class="intro-band" id="about">
        <div class="section-kicker">01 / ABOUT ME</div>
        <div>
          <h2>배우고, 질문하고, 함께 나눕니다.</h2>
          <p>청주교육대학교 수학교육과에서 수학을 배우고 있습니다. 답을 찾는 과정의 재미와 개념을 이해하는 순간의 기쁨을 학생들과 나누는 교사가 되고 싶습니다.</p>
        </div>
      </section>

      <section class="details" aria-label="소개 정보">
        <div class="detail"><div class="detail-label">NAME</div><div class="detail-value">이주훈</div></div>
        <div class="detail"><div class="detail-label">ROLE</div><div class="detail-value">예비 초등 교사</div></div>
        <div class="detail"><div class="detail-label">AFFILIATION</div><div class="detail-value">청주교육대학교</div></div>
        <div class="detail"><div class="detail-label">MAJOR</div><div class="detail-value">수학교육과</div></div>
      </section>

      <section class="dream" id="dream">
        <div>
          <div class="section-kicker">02 / MY DREAM</div>
          <h2>수학이 어렵기만 한 과목이 아니라,<br>“아하!” 하고 웃게 되는 경험이 되도록.</h2>
        </div>
        <div class="dream-symbol">∑</div>
      </section>
    </main>

    <div class="footer">
      <span>이주훈 · 청주교육대학교 수학교육과</span>
      <span>MADE WITH CURIOSITY / 2026</span>
    </div>
    """,
    unsafe_allow_html=True,
)