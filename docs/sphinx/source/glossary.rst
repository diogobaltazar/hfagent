Glossary
========

.. glossary::

    agent
        An entity that has the ability to interact with and affect the environment.

    agency
        The capacity of an agent to act in a given environment.

    reasoning
        The process of creating a plan.

    plan
        A detailed proposal for doing or achieving something.

    tools
        Tools or actions that execute the plan and affect the environment.

    encoder
        An encoder-based transformer takes text (or other data) as input and outputs a dense representation (or :term:`embedding`) of that text.

        - **example** BERT, Google
        - **use cases** Text classification, semantic search, Named Entity Recognition
        - **size** Millions of parameters

    decoder
        A decoder-based Transformer focuses on generating new tokens to complete a sequence, one token at a time.

        - **example** Llama, Google
        - **use cases** Text generation, chatbots, code generation
        - **size** Billions of parameters

    seq2seq
        A sequence-to-sequence transformer combines an encoder and a decoder. The encoder first processes the input sequence into an :term:`embedding`, then the decoder generates an output sequence.

        - **example** T5, BART
        - **use cases** Translation, Summarization, Paraphrasing
        - **size** Millions of parameters

    Text generation
        The process of generating coherent and contextually relevant text based on a given input or prompt.

    chatbots
        Software applications designed to simulate human conversation and interact with users, typically through text or voice.

    Translation
        The process of converting text from one language to another while preserving its meaning.

    Summarization
        The process of creating a concise and coherent summary of a longer text while retaining the key information.

    Paraphrasing
        The process of rephrasing text in different words while maintaining the original meaning.

    BERT
        Bidirectional Encoder Representations from Transformers, a pre-trained transformer model developed by Google for natural language understanding tasks.

    Llama
        A decoder-based transformer model designed for generating text, developed by Google.

    T5
        Text-To-Text Transfer Transformer, a model developed by Google that converts all NLP tasks into a text-to-text format.

    BART
        Bidirectional and Auto-Regressive Transformers, a model developed by Facebook that combines bidirectional and autoregressive transformers for text generation tasks.

    meta-token
        Special tokens used in language models to indicate specific events or conditions, such as the end of a sequence (EOS). Example:

    meta-token
        Special tokens used in language models to indicate specific events or conditions, such as the end of a sequence (EOS). Example:

        .. list-table:: Title
           :widths: 25 25 50
           :header-rows: 1

           * - Model
               - Provider
               - EOS Token
               - Functionality
           * - GPT4
               - OpenAI
               - <\|endoftext\|>
               - End of message text
           * - Llama 3
               - Meta (Facebook AI Research)
               - <\|eot_id\|>
               - End of sequence
           * - Deepseek-R1
               - DeepSeek
               - <\|end_of_sentence\|>
               - End of message text
           * - SmolLM2
               - Hugging Face
               - <\|im_end\|>
               - End of instruction or message
           * - Gemma
               - Google
               - <end_of_turn>
               - End of conversation turn

    T19 autoregressive
        A property of language models where the output from one pass becomes the input for the next one, creating a loop that continues until a stopping condition is met.

    T20 vocabulary
        The set of unique tokens or words that a language model can understand and generate.

    T21 beam search
        A search algorithm used in sequence generation tasks that explores multiple candidate sequences to find the one with the maximum total score, even if some individual tokens have lower scores.

    T22 attention algorithm
        A mechanism in deep learning models that allows the model to focus on specific parts of the input sequence when making predictions. When predicting the next word, not every word in a sentence is equally important. Words like **France** and **capital** in the sentence **The capital of France is** carry the most meaning. They have a higher **attention** value than the rest of the words.

        Significant advancements in scaling neural networks and making the attention mechanism work for longer and longer sequences. **context length** is the maximum number of tokens an LLM can process, or its :term:`attention span`. :term:`gpt4o` has an attention span of 128K tokens.

    T23 attention span
        The maximum number of tokens an LLM can process in a single pass. This value is determined by the model's architecture and the computational resources available.

    T24 gpt4o
        A large language model developed by OpenAI that has an attention span of 128K tokens.