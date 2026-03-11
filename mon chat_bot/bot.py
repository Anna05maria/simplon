# chatbot_mini.py - LE BOT LE PLUS SIMPLE

reponses = {
    "bonjour": "Salut! ",
    "comment": "Bien et toi?",
    "merci": "Avec plaisir!",
    "au revoir": "À plus!"
}

print("Bot prêt! Tape ton message:")
msg = input("> ").lower()

trouve = False
for mot in reponses:
    if mot in msg:
        print("Réponse:", reponses[mot])
        trouve = True

if not trouve:
    print("éponse: Désolé, j'ai pas compris")