import pyttsx3
import speech_recognition as sr
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import time


questions = {
    "Q1": {
        "question": "What is supervised learning?",
        "answer": "It technique where the model learns from labeled training data to make predictions or classify new unseen data."
    },
    "Q2": {

        "question": "What is overfitting? ",
        "answer": " when a machine learning model learns the training data too well and fails to generalize to new, unseen data."
    },
    "Q3": {
        "question": "What is feature selection",
        "answer": "Feature selection is the process of selecting relevant features from the input data to improve model performance and reduce complexity."
    },
    "Q4": {
        "question": "What is cross-validation",
        "answer": "It is a technique used to assess the performance of a machine learning model by dividing the data into multiple subsets for training and testing.."
        
    },
    "Q5": {
        "question": "What is the purpose of regularization in machine learning?",
        "answer": "Regularization is used to prevent overfitting by adding a penalty term to the model's objective function, encouraging simpler models."
    },
    "Q6": {
        "question": "What is underfitting? ",
        "answer": " Underfitting occurs when a machine learning model fails to capture the underlying patterns and relationships in the training data, resulting in poor performance on both the training and unseen data."
    },
    "Q7": {
        "question": "What is gradient descent?",
        "answer": "Gradient descent is an optimization algorithm used to minimize the error of a model by iteratively adjusting the model's parameters in the direction of steepest descent.."
    },
    "Q8": {
        "question": "What are hyperparameters in machine learning models?",
        "answer": "Hyperparameters in machine learning models are adjustable parameters that are set before training and impact the model's behavior and performance."
        
    },
    "Q9": {
        "question": "Explain the concept of cross-entropy loss in classification problem",
        "answer": "Cross-entropy loss in classification problems measures the dissimilarity between predicted class probabilities and true class labels to guide the model towards better predictions.."
    },
    "Q10": {
        "question": "What is the tradeoff between bias and variance in machine learning models",
        "answer": "The tradeoff between bias and variance in machine learning models is the delicate balance between model simplicity and ability to capture complex patterns in the data.."
        
    }
    
    
}

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def convert_speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:

        speak("please speak your answer")
        print("Please speak your answer:")
        audio = r.listen(source, phrase_time_limit=8)  # Adjust the phrase time limit as needed
        try:
            text = r.recognize_google(audio)
            print("Your answer:", text)
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand your answer.")
            return None
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            return None

def calculate_similarity(answer, candidate_answer):
    documents = [answer, candidate_answer]
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(documents)
    similarity = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])
    return similarity[0][0]

def get_comment(score):
    #threshold = 0.6  # Set your desired threshold value
    if score >= 0.6:
        return "Excellent!"
    elif score >= 0.3:
        return " Good!"
    elif score >=0.2:
        return "fine"
    else:
        return "okey"
        
    
speak("Hi I m Interview Assistant")
speak("welcome to interview")


    

def ask_question(question_id):
    if question_id in questions:
        question = questions[question_id]["question"]
        answer = questions[question_id]["answer"]
        repeat_prompt = "If you would like me to repeat the question, please say 'repeat'."
        print("Question:", question)
        speak(question)  # Speak the question
        time.sleep(3)  # Pause for 3 seconds
        candidate_answer = None
        while candidate_answer is None:
            candidate_answer = convert_speech_to_text()
            if candidate_answer is None or candidate_answer.lower() == "repeat":
                speak(question)  # Repeat the question
                time.sleep(3)  # Pause for 3 seconds
                candidate_answer = None
        score = calculate_similarity(answer, candidate_answer)
        print("Score:", score)
        comment = get_comment(score)
        print("Comment:", comment)
        speak(comment)  # Speak the comment
        if question_id != list(questions.keys())[-1]:
            speak("Moving to the next question")
        return score
    else:
        print("Invalid question ID.")
        return 0.0

# Ask questions and evaluate answers
total_score = 0.0
interrupted = False
for question_id in questions:
    if interrupted:
        break
    score = ask_question(question_id)
    total_score += score
    print()

    # Prompt the candidate to end the interview
    #speak("Do you want to end the interview? Please say 'yes' or 'no'.")
    #response = convert_speech_to_text()
    #if response and response.lower() == "yes":
        #interrupted = True

print("Total Score:", total_score)
if total_score >5.0:
    speak("phenomenal Performance")
    print("phenomenal Performance")
else:
    speak("good performance")
    print("good performance")

speak("Thank you for taking the first step towards a rewarding career with us!")
print("Thank you for taking the first step towards a rewarding career with us!")
