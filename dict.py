class Solution:
    def longestWord(self, words):
        # Create a set for quick lookup
        word_set = set(words)
        
        # Sort words by length and then lexicographically
        words.sort(key=lambda x: (-len(x), x))
        
        longest_word = ""
        
        # Check each word in the sorted list
        for word in words:
            # Check if all prefixes of the word are in the set
            if all(word[:i] in word_set for i in range(1, len(word))):
                longest_word = word
                break  # We can break as we are looking for the first longest valid word
        
        return longest_word

# Example usage
if __name__ == "__main__":
    solution = Solution()
    words = [
        "a", "at", "bat", "banana", "b", "ban", "band", "bandana", 
        "car", "c", "ca", "cat", "cats", "do", "dog", 
        "dot", "dote", "dotty", "e", "eat", "ear", "earring", 
        "g", "go", "goat", "got", "hello", "he", "her", "h", 
        "hi", "hit", "i", "it", "k", "kit", "kite", "kitten",
        "l", "la", "lad", "ladder", "m", "man", "mad", "made", 
        "n", "no", "not", "on", "one", "own", "our", "out",
        "pen", "pencil", "pet", "pick", "pizza", "rat", "rate",
        "ratty", "s", "sat", "see", "see-saw", "so", "to", "top",
        "two", "who", "whom", "word", "world", "work", "worker"
    ]
    print(solution.longestWord(words))  # Output: "word"
