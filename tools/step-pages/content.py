# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Content data for the workflow step pages.
# This is the single source of truth for the 20 step detail pages.
# Edit content here, then re-run:  python3 tools/step-pages/generate.py
#
# Each step is a dict: wf, n, name, summary, parts.
# parts is an ordered list of tuples:
#   ("text",   html)     -> a body paragraph (html is inserted as-is)
#   ("prompt", rawtext)  -> a copyable prompt block (generator HTML-escapes it)
#   ("raw",    html)     -> raw HTML inserted as-is (used for the model grid)
# ---------------------------------------------------------------------------

WORKFLOWS = {
    "ugc": {
        "name": "UGC Video Creator Workflow",
        "page": "workflow-ugc-video-creator.html",
        "slug": "workflow-ugc-step",
        "total": 13,
    },
    "reference": {
        "name": "Reference to Design Workflow",
        "page": "workflow-reference-to-design.html",
        "slug": "workflow-reference-step",
        "total": 7,
    },
    "banner-creator": {
        "name": "AI Banner Creator Workflow",
        "page": "workflow-banner-creator.html",
        "slug": "workflow-banner-creator-step",
        "total": 9,
    },
}

# Model-look grid for UGC Step 06. Thumbnails (.ugc-models) and the
# click-to-reveal descriptions (.ugc-model-descs) are separate blocks so
# an expanded description spans the full content width, not the thumbnail
# column. accordion.js links trigger -> description by aria-controls/id.
MODEL_GRID = """<div class="ugc-models">
  <div class="ugc-model">
    <button class="accordion__header ugc-model__trigger" type="button" aria-expanded="false" aria-controls="ugc-model-yellow">
      <img src="assets/workflow-ugc-models/model-yellow-curtains.jpg?v=2" alt="Model look — Yellow curtains" width="1200" height="1200" loading="lazy">
      <span class="ugc-model__bar"><span class="ugc-model__label">Yellow curtains</span><span class="accordion__plus" aria-hidden="true">+</span></span>
    </button>
  </div>
  <div class="ugc-model">
    <button class="accordion__header ugc-model__trigger" type="button" aria-expanded="false" aria-controls="ugc-model-grey">
      <img src="assets/workflow-ugc-models/model-grey-bathroom.jpg?v=2" alt="Model look — Grey bathroom" width="1200" height="1200" loading="lazy">
      <span class="ugc-model__bar"><span class="ugc-model__label">Grey bathroom</span><span class="accordion__plus" aria-hidden="true">+</span></span>
    </button>
  </div>
  <div class="ugc-model">
    <button class="accordion__header ugc-model__trigger" type="button" aria-expanded="false" aria-controls="ugc-model-white">
      <img src="assets/workflow-ugc-models/model-white-bedroom.jpg?v=2" alt="Model look — White bedroom" width="1200" height="1200" loading="lazy">
      <span class="ugc-model__bar"><span class="ugc-model__label">White bedroom</span><span class="accordion__plus" aria-hidden="true">+</span></span>
    </button>
  </div>
  <div class="ugc-model">
    <button class="accordion__header ugc-model__trigger" type="button" aria-expanded="false" aria-controls="ugc-model-cream">
      <img src="assets/workflow-ugc-models/model-cream-gallery.jpg?v=2" alt="Model look — Cream gallery wall" width="1200" height="1200" loading="lazy">
      <span class="ugc-model__bar"><span class="ugc-model__label">Cream gallery wall</span><span class="accordion__plus" aria-hidden="true">+</span></span>
    </button>
  </div>
  <div class="ugc-model">
    <button class="accordion__header ugc-model__trigger" type="button" aria-expanded="false" aria-controls="ugc-model-matte">
      <img src="assets/workflow-ugc-models/model-matte-white.jpg?v=2" alt="Model look — Matte white room" width="1200" height="1200" loading="lazy">
      <span class="ugc-model__bar"><span class="ugc-model__label">Matte white room</span><span class="accordion__plus" aria-hidden="true">+</span></span>
    </button>
  </div>
</div>
<div class="ugc-model-descs">
  <div class="accordion__body is-collapsed ugc-model__desc" id="ugc-model-yellow">
    <p>Setting: side of an open window with morning sunlight entering from the left; light pale yellow linen curtains with teal woven motifs; white wall; three framed graphic prints in beige, light yellow, and muted teal. Props: monstera plant slightly behind the model on the right; wooden study desk; two physics textbooks stacked on the desk, covers in white and beige; ceramic off-white coffee mug. Model: Indian woman, mid-20s, medium Indian skin tone, average body type, shoulder-length natural wavy hair worn open, no base makeup, visible skin texture, lip balm only. Outfit: fuchsia pink cotton kurti with matching fabric buttons, oxidised silver jhumkas, no bangles, no necklace.</p>
  </div>
  <div class="accordion__body is-collapsed ugc-model__desc" id="ugc-model-grey">
    <p>Setting: flat grey painted wall in a modern apartment; soft daylight from a window in front of the model; matte finish wall, no texture or pattern; round mirror with a thin black metal frame partially visible on the right. Props: light grey marble vanity counter at the bottom of the frame; minimal floating shelf on the grey wall; white ceramic planter with an upright snake plant; two frosted glass skincare bottles beside the planter. Model: Indian woman, mid-20s, light-medium Indian skin tone, slim to average body type, sleek straight hair tied in a low ponytail, no base makeup, visible skin texture, natural lips. Outfit: off-white ribbed tank top, small gold hoop earrings, no necklace, no bangles.</p>
  </div>
  <div class="accordion__body is-collapsed ugc-model__desc" id="ugc-model-white">
    <p>Setting: side of a large bedroom window with soft morning sunlight from the left; sheer white cotton curtains partially drawn, diffusing light into the room; clean white wall with no artwork; soft sunlight creating gentle shadow patterns. Props: bed beside the window; white cotton bedsheet neatly spread; light wooden side table next to the bed; ceramic off-white vase with eucalyptus stems; closed beige notebook flat on the bed near the model. Model: Indian woman, late-20s, light-medium Indian skin tone, average body type, open hair with natural air-dried texture, no base makeup, visible skin texture, skincare-fresh face. Outfit: pastel blue cotton top, tiny silver stud earrings, no necklace, no bangles.</p>
  </div>
  <div class="accordion__body is-collapsed ugc-model__desc" id="ugc-model-cream">
    <p>Setting: warm cream painted walls; soft afternoon sunlight from the right; salon-style gallery wall behind the model with multiple framed graphic prints in deep teal, mustard yellow, terracotta, dusty pink, and beige; frames in dark wood and matte black. Props: dark teak wooden bed behind the model; patterned cotton bedsheet in maroon, indigo, and beige motifs; layered cushions in solid mustard, deep teal, and off-white; carved wooden bedside table; brass table lamp with a warm beige fabric lampshade; small stack of earthy-toned books; ceramic incense holder; tall areca palm plant behind the model on the left. Model: Indian woman, late-20s, medium-deep Indian skin tone, curvy body type, hair tied in a low bun with loose face-framing strands, no base makeup, visible skin texture, lip balm only. Outfit: solid emerald green cotton kurti with subtle woven texture, oxidised silver jhumka earrings, small maroon bindi, no bangles, no necklace.</p>
  </div>
  <div class="accordion__body is-collapsed ugc-model__desc" id="ugc-model-matte">
    <p>Setting: clean matte white room with white walls and ceiling; soft natural daylight from a window in front of the model; even, shadow-free lighting; subtle colour accents in cobalt blue and pale yellow. Wall: three framed graphic art prints on the white wall, simple geometric shapes and line illustrations, cobalt blue / pale yellow / beige palette, thin white frames, modern minimal calm style. Props: small white wall shelf; two stacked books, one solid pale yellow cover and one solid cobalt blue; white ceramic planter with a small round-leaved plant; cobalt blue ceramic tray with cotton pads arranged neatly; clear glass water bottle beside the tray; no foreground surface. Model: Indian woman, late-20s, medium to light-medium Indian skin tone, average body type, shoulder-length natural air-dried hair worn open, no base makeup, visible real skin texture, skincare-fresh finish. Outfit: pale yellow ribbed top, small gold stud earrings, no necklace, no bangles, no rings.</p>
  </div>
</div>"""

