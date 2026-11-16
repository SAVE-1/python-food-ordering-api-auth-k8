from sqlalchemy import BigInteger, CheckConstraint, Column, Identity, Text, text

# CREATE TABLE ingredients (
#     id             BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
#     name           TEXT NOT NULL UNIQUE,
#     is_allergen    BOOLEAN NOT NULL DEFAULT false,
#     allergen_type  TEXT,
#     dietary_flag   TEXT CHECK (dietary_flag IN ('Vegan', 'Vegetarian', 'Meat')),
#     CHECK (is_allergen OR allergen_type IS NULL)



# class Ingredients(SQLModel, table=True):
#     __tablename__ = "ingredients"
#     __table_args__ = (
#         CheckConstraint(
#             "dietary_flag IN ('Vegan', 'Vegetarian', 'Meat')",
#             name="ck_ingredients_dietary_flag",
#         ),
#         CheckConstraint(
#             "is_allergen OR allergen_type IS NULL",
#             name="ck_ingredients_allergen_type_requires_allergen",
#         ),
#     )

#     id: int | None = Field(
#         default=None,
#         sa_column=Column(BigInteger, Identity(always=True), primary_key=True),
#     )
#     name: str = Field(sa_type=Text, unique=True, nullable=False)
#     is_allergen: bool = Field(
#         default=False,
#         nullable=False,
#         sa_column_kwargs={"server_default": text("false")},
#     )
#     allergen_type: str | None = Field(default=None, sa_type=Text)
#     dietary_flag: str | None = Field(default=None, sa_type=Text)

