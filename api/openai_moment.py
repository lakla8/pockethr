from openai import OpenAI


def analysis():
    client = OpenAI(
        api_key="c5949f59147d4771aa5e57ed1cdf7031",
        base_url="https://api.aimlapi.com",
    )

    response = client.chat.completions.create(
        model="mistralai/Mistral-7B-Instruct-v0.2",
        messages=[
            {
                "role": "system",
                "content": "You are an AI-HR assistant who knows everything and specializes on human resources and their promotion.",
            },
            {
                "role": "user",
                "content": "Write 3 random different strategies for an average It worker. Each strategy should be in 50 characters."
            },
        ],
    )
    answer = response.choices[0].message.content.split('\n')
    return answer


def statistics(profile: dict):
    location = profile['location']
    communication = profile['communication']
    criticism = profile['criticism']
    making_decisions = profile['making_decisions']
    structure = profile['structure']
    leaderships = profile['leaderships']
    conflicts = profile['conflicts']
    time_managment = profile['time managment']
    communicator = profile['communicator']
    link = profile['link']
    keeper = profile['keeper']
    observer = profile['observer']
    rate = profile['rate']
    text = f"Analyze the success of the user on a 100-point scale based on the following attributes: Location: {location}, Communication Skills: {communication}, Ability to Handle Criticism: {criticism}, Decision-Making Skills: {making_decisions}, Structural Organization: {structure}, Leadership Qualities: {leaderships}, Conflict Management Skills: {conflicts}, Time Management: {time_managment}, Communication Style: {communicator}, Professional Networking: {link}, Reliability: {keeper}, Observational Skills: {observer}, Current Performance Rating: {rate}. Please provide a detailed analysis in 3 sentences with a score out of 100, including factors contributing to the score and areas for improvement. In first row write a number, in next row write your thoughts(in one line)"

    client = OpenAI(
        api_key="c5949f59147d4771aa5e57ed1cdf7031",
        base_url="https://api.aimlapi.com",
    )

    response = client.chat.completions.create(
        model="mistralai/Mistral-7B-Instruct-v0.2",
        messages=[
            {
                "role": "system",
                "content": "You are an AI-HR assistant who knows everything and specializes on human resources and their promotion.",
            },
            {
                "role": "user",
                "content": text
            },
        ],
    )
    answer = response.choices[0].message.content.split('\n')
    return answer


def goal(information):
    link_description = information['link_description']
    name = information['name']
    company = information['company']

    text = f"Predict the success of the goal based on: Link Description: {link_description}, Name: {name}, Company: {company}"
    client = OpenAI(
        api_key="c5949f59147d4771aa5e57ed1cdf7031",
        base_url="https://api.aimlapi.com",
    )

    response = client.chat.completions.create(
        model="mistralai/Mistral-7B-Instruct-v0.2",
        messages=[
            {
                "role": "system",
                "content": "You are an AI-HR assistant who knows everything and specializes on human resources and their promotion.",
            },
            {
                "role": "user",
                "content": text
            },
        ],
    )
    answer = response.choices[0].message.content
    return answer

