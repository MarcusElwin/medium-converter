# Self-Hosted LLMs

Medium Converter can integrate with self-hosted LLMs, giving you privacy, cost savings, and control over the enhancement process.

## Local LLM Setup

### Installation

```bash
pip install medium-converter[local]
```

This installs the `llama-cpp-python` package which allows running various local LLMs.

## Using Local Models

### Command Line

```bash
# Use local LLM for enhancement
medium convert https://medium.com/example-article --enhance --llm-provider local \
  --option llm.model_path="path/to/model.gguf"
```

### Python API

```python
from medium_converter import convert_article
from medium_converter.llm.config import LLMConfig, LLMProvider

llm_config = LLMConfig(
    provider=LLMProvider.LOCAL,
    extra_params={
        "model_path": "path/to/model.gguf",
        "n_ctx": 4096,
        "n_batch": 512
    }
)

await convert_article(
    url="https://medium.com/example-article",
    enhance=True,
    llm_config=llm_config
)
```

## Recommended Models

The following models work well with Medium Converter:

1. **Mistral-7B-Instruct** - Good balance of quality and performance
   - [TheBloke/Mistral-7B-Instruct-v0.2-GGUF](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF)
   - Recommended quantization: Q4_K_M

2. **Llama-2-7b-chat** - Good text enhancement capabilities
   - [TheBloke/Llama-2-7B-Chat-GGUF](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF)
   - Recommended quantization: Q4_K_M

3. **Phi-2** - Lightweight model for basic enhancements
   - [TheBloke/phi-2-GGUF](https://huggingface.co/TheBloke/phi-2-GGUF)
   - Recommended quantization: Q4_0

## Configuration Options

| Option | Description | Default |
|--------|-------------|--------|
| `model_path` | Path to the model file (.gguf) | Required |
| `n_ctx` | Context window size | 2048 |
| `n_batch` | Batch size for prompt processing | 512 |
| `n_gpu_layers` | Number of layers to offload to GPU | 0 |
| `temperature` | Randomness of generations | 0.7 |
| `repeat_penalty` | Penalty for repeating tokens | 1.1 |
| `top_p` | Nucleus sampling parameter | 0.9 |
| `top_k` | Limit vocabulary to top K options | 40 |

## Server Integration

Medium Converter can use local LLMs running on a server with compatible APIs.

### Using LM Studio

1. Download and install [LM Studio](https://lmstudio.ai/)
2. Load a model of your choice
3. Start the local server (OpenAI API compatible)
4. Configure Medium Converter:

```python
from medium_converter import convert_article
from medium_converter.llm.config import LLMConfig, LLMProvider

llm_config = LLMConfig(
    provider=LLMProvider.OPENAI,  # Uses OpenAI-compatible API
    model="local-model",  # Model name doesn't matter
    api_base="http://localhost:1234/v1",  # LM Studio server URL
    api_key="lm-studio",  # Any string works
)

await convert_article(
    url="https://medium.com/example-article",
    enhance=True,
    llm_config=llm_config
)
```

### Using Ollama

1. Install [Ollama](https://ollama.ai/)
2. Pull a model: `ollama pull mistral`
3. Start Ollama
4. Configure Medium Converter:

```python
from medium_converter import convert_article
from medium_converter.llm.config import LLMConfig

llm_config = LLMConfig(
    model="ollama/mistral",  # Must prefix with ollama/
    extra_params={
        "api_base": "http://localhost:11434"
    }
)

await convert_article(
    url="https://medium.com/example-article",
    enhance=True,
    llm_config=llm_config
)
```

## Performance Considerations

- **Hardware Requirements**: Most 7B models require at least 8GB of RAM
- **GPU Acceleration**: Setting `n_gpu_layers` > 0 can dramatically improve performance if you have a GPU
- **Quantization**: Lower precision (e.g., Q4_K_M) reduces memory requirements but may affect quality
- **Context Length**: Reducing `n_ctx` can save memory but limits the text length that can be processed at once

## Troubleshooting

### Common Issues

1. **Out of Memory**
   - Try a smaller model or lower quantization (Q4 instead of Q8)
   - Reduce the context length (`n_ctx`)
   - Process the article in smaller chunks

2. **Slow Performance**
   - Enable GPU acceleration if available
   - Increase batch size (`n_batch`) if you have sufficient memory
   - Use a smaller model

3. **Poor Quality Output**
   - Try a larger or more recent model
   - Adjust temperature (lower for more deterministic output)
   - Fine-tune prompt templates (see the docs on customizing prompts)