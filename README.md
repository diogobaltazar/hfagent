[course material](https://huggingface.co/learn/agents-course/unit0/introduction)

An `agent` is that which has `agency`, or the ability to interact with and affect the environment. This ability is provided by `reasoning` (which creates a `plan`) and `utils` (which action the plan and affect the environment).

```
An Agent is a system that leverages an AI model to interact with its environment in order to achieve a user-defined objective. It combines reasoning, planning, and the execution of actions (often via external tools) to fulfill tasks.
```

## The Brain (AI Model, LLMs typically but also VLM and so on)

The AI model handles reasoning and planning. It decides which Actions to take based on the situation.

An LLM is a type of AI model that excels at understanding and generating human language. They are trained on vast amounts of text data, allowing them to learn patterns, structure, and even nuance in language. These models typically consist of many millions of parameters. Most LLMs nowadays are built on the Transformer architecture—a deep learning architecture based on the “Attention” algorithm, that has gained significant interest since the release of BERT from Google in 2018.

There are 3 types of transformers:

`Encoders`
An encoder-based Transformer takes text (or other data) as input and outputs a dense representation (or embedding) of that text.

Example: BERT from Google
Use Cases: Text classification, semantic search, Named Entity Recognition
Typical Size: Millions of parameters

`Decoders`
A decoder-based Transformer focuses on generating new tokens to complete a sequence, one token at a time.

Example: Llama from Meta
Use Cases: Text generation, chatbots, code generation
Typical Size: Billions (in the US sense, i.e., 10^9) of parameters

`Seq2Seq (Encoder–Decoder)`
A sequence-to-sequence Transformer combines an encoder and a decoder. The encoder first processes the input sequence into a context representation, then the decoder generates an output sequence.

Example: T5, BART
Use Cases: Translation, Summarization, Paraphrasing
Typical Size: Millions of parameters
Although Large Language Models come in various forms, LLMs are typically decoder-based models with billions of parameters.

The underlying principle of an LLM is simple yet highly effective: its objective is to predict the next token, given a sequence of previous tokens. A “token” is the unit of information an LLM works with. You can think of a “token” as if it was a “word”, but for efficiency reasons LLMs don’t use whole words.

For example, while English has an estimated 600,000 words, an LLM might have a vocabulary of around 32,000 tokens (as is the case with Llama 2). Tokenization often works on sub-word units that can be combined.

Each LLM has some special `tokens specific to the model`. The LLM uses these tokens to open and close the structured components of its generation. For example, to indicate the start or end of a sequence, message, or response. Moreover, the input prompts that we pass to the model are also structured with special tokens. The most important of those is the `End of sequence token (EOS)`.

| Model         | Provider                     | EOS Token         | Functionality               |
|---------------|------------------------------|-------------------|-----------------------------|
| GPT4          | OpenAI                       | <\|endoftext\|>   | End of message text         |
| Llama 3       | Meta (Facebook AI Research)  | <\|eot_id\|>      | End of sequence             |
| Deepseek-R1   | DeepSeek                     | <\|end_of_sentence\|> | End of message text      |
| SmolLM2       | Hugging Face                 | <\|im_end\|>      | End of instruction or message |
| Gemma         | Google                       | <end_of_turn>     | End of conversation turn    |

The forms of special tokens are highly diverse across model providers.

### Understanding next token prediction.

LLMs are said to be `autoregressive`, meaning that `the output from one pass becomes the input for the next one`. This loop continues until the model predicts the next token to be the EOS token, at which point the model can stop.

![Autoregression Schema]

In other words, an LLM will decode text until it reaches the `EOS`. But what happens during a single decoding loop? A brief overview:

Once the input text is tokenized, the model computes a representation of the sequence that captures information about the meaning and the position of each token in the input sequence.
This representation goes into the model, which outputs scores that rank the likelihood of each token in its vocabulary as being the next one in the sequence.

Based on these scores, we have multiple strategies to select the tokens to complete the sentence. The easiest decoding strategy would be to always take the token with the maximum score. But there are more advanced decoding strategies. For example, beam search explores multiple candidate sequences to find the one with the maximum total score–even if some individual tokens have lower scores.

#### Beam Search Visualiser
TODO

#### Attention is all you need
A key aspect of the Transformer architecture is `Attention`. When predicting the next word, not every word in a sentence is equally important. Words like `France` and `capital` in the sentence `The capital of France is …` carry the most meaning. They have a higher `attention` value than the rest of the words.

![tmp]

Significant advancements in scaling neural networks and making the attention mechanism work for longer and longer sequences. `context length` is the `maximum number of tokens` an LLM can process, or its `attention span`. `gpt4o` has an `attention span` of `128K` tokens.

#### LLM Training

LLMs are trained on large datasets of text, from this `unsupervised learning`, the model learns the `structure of the language` and `underlying patterns in text`, allowing the model to `generalize` to unseen data. After this `initial pre-training`, LLMs can be `fine-tuned` on a `supervised learning objective` to perform specific tasks. For example, some models are trained for conversational structures or tool usage, while others focus on classification or code generation.

#### LLM Running

Locally or remotely via APIs.

## The Body (Capabilities and Tools)

What the Agent is equipped to do. An agent can do anything provided it has the adequate tools.

Actions are the steps the Agent takes, while Tools are external resources the Agent can use to perform those actions.

# Understand

Which of the following best describes an AI Agent?

    - A system that solely processes static text, without any inherent mechanism to interact dynamically with its surroundings or execute meaningful actions.
    - OK An AI model that can reason, plan, and use tools to interact with its environment to achieve a specific goal.
    - A conversational agent restricted to answering queries, lacking the ability to perform any actions or interact with external systems.
    - An online repository of information that offers static content without the capability to execute tasks or interact actively with users.

Q2: What is the Role of Planning in an Agent?

Why does an Agent need to plan before taking an action?

    - To primarily store or recall past interactions, rather than mapping out a sequence of future actions.
    - OK To decide on the sequence of actions and select appropriate tools needed to fulfill the user’s request.
    - To execute a sequence of arbitrary and uncoordinated actions that lack any defined strategy or intentional objective.
    - To merely convert or translate text, bypassing any process of formulating a deliberate sequence of actions or employing strategic reasoning.

Q3: How Do Tools Enhance an Agent’s Capabilities?

Why are tools essential for an Agent?

    - Tools serve no real purpose and do not contribute to the Agent’s ability to perform actions beyond basic text generation.
    - OK Tools provide the Agent with the ability to execute actions a text-generation model cannot perform natively, such as making coffee or generating images.
    - Tools are solely designed for memory storage, lacking any capacity to facilitate the execution of tasks or enhance interactive performance.
    - Tools severely restrict the Agent exclusively to generating text, thereby preventing it from engaging in a broader range of interactive actions.

Q4: How Do Actions Differ from Tools?

What is the key difference between Actions and Tools?

    - OK Actions are the steps the Agent takes, while Tools are external resources the Agent can use to perform those actions.
    - Actions and Tools are entirely identical components that can be used interchangeably, with no clear differences between them.
    - Tools are considered broad utilities available for various functions, whereas Actions are mistakenly thought to be restricted only to physical interactions.
    - Actions inherently require the use of LLMs to be determined and executed, whereas Tools are designed to function autonomously without such dependencies.

Q5: What Role Do Large Language Models (LLMs) Play in Agents?

How do LLMs contribute to an Agent’s functionality?

    - LLMs function merely as passive repositories that store information, lacking any capability to actively process input or produce dynamic responses.
    - OK LLMs serve as the reasoning 'brain' of the Agent, processing text inputs to understand instructions and plan actions.
    - LLMs are erroneously believed to be used solely for image processing, when in fact their primary function is to process and generate text.
    - LLMs are considered completely irrelevant to the operation of AI Agents, implying that they are entirely superfluous in any practical application.

Q6: Which of the Following Best Demonstrates an AI Agent?

Which real-world example best illustrates an AI Agent at work?

    - A static FAQ page on a website that provides fixed information and lacks any interactive or dynamic response capabilities.
    - OK A virtual assistant like Siri or Alexa that can understand spoken commands, reason through them, and perform tasks like setting reminders or sending messages.
    - A simple calculator that performs arithmetic operations based on fixed rules, without any capability for reasoning or planning.
    - A video game NPC that operates on a fixed script of responses, without the ability to reason, plan, or use external tools.

[Autoregression Schema]: https://cdn-lfs-us-1.hf.co/repos/45/f4/45f48d5b3577034b76ee728dfe60afca3d0aa70790fda3e706eeb9276d8d5331/53a020cfddcd2f7b93c048b98335f38535a398caf2c7b3c97a7c1c1bcf96e13d?response-content-disposition=inline%3B+filename*%3DUTF-8%27%27AutoregressionSchema.gif%3B+filename%3D%22AutoregressionSchema.gif%22%3B&response-content-type=image%2Fgif&Expires=1740343226&Policy=eyJTdGF0ZW1lbnQiOlt7IkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0MDM0MzIyNn19LCJSZXNvdXJjZSI6Imh0dHBzOi8vY2RuLWxmcy11cy0xLmhmLmNvL3JlcG9zLzQ1L2Y0LzQ1ZjQ4ZDViMzU3NzAzNGI3NmVlNzI4ZGZlNjBhZmNhM2QwYWE3MDc5MGZkYTNlNzA2ZWViOTI3NmQ4ZDUzMzEvNTNhMDIwY2ZkZGNkMmY3YjkzYzA0OGI5ODMzNWYzODUzNWEzOThjYWYyYzdiM2M5N2E3YzFjMWJjZjk2ZTEzZD9yZXNwb25zZS1jb250ZW50LWRpc3Bvc2l0aW9uPSomcmVzcG9uc2UtY29udGVudC10eXBlPSoifV19&Signature=bwKfPQu4JRFWDotv2UeDpgJzXFQLV40ZbQztRH0TgAw961m-e3lGd5k1I8lax1thtYJXrYN1cMLDz5gR0XdpIenGaREVJNtQrxUnziR8WirpwttLN3D4UPmS9OIYOigbgIr69oJOMdotMhMwH-lpmlfiSgs8iLJcutIV4QImUpuyz9jQ%7EFVAOLDabKlrnHaGVQrQjhXF6D1Q40W1CscC3AWTI4uozykEcMzRpRld5Lr6Ty2ep2ZsNeyF7KaUkTXhPyZpeFVUqyoHzFPWnezU43uMZ0gxvMjJarG6PHTcz8j83ei4F7-CzmZvRIKy9e5u4PELdoUfKS9c%7EqplOEuJvQ__&Key-Pair-Id=K24J24Z295AEI9

[tmp]: https://huggingface.co/datasets/agents-course/course-images/resolve/main/en/unit1/DecodingFinal.gif
