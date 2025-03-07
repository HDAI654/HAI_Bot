from HAI_Bot import HAI_model
n = HAI_model("NLP_Data.json", "chatbot_model.h5")

while True:
    m = str(input("TEXT ==>    ")).lower()
    if m == 'quit':
        break
    print(n.Chat(m))