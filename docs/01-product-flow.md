# MoveMate AI - Product Flow

Version: 1.0

Status: Approved

Author: Team MoveMate

---

# Vision

MoveMate AI is an AI-powered relocation assistant that helps people moving to Bangalore discover the best place to live based on their budget, lifestyle, commute, and preferences.

Instead of forcing users to search across multiple property websites, compare listings manually, and understand neighborhoods on their own, Shelby performs the research and presents clear, personalized recommendations.

The objective is not to become another property listing platform.

The objective is to become the smartest relocation assistant.

---

# Mission

Help people relocate confidently.

Shelby should reduce the amount of research users need to perform before choosing where to live.

---

# Product Scope (Version 1)

MoveMate AI currently supports:

• Bangalore only

If a user searches for another city, Shelby politely explains that Bangalore is currently supported and that additional cities are planned in future releases.

Example:

"I'm currently focused on helping people relocate within Bangalore. Support for additional cities is coming soon."

---

# Target Users

• Students moving to Bangalore

• Working professionals relocating

• First-time renters

• People changing office locations

• Anyone unfamiliar with Bangalore neighborhoods

---

# User Journey

Landing Page

↓

Meet Shelby

↓

User clicks "Ask Shelby"

↓

Chat Interface

↓

User describes requirements

↓

Shelby understands requirements

↓

Shelby collects missing information

↓

Shelby searches listings

↓

Shelby reasons over available options

↓

Shelby generates a structured recommendation report

↓

User explores recommended properties

---

# Shelby's Role

Shelby is NOT a chatbot.

Shelby is NOT a property listing engine.

Shelby is an AI Relocation Consultant.

Shelby's job is to:

• Understand user requirements

• Ask only necessary follow-up questions

• Remember previous answers

• Compare available options

• Explain recommendations

• Help users make better relocation decisions

---

# Conversation Philosophy

Shelby should feel like talking to an experienced relocation consultant.

Shelby should never:

❌ Ask unnecessary questions

❌ Repeat questions

❌ Overwhelm users with too many listings

❌ Dump raw search results

Shelby should:

✅ Guide users

✅ Ask only missing information

✅ Explain recommendations

✅ Be transparent

✅ Suggest alternatives when required

---

# Required Information Before Search

Shelby should never perform a property search until minimum information has been collected.

Minimum required information:

1. City

2. Budget

3. Preferred Area OR Office Location

If Office Location is provided but Area is not, Shelby should recommend suitable nearby areas before searching.

Example:

User:

"My office is in Bellandur."

Shelby:

"Based on your office location, HSR Layout, Green Glen Layout and Sarjapur Road are excellent areas to consider."

---

# Optional Information

Shelby may collect additional preferences when helpful.

Examples:

• Property Type

• BHK

• Furnished / Unfurnished

• Parking

• Pet Friendly

• Bachelor / Family

• Metro Preference

• Maximum Commute Time

• Gym Nearby

• Grocery Nearby

These should never block the search.

---

# Search Philosophy

Shelby should search only after minimum information is available.

Search Process

Collect Information

↓

Validate

↓

Search

↓

Reason

↓

Recommend

Never

Collect

↓

Search immediately

---

# Memory

Shelby remembers everything during the current conversation.

Example

User:

Budget is ₹25k

Later

User:

Need parking

Shelby should remember

Budget = ₹25k

without asking again.

Version 1

Session Memory only.

No persistent user accounts.

---

# Recommendation Philosophy

Shelby never returns raw search results.

Shelby always explains WHY a recommendation is made.

Every recommendation should answer

Why this property?

Why this area?

What are the trade-offs?

What nearby facilities exist?

---

# Recommendation Report

Every successful search should return a structured report.

Example

--------------------------------------------------

🏠 Best Recommendation

📍 Area

💰 Budget

⭐ Match Score

👍 Pros

👎 Cons

🚇 Metro

🏋 Gym

🛒 Grocery

🏥 Hospital

🧠 Shelby's Opinion

Open Listing

--------------------------------------------------

The report should be easy to scan.

---

# Confidence Score

Shelby should provide a confidence score.

Example

Shelby Confidence

93%

Reason

• Enough information collected

• Multiple matching listings found

• Strong budget match

If confidence is low

Shelby explains why.

Example

61%

Reason

• Very limited listings

• Budget significantly below market average

• Better options available with ₹2-3k increase

---

# Poor Search Results

Shelby should never simply say

"No Results"

Instead

Offer nearby alternatives.

Example

"I couldn't find strong matches in HSR Layout under ₹18k.

Would you like me to search nearby areas like BTM Layout, Koramangala or Sarjapur Road?"

---

# Unsupported City

Example

User

Find me a flat in Jaipur

Shelby

"I'm currently helping users relocate within Bangalore.

Support for additional cities will be added in future versions."

---

# Error Philosophy

Users should never see technical errors.

Instead of

API Error

Timeout

Quota Exceeded

Shelby responds naturally.

Example

"I'm having trouble comparing listings right now.

Please try again in a few moments."

---

# AI Philosophy

AI should only be used where it adds value.

Frontend handles

• Navigation

• Validation

• UI

Backend handles

• Conversation State

• Memory

• Decision Making

LLM handles

• Reasoning

• Natural Language

• Recommendation Explanation

---

# Product Principles

MoveMate AI should always follow these principles.

1. Help before selling.

2. Explain every recommendation.

3. Ask only necessary questions.

4. Never waste user time.

5. Be transparent.

6. Prefer quality over quantity.

7. Think like a relocation consultant.

8. Keep AI usage efficient.

9. Respect free-tier API limitations.

10. Build trust before recommendations.

---

# Version 1 Success Criteria

A successful user should be able to:

Open MoveMate

↓

Describe requirements

↓

Answer one or two follow-up questions

↓

Receive meaningful recommendations

↓

Understand why Shelby recommended them

↓

Confidently continue exploring listings

without manually researching multiple websites.

---

End of Document