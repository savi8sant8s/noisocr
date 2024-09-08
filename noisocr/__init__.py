import random
import typo
from hyphen import Hyphenator

annotations = [
    '##@@???@@##',
    '$$@@???@@$$',
    '@@???@@', 
    '##--xxx--##', 
    '$$--xxx--$$',
    '--xxx--',
    '##--text--##',
    '$$--text--$$',
    '##text##',
    '$$text$$', 
    '--text--' 
]

def simulate_annotation(text, annotations=annotations, probability=0.01):
    """
    Simulate the annotation of a word in a text.
    
    :param text: The text to be annotated.
    :param annotations: A list of possible annotations.
    :param probability: The probability of a word being annotated.

    :return: The text with the annotation
    """
    
    words = text.split()
    
    if len(words) > 1:
        target_word = random.choice(words)
    else:
        return text
    
    if random.random() < probability:
        annotation = random.choice(annotations)
        
        if 'text' in annotation:
            annotated_text = annotation.replace('text', target_word)
        else:
            annotated_text = annotation
        
        result_text = text.replace(target_word, annotated_text, 1)
        return result_text
    else:
        return text
    
def simulate_errors(text, interactions=3, seed=None):
    """
    Simulate errors in a text.

    :param text: The text to be modified.
    :param interactions: The number of interactions to simulate errors.
    :param seed: The seed for the random generator.

    :return: The text with errors.
    """
    
    methods = ["char_swap", "missing_char", "extra_char", "nearby_char", "similar_char", "skipped_space", "random_space", "repeated_char", "unichar"]

    if seed is not None:
        random.seed(seed)
    else:
        random.seed()

    instance = typo.StrErrer(text)
    method = random.choice(methods)
    method_to_call = getattr(instance, method)
    text = method_to_call().result

    if interactions > 0:
        interactions -= 1
        text = simulate_errors(text, interactions, seed=seed)

    return text

def sliding_window_with_hyphenation(text, window_size=80, language='pt_BR'):
    """
    Slide a window over a text and hyphenize the words.

    :param text: The text to be split.
    :param window_size: The size of the window.
    :param language: The language for hyphenation.

    :return: A list of windows.
    """

    hyphenator = Hyphenator(language)
    words = text.split()
    windows = []
    current_window = []
    remaining_word = ""

    for word in words:
        if remaining_word:
            word = remaining_word + word
            remaining_word = ""

        if len(" ".join(current_window)) + len(word) + 1 <= window_size:
            current_window.append(word)
        else:
            syllables = hyphenator.syllables(word)
            temp_word = ""

            for i, syllable in enumerate(syllables):
                if len(" ".join(current_window)) + len(temp_word) + len(syllable) + 1 <= window_size:
                    temp_word += syllable
                else:
                    if temp_word:
                        current_window.append(temp_word + "-")
                        remaining_word = "".join(syllables[i:]) + " "
                        break
                    else:
                        remaining_word = word + " "
                        break
            else:
                current_window.append(temp_word)
                remaining_word = ""

            windows.append(" ".join(current_window))
            current_window = []

    if remaining_word:
        current_window.append(remaining_word)
    if current_window:
        windows.append(" ".join(current_window))

    return windows

def sliding_window(text, window_size=80):
    """
    Slide a window over a text.

    :param text: The text to be split.
    :param window_size: The size of the window.

    :return: A list of windows.
    """
     
    words = text.split()
    windows = []
    current_window = []
    for word in words:
        if len(" ".join(current_window)) + len(word) + 1 <= window_size:
            current_window.append(word)
        else:
            windows.append(" ".join(current_window))
            current_window = [word]
    windows.append(" ".join(current_window))
    return windows