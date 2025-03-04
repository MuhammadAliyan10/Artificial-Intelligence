# Harvard University Artificial Intelligence Course Overview

This document serves as a comprehensive guide to the key topics and subtopics covered in the Harvard University course on Artificial Intelligence, emphasizing algorithms, concepts, and practical applications.

## 1. Search Algorithms

### Search Problems

- **State Space Representation**: Understanding how to represent various states in a problem, defining states, actions, and transitions. For example, in a maze-solving problem, each position in the maze is a state, and moving up, down, left, or right are the possible actions.
- **Initial State, Actions, Goal State, and Path Cost**: Each component of search problems is critical for designing algorithms. For instance, in a GPS navigation system, the initial state is the current location, actions are possible routes, the goal state is the destination, and the path cost could be the distance or time taken.

### Uninformed Search Strategies

- **Depth-First Search (DFS)**:
  - **Implementation**: Recursive vs. iterative approaches to explore nodes. DFS is useful for problems like solving a maze where we need to explore all possible paths.
  - **Backtracking**: Handling dead ends by reverting to previous states. Example: Solving a Sudoku puzzle where an incorrect number placement is undone by backtracking.
- **Breadth-First Search (BFS)**:
  - **Queue Management**: Exploring nodes level by level using a queue. Example: Finding the shortest path in an unweighted graph like social network friend connections.
  - **Optimality**: BFS guarantees the shortest path in unweighted graphs.

### Informed Search Strategies

- **A\* Search**:
  - **Heuristic Design**: Creating effective heuristics that guide the search process efficiently. Example: In a chess game, a heuristic could be the estimated number of moves to checkmate.
  - **Cost Function**: Understanding the combined cost of movement and heuristic value to find optimal paths.
- **Greedy Best-First Search**:
  - **Heuristic Evaluation**: Selecting nodes based on the lowest heuristic estimate, though it may lead to non-optimal solutions. Example: A GPS system selecting roads based on the shortest straight-line distance instead of actual road conditions.

### Heuristics

- **Types of Heuristics**: Differentiating between admissible (never overestimates) and consistent heuristics.
- **Practical Examples**: Designing heuristics for real-world problems like pathfinding in mazes using Manhattan distance or Euclidean distance.

## 2. Knowledge Representation

### Propositional Logic

- **Syntax and Semantics**: Logical statements and their truth conditions. Example: "If it rains, the ground is wet."
- **Logical Inference**: Rules for deriving new facts from known premises, such as Modus Ponens: "If A implies B, and A is true, then B must be true."

### First-Order Logic

- **Quantifiers**: Use of universal and existential quantifiers to express statements. Example: "For all students, if they study, they pass the exam."
- **Predicate Logic**: Extending propositional logic to handle more complex relationships. Example: "John is a brother of Mary" can be represented as `Brother(John, Mary)`.

### Semantic Networks

- **Node and Edge Representation**: Graphical models that illustrate relationships between concepts. Example: A semantic network representing animals could have edges like "is a mammal" or "can fly."
- **Inference Mechanisms**: Drawing conclusions based on the structure of semantic networks, like understanding that a dog is a mammal because mammals are a broader category of animals.

## 3. Handling Uncertainty

### Probability Basics

- **Bayes’ Theorem**: Updating probabilities with new evidence to refine predictions. Example: Diagnosing a disease given a test result.
- **Independence and Conditional Probability**: Fundamental concepts for probabilistic reasoning.

### Bayesian Networks

- **Structure and Interpretation**: Representing joint probability distributions graphically. Example: A network predicting the likelihood of a car accident based on factors like weather and driver experience.
- **Inference in Bayesian Networks**: Techniques for calculating probabilities from the network.

### Markov Decision Processes (MDPs)

- **States, Actions, Rewards**: Defining components of MDPs for decision-making under uncertainty.
- **Value Functions**: Evaluating expected returns of states under specific policies.

## 4. Optimization

### Linear Programming

- **Formulating Problems**: Expressing optimization problems in linear form with constraints.
- **Simplex Method**: An algorithm for solving linear programming problems efficiently.

### Integer Programming

- **Branch and Bound**: Techniques for solving optimization problems with integer constraints.

### Genetic Algorithms

- **Selection, Crossover, Mutation**: Processes that drive evolutionary optimization, simulating natural selection.
- **Fitness Evaluation**: Assessing the effectiveness of candidate solutions based on defined criteria.

## 5. Machine Learning

### Supervised Learning

- **Regression Analysis**: Techniques for predicting continuous outcomes like house prices based on size and location.
- **Classification Algorithms**: Implementing decision trees, support vector machines (SVMs), and ensemble methods.

### Unsupervised Learning

- **Clustering Techniques**: Using K-means, hierarchical clustering, and DBSCAN to identify patterns in data.
- **Dimensionality Reduction**: Techniques like PCA and t-SNE for reducing feature space and visualizing data.

### Reinforcement Learning

- **Q-Learning**: Understanding value iteration and policy improvement for decision-making.
- **Markov Decision Processes in RL**: Applying MDPs to learn optimal policies through trial-and-error interactions.

### Neural Networks

- **Architecture**: Understanding layers, neurons, and activation functions.
- **Training Process**: Utilizing backpropagation and gradient descent for model training.
- **Perceptron**: How neural networks process input data and learn features through training.

## 6. Natural Language Processing (NLP)

### Tokenization and Preprocessing

- **Text Normalization**: Techniques for preparing text data, including lowercasing, stemming, and lemmatization.

### Part-of-Speech Tagging

- **Tagging Algorithms**: Using Hidden Markov Models and Conditional Random Fields for grammatical analysis.

### Named Entity Recognition (NER)

- **Entity Classification**: Identifying and categorizing key entities within text data.

### Sentiment Analysis

- **Lexicon-Based Approaches**: Using dictionaries to gauge sentiment from text.
- **Machine Learning Approaches**: Training classifiers to analyze and predict sentiment.

### Machine Translation

- **Statistical Machine Translation**: Early approaches using statistical models for language translation.
- **Neural Machine Translation**: Utilizing recurrent neural networks and transformers for improved translation quality.

## 7. Adversarial Search

### Minimax Algorithm

- **Utility Values**: Assigning numerical values to terminal states based on the game outcome.
- **Tree Representation**: Visualizing game states as a tree structure for decision-making.

### Alpha-Beta Pruning

- **Pruning Techniques**: Reducing the number of nodes evaluated in the Minimax tree to improve efficiency.

### Game Trees

- **Evaluating Moves**: Understanding how to assess multiple future game states to determine optimal strategies.

---

This expanded version provides explanations and examples for each topic, offering a deeper understanding of the AI concepts covered in the course.
