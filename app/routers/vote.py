from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session

# creating router instance
router = APIRouter(prefix="/vote", tags=["Vote"])

# post operation to send some information to the server, in paranteza e url("/")
@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(vote: schemas.Vote, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):
    
# send a 404 if the post dosen't exist
    post = db.query(models.Post).filter(models.Post.id == vote.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {vote.post_id} not found")

# to create a vote the first thing to do is to query to see if the vote alraedy exists
    vote_query = db.query(models.Vote).filter(models.Vote.post_id == vote.post_id, models.Vote.user_id == current_user.id)
# if the user want ot like a post(the is statement below) but we already found the post(the found_vote) that means that he already liked this specific post
#so he cannot liked again and we will rise an HTTP exceptions.
    found_vote = vote_query.first()
# the logic when the vote direction is 1:
    if (vote.dir == 1):
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"user{current_user.id} has already voted on post with {vote.post_id}")
# if we didnt find the vote we will create a new vote
        new_vote = models.Vote(post_id = vote.post_id, user_id=current_user.id)   
# to ad the above changes to db
        db.add(new_vote)
        db.commit()
# send a message to the user
        return{"message": "successfully added vote"}
    else:
# if the vote does not exist
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"vote does not exist")
# if we found the vote we have to delete it
        vote_query.delete(synchronize_session=False)
        db.commit()
        return{"message": "successfully deleted vote"}
# dupa aceasta am importat vote.py in main.py si app.include_router(vote.router)-aici, mai jos in main.py, si sa verific in postman, autorization+bearer token/ min 09:47


