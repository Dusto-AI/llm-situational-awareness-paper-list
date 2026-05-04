# LLM Situational Awareness — Paper List

A curated bibliography of papers on **situational awareness in large language
models** — what models know about themselves, their context, and their place
in the world; how that knowledge is measured; and where it breaks down.

Maintained alongside ongoing thesis work. Updated as new papers land.

## About this list

- **Scope.** Situational awareness as understood in two traditions: classical
  SA from human factors (Endsley and successors) and the more recent AI safety
  framing (evaluation awareness, and self-knowledge). Adjacent literatures
  — agentic memory, theory of mind, anthropomorphism, evaluation methodology —
  are included where they directly inform the SA question.
- **Curation.** Selections are working notes from a thesis-in-progress, not an
  exhaustive survey. Some entries are foundational, some are recent and
  unsettled. The list reflects what I've found load-bearing — others may
  reasonably disagree.
- **Categories.** Twelve topical groupings, ordered roughly from foundations
  toward open problems.

Contributions welcome — see [CONTRIBUTING.md](CONTRIBUTING.md).


## Contents

- [Foundational SA and Human Factors](#foundational-sa-and-human-factors) — 14
- [AI Safety and SA](#ai-safety-and-sa) — 18
- [Evaluation Methodology and Critique](#evaluation-methodology-and-critique) — 8
- [Agentic AI, Failures, and Deployment](#agentic-ai-failures-and-deployment) — 5
- [LLM Capability Evaluation](#llm-capability-evaluation) — 10
- [Self-Knowledge, Introspection, and Metacognition](#self-knowledge-introspection-and-metacognition) — 15
- [Theory of Mind](#theory-of-mind) — 2
- [Memory and Scaffolding](#memory-and-scaffolding) — 10
- [Architectural Critiques and Formal Limits](#architectural-critiques-and-formal-limits) — 8
- [Anthropomorphism and Construct Transfer](#anthropomorphism-and-construct-transfer) — 2
- [Autonomy, Grounding, and Drift](#autonomy-grounding-and-drift) — 10
- [Parking Lot (not yet integrated, may be useful)](#parking-lot-not-yet-integrated-may-be-useful) — 17

## Foundational SA and Human Factors

- **Fang, R., et al. (2025).** A Systematic Review of Empirical Studies on Situation Awareness: Perspectives From the Interaction Among Humans, Machines, and the Task Environment. [[link]](https://pubmed.ncbi.nlm.nih.gov/40619647/)
- **Endsley, M. R. (2023).** Supporting Human-AI Teams: Transparency, explainability, and situation awareness. *Computers in Human Behavior*, 140, 107574. [[link]](https://doi.org/10.1016/j.chb.2022.107574)
- **Jiang, X., et al. (2022).** A Situation Awareness Perspective on Human-AI Interaction: Tensions and Opportunities. *International Journal of Human-Computer Interaction*. [[link]](https://www.tandfonline.com/doi/full/10.1080/10447318.2022.2093863)
- **Rastogi, C., et al. (2022).** Deciding Fast and Slow: The Role of Cognitive Biases in AI-assisted Decision-making. CMU/IBM. [[link]](https://arxiv.org/abs/2010.07938)
- **Endsley, M. R. (2015).** Situation Awareness Misconceptions and Misunderstandings. *Journal of Cognitive Engineering and Decision Making*, 9(1), 4-32. [[link]](https://doi.org/10.1177/1555343415572631)
- **Salmon, P. M., Stanton, N. A., Walker, G. H., & Jenkins, D. P. (2009).** *Distributed Situation Awareness: Theory, Measurement and Application to Teamwork*. Ashgate. [[link]](https://www.semanticscholar.org/paper/d31419a5e9254c34e2cae175f727c2c29a9a3187)
- **Stanton, N. A., Stewart, R., Harris, D., et al. (2006).** Distributed situation awareness in dynamic systems: theoretical development and application of an ergonomics methodology. *Ergonomics*, 49(12-13), 1288-1311. [[link]](https://doi.org/10.1080/00140130600612762)
- **Lee, J. D., & See, K. A. (2004).** Trust in automation: Designing for appropriate reliance. *Human Factors*, 46(1), 50-80. [[link]](https://doi.org/10.1518/hfes.46.1.50_30392)
- **Parasuraman, R., Sheridan, T. B., & Wickens, C. D. (2000).** A model for types and levels of human interaction with automation. *IEEE Transactions on Systems, Man, and Cybernetics*, 30(3), 286-297. [[link]](https://doi.org/10.1109/3468.844354)
- **Endsley, M. R. (1995).** Toward a Theory of Situation Awareness in Dynamic Systems. *Human Factors*, 37(1), 32-64. [[link]](https://doi.org/10.1518/001872095779049543)
- **Sarter, N. B., & Woods, D. D. (1995).** How in the World Did We Ever Get into That Mode? Mode Error and Awareness in Supervisory Control. *Human Factors*, 37(1), 5-19. [[link]](https://doi.org/10.1518/001872095779049516)
- **Vidulich, M. A., et al. (1994).** Situational Awareness: Papers and Annotated Bibliography. Armstrong Laboratory Technical Report. [[link]](https://doi.org/10.21236/ada284752)
- **R. M. Taylor (1990).** Situational Awareness Rating Technique (Sart): The Development of a Tool for Aircrew Systems Design. *AGARD Conference Proceedings No. 478*. [[link]](https://doi.org/10.4324/9781315087924-8)
- **Endsley, M. R. (1988).** Situation awareness global assessment technique (SAGAT). *Proceedings of the IEEE 1988 National Aerospace and Electronics Conference*, 789-795. [[link]](https://doi.org/10.1109/NAECON.1988.195097)

## AI Safety and SA

- **Sahoo, R., & Chaudhary, M. (2026).** Position: The Reasoning Trap -- Logical Reasoning as a Mechanistic Pathway to Situational Awareness. ICLR 2026 Workshop. [[link]](https://arxiv.org/abs/2603.09200)
- **Chaudhary, M., et al. (2025).** Evaluation Awareness Scales Predictably in Open-Weights Large Language Models. *arXiv preprint arXiv:2509.13333*. [[link]](https://arxiv.org/abs/2509.13333)
- **Korbak, T., Balesni, M., Shlegeris, B., & Irving, G. (2025).** How to evaluate control measures for LLM agents? *arXiv preprint arXiv:2504.05259*. [[link]](https://doi.org/10.48550/arXiv.2504.05259)
- **Korbak, T., Clymer, J., Hilton, B., Shlegeris, B., & Irving, G. (2025).** A sketch of an AI control safety case. *arXiv preprint arXiv:2501.17315*. [[link]](https://doi.org/10.48550/arXiv.2501.17315)
- **Needham, J., Edkins, G., Pimpale, G., Bartsch, H., & Hobbhahn, M. (2025).** Large Language Models Often Know When They Are Being Evaluated. *arXiv preprint arXiv:2505.23836*. [[link]](https://doi.org/10.48550/arXiv.2505.23836)
- **Nguyen, J., Hoang, K., Attubato, C. L., & Hofstätter, F. (2025).** Probing and Steering Evaluation Awareness of Language Models. *arXiv preprint arXiv:2507.01786*. [[link]](https://doi.org/10.48550/arXiv.2507.01786)
- **Phuong, M., Zimmermann, R. S., Wang, Z., et al. (2025).** Evaluating Frontier Models for Stealth and Situational Awareness. *arXiv preprint arXiv:2505.01420*. [[link]](https://doi.org/10.48550/arXiv.2505.01420)
- **Sheshadri, A., et al. (2025).** Why Do Some Language Models Fake Alignment While Others Don't? Anthropic. [[link]](https://arxiv.org/abs/2506.18032)
- **Xiaojian Li, Haoyuan Shi, Rongwu Xu, Wei Xu (2025).** AI Awareness. [[link]](https://arxiv.org/abs/2504.20084v1)
- **Balesni, M., et al. (2024).** Towards evaluations-based safety cases for AI scheming. *arXiv preprint arXiv:2411.03336*. [[link]](https://doi.org/10.48550/arXiv.2411.03336)
- **Bondarenko, A., et al. (2024).** Demonstrating specification gaming in reasoning models. [[link]](https://arxiv.org/abs/2502.13295)
- **Laine, R., Chughtai, B., Betley, J., et al. (2024).** Me, Myself, and AI: The Situational Awareness Dataset (SAD) for LLMs. [[link]](https://arxiv.org/abs/2407.04694)
- **Meinke, A., Schoen, B., Scheurer, J., Balesni, M., Shah, R., & Hobbhahn, M. (2024).** Frontier Models are Capable of In-context Scheming. [[link]](https://arxiv.org/abs/2412.04984)
- **Ngo, R., Chan, L., & Mindermann, S. (2024).** The alignment problem from a deep learning perspective. *arXiv preprint arXiv:2209.00626*. [[link]](https://doi.org/10.48550/arXiv.2209.00626)
- **Phuong, M., et al. (2024).** Evaluating Frontier Models for Dangerous Capabilities. *arXiv preprint arXiv:2403.13793*. [[link]](https://doi.org/10.48550/arXiv.2403.13793)
- **Berglund, L., Stickland, A. C., Balesni, M., et al. (2023).** Taken out of context: On measuring situational awareness in LLMs. *arXiv preprint arXiv:2309.00667*. [[link]](https://doi.org/10.48550/arXiv.2309.00667)
- **Ajeya Cotra (2022).** Without specific countermeasures, the easiest path to transformative AI likely leads to AI takeover. *AI Alignment Forum*. [[link]](https://www.lesswrong.com/posts/pRkFkzwKZ2zfa3R6H/without-specific-countermeasures-the-easiest-path-to)
- **Jiahai Feng, Stuart Russell, Jacob Steinhardt (n.d.).** Extractive Structures Learned in Pretraining Enable Generalization on Finetuned Facts. [[link]](https://arxiv.org/abs/2412.04614)

## Evaluation Methodology and Critique

- **Khalifa, M., et al. (2026).** Gaming the Judge: Unfaithful Chain-of-Thought Can Undermine Agent Evaluation. [[link]](https://arxiv.org/abs/2601.14691)
- **Marthe Ballon, Andres Algaba, Brecht Verbeken, Vincent Ginis (2026).** Benchmarks Saturate When The Model Gets Smarter Than The Judge. [[link]](https://arxiv.org/abs/2601.19532)
- **Gabriel Mukobi (2025).** Reasons to Doubt the Impact of AI Risk Evaluations. [[link]](https://arxiv.org/abs/2408.02565)
- **Hou, G., Zhang, W., Shen, Y., et al. (2025).** EgoSocialArena: Benchmarking the Social Intelligence of Large Language Models from a First-person Perspective. *arXiv preprint arXiv:2410.06195*. [[link]](https://doi.org/10.48550/arXiv.2410.06195)
- **Ibrahim, L., et al. (2025).** Multi-turn Evaluation of Anthropomorphic Behaviours in Large Language Models. Google DeepMind. [[link]](https://arxiv.org/abs/2502.07077)
- **Summerfield, C., et al. (2025).** Lessons from a Chimp: AI "Scheming" and the Quest for Ape Language. *arXiv preprint arXiv:2507.03409*. [[link]](https://doi.org/10.48550/arXiv.2507.03409)
- **Sypherd, C., Tang, W., & Belle, V. (2025).** Breaking the Illusion: Revisiting LLM anthropomorphism. [[link]](https://www.pure.ed.ac.uk/ws/portalfiles/portal/556462843/SypherdEtalHAR2025BreakingtheIllusion.pdf)
- **Tang, G., Chu, Z., Zheng, W., Liu, M., & Qin, B. (2024).** Towards Benchmarking Situational Awareness of Large Language Models. *Findings of the Association for Computational Linguistics: EMNLP 2024*, 7904-7928. [[link]](https://doi.org/10.18653/v1/2024.findings-emnlp.464)

## Agentic AI, Failures, and Deployment

- **AI Digest. (2026).** What did we learn from the AI Village in 2025? [[link]](https://theaidigest.org/village/blog/what-we-learned-2025)
- **Bryan, P., et al. (2025).** Taxonomy of Failure Mode in Agentic AI Systems. Microsoft. [[link]](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/final/en-us/microsoft-brand/documents/Taxonomy-of-Failure-Mode-in-Agentic-AI-Systems-Whitepaper.pdf)
- **Pipis, C., et al. (2025).** Wait, Wait, Wait... Why Do Reasoning Models Loop? MIT/Microsoft. [[link]](https://arxiv.org/abs/2512.12895)
- **Reid, A., O'Callaghan, S., Carroll, L., & Caetano, T. (2025).** Risk analysis techniques for governed LLM-based multi-agent systems. *arXiv preprint arXiv:2508.05687*. [[link]](https://arxiv.org/abs/2508.05687)
- **Park, P. S., Goldstein, S., O'Gara, A., Chen, M., & Hendrycks, D. (2024).** AI deception: A survey of examples, risks, and potential solutions. *Patterns*, 5(5), 100988. [[link]](https://doi.org/10.1016/j.patter.2024.100988)

## LLM Capability Evaluation

- **Liv G. d'Aliberti, Manoel Horta Ribeiro (2026).** The Illusion of Insight in Reasoning Language Models. Princeton. [[link]](https://arxiv.org/abs/2601.00514)
- **Bogdan, O., et al. (2025).** Thought Anchors: Which LLM Reasoning Steps Matter? *arXiv preprint arXiv:2506.19143*. [[link]](https://arxiv.org/abs/2506.19143)
- **Ezra, E., Weizman, A., & Azaria, A. (2025).** The Self-Execution Benchmark: Measuring LLMs' Attempts to Overcome Their Lack of Self-Execution. *arXiv preprint arXiv:2508.12277*. [[link]](https://doi.org/10.48550/arXiv.2508.12277)
- **Fu, Y., et al. (2025).** AbsenceBench: Language Models Can't Tell What's Missing. *arXiv preprint arXiv:2506.11440*. [[link]](https://arxiv.org/abs/2506.11440)
- **Hagendorff, T., & Fabi, S. (2025).** Beyond Chains of Thought: Benchmarking Latent-Space Reasoning Abilities in Large Language Models. [[link]](https://arxiv.org/abs/2504.10615)
- **Kirichenko, P., et al. (2025).** AbstentionBench: Reasoning LLMs Fail on Unanswerable Questions. *arXiv preprint arXiv:2506.09038*. [[link]](https://arxiv.org/abs/2506.09038)
- **Lan Pan, Hanbo Xie, Robert C. Wilson (2025).** Large Language Models Think Too Fast To Explore Effectively. Georgia Tech. [[link]](https://arxiv.org/abs/2501.18009)
- **Li, B., & Andreas, J. (2025).** (How) Do Language Models Track State? [[link]](https://arxiv.org/abs/2503.02854)
- **Sharma, M., et al. (2025).** Towards Understanding Sycophancy in Language Models. *arXiv preprint arXiv:2310.13548*. [[link]](https://arxiv.org/abs/2310.13548)
- **Wenbo Zhang, Zihang Xu, Hengrui Cai (2024).** Defining Boundaries: A Spectrum of Task Feasibility for Large Language Models. [[link]](https://arxiv.org/abs/2408.05873v1)

## Self-Knowledge, Introspection, and Metacognition

- **Christina Lu, Jack Gallagher, Jonathan Michala, Kyle Fish, Jack Lindsey (2026).** The Assistant Axis: Situating and Stabilizing the Default Persona of Language Models. Anthropic. [[link]](https://arxiv.org/abs/2601.10387)
- **Ackerman, C. (2025).** Evidence for Limited Metacognition in LLMs. *arXiv preprint arXiv:2509.21545*. [[link]](https://arxiv.org/abs/2509.21545)
- **Betley, J., Bao, X., Soto, M., Sztyber-Betley, A., Chua, J., & Evans, O. (2025).** Tell me about yourself: LLMs are aware of their learned behaviors. *arXiv preprint arXiv:2501.11120*. [[link]](https://doi.org/10.48550/arXiv.2501.11120)
- **Cheang, C., et al (2025).** Do LLMs Really Know What They Don't Know? Internal States Mainly Reflect Knowledge Recall Rather Than Truthfulness. [[link]](https://arxiv.org/abs/2510.09033)
- **Eric Bigelow, Zergham Ahmed, Tomer Ullman (2025).** Evaluating Self-Orienting in Language and Reasoning Models. [[link]](https://icml.cc/virtual/2025/49124)
- **Keheng Wang, Feiyu Duan, Peiguang Li, Sirui Wang, Xunliang Cai (2025).** LLMs Know What They Need: Leveraging a Missing Information Guided Framework to Empower Retrieval-Augmented Generation. [[link]](https://arxiv.org/abs/2404.14043)
- **Li Ji-An, Xiong, H.-D., Wilson, R. C., Mattar, M. G., & Benna, M. K. (2025).** Language Models Are Capable of Metacognitive Monitoring and Control of Their Internal Activations. *arXiv preprint arXiv:2505.13763*. [[link]](https://arxiv.org/abs/2505.13763)
- **Manvi, R., Hong, J., Seyde, T., Labonne, M., Lechner, M., Levine, S. (2025).** Zero-Overhead Introspection for Adaptive Test-Time Compute. [[link]](https://arxiv.org/abs/2512.01457v3)
- **Qiao, S., et al. (2025).** Agentic Knowledgeable Self-awareness. ACL 2025. [[link]](https://arxiv.org/abs/2504.03553)
- **Struber, J., Auzina, I., Goel, S., Keller, S., Geiping, J., Prabhu, A., Bethge, M. (2025).** Measuring Belief Updates in Curious Agents. [[link]](https://openreview.net/forum?id=vIddey7z1I)
- **Younwoo Choi, Changling Li, Yongjin Yang, Zhijing Jin (2025).** Agent-to-Agent Theory of Mind: Testing Interlocutor Awareness among Large Language Models. [[link]](https://arxiv.org/abs/2506.22957)
- **Ziyang Ma, Qingyue Yuan, Zhenglin Wang, Deyu Zhou (2025).** Large Language Models Have Intrinsic Meta-Cognition, but Need a Good Lens. [[link]](https://arxiv.org/abs/2506.08410)
- **Chen, D., Shi, J., Wan, Y., Zhou, P., Gong, N. Z., & Sun, L. (2024).** Self-Cognition in Large Language Models: An Exploratory Study. *arXiv preprint arXiv:2407.01505*. [[link]](https://doi.org/10.48550/arXiv.2407.01505)
- **Prato, G., et al. (2024).** Do Large Language Models Know How Much They Know? [[link]](https://arxiv.org/abs/2502.19573)
- **Suzgum, M., et al. (2024).** Belief in the Machine: Investigating Epistemological Blind Spots of Language Models. Stanford. [[link]](https://arxiv.org/abs/2410.21195)

## Theory of Mind

- **Gu, Y., et al. (2026).** SimpleToM: Exposing the Gap between Explicit ToM Inference and Implicit ToM Application in LLMs. ICLR 2026. [[link]](https://arxiv.org/abs/2410.13648)
- **Jared Moore, Ned Cooper, Rasmus Overmark, Beba Cibralic, Nick Haber, Cameron Jones (2025).** Do Large Language Models Have a Planning Theory of Mind? Evidence from MindGames: a Multi-Step Persuasion Task. (MindGames). [[link]](https://arxiv.org/abs/2507.16196)

## Memory and Scaffolding

- **Yang, Z., et al. (2026).** PlugMem: Task-Agnostic Plugin Memory Module for LLM Agents. UIUC/Microsoft. [[link]](https://arxiv.org/abs/2603.03296)
- **Yu, Y., et al. (2026).** Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for Large Language Model Agents. Alibaba. [[link]](https://arxiv.org/abs/2601.01885)
- **Chhikara, P., et al. (2025).** Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory. [[link]](https://arxiv.org/abs/2504.19413)
- **Cross, L., Haber, N., et al. (2025).** Hypothetical Minds: Scaffolding Theory of Mind for Multi-Agent Tasks. ICLR 2025. [[link]](https://arxiv.org/abs/2407.07086)
- **Du, Y., et al. (2025).** Rethinking Memory in AI: Taxonomy, Operations, Topics, and Future Directions. [[link]](https://arxiv.org/abs/2505.00675v1)
- **Fountas, Z., et al. (2025).** Human-inspired Episodic Memory for Infinite Context LLMs. ICLR 2025. [[link]](https://arxiv.org/abs/2407.09450)
- **Guo, S., et al. (2025).** World Modelling Improves Language Model Agents. [[link]](https://arxiv.org/abs/2506.02918)
- **Hu, Y., et al. (2025).** Memory in the Age of AI Agents. [[link]](https://arxiv.org/abs/2512.13564)
- **Tao An (2025).** Cognitive Workspace: Active Memory Management for LLMs -- An Empirical Study of Functional Infinite Context. [[link]](https://arxiv.org/abs/2508.13171v1)
- **Xu, Y., et al. (2025).** A-MEM: Agentic Memory for LLM Agents. [[link]](https://arxiv.org/abs/2502.12110)

## Architectural Critiques and Formal Limits

- **Elija Perrier, Michael Timothy Bennett (2025).** Position: Stop Acting Like Language Model Agents Are Normal Agents. [[link]](https://arxiv.org/abs/2502.10420)
- **Kalai, A. T., et al. (2025).** Why Language Models Hallucinate. OpenAI. [[link]](https://arxiv.org/abs/2509.04664)
- **Sara Hooker (2025).** On the Slow Death of Scaling. Cohere. [[link]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5877662)
- **Wang, K., & Nanda, N. (2025).** Simple Mechanistic Explanations for Out-of-Context Reasoning. MIT. [[link]](https://arxiv.org/abs/2507.08218)
- **Xu, Z., & Kankanhalli, M. (2025).** Hallucination is Inevitable: An Innate Limitation of Large Language Models. NUS. [[link]](https://arxiv.org/abs/2401.11817)
- **M. Shanahan (2022).** Talking about Large Language Models. *Communications of the ACM*, 67(2), 68-79. [[link]](https://arxiv.org/abs/2212.03551)
- **Kambhampati, S., et al. (various).** LLMs Can't Plan, But Can Help Planning in LLM-Modulo Frameworks. [[link]](https://arxiv.org/abs/2402.01817)
- **Yann LeCun (various).** A Path Towards Autonomous Machine Intelligence. [[link]](https://openreview.net/pdf?id=BZ5a1r-kVsf)

## Anthropomorphism and Construct Transfer

- **Henry Shevlin (2026).** Three frameworks for AI mentality. [[link]](https://doi.org/10.3389/fpsyg.2026.1715835)
- **Raj Sanjay Shah, Sashank Varma (2025).** The potential -- and the pitfalls -- of using pre-trained language models as cognitive science theories. Georgia Tech. [[link]](https://arxiv.org/abs/2501.12651)

## Autonomy, Grounding, and Drift

- **Huang, J. Y., Choshen, L., Astudillo, R., Broderick, T., & Andreas, J. (2026).** Do LLMs Benefit from Their Own Words? *arXiv preprint arXiv:2602.24287*. [[link]](https://arxiv.org/abs/2602.24287)
- **Rath, A. (2026).** Agent Drift: Quantifying Behavioral Degradation in Multi-Agent LLM Systems Over Extended Interactions. *arXiv preprint arXiv:2601.04170*. [[link]](https://arxiv.org/abs/2601.04170)
- **Casey O. Barkan, Sid Black, Oliver Sourbut (2025).** Do Large Language Models Know What They Are Capable Of? *arXiv preprint arXiv:2512.24661*. [[link]](https://arxiv.org/abs/2512.24661)
- **Feng, K. J. K., McDonald, D. W., & Zhang, A. X. (2025).** Levels of Autonomy for AI Agents. *arXiv preprint arXiv:2506.12469*. [[link]](https://arxiv.org/abs/2506.12469)
- **Lin, X., et al. (2025).** LLM-based Agents Suffer from Hallucinations: A Survey. *arXiv preprint arXiv:2509.18970*. [[link]](https://arxiv.org/abs/2509.18970)
- **Max Heitmann, Ture Hinrichsen, David Africa, Jonas Sandbrink (2025).** Understanding AI Trajectories: Mapping the Limitations of Current AI Systems. UK AISI. [[link]](https://www.aisi.gov.uk/research/understanding-ai-trajectories-mapping-the-limitations-of-current-ai-systems)
- **Ziming Luo, Atoosa Kasirzadeh, Nihar B. Shah (2025).** The More You Automate, the Less You See: Hidden Pitfalls of AI Scientist Systems. CMU. [[link]](https://arxiv.org/abs/2509.08713)
- **Shumailov, I., Shumaylov, Z., Zhao, Y., Gal, Y., Papernot, N., & Anderson, R. (2024).** AI models collapse when trained on recursively generated data. *Nature*, 631, 755-759. [[link]](https://doi.org/10.1038/s41586-024-07566-y)
- **Alemohammad, S., et al. (2023).** Self-Consuming Generative Models Go MAD. *NeurIPS 2023*. arXiv:2307.01850. [[link]](https://arxiv.org/abs/2307.01850)
- **Zhang, M., Press, O., Merrill, W., Liu, A., & Smith, N. A. (2023).** How Language Model Hallucinations Can Snowball. *arXiv preprint arXiv:2305.13534*. ICML 2024. [[link]](https://arxiv.org/abs/2305.13534)

## Parking Lot (not yet integrated, may be useful)

- **Elenjical, T., Kavuri, S., & Varma, V. (2026).** Think2: Grounded Metacognitive Reasoning in Large Language Models. *arXiv preprint arXiv:2602.18806*. [[link]](https://arxiv.org/abs/2602.18806)
- **Ahmed, N., et al. (2025).** Do LLMs Know They Are Being Tested? Evaluation Awareness and Incentive-Sensitive Failures in GPT-OSS-20B. *arXiv preprint arXiv:2510.08624*. [[link]](https://arxiv.org/abs/2510.08624)
- **Betley, J., et al. (2025).** Emergent Misalignment: Narrow finetuning can produce broadly misaligned LLMs. *arXiv preprint arXiv:2502.17424*. [[link]](https://arxiv.org/abs/2502.17424)
- **Cintas, C., et al. (2025).** Localizing Persona Representations in LLMs. *arXiv preprint arXiv:2505.24539*. [[link]](https://arxiv.org/abs/2505.24539)
- **Comsa, I. M., & Shanahan, M. (2025).** Does It Make Sense to Speak of Introspection in Large Language Models? *arXiv preprint arXiv:2506.05068*. [[link]](https://arxiv.org/abs/2506.05068)
- **Imran, S., Lamb, R., & Atkinson, P. M. (2025).** Out-of-Context Abduction: LLMs Make Inferences About Procedural Data Leveraging Declarative Facts in Earlier Training Data. *arXiv preprint arXiv:2508.00741*. [[link]](https://arxiv.org/abs/2508.00741)
- **Kumaran, S., et al. (2025).** How Overconfidence in Initial Choices and Underconfidence Under Criticism Modulate Change of Mind in LLMs. *arXiv preprint arXiv:2507.03120*. [[link]](https://arxiv.org/abs/2507.03120)
- **Mallen, A., et al. (2025).** Subversion Strategy Eval: Can language models statelessly strategize to subvert control protocols? *arXiv preprint arXiv:2412.12480*. [[link]](https://arxiv.org/abs/2412.12480)
- **Sharkey, L., et al. (2025).** Open Problems in Mechanistic Interpretability. *arXiv preprint arXiv:2501.16496*. [[link]](https://arxiv.org/abs/2501.16496)
- **Shen, G., et al. (2025).** From Poisoned to Aware: Fostering Backdoor Self-Awareness in LLMs. *arXiv preprint arXiv:2510.05169*. [[link]](https://arxiv.org/abs/2510.05169)
- **Sühr, T., et al. (2025).** Stop Evaluating AI with Human Tests, Develop Principled, AI-specific Tests instead. *arXiv preprint arXiv:2507.23009*. [[link]](https://arxiv.org/abs/2507.23009)
- **Tian Hua, T., Qin, A., Marks, S., & Nanda, N. (2025).** Steering Evaluation-Aware Language Models to Act Like They Are Deployed. *arXiv preprint arXiv:2510.20487*. [[link]](https://arxiv.org/abs/2510.20487)
- **Binder, F. J., et al. (2024).** Looking Inward: Language Models Can Learn About Themselves by Introspection. *arXiv preprint arXiv:2410.13787*. [[link]](https://arxiv.org/abs/2410.13787)
- **Panickssery, A., Bowman, S. R., & Feng, S. (2024).** LLM Evaluators Recognize and Favor Their Own Generations. [[link]](https://arxiv.org/abs/2404.13076)
- **Perez, E., et al. (2023).** Discovering Language Model Behaviors with Model-Written Evaluations. *Findings of ACL 2023*, 13387-13434. [[link]](https://arxiv.org/abs/2212.09251)
- **Sanneman, L., & Shah, J. A. (2022).** The Situation Awareness Framework for Explainable AI (SAFE-AI) and Human Factors Considerations for XAI Systems. *International Journal of Human-Computer Interaction*, 38(18-20), 1772-1788. [[link]](https://www.tandfonline.com/doi/full/10.1080/10447318.2022.2081282)
- **Flavell, J. H. (1979).** Metacognition and cognitive monitoring: A new area of cognitive–developmental inquiry.. *American Psychologist*, 34(10), 906-911. [[link]](https://psycnet.apa.org/record/1980-09388-001)

*This list contains 119 entries across 12 categories.*


## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Pull requests welcome for new papers,
corrections, or category suggestions.

## License

- Code (parsers, generators): [MIT](LICENSE)
- Curated list: [CC-BY-4.0](LIST_LICENSE)

---

*Last updated 2026-05-05. Generated from the maintainer's working bibliography.*
