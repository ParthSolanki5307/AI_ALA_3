from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__, static_folder="static", template_folder="templates")

# Simple rule-based QA pairs (keywords -> response)
QA_RULES = [
    # greetings
    (r"\bhi\b|\bhello\b|\bhey\b", "CricBot: Hello! Kaise madad karu cricket se related?"),
    (r"\bthank(s| you)\b|\bthx\b", "CricBot: You're welcome! Aur kuch poochna hai?"),
    # players
    (r"who is virat kohli", "CricBot: Virat Kohli is a famous Indian cricketer and former captain of the Indian national team."),
    (r"who is ms dhoni|who is dhoni", "CricBot: Mahendra Singh Dhoni — former Indian captain, wicket-keeper and one of the best finishers."),
    (r"who is sachin tendulkar|who is sachin", "CricBot: Sachin Tendulkar — legendary Indian batsman, 'God of Cricket'."),
    (r"who is rohit sharma|who is rohit", "CricBot: Rohit Sharma — Indian opener and current (as of recent years) limited-overs captain in various formats."),
    # history & tournaments
    (r"who won 2011 world cup", "CricBot: India won the 2011 ICC Cricket World Cup by defeating Sri Lanka in the final."),
    (r"who won 2003 world cup", "CricBot: Australia won the 2003 Cricket World Cup."),
    # rules & basics
    (r"\brules\b|\bhow to play\b|\bhow do you play\b", "CricBot: Cricket is played between two teams of 11 players. Each team bats once or twice depending on format. Aim: score more runs than opponent. Ask for specifics (overs, lbw, powerplay)."),
    (r"\bwhat is an over\b|\bover\b", "CricBot: An over consists of 6 legal deliveries bowled by one bowler."),
    (r"\bwhat is lbw\b|\blbw\b", "CricBot: LBW (leg before wicket) is when a ball would have hit the stumps but hits batter's pads first. Several conditions apply (impact, pitching, hitting stumps)."),
    (r"\bwhat is drs\b|\bdecision review system\b", "CricBot: DRS is the Decision Review System used to review umpire decisions using technology (replays, ball-tracking). Teams have limited reviews."),
    (r"\bwhat is powerplay\b|\bpower play\b", "CricBot: Powerplay = fielding restrictions early in innings (limits on outside-30-yard-circle fielders). Rules vary by format."),
    (r"\bwhat is a maiden\b|\bmaiden over\b", "CricBot: Maiden over = an over with 0 runs conceded."),
    # stadiums & venues
    (r"how many cricket stadiums in india|how many stadiums in india", "CricBot: Around 50+ stadiums in India; about 25-30 host international matches regularly (exact count changes)."),
    (r"famous cricket stadiums", "CricBot: Famous ones: MCG (Melbourne), Eden Gardens (Kolkata), Lord's (London), Wankhede (Mumbai), Sydney Cricket Ground."),
    # records & stats
    (r"most runs in odi|highest odi score", "CricBot: Rohit Sharma holds the highest individual ODI score (264). Sachin Tendulkar has the most ODI runs overall."),
    (r"most test centuries", "CricBot: Sachin Tendulkar holds the record for most international centuries overall. For Test centuries, Sachin also ranks very high; as of older stats, Tendulkar and others top lists."),
    # match updates / live
    (r"latest match|recent match|live score", "CricBot: Sorry, I can't provide live updates here. Use cricket websites or APIs (ESPN Cricinfo, Cricbuzz) for live scores."),
    # opinions
    (r"best bowler", "CricBot: Some great bowlers: Wasim Akram, Glenn McGrath, Muttiah Muralitharan, James Anderson, Jasprit Bumrah."),
    (r"best wicket keeper", "CricBot: MS Dhoni is widely regarded as one of the best wicket-keepers and finishers."),
    # misc
    (r"how many players in a team", "CricBot: 11 players play in the playing XI for each team."),
    (r"what are the formats of cricket|formats of cricket", "CricBot: Main formats: Test (5 days), ODI (50 overs each), T20 (20 overs each)."),
    (r"what is an innings", "CricBot: An innings is when one team bats and the other bowls/fields. Test matches have two innings per team; ODIs and T20s have one innings per team."),
    (r"\bexit\b|\bquit\b|\bbye\b", "CricBot: Bye! Good luck and enjoy cricket."),
]

def generate_response(user_text: str) -> str:
    text = user_text.lower().strip()
    # Try matching rules in order
    for pattern, response in QA_RULES:
        if re.search(pattern, text):
            return response
    # fallback: try keyword-based short answers
    if "score" in text or "runs" in text:
        return "CricBot: Agar specific match ka score chahiye to live score API dekho. Main static info de sakta hu."
    # default reply
    return "CricBot: Sorry, mujhe iska exact answer nahi pata — tum yeh question thoda aur clear likh sakte ho ya main common topics bata dun?"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json() or {}
    user_text = data.get("message", "")
    if not user_text:
        return jsonify({"reply": "CricBot: Please type a question."})
    # If user types 'exit', return exit message
    if user_text.strip().lower() in ("exit", "quit", "bye"):
        return jsonify({"reply": "CricBot: Bye! Chat closed."})
    reply = generate_response(user_text)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
