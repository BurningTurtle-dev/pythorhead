from typing import Any, List, Literal, Optional
from pythorhead.requestor import Request, Requestor

class Admin:
    def __init__(self, _requestor: Requestor):
        self._requestor = _requestor

    def list_applications(
        self,
        limit: Optional[int] = None,
        page: Optional[int] = None,
        unread_only: Optional[str] = None,
    ) -> Optional[dict]:
        """
        Pull applications from site. Note user must be admin.

        Args:
            limit (Optional[int], optional): Defaults to None.
            page (Optional[int], optional): Defaults to None.
            undread_only (Optional[str], optional): Must be "true" or "false". Defaults to false
        Returns:
            dict: list applications
        """
        params: dict[str, Any] = {key: value for key, value in locals().items() if value is not None and key != "self"}
        return self._requestor.api(Request.GET, "/admin/registration_application/list", params=params)
    
    def accept_application(
        self,
        user_id: int,
        approve: Optional[bool] = True,
        deny_reason: Optional[str] = None
    ) -> Optional[dict]:
        process_application: dict[str, Any] = {"id": id, "approve": approve}

        if id is not None:
            process_application["id"] = user_id
        if approve is not None:
            process_application["approve"] = approve

        print (process_application)
        return self._requestor.api(
            Request.POST,
            "/admin/registration_application/approve",
            json=process_application
        )
