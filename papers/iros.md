# IROS 2025 Paper

You are a top level robotics AI researcher, give a clear structure of a conference paper about my idea. Never use ambigious words, use straight forward english. Write a clear explaination.


## conference requirement
Overview
Situation cognition in driving is the active perception and prediction of the intentions and future behaviors of involving agents and facilitating the inference of spatiotemporal constraint for behavior decision-making, motion planning, and motion control of autonomous vehicles. In the workshop, we would like to discuss how recent advances in situation cognition from the AI communities could benefit driving autonomy research, e.g., incorporating foundation models, scene graphs, causal theory, etc., potentially facilitating fully autonomy of driving systems and enhancing the interpretability, safety, robustness, and generalizable ability of autonomous vehicles. 

Nowadays, the situation cognition computing in the open traffic world faces various environmental disturbances, causal confusion, and various physical properties and rules. Current paradigms fall short of the traffic situation reasoning that vehicles need to consider, such as human experience, real-world knowledge, situation causal relations, etc. These issues may be alleviated by integration with driving systems, where real-world driving experiences that contain rich sensory input and introspection can potentially bring driving autonomy to the next level. 

The workshop aims to create an inclusive and collaborative platform for professionals, researchers, and enthusiasts alike to exchange ideas, share experiences, and foster meaningful connections within the autonomous driving community. It will feature a mix of presentations, open panel discussions, and results and demos from our Visual-CognitiveAccident-Understanding (Cog-AU) competition challenge. Five invited speakers will share their related research, thoughts, and experiences at the intersection of autonomous systems, with broad coverage of topics such as available datasets, benchmarks, closedloop driving, foundation models, and more.


                                                             Call for Papers
Autonomous driving has the dual attributes of strategic technology and emerging industry and has long been highly concerned by local governments, industry, and academia. In recent years, continuous breakthroughs in learning technology have pushed autonomous vehicles into a new stage of development. In this way, existing autonomous driving systems still cannot omit manual supervision. Driven by the increasing scale of model parameters (e.g., LLMs, VLMs) and the massive expansion of data, deep learning technology promotes the continuous iterative upgrade of driving system performance along three technical routes: modular cascade, end-to-end perception-decision integrated model, and foundation model empowerment. However, bottlenecks such as interpretability, generalization, robustness, and causal confusion still exist and are increasingly obvious, seriously affecting the industrialization process of autonomous driving systems.

Traffic scenes are uncertain and open. The human driving process is a dynamic process that continuously recognizes the traffic situation and generates driving behaviors, which is obviously different from the current perception-to-control calculation process of autonomous driving. Humans learn, interpret, reason, and remember situations and corresponding driving operations from their interactions with real traffic environments, conduct inductive reasoning, summarize common sense rules, and accumulate driving experience. When humans drive, the process of triggering driving behavior by the current traffic situation is the result of cognitive mapping between human experience and the current situation.

How to transfer the scene semantics, abstract representations, and mapping mechanisms of driving experience formed by humans to autonomous driving systems, so that they can recognize and respond to highly dynamic and highly random traffic situations like humans? Obviously, the "representation+calculation" paradigm followed by current data-driven deep learning cannot adapt to the closed-loop characteristics of intelligent driving perception-motion, especially the unique introspection and reflection mechanism of human driving strategy learning. This requires exploring new types of autonomous driving systems with human-like cognitive mechanisms (abstract representation of situations and human-like policy generation for introspection and reflection) from the perspective of computational thinking. 

The workshop aims to create an inclusive and collaborative platform for professionals, researchers, and enthusiasts alike to exchange ideas, share experiences, and foster meaningful connections within the human-like autonomous driving field. It will feature a mix of presentations, open panel discussions, and results and demos from our VisualCognitive-Accident-Understanding (Cog-AU) competition challenge to facilitate the development of safety-critical driving scene understanding. In this challenge, we plan to host the challenge over the span of a few months before IROS 2025 and present the first stage of results at the workshop. We will release a novel human-gaze-aligned egocentric accident video benchmark collected in driving scenes. Specifically, the benchmark contains well-annotated human-gaze maps, object bounding boxes, accident videos, text descriptions of accident reasons, prevention advice, and accident types. The challenge will be open to anyone interested in the field to participate and we will summarize the results and invite the winning teams to present their work at the workshop. More information on the Cog-AU Challenge can be found on the workshop website.

