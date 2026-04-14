"""Advanced Prompt Engineering: Zero-shot, one-shot, and few-shot
techniques Week2 -
Objective: To explore and compare Zero-shot, One-shot, and Few-shot
prompting techniques for classifying emails into predefined categories
using a large language model (LLM).
1. Suppose that you work for a company that receives hundreds of
customer emails daily. Management wants to automatically classify
emails into categories like "Billing", "Technical Support", "Feedback",
and "Others" before assigning them to appropriate departments.
Instead of training a new model, your task is to use prompt
engineering techniques with an existing LLM to handle the
classification.
Tasks to be completed are as below
a. Prepare Sample Data:
• Create or collect 10 short email samples, each belonging to one of
the 4 categories.
b. Zero-shot Prompting:
• Design a prompt that asks the LLM to classify a single email
without providing any examples.
• Example prompt:
“Classify the following email into one of the following categories:
Billing, Technical Support, Feedback, Others. Email: ‘I have not
received my invoice for last month.’”
c. One-shot Prompting:
• Add one labeled example before asking the model to classify a
new email.
d. Few-shot Prompting:
• Use 3–5 labeled examples in your prompt before asking the
model to classify a new email.
e. Evaluation:
• Run all three techniques on the same set of 5 test emails.
• Compare and document the accuracy and clarity of responses."""

"""def classify_email(email):
    email = email.lower()
    
    if "invoice" in email or "payment" in email or "refund" in email:
        return "Billing"
    elif "error" in email or "login" in email or "crash" in email:
        return "Technical Support"
    elif "love" in email or "good" in email or "excellent" in email:
        return "Feedback"
    else:
        return "Others"

email = input("Enter email: ")
print("Category:", classify_email(email))
"""


"""2. Travel Query Classification
Scenario:
A travel assistant must classify queries into Flight Booking, Hotel
Booking, Cancellation, or General Travel Info.
Tasks:
a. Prepare labeled travel queries.
b. Apply Zero-shot prompting.
c. Apply One-shot prompting.
d. Apply Few-shot prompting.
e. Compare response consistency."""

"""def classify_travel(query):
    query = query.lower()
    
    if "flight" in query or "ticket" in query:
        return "Flight Booking"
    elif "hotel" in query or "room" in query:
        return "Hotel Booking"
    elif "cancel" in query or "refund" in query:
        return "Cancellation"
    else:
        return "General Travel Info"

query = input("Enter travel query: ")
print("Category:", classify_travel(query))"""


"""3. Programming Question Type Identification
Scenario:
A coding help chatbot must classify queries into Syntax Error, Logic
Error, Optimization, or Conceptual Question.
Tasks:
a. Prepare coding-related user queries.
b. Perform Zero-shot classification.
c. Perform One-shot classification.
d. Perform Few-shot classification.
e. Analyze improvements in technical accuracy."""

"""def classify_programming(query):
    query = query.lower()
    
    if "syntax" in query or "indent" in query:
        return "Syntax Error"
    elif "wrong output" in query or "logic" in query:
        return "Logic Error"
    elif "optimize" in query or "fast" in query:
        return "Optimization"
    else:
        return "Conceptual Question"

query = input("Enter coding query: ")
print("Category:", classify_programming(query))
"""



"""4. Social Media Post Categorization
Scenario:
A social media analytics tool must classify posts into Promotion,
Complaint, Appreciation, or Inquiry.
Tasks:
1. Prepare sample social media posts.
2. Use Zero-shot prompting.
3. Use One-shot prompting.
4. Use Few-shot prompting.
5. Analyze informal language handling"""

def classify_post(post):
    post = post.lower()
    
    if "buy" in post or "offer" in post or "sale" in post:
        return "Promotion"
    elif "bad" in post or "worst" in post or "issue" in post:
        return "Complaint"
    elif "love" in post or "great" in post:
        return "Appreciation"
    else:
        return "Inquiry"

post = input("Enter social media post: ")
print("Category:", classify_post(post))
