from string import punctuation as punct

MAPPINGS = {
        'g': r'(sdgs|sdg|goals|goal)',
        't': r'(target)',
        'i': r'(indicator)'
    }


def extract_type(type_):
    """
    Extract the type of label
    :param type_:
    :return:
    """
    for key, pattern in MAPPINGS.items():
        if type_.lower() in pattern:
            return key

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def extract_num(numbers):
    results = []
    for i in numbers.replace(',', ' ').split():
        if i.lower() not in 'and':
            i = i.strip(punct).split('.')[0]
            if is_number(i) and int(i) in range(1, 18):
                results.append(i)
    return set(results)


def format_labels(type_, numbers):
    """
    :param type_:
    :param numbers:
    :return: list of labels
    """
    labels = []
    label_numbers = extract_num(numbers)
    for number in label_numbers:
        labels.append(number)
    return labels


def trans_labels(labels):
    results = dict()
    for i in range(1,18):
        label = f'g_{i}'
        if label in labels:
            results[label] = True
        else:
            results[label] = False
    return results

