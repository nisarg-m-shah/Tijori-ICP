import streamlit as st

st.set_page_config(
    page_title="Tijori.ai — ICP Cards",
    page_icon="🃏",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ── Global CSS ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:wght@300;400;500;600&family=Space+Mono:wght@400;700&display=swap');

/* Reset & base */
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: #0a0a0f;
    color: #e8e4d9;
}
.stApp { background: #0a0a0f; }
.block-container { max-width: 720px; padding: 1.5rem 1.5rem 4rem; }

/* Hide Streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
.stDeployButton { display: none; }

/* Navigation bar */
.nav-bar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0.6rem 0 1.2rem;
    border-bottom: 1px solid #2a2a3a;
    margin-bottom: 1.8rem;
}
.nav-logo {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 1.5rem;
    letter-spacing: .12em;
    color: #e8e4d9;
}
.nav-count {
    font-family: 'Space Mono', monospace;
    font-size: 0.7rem;
    color: #666;
    letter-spacing: .08em;
}

/* Page indicator dots */
.page-dots {
    display: flex;
    gap: 5px;
    justify-content: center;
    margin-bottom: 1.6rem;
    flex-wrap: wrap;
}
.dot {
    width: 7px; height: 7px;
    border-radius: 50%;
    background: #2a2a3a;
    transition: background 0.2s;
}
.dot.active { background: #e8e4d9; }
.dot.b2b { background: #2a3a4a; }
.dot.b2b.active { background: #4ab8d4; }

/* ── CARD SHELL ─────────────────────────────────────────────── */
.card-shell {
    border-radius: 18px;
    overflow: hidden;
    position: relative;
    box-shadow: 0 24px 60px rgba(0,0,0,0.6);
    border: 1px solid rgba(255,255,255,0.06);
}

/* Card header band */
.card-header {
    padding: 1.4rem 1.6rem 1.1rem;
    position: relative;
    overflow: hidden;
}
.card-header::before {
    content: '';
    position: absolute;
    inset: 0;
    opacity: 0.12;
    background-image: repeating-linear-gradient(
        45deg,
        transparent,
        transparent 6px,
        rgba(255,255,255,0.15) 6px,
        rgba(255,255,255,0.15) 7px
    );
}
.card-meta {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 0.7rem;
    position: relative;
    z-index: 1;
}
.card-type-badge {
    font-family: 'Space Mono', monospace;
    font-size: 0.6rem;
    letter-spacing: .14em;
    padding: 3px 8px;
    border-radius: 3px;
    font-weight: 700;
    text-transform: uppercase;
}
.card-rank {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 1.1rem;
    letter-spacing: .08em;
    opacity: 0.85;
}
.card-name {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 2.3rem;
    letter-spacing: .06em;
    line-height: 1.0;
    margin-bottom: 0.35rem;
    position: relative;
    z-index: 1;
}
.card-tagline {
    font-size: 0.78rem;
    line-height: 1.5;
    opacity: 0.75;
    position: relative;
    z-index: 1;
    font-weight: 300;
    max-width: 90%;
}

/* Card body */
.card-body {
    padding: 1.3rem 1.6rem 1.5rem;
    background: #111118;
}

/* Stat row */
.stat-row {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr;
    gap: 8px;
    margin-bottom: 1.2rem;
}
.stat-box {
    background: #1a1a25;
    border-radius: 8px;
    padding: 8px 10px;
    text-align: center;
    border: 1px solid #2a2a3a;
}
.stat-label {
    font-family: 'Space Mono', monospace;
    font-size: 0.52rem;
    letter-spacing: .1em;
    text-transform: uppercase;
    color: #666;
    margin-bottom: 4px;
}
.stat-value {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 1.15rem;
    letter-spacing: .04em;
    line-height: 1;
}
.sv-hi { color: #4cd990; }
.sv-mid { color: #f0b429; }
.sv-lo { color: #e05a4e; }

/* Section label */
.sec-label {
    font-family: 'Space Mono', monospace;
    font-size: 0.58rem;
    letter-spacing: .14em;
    text-transform: uppercase;
    color: #555;
    margin-bottom: 6px;
    margin-top: 14px;
}
.sec-label:first-of-type { margin-top: 0; }

/* Definition text */
.def-text {
    font-size: 0.8rem;
    line-height: 1.62;
    color: #b0aaaa;
    margin-bottom: 0;
}

/* Merged cards tags */
.tag-row { display: flex; flex-wrap: wrap; gap: 5px; margin-bottom: 0; }
.tag {
    font-size: 0.65rem;
    padding: 3px 7px;
    border-radius: 4px;
    border: 1px solid #2a2a3a;
    color: #888;
    font-family: 'DM Sans', sans-serif;
    line-height: 1.4;
}

/* Jobs grid */
.jobs-grid { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 8px; }
.job-box {
    background: #1a1a25;
    border-radius: 8px;
    padding: 9px 10px;
    border: 1px solid #2a2a3a;
}
.job-type {
    font-family: 'Space Mono', monospace;
    font-size: 0.52rem;
    letter-spacing: .1em;
    text-transform: uppercase;
    margin-bottom: 4px;
}
.jt-fn { color: #4cd990; }
.jt-so { color: #4ab8d4; }
.jt-em { color: #d97bca; }
.job-text { font-size: 0.7rem; color: #999; line-height: 1.5; }

/* Trigger pills */
.trigger-row { display: flex; flex-wrap: wrap; gap: 6px; }
.trigger-pill {
    font-size: 0.68rem;
    padding: 4px 9px;
    border-radius: 20px;
    background: #1e1e2e;
    border: 1px solid #333350;
    color: #aaa;
}

/* Struggle grid */
.struggle-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }
.struggle-box {
    background: #1a1a25;
    border-radius: 8px;
    padding: 9px 10px;
    border: 1px solid #2a2a3a;
}
.struggle-label {
    font-family: 'Space Mono', monospace;
    font-size: 0.52rem;
    letter-spacing: .1em;
    text-transform: uppercase;
    margin-bottom: 4px;
}
.sl-push { color: #7b6cf0; }
.sl-pull { color: #4cd990; }
.sl-ax   { color: #e05a4e; }
.sl-in   { color: #888; }
.struggle-text { font-size: 0.7rem; color: #999; line-height: 1.5; }

/* Value grid */
.value-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }
.value-box {
    background: #1a1a25;
    border-radius: 8px;
    padding: 9px 10px;
    border: 1px solid #2a2a3a;
}
.value-label {
    font-family: 'Space Mono', monospace;
    font-size: 0.52rem;
    letter-spacing: .1em;
    color: #7b6cf0;
    text-transform: uppercase;
    margin-bottom: 4px;
}
.value-text { font-size: 0.7rem; color: #999; line-height: 1.5; }

/* Card footer strip */
.card-footer {
    padding: 0.7rem 1.6rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-top: 1px solid #2a2a3a;
}
.footer-type {
    font-family: 'Space Mono', monospace;
    font-size: 0.6rem;
    letter-spacing: .1em;
    text-transform: uppercase;
    color: #555;
}
.footer-id {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 1rem;
    letter-spacing: .1em;
    color: #333;
}

/* ── Rankings table ─────────────────────────────────────────── */
.rank-card {
    background: #111118;
    border-radius: 18px;
    overflow: hidden;
    border: 1px solid rgba(255,255,255,0.06);
    box-shadow: 0 24px 60px rgba(0,0,0,0.6);
}
.rank-header {
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
    padding: 1.4rem 1.6rem 1.1rem;
    border-bottom: 1px solid #2a2a3a;
}
.rank-title {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 2rem;
    letter-spacing: .08em;
    margin-bottom: 0.2rem;
}
.rank-sub {
    font-size: 0.75rem;
    color: #888;
    font-weight: 300;
}
.rank-table { width: 100%; border-collapse: collapse; }
.rank-table th {
    font-family: 'Space Mono', monospace;
    font-size: 0.55rem;
    letter-spacing: .12em;
    text-transform: uppercase;
    color: #555;
    padding: 10px 14px;
    border-bottom: 1px solid #2a2a3a;
    text-align: left;
}
.rank-table td {
    padding: 10px 14px;
    border-bottom: 1px solid #1e1e28;
    vertical-align: top;
    font-size: 0.75rem;
    color: #aaa;
    line-height: 1.5;
}
.rank-table tr:last-child td { border-bottom: none; }
.rank-table tr:hover td { background: rgba(255,255,255,0.02); }
.rank-num {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 1.4rem;
    line-height: 1;
}
.icp-name-cell { color: #e8e4d9; font-weight: 500; }
.type-b2b { color: #4ab8d4; }
.type-b2c { color: #d97bca; }
.dot-hi-s  { color: #4cd990; font-size: 0.65rem; }
.dot-mid-s { color: #f0b429; font-size: 0.65rem; }
.dot-lo-s  { color: #e05a4e; font-size: 0.65rem; }
.why-text { font-size: 0.7rem; color: #777; }

/* Notes page */
.notes-card {
    background: #111118;
    border-radius: 18px;
    overflow: hidden;
    border: 1px solid rgba(255,255,255,0.06);
    box-shadow: 0 24px 60px rgba(0,0,0,0.6);
    padding: 1.6rem;
}
.notes-title {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 2rem;
    letter-spacing: .08em;
    margin-bottom: 0.3rem;
}
.notes-sub { font-size: 0.75rem; color: #666; margin-bottom: 1.6rem; }
.note-block {
    background: #1a1a25;
    border-radius: 10px;
    padding: 14px 16px;
    margin-bottom: 12px;
    border-left: 3px solid;
}
.note-block.nb-start  { border-color: #7b6cf0; }
.note-block.nb-entry  { border-color: #4cd990; }
.note-block.nb-expand { border-color: #4ab8d4; }
.note-block.nb-avoid  { border-color: #e05a4e; }
.note-block.nb-long   { border-color: #f0b429; }
.note-heading {
    font-family: 'Space Mono', monospace;
    font-size: 0.62rem;
    letter-spacing: .12em;
    text-transform: uppercase;
    margin-bottom: 6px;
}
.nh-start  { color: #7b6cf0; }
.nh-entry  { color: #4cd990; }
.nh-expand { color: #4ab8d4; }
.nh-avoid  { color: #e05a4e; }
.nh-long   { color: #f0b429; }
.note-text { font-size: 0.78rem; color: #aaa; line-height: 1.65; }

/* Nav buttons */
div[data-testid="column"] .stButton button {
    width: 100%;
    background: #1a1a25;
    color: #e8e4d9;
    border: 1px solid #2a2a3a;
    border-radius: 8px;
    font-family: 'Space Mono', monospace;
    font-size: 0.7rem;
    letter-spacing: .08em;
    padding: 0.5rem;
    transition: all 0.15s;
}
div[data-testid="column"] .stButton button:hover {
    background: #2a2a3a;
    border-color: #4a4a6a;
}
</style>
""", unsafe_allow_html=True)

# ── Data ────────────────────────────────────────────────────────────────────

ICPS = [
    {
        "id": "B1",
        "rank": 1,
        "type": "B2B",
        "name": "Client-Risk Advisor",
        "tagline": "Professional whose practice is damaged — and whose revenue is capped — by client disorganization",
        "color_bg": "#0d1b2a",
        "color_accent": "#4ab8d4",
        "color_badge_bg": "#0a2a3a",
        "color_badge_text": "#4ab8d4",
        "definition": "A financial or legal professional — CA, wealth planner, insurance advisor, estate lawyer, property lawyer, or company secretary — whose practice quality, client retention, and liability exposure are directly shaped by how organized their clients' financial and legal lives are. Every disorganized client is a latent liability. Every crisis call is avoidable revenue loss. Tijori converts client disorganization from their problem into their product.",
        "merged": ["CA — crisis coordinator for disorganized client estates", "CA — retiring with untransferable client knowledge", "Estate lawyer — reconstruction before advice", "Property lawyer — transaction stalls", "Company secretary — founder continuity failure", "Insurance advisor — claim disputes and renewal losses", "Fee-only planner — incomplete client data"],
        "struggle": {
            "push": "Client disorganization wastes engagement time, caps advice quality, and creates liability exposure. Crisis calls arrive for situations the professional had no system to prevent.",
            "pull": "A system that makes client organization a productized, billable service — so every client arrives prepared and the professional is embedded in the client's life record.",
            "anxiety": "A client crisis, deal failure, or liability event that organized records would have prevented — landing on the professional's reputation and revenue.",
            "inertia": "Client disorganization is treated as the client's problem. The professional hasn't framed a solution as a billable service with measurable retention upside."
        },
        "jobs": {
            "fn": "Offer Tijori as a client onboarding service — organized records that make every engagement more efficient, reduce liability, and generate a recurring revenue stream from annual review.",
            "so": "Be known as the advisor who proactively organizes clients' lives — not just the one who shows up after the crisis. Differentiate through care, not just expertise.",
            "em": "Stop absorbing the cost of client disorganization — feel that the practice is protected by a system rather than exposed by the absence of one."
        },
        "triggers": ["Client death or estate chaos", "Claim dispute involving their name", "CA or CS retirement forcing knowledge transfer", "Competitor wins a client by offering more"],
        "value": {"Productized service": "A 'life organization audit' as a billable onboarding engagement.", "Recurring revenue": "Annual review subscription on top of core fees.", "Client retention": "Clients embedded in the system are far less likely to switch.", "Reduced liability": "Documented records protect from blame when complications arise."},
        "filters": {"Pain": ("Very high", "hi"), "Activity": ("Post-crisis", "mid"), "Belief": ("Moderate", "mid"), "Pay": ("High", "hi")},
    },
    {
        "id": "B4",
        "rank": 2,
        "type": "B2B",
        "name": "Corporate Welfare Champion",
        "tagline": "HR leader seeking a differentiated benefit that solves a real employee problem at institutional scale",
        "color_bg": "#1a1a0d",
        "color_accent": "#c8d94a",
        "color_badge_bg": "#2a2a0a",
        "color_badge_text": "#c8d94a",
        "definition": "An HR leader or employee benefits manager at a mid-to-large employer who is actively looking for differentiated, genuinely useful benefits that improve employee financial wellbeing, reduce HR support burden, and signal organizational care beyond working hours. Tijori as an employee benefit is the only offering that solves a real, recurring employee problem while also reducing HR's operational cost.",
        "merged": ["HR / employee benefits — statutory dues unclaimed, disorganization creates HR burden and liability"],
        "struggle": {
            "push": "Employees across career stages are financially disorganized — old PF accounts, unclaimed gratuity, group insurance confusion. HR spends significant time helping individuals reconstruct records that should have been maintained throughout their career.",
            "pull": "A genuine financial life organization benefit offered to every employee — reducing HR burden, ensuring entitlements are claimed cleanly, and creating a visible, differentiated welfare signal.",
            "anxiety": "An employee dies and HR cannot guide the family through claims. Unclaimed PF creates regulatory scrutiny. Gratuity disputes at exit generate legal and reputational risk.",
            "inertia": "Employee personal financial organization is treated as a personal responsibility. The cost is absorbed as overhead rather than solved systematically."
        },
        "jobs": {
            "fn": "Offer Tijori as a standard employee benefit — reducing HR support burden, ensuring statutory entitlements are claimed, creating an organized financial life record that extends into every employee's household.",
            "so": "Be the employer genuinely known for caring about employee financial wellbeing — not just salary and perks, but the organized life that enables an employee to be fully present.",
            "em": "Feel that the organization's care for its people extends into their lives — not just their working hours."
        },
        "triggers": ["Employee death with no claim documentation", "PF dispute at exit", "Benefits benchmarking against competitors", "New CHRO mandate on employee wellbeing"],
        "value": {"Productized service": "Tijori as a standard benefit alongside health insurance and PF.", "Reduced liability": "Organized records mean entitlements claimed correctly, reducing disputes.", "Client retention": "Genuine benefit increases employee loyalty at mid-career level.", "Recurring revenue": "Per-employee annual subscription that scales with headcount."},
        "filters": {"Pain": ("High", "hi"), "Activity": ("Active", "hi"), "Belief": ("Very high", "hi"), "Pay": ("Very high", "hi")},
    },
    {
        "id": "C1",
        "rank": 3,
        "type": "B2C",
        "name": "The Family Architect",
        "tagline": "Breadwinner with a large, complex life and a family that has zero visibility into any of it",
        "color_bg": "#1a0d1a",
        "color_accent": "#d97bca",
        "color_badge_bg": "#2a0a2a",
        "color_badge_text": "#d97bca",
        "definition": "A mid-to-late career professional or business owner with a large, complex asset base across financial, legal, and property document types. Has a family that depends on them but has no visibility into what exists or how to act if the primary person becomes unavailable. Has never organized their life because it felt morbid, premature, or too sensitive while healthy.",
        "merged": ["Financial — Investments: large corpus, no family visibility", "Financial — Insurance: family can't locate or claim policies", "Financial — Bank accounts: family can't locate accounts after death", "Financial — Loans: family inherits unknown debt", "Legal — Will: no will, estate defaults to intestacy", "Legal — Property: heirs can't establish ownership", "Personal/Social — Emergency contacts: family can't reach right people"],
        "struggle": {
            "push": "A complex, multi-decade life — financial assets, legal documents, property, informal arrangements — exists entirely in one person's knowledge and scattered across platforms, advisors, and physical files with no organized family-accessible record.",
            "pull": "A single, organized life record the family can open in any crisis — showing what exists, who has access to what, and exactly what to do across every dimension of the person's financial and legal life.",
            "anxiety": "The family is helpless at the worst possible moment — assets lost, rights contested, debts discovered too late. Decades of accumulated wealth and care undone by a failure to organize.",
            "inertia": "Organizing feels morbid while healthy. Verbal communication feels sufficient. No tool has felt trustworthy enough with data of this sensitivity."
        },
        "jobs": {
            "fn": "Consolidate the entire financial and legal life into one organized, family-accessible system. Audit and correct nominees, ownership records, and legal documents. Create step-by-step instructions the family can execute without professional help.",
            "so": "Be the responsible provider who prepared everything — who left the family with clarity rather than chaos, and whose care extended beyond their presence.",
            "em": "Eliminate the persistent, low-level dread of 'what happens to all of this if something happens to me.' Arrive at genuine peace of mind."
        },
        "triggers": ["Death or serious illness in peer circle", "Own health scare", "Child's birth or marriage", "Retirement approaching", "Advisor departing"],
        "value": {},
        "filters": {"Pain": ("Very high", "hi"), "Activity": ("Event-triggered", "mid"), "Belief": ("Needs trust", "mid"), "Pay": ("High", "hi")},
    },
    {
        "id": "C5",
        "rank": 4,
        "type": "B2C",
        "name": "The Emergency Preparer",
        "tagline": "Parent or spouse who knows viscerally that the right information at the right moment prevents irreversible harm",
        "color_bg": "#0d1a0d",
        "color_accent": "#4cd990",
        "color_badge_bg": "#0a2a0a",
        "color_badge_text": "#4cd990",
        "definition": "An individual — typically a parent or spouse in their 30s to 50s — who has experienced or vividly imagined a health emergency and understands viscerally that the right information, in the right hands, at the right moment, can prevent irreversible harm. They want a system that ensures any family member can act competently in any emergency — medical, financial, or logistical — without needing to reach the primary person first.",
        "merged": ["Personal/Social — Medical record: family can't communicate critical health info in ER", "Personal/Social — Emergency contacts: family can't reach right people in a crisis", "Compliance — Medical record: chronic condition, treatment continuity breaks", "Personal/Social — Pets: care breaks down when owner is unavailable"],
        "struggle": {
            "push": "Critical information — health, contacts, care instructions, current medications — exists in one person's knowledge or on their device, not in a form any other family member can access independently in a high-stress situation.",
            "pull": "A family-accessible emergency system — health summaries, critical contacts, care instructions — that any family member can open and act on immediately without needing to reach the primary person first.",
            "anxiety": "A preventable harm occurs in an emergency because the right information wasn't available: the wrong medication given, a specialist not called, a critical contact not reached. The harm is irreversible and entirely avoidable.",
            "inertia": "Assumes family members know enough. Assumes the patient's phone will be accessible. The gap is invisible until an emergency makes it devastatingly visible."
        },
        "jobs": {
            "fn": "Ensure every family member can immediately access critical health, contact, and care information for every other family member — without needing any device, password, or the primary person to be reachable.",
            "so": "Be the family member who had everything ready — who walked into any emergency prepared, not helpless.",
            "em": "Remove the specific, visceral anxiety of imagining a family member in an emergency and the right information not being there. Replace it with genuine, grounded readiness."
        },
        "triggers": ["Family member hospitalized unexpectedly", "Child starts traveling independently", "Elderly parent living alone", "Own chronic condition diagnosed"],
        "value": {},
        "filters": {"Pain": ("Very high", "hi"), "Activity": ("Converts fast", "hi"), "Belief": ("Very high", "hi"), "Pay": ("High", "hi")},
    },
    {
        "id": "B2",
        "rank": 5,
        "type": "B2B",
        "name": "Transaction Enabler",
        "tagline": "Real estate professional who loses deals, referrals, and relationships to property document disorganization",
        "color_bg": "#1a1200",
        "color_accent": "#f0b429",
        "color_badge_bg": "#2a1e00",
        "color_badge_text": "#f0b429",
        "definition": "A real estate professional — developer, broker, or housing society — whose transaction success, post-sale relationships, and operational management are directly shaped by how organized buyers, sellers, and residents are with their property documentation. Disorganization is the single most common cause of deal failures, post-handover friction, and society management breakdowns.",
        "merged": ["Builder — post-handover relationship dissolves, referral value lost", "Property broker — deals stall from seller document gaps", "Housing society — resident records fragmented, emergencies unmanageable"],
        "struggle": {
            "push": "Property document disorganization is the most common preventable cause of failed transactions, post-handover friction, and society management breakdowns — and the professional absorbs the commercial and reputational cost every time.",
            "pull": "Buyers, sellers, and residents who maintain organized property document records — so transactions close on time, handovers create lasting positive relationships, and societies run on records rather than memory.",
            "anxiety": "A deal falls through, a handover creates a negative brand moment, or a society emergency exposes the absence of a resident record — all for the same preventable reason.",
            "inertia": "Document organization is treated as the buyer's or seller's responsibility. The commercial case for investing in client organization hasn't been made internally."
        },
        "jobs": {
            "fn": "Offer Tijori as a document organization service at the point of transaction or handover — creating organized property records that protect deals, generate referrals, and differentiate the practice.",
            "so": "Be the real estate professional known for organized, friction-free transactions and lasting buyer relationships — not just deal sourcing.",
            "em": "Stop losing deals and referrals to a preventable, recurring problem — feel that the practice is built on a system that protects every transaction."
        },
        "triggers": ["High-value deal falls through over missing document", "Competitor builder differentiates on post-handover experience", "Society emergency exposes outdated resident record", "Buyer can't get loan because document chain incomplete"],
        "value": {"Productized service": "A 'document-ready listing' audit before any transaction begins.", "New client acquisition": "Clean transactions become word-of-mouth differentiators.", "Client retention": "Buyers with organized records return for every subsequent transaction.", "Reduced liability": "Documented handover record protects from future missing-document claims."},
        "filters": {"Pain": ("Very high", "hi"), "Activity": ("Post-deal fail", "hi"), "Belief": ("Very high", "hi"), "Pay": ("High", "hi")},
    },
    {
        "id": "C2",
        "rank": 6,
        "type": "B2C",
        "name": "The Responsible Child",
        "tagline": "Adult child managing an ageing parent's undocumented financial and legal life from a distance",
        "color_bg": "#0d1520",
        "color_accent": "#4ab8d4",
        "color_badge_bg": "#0a1e2e",
        "color_badge_text": "#4ab8d4",
        "definition": "An adult child — typically in their 30s or 40s, often living in a different city or abroad — whose ageing parent holds a complex financial, legal, and property life that was never documented. The parent's ability to manage it is declining. The child needs visibility and control without a full handover, and is actively looking for a solution before a crisis forces one.",
        "merged": ["Financial — Investments: adult child managing parent's declining cognition", "Legal — Property: heirs can't establish title after owner's death", "Legal — Business documents: family inherits founder business with no legal picture", "Personal/Social — Medical record: family can't communicate critical health info in emergency"],
        "struggle": {
            "push": "A parent's entire financial, legal, and personal life exists in their memory and in relationships — advisors, lawyers, banks — that the child cannot access. As the parent's capacity declines, the knowledge is becoming permanently inaccessible.",
            "pull": "Remote, organized visibility into the parent's full picture — every asset, document, contact, and time-sensitive action — accessible without requiring a full control transfer or disrupting the parent's dignity.",
            "anxiety": "Something irreversible happens — an asset lapses, a property is disputed, the parent is hospitalized — before the child has the information needed to act. The window to organize closes without warning.",
            "inertia": "Parent is still functional enough to resist. Intervention feels like taking over. Distance makes it easy to defer. The urgency isn't visible until a crisis makes it impossible."
        },
        "jobs": {
            "fn": "Get organized, remote visibility into the parent's full financial, legal, and health picture. Surface time-sensitive actions before they become permanent losses. Create a shared record the family can act on.",
            "so": "Be the child who stepped in and organized things before it was too late — not the one who scrambled through chaos after a crisis exposed the gap.",
            "em": "Stop carrying the quiet, persistent anxiety that something irreversible is happening while nothing is organized. Feel in control of a situation that currently feels out of control."
        },
        "triggers": ["Parent's first cognitive episode", "Parent hospitalized unexpectedly", "Peer's parent passes away in chaos", "Advisor or lawyer the parent relied on retires"],
        "value": {},
        "filters": {"Pain": ("High & growing", "hi"), "Activity": ("Actively searching", "hi"), "Belief": ("Moderate", "mid"), "Pay": ("High", "hi")},
    },
    {
        "id": "C3",
        "rank": 7,
        "type": "B2C",
        "name": "The Founder at Risk",
        "tagline": "Founder whose business and family collapse simultaneously when they become unavailable",
        "color_bg": "#1a0d00",
        "color_accent": "#f07040",
        "color_badge_bg": "#2a1500",
        "color_badge_text": "#f07040",
        "definition": "A founder or sole proprietor of a small-to-mid business whose entire operational, legal, and compliance knowledge is concentrated in themselves. A hospitalization or sudden absence creates both a personal family crisis and a business continuity crisis simultaneously — and they have never built a system to separate the two or ensure either can continue without them.",
        "merged": ["Legal — Business documents: founder unavailable, business has no legal representation", "Compliance — Business documents: compliance lapses silently", "Financial — Investments: large corpus, no family visibility (personal dimension)", "Legal — Will: no will, business and personal estate undifferentiated"],
        "struggle": {
            "push": "The founder is the single point of knowledge and authority for both their personal financial life and their business — credentials, compliance deadlines, signing authority, and asset records all concentrated in one person with no documented backup.",
            "pull": "A separation of personal and business records — each organized, documented, and accessible to the right trusted person — so absence triggers a managed handover rather than simultaneous personal and business collapse.",
            "anxiety": "A health event triggers two simultaneous crises: the family discovers they have no financial picture, and the business discovers it has no legal representation or compliance continuity. Both are irreversible within days.",
            "inertia": "Building a system feels like a distraction from running the business. Trusts key employees to figure it out. Has never been absent long enough for the fragility to become visible."
        },
        "jobs": {
            "fn": "Document the full personal financial life for the family AND the full business operational and legal structure for a trusted successor — so any period of unavailability triggers a managed, informed handover rather than chaos on both fronts.",
            "so": "Be the founder who built something resilient — whose business and family are both protected by a system, not dependent on a single person's constant availability.",
            "em": "Stop carrying the unspoken weight of knowing that everything — business and family — collapses if something happens to them. Feel genuinely secure rather than indispensable in a fragile way."
        },
        "triggers": ["Own health scare", "Fellow founder's sudden death", "Business partner dispute exposing undocumented arrangements", "CA or CS departure"],
        "value": {},
        "filters": {"Pain": ("Very high", "hi"), "Activity": ("Event-triggered", "mid"), "Belief": ("Moderate", "mid"), "Pay": ("High", "hi")},
    },
    {
        "id": "C4",
        "rank": 8,
        "type": "B2C",
        "name": "The Compliance Carrier",
        "tagline": "Household manager overwhelmed by fragmented compliance obligations that lapse silently and punish loudly",
        "color_bg": "#0f0f1a",
        "color_accent": "#7b6cf0",
        "color_badge_bg": "#1a1530",
        "color_badge_text": "#9b8cf0",
        "definition": "A working professional or household manager — typically in their 30s to 50s — responsible for managing a complex web of time-sensitive compliance obligations across vehicles, insurance policies, employment records, and household services. The obligations are distributed, the reminders are fragmented, and a lapse in any one triggers a disproportionate consequence that lands on them personally.",
        "merged": ["Compliance — Vehicles: lapse discovered at traffic stop or accident", "Compliance — Vehicles: multi-vehicle family, no consolidated view", "Compliance — Insurance: policy lapses silently, discovered at claim", "Compliance — Medical record: claim rejected for lack of documented history", "Compliance — Employee: PF and gratuity unclaimed", "Compliance — Service provider: household services break down"],
        "struggle": {
            "push": "Compliance obligations — renewals, filings, certifications, employment records — are distributed across different systems and channels with no single place to see what is current, what is due, and what is at risk.",
            "pull": "A unified compliance calendar and record — every obligation, renewal date, and current status in one place — with reminders early enough to act even during a busy or distracted period.",
            "anxiety": "A lapse is discovered only when the consequence arrives — at a traffic stop, an accident, a hospital, a claim. The consequence is disproportionate to the administrative failure that caused it.",
            "inertia": "Has always managed reactively and it has mostly worked. The risk feels theoretical until a lapse makes the cost real."
        },
        "jobs": {
            "fn": "Maintain a complete, real-time view of every compliance obligation with proactive reminders — so nothing ever lapses silently and every consequence is preventable.",
            "so": "Be the organized household manager who is never caught off-guard — never fined, never rejected, never scrambling at the moment when being prepared would have cost nothing.",
            "em": "Shed the low-level, persistent anxiety of managing too many obligations across too many systems — feel that everything is genuinely under control rather than just probably fine."
        },
        "triggers": ["Insurance lapse discovered at claim", "Traffic fine for expired PUC", "PF claim from previous employer rejected", "Family member in accident in uninsured vehicle"],
        "value": {},
        "filters": {"Pain": ("Spikes at lapse", "mid"), "Activity": ("Post-lapse", "mid"), "Belief": ("High", "hi"), "Pay": ("Mid to high", "mid")},
    },
    {
        "id": "C6",
        "rank": 9,
        "type": "B2C",
        "name": "The Legacy Keeper",
        "tagline": "Family elder who carries irreplaceable identity, memory, and context that will vanish without a record",
        "color_bg": "#1a1000",
        "color_accent": "#e8b84b",
        "color_badge_bg": "#2a1c00",
        "color_badge_text": "#e8b84b",
        "definition": "An individual — often a family elder, a culturally conscious parent, or the person who holds the family together socially — who is acutely aware that irreplaceable things: recipes, traditions, photographs, family history, relationships, objects of significance — will be permanently lost when they are gone. They want to preserve not just the financial and legal life but the human life — the context, the identity, and the memory that makes the family distinctly itself.",
        "merged": ["Personal/Social — Family secrets: critical context dies with the person who held it", "Personal/Social — Traditions / Recipe / Paintings: irreplaceable identity lost", "Personal/Social — Photo/Video: visual memory lost to device or account failure", "Personal/Social — Friends/Relatives: social world undocumented at death", "Personal/Social — Birthday/Anniversary: family social fabric frays without a keeper"],
        "struggle": {
            "push": "Everything irreplaceable — recipes, stories, photographs, relationships, traditions — exists in one person's memory, habits, and devices. There is no system to transfer it to the people who will need it.",
            "pull": "A personal legacy archive — organized, accessible, and alive — that the family can return to long after the person is gone. Not just documents, but context, identity, and the things that made this family distinctly itself.",
            "anxiety": "The things that matter most — the recipe that defined every celebration, the story behind a photograph, the relationship that should have been honored — are gone permanently because they were never written down in time.",
            "inertia": "There is always more time. The person is still present. Documenting feels unnecessary while they can still be asked. The urgency only arrives after it is too late."
        },
        "jobs": {
            "fn": "Create a living, organized personal legacy archive — recipes, stories, traditions, photographs, relationships — that the family can access, use, and build on long after the person who held it is gone.",
            "so": "Be the generation that chose to preserve rather than let things disappear — who gave the next generation the context and identity they need to know where they came from.",
            "em": "Not let the most personal parts of a life vanish without a trace — feel that what was held has been passed on in a form that outlasts the person who carried it."
        },
        "triggers": ["Death of a parent or elder", "Child leaving home or getting married", "Own serious illness", "Family gathering with a 'we should have recorded this' moment"],
        "value": {},
        "filters": {"Pain": ("Irreversible when hit", "hi"), "Activity": ("Low until triggered", "lo"), "Belief": ("High", "hi"), "Pay": ("Mid to high", "mid")},
    },
    {
        "id": "B3",
        "rank": 10,
        "type": "B2B",
        "name": "Institutional Care Provider",
        "tagline": "Hospital or elder care facility treating patients and residents on dangerously incomplete information",
        "color_bg": "#0d1a1a",
        "color_accent": "#40c8c8",
        "color_badge_bg": "#0a2a2a",
        "color_badge_text": "#40c8c8",
        "definition": "A healthcare or elder care institution — hospital, nursing home, or assisted living facility — whose clinical outcomes, liability exposure, and family trust are directly shaped by how organized patients and residents are with their personal health and legal records. Every emergency treated on incomplete information is a clinical risk. Every outdated resident record is a liability event waiting to happen.",
        "merged": ["Hospital — emergency treatment on incomplete patient information", "Elder care facility — resident records outdated, emergencies unmanageable"],
        "struggle": {
            "push": "Patients and residents arrive without portable, current personal health and legal records. Treatment and care decisions are made on incomplete information. Every gap is a clinical risk and a potential liability event.",
            "pull": "Patients and residents who maintain current, family-shared personal health and legal records — so every clinical and care decision is informed, every emergency is manageable.",
            "anxiety": "An adverse event occurs that a complete record would have prevented. The institution is held liable for a decision made on information it had no system to obtain more completely.",
            "inertia": "Patient-held records are not a standard institutional expectation. Procurement cycles are long. The partnership model hasn't been framed in clinical and liability outcome terms."
        },
        "jobs": {
            "fn": "Partner with Tijori to make organized, current personal health and legal records a standard expectation — improving clinical outcomes and reducing liability through better information at point of care.",
            "so": "Be the institution that champions patient and resident preparedness — a visible quality signal in a sector where clinical reputation is the primary competitive differentiator.",
            "em": "Reduce the clinical anxiety of treating people on incomplete information — feel that every patient arrives with at least the basic facts needed to serve them safely."
        },
        "triggers": ["Adverse event from medication conflict or unknown allergy", "Liability claim citing incomplete records", "NABH or JCI accreditation review", "Competitor hospital launches patient preparedness program"],
        "value": {"Reduced liability": "Patient-held records reduce adverse events from information gaps.", "New client acquisition": "Attracts health-conscious HNI patients who value preparedness.", "Productized service": "Tijori as part of a premium concierge health program.", "Client retention": "Families who trust the facility has complete resident records stay longer."},
        "filters": {"Pain": ("Very high", "hi"), "Activity": ("Post-liability", "mid"), "Belief": ("Low", "lo"), "Pay": ("Very high", "hi")},
    },
]

RANK_DATA = [
    (1,  "B1", "B2B", "Professional whose practice is damaged by client disorganization", "hi","mid","mid","hi", "Highest reach — one advisor brings dozens of end users. Recurring institutional revenue."),
    (2,  "B4", "B2B", "HR leader offering Tijori as employee benefit at corporate scale", "hi","hi","hi","hi",  "One HR deal = hundreds of users. Corporate budget removes price sensitivity."),
    (3,  "C1", "B2C", "Breadwinner with large corpus and zero family visibility", "hi","mid","mid","hi",      "Largest B2C segment by volume. Highest financial stakes. Core product use case."),
    (4,  "C5", "B2C", "Individual ensuring family can act in any health emergency", "hi","hi","hi","hi",      "Highest belief in B2C. Converts immediately once scenario is imagined. Natural entry point."),
    (5,  "B2", "B2B", "Real estate professional losing deals to document gaps", "hi","hi","hi","hi",         "Very high belief, direct ROI in commissions saved. Strong referral flywheel."),
    (6,  "C2", "B2C", "Adult child managing ageing parent's undocumented life", "hi","hi","mid","hi",       "Already in problem-solving mode. High activity makes conversion easier than C1."),
    (7,  "C3", "B2C", "Founder whose business and family collapse simultaneously on unavailability", "hi","mid","mid","hi", "Two simultaneous failure modes. Reachable through B1 partners serving the same person."),
    (8,  "C4", "B2C", "Household manager overwhelmed by fragmented compliance obligations", "mid","mid","hi","mid",     "High belief, broad addressable market. Fast conversion after a single lapse event."),
    (9,  "C6", "B2C", "Family elder preserving irreplaceable identity and memory", "hi","lo","hi","mid",    "Emotionally powerful but hard to activate cold. Best as an upsell after C1 or C2."),
    (10, "B3", "B2B", "Hospital or elder care facility treating patients on incomplete records", "hi","mid","lo","hi",  "Highest long-term value, lowest near-term convertibility. A 12–24 month play."),
]

NOTES = [
    ("nb-start", "nh-start", "Start with B1 and B4",
     "The Client-Risk Advisor and Corporate Welfare Champion are the two highest-priority acquisitions because each one brings dozens to hundreds of end users with a single conversion. One CA with 50 HNI clients is worth 50 B2C acquisitions. One HR deal at a 500-person company is worth 500. These are distribution channels, not just customers."),
    ("nb-entry", "nh-entry", "B2C entry point is C5, not C1",
     "The Emergency Preparer converts fastest and with the least friction — the value is immediately visceral and the trust bar is lower because the first use case is health information, not financial data. Onboard them through the emergency health card, then expand into the full financial and legal life. C1 is the larger segment but requires more trust-building before uploading financial data."),
    ("nb-expand", "nh-expand", "C3 and C6 are expansion ICPs, not acquisition ICPs",
     "The Founder at Risk is best reached through B1 partners who already serve them. The Legacy Keeper is an emotional upsell once the practical foundation is in place. Neither converts well cold — they are deepening plays once the user is already on the platform."),
    ("nb-avoid", "nh-avoid", "B3 is a 2026 play, not today",
     "Hospital partnerships require clinical evidence, long procurement cycles, and institutional champions. Build the product, accumulate the B2C user base and emergency health use cases, then approach with data. Attempting this early wastes sales resources on a cycle that cannot close in the near term."),
    ("nb-long", "nh-long", "Medical Record is the most cross-cutting document type",
     "Medical Record appears across three groups — Compliance (insurance claims), Personal/Social (emergency access), and as a thread through C5 (Emergency Preparer) and C2 (Responsible Child). The emergency health card is the single highest-belief feature in the entire product and the most natural first-use onboarding moment across multiple ICPs."),
    ("nb-start", "nh-start", "The framework produced 10 ICPs from 52 persona cards",
     "36 B2C cards across 4 groups (Financial, Legal, Compliance, Personal/Social) merged into 6 B2C ICPs. 16 B2B cards across 4 partner categories merged into 4 B2B ICPs. The merge logic: same user + same functional job + same push/anxiety = merge. Different failure mode = separate ICP even if the document type overlaps."),
]

# ── State ────────────────────────────────────────────────────────────────────
if "page" not in st.session_state:
    st.session_state.page = 0

total_pages = 12  # 10 ICPs + rankings + notes

def go(p): st.session_state.page = p

# ── Nav bar ──────────────────────────────────────────────────────────────────
dots_html = '<div class="page-dots">'
for i in range(12):
    cls = "dot"
    if i < 10:
        cls += " b2b" if ICPS[i]["type"] == "B2B" else ""
    if i == st.session_state.page:
        cls += " active"
    dots_html += f'<div class="{cls}"></div>'
dots_html += "</div>"

st.markdown(f"""
<div class="nav-bar">
  <div class="nav-logo">TIJORI.AI — ICP CARDS</div>
  <div class="nav-count">PAGE {st.session_state.page + 1} / 12</div>
</div>
{dots_html}
""", unsafe_allow_html=True)

# ── Render page ──────────────────────────────────────────────────────────────
p = st.session_state.page

def filter_dot(level):
    if level == "hi":  return "●", "sv-hi"
    if level == "mid": return "●", "sv-mid"
    return "●", "sv-lo"

def filter_val_class(level):
    if level == "hi":  return "sv-hi"
    if level == "mid": return "sv-mid"
    return "sv-lo"

if p < 10:
    icp = ICPS[p]
    acc = icp["color_accent"]
    bg  = icp["color_bg"]

    # ── Stats row ──
    filters_html = ""
    for k, (v, lv) in icp["filters"].items():
        vc = filter_val_class(lv)
        filters_html += f"""
        <div class="stat-box">
          <div class="stat-label">{k}</div>
          <div class="stat-value {vc}">{v}</div>
        </div>"""

    # ── Merged tags ──
    tags_html = "".join(f'<span class="tag">{t}</span>' for t in icp["merged"])

    # ── Struggle ──
    s = icp["struggle"]
    struggle_html = f"""
    <div class="struggle-grid">
      <div class="struggle-box">
        <div class="struggle-label sl-push">Push</div>
        <div class="struggle-text">{s['push']}</div>
      </div>
      <div class="struggle-box">
        <div class="struggle-label sl-pull">Pull</div>
        <div class="struggle-text">{s['pull']}</div>
      </div>
      <div class="struggle-box">
        <div class="struggle-label sl-ax">Anxiety</div>
        <div class="struggle-text">{s['anxiety']}</div>
      </div>
      <div class="struggle-box">
        <div class="struggle-label sl-in">Inertia</div>
        <div class="struggle-text">{s['inertia']}</div>
      </div>
    </div>"""

    # ── Jobs ──
    j = icp["jobs"]
    jobs_html = f"""
    <div class="jobs-grid">
      <div class="job-box">
        <div class="job-type jt-fn">Functional</div>
        <div class="job-text">{j['fn']}</div>
      </div>
      <div class="job-box">
        <div class="job-type jt-so">Social</div>
        <div class="job-text">{j['so']}</div>
      </div>
      <div class="job-box">
        <div class="job-type jt-em">Emotional</div>
        <div class="job-text">{j['em']}</div>
      </div>
    </div>"""

    # ── Triggers ──
    triggers_html = "".join(f'<span class="trigger-pill">{t}</span>' for t in icp["triggers"])

    # ── Value (B2B only) ──
    value_html = ""
    if icp["value"]:
        vboxes = "".join(f"""
        <div class="value-box">
          <div class="value-label">{k}</div>
          <div class="value-text">{v}</div>
        </div>""" for k, v in icp["value"].items())
        value_html = f"""
        <div class="sec-label">Value dimensions</div>
        <div class="value-grid">{vboxes}</div>"""

    type_label = "B2B PARTNER" if icp["type"] == "B2B" else "B2C INDIVIDUAL"

    st.markdown(f"""
    <div class="card-shell">
      <div class="card-header" style="background:{bg};">
        <div class="card-meta">
          <span class="card-type-badge" style="background:{icp['color_badge_bg']};color:{icp['color_badge_text']};">{type_label}</span>
          <span class="card-rank" style="color:{acc};">RANK #{icp['rank']} / 10</span>
        </div>
        <div class="card-name" style="color:{acc};">{icp['name']}</div>
        <div class="card-tagline">{icp['tagline']}</div>
      </div>

      <div class="card-body">
        <div class="stat-row">{filters_html}</div>

        <div class="sec-label">Definition</div>
        <div class="def-text">{icp['definition']}</div>

        <div class="sec-label" style="margin-top:14px;">Merged from</div>
        <div class="tag-row">{tags_html}</div>

        <div class="sec-label" style="margin-top:14px;">Struggle</div>
        {struggle_html}

        <div class="sec-label">Jobs to be done</div>
        {jobs_html}

        <div class="sec-label" style="margin-top:14px;">Activation triggers</div>
        <div class="trigger-row">{triggers_html}</div>

        {value_html}
      </div>

      <div class="card-footer" style="background:{bg};">
        <span class="footer-type">{icp['id']} — TIJORI.AI ICP FRAMEWORK</span>
        <span class="footer-id">{icp['id']}</span>
      </div>
    </div>
    """, unsafe_allow_html=True)

elif p == 10:
    # Rankings table
    def dot_s(lv):
        if lv == "hi":  return '<span class="dot-hi-s">●●●</span>'
        if lv == "mid": return '<span class="dot-mid-s">●●○</span>'
        return '<span class="dot-lo-s">●○○</span>'

    rows = ""
    for rank, icp_id, typ, scenario, pain, act, bel, pay, why in RANK_DATA:
        type_class = "type-b2b" if typ == "B2B" else "type-b2c"
        rows += f"""
        <tr>
          <td><span class="rank-num" style="color:#{'4cd990' if rank<=2 else 'f0b429' if rank<=6 else '888'};">{rank}</span></td>
          <td><span class="{type_class}" style="font-family:'Space Mono',monospace;font-size:0.65rem;">{icp_id}</span><br><span class="icp-name-cell">{next(i['name'] for i in ICPS if i['id']==icp_id)}</span></td>
          <td><span class="{type_class}">{typ}</span></td>
          <td style="font-size:0.7rem;color:#888;">{scenario}</td>
          <td>{dot_s(pain)}</td>
          <td>{dot_s(act)}</td>
          <td>{dot_s(bel)}</td>
          <td>{dot_s(pay)}</td>
          <td><span class="why-text">{why}</span></td>
        </tr>"""

    st.markdown(f"""
    <div class="rank-card">
      <div class="rank-header">
        <div class="rank-title">All 10 ICPs — Ranked</div>
        <div class="rank-sub">Ranked by composite of pain intensity, ability to pay, activity level, and belief. Rank reflects who to acquire first.</div>
      </div>
      <div style="padding:0 0 1rem;overflow-x:auto;">
        <table class="rank-table">
          <thead><tr>
            <th>#</th><th>ICP</th><th>Type</th><th>Core scenario</th>
            <th>Pain</th><th>Activity</th><th>Belief</th><th>Pay</th><th>Why this rank</th>
          </tr></thead>
          <tbody>{rows}</tbody>
        </table>
      </div>
    </div>
    """, unsafe_allow_html=True)

else:
    # Notes page
    notes_html = ""
    for cls, hcls, heading, body in NOTES:
        notes_html += f"""
        <div class="note-block {cls}">
          <div class="note-heading {hcls}">{heading}</div>
          <div class="note-text">{body}</div>
        </div>"""

    st.markdown(f"""
    <div class="notes-card">
      <div class="notes-title">Strategic Notes</div>
      <div class="notes-sub">Key takeaways from the ICP merge — acquisition sequence, entry points, and long-term plays</div>
      {notes_html}
    </div>
    """, unsafe_allow_html=True)

# ── Navigation ───────────────────────────────────────────────────────────────
st.markdown("<div style='height:1.4rem'></div>", unsafe_allow_html=True)
c1, c2, c3 = st.columns([1, 2, 1])
with c1:
    if st.button("← Prev", disabled=p == 0):
        go(p - 1)
        st.rerun()
with c2:
    cols = st.columns(6)
    shortcuts = [
        ("B1", 0), ("B4", 1), ("C1", 2),
        ("C5", 3), ("B2", 4), ("C2", 5),
    ]
    for i, (label, idx) in enumerate(shortcuts):
        with cols[i]:
            if st.button(label, key=f"sc_{idx}"):
                go(idx)
                st.rerun()
with c3:
    if st.button("Next →", disabled=p == total_pages - 1):
        go(p + 1)
        st.rerun()

st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)
c4, c5, c6 = st.columns([1, 2, 1])
with c4:
    pass
with c5:
    cols2 = st.columns(6)
    shortcuts2 = [
        ("C3", 6), ("C4", 7), ("C6", 8),
        ("B3", 9), ("📊", 10), ("📝", 11),
    ]
    for i, (label, idx) in enumerate(shortcuts2):
        with cols2[i]:
            if st.button(label, key=f"sc2_{idx}"):
                go(idx)
                st.rerun()
with c6:
    pass