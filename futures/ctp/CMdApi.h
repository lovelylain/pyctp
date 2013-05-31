#ifndef CMDAPI_H
#define CMDAPI_H

#include <Python.h>
#include "ThostFtdcMdApi.h"

static inline void MdSpi_OnFrontConnected(PyObject *);
static inline void MdSpi_OnFrontDisconnected(PyObject *, int);
static inline void MdSpi_OnHeartBeatWarning(PyObject *, int);
static inline void MdSpi_OnRspUserLogin(PyObject *, CThostFtdcRspUserLoginField *, CThostFtdcRspInfoField *, int, bool);
static inline void MdSpi_OnRspUserLogout(PyObject *, CThostFtdcUserLogoutField *, CThostFtdcRspInfoField *, int, bool);
static inline void MdSpi_OnRspError(PyObject *, CThostFtdcRspInfoField *, int, bool);
static inline void MdSpi_OnRspSubMarketData(PyObject *, CThostFtdcSpecificInstrumentField *, CThostFtdcRspInfoField *, int, bool);
static inline void MdSpi_OnRspUnSubMarketData(PyObject *, CThostFtdcSpecificInstrumentField *, CThostFtdcRspInfoField *, int, bool);
static inline void MdSpi_OnRtnDepthMarketData(PyObject *, CThostFtdcDepthMarketDataField *);

class CMdSpi : public CThostFtdcMdSpi {
public:
	CMdSpi(PyObject *obj):self(obj) {}
	virtual ~CMdSpi() {}

	virtual void OnFrontConnected() {
		MdSpi_OnFrontConnected(self);
	}

	virtual void OnFrontDisconnected(int nReason) {
		MdSpi_OnFrontDisconnected(self, nReason);
	}

	virtual void OnHeartBeatWarning(int nTimeLapse) {
		MdSpi_OnHeartBeatWarning(self, nTimeLapse);
	}

	virtual void OnRspUserLogin(CThostFtdcRspUserLoginField *pRspUserLogin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		MdSpi_OnRspUserLogin(self, pRspUserLogin, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspUserLogout(CThostFtdcUserLogoutField *pUserLogout, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		MdSpi_OnRspUserLogout(self, pUserLogout, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspError(CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		MdSpi_OnRspError(self, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspSubMarketData(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		MdSpi_OnRspSubMarketData(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspUnSubMarketData(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		MdSpi_OnRspUnSubMarketData(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRtnDepthMarketData(CThostFtdcDepthMarketDataField *pDepthMarketData) {
		MdSpi_OnRtnDepthMarketData(self, pDepthMarketData);
	}

private:
	PyObject *self;
};

static inline void ReleaseMdApi(CThostFtdcMdApi *api, CMdSpi *spi) {
	if (api) {
		api->RegisterSpi(NULL);
#ifndef _WIN32
		if (!spi) {api->Init(); usleep(100000);}
#endif
		api->Release();
		if (spi) delete spi;
	}
}

#define CheckMemory(p) (p || PyErr_NoMemory())
#if PY_MAJOR_VERSION < 3
#define XStr PyString_FromString
#else
#define XStr PyUnicode_FromString
#endif

#define S_dot "."
#define S_ApiStruct ".ApiStruct"
#define S___name__ "__name__"
#define S_rpartition "rpartition"
#define S_ctypes "ctypes"
#define S_addressof "addressof"
#define S_from_address "from_address"
#define S_DepthMarketData "DepthMarketData"
#define S_RspInfo "RspInfo"
#define S_RspUserLogin "RspUserLogin"
#define S_SpecificInstrument "SpecificInstrument"
#define S_UserLogout "UserLogout"

#endif /* CMDAPI_H */