Five invited speakers will discuss their related research, thoughts, and experiences in various aspects at the intersection of AI and autonomous driving systems, with broad coverage of topics such as available datasets, benchmarks, software stacks, world models, spatial reasoning, foundation models, and more. Additionally, this workshop calls for workshop papers to absorb cutting-edge works with poster presentations. 

Topics of interest span a diverse range across the field of autonomous driving and other disciplines and include but are not limited to the following:

-embodied driving intelligence
-spatial and causal reasoning
-social concept reasoning in driving scenes
-human-vehicle collaborations
-memory modeling and retrospection in driving autonomy
-foundation models for autonomous driving
-vision-language-driving world models
-Real-to-sim-to-real gap in fast-driving testing

## My idea

1. 方向：可解释性驱动的危险场景理解
标题："Why Did the Car Swerve? Causal Attribution in Vision-Language Models for Autonomous Driving Risk Prediction"
- 研究重点：分析VLM如何通过视觉和文本模态识别危险因素（如行人突然出现）并生成可解释的因果链。
- 实现细节：
  - 方法：结合Grad-CAM（视觉归因）和输入梯度法（文本归因），定位关键区域与词汇。
  - 数据：使用风险等级≥4的场景，标注真值因果链（如“行人闯入车道→车辆急刹”）。
  - 评估指标：归因准确率（IoU）、人类对齐度（人工评分）。

## My dataset
In our Subjective Risk Causal Dataset, we collected driving data from urban areas in Japan, which included rosbag data and forward-facing camera video information. From continuous driving records, we carefully selected 2,658 video clips of 6 seconds in duration each. To further our study, we recruited 10 participants to participate in an experiment focused on subjective risk level and driving scene understanding. In the experiment, participants were asked to rate each video on a scale from 1 (safe) to 5 (risky). Subsequently, they were tasked with providing a natural language description of the events occurring in the video. They were also prompted to select relevant keywords or write description sentences, which encompassed five categories (Table \ref{tab:scene_dec}). Each annotation corresponds to a driving scene in urban city, and each column represents the following information:

\begin{enumerate}
    \item Scene type ID: ID for each urban driving scene, which is defined in Table \ref{tab:scene_dec}.
    \item Risk score: Normalized risk score calculated using Likert's Sigma method from the five-level subjective risk level assigned by each participant.
    \item Subjective risk level: Five-level risk level assigned by the participant to the scene (1: safe - 5: risky)
    \item Scene Description: Short sentences describing the driving situation  (e.g. Ego vehicle stopped in front of the forked road., Next ego vehicle turned right. etc.)
    \item Risky factor: Short sentences describing the danger factors (only for scenes where the worker assigned a subjective risk level of 4 or 5)  (e.g. Ego vehicle overtook the bike without slowing down to avoid the oncoming vehicle on the left lane. etc.)
    \item Environment Tag: Static keywords representing the driving environment and situation (e.g.  Night, Sparse traffic,  etc.)
    \item Action Tag: Short keywords representing the driving environment and situation (e.g.  start at the green light, overtaking, turning the steering wheel in a zigzag etc.)
\end{enumerate}

\begin{table}[]
    \centering
    \begin{tabular}{|c|l|} \hline 
        ID & Scene Description \\ \hline\hline
        1 &  Pedestrian and bicycle crossing \\
        2 &  Overtaking pedestrians and bicycles\\
        3 &  Overtaking parked vehicles\\
        4 &  Left turn with pedestrians and bicycles\\
        5 &  Right turn with pedestrians and bicycles\\
        6 &  Right turn against oncoming four-wheel vehicles\\
        7 &  Right turn against oncoming two-wheel vehicles\\
        9 &  Oncoming right-turning two-wheel vehicles while going straights\\
        10 &  Oncoming cross-cutting four-wheel vehicles while going straights\\
        11 &  Oncoming cross-cutting two-wheel vehicles while going straights\\
        12 &  Violation involving pedestrians and bicycles\\
        13 & Scenes where the participant felt a near miss\\\hline
    \end{tabular}
    \caption{Types of urban driving scenes categorized into 13 distinct categories.}
    \label{tab:scene_dec}
