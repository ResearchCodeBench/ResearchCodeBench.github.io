---
title: "Paper2Code: Measuring Language Models' Capacity to Implement Novel Machine Learning Research Ideas"
description: "Evaluating Large Language Models' Ability to Implement Novel Machine Learning Research"
---


# Paper2Code-bench: Evaluating Large Language Models' Ability to Implement Novel Machine Learning Research




TL;DR


Large language models (LLMs) have demonstrated significant promise in machine learning research; however, their ability to implement genuinely novel ideas from recent academic papers remains uncertain. To address this gap, we introduce Paper2Code, a coding benchmark designed to evaluate LLMs on their capability to translate concepts from top-tier conference papers into executable code.

To this end, we introduce Paper2Code-bench, an evaluation benchmark consisting of 1,000 coding challenges with varying levels of difficulty. These challenges have been curated from 20 recent machine learning papers accepted at top ML conferences or recent arXiv submissions from the past year, with 800f the papers published within the last six months. For each challenge, the LLM is provided with the original research paper and a scaffold of its corresponding codebase. The model is then tasked with implementing the core contributions described in the paper. Each solution is rigorously evaluated using comprehensive tests againt the original code written by the authors.

Solving these challenges is nontrivial, requiring models to keep up with recent innovations in AI, maintain long-horizon reasoning about research papers, and possess the coding capability to translate these complex ideas into executable code. We show that models perform well when completing the shorter version of the questions while failes dramatically when the dificult increases to the function level.

 Progress on Paper2Code-bench marks a significant step toward creating AI systems capable of supporting AI researchers and advancing the broader scientific community.



Github Repo
Leaderboard
How to contribute to the Benchmark?