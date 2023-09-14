import csv


def test_cluSequence():
    test_data = read_from_csv_file()

    results, intent_similarity_percentage, entity_similarity_percentage, test_result = run_clu_via_api_and_get_test_result(test_data, pass_criteria_percentage=70)

    # Create a results log
    header = ["Utterance", "Expected Intent", "API Intent", "Expected Entity", "API Entity", "Intent Similarity", "Entity Similarity"]
    results.insert(0, header)

    # Print the results log
    for row in results:
        print("\t".join(row))

    print(f"Intent Similarity Percentage: {intent_similarity_percentage}%")
    print(f"Entity Similarity Percentage: {entity_similarity_percentage}%")
    print(f"Test Result: {test_result}")


# Method for create csv file for utterances and the relevant intents and entities
def read_from_csv_file():
    test_data = []
    with open("utterances.csv", 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            utterance, expected_intent, expected_entity = row
            test_data.append((utterance, expected_intent, expected_entity))
    return test_data


# Function to run CLU AI Tests
def run_clu_via_api_and_get_test_result(test_data, pass_criteria_percentile):
    results = []
    similar_intents = 0
    similar_entities = 0

    for utterance, expected_intent, expected_entity in test_data:
        api_intent, api_entity, intent_similarity, entity_similarity = compare_results(utterance, expected_intent, expected_entity)

        results.append([utterance, expected_intent, api_intent, expected_entity, api_entity, intent_similarity, entity_similarity])

        if intent_similarity == "Similar":
            similar_intents += 1
        if entity_similarity == "Similar":
            similar_entities += 1

    intent_similarity_percentage = (similar_intents / len(test_data)) * 100
    entity_similarity_percentage = (similar_entities / len(test_data)) * 100

    test_result = "Pass" if intent_similarity_percentage >= pass_criteria_percentile and entity_similarity_percentage >= pass_criteria_percentile else "Fail"

    return results, intent_similarity_percentage, entity_similarity_percentage, test_result


# Method to compare actual and expected results and calculate similarity
def compare_results(expected_intent, expected_entity):
    # Api Simulation
    api_intent = "API_intent"
    api_entity = "API_entity"

    # Compare actual results with expected results
    intent_similarity = "Similar" if api_intent == expected_intent else "NotSimilar"
    entity_similarity = "Similar" if api_entity == expected_entity else "NotSimilar"

    return api_intent, api_entity, intent_similarity, entity_similarity