from datetime import date
from typing import Optional

from fastapi import UploadFile, Form, File, HTTPException
from pydantic import BaseModel, field_validator, HttpUrl, ConfigDict, Field

from database.models.accounts import GenderEnum
from validation import (
    validate_name,
    validate_image,
    validate_gender,
    validate_birth_date
)


class ProfileCreateRequestSchema(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    gender: Optional[GenderEnum]
    date_of_birth: Optional[date]
    info: Optional[str]
    avatar: Optional[UploadFile]

    @field_validator("first_name", "last_name")
    @classmethod
    def validate_first_name(cls, value: Optional[str]) -> Optional[str]:
        if value is not None:
            return validate_name(value.lower())
        return value

    @field_validator("gender")
    @classmethod
    def validate_gender(cls, value: Optional[GenderEnum]) -> Optional[
        GenderEnum]:
        if value is not None:
            return validate_gender(value)
        return value

    @field_validator("date_of_birth")
    @classmethod
    def validate_date_of_birth(cls, value: Optional[date]) -> Optional[date]:
        if value is not None:
            return validate_birth_date(value)
        return value

    @field_validator("avatar")
    @classmethod
    def validate_avatar(
            cls,
            value: Optional[UploadFile]
    ) -> Optional[UploadFile]:
        if value is not None:
            return validate_image(value)
        return value

    model_config = ConfigDict(
        arbitrary_types_allowed=True
    )


class ProfileResponseSchema(BaseModel):
    id: int
    user_id: int
    first_name: str
    last_name: str
    gender: str
    date_of_birth: date
    info: str
    avatar: HttpUrl
