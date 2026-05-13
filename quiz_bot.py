import asyncio
import os

from telegram import Update, Poll
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    PollAnswerHandler,
)

TOKEN = os.getenv("TOKEN")

# ---------------- QUESTIONS ----------------
questions = [

# ---------------- QUESTIONS ----------------
questions = [


# ---------------- PHYSIOLOGY (26–65) ----------------

{"q":"ANP is released from:","options":["Ventricle","Atrium","Kidney","Brain"],"answer":1},
{"q":"BNP is released from:","options":["Atria","Ventricles","Liver","Kidney"],"answer":1},
{"q":"Main action of ANP is:","options":["Vasoconstriction","Na+ retention","Diuresis","K+ retention"],"answer":2},
{"q":"BNP is best used for:","options":["MI diagnosis","Heart failure diagnosis","Stroke","Arrhythmia"],"answer":1},
{"q":"Baroreceptors are located in:","options":["Kidney","Aortic arch and carotid sinus","Lung","Liver"],"answer":1},
{"q":"Carotid sinus sends signals via:","options":["Vagus nerve","Glossopharyngeal nerve","Phrenic nerve","Sympathetic chain"],"answer":1},
{"q":"Aortic arch baroreceptors send via:","options":["Vagus nerve","Glossopharyngeal nerve","Hypoglossal nerve","Facial nerve"],"answer":0},
{"q":"Hypotension causes:","options":["Increased parasympathetic","Decreased sympathetic","Increased sympathetic","No change"],"answer":2},
{"q":"Central chemoreceptors respond to:","options":["O2 only","CO2 and pH","Na+","K+"],"answer":1},
{"q":"Peripheral chemoreceptors respond to:","options":["O2, CO2, pH","Only CO2","Only O2","Glucose"],"answer":0},
{"q":"Pulmonary hypoxia causes:","options":["Vasodilation","Vasoconstriction","No effect","Bradycardia"],"answer":1},
{"q":"Systemic hypoxia causes:","options":["Vasodilation","Vasoconstriction","No change","Hypotension only"],"answer":0},
{"q":"Capillary hydrostatic pressure pushes fluid:","options":["Into capillary","Out of capillary","No movement","Into cells"],"answer":1},
{"q":"Plasma oncotic pressure pulls fluid:","options":["Out of capillary","Into capillary","Into tissues","No effect"],"answer":1},
{"q":"Edema in nephrotic syndrome due to:","options":["High albumin","Low plasma protein","High RBC","Low glucose"],"answer":1},
{"q":"Starling forces determine:","options":["Heart rate","Blood flow","Capillary fluid exchange","BP only"],"answer":2},
{"q":"Most important determinant of tissue flow is:","options":["Blood viscosity","Pressure gradient","Oxygen level","pH"],"answer":1},
{"q":"Brain autoregulation mainly depends on:","options":["O2","CO2","Na+","Glucose"],"answer":1},
{"q":"Heart autoregulation depends on:","options":["NO, CO2","Na+","K+ only","Glucose"],"answer":0},
{"q":"Kidney autoregulation uses:","options":["Myogenic + tubuloglomerular feedback","Hormones only","Nerves only","Lungs"],"answer":0},
{"q":"Resting cardiac output normal is about:","options":["2 L/min","5 L/min","10 L/min","15 L/min"],"answer":1},
{"q":"SVR is mainly controlled by:","options":["Heart valves","Arterioles","Veins","Capillaries"],"answer":1},
{"q":"Preload is related to:","options":["EDV","ESV","HR","BP"],"answer":0},
{"q":"Afterload mainly depends on:","options":["Venous return","Arterial resistance","Heart rate","Oxygen"],"answer":1},
{"q":"Frank-Starling law states:","options":["More stretch = more force","Less stretch = more force","No relation","BP decreases contraction"],"answer":0},
{"q":"Main effect of sympathetic system on heart:","options":["Decrease HR","Increase HR","No change","Stop heart"],"answer":1},
{"q":"Parasympathetic effect on heart:","options":["Increase HR","Decrease HR","Increase BP","No effect"],"answer":1},
{"q":"Coronary blood flow occurs mainly during:","options":["Systole","Diastole","Both equally","None"],"answer":1},
{"q":"Most important coronary artery:","options":["RCA","LAD","LCX","PDA"],"answer":1},
{"q":"LAD supplies mainly:","options":["Inferior wall","Anterior wall","Right atrium","Lung"],"answer":1},
{"q":"RCA supplies mainly:","options":["Inferior wall","Anterior wall","Brain","Kidney"],"answer":0},
{"q":"Troponin is marker of:","options":["Stroke","MI","Liver disease","Kidney failure"],"answer":1},
{"q":"BNP is increased in:","options":["Heart failure","Asthma","MI only","Stroke"],"answer":0},

# ---------------- ISCHEMIC HEART DISEASE (66–100) ----------------

{"q":"Most common cause of IHD:","options":["Vasculitis","Atherosclerosis","Infection","Congenital"],"answer":1},
{"q":"Most common site of atherosclerosis:","options":["Abdominal aorta","Coronary arteries","Lungs","Veins"],"answer":0},
{"q":"Foam cells are:","options":["RBCs","LDL macrophages","Platelets","Neutrophils"],"answer":1},
{"q":"Stable angina is due to:","options":["Plaque rupture","Fixed narrowing","Infection","Spasm only"],"answer":1},
{"q":"Unstable angina is due to:","options":["Fixed plaque","Plaque rupture","Normal arteries","Bradycardia"],"answer":1},
{"q":"MI marker most specific:","options":["CK-MB","Troponin I","LDH","Myoglobin"],"answer":1},
{"q":"STEMI indicates:","options":["Subendocardial infarct","Transmural infarct","No infarct","Spasm"],"answer":1},
{"q":"NSTEMI shows:","options":["ST elevation","ST depression","No change","Bradycardia"],"answer":1},
{"q":"Earliest MI change:","options":["Fibrosis","Coagulative necrosis","Calcification","Hypertrophy"],"answer":1},
{"q":"Most common MI artery:","options":["RCA","LAD","LCX","PDA"],"answer":1},
{"q":"LAD occlusion causes:","options":["Inferior MI","Anterior MI","Lateral MI","Right MI"],"answer":1},
{"q":"RCA occlusion causes:","options":["Inferior MI","Anterior MI","Brain stroke","Lung infarct"],"answer":0},
{"q":"Arrhythmia after MI occurs in:","options":["Minutes","1-3 days","Weeks","Months"],"answer":1},
{"q":"Papillary muscle rupture causes:","options":["Aortic stenosis","Mitral regurgitation","ASD","VSD"],"answer":1},
{"q":"Dressler syndrome occurs:","options":["Hours after MI","Days after MI","Weeks after MI","Before MI"],"answer":2},
{"q":"Most atherogenic lipoprotein:","options":["HDL","LDL","Chylomicron","VLDL"],"answer":1},
{"q":"HDL function is:","options":["Increase plaque","Remove cholesterol","Cause MI","Increase LDL"],"answer":1},
{"q":"Endothelial dysfunction causes:","options":["Less inflammation","More macrophages","Less LDL","No change"],"answer":1},
{"q":"Plaque rupture leads to:","options":["Hypotension","Thrombosis","Bradycardia","Fever"],"answer":1},
{"q":"Eisenmenger syndrome is:","options":["Right to left shunt reversal","Normal circulation","Valve disease","Arrhythmia"],"answer":0},
{"q":"Most dangerous complication of plaque rupture:","options":["Vasodilation","Thrombosis","Fever","Hypoxia"],"answer":1},
{"q":"Chest pain + troponin means:","options":["Stable angina","MI","Asthma","GERD"],"answer":1}
]

# ---------------- DATA STORAGE ----------------
user_scores = {}
poll_answers = {}

# ---------------- START ----------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Quiz Bot Ready 🚀 Use /quiz")

# ---------------- QUIZ ----------------
async def quiz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    username = update.message.from_user.username or "Unknown"

    if user_id not in user_scores:
        user_scores[user_id] = {"score": 0, "username": username}

    for i, q in enumerate(questions):
        message = await update.message.reply_poll(
            question=f"Q{i+1}: {q['q']}",
            options=q["options"],
            type=Poll.QUIZ,
            correct_option_id=q["answer"],
            is_anonymous=False,
            open_period=35
        )

        poll_answers[message.poll.id] = q["answer"]

        await asyncio.sleep(35)

    await update.message.reply_text("Quiz finished! Use /result")

# ---------------- ANSWERS ----------------
async def handle_poll_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.poll_answer.user.id
    username = update.poll_answer.user.username or "Unknown"

    selected = update.poll_answer.option_ids[0]
    poll_id = update.poll_answer.poll_id

    correct = poll_answers.get(poll_id)

    if correct is None:
        return

    if user_id not in user_scores:
        user_scores[user_id] = {"score": 0, "username": username}

    if selected == correct:
        user_scores[user_id]["score"] += 2.26

# ---------------- RESULT ----------------
async def result(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not user_scores:
        await update.message.reply_text("No results yet")
        return

    leaderboard = []

    for user_id, data in user_scores.items():
        score = data["score"]
        username = data["username"]

        percent = (score / (len(questions) * 2.26)) * 100

        leaderboard.append({
            "username": username,
            "score": score,
            "percent": percent
        })

    leaderboard.sort(key=lambda x: x["score"], reverse=True)

    text = "🏆 QUIZ RESULTS (LEADERBOARD)\n\n"

    for i, user in enumerate(leaderboard):
        rank = i + 1

        if rank == 1:
            medal = "🥇 GOLD"
        elif rank == 2:
            medal = "🥈 SILVER"
        elif rank == 3:
            medal = "🥉 BRONZE"
        else:
            medal = ""

        status = "PASS ✅" if user["percent"] >= 60 else "FAIL ❌"

        text += (
            f"{rank}. {user['username']} {medal}\n"
            f"Score: {user['score']:.2f}\n"
            f"{user['percent']:.1f}% → {status}\n\n"
        )

    await update.message.reply_text(text)

# ---------------- APP ----------------
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("quiz", quiz))
app.add_handler(CommandHandler("result", result))
app.add_handler(PollAnswerHandler(handle_poll_answer))

print("Bot running...")
app.run_polling()