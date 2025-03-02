from collections import Counter
import nltk
import sys
from typing import List
from pathlib import Path
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context


def ensure_nltk_resources() -> None:
    try:
        try:
            nltk.data.find("tokenizers/punkt")
            nltk.data.find("tokenizers/punkt_tab/english")
        except LookupError:
            print("Downloading required NLTK resources...")
            nltk.download("punkt", quiet=True)
            nltk.download("punkt_tab", quiet=True)
        nltk.data.find("tokenizers/punkt")
        nltk.data.find("tokenizers/punkt_tab/english")
        print("NLTK resources verified")

    except Exception as e:
        sys.exit(
            f"Failed to setup NLTK resources: {e}\n"
            "Please try manually:\n"
            ">>> import nltk\n"
            ">>> nltk.download('punkt')\n"
            ">>> nltk.download('punkt_tab')\n"
            "Or fix your SSL configuration"
        )


def load_data(directory: str) -> List[str]:
    contents: List[str] = []
    directory_path = Path(directory)

    if not directory_path.exists() or not directory_path.is_dir():
        raise ValueError(f"Invalid directory: {directory}")

    for filepath in directory_path.iterdir():
        if filepath.is_file():
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    text = f.read()
                    tokens = [
                        word.lower()
                        for word in nltk.word_tokenize(text)
                        if any(c.isalpha() for c in word)
                    ]
                    contents.extend(tokens)
            except (IOError, UnicodeDecodeError) as e:
                print(f"Warning: Skipping file {filepath} due to error: {e}")

    return contents


def main() -> None:
    try:
        if len(sys.argv) != 3:
            sys.exit(
                "Usage: python ngrams.py n corpus\n"
                "  n: size of n-grams\n"
                "  corpus: directory containing text files"
            )

        print("Loading data...")

        ensure_nltk_resources()

        n = int(sys.argv[1])
        if n <= 0:
            raise ValueError("n must be a positive integer")

        corpus = load_data(sys.argv[2])

        if not corpus:
            print("No valid text data found in corpus")
            return

        ngrams = Counter(nltk.ngrams(corpus, n))

        if not ngrams:
            print("No n-grams found in corpus")
            return

        print(f"\nTop 10 {n}-grams:")
        for ngram, freq in ngrams.most_common(10):
            ngram_str = " ".join(ngram)
            print(f"{freq}: {ngram_str}")

    except ValueError as e:
        sys.exit(f"Error: {e}")
    except Exception as e:
        sys.exit(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
