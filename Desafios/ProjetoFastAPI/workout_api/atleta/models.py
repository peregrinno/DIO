from workout_api.contrib.models import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import DateTime, ForeignKey, Integer, String, Float
from datetime import datetime


class AtletaModel(BaseModel):
    
    __tablename__ = 'atletas'
    
    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)   
    nome: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)   
    cpf: Mapped[str] = mapped_column(String(11), nullable=False)   
    idade: Mapped[float] = mapped_column(Integer, nullable=False)   
    peso: Mapped[float] = mapped_column(Float, nullable=False)   
    altura: Mapped[str] = mapped_column(Float, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    categoria: Mapped['CategoriaModel'] = relationship(back_populates='atleta')
    categoria_id: Mapped[int] = mapped_column(ForeignKey('categorias.pk_id'))
    centro_treinamento: Mapped['CentroTreinamentoModel'] = relationship(back_populates='atleta')
    centro_treinamento_id: Mapped[int] = mapped_column(ForeignKey('centros_treinamento.pk_id'))
    