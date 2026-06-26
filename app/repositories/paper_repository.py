from typing import Optional
from sqlalchemy.orm import Session

from app.models.paper import Paper


class PaperRepository:
    """
    Repository responsible for database operations on papers.
    """

    def create_paper(self, db: Session, paper: Paper) -> Paper:
        db.add(paper)
        db.commit()
        db.refresh(paper)
        return paper

    def get_paper_by_id(
        self,
        db: Session,
        paper_id: int,
    ) -> Optional[Paper]:
        """
        Retrieve a paper by its ID.
        """
        return (
            db.query(Paper)
            .filter(Paper.id == paper_id)
            .first()
        )