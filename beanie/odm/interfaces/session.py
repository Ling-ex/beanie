from typing import Optional

from async_pymongo.client_session import AsyncClientSession


class SessionMethods:
    """
    Session methods
    """

    def set_session(self, session: Optional[AsyncClientSession] = None):
        """
        Set session
        :param session: Optional[AsyncClientSession] - async_pymongo session
        :return:
        """
        if session is not None:
            self.session: Optional[AsyncClientSession] = session
        return self
