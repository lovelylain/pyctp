#ifndef CUSERAPI_H
#define CUSERAPI_H

#include <Python.h>
#include "ThostFtdcLevel2UserApi.h"

_USING_LEVEL2_NS_
static inline void UserSpi_OnFrontConnected(PyObject *);
static inline void UserSpi_OnFrontDisconnected(PyObject *, int);
static inline void UserSpi_OnHeartBeatWarning(PyObject *, int);
static inline void UserSpi_OnRspUserLogin(PyObject *, CThostFtdcRspUserLoginField *, CThostFtdcRspInfoField *, int, bool);
static inline void UserSpi_OnRspUserLogout(PyObject *, CThostFtdcUserLogoutField *, CThostFtdcRspInfoField *, int, bool);
static inline void UserSpi_OnRspError(PyObject *, CThostFtdcRspInfoField *, int, bool);
static inline void UserSpi_OnRspSubLevel2MarketData(PyObject *, CThostFtdcSpecificSecurityField *, CThostFtdcRspInfoField *, int, bool);
static inline void UserSpi_OnRspUnSubLevel2MarketData(PyObject *, CThostFtdcSpecificSecurityField *, CThostFtdcRspInfoField *, int, bool);
static inline void UserSpi_OnRspSubNGTSIndex(PyObject *, CThostFtdcSpecificSecurityField *, CThostFtdcRspInfoField *, int, bool);
static inline void UserSpi_OnRspUnSubNGTSIndex(PyObject *, CThostFtdcSpecificSecurityField *, CThostFtdcRspInfoField *, int, bool);
static inline void UserSpi_OnRtnLevel2MarketData(PyObject *, CThostFtdcLevel2MarketDataField *);
static inline void UserSpi_OnRtnNGTSIndex(PyObject *, CThostFtdcNGTSIndexField *);

class CUserSpi : public CThostFtdcLevel2UserSpi {
public:
	CUserSpi(PyObject *obj):self(obj) {}
	virtual ~CUserSpi() {}

	virtual void OnFrontConnected() {
		UserSpi_OnFrontConnected(self);
	}

	virtual void OnFrontDisconnected(int nReason) {
		UserSpi_OnFrontDisconnected(self, nReason);
	}

	virtual void OnHeartBeatWarning(int nTimeLapse) {
		UserSpi_OnHeartBeatWarning(self, nTimeLapse);
	}

	virtual void OnRspUserLogin(CThostFtdcRspUserLoginField *pRspUserLogin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		UserSpi_OnRspUserLogin(self, pRspUserLogin, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspUserLogout(CThostFtdcUserLogoutField *pUserLogout, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		UserSpi_OnRspUserLogout(self, pUserLogout, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspError(CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		UserSpi_OnRspError(self, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspSubLevel2MarketData(CThostFtdcSpecificSecurityField *pSpecificSecurity, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		UserSpi_OnRspSubLevel2MarketData(self, pSpecificSecurity, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspUnSubLevel2MarketData(CThostFtdcSpecificSecurityField *pSpecificSecurity, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		UserSpi_OnRspUnSubLevel2MarketData(self, pSpecificSecurity, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspSubNGTSIndex(CThostFtdcSpecificSecurityField *pSpecificSecurity, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		UserSpi_OnRspSubNGTSIndex(self, pSpecificSecurity, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspUnSubNGTSIndex(CThostFtdcSpecificSecurityField *pSpecificSecurity, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		UserSpi_OnRspUnSubNGTSIndex(self, pSpecificSecurity, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRtnLevel2MarketData(CThostFtdcLevel2MarketDataField *pLevel2MarketData) {
		UserSpi_OnRtnLevel2MarketData(self, pLevel2MarketData);
	}

	virtual void OnRtnNGTSIndex(CThostFtdcNGTSIndexField *pNGTSIndex) {
		UserSpi_OnRtnNGTSIndex(self, pNGTSIndex);
	}

private:
	PyObject *self;
};

static inline void ReleaseUserApi(CThostFtdcLevel2UserApi *api, CUserSpi *spi) {
	if (api) {
		api->RegisterSpi(NULL);
#ifndef _WIN32
		if (!spi) {api->Init(); usleep(100000);}
#endif
		api->Release();
		if (spi) delete spi;
	}
}

static const char *const PY_STRINGS[] = {"from_address", "Level2MarketData", "NGTSIndex", "RspInfo", "RspUserLogin", "SpecificSecurity", "UserLogout"};

#endif /* CUSERAPI_H */
