# _*_ coding : utf-8 _*_
# @Time : 2025/3/4 15:32
# @Author : 鑫
# @File : JugRouge
# @Project JugRouge

from difflib import SequenceMatcher
from Levenshtein import distance as levenshtein_distance

def lcs_length(s1, s2):
    matcher = SequenceMatcher(None, s1, s2)
    return sum(triple.size for triple in matcher.get_matching_blocks())

def jaccard_similarity(s1, s2):
    set1, set2 = set(s1.split()), set(s2.split())
    intersection = len(set1 & set2)
    union = len(set1 | set2)
    return intersection / union if union != 0 else 0

def compare_rpa_similarity(predicted, standard):
    lcs_score = lcs_length(predicted, standard) / len(standard) if len(standard) > 0 else 0
    jaccard_score = jaccard_similarity(predicted, standard)
    edit_distance = levenshtein_distance(predicted, standard)

    return {
        "LCS 相似度": lcs_score,
        "Jaccard 相似度": jaccard_score,
        "编辑距离": edit_distance
    }

# 示例：标准答案和预测结果
standard_rpa = "Click Button 'Submit' -> Wait 2s -> Read Message"
predicted_rpa = "Click Button 'Submit' -> Wait 3s -> Read Text"

# 计算相似度
similarity_scores = compare_rpa_similarity(predicted_rpa, standard_rpa)
print(similarity_scores)
