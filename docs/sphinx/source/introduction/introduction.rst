Introduction
============

.. include:: ../quotes.rst

An :term:`agent` is that which has :term:`agency`, or the ability to interact with and affect the environment. This ability is provided by :term:`reasoning` and :term:`tools`. :term:`reasoning` creates a :term:`plan` (or set of :term:`actions`) which is executed with :term:`tools`. The agent's :term:`mind` actions :term:`reasoning` through an :term:`AI model`. These models are typically :term:`LLM`. These large language models are trained on a large corpus of text, learning semantical patterns with a large quantity of parameters, and generating human-like text. Most LLMs are built on the :term:`transformer` architecture, an :term:`deep learning` architecture based on the :term:`attention algorithm`. There are three types of transformers:

- :term:`encoder` Takes text (or other data) as input and outputs a dense representation (or :term:`embedding`) of that text.
- :term:`decoder` Generates new tokens to complete a sequence, one token at a time.
- :term:`seq2seq (encoder-decoder)` (**typical**) Combination of an encoder and a decoder, the encoder processes the input sequence into an embedding and the decoder generates an output sequence.

The underlying principle of an LLM is to predict the next :term:`token`, given a sequence of previous tokens. A token is the unit of information an LLM works with. A token is a sub-word (from a natural language). For example, while English has an estimated 600000 words, an LLM might have a :term:`vocabulary` of around 32000 tokens (as is the case with Llama 2). Each LLM has :term:`meta-tokens` like the **EOS - End of sequence**.

LLMs are said to be :term:`autoregressive`, meaning that the output from one pass becomes the input for the next one. This loop continues until the model predicts the next token to be the EOS token, at which point the model can stop. Once the input text is tokenized, the model computes a representation of the sequence that captures information about the meaning and the position of each token in the input sequence.
This representation goes into the model, which outputs :term:`scores` that rank the likelihood of each token in its vocabulary as being the next one in the sequence. Based on these scores, we have multiple strategies to select the tokens to complete the sentence. The easiest decoding strategy would be to always take the token with the maximum score. But there are more advanced decoding strategies. For example, :term:`beam search` explores multiple candidate sequences to find the one with the maximum total score – even if some individual tokens have lower scores.

LLMs are trained on large datasets of text, from this unsupervised learning, the model learns the structure of the language and underlying patterns in text, allowing the model to generalize to unseen data. After this initial pre-training, LLMs can be fine-tuned on a supervised learning objective to perform specific tasks. For example, some models are trained for conversational structures or tool usage, while others focus on classification or code generation.

The agent's :term:`body` actions the :term:`plan` through :term:`tools`. These :term:`tools` are often APIs interfacing external tools that interact with the environment, be it physical (robotics) or digital.

|agent_definition|

.. image:: /_static/img/agent.png
   :class: centered-image

.. image:: /_static/img/agent_2.png
   :class: centered-image

