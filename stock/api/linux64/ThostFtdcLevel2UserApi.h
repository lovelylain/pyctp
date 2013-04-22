/////////////////////////////////////////////////////////////////////////
///@system LEVEL2行情API
///@company 上海期货信息技术有限公司
///@file ThostFtdcLevel2UserApi.h
///@brief 定义了客户端接口
///@history 
///20060106	赵鸿昊		创建该文件
/////////////////////////////////////////////////////////////////////////

#ifndef THOST_FTDCLEVEL2USERAPI_H
#define THOST_FTDCLEVEL2USERAPI_H

#include "ThostFtdcLevel2UserApiStruct.h"

_LEVEL2_NS_BEGIN_
#if defined(LEVEL2_USERAPI_IS_LIB) && defined(WINDOWS)
#ifdef LIB_LEVEL2_USER_API_EXPORT
#define LEVEL2_USER_API_EXPORT __declspec(dllexport)
#else
#define LEVEL2_USER_API_EXPORT __declspec(dllimport)
#endif
#else
#define LEVEL2_USER_API_EXPORT 
#endif

class CThostFtdcLevel2UserSpi
{
public:
	virtual ~CThostFtdcLevel2UserSpi() {};
	///当客户端与交易后台建立起通信连接时（还未登录前），该方法被调用。
	virtual void OnFrontConnected(){};
	
	///当客户端与交易后台通信连接断开时，该方法被调用。当发生这个情况后，API会自动重新连接，客户端可不做处理。
	///@param nReason 错误原因
	///        0x1001 网络读失败
	///        0x1002 网络写失败
	///        0x2001 接收心跳超时
	///        0x2002 发送心跳失败
	///        0x2003 收到错误报文
	virtual void OnFrontDisconnected(int nReason){};
		
	///心跳超时警告。当长时间未收到报文时，该方法被调用。
	///@param nTimeLapse 距离上次接收报文的时间
	virtual void OnHeartBeatWarning(int nTimeLapse){};
	
	///客户端认证响应
	//virtual void OnRspAuthenticate(CThostFtdcRspAuthenticateField *pRspAuthenticate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
	

	///登录请求响应
	virtual void OnRspUserLogin(CThostFtdcRspUserLoginField *pRspUserLogin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};

	///登出请求响应
	virtual void OnRspUserLogout(CThostFtdcUserLogoutField *pUserLogout, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};

	///错误应答
	virtual void OnRspError(CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};

	///订阅Level2行情应答
	virtual void OnRspSubLevel2MarketData(CThostFtdcSpecificSecurityField *pSpecificSecurity, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};

	///取消订阅Level2行情应答
	virtual void OnRspUnSubLevel2MarketData(CThostFtdcSpecificSecurityField *pSpecificSecurity, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};

	///订阅Level2指数行情应答
	virtual void OnRspSubNGTSIndex(CThostFtdcSpecificSecurityField *pSpecificSecurity, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};

	///取消订阅Level2指数行情应答
	virtual void OnRspUnSubNGTSIndex(CThostFtdcSpecificSecurityField *pSpecificSecurity, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};

	///Level2行情通知
	virtual void OnRtnLevel2MarketData(CThostFtdcLevel2MarketDataField *pLevel2MarketData) {};

	///Level2指数行情通知
	virtual void OnRtnNGTSIndex(CThostFtdcNGTSIndexField *pNGTSIndex) {};
};

class LEVEL2_USER_API_EXPORT CThostFtdcLevel2UserApi
{
public:
	///创建UserApi
	///@param pszFlowPath 存贮订阅信息文件的目录，默认为当前目录
	///@return 创建出的UserApi
	//modify for udp marketdata
	static CThostFtdcLevel2UserApi *CreateFtdcLevel2UserApi(const char *pszFlowPath = "", const bool bIsUsingUdp=false);
	
	///删除接口对象本身
	///@remark 不再使用本接口对象时,调用该函数删除接口对象
	virtual void Release() = 0;
	
	///初始化
	///@remark 初始化运行环境,只有调用后,接口才开始工作
	virtual void Init() = 0;
	
	///等待接口线程结束运行
	///@return 线程退出代码
	virtual int Join() = 0;
	
	///获取当前交易日
	///@retrun 获取到的交易日
	///@remark 只有登录成功后,才能得到正确的交易日
	virtual const char *GetTradingDay() = 0;
	
	///注册前置机网络地址
	///@param pszFrontAddress：前置机网络地址。
	///@remark 网络地址的格式为：“protocol://ipaddress:port”，如：”tcp://127.0.0.1:17001”。 
	///@remark “tcp”代表传输协议，“127.0.0.1”代表服务器地址。”17001”代表服务器端口号。
	virtual void RegisterFront(char *pszFrontAddress) = 0;
	
	///注册名字服务器网络地址
	///@param pszNsAddress：名字服务器网络地址。
	///@remark 网络地址的格式为：“protocol://ipaddress:port”，如：”tcp://127.0.0.1:12001”。 
	///@remark “tcp”代表传输协议，“127.0.0.1”代表服务器地址。”12001”代表服务器端口号。
	///@remark RegisterNameServer优先于RegisterFront
	//virtual void RegisterNameServer(char *pszNsAddress) = 0;
	
	///注册回调接口
	///@param pSpi 派生自回调接口类的实例
	virtual void RegisterSpi(CThostFtdcLevel2UserSpi *pSpi) = 0;
	
	virtual int SubscribeLevel2MarketData(CThostFtdcSpecificSecurityField *pSecurityList, int nCount) = 0;

	virtual int UnSubscribeLevel2MarketData(CThostFtdcSpecificSecurityField *pSecurityList, int nCount) = 0;
	
	virtual int SubscribeNGTSIndex(CThostFtdcSpecificSecurityField *pSecurityList, int nCount) = 0;

	virtual int UnSubscribeNGTSIndex(CThostFtdcSpecificSecurityField *pSecurityList, int nCount) = 0;
	
	///订阅公共流。
	///@param nResumeType 公共流重传方式  
	///        THOST_TERT_RESTART:从本交易日开始重传
	///        THOST_TERT_RESUME:从上次收到的续传
	///        THOST_TERT_QUICK:只传送登录后公共流的内容
	///@remark 该方法要在Init方法前调用。若不调用则不会收到公共流的数据。
	virtual void SubscribePublicTopic(THOST_TE_RESUME_TYPE nResumeType) = 0;

	///客户端认证请求
	//virtual int ReqAuthenticate(CThostFtdcReqAuthenticateField *pReqAuthenticate, int nRequestID) = 0;
	
	///用户登录请求
	virtual int ReqUserLogin(CThostFtdcReqUserLoginField *pReqUserLogin, int nRequestID) = 0;

	///登出请求
	virtual int ReqUserLogout(CThostFtdcUserLogoutField *pUserLogout, int nRequestID) = 0;
protected:
	~CThostFtdcLevel2UserApi(){};
};

_LEVEL2_NS_END_
#endif

