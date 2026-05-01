# LLM Situational Awareness — Paper List

A curated bibliography of papers on **situational awareness in large language
models** — what models know about themselves, their context, and their place
in the world; how that knowledge is measured; and where it breaks down.

Maintained alongside ongoing thesis work. Updated as new papers land.

## About this list

- **Scope.** Situational awareness as understood in two traditions: classical
  SA from human factors (Endsley and successors) and the more recent AI safety
  framing (evaluation awareness, self-knowledge, scheming). Adjacent literatures
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

- [Foundational SA and Human Factors](#foundational-sa-and-human-factors) — 15
- [AI Safety and SA](#ai-safety-and-sa) — 19
- [Evaluation Methodology and Critique](#evaluation-methodology-and-critique) — 8
- [Agentic AI, Failures, and Deployment](#agentic-ai-failures-and-deployment) — 6
- [LLM Capability Evaluation](#llm-capability-evaluation) — 10
- [Self-Knowledge, Introspection, and Metacognition](#self-knowledge-introspection-and-metacognition) — 15
- [Theory of Mind](#theory-of-mind) — 2
- [Memory and Scaffolding](#memory-and-scaffolding) — 10
- [Architectural Critiques and Formal Limits](#architectural-critiques-and-formal-limits) — 8
- [Anthropomorphism and Construct Transfer](#anthropomorphism-and-construct-transfer) — 2
- [Autonomy, Grounding, and Drift](#autonomy-grounding-and-drift) — 11
- [Parking Lot (not yet integrated, may be useful)](#parking-lot-not-yet-integrated-may-be-useful) — 17

## Foundational SA and Human Factors

- **Endsley, M. R. (1988).** [Situation awareness global assessment technique (SAGAT)](https://doi.org/10.1109/NAECON.1988.195097). *Proceedings of the IEEE 1988 National Aerospace and Electronics Conference*, 789-795.
- **Endsley, M. R. (1995).** [Toward a Theory of Situation Awareness in Dynamic Systems](https://doi.org/10.1518/001872095779049543). *Human Factors*, 37(1), 32-64.
- **Endsley, M. R. (2015).** [Situation Awareness Misconceptions and Misunderstandings](https://doi.org/10.1177/1555343415572631). *Journal of Cognitive Engineering and Decision Making*, 9(1), 4-32.
- **Endsley, M. R. (2023).** [Supporting Human-AI Teams: Transparency, explainability, and situation awareness](https://doi.org/10.1016/j.chb.2022.107574). *Computers in Human Behavior*, 140, 107574.
- **Fang, Y., et al. (2025).** Systematic review of 2,860 SA studies across 11 fields.
- **Jiang, X., & Beringer, D. (2022).** SA perspective on human-AI interaction. *International Journal of Human-Computer Interaction*.
- **Lee, J. D., & See, K. A. (2004).** Trust in automation: Designing for appropriate reliance. *Human Factors*, 46(1), 50-80.
- **Parasuraman, R., Sheridan, T. B., & Wickens, C. D. (2000).** A model for types and levels of human interaction with automation. *IEEE Transactions on Systems, Man, and Cybernetics*, 30(3), 286-297.
- **Rastogi, C., et al. (2022).** Cognitive Biases in AI-Assisted Decision Making. CMU/IBM.
- *(reference note)* SA Recovery literature: see Endsley (2015); also PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC4753990/
- **Salmon, P. M., Stanton, N. A., Walker, G. H., & Jenkins, D. P. (2009).** *Distributed Situation Awareness: Theory, Measurement and Application to Teamwork*. Ashgate.
- **Sarter, N. B., & Woods, D. D. (1995).** How in the World Did We Ever Get into That Mode? Mode Error and Awareness in Supervisory Control. *Human Factors*, 37(1), 5-19.
- **Stanton, N. A., Stewart, R., Harris, D., et al. (2006).** Distributed situation awareness in dynamic systems: theoretical development and application of an ergonomics methodology. *Ergonomics*, 49(12-13), 1288-1311.
- **Taylor, R. M. (1990).** Situational Awareness Rating Technique (SART): The development of a tool for aircrew systems design. *AGARD Conference Proceedings No. 478*.
- **Vidulich, M. A., et al. (1994).** Situational Awareness: Papers and Annotated Bibliography. Armstrong Laboratory Technical Report.

## AI Safety and SA

- **Balesni, M., et al. (2024).** [Towards evaluations-based safety cases for AI scheming](https://doi.org/10.48550/arXiv.2411.03336). *arXiv preprint arXiv:2411.03336*.
- **Berglund, L., Stickland, A. C., Balesni, M., et al. (2023).** [Taken out of context: On measuring situational awareness in LLMs](https://doi.org/10.48550/arXiv.2309.00667). *arXiv preprint arXiv:2309.00667*.
- **Bondarenko, Y., et al. (2024).** Spec-Gaming in LLMs.
- **Chaudhary, M., et al. (2025).** Evaluation Awareness Scales Predictably in Open-Weights LLMs. *arXiv preprint arXiv:2509.13333*.
- **Cotra, A. (2022).** Without specific countermeasures, the easiest path to transformative AI likely leads to AI takeover. *AI Alignment Forum*.
- **Feng, J., Russell, S., & Steinhardt, J. (n.d.).** How do language models generalize to implications of facts they are trained on?
- **Korbak, T., Balesni, M., Shlegeris, B., & Irving, G. (2025).** [How to evaluate control measures for LLM agents?](https://doi.org/10.48550/arXiv.2504.05259) *arXiv preprint arXiv:2504.05259*.
- **Korbak, T., Clymer, J., Hilton, B., Shlegeris, B., & Irving, G. (2025).** [A sketch of an AI control safety case](https://doi.org/10.48550/arXiv.2501.17315). *arXiv preprint arXiv:2501.17315*.
- **Laine, R., Chughtai, B., Betley, J., et al. (2024).** Me, Myself, and AI: The Situational Awareness Dataset (SAD) for LLMs.
- **Li, Y., & Xu, K. (2025).** AI Awareness: Self-awareness, situational awareness, and social awareness taxonomy.
- **Meinke, A., Schoen, B., Scheurer, J., Balesni, M., Shah, R., & Hobbhahn, M. (2024).** Frontier Models are Capable of In-context Scheming.
- **Needham, J., Edkins, G., Pimpale, G., Bartsch, H., & Hobbhahn, M. (2025).** [Large Language Models Often Know When They Are Being Evaluated](https://doi.org/10.48550/arXiv.2505.23836). *arXiv preprint arXiv:2505.23836*.
- **Ngo, R., Chan, L., & Mindermann, S. (2024).** [The alignment problem from a deep learning perspective](https://doi.org/10.48550/arXiv.2209.00626). *arXiv preprint arXiv:2209.00626*.
- **Nguyen, J., Hoang, K., Attubato, C. L., & Hofstätter, F. (2025).** [Probing and Steering Evaluation Awareness of Language Models](https://doi.org/10.48550/arXiv.2507.01786). *arXiv preprint arXiv:2507.01786*.
- **Phuong, M., et al. (2024).** [Evaluating Frontier Models for Dangerous Capabilities](https://doi.org/10.48550/arXiv.2403.13793). *arXiv preprint arXiv:2403.13793*.
- **Phuong, M., Zimmermann, R. S., Wang, Z., et al. (2025).** [Evaluating Frontier Models for Stealth and Situational Awareness](https://doi.org/10.48550/arXiv.2505.01420). *arXiv preprint arXiv:2505.01420*.
- **Sahoo, R., & Chaudhary, M. (2026).** Position: The Reasoning Trap -- Logical Reasoning as a Mechanistic Pathway to Situational Awareness. ICLR 2026 Workshop.
- **Sheshadri, A., et al. (2025).** Why Do Some LLMs Fake Alignment? Anthropic.
- **Tran, D., & Jarviniemi, A. (2024).** SA-informed deception varies with CoT privacy.

## Evaluation Methodology and Critique

- **Ballon, B., & Ginis, P. (2026).** Benchmark Saturation When Model Surpasses the Judge.
- **Hou, G., Zhang, W., Shen, Y., et al. (2025).** [EgoSocialArena: Benchmarking the Social Intelligence of Large Language Models from a First-person Perspective](https://doi.org/10.48550/arXiv.2410.06195). *arXiv preprint arXiv:2410.06195*.
- **Ibrahim, L., et al. (2025).** Evaluation of Anthropomorphic Behaviour in LLMs. Google DeepMind.
- **Khalifa, M., et al. (2026).** Gaming the Judge: Unfaithful CoT in Agent Evaluation.
- **Mukobi, G. (2025).** Reasons to Doubt AI Risk Evaluations.
- **Summerfield, C., et al. (2025).** [Lessons from a Chimp: AI "Scheming" and the Quest for Ape Language](https://doi.org/10.48550/arXiv.2507.03409). *arXiv preprint arXiv:2507.03409*.
- **Sypherd, C., Tang, W., & Belle, V. (n.d.).** Breaking the Illusion: Revisiting LLM Anthropomorphism.
- **Tang, G., Chu, Z., Zheng, W., Liu, M., & Qin, B. (2024).** [Towards Benchmarking Situational Awareness of Large Language Models](https://doi.org/10.18653/v1/2024.findings-emnlp.464). *Findings of the Association for Computational Linguistics: EMNLP 2024*, 7904-7928.

## Agentic AI, Failures, and Deployment

- **AI Digest. (2026).** [What did we learn from the AI Village in 2025?](https://theaidigest.org/village/blog/what-we-learned-2025)
- **Bryan, C., et al. (2025).** Taxonomy of Failure Modes in Agentic AI. Microsoft.
- **Luo, J., & Shah, S. (2025).** The More You Automate, the Less You See. CMU.
- **Park, P. S., Goldstein, S., O'Gara, A., Chen, M., & Hendrycks, D. (2024).** [AI deception: A survey of examples, risks, and potential solutions](https://doi.org/10.1016/j.patter.2024.100988). *Patterns*, 5(5), 100988.
- **Pipis, K., et al. (2025).** Why Do Reasoning Language Models Loop? MIT/Microsoft.
- **Reid, A., O'Callaghan, S., Carroll, L., & Caetano, T. (2025).** Risk analysis techniques for governed LLM-based multi-agent systems. *arXiv preprint arXiv:2508.05687*.

## LLM Capability Evaluation

- **Bogdan, O., et al. (2025).** Thought Anchors: Which LLM Reasoning Steps Matter? *arXiv preprint arXiv:2506.19143*.
- **D'Aliberti, J., et al. (2026).** The Illusion of Insight in Reasoning Language Models. Princeton.
- **Ezra, E., Weizman, A., & Azaria, A. (2025).** [The Self-Execution Benchmark: Measuring LLMs' Attempts to Overcome Their Lack of Self-Execution](https://doi.org/10.48550/arXiv.2508.12277). *arXiv preprint arXiv:2508.12277*.
- **Fu, Y., et al. (2025).** AbsenceBench: Language Models Can't Tell What's Missing. *arXiv preprint arXiv:2506.11440*.
- **Hagendorff, T., & Fabi, S. (2025).** Beyond Chains of Thought: Benchmarking Latent-Space Reasoning Abilities in Large Language Models.
- **Kirichenko, P., et al. (2025).** AbstentionBench: Reasoning LLMs Fail on Unanswerable Questions. *arXiv preprint arXiv:2506.09038*.
- **Li, B., & Andreas, J. (2025).** (How) Do Language Models Track State?
- **Pan, L., & Wilson, R. C. (2025).** LLMs Think Too Fast. Georgia Tech.
- **Sharma, M., et al. (2025).** Towards Understanding Sycophancy in Language Models. *arXiv preprint arXiv:2310.13548*.
- **Zhang, Z., & Cai, Y. (2024).** Defining Boundaries: A Spectrum of Task Feasibility for LLMs.

## Self-Knowledge, Introspection, and Metacognition

- **Ackerman, C. (2025).** Evidence for Limited Metacognition in LLMs. *arXiv preprint arXiv:2509.21545*.
- **Betley, J., Bao, X., Soto, M., Sztyber-Betley, A., Chua, J., & Evans, O. (2025).** [Tell me about yourself: LLMs are aware of their learned behaviors](https://doi.org/10.48550/arXiv.2501.11120). *arXiv preprint arXiv:2501.11120*.
- **Bigelow, E., & Ullman, T. (2025).** Evaluating Self-Orienting in LLMs.
- **Cheang, B., & Deng, J. (2025).** Large Language Models Do NOT Really Know What They Don't Know.
- **Chen, D., Shi, J., Wan, Y., Zhou, P., Gong, N. Z., & Sun, L. (2024).** [Self-Cognition in Large Language Models: An Exploratory Study](https://doi.org/10.48550/arXiv.2407.01505). *arXiv preprint arXiv:2407.01505*.
- **Choi, J., & Jin, Y. (2025).** Agent-to-Agent Theory of Mind.
- **Li Ji-An, Xiong, H.-D., Wilson, R. C., Mattar, M. G., & Benna, M. K. (2025).** Language Models Are Capable of Metacognitive Monitoring and Control of Their Internal Activations. *arXiv preprint arXiv:2505.13763*.
- **Lu, S., & Lindsey, J. (2026).** The Assistant Axis. Anthropic.
- **Ma, Y., & Zhou, J. (2025).** Large Language Models Have Intrinsic Meta-Cognition.
- **Manvi, R., & Levine, S. (2025).** Zero-Overhead Introspection.
- **Prato, G., et al. (2024).** Do Large Language Models Know How Much They Know?
- **Qiao, S., et al. (2025).** KnowSelf: Agentic Knowledgeable Self-awareness. ACL 2025.
- **Struber, S., & Bethge, M. (2025).** Measuring Belief Updates in Curious Agents.
- **Suzgun, M., & Zou, J. (2024).** Epistemological Blind Spots in LLMs. Stanford.
- **Wang, Z., & Cai, D. (2025).** LLMs Know What They Need.

## Theory of Mind

- **Gu, Y., Tafjord, O., Kim, H., Moore, J., Le Bras, R., Clark, P., & Choi, Y. (2026).** SimpleTOM: Exposing the Gap Between Explicit ToM Inference and Implicit ToM Application in LLMs. ICLR 2026.
- **Moore, J. W., & Jones, E. (2025).** Do Large Language Models Have a Planning Theory of Mind? (MindGames).

## Memory and Scaffolding

- **An, B., et al. (2025).** Cognitive Workspace: Baddeley-Inspired Active Memory with Metacognitive Awareness.
- **Chhikara, P., et al. (2025).** Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory.
- **Cross, L., Haber, N., et al. (2025).** Hypothetical Minds: Scaffolding Theory of Mind for Multi-Agent Tasks. ICLR 2025.
- **Du Pan, K., et al. (2025).** Rethinking Memory in AI: Taxonomy, Operations, and Benchmarks.
- **Fountas, Z., et al. (2025).** EM-LLM: Human-Inspired Episodic Memory for LLM Agents. ICLR 2025.
- **Guo, Z., et al. (2025).** DyMo: Dynamic World Modeling via Next-State Prediction for Agents.
- **Hu, S., & Yan, L. (2025).** Memory in the Age of AI Agents: Forms, Functions, and Dynamics.
- **Xu, Y., et al. (2025).** A-MEM: Agentic Memory for LLM Agents.
- **Yang, Z., et al. (2026).** PlugMem: Task-Agnostic Plugin Memory Module for LLM Agents. UIUC/Microsoft.
- **Yu, X., & Wu, L. (2026).** Agentic Memory: Long and Short Term Memory for LLM Agents. Alibaba.

## Architectural Critiques and Formal Limits

- **Hooker, S. (2025).** On the Slow Death of Scaling. Cohere.
- **Kalai, A. T., et al. (2025).** Why Language Models Hallucinate. OpenAI.
- **Kambhampati, S. (various).** LLMs can't plan: pattern matching on training data rather than genuine planning.
- **LeCun, Y. (various).** Arguments for world models and against autoregressive LLMs for planning (JEPA architecture proposals).
- **Perrier, R., & Bennett, K. (2025).** Not Normal Agents: LLMs lack unified goal-directed architecture.
- **Shanahan, M. (2024).** Talking About Large Language Models. *Communications of the ACM*, 67(2), 68-79.
- **Wang, K., & Nanda, N. (2025).** Simple Mechanistic Explanations for Out-of-Context Reasoning. MIT.
- **Xu, Z., & Kankanhalli, M. (2025).** Hallucination is Inevitable: An Innate Limitation of Large Language Models. NUS.

## Anthropomorphism and Construct Transfer

- **Shah, H., & Varma, S. (2025).** Potentials and Pitfalls of LLMs in Cognitive Science. Georgia Tech.
- **Shetff, A. (2026).** Three Frameworks for AI Mentality.

## Autonomy, Grounding, and Drift

- **Alemohammad, S., et al. (2023).** Self-Consuming Generative Models Go MAD. *NeurIPS 2023*. arXiv:2307.01850.
- **Anon. (2024).** Language Models Can Articulate Implicit Goals.
- **Barkan, C. O., Black, S., & Sourbut, O. (2025).** Do LLMs Know What They Are Capable Of? *arXiv preprint arXiv:2512.24661*.
- **Feng, K. J. K., McDonald, D. W., & Zhang, A. X. (2025).** Levels of Autonomy for AI Agents. *arXiv preprint arXiv:2506.12469*.
- **Heitmann, S., et al. (2025).** Understanding AI Trajectories: Mapping the Limitations of Current LLMs. UK AISI.
- **Huang, J. Y., Choshen, L., Astudillo, R., Broderick, T., & Andreas, J. (2026).** Do LLMs Benefit from Their Own Words? *arXiv preprint arXiv:2602.24287*.
- **Lin, X., et al. (2025).** LLM-based Agents Suffer from Hallucinations: A Survey. *arXiv preprint arXiv:2509.18970*.
- **Luo, J., & Shah, S. (2025).** The More You Automate, the Less You See. CMU.
- **Rath, A. (2026).** Agent Drift: Quantifying Behavioral Degradation in Multi-Agent LLM Systems Over Extended Interactions. *arXiv preprint arXiv:2601.04170*.
- **Shumailov, I., Shumaylov, Z., Zhao, Y., Gal, Y., Papernot, N., & Anderson, R. (2024).** AI models collapse when trained on recursively generated data. *Nature*, 631, 755-759.
- **Zhang, M., Press, O., Merrill, W., Liu, A., & Smith, N. A. (2023).** How Language Model Hallucinations Can Snowball. *arXiv preprint arXiv:2305.13534*. ICML 2024.

## Parking Lot (not yet integrated, may be useful)

- **Ahmed, N., et al. (2025).** Do LLMs Know They Are Being Tested? *arXiv preprint arXiv:2510.08624*.
- **Binder, F. J., et al. (2024).** Looking Inward: Language Models Can Learn About Themselves by Introspection. *arXiv preprint arXiv:2410.13787*.
- **Betley, J., Tan, D., et al. (2025).** Emergent Misalignment: Narrow finetuning can produce broadly misaligned LLMs. *arXiv preprint arXiv:2502.17424*.
- **Cintas, C., et al. (2025).** Localizing Persona Representations in LLMs. *arXiv preprint arXiv:2505.24539*.
- **Comsa, I. M., & Shanahan, M. (2025).** Does It Make Sense to Speak of Introspection in Large Language Models? *arXiv preprint arXiv:2506.05068*.
- **Elenjical, T., Kavuri, S., & Varma, V. (2026).** Think2: Grounded Metacognitive Reasoning in Large Language Models. *arXiv preprint arXiv:2602.18806*.
- **Flavell, J. H. (1979).** Metacognition and cognitive monitoring. *American Psychologist*, 34(10), 906-911.
- **Imran, S., Lamb, R., & Atkinson, P. M. (2025).** Out-of-Context Abduction. *arXiv preprint arXiv:2508.00741*.
- **Kumaran, S., et al. (2025).** How Overconfidence in Initial Choices and Underconfidence Under Criticism Modulate Change of Mind in LLMs. *arXiv preprint arXiv:2507.03120*.
- **Mallen, A., et al. (2025).** Subversion Strategy Eval. *arXiv preprint arXiv:2412.12480*.
- **Panickssery, A., Bowman, S. R., & Feng, S. (n.d.).** LLM Evaluators Recognize and Favor Their Own Generations.
- **Perez, E., et al. (2023).** Discovering Language Model Behaviors with Model-Written Evaluations. *Findings of ACL 2023*, 13387-13434.
- **Sanneman, L., & Shah, J. A. (2022).** The Situation Awareness Framework for Explainable AI (SAFE-AI). *International Journal of Human-Computer Interaction*, 38(18-20), 1772-1788.
- **Sharkey, L., et al. (2025).** Open Problems in Mechanistic Interpretability. *arXiv preprint arXiv:2501.16496*.
- **Shen, G., et al. (2025).** From Poisoned to Aware: Fostering Backdoor Self-Awareness in LLMs. *arXiv preprint arXiv:2510.05169*.
- **Sühr, T., et al. (2025).** Stop evaluating AI with human tests. *arXiv preprint arXiv:2507.23009*.
- **Tian Hua, T., Qin, A., Marks, S., & Nanda, N. (2025).** Steering Evaluation-Aware Language Models to Act Like They Are Deployed. *arXiv preprint arXiv:2510.20487*.

*This list contains 123 entries across 12 categories.*


## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Pull requests welcome for new papers,
corrections, or category suggestions.

## License

- Code (parsers, generators): [MIT](LICENSE)
- Curated list: [CC-BY-4.0](LIST_LICENSE)

---

*Last updated 2026-05-02. Generated from the maintainer's working bibliography.*
