from fastapi import (
    APIRouter,
    Body,
    Depends,
)
from ..schemas import (
    ErrorResponse,
    ParsingRequest,
    ParsingResponse,
    ParsingHistory,
    ParsingHistoryResponse,
)
from ..auth import auth
from ..parsing import parsing
from ..database import methods as db_methods


router = APIRouter()


@router.post(
    "/parse/data", 
    response_model=ParsingResponse | ErrorResponse,
    dependencies=[Depends(auth.auth)],
)
def parse_html(data: ParsingRequest = Body(), uuid: str = Depends(auth.parse_uuid)):
    try:
        filter_data = parsing.filter_and_sorting_data(url=data.url)
    except:
        return ErrorResponse(message="Error while parsing data")
    if data.save:
        try:
            assert db_methods.db_add_parsing_result(uuid, filter_data, data.url)
        except:
            return ErrorResponse(message="Error while saving data")
    return ParsingResponse(data=filter_data, url=data.url)


@router.get(
    "/parse/history", 
    response_model=ParsingHistoryResponse | ErrorResponse,
    dependencies=[Depends(auth.auth)],
)
def parse_html(uuid: str = Depends(auth.parse_uuid)):
    data = [ParsingHistory(id=el[0], url=el[1]) for el in db_methods.db_get_parsing_ids(uuid)]
    return ParsingHistoryResponse(data=data)


@router.get(
    "/parse/history/{id}", 
    response_model=ParsingResponse | ErrorResponse,
    dependencies=[Depends(auth.auth)],
)
def parse_html(id: int, uuid: str = Depends(auth.parse_uuid)):
    if id > db_methods.db_get_last_notice():
        return ErrorResponse(message="This entry does not exist")
    result = db_methods.db_get_parsing_result(uuid, id)
    if not result:
        return ErrorResponse(message="This entry does not belong to the user")
    data = parsing.organize_from_db_data(result)
    return ParsingResponse(data=data, url=result[2])
