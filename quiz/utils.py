def process_answer(user_quiz_session):
    score = 0
    for user_answer_map in user_quiz_session.useranswermap_set.all():
        if user_answer_map.user_answer == user_answer_map.question.answer:
            user_answer_map.is_correct = True
            score += 1
    return score
        