from typing import Any, Literal, NotRequired, TypedDict
from uuid import uuid4

from freqtrade.exchange.exchange import Exchange


class JobsContainer(TypedDict):
    category: Literal["pairlist", "download_data"]
    is_running: bool
    status: str
    progress: float | None
    progress_tasks: NotRequired[dict[str, Any]]
    result: Any
    error: str | None


class ApiBG:
    # Backtesting type: Backtesting
    bt: dict[str, Any] = {
        "bt": None,
        "data": None,
        "timerange": None,
        "last_config": {},
        "bt_error": None,
    }
    bgtask_running: bool = False
    # Exchange - only available in webserver mode.
    exchanges: dict[str, Exchange] = {}

    # Generic background jobs

    # TODO: Change this to TTLCache
    jobs: dict[str, JobsContainer] = {}
    # Pairlist evaluate things
    pairlist_running: bool = False
    download_data_running: bool = False

    @staticmethod
    def get_job_id() -> str:
        return str(uuid4())
