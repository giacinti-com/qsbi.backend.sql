import typing as t

from sqlalchemy import inspect
from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base(object):
    id: t.Any
    __name__: str

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    # convenient function to convert to dict
    def as_dict(self) -> t.Dict:
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}

    # required in order to access columns with server defaults
    # or SQL expression defaults, subsequent to a flush, without
    # triggering an expired load
    __mapper_args__ = {"eager_defaults": True}