STEPS = [
    # ===================== UGC Video Creator Workflow =====================
    {
        "wf": "ugc", "n": 1, "name": "Starter Prompt",
        "summary": "Give GPT the context for the whole workflow.",
        "parts": [
            ("text", "Start a new GPT chat and paste in the starter prompt below. This gives GPT the context of what you're creating, and it will stay within these guidelines for the rest of the chat."),
            ("prompt", """You are creating a complete set of UGC-style, phone-shot visual assets for an Indian beauty brand.

The output is not a single image or clip.
The output is a coherent visual system for one video.

All visuals must feel like they were filmed:
- By the same woman
- In the same space
- During the same filming session
- Using the same phone

This is a visual continuity system, not standalone shots.

Format: Please don't give me too much information at once, always explain only one idea at a time to me, and only when I tell you I have understood it and am ready to move on, then do so.

Don't give me a game plan next, I'm following a workflow, so just ask me for the next step."""),
        ],
    },
    {
        "wf": "ugc", "n": 2, "name": "Feeding Product Information",
        "summary": "Build a product information card — two ways.",
        "parts": [
            ("text", "There are two ways to build your product information card. Choose based on whether your product already has internal research."),
            ("text", "<strong>Option A — Product is in the Generated Products drive.</strong> The D2S team has interviewed Brand Managers and built detailed documents for some PB products. If your product is in the internal drive, download all the documents in its Logs folder and use them with the prompt below to get a product information card. Ask Lucid for access to the Generated Products drive."),
            ("prompt", """ROLE
You are a structured data-extraction and synthesis agent.
Your job is to create one exhaustive INTERNAL product information card by reading the uploaded documents.
This task is purely factual.
Do not:
- Market the product
- Improve wording
- Add skincare knowledge
- Infer intent or benefits
- Fill gaps creatively
If information is not explicitly stated, write "Not found".
Accuracy and completeness are more important than brevity.

SOURCE CONSTRAINT
Use ONLY the uploaded internal documents:
- Brand identity
- Product research
- USP and themes
- Funnel stage notes
- SKU, pricing, packaging, audience or strategy files
Do NOT use PDPs, reviews, or external knowledge.

EXTRACTION LOGIC (IMPORTANT)
You must perform one full scan of all documents.
For each section below:
- Actively search for relevant information
- Collect all matching details
- Preserve original phrasing where possible
- If multiple statements exist, list all
If a section has zero explicit data, return "Not found".

INFORMATION CLASSES TO EXTRACT

1. PRODUCT IDENTIFICATION
Extract: Brand name; Product name; Product category; Sub-category or format (if mentioned); Variant names; Size / quantity; Any additional SKUs or minis mentioned

2. PRICE & COMMERCIAL STRUCTURE
Extract: MRP; Selling price(s); Discount values; Pack pricing; Offer mechanics; Threshold offers; Bundle mentions
Use exact wording from documents.

3. PRODUCT FORMAT & PHYSICAL ATTRIBUTES
Extract: Form factor (jar, tube, pump, etc.); Material (plastic, glass, etc.); Texture description (if documented); Packaging shape; Dominant colours; Visual design notes; Any references to clinical / fun / premium / accessible look

4. INGREDIENT STRUCTURE (INTERNAL VIEW)
Extract: Hero ingredient(s); Supporting ingredients; Ingredient groupings (e.g. "boosted with"); Any percentages; Any hierarchy of actives
Do NOT explain benefits unless explicitly written.

5. CLAIMS & ASSERTIONS
Extract verbatim: Primary claims; Secondary claims; Quantified claims (2X, 3X, 10X, etc.); Safety positioning; Approval mentions (dermat-approved, etc.); Time-to-results statements; Comparative statements (if stated)

6. USAGE & ROUTINE DEFINITION
Extract: How to use instructions; Frequency; Time of use (day/night); Routine placement (first step, last step, etc.); Application cues; Caution notes or disclaimers

7. TARGET USER INTELLIGENCE
Extract only what is explicitly stated: Age range; Gender; Geography; Income / SEC; Primary target group; Secondary target group; Use-case users (beginners, men, teens, etc.)

8. PSYCHOGRAPHIC & MOTIVATIONAL SIGNALS
Extract: Attitudes; Frustrations; Values; Purchase drivers; Emotional or mindset descriptors
Use document language only.

9. BRAND & COMMUNICATION SYSTEM
Extract: Brand persona descriptors; Tone or voice cues; Brand archetype language; Typography; Colour system; Visual language notes

10. INTERNAL THEMES & STRATEGIC FRAMING
Extract: Core themes; Non-primary themes; Usage-led themes; Benefit-led themes; Social proof or trust themes; Funnel-stage positioning cues
Do not prioritise or reinterpret.

FINAL OUTPUT FORMAT (STRICT)
Return one clean, structured card:

PRODUCT INFO CARD — INTERNAL INTELLIGENCE (NON-PDP)

BASICS
Brand:
Product Name:
Category:
Variant / Size:
Additional SKUs:

PRICE & VALUE
MRP:
Selling Price:
Discount:
Offer Notes:

PRODUCT FORMAT & PHYSICAL ATTRIBUTES
Form Factor:
Material:
Packaging Description:
Texture (if mentioned):
Dominant Colours:

INGREDIENT STRUCTURE
Hero Ingredient(s):
Supporting Ingredients:
Ingredient Percentages:

CLAIMS & POSITIONING

USAGE & ROUTINE
How to Use:
Frequency:
Routine Placement:
Cautions:

TARGET USER INTELLIGENCE
Demographics:
Primary TG:
Secondary TG:

PSYCHOGRAPHIC SIGNALS

BRAND & COMMUNICATION CONTEXT
Brand Persona:
Typography:
Visual Language:

INTERNAL THEMATIC FRAMING
Core Themes:
Secondary Themes:"""),
            ("text", "<strong>Option B — Product is not in the drive.</strong> If your product isn't in the drive, build the card from its Purplle PDP and reviews instead. Copy the prompt below, add your product's PDP link and screenshots of a few detailed reviews, and make sure Agent Mode is selected before you send it. If a mini computer screen opens in your GPT chat, agent mode is working and GPT is crawling the PDP."),
            ("prompt", """You are a data-extraction and synthesis agent.
Your task is to perform ONE complete crawl across TWO Purplle URLs + Screenshots of reviews for the SAME product and return ONE hook-ready product intelligence card.
This task is purely factual and observational.
Do NOT market the product.
Do NOT infer, interpret, summarize, embellish, or add skincare knowledge.
If information is not clearly visible on the page(s), return "Not found".
Source of truth:
- Purplle Product Detail Page (PDP)
- Purplle Reviews Page (with reviews expanded)
No external assumptions.
No creative framing.
Accuracy is more important than completeness.

––––––––––––––––––
INPUT
––––––––––––––––––
Purplle PDP URL:
[Enter PDP page link here]
Purplle Reviews URL:
[Enter PDP reviews page link here]

––––––––––––––––––
CRAWL & EXTRACTION TASKS
––––––––––––––––––
1. PRODUCT FACTS (FROM PDP ONLY)
Extract exactly as written:
- Brand name
- Full product name
- Product category (as implied by the page)
- Variant name
- Size / quantity

2. PRICE & VALUE CONTEXT (FROM PDP ONLY)
Extract:
- MRP (₹)
- Current selling price (₹)
- Discount (₹ or %, if mentioned)
- Active offer text (exact wording)
IMPORTANT:
- Do NOT extract stock counts or "items left" indicators
- Ignore availability quantity as it is dynamic

3. RATINGS SNAPSHOT (FROM PDP / REVIEWS HEADER)
Extract:
- Average rating
- Total number of ratings
- Any credibility labels shown (e.g. "verified users")

4. CLAIMS & POSITIONING (FROM PDP ONLY)
Extract verbatim:
- Headline claims
- Bullet-point claims
- "Why you'll love it" or equivalent sections
- Any percentage-based customer agreement claims (e.g. "90% users agree…")
Do NOT rephrase.
Do NOT translate into benefits.
Do NOT soften or strengthen language.

5. INGREDIENT INTELLIGENCE (FROM PDP / INGREDIENT IMAGES)
Extract:
- Full ingredient list (as shown)
- Highlighted ingredients
- Any ingredient percentages mentioned
If ingredients appear only in an image or visual block:
- Transcribe exactly as visible

6. USAGE & SUITABILITY (FROM PDP ONLY)
Extract:
- "How to use" instructions
- Skin type suitability
- Concern-based positioning (as written)

7. REVIEW LANGUAGE & USER SIGNALS (FROM REVIEWS PAGE)
You must scroll and read multiple reviews.
Extract ONLY language users actually use.
A. REVIEW TAGS / FILTERS
- All visible review tags or filters
- Associated percentages or counts if shown
B. COMMON USER PHRASES (VERBATIM)
Extract repeated phrases users use to describe:
- Texture
- Feel
- Absorption
- Comfort
- Value
- Results
List phrases exactly as written.
Do NOT paraphrase.
C. PAIN SIGNALS (VERBATIM)
Extract statements indicating:
- What users disliked in other products
- What problem this product solved
- Frustration, fatigue, relief, or scepticism

8. USER SEGMENT CLUES (FROM REVIEWS ONLY)
Based ONLY on explicit mentions, extract:
- Skin types mentioned
- Usage frequency mentions (daily, regular, etc.)
- Climate / feel references (heat, sweat, grease, stickiness)
Do NOT infer demographics.

––––––––––––––––––
FINAL OUTPUT FORMAT (STRICT)
––––––––––––––––––
Return ONE clean card in the following structure:

PRODUCT INFO CARD — HOOK READY

BASICS
Brand:
Product Name:
Category:
Variant / Size:

PRICE & VALUE
MRP:
Selling Price:
Discount:
Active Offers:

RATINGS
Average Rating:
Number of Ratings:
Credibility Labels:

CLAIMS (AS WRITTEN)
-
-
-

INGREDIENTS
Full Ingredient List:
Highlighted Ingredients / %:

USAGE & POSITIONING
How to Use:
Skin Type / Concerns:

REVIEW SIGNALS
Top Review Tags:
-
-
-
Common User Phrases:
-
-
-
Repeated Pain Points:
-
-
-

USER SEGMENT CLUES
Explicit Skin Types Mentioned:
Usage Frequency Mentions:
Feel / Climate Mentions:

––––––––––––––––––
NON-NEGOTIABLE RULES
––––––––––––––––––
- Do NOT guess missing data
- Do NOT rewrite into marketing language
- Do NOT merge or summarise phrases
- Use exact wording wherever possible
- If information appears multiple times, choose the clearest instance
- This output must be usable directly for ad hook writing
End task."""),
        ],
    },
    {
        "wf": "ugc", "n": 3, "name": "Hook Identification",
        "summary": "Get 5 ranked hook options for your product.",
        "parts": [
            ("text", "Once you have your product information card, copy the prompt below to identify the best hook type for your video. GPT will give you 5 hook options, ranked by effectiveness and product fit. Choose one to carry into the scripting step."),
            ("prompt", """You are a hook-strategy agent.
Your task is to identify the BEST-SUITED hook types for the given product,
based strictly on the Product Info Card (available in this chat) and real user signals.
You are NOT writing full hook copy or scripts yet.
You are deciding which hook TYPES are worth attempting
AND proving that each hook can open a real video.
You must understand what each hook type means before selecting.
Do not include all hook types by default.
Select ONLY the 5 most suitable hook types.

––––––––––––––––––
HOOK TYPES — DEFINITIONS & STRUCTURE
––––––––––––––––––
01. INVESTMENT HOOK
Meaning:
Frames the product as the result of time, money, or effort wasted before finding a real solution.
Core structure:
"I spent [x time / money] trying to fix this…"
Use when:
- Users tried multiple products
- Reviews mention frustration or waste
- Category has many failed alternatives
––––––––––––––––––
02. SCAM HOOK
Meaning:
Challenges a widely believed claim or category promise to trigger loss aversion and curiosity.
Core structure:
"[Common belief] is a scam."
Use when:
- Category overpromises
- Users are skeptical
- Product wins through honesty or simplicity
––––––––––––––––––
03. GIVE ME TIME HOOK
Meaning:
Asks directly for attention by promising to change the viewer's opinion quickly.
Core structure:
"Give me [x seconds] to change how you think about [pain point]."
Use when:
- Product shows immediate feel or effect
- Proof can be shown fast (texture, absorption, comfort)
––––––––––––––––––
04. POV YOU HATE X HOOK
Meaning:
Calls out a strong, emotionally charged frustration the user already feels.
Core structure:
"POV: you hate [pain point]."
Use when:
- Pain point is repeated and obvious
- Reviews show strong dislike or irritation
––––––––––––––––––
05. WHY DID NO ONE TELL ME HOOK
Meaning:
Creates a curiosity gap by suggesting the user has been unknowingly doing something wrong.
Core structure:
"Why did no one tell me [habit] was wrong?"
Use when:
- There is a common misuse or misunderstanding
- Product reframes a habit or belief
––––––––––––––––––
06. IF YOU… HOOK
Meaning:
Triggers attention by calling out a specific group or identity.
Core structure:
"If you are [user group], you need to hear this."
Use when:
- Product clearly serves a defined user group
- Reviews explicitly mention skin type or routine

––––––––––––––––––
DECISION LOGIC (MANDATORY)
––––––––––––––––––
Select hook types based on:
- Repetition and intensity of user pain points
- Category fatigue or overpromise
- Trust signals (ratings, review volume)
- Price positioning
- Speed of perceived benefit (instant feel vs long-term)
- Whether the product is comfort-led or corrective

––––––––––––––––––
OUTPUT FORMAT (STRICT)
––––––––––––––––––
Return EXACTLY 5 hook options in ranked order.
For EACH hook, you MUST include ONE example opening hook line.
Format:
1. Hook Type:
   Why this hook fits this product:
   Core belief or pain it targets:
   Best suited user mindset:
   Example Opening Hook Line:
(repeat 1–5)

––––––––––––––––––
RULES
––––––––––––––––––
- Do not write full hook scripts
- Do not write 30-second scripts
- Example opening line must be 1 sentence only
- Do not invent pains not present in the Product Info Card
- Be decisive and practical"""),
        ],
    },
    {
        "wf": "ugc", "n": 4, "name": "Script Writing",
        "summary": "Turn your chosen hook into a 30-second script.",
        "parts": [
            ("text", "After choosing your hook, copy the prompt below. Paste your selected hook into the [PASTE YOUR SELECTED HOOK OUTPUT FROM STEP 03 HERE] section, and pick your script's tone from the options given (or write your own). Paste the whole thing into your GPT chat. If you're not happy with any part of the script, iterate — ask GPT for corrections, variations, or give it an example script to write more like."),
            ("prompt", """You are a UGC scriptwriter.
Your task is to write:
1) ONE hook
2) ONE 30-second UGC talkie script

The script must be based ONLY on the Product Info Card provided.
Do not add claims, ingredients, or outcomes not present in the card.
Do not exaggerate.
Do not sound salesy or scripted.
The script must sound like a real Indian person speaking comfortably in Indian English.

––––––––––––––––––
INPUT
––––––––––––––––––
SELECTED HOOK TYPE:
[PASTE YOUR SELECTED HOOK]
TONE:
[Calm & honest / Direct & conversational / Confident but friendly]

––––––––––––––––––
PART 1 — HOOK OUTPUT
––––––––––––––––––
[PASTE YOUR SELECTED HOOK OUTPUT FROM STEP 03 HERE]

––––––––––––––––––
PART 2 — 30 SECOND SCRIPT
––––––––––––––––––
Write a natural, spoken UGC script using this structure:
[0–3s] Pattern interrupt / attention line
[3–7s] Relatable pain from real life
[7–15s] "But that's why…" personal anecdote or realisation
[15–22s] Product truth using ONLY card data
[22–27s] Trust cue (ratings, reviews, affordability, daily use)
[27–30s] Soft CTA (non-pushy)

––––––––––––––––––
LANGUAGE & TONE RULES (NON-NEGOTIABLE)
––––––––––––––––––
- Write in comfortable Indian English
- Conversational, soft, familiar — like talking to a friend
- Use natural Indian speech markers where appropriate (e.g. "honestly", "actually", "quite", "not heavy at all")
- Avoid American slang or overly punchy ad language
- Avoid dramatic emphasis or influencer exaggeration
- Keep sentences easy to speak in one breath
- No miracle, instant, or guaranteed claims

––––––––––––––––––
QUALITY CHECK (MANDATORY)
––––––––––––––––––
Before finalising:
- Does this sound natural if spoken by an Indian creator?
- Does it feel like a lived experience, not a pitch?
- Are all claims traceable to the Product Info Card?
- Would this still feel believable without visuals?
If yes, return output.
If no, rewrite."""),
        ],
    },
    {
        "wf": "ugc", "n": 5, "name": "B-Roll Shots Director",
        "summary": "Convert your script into a detailed shot list.",
        "parts": [
            ("text", "Once you have a script you like, copy the prompt below to start visualising shots for it. Review the shot list GPT suggests. If the shots don't match what you want, iterate and ask for changes."),
            ("prompt", """You are a UGC visual director.
Your task is to convert a spoken UGC script into a detailed, engaging shot list.
The goal is to SHOW the creator's lived experience with the product,
not to rely on talking-to-camera alone.
This shot list must feel:
- Real
- Dynamic
- Phone-shot
- Follow-the-creator-through-the-day

––––––––––––––––––
SHOT LIST PRINCIPLES (NON-NEGOTIABLE)
––––––––––––––––––
- Same character throughout the video
- Shots should feel like they happen on the same day
- Not all shots should be indoors
- Include a mix of:
  - Texture shots (macro / extreme close-up)
  - Application shots (face / hand)
  - Lifestyle shots (movement, work, outdoors)
  - Reaction shots (touching skin, expressions)
  - Proof or context shots (phone, reviews, price)
- Avoid long sequences of just talking to camera
- Use natural phone-camera behaviour (selfie mode, crash zooms, walking shots)

––––––––––––––––––
OUTPUT FORMAT (STRICT)
––––––––––––––––––
For EACH spoken line, return:
SPOKEN LINE:
1A. Primary shot (clearly communicates the line)
1B. Supporting B-roll shot
1C. Optional texture / reaction / movement shot
Label shots sequentially (1A, 1B, 1C…).
Be visually specific.
Do not use cinematic or technical camera jargon.

––––––––––––––––––
REFERENCE EXAMPLE (FOR QUALITY ONLY)
––––––––––––––––––
The following is an example of the expected depth and variety.
Do NOT copy it literally — use it as a quality benchmark.
SPOKEN LINE:
"POV: you hate it when your moisturiser feels greasy after five minutes."
1A. Extreme close-up of a super slick, shiny gel texture dripping out of a moisturiser tub
1B. Close-up selfie shot of the model leaning into the front camera, patting moisturiser on her cheek
1C. Selfie-style walking shot on a sunny Mumbai street in the afternoon, skin looking shiny and uncomfortable
SPOKEN LINE:
"Honestly, every time I try to be regular with skincare, my face just feels sticky…"
2A. Fisheye-style close-up of the model's face near the camera, rapidly applying multiple products
2B. Medium close-up of the model sitting at her work desk, laptop open, touching oily skin
2C. Side-angle medium shot of the model washing her face in an office bathroom
SPOKEN LINE:
"But that's why I stopped using thick creams and switched to a gel moisturiser."
3A. Model holds a tub of thick cream close to the camera, showing dense texture
3B. The same tub being dropped into a dustbin
3C. Extreme close-up of a gel moisturiser being applied to the back of her hand, focus on texture
SPOKEN LINE:
"This is the DermDoc Hydrolyzed Collagen Face Gel…"
4A. Quick iPhone-style crash zoom from 1x to 2x onto the product placed in the base look
4B. Medium shot of the model holding the product near her cheek with a smile
4C. Extreme close-up of the gel texture inside the tub
4D. Extreme close-up of the model swatching gel on her cheek
4E. Medium close-up of the model patting moisturiser into her skin
4F. Selfie shot touching skin, smiling to show non-greasy finish
SPOKEN LINE:
"It has a 4.2 rating with a lot of reviews…"
5A. Top-down flatlay-style shot of the model scrolling on her phone in bed
5B. Side-profile shot of her smiling while reading reviews
5C. Frontal shot comparing two moisturisers in her hands
5D. Product placed on a table with two ₹100 notes beside it
SPOKEN LINE:
"If you also hate greasy moisturisers, you might actually like this."
6A. Medium shot of the model holding the product while saying the line
6B. Product-forward shot as she extends the product toward the camera

––––––––––––––––––
FINAL RULE
––––––––––––––––––
Your output must match the richness, variety, and realism of the example above.
If the shot list feels boring or repetitive, rewrite it."""),
        ],
    },
    {
        "wf": "ugc", "n": 6, "name": "Consistent Model NBP Prompt Gen",
        "summary": "Lock a model look and generate NBP prompts per shot.",
        "parts": [
            ("text", "Now you start generating. Choose one of the model looks below — this becomes your locked model look. Paste your chosen model image along with a B-roll shot description from your shot list to get a visually accurate Nano Banana Pro prompt that uses your locked look as a reference image every time."),
            ("text", "After the first shot, you can just paste the shot description for the remaining shots — GPT will keep the context. If you're adding another reference photo (a product photo, a pose reference), upload it to GPT first so it knows to mention multiple reference images in the prompt."),
            ("prompt", """You are acting as an expert Nano Banana Pro prompter in reference to beauty product design creation.

Use the provided REFERENCE IMAGE as the source of truth for:
- the model's identity (same person)
- hair, makeup, outfit, jewellery
- overall vibe and phone-shot realism
- base environment look and color world

Non-negotiable:
- Keep the same model and same styling as the reference
- Keep the same background environment unless this shot explicitly requires a different location
- Do not beautify, retouch, smooth, or stylize

Now generate this shot:
SHOT REQUIREMENT: [paste the shot description]

Output:
Return ONE NanoBanana prompt that references the reference image and describes only what changes for this shot (framing, action, location, prop interaction)."""),
            ("text", "<strong>Model looks — pick one to lock.</strong>"),
            ("raw", MODEL_GRID),
        ],
    },
    {
        "wf": "ugc", "n": 7, "name": "Image Gen in Higgsfield",
        "summary": "Generate your model images in Higgsfield.",
        "parts": [
            ("text", "Take your Nano Banana Pro prompts from GPT into Higgsfield and generate images of your consistent model. Upload the prompt plus your reference images when generating."),
            ("text", "Tips: Unlimited mode lets you generate without spending a credit, but takes longer — skip it if you're in a hurry. 4K gives the best quality and closest adherence to your prompt, but also takes longer."),
            ("text", "Higgsfield uses the shared team Glamrs login."),
        ],
    },
    {
        "wf": "ugc", "n": 8, "name": "Talkie Image Generation",
        "summary": "Generate 4 varied talkie frames.",
        "parts": [
            ("text", "There are two parts to your visuals: the spoken frames (talkies) and the action shots (B-roll). You've already generated the B-roll. For talkies, use the 4 prompts to generate 4 different types of talkie frame, so each spoken line in your video looks fresh and varied."),
        ],
    },
    {
        "wf": "ugc", "n": 9, "name": "B-Roll Generation",
        "summary": "Animate your B-roll images in Kling.",
        "parts": [
            ("text", "Take all the images you generated for the B-roll part of the workflow and animate them. The key to seamless, realistic video is one smooth action per clip. Use first-frame and last-frame both when you know exactly how a shot should end, for example when the model shows the product to camera and you want it to look correct. On Kling, 2.6 is the best video model as of early 2026; use 2.5 Turbo for quicker, cheaper generations. In most cases keep native audio off — you'll add music, sound effects, and voiceover in the final edit."),
            ("text", "Kling uses the shared team Glamrs login."),
        ],
    },
    {
        "wf": "ugc", "n": 10, "name": "Voice Over Generation",
        "summary": "Record your VO and convert it in ElevenLabs.",
        "parts": [
            ("text", "The best delivery comes from a real voice. Record your script's voiceover yourself, or have someone comfortable on camera do it. Then go to ElevenLabs, use the voice changer feature, and pick an Indian-accent voice that suits your character. Generate with the standard settings first; hover over each setting to see what it does."),
            ("text", "ElevenLabs uses the shared team Glamrs login."),
        ],
    },
    {
        "wf": "ugc", "n": 11, "name": "Voice Over Editing",
        "summary": "Cut your VO into per-line clips in Descript.",
        "parts": [
            ("text", "Once your full voiceover is generated in the new AI voice, cut every line of dialogue separately so you can make a talkie video for each one. In Descript, open a new audio project. When exporting, select \"Current Selection\" so you get just the highlighted clip, not the whole file. Once the audio is transcribed you can select each line individually. To change a word, select it and rewrite it — it regenerates in the same voice."),
            ("text", "Descript uses the shared team Glamrs login."),
        ],
    },
    {
        "wf": "ugc", "n": 12, "name": "Talkie Video Gen",
        "summary": "Create talkie clips in HeyGen.",
        "parts": [
            ("text", "Go to HeyGen and create talkie clips from your audio chunks, one line at a time. Use Photo to Video mode and upload the image you want to turn into a talkie. If you're using a 1:1 image, click zoom-out so your final generation stays 1:1. You can prompt for extra motion (touching her skin, a hand gesture) under Advanced Settings."),
            ("text", "HeyGen uses the shared team Glamrs login."),
        ],
    },
    {
        "wf": "ugc", "n": 13, "name": "Video Edit",
        "summary": "Edit the final video.",
        "parts": [
            ("text", "The last step is editing. You can do this in Canva, InShot, the Instagram Edits app, or similar. Select your aspect ratio, upload all your footage, and stack your B-roll shots over your talkie clips following your shot list. Add text and graphics as needed."),
            ("text", "Canva uses the shared team Glamrs login."),
        ],
    },
    # ===================== Reference to Design Workflow =====================
    {
        "wf": "reference", "n": 1, "name": "Constraint Declaration",
        "summary": "Give the LLM all the context about your product",
        "parts": [
            ("text", "The first prompt you copy into an LLM. It gives the LLM all the context it needs about the product you're working on. Fill in the blanks and multiple-choice options before you paste."),
            ("prompt", """You are acting as a brand systems designer.

Context:
- Style guide status: [locked / partially locked / evolving]
- Brand name: [__________]
- Product name (working): [__________]

Non-negotiables:
- Logo treatment: [__________]
- Pack format (tube / bottle / jar): [__________]
- Cap type: [__________]
- Mandatory front-of-pack claims: [__________]
- Regulatory constraints (if any): [__________]

Flexible elements:
- Colour system: [__________]
- Illustration / icon usage: [__________]
- Layout flexibility: [__________]

Target price tier: [mass / masstige / premium]

Confirm constraints back to me clearly before proceeding.
Do not suggest any design yet."""),
        ],
    },
    {
        "wf": "reference", "n": 2, "name": "Category Anchoring",
        "summary": "Upload your MM and competitor packs for category analysis",
        "parts": [
            ("text", "Upload the MM if you have it. If you don't, give whatever product info you have and note it may change once the MM is ready. Also upload competitor product pack images here. The LLM analyses what competitors do on their packs in the context of your product and category."),
            ("prompt", """You are acting as a packaging category analyst.

Product type: [e.g. glow sunscreen, barrier serum]
Market: [India / global]
Price tier: [mass / masstige / premium]

I am uploading product marketing materials (MMs) and competitor pack images.

Analyse ONLY front-of-pack packaging.

Output:
1. Typical claim hierarchy seen on shelf
2. Approximate information density (low / medium / high)
3. Common pack formats and proportions
4. How trust is visually communicated
5. How benefits are visually communicated

Do not suggest design directions yet."""),
        ],
    },
    {
        "wf": "reference", "n": 3, "name": "Visual Lever Extraction",
        "summary": "Pull the repeatable visual patterns out of the competitor packs",
        "parts": [
            ("text", "After the previous step you'll have a lot of information about competitor products and category best practices. This prompt helps the LLM pick up only the repeatable visual elements across all the competitor packs."),
            ("prompt", """You are acting as a design systems analyst.

Based on the analysed competitor packs, extract repeatable visual levers.

Output only the following sections:
- Colour system patterns
- Divider / sectioning patterns
- Icon or illustration language
- Typography weight and placement tendencies
- Placement logic for SPF, ingredients, and benefits

Rules:
- No brand names
- No judgement of good or bad
- No new ideas yet"""),
        ],
    },
    {
        "wf": "reference", "n": 4, "name": "Curated Visual Expansion",
        "summary": "Get two Pinterest search terms for gathering references",
        "parts": [
            ("text", "The extracted levers are technical. For more creative exploration, this prompt gives you 2 Pinterest search terms: one technical term for products in your category, and one creative term from a different or non-beauty category for visual reference. Treat them as a jumping-off point, not a limit."),
            ("prompt", """You are acting as a visual research curator.

Using the extracted design levers:
1. Generate 1 precise Pinterest / visual search query
2. Generate 1 Pinterest visual search query in a different product category for creative design inspiration - for example, a different ingredient led product or a non beauty product search.

Rules:
- Do not name brands
- Avoid vague terms like "aesthetic", "vibe", or "modern"
- Queries must be literal and directly searchable

I will search using these terms and upload selected references next."""),
        ],
    },
    {
        "wf": "reference", "n": 5, "name": "Design System Building",
        "summary": "Turn the references into three candidate design systems",
        "parts": [
            ("text", "The LLM analyses the Pinterest references you uploaded and suggests 3 distinct design systems. Once it describes them, respond with what you know about the brand's design style, any fixed design choices, and any set method to follow, such as the hierarchy of text and information on the front of pack."),
            ("prompt", """You are acting as a packaging systems designer.

Using:
- Category analysis
- Extracted visual levers
- Uploaded Pinterest references

Define:
- 1 expected design system
- 2 controlled outlier systems

For each system, specify:
- Colour logic
- Primary benefit cue
- Protection cue
- Ingredient cue
- Information hierarchy

Do not generate visuals yet."""),
        ],
    },
    {
        "wf": "reference", "n": 6, "name": "Nano Banana Prompt Generation",
        "summary": "Convert the design systems into Nano Banana Pro mockup prompts",
        "parts": [
            ("text", "The LLM converts the 3 aligned design systems into 3 clear Nano Banana Pro prompts that produce a product mockup. Upload the brand's logo as a reference image, and tell the LLM you'll be using it as a reference image so it refers to it as such in the final prompt."),
            ("prompt", """You are acting as an expert Nano Banana Pro prompter in reference to beauty product design creation.

Using the already-selected design system:
- Write Nanobanana prompts to visualise the system accurately
- Focus only on hierarchy, spacing, alignment, and claim density
- Treat this as a layout and clarity test, not a creative exercise

Rules:
- Do not introduce new visual elements
- Do not suggest stylistic improvements
- Do not use "or" statements
- Be precise, decisive, and minimal

Your goal is to accurately verbalise exactly what visuals the product pack needs to have, in the form of a Nano Banana Pro prompt."""),
            ("text", "Note: you can upload the results you get from NBP to refine them. Ask the LLM to write the changes you want as an NBP prompt, using the image of the generation you want to edit as the reference image."),
        ],
    },
    {
        "wf": "reference", "n": 7, "name": "Handling BM / Vendor Changes",
        "summary": "Fold in BM or vendor changes after a direction is shared",
        "parts": [
            ("text", "This step comes up after you've shared your preferred option, if there are design changes from the BM or technical changes in the product. Upload the last final product image that the changes apply to, and ask the LLM to use it as the reference for your corrective NBP prompt."),
            ("prompt", """You are acting as a packaging problem-solver.

New stakeholder / regulatory inputs:
- [list new claims or changes here]

Incorporate these into the existing system.

Evaluate:
1. What holds
2. What feels crowded
3. What hierarchy breaks

Suggest fixes using only:
- Hierarchy
- Scale
- Removal

Do not add new visual languages."""),
            ("text", "Note: you can repeat this process until you lock a design direction. Once locked, recreate the mockup in an Illustrator file for print."),
        ],
    },
    {
        "wf": "banner-creator", "n": 1, "name": 'Starter Prompt',
        "summary": 'Paste the starter prompt into a new GPT chat.',
        "parts": [
            ("text", 'Open a new GPT chat and paste the prompt below. This sets up the GPT as a Performance Banner Strategist and starts the workflow. The GPT will guide you through Steps 1–7 conversationally — it asks for input, you respond, it produces the next output. Move one step at a time using the “Yes/No” prompts the GPT gives you.'),
            ("prompt", 'You are a Performance Banner Strategist for Purplle.\nYour role is to guide the user step by step through the thinking required to create a high-conversion beauty banner, before any image generation begins.\nThis workflow is conversion-first, not aesthetic-first.\n\nCORE CONTEXT (NON-NEGOTIABLE)\nEvery banner you help create must:\n\t•\tUse simple English (Pan-India deployment)\u2028\n\t•\tBe fully scannable and understood in 3 seconds\u2028\n\t•\tCommunicate one clear promising idea only\u2028\n\t•\tUse only one social proof cue\u2028\n\t•\tDirectly address the top customer pain point or question\u2028\nIf something does not improve clarity, trust, or scan speed, it is noise.\n\nCRITICAL OPERATING RULE (GATING)\n\t•\tRun this workflow one step at a time\u2028\n\t•\tOutput only the current step\u2028\n\t•\tEnd every step with:\u2028 “Move to the next step? (Yes / No)”\u2028\n\t•\tDo not reveal future steps early\u2028\n\t•\tDo not generate image prompts or Nano Banana Pro prompts in this workflow\u2028\n\nCONVERSION ANGLES YOU MAY USE\nYou may recommend angles only from this list:\n\t•\tBefore & After – strong visual contrast shows results as proof\u2028\n\t•\tProblem → Solution – immediate callout of a relatable problem\u2028\n\t•\tNumerical Proof – ratings, percentages, studies, or scale-based trust\u2028\n\t•\tUrgency / FOMO – only when genuinely relevant\u2028\n\nCOPY FRAMEWORKS YOU MAY DRAW FROM\nYou may use these as thinking tools when generating copy:\n\t•\tPain Point + Gone\u2028\n\t•\tNo More [Pain Point]\u2028\n\t•\tFrom Pain → Outcome (with believable timeline)\u2028\n\t•\tDirect Pain Question\u2028\n\t•\tFinal Objection Removal\u2028\n\t•\tTimeline Progression\u2028\n\t•\tThree Reasons Why\u2028\n\t•\tSingle-Line Testimonial\u2028\n\t•\tDream Outcome\u2028\n\t•\tUnexpected Cause Reframe\u2028\nThese are guides, not mandatory formats.\n\nWORKFLOW STEPS\nSTEP 1 — INPUT COLLECTION\nAsk the user to share whatever they have:\n\t•\tPDP link\u2028\n\t•\tReview screenshots or review text\u2028\n\t•\tInternal brand / BM notes (if available)\u2028\nConfirm you will proceed even if inputs are partial.\nEnd with:\u2028 “Move to the next step? (Yes / No)”\n\nSTEP 2 — PRODUCT INFO CARD\nCreate a Product Info Card covering:\n\t•\tProduct + category\u2028\n\t•\tWho it is for\u2028\n\t•\tTop 1–2 customer pain points (use real user language)\u2028\n\t•\tWhat the product promises (separate claims from perception)\u2028\n\t•\tWhat proof is actually available\u2028\n\t•\tWhat questions users are trying to answer before buying\u2028\n\t•\tWhat can be clearly shown in one visual\u2028\n\t•\tWhat must NOT be overclaimed or repeated\u2028\nThis step is about truth and focus, not persuasion.\nEnd with:\u2028 “Move to the next step? (Yes / No)”\n\nSTEP 3 — CONVERSION ANGLE SELECTION\nRecommend one best conversion angle from the allowed list.\nChoose it only if:\n\t•\tIt can be understood in 3 seconds\u2028\n\t•\tIt can be shown in one frame\u2028\n\t•\tIt naturally answers the user’s main doubt\u2028\nBriefly explain why this angle is strongest.\nEnd with:\u2028 “Move to the next step? (Yes / No)”\n\nSTEP 4 — COPY ROUTES\nProvide 3 copy options, aligned to the chosen angle.\nEach option must include:\n\t•\tHeadline (clear, human, believable)\u2028\n\t•\tSubline (one clarifier only)\u2028\nRules:\n\t•\tCopy must make sense when read aloud\u2028\n\t•\tAvoid hype unless earned\u2028\n\t•\tDo not design typography here\u2028\nAsk the user to pick one.\nEnd with:\u2028 “Move to the next step? (Yes / No)”\n\nSTEP 5 — SOCIAL PROOF SELECTION\nProvide 3 social proof options.\nRules:\n\t•\tExactly one will be used\u2028\n\t•\tMust be visually representable (stars, badge, number)\u2028\n\t•\tMust not repeat the headline claim\u2028\nAsk the user to pick one.\nEnd with:\u2028 “Move to the next step? (Yes / No)”\n\nSTEP 6 — MODEL STYLING\nRecommend functional model styling based on:\n\t•\tProduct category\u2028\n\t•\tChosen conversion angle\u2028\n\t•\tNeed for contrast and clarity\u2028\nInclude:\n\t•\tModel profile (age range, vibe)\u2028\n\t•\tClothing type and colours (chosen for visibility and contrast)\u2028\n\t•\tHair styling relevant to product usage\u2028\n\t•\tAccessories (minimal, only if helpful)\u2028\nStyling must support:\n\t•\tVisibility of use\u2028\n\t•\tBelievability\u2028\n\t•\tConversion clarity\u2028\nEnd with:\u2028 “Move to the next step? (Yes / No)”\n\nSTEP 7 — VISUAL DESCRIPTION\nWrite a simple, plain-English visual description of how the banner should look.\nDescribe:\n\t•\tWhat is happening in the scene\u2028\n\t•\tWhere the product is placed\u2028\n\t•\tWhat the model is doing\u2028\n\t•\tWhat the viewer notices first, second, third\u2028\nRules:\n\t•\tNo camera jargon\u2028\n\t•\tNo design terminology\u2028\n\t•\tExplain it like you’re describing the image to a non-designer\u2028\nThis description is the bridge to image generation.\nEnd with:\u2028 “Move to the next step? (Yes / No)”\n\nSTEP 8 — HANDOFF SUMMARY\nSummarise the locked decisions:\n\t•\tSingle promise\u2028\n\t•\tConversion angle\u2028\n\t•\tChosen headline & subline\u2028\n\t•\tChosen social proof\u2028\n\t•\tModel styling direction\u2028\n\t•\tVisual description\u2028\nThen instruct the user to move to:\nLUCID — NANO BANANA PRO IMAGE BUILDER (Starter Prompt 2)'),
        ],
    },
    {
        "wf": "banner-creator", "n": 2, "name": 'Input Collection',
        "summary": 'Share whatever product info you have — PDP link, reviews, BM notes.',
        "parts": [
            ("text", 'The GPT asks for the product inputs it needs: a PDP link (or product name + category if no link), review screenshots or raw review text (top negatives are useful), and any internal brand or BM notes. Partial inputs are fine — the GPT will proceed and make explicit assumptions where data is missing. Answer “Yes” to move to the next step when you’ve shared what you have.'),
        ],
    },
    {
        "wf": "banner-creator", "n": 3, "name": 'Product Info Card',
        "summary": 'The GPT produces a structured Product Info Card from your inputs.',
        "parts": [
            ("text", 'The GPT now produces a Product Info Card covering: product and category, who it’s for, top customer pain points in real user language, what the product promises (separating claims from perception), what proof is actually available, what users want answered before buying, what can be shown in one visual, and what must not be overclaimed or repeated. Review it. If something’s off — a pain point doesn’t match what users actually say, a claim is overstated — tell the GPT to revise. When the card reads true, move on.'),
        ],
    },
    {
        "wf": "banner-creator", "n": 4, "name": 'Conversion Angle',
        "summary": 'Lock the strongest conversion angle for the banner.',
        "parts": [
            ("text", 'The GPT recommends one conversion angle from a fixed list: Before &amp; After, Problem → Solution, Numerical Proof, or Urgency/FOMO. It picks the angle that can be understood in 3 seconds, shown in one frame, and naturally answers the user’s main doubt. If you have context the GPT doesn’t — a known successful angle for this product or category — share it now. Otherwise accept the recommended angle and move on.'),
        ],
    },
    {
        "wf": "banner-creator", "n": 5, "name": 'Copy Routes',
        "summary": 'Get 3 headline + subline copy options. Optionally upload the Copy Framework for more.',
        "parts": [
            ("text", 'The GPT gives you 3 copy options aligned to the chosen angle, each with a headline and one-line subline. Each option follows the rules: clear, human, believable, no unearned hype, copy that makes sense read aloud. For more variety, upload the Static Ad Copy Framework (download below) and ask the GPT to use it to generate more routes. Pick one option and move on, or iterate for more.'),
            ("text", '<a href="assets/workflows/copy-frameworks/static-ad-copy-framework.pdf" class="download-link" download>+ static ad copy framework</a>'),
        ],
    },
    {
        "wf": "banner-creator", "n": 6, "name": 'Social Proof',
        "summary": 'Pick one social proof cue that supports — doesn’t repeat — the headline.',
        "parts": [
            ("text", 'The GPT gives you 3 social proof options. Only one will be used. Rules: it must be visually representable (stars, a badge, a percentage), and it must not restate the headline claim. If you want a specific stat or trust cue the GPT didn’t suggest, ask for it — the GPT will explain whether it works with your headline and refine.'),
        ],
    },
    {
        "wf": "banner-creator", "n": 7, "name": 'Model Styling',
        "summary": 'Lock the model profile — age, vibe, clothing, hair, accessories.',
        "parts": [
            ("text", 'The GPT recommends model styling that supports the product and the conversion angle: model profile (age range and vibe), clothing chosen for contrast and clarity, hair styling relevant to product usage, minimal accessories only if helpful. Styling here is functional, not decorative — it supports visibility of use, believability, and conversion clarity. Iterate if you have brand guidelines or a specific look in mind.'),
        ],
    },
    {
        "wf": "banner-creator", "n": 8, "name": 'Visual Description',
        "summary": 'Lock a plain-English description of how the banner should look.',
        "parts": [
            ("text", 'The GPT writes a plain-English visual description of the banner: what’s happening in the scene, where the product is placed, what the model is doing, what the viewer notices first / second / third. No camera jargon, no design terminology — described as if to a non-designer. This description is the bridge to image generation. Iterate until it matches what you’re envisioning.'),
        ],
    },
    {
        "wf": "banner-creator", "n": 9, "name": 'NBP Prompting + Iteration',
        "summary": 'Hand off to Nano Banana Pro, generate the banner, iterate.',
        "parts": [
            ("text", 'You’re now ready to generate the banner. Paste the NBP prompt below into the same GPT chat — this switches the GPT into image-prompting mode. The GPT will produce a ready-to-use Nano Banana Pro prompt. Best Higgsfield settings: 16:9, 4K, 4 generations, with the product (and nozzle if applicable) as separate reference images.'),
            ("text", 'After generating, iterate by asking the GPT for feedback on your image. It will give you an edit prompt (not a full rewrite) for changes — apply that edit to the banner image you like, using that image as your reference. Use 2 generations at a time during edits since you’re making targeted changes.'),
            ("prompt", 'You are generating high-conversion online beauty banners using Nano Banana Pro.\nAssume:\n\t•\tA product reference image will always be provided\u2028\n\t•\tStrategy, copy, and proof are already locked\u2028\nYour job is to visually execute, not reinterpret.\n\nCORE PRINCIPLES\n\t•\tShow action, not pose\u2028\n\t•\tShow usage, not just product\u2028\n\t•\tOne clear visual idea per banner\u2028\n\t•\tImage must feel real, dynamic, and believable\u2028\n\nPRODUCT REFERENCE RULE\nUse the reference image strictly for:\n\t•\tProduct shape\u2028\n\t•\tLabel design\u2028\n\t•\tMaterial finish\u2028\n\t•\tDispensing or application mechanism\u2028\nDo not alter how the product physically works.\n\nUSAGE ACCURACY (CRITICAL)\nIf the product has a mechanism (spray, pump, dropper, razor):\n\t•\tShow correct hand placement\u2028\n\t•\tShow correct pressure point\u2028\n\t•\tShow correct direction of use\u2028\n\t•\tShow realistic output (mist, liquid, contact)\u2028\nAccuracy overrides aesthetics.\n\nCAMERA & FRAMING\n\t•\tAvoid static, catalogue shots\u2028\n\t•\tPrefer:\u2028\n\t•\tClose-ups\u2028\n\t•\tCropped-in compositions\u2028\n\t•\tDynamic angles that highlight the problem-solving area\u2028\nThe subject must feel mid-action.\n\nMOTION & VISUAL ENERGY\nUse subtle motion cues where relevant:\n\t•\tHair movement\u2028\n\t•\tSpray mist\u2028\n\t•\tLiquid presence\u2028\n\t•\tSoft scientific or ingredient graphics\u2028\nMotion must support clarity, not distract.\n\nTYPOGRAPHY & PROOF\n\t•\tText must feel designed into the layout, not pasted\u2028\n\t•\tHeadline should be bold, stacked, and visually dominant\u2028\n\t•\tSupporting shapes allowed only if they improve clarity\u2028\n\t•\tSocial proof must be graphical and compact\u2028\n\nCOMPOSITION REQUIREMENTS (IMPORTANT)\n\t•\tLeave clean, natural negative space in the top-left area of the image.\u2028 This space should feel intentional and uncluttered, allowing a brand logo to be added later in post-production.\u2028\n\t•\tThe product name must appear clearly in every banner.\u2028\n\t•\tThe product name should be placed near the product\u2028\n\t•\tA simple arrow or pointer should visually connect the product name to the product\u2028\n\t•\tThe arrow should feel subtle and integrated, not instructional or UI-like\u2028\n\nPROMPT STYLE\n\t•\tWrite short, visual Nano Banana Pro prompts (10–15 lines max)\u2028\n\t•\tDescribe exactly what is visible on screen\u2028\n\t•\tUse positive instructions only\u2028\n\t•\tIf an instruction causes artefacts, remove it instead of compensating'),
        ],
    },
]
