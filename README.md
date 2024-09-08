# NoisOCR

Tools to simulate post-OCR noisy texts.

**Tools:**
- Sliding window;
- Sliding window with hyphenization;
- Simulate text errors;
- Simulate text annotations.

#### Sliding window:
```py
import noisocr

text = "Lorem Ipsum is simply dummy...type specimen book."
max_window_size = 50

windows = noisocr.sliding_window(text, max_window_size)

# Output:
# [
#   'Lorem Ipsum is simply dummy text of the printing', 
#   ...
#   'type and scrambled it to make a type specimen', 
#   'book.'
# ]
```

#### Sliding window with hyphenization:
* See the package https://pypi.org/project/PyHyphen to see all supported languages.

```py
import noisocr

text = "Lorem Ipsum is simply dummy...type specimen book."
max_window_size = 50

windows = noisocr.sliding_window(text, max_window_size)

# Output:
# [
#   'Lorem Ipsum is simply dummy text of the printing ',        
#   'typesetting industry. Lorem Ipsum has been the in-', 
#   ...
#   'scrambled it to make a type specimen book.'
# ]
```

#### Simulate text errors:
* See the package https://pypi.org/project/typo to see all possible error types.

```py
import noisocr

text = "Hello world."
text_with_errors = noisocr.simulate_errors(text, interactions=1)
# Output: Hello, wotrld!
text_with_errors = noisocr.simulate_errors(text, 2)
# Output: Hsllo,wlorld!
text_with_errors = noisocr.simulate_errors(text, 5)
# Output: fllo,w0rlr!
```

#### Simulate text annotations:
* By default, the annotations found in the [BRESSAY](https://icdar2024.ecomp.poli.br/dataset) dataset were used. But you can define which types of annotations you want to simulate. For annotations with internal text, use the pattern `##--text--##`.

```py
import noisocr

text = "Hello world."
text_with_annotation = noisocr.simulate_annotation(text, probability=0.5)
# Output: Hello, $$--xxx--$$
text_with_annotation = noisocr.simulate_annotation(text, probability=0.5)
# Output: Hello, ##--world!--##
text_with_annotation = noisocr.simulate_annotation(text, 0.01)
# Output: Hello world.
```