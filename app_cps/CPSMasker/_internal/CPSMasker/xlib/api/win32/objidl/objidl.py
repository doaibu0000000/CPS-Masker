from ctypes import POINTER, c_void_p
from ..wintypes import (GUID, DWORD, IUnknown, CLSID, interface, HRESULT, REFIID, BOOL, ULARGE_INTEGER)

@interface
class IStream(IUnknown):  #ISequentialStream
    IID = GUID('0000000c-0000-0000-c000-000000000046')


@interface
class IPersist(IUnknown):
    def GetClassID(self, pClassID : POINTER(CLSID) ) -> HRESULT: ...
    IID = GUID('0000010c-0000-0000-c000-000000000046')

@interface
class IPersistStream(IPersist):
    def IsDirty(self) -> HRESULT: ...
    def Load(self, pStm : IStream) -> HRESULT: ...
    def Save(self, pStm : IStream, fClearDirty : BOOL) -> HRESULT: ...
    def GetSizeMax(self, pcbSize : POINTER(ULARGE_INTEGER) ) -> HRESULT: ...
    IID = GUID('00000109-0000-0000-c000-000000000046')

@interface
class IMoniker(IPersistStream):

    def BindToObject(self,
        pbc : c_void_p, #IBindCtx
        pmkToLeft : IUnknown, #IMoniker,
        riidResult : REFIID,
        ppvResult : POINTER(c_void_p))  -> HRESULT: ...

    def BindToStorage(self,
        pbc : c_void_p, #IBindCtx
        pmkToLeft : IUnknown, #IMoniker,
        riid : REFIID,
        ppvObj : POINTER(c_void_p))  -> HRESULT: ...

    IID = GUID('0000000f-0000-0000-c000-000000000046')


@interface
class IEnumMoniker(IUnknown):

    def Next(self, celt : DWORD, rgelt : POINTER(IMoniker), pceltFetched : POINTER(DWORD)) -> HRESULT: ...


    IID = GUID('00000102-0000-0000-C000-000000000046')
