# CECS 574-Privacy-preservation-in-distributed-machine-learning-or-deep-learning
This repository aims to distill key insights from a research paper exploring Distributed or Collaborative Deep Learning, where multiple participants contribute to model training from varied datasets while addressing significant privacy concerns. We categorize this paradigm into direct, indirect, and peer-to-peer approaches, examining associated privacy issues. Surveying cryptographic algorithms and techniques for privacy preservation, particularly focusing on Homomorphic Encryption, our repository highlights fundamental theories and suggests future directions, emphasizing the importance of mitigating privacy concerns in collaborative deep learning.

# Introduction:
Within the context of Machine Learning (ML) and Deep Learning (DL) domains, this repository emphasizes the challenge of limited access to labeled datasets, especially in sensitive sectors like healthcare. We introduce Collaborative or Distributed Deep Learning as a potential solution, leveraging multiple data sources to refine model accuracy. However, we stress the critical necessity of privacy preservation, particularly in domains dealing with sensitive data. Critiquing existing survey papers for their generic approach and limited focus on privacy preservation, we highlight our unique contribution: categorizing collaborative deep learning into direct, indirect, and peer-to-peer approaches. We explore associated privacy concerns, review privacy preservation techniques, and underscore the significance of Homomorphic Encryption. Finally, we outline the repository's structure and contributions, including analyses of weight update theories and comparisons of privacy preservation approaches.

# Collaborative/Distributed Deep Learning:

This section of the research paper delves into Collaborative/Distributed Deep Learning, emphasizing the interchangeability of terms and the associated privacy concerns. It introduces Collaborative Deep Learning, where multiple participants jointly train a Deep Learning model by contributing their training datasets. The approach, inspired by data parallelism in Deep Learning, is depicted as advantageous in scenarios with limited training datasets or where data must remain at its source location.

The paper outlines three approaches to Collaborative Deep Learning: Direct, Indirect, and Peer-to-peer. Direct involves participants directly sharing datasets with a central server, while Indirect participants train locally and share parameter updates with the server. Peer-to-peer participants share parameters directly with each other, bypassing the need for a central server.

Privacy concerns are addressed, highlighting direct and indirect leakage risks. Direct leakage pertains to uploading datasets to a central server, while indirect leakage involves sharing parameters, potentially revealing sensitive information. The importance of embedding privacy measures into collaborative solutions, particularly in sensitive domains like healthcare, is emphasized.

# Privacy Preservation Techniques:

The section reviews common privacy preservation techniques used in Distributed Deep Learning: Secure Multi-Party Computing (SMC), Differential Privacy (DP), and Homomorphic Encryption (HE).

**Secure Multi-Party Computing (SMC):** Allows multiple parties to compute a function over their inputs while keeping those inputs private. Challenges include high communication costs and scalability limitations.

<img width="576" alt="image" src="https://github.com/dikshanpatil/CECS---574---Privacy-preservation-in-distributed-machine-learning-or-deep-learning/assets/128430331/9bd48b13-3901-431a-8015-d67942789eeb">

**Differential Privacy (DP):** Involves adding random noise to data to preserve privacy. Challenges include balancing model usability and privacy.
<img width="458" alt="image" src="https://github.com/dikshanpatil/CECS---574---Privacy-preservation-in-distributed-machine-learning-or-deep-learning/assets/128430331/0c4da001-6358-4e25-ae1b-e0d6cf1504f8">


**Homomorphic Encryption (HE):** Allows operations on encrypted data without decryption, suitable for cloud environments. Challenges include computational cost and efficiency limitations.

![information-11-00357-g002](https://github.com/dikshanpatil/CECS---574---Privacy-preservation-in-distributed-machine-learning-or-deep-learning/assets/128430331/3fa0a057-1e39-4f24-98e3-168ab0a1d5ec)

The importance of privacy, efficiency, and accuracy in Distributed Deep Learning is underscored, with a discussion on combining privacy preservation techniques to address individual limitations. Careful consideration is emphasized when choosing an approach.

# Summary:

This repository explores Collaborative/Distributed Deep Learning and privacy preservation techniques in the context of Deep Learning research. It discusses various collaborative approaches and associated privacy concerns, along with reviewing common privacy preservation techniques such as SMC, DP, and HE. The aim is to provide insights into addressing privacy concerns while leveraging collaborative Deep Learning for improved model accuracy.

# References:
https://www.sciencedirect.com/science/article/pii/S2214212621001630
https://www.researchgate.net/publication/346288300_Privacy-Preserving_Deep_Learning_on_Machine_Learning_as_a_Service-a_Comprehensive_Survey
