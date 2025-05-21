"""Data models for Medium Converter."""

from enum import Enum
from typing import List, Optional, Dict, Any, Union
from pydantic import BaseModel, Field
from datetime import datetime


class ContentType(str, Enum):
    """Types of content blocks in Medium articles."""
    
    TEXT = "text"
    IMAGE = "image"
    CODE = "code"
    QUOTE = "quote"
    LIST = "list"
    HEADING = "heading"


class ContentBlock(BaseModel):
    """A block of content in a Medium article."""
    
    type: ContentType
    content: str
    metadata: Dict[str, Any] = Field(default_factory=dict)


class Section(BaseModel):
    """A section of a Medium article."""
    
    title: Optional[str] = None
    blocks: List[ContentBlock] = Field(default_factory=list)


class Article(BaseModel):
    """A Medium article."""
    
    title: str
    author: str
    date: Union[str, datetime]
    content: List[Union[Section, ContentBlock]] = Field(default_factory=list)
    estimated_reading_time: Optional[int] = None
    url: Optional[str] = None
    tags: List[str] = Field(default_factory=list)