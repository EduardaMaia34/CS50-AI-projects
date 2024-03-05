import csv
import sys
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions) #evaluate(output_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """
    evidence = []
    labels = []
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            if row[-1]==True:
                labels.append(1)
            else:
                labels.append(0)

            temp = []
            temp.append(int(row[0]))
            temp.append(float(row[1]))
            temp.append(int(row[2]))
            temp.append(float(row[3]))
            temp.append(int(row[4]))
            temp.append(float(row[5]))
            temp.append(float(row[6]))
            temp.append(float(row[7]))
            temp.append(float(row[8]))
            temp.append(float(row[9]))
            temp.append(months.index(row[10]))
            temp.append(int(row[11]))
            temp.append(int(row[12]))
            temp.append(int(row[13]))
            temp.append(int(row[14]))
            temp.append(1 if row[15] == "Returning_Visitor" else 0,)
            temp.append(1 if row[16] == "TRUE" else 0)
            evidence.append(temp)

    return evidence, labels

def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    model = KNeighborsClassifier(n_neighbors=1)
    model.fit(evidence, labels)
    return model

def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificity).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    positive = 0
    negative = 0
    true_pos = 0
    true_neg = 0

    for index in range(len(labels)):
        if labels[index] == 1:
            positive += 1
            if predictions[index] == 1:
                true_pos += 1

        else:
            negative += 1
            if predictions[index] == 0:
                true_neg += 1

    sensitivity = true_pos / positive
    specificity = true_neg / negative

    return sensitivity, specificity



if __name__ == "__main__":
    main()
