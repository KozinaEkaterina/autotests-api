from typing import Optional

from pydantic import BaseModel, Field, ConfigDict


class ExerciseSchema(BaseModel):
    """
    Описание структуры упражнения.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    course_id: str = Field(alias='courseId')
    max_score: int = Field(alias='maxScore')
    min_score: int = Field(alias='minScore')
    order_index: int = Field(alias='orderIndex')
    description: str
    estimated_time: str = Field(alias='estimatedTime')


class GetExercisesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка упражнений.
    """
    model_config = ConfigDict(populate_by_name=True)

    course_id: str = Field(alias='courseId')


class GetExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа на получение упражнения.
    """
    exercise: ExerciseSchema


class GetExercisesResponseSchema(BaseModel):
    """
    Описание структуры ответа на получение упражнений.
    """
    exercises: list[ExerciseSchema]


class CreateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание упражнения.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str
    course_id: str = Field(alias='courseId')
    max_score: int = Field(alias='maxScore')
    min_score: int = Field(alias='minScore')
    order_index: int = Field(alias='orderIndex')
    description: str
    estimated_time: str = Field(alias='estimatedTime')


class UpdateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление упражнения.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: Optional[str]
    max_score: Optional[int] = Field(alias='maxScore')
    min_score: Optional[int] = Field(alias='minScore')
    order_index: Optional[int] = Field(alias='orderIndex')
    description: Optional[str]
    estimated_time: Optional[str] = Field(alias='estimatedTime')