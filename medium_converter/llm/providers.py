"""LLM provider clients."""

from abc import ABC, abstractmethod
from typing import Optional, Dict, Any
from .config import LLMConfig, LLMProvider


class LLMClient(ABC):
    """Base class for LLM clients."""
    
    def __init__(self, config: LLMConfig):
        """Initialize the LLM client.
        
        Args:
            config: LLM configuration
        """
        self.config = config
    
    @abstractmethod
    async def generate(self, prompt: str) -> str:
        """Generate text from a prompt.
        
        Args:
            prompt: The prompt to generate from
            
        Returns:
            Generated text
        """
        pass


class OpenAIClient(LLMClient):
    """OpenAI API client."""
    
    async def generate(self, prompt: str) -> str:
        """Generate text using OpenAI.
        
        Args:
            prompt: The prompt to generate from
            
        Returns:
            Generated text
        """
        try:
            import openai
        except ImportError:
            raise ImportError("OpenAI support requires the openai package. Install with 'pip install openai' or 'pip install medium-converter[openai]'")
        
        # Placeholder for real implementation
        return f"Enhanced with OpenAI: {prompt[:50]}..."


class AnthropicClient(LLMClient):
    """Anthropic API client."""
    
    async def generate(self, prompt: str) -> str:
        """Generate text using Anthropic.
        
        Args:
            prompt: The prompt to generate from
            
        Returns:
            Generated text
        """
        try:
            import anthropic
        except ImportError:
            raise ImportError("Anthropic support requires the anthropic package. Install with 'pip install anthropic' or 'pip install medium-converter[anthropic]'")
        
        # Placeholder for real implementation
        return f"Enhanced with Anthropic: {prompt[:50]}..."


class GoogleClient(LLMClient):
    """Google API client."""
    
    async def generate(self, prompt: str) -> str:
        """Generate text using Google.
        
        Args:
            prompt: The prompt to generate from
            
        Returns:
            Generated text
        """
        try:
            import google.generativeai as genai
        except ImportError:
            raise ImportError("Google support requires the google-generativeai package. Install with 'pip install google-generativeai' or 'pip install medium-converter[google]'")
        
        # Placeholder for real implementation
        return f"Enhanced with Google: {prompt[:50]}..."


class LiteLLMClient(LLMClient):
    """LiteLLM client for unified access to multiple providers."""
    
    async def generate(self, prompt: str) -> str:
        """Generate text using LiteLLM.
        
        Args:
            prompt: The prompt to generate from
            
        Returns:
            Generated text
        """
        try:
            import litellm
        except ImportError:
            raise ImportError("LiteLLM support requires the litellm package. Install with 'pip install litellm' or 'pip install medium-converter[llm]'")
        
        # Placeholder for real implementation
        return f"Enhanced with LiteLLM: {prompt[:50]}..."


def get_llm_client(config: LLMConfig) -> LLMClient:
    """Get an LLM client based on the provider.
    
    Args:
        config: LLM configuration
        
    Returns:
        LLM client
    """
    # Always use LiteLLM if available
    try:
        import litellm
        return LiteLLMClient(config)
    except ImportError:
        pass
    
    # Fallback to specific providers
    if config.provider == LLMProvider.OPENAI:
        return OpenAIClient(config)
    elif config.provider == LLMProvider.ANTHROPIC:
        return AnthropicClient(config)
    elif config.provider == LLMProvider.GOOGLE:
        return GoogleClient(config)
    elif config.provider == LLMProvider.MISTRAL:
        # Placeholder for Mistral client
        return OpenAIClient(config)  # Temporary use OpenAI client
    elif config.provider == LLMProvider.LOCAL:
        # Placeholder for local client
        return OpenAIClient(config)  # Temporary use OpenAI client
    else:
        # Fallback to OpenAI
        return OpenAIClient(config)