\end{table}


## My previous work
Personalized Causal Factor Generalization for Subjective Risky Scene Understanding with Vision Transformer: In this study, we use the Vision Transformer (ViT) to pull out key features from driving video clips, aiming to understand how different participants perceive risks during driving. We then apply Counterfactual Causal Models to see how these features affect subjective driving risk among different individuals. By testing our approach with 10 participants, we found that it can personally identify which driving situations they find risky. By combining this causal analysis with the ViT's ability to understand scenes, our method showed better accuracy in detecting subjective risky situations.



# Proposal 1
# Why Did the Car Swerve? Causal Attribution in Vision-Language Models for Autonomous Driving Risk Prediction

## Abstract
This paper presents a novel approach to interpretable risk prediction in autonomous driving using vision-language models (VLMs) with causal attribution mechanisms. We address the critical need for explainable AI in safety-critical driving scenarios by developing methods that not only predict risk levels but also provide clear causal explanations for their predictions. Using our Subjective Risk Causal Dataset containing 2,658 urban driving video clips with human-annotated risk assessments and causal descriptions, we demonstrate how VLMs can generate human-aligned causal chains explaining risk factors in driving scenarios.

## 1. Introduction

### 1.1 Problem Statement
Current autonomous driving systems lack interpretability when making risk assessments, creating a significant barrier to trust and adoption. While deep learning models can predict dangerous situations, they cannot explain why a scenario is risky or what specific factors contribute to the risk assessment.

### 1.2 Research Motivation
Human drivers naturally understand risk through causal reasoning - they can explain why they braked (pedestrian stepped into road) or why they changed lanes (vehicle ahead stopped suddenly). Autonomous systems need similar interpretable decision-making capabilities.

### 1.3 Contributions
- A novel framework combining visual and textual attribution methods for causal explanation in driving risk prediction
- Integration of Grad-CAM for visual attribution and input gradient methods for text attribution
- Evaluation on real-world urban driving data with human-annotated ground truth causal chains
- Demonstration of human-aligned risk factor identification in complex driving scenarios

## 2. Related Work

### 2.1 Interpretable AI in Autonomous Driving
Review existing work on explainable AI methods in autonomous driving, highlighting limitations in current approaches that focus primarily on visual explanations without causal reasoning.

### 2.2 Vision-Language Models for Driving
Discuss recent advances in VLMs applied to driving scenarios, emphasizing the gap in interpretability and causal understanding.

### 2.3 Causal Attribution Methods
Overview of attribution techniques including Grad-CAM, integrated gradients, and attention mechanisms, establishing the foundation for your combined approach.

## 3. Methodology

### 3.1 Vision-Language Model Architecture
Describe the VLM architecture used for processing both visual (driving video) and textual (scene descriptions) inputs simultaneously.

### 3.2 Causal Attribution Framework

#### 3.2.1 Visual Attribution Module
- **Grad-CAM Implementation**: Explain how Grad-CAM identifies visually important regions in driving scenes
- **Spatial Localization**: Detail the method for localizing risk factors in the visual field
- **Temporal Analysis**: Describe how attribution maps change over the 6-second video clips

#### 3.2.2 Textual Attribution Module
- **Input Gradient Method**: Explain the gradient-based approach for identifying important words in scene descriptions
- **Keyword Extraction**: Detail the process of extracting relevant risk-related terms
- **Semantic Alignment**: Describe how textual attributions align with visual findings

#### 3.2.3 Multimodal Fusion
- **Cross-Modal Attention**: Explain how visual and textual attributions are combined
- **Causal Chain Generation**: Detail the process of creating interpretable causal explanations
- **Consistency Verification**: Describe methods ensuring coherent multimodal explanations

