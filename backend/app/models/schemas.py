from pydantic import BaseModel, Field
from typing import Optional


class CommandRequest(BaseModel):
    """
    Request schema for command execution.
    """

    command: str = Field(
        ...,
        min_length=1,
        max_length=500,
        description="Linux command to be executed",
        examples=["ls -l"]
    )


class CommandResponse(BaseModel):
    """
    Response schema for command execution result.
    """

    output: str = Field(
        ...,
        description="Output generated after executing the command"
    )


class ErrorResponse(BaseModel):
    """
    Standard error response schema.
    """

    detail: str = Field(
        ...,
        description="Error message describing what went wrong"
    )