from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from model.parser import extract_text
from model.utils import clean_text

def get_keywords(vectorizer, vector):
    feature_names = vectorizer.get_feature_names_out()
    dense = vector.toarray()[0]
    return [feature_names[i] for i in dense.argsort()[-15:]]

def match_resume(resume_path, job_desc):
    resume_text = extract_text(resume_path)

    if not resume_text.strip():
        return {
            "score": 0,
            "similarity": 0,
            "keyword_score": 0,
            "matched": [],
            "missing": []
        }

    resume_clean = clean_text(resume_text)
    job_clean = clean_text(job_desc)

    vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1,2))
    vectors = vectorizer.fit_transform([resume_clean, job_clean])

    similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]

    resume_keywords = get_keywords(vectorizer, vectors[0])
    job_keywords = get_keywords(vectorizer, vectors[1])

    matched = list(set(resume_keywords) & set(job_keywords))
    missing = list(set(job_keywords) - set(resume_keywords))

    keyword_score = len(matched) / (len(job_keywords) + 1)
    final_score = (0.6 * similarity) + (0.4 * keyword_score)

    return {
        "score": round(final_score * 100, 2),
        "similarity": round(similarity * 100, 2),
        "keyword_score": round(keyword_score * 100, 2),
        "matched": matched[:10],
        "missing": missing[:10]
    }