### 3.3 Ground Truth Causal Chain Construction
Explain how human-annotated risky factors (risk level ≥4) are structured into causal chains for training and evaluation.

## 4. Dataset and Experimental Setup

### 4.1 Subjective Risk Causal Dataset
- **Data Collection**: 2,658 six-second video clips from urban driving in Japan
- **Annotation Process**: 10 participants rating risk levels (1-5) and providing descriptions
- **Scene Categories**: 13 distinct urban driving scenarios (Table 1)
- **Risk Distribution**: Focus on high-risk scenarios (levels 4-5) for causal analysis

### 4.2 Annotation Schema
Detail the five-category annotation system:
- Scene type ID and risk scores
- Subjective risk levels and scene descriptions
- Risky factor identification
- Environment and action tags

### 4.3 Experimental Configuration
- **Model Training**: Training procedures for the VLM with attribution components
- **Evaluation Metrics**: Attribution accuracy (IoU), human alignment scores
- **Baseline Comparisons**: Comparison with existing interpretability methods

## 5. Results and Analysis

### 5.1 Risk Prediction Performance
Present accuracy results for risk level prediction across different scene types and risk levels.

### 5.2 Attribution Quality Assessment

#### 5.2.1 Visual Attribution Results
- **Localization Accuracy**: IoU scores for risk factor localization
- **Temporal Consistency**: Analysis of attribution stability across video frames
- **Scene Type Analysis**: Performance breakdown by driving scenario categories

#### 5.2.2 Textual Attribution Results
- **Keyword Relevance**: Accuracy of risk-related keyword identification
- **Semantic Coherence**: Evaluation of textual explanation quality
- **Human Alignment**: Comparison with human-provided risk descriptions

### 5.3 Causal Chain Evaluation
- **Chain Completeness**: Assessment of generated causal explanations
- **Logical Consistency**: Evaluation of cause-effect relationships
- **Human Preference Study**: User study comparing generated vs. human explanations

### 5.4 Qualitative Analysis
Present case studies showing successful causal attribution in complex scenarios like pedestrian crossings, vehicle overtaking, and intersection navigation.

## 6. Discussion

### 6.1 Interpretability vs. Accuracy Trade-off
Analyze the relationship between model interpretability and prediction accuracy.

### 6.2 Cross-Cultural Considerations
Discuss how subjective risk perception varies among participants and its impact on model training.

### 6.3 Real-World Deployment Considerations
Address practical aspects of implementing interpretable risk prediction in autonomous vehicles.

### 6.4 Limitations
- **Dataset Scope**: Limited to urban Japanese driving scenarios
- **Subjective Nature**: Dependence on human risk perception
- **Computational Overhead**: Attribution computation costs

## 7. Conclusion and Future Work

### 7.1 Key Findings
Summarize the main contributions and their significance for interpretable autonomous driving.

### 7.2 Impact on Autonomous Driving
Discuss how causal attribution can improve trust and safety in autonomous systems.

### 7.3 Future Directions
- **Multi-Cultural Dataset**: Expanding to diverse driving environments and cultures
- **Real-Time Implementation**: Optimizing attribution methods for online deployment
- **Advanced Causal Models**: Incorporating more sophisticated causal reasoning frameworks
- **Integration with Planning**: Connecting interpretable risk assessment to motion planning

## References
Include relevant citations covering interpretable AI, vision-language models, autonomous driving, and causal attribution methods.

---

## Appendices

### Appendix A: Scene Type Definitions
Detailed descriptions of the 13 urban driving scene categories.

### Appendix B: Annotation Guidelines
Complete annotation instructions provided to human evaluators.

### Appendix C: Additional Results
Supplementary experimental results and visualizations.

---

**Note**: This structure aligns with the IROS workshop's emphasis on interpretability, causal reasoning, and human-vehicle collaboration while addressing the call for papers' focus on embodied driving intelligence and foundation models for autonomous driving.