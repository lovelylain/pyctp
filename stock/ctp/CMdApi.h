#ifndef CMDAPI_H
#define CMDAPI_H

#include <Python.h>
#include "ThostFtdcMdApiSSE.h"

static inline void MdSpi_OnFrontConnected(PyObject *);
static inline void MdSpi_OnFrontDisconnected(PyObject *, int);
static inline void MdSpi_OnHeartBeatWarning(PyObject *, int);
static inline void MdSpi_OnRspUserLogin(PyObject *, CZQThostFtdcRspUserLoginField *, CZQThostFtdcRspInfoField *, int, bool);
static inline void MdSpi_OnRspUserLogout(PyObject *, CZQThostFtdcUserLogoutField *, CZQThostFtdcRspInfoField *, int, bool);
static inline void MdSpi_OnRspError(PyObject *, CZQThostFtdcRspInfoField *, int, bool);
static inline void MdSpi_OnRspSubMarketData(PyObject *, CZQThostFtdcSpecificInstrumentField *, CZQThostFtdcRspInfoField *, int, bool);
static inline void MdSpi_OnRspUnSubMarketData(PyObject *, CZQThostFtdcSpecificInstrumentField *, CZQThostFtdcRspInfoField *, int, bool);
static inline void MdSpi_OnRtnDepthMarketData(PyObject *, CZQThostFtdcDepthMarketDataField *);

class CMdSpi : public CZQThostFtdcMdSpi {
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

	virtual void OnRspUserLogin(CZQThostFtdcRspUserLoginField *pRspUserLogin, CZQThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		MdSpi_OnRspUserLogin(self, pRspUserLogin, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspUserLogout(CZQThostFtdcUserLogoutField *pUserLogout, CZQThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		MdSpi_OnRspUserLogout(self, pUserLogout, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspError(CZQThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		MdSpi_OnRspError(self, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspSubMarketData(CZQThostFtdcSpecificInstrumentField *pSpecificInstrument, CZQThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		MdSpi_OnRspSubMarketData(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspUnSubMarketData(CZQThostFtdcSpecificInstrumentField *pSpecificInstrument, CZQThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		MdSpi_OnRspUnSubMarketData(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRtnDepthMarketData(CZQThostFtdcDepthMarketDataField *pDepthMarketData) {
		MdSpi_OnRtnDepthMarketData(self, pDepthMarketData);
	}

private:
	PyObject *self;
};

static inline void ReleaseMdApi(CZQThostFtdcMdApi *api, CMdSpi *spi) {
	if (api) {
		api->RegisterSpi(NULL);
#ifndef _WIN32
		if (!spi) {api->Init(); usleep(100000);}
#endif
		api->Release();
		if (spi) delete spi;
	}
}

static const char *const PY_STRINGS[] = {"from_address", "DepthMarketData", "RspInfo", "RspUserLogin", "SpecificInstrument", "UserLogout"};

#endif /* CMDAPI_H */
