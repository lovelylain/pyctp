# -*- coding: utf-8 -*-

from __future__ import absolute_import as _init

__author__ = 'lovelylain'
__version__ = '0.1.0'

def ACOS(Real):
    """ACOS(Real) -> (BegIdx, Real)

    TA_ACOS - Vector Trigonometric ACos
    Input  = double
    Output = double
    """
    return None, 1

def ACOS_Lookback():
    """ACOS_Lookback() -> int"""
    return -1

def AD(High, Low, Close, Volume):
    """AD(High, Low, Close, Volume) -> (BegIdx, Real)

    TA_AD - Chaikin A/D Line
    Input  = High, Low, Close, Volume
    Output = double
    """
    return None, 1

def AD_Lookback():
    """AD_Lookback() -> int"""
    return -1

def ADD(Real0, Real1):
    """ADD(Real0, Real1) -> (BegIdx, Real)

    TA_ADD - Vector Arithmetic Add
    Input  = double, double
    Output = double
    """
    return None, 1

def ADD_Lookback():
    """ADD_Lookback() -> int"""
    return -1

def ADOSC(High, Low, Close, Volume, FastPeriod, SlowPeriod):
    """ADOSC(High, Low, Close, Volume[, FastPeriod, SlowPeriod]) -> (BegIdx, Real)

    TA_ADOSC - Chaikin A/D Oscillator
    Input  = High, Low, Close, Volume
    Output = double
    Optional Parameters
    -------------------
    optInFastPeriod:(From 2 to 100000)
       Number of period for the fast MA
    optInSlowPeriod:(From 2 to 100000)
       Number of period for the slow MA
    """
    return None, 1

def ADOSC_Lookback(FastPeriod, SlowPeriod):
    """ADOSC_Lookback([FastPeriod, SlowPeriod]) -> int"""
    return -1

def ADX(High, Low, Close, TimePeriod):
    """ADX(High, Low, Close[, TimePeriod]) -> (BegIdx, Real)

    TA_ADX - Average Directional Movement Index
    Input  = High, Low, Close
    Output = double
    Optional Parameters
    -------------------
    optInTimePeriod:(From 2 to 100000)
       Number of period
    """
    return None, 1

def ADX_Lookback(TimePeriod):
    """ADX_Lookback([TimePeriod]) -> int"""
    return -1

def ADXR(High, Low, Close, TimePeriod):
    """ADXR(High, Low, Close[, TimePeriod]) -> (BegIdx, Real)

    TA_ADXR - Average Directional Movement Index Rating
    Input  = High, Low, Close
    Output = double
    Optional Parameters
    -------------------
    optInTimePeriod:(From 2 to 100000)
       Number of period
    """
    return None, 1

def ADXR_Lookback(TimePeriod):
    """ADXR_Lookback([TimePeriod]) -> int"""
    return -1

def APO(Real, FastPeriod, SlowPeriod, MAType):
    """APO(Real[, FastPeriod, SlowPeriod, MAType]) -> (BegIdx, Real)

    TA_APO - Absolute Price Oscillator
    Input  = double
    Output = double
    Optional Parameters
    -------------------
    optInFastPeriod:(From 2 to 100000)
       Number of period for the fast MA
    optInSlowPeriod:(From 2 to 100000)
       Number of period for the slow MA
    optInMAType:
       Type of Moving Average
    """
    return None, 1

def APO_Lookback(FastPeriod, SlowPeriod, MAType):
    """APO_Lookback([FastPeriod, SlowPeriod, MAType]) -> int"""
    return -1

def AROON(High, Low, TimePeriod):
    """AROON(High, Low[, TimePeriod]) -> (BegIdx, AroonDown, AroonUp)

    TA_AROON - Aroon
    Input  = High, Low
    Output = double, double
    Optional Parameters
    -------------------
    optInTimePeriod:(From 2 to 100000)
       Number of period
    """
    return None, 1, None

def AROON_Lookback(TimePeriod):
    """AROON_Lookback([TimePeriod]) -> int"""
    return -1

def AROONOSC(High, Low, TimePeriod):
    """AROONOSC(High, Low[, TimePeriod]) -> (BegIdx, Real)

    TA_AROONOSC - Aroon Oscillator
    Input  = High, Low
    Output = double
    Optional Parameters
    -------------------
    optInTimePeriod:(From 2 to 100000)
       Number of period
    """
    return None, 1

def AROONOSC_Lookback(TimePeriod):
    """AROONOSC_Lookback([TimePeriod]) -> int"""
    return -1

def ASIN(Real):
    """ASIN(Real) -> (BegIdx, Real)

    TA_ASIN - Vector Trigonometric ASin
    Input  = double
    Output = double
    """
    return None, 1

def ASIN_Lookback():
    """ASIN_Lookback() -> int"""
    return -1

def ATAN(Real):
    """ATAN(Real) -> (BegIdx, Real)

    TA_ATAN - Vector Trigonometric ATan
    Input  = double
    Output = double
    """
    return None, 1

def ATAN_Lookback():
    """ATAN_Lookback() -> int"""
    return -1

def ATR(High, Low, Close, TimePeriod):
    """ATR(High, Low, Close[, TimePeriod]) -> (BegIdx, Real)

    TA_ATR - Average True Range
    Input  = High, Low, Close
    Output = double
    Optional Parameters
    -------------------
    optInTimePeriod:(From 1 to 100000)
       Number of period
    """
    return None, 1

def ATR_Lookback(TimePeriod):
    """ATR_Lookback([TimePeriod]) -> int"""
    return -1

def AVGPRICE(Open, High, Low, Close):
    """AVGPRICE(Open, High, Low, Close) -> (BegIdx, Real)

    TA_AVGPRICE - Average Price
    Input  = Open, High, Low, Close
    Output = double
    """
    return None, 1

def AVGPRICE_Lookback():
    """AVGPRICE_Lookback() -> int"""
    return -1

def BBANDS(Real, TimePeriod, NbDevUp, NbDevDn, MAType):
    """BBANDS(Real[, TimePeriod, NbDevUp, NbDevDn, MAType]) -> (BegIdx, RealUpperBand, RealMiddleBand, RealLowerBand)

    TA_BBANDS - Bollinger Bands
    Input  = double
    Output = double, double, double
    Optional Parameters
    -------------------
    optInTimePeriod:(From 2 to 100000)
       Number of period
    optInNbDevUp:(From TA_REAL_MIN to TA_REAL_MAX)
       Deviation multiplier for upper band
    optInNbDevDn:(From TA_REAL_MIN to TA_REAL_MAX)
       Deviation multiplier for lower band
    optInMAType:
       Type of Moving Average
    """
    return None, 1, None, None

def BBANDS_Lookback(TimePeriod, NbDevUp, NbDevDn, MAType):
    """BBANDS_Lookback([TimePeriod, NbDevUp, NbDevDn, MAType]) -> int"""
    return -1

def BETA(Real0, Real1, TimePeriod):
    """BETA(Real0, Real1[, TimePeriod]) -> (BegIdx, Real)

    TA_BETA - Beta
    Input  = double, double
    Output = double
    Optional Parameters
    -------------------
    optInTimePeriod:(From 1 to 100000)
       Number of period
    """
    return None, 1

def BETA_Lookback(TimePeriod):
    """BETA_Lookback([TimePeriod]) -> int"""
    return -1

def BOP(Open, High, Low, Close):
    """BOP(Open, High, Low, Close) -> (BegIdx, Real)

    TA_BOP - Balance Of Power
    Input  = Open, High, Low, Close
    Output = double
    """
    return None, 1

def BOP_Lookback():
    """BOP_Lookback() -> int"""
    return -1

def CCI(High, Low, Close, TimePeriod):
    """CCI(High, Low, Close[, TimePeriod]) -> (BegIdx, Real)

    TA_CCI - Commodity Channel Index
    Input  = High, Low, Close
    Output = double
    Optional Parameters
    -------------------
    optInTimePeriod:(From 2 to 100000)
       Number of period
    """
    return None, 1

def CCI_Lookback(TimePeriod):
    """CCI_Lookback([TimePeriod]) -> int"""
    return -1

def CDL2CROWS(Open, High, Low, Close):
    """CDL2CROWS(Open, High, Low, Close) -> (BegIdx, Integer)

    TA_CDL2CROWS - Two Crows
    Input  = Open, High, Low, Close
    Output = int
    """
    return None, 1

def CDL2CROWS_Lookback():
    """CDL2CROWS_Lookback() -> int"""
    return -1

def CDL3BLACKCROWS(Open, High, Low, Close):
    """CDL3BLACKCROWS(Open, High, Low, Close) -> (BegIdx, Integer)

    TA_CDL3BLACKCROWS - Three Black Crows
    Input  = Open, High, Low, Close
    Output = int
    """
    return None, 1

def CDL3BLACKCROWS_Lookback():
    """CDL3BLACKCROWS_Lookback() -> int"""
    return -1

def CDL3INSIDE(Open, High, Low, Close):
    """CDL3INSIDE(Open, High, Low, Close) -> (BegIdx, Integer)

    TA_CDL3INSIDE - Three Inside Up/Down
    Input  = Open, High, Low, Close
    Output = int
    """
    return None, 1

def CDL3INSIDE_Lookback():
    """CDL3INSIDE_Lookback() -> int"""
    return -1

def CDL3LINESTRIKE(Open, High, Low, Close):
    """CDL3LINESTRIKE(Open, High, Low, Close) -> (BegIdx, Integer)

    TA_CDL3LINESTRIKE - Three-Line Strike 
    Input  = Open, High, Low, Close
    Output = int
    """
    return None, 1

def CDL3LINESTRIKE_Lookback():
    """CDL3LINESTRIKE_Lookback() -> int"""
    return -1

def CDL3OUTSIDE(Open, High, Low, Close):
    """CDL3OUTSIDE(Open, High, Low, Close) -> (BegIdx, Integer)

    TA_CDL3OUTSIDE - Three Outside Up/Down
    Input  = Open, High, Low, Close
    Output = int
    """
    return None, 1

def CDL3OUTSIDE_Lookback():
    """CDL3OUTSIDE_Lookback() -> int"""
    return -1

def CDL3STARSINSOUTH(Open, High, Low, Close):
    """CDL3STARSINSOUTH(Open, High, Low, Close) -> (BegIdx, Integer)

    TA_CDL3STARSINSOUTH - Three Stars In The South
    Input  = Open, High, Low, Close
    Output = int
    """
    return None, 1

def CDL3STARSINSOUTH_Lookback():
    """CDL3STARSINSOUTH_Lookback() -> int"""
    return -1

def CDL3WHITESOLDIERS(Open, High, Low, Close):
    """CDL3WHITESOLDIERS(Open, High, Low, Close) -> (BegIdx, Integer)

    TA_CDL3WHITESOLDIERS - Three Advancing White Soldiers
    Input  = Open, High, Low, Close
    Output = int
    """
    return None, 1

def CDL3WHITESOLDIERS_Lookback():
    """CDL3WHITESOLDIERS_Lookback() -> int"""
    return -1

def CDLABANDONEDBABY(Open, High, Low, Close, Penetration):
    """CDLABANDONEDBABY(Open, High, Low, Close[, Penetration]) -> (BegIdx, Integer)

    TA_CDLABANDONEDBABY - Abandoned Baby
    Input  = Open, High, Low, Close
    Output = int
    Optional Parameters
    -------------------
    optInPenetration:(From 0 to TA_REAL_MAX)
       Percentage of penetration of a candle within another candle
    """
    return None, 1

def CDLABANDONEDBABY_Lookback(Penetration):
    """CDLABANDONEDBABY_Lookback([Penetration]) -> int"""
    return -1

def CDLADVANCEBLOCK(Open, High, Low, Close):
    """CDLADVANCEBLOCK(Open, High, Low, Close) -> (BegIdx, Integer)

    TA_CDLADVANCEBLOCK - Advance Block
    Input  = Open, High, Low, Close
    Output = int
    """
    return None, 1

def CDLADVANCEBLOCK_Lookback():
    """CDLADVANCEBLOCK_Lookback() -> int"""
    return -1

def CDLBELTHOLD(Open, High, Low, Close):
    """CDLBELTHOLD(Open, High, Low, Close) -> (BegIdx, Integer)

    TA_CDLBELTHOLD - Belt-hold
    Input  = Open, High, Low, Close
    Output = int
    """
    return None, 1

def CDLBELTHOLD_Lookback():
    """CDLBELTHOLD_Lookback() -> int"""
    return -1

def CDLBREAKAWAY(Open, High, Low, Close):
    """CDLBREAKAWAY(Open, High, Low, Close) -> (BegIdx, Integer)

    TA_CDLBREAKAWAY - Breakaway
    Input  = Open, High, Low, Close
    Output = int
    """
    return None, 1

def CDLBREAKAWAY_Lookback():
    """CDLBREAKAWAY_Lookback() -> int"""
    return -1

def CDLCLOSINGMARUBOZU(Open, High, Low, Close):
    """CDLCLOSINGMARUBOZU(Open, High, Low, Close) -> (BegIdx, Integer)

    TA_CDLCLOSINGMARUBOZU - Closing Marubozu
    Input  = Open, High, Low, Close
    Output = int
    """
    return None, 1

def CDLCLOSINGMARUBOZU_Lookback():
    """CDLCLOSINGMARUBOZU_Lookback() -> int"""
    return -1

def CDLCONCEALBABYSWALL(Open, High, Low, Close):
    """CDLCONCEALBABYSWALL(Open, High, Low, Close) -> (BegIdx, Integer)

    TA_CDLCONCEALBABYSWALL - Concealing Baby Swallow
    Input  = Open, High, Low, Close
    Output = int
    """
    return None, 1

def CDLCONCEALBABYSWALL_Lookback():
    """CDLCONCEALBABYSWALL_Lookback() -> int"""
    return -1

def CDLCOUNTERATTACK(Open, High, Low, Close):
    """CDLCOUNTERATTACK(Open, High, Low, Close) -> (BegIdx, Integer)

    TA_CDLCOUNTERATTACK - Counterattack
    Input  = Open, High, Low, Close
    Output = int
    """
    return None, 1

def CDLCOUNTERATTACK_Lookback():
    """CDLCOUNTERATTACK_Lookback() -> int"""
    return -1

def CDLDARKCLOUDCOVER(Open, High, Low, Close, Penetration):
    """CDLDARKCLOUDCOVER(Open, High, Low, Close[, Penetration]) -> (BegIdx, Integer)

    TA_CDLDARKCLOUDCOVER - Dark Cloud Cover
    Input  = Open, High, Low, Close
    Output = int
    Optional Parameters
    -------------------
    optInPenetration:(From 0 to TA_REAL_MAX)
       Percentage of penetration of a candle within another candle
    """
    return None, 1

def CDLDARKCLOUDCOVER_Lookback(Penetration):
    """CDLDARKCLOUDCOVER_Lookback([Penetration]) -> int"""
    return -1

def CDLDOJI(Open, High, Low, Close):
    """CDLDOJI(Open, High, Low, Close) -> (BegIdx, Integer)

    TA_CDLDOJI - Doji
    Input  = Open, High, Low, Close
    Output = int
    """
    return None, 1

def CDLDOJI_Lookback():
    """CDLDOJI_Lookback() -> int"""
    return -1

def CDLDOJISTAR(Open, High, Low, Close):
    """CDLDOJISTAR(Open, High, Low, Close) -> (BegIdx, Integer)

    TA_CDLDOJISTAR - Doji Star
    Input  = Open, High, Low, Close
    Output = int
    """
    return None, 1

def CDLDOJISTAR_Lookback():
    """CDLDOJISTAR_Lookback() -> int"""
    return -1

def CDLDRAGONFLYDOJI(Open, High, Low, Close):
    """CDLDRAGONFLYDOJI(Open, High, Low, Close) -> (BegIdx, Integer)

    TA_CDLDRAGONFLYDOJI - Dragonfly Doji
    Input  = Open, High, Low, Close
    Output = int
    """
    return None, 1

def CDLDRAGONFLYDOJI_Lookback():
    """CDLDRAGONFLYDOJI_Lookback() -> int"""
    return -1

def CDLENGULFING(Open, High, Low, Close):
    """CDLENGULFING(Open, High, Low, Close) -> (BegIdx, Integer)

    TA_CDLENGULFING - Engulfing Pattern
    Input  = Open, High, Low, Close
    Output = int
    """
    return None, 1

def CDLENGULFING_Lookback():
    """CDLENGULFING_Lookback() -> int"""
    return -1

def CDLEVENINGDOJISTAR(Open, High, Low, Close, Penetration):
    """CDLEVENINGDOJISTAR(Open, High, Low, Close[, Penetration]) -> (BegIdx, Integer)

    TA_CDLEVENINGDOJISTAR - Evening Doji Star
    Input  = Open, High, Low, Close
    Output = int
    Optional Parameters
    -------------------
    optInPenetration:(From 0 to TA_REAL_MAX)
       Percentage of penetration of a candle within another candle
    """
    return None, 1

def CDLEVENINGDOJISTAR_Lookback(Penetration):
    """CDLEVENINGDOJISTAR_Lookback([Penetration]) -> int"""
    return -1

def CDLEVENINGSTAR(Open, High, Low, Close, Penetration):
    """CDLEVENINGSTAR(Open, High, Low, Close[, Penetration]) -> (BegIdx, Integer)

    TA_CDLEVENINGSTAR - Evening Star
    Input  = Open, High, Low, Close
    Output = int
    Optional Parameters
    -------------------
    optInPenetration:(From 0 to TA_REAL_MAX)
       Percentage of penetration of a candle within another candle
    """
    return None, 1

def CDLEVENINGSTAR_Lookback(Penetration):
    """CDLEVENINGSTAR_Lookback([Penetration]) -> int"""
    return -1

def CDLGAPSIDESIDEWHITE(Open, High, Low, Close):
    """CDLGAPSIDESIDEWHITE(Open, High, Low, Close) -> (BegIdx, Integer)

    TA_CDLGAPSIDESIDEWHITE - Up/Down-gap side-by-side white lines
    Input  = Open, High, Low, Close
    Output = int
    """
    return None, 1

def CDLGAPSIDESIDEWHITE_Lookback():
    """CDLGAPSIDESIDEWHITE_Lookback() -> int"""
    return -1

def CDLGRAVESTONEDOJI(Open, High, Low, Close):
    """CDLGRAVESTONEDOJI(Open, High, Low, Close) -> (BegIdx, Integer)

    TA_CDLGRAVESTONEDOJI - Gravestone Doji
    Input  = Open, High, Low, Close
    Output = int
    """
    return None, 1

def CDLGRAVESTONEDOJI_Lookback():
    """CDLGRAVESTONEDOJI_Lookback() -> int"""
    return -1

def CDLHAMMER(Open, High, Low, Close):
    """CDLHAMMER(Open, High, Low, Close) -> (BegIdx, Integer)

    TA_CDLHAMMER - Hammer
    Input  = Open, High, Low, Close
    Output = int
    """
    return None, 1

def CDLHAMMER_Lookback():
    """CDLHAMMER_Lookback() -> int"""
    return -1

def CDLHANGINGMAN(Open, High, Low, Close):
    """CDLHANGINGMAN(Open, High, Low, Close) -> (BegIdx, Integer)

    TA_CDLHANGINGMAN - Hanging Man
    Input  = Open, High, Low, Close
    Output = int
    """
    return None, 1

def CDLHANGINGMAN_Lookback():
    """CDLHANGINGMAN_Lookback() -> int"""
    return -1

def CDLHARAMI(Open, High, Low, Close):
    """CDLHARAMI(Open, High, Low, Close) -> (BegIdx, Integer)

    TA_CDLHARAMI - Harami Pattern
    Input  = Open, High, Low, Close
    Output = int
    """
    return None, 1

def CDLHARAMI_Lookback():
    """CDLHARAMI_Lookback() -> int"""
    return -1

def CDLHARAMICROSS(Open, High, Low, Close):
    """CDLHARAMICROSS(Open, High, Low, Close) -> (BegIdx, Integer)

    TA_CDLHARAMICROSS - Harami Cross Pattern
    Input  = Open, High, Low, Close
    Output = int
    """
    return None, 1

def CDLHARAMICROSS_Lookback():
    """CDLHARAMICROSS_Lookback() -> int"""
    return -1

def CDLHIGHWAVE(Open, High, Low, Close):
    """CDLHIGHWAVE(Open, High, Low, Close) -> (BegIdx, Integer)

    TA_CDLHIGHWAVE - High-Wave Candle
    Input  = Open, High, Low, Close
    Output = int
    """
    return None, 1

def CDLHIGHWAVE_Lookback():
    """CDLHIGHWAVE_Lookback() -> int"""
    return -1

def CDLHIKKAKE(Open, High, Low, Close):
    """CDLHIKKAKE(Open, High, Low, Close) -> (BegIdx, Integer)

    TA_CDLHIKKAKE - Hikkake Pattern
    Input  = Open, High, Low, Close
    Output = int
    """
    return None, 1

def CDLHIKKAKE_Lookback():
    """CDLHIKKAKE_Lookback() -> int"""
    return -1

def CDLHIKKAKEMOD(Open, High, Low, Close):
    """CDLHIKKAKEMOD(Open, High, Low, Close) -> (BegIdx, Integer)

    TA_CDLHIKKAKEMOD - Modified Hikkake Pattern
    Input  = Open, High, Low, Close
    Output = int
    """
    return None, 1

def CDLHIKKAKEMOD_Lookback():
    """CDLHIKKAKEMOD_Lookback() -> int"""
    return -1

def CDLHOMINGPIGEON(Open, High, Low, Close):
    """CDLHOMINGPIGEON(Open, High, Low, Close) -> (BegIdx, Integer)

    TA_CDLHOMINGPIGEON - Homing Pigeon
    Input  = Open, High, Low, Close
    Output = int
    """
    return None, 1

def CDLHOMINGPIGEON_Lookback():
    """CDLHOMINGPIGEON_Lookback() -> int"""
    return -1

def CDLIDENTICAL3CROWS(Open, High, Low, Close):
    """CDLIDENTICAL3CROWS(Open, High, Low, Close) -> (BegIdx, Integer)

    TA_CDLIDENTICAL3CROWS - Identical Three Crows
    Input  = Open, High, Low, Close
    Output = int
    """
    return None, 1

def CDLIDENTICAL3CROWS_Lookback():
    """CDLIDENTICAL3CROWS_Lookback() -> int"""
    return -1

def CDLINNECK(Open, High, Low, Close):
    """CDLINNECK(Open, High, Low, Close) -> (BegIdx, Integer)

    TA_CDLINNECK - In-Neck Pattern
    Input  = Open, High, Low, Close
    Output = int
    """
    return None, 1

def CDLINNECK_Lookback():
    """CDLINNECK_Lookback() -> int"""
    return -1

def CDLINVERTEDHAMMER(Open, High, Low, Close):
    """CDLINVERTEDHAMMER(Open, High, Low, Close) -> (BegIdx, Integer)

    TA_CDLINVERTEDHAMMER - Inverted Hammer
    Input  = Open, High, Low, Close
    Output = int
    """
    return None, 1

def CDLINVERTEDHAMMER_Lookback():
    """CDLINVERTEDHAMMER_Lookback() -> int"""
    return -1

def CDLKICKING(Open, High, Low, Close):
    """CDLKICKING(Open, High, Low, Close) -> (BegIdx, Integer)

    TA_CDLKICKING - Kicking
    Input  = Open, High, Low, Close
    Output = int
    """
    return None, 1

def CDLKICKING_Lookback():
    """CDLKICKING_Lookback() -> int"""
    return -1

def CDLKICKINGBYLENGTH(Open, High, Low, Close):
    """CDLKICKINGBYLENGTH(Open, High, Low, Close) -> (BegIdx, Integer)

    TA_CDLKICKINGBYLENGTH - Kicking - bull/bear determined by the longer marubozu
    Input  = Open, High, Low, Close
    Output = int
    """
    return None, 1

def CDLKICKINGBYLENGTH_Lookback():
    """CDLKICKINGBYLENGTH_Lookback() -> int"""
    return -1

def CDLLADDERBOTTOM(Open, High, Low, Close):
    """CDLLADDERBOTTOM(Open, High, Low, Close) -> (BegIdx, Integer)

    TA_CDLLADDERBOTTOM - Ladder Bottom
    Input  = Open, High, Low, Close
    Output = int
    """
    return None, 1

def CDLLADDERBOTTOM_Lookback():
    """CDLLADDERBOTTOM_Lookback() -> int"""
    return -1

def CDLLONGLEGGEDDOJI(Open, High, Low, Close):
    """CDLLONGLEGGEDDOJI(Open, High, Low, Close) -> (BegIdx, Integer)

    TA_CDLLONGLEGGEDDOJI - Long Legged Doji
    Input  = Open, High, Low, Close
    Output = int
    """
    return None, 1

def CDLLONGLEGGEDDOJI_Lookback():
    """CDLLONGLEGGEDDOJI_Lookback() -> int"""
    return -1

def CDLLONGLINE(Open, High, Low, Close):
    """CDLLONGLINE(Open, High, Low, Close) -> (BegIdx, Integer)

    TA_CDLLONGLINE - Long Line Candle
    Input  = Open, High, Low, Close
    Output = int
    """
    return None, 1

def CDLLONGLINE_Lookback():
    """CDLLONGLINE_Lookback() -> int"""
    return -1

def CDLMARUBOZU(Open, High, Low, Close):
    """CDLMARUBOZU(Open, High, Low, Close) -> (BegIdx, Integer)

    TA_CDLMARUBOZU - Marubozu
    Input  = Open, High, Low, Close
    Output = int
    """
    return None, 1

def CDLMARUBOZU_Lookback():
    """CDLMARUBOZU_Lookback() -> int"""
    return -1

def CDLMATCHINGLOW(Open, High, Low, Close):
    """CDLMATCHINGLOW(Open, High, Low, Close) -> (BegIdx, Integer)

    TA_CDLMATCHINGLOW - Matching Low
    Input  = Open, High, Low, Close
    Output = int
    """
    return None, 1

def CDLMATCHINGLOW_Lookback():
    """CDLMATCHINGLOW_Lookback() -> int"""
    return -1

def CDLMATHOLD(Open, High, Low, Close, Penetration):
    """CDLMATHOLD(Open, High, Low, Close[, Penetration]) -> (BegIdx, Integer)

    TA_CDLMATHOLD - Mat Hold
    Input  = Open, High, Low, Close
    Output = int
    Optional Parameters
    -------------------
    optInPenetration:(From 0 to TA_REAL_MAX)
       Percentage of penetration of a candle within another candle
    """
    return None, 1

def CDLMATHOLD_Lookback(Penetration):
    """CDLMATHOLD_Lookback([Penetration]) -> int"""
    return -1

def CDLMORNINGDOJISTAR(Open, High, Low, Close, Penetration):
    """CDLMORNINGDOJISTAR(Open, High, Low, Close[, Penetration]) -> (BegIdx, Integer)

    TA_CDLMORNINGDOJISTAR - Morning Doji Star
    Input  = Open, High, Low, Close
    Output = int
    Optional Parameters
    -------------------
    optInPenetration:(From 0 to TA_REAL_MAX)
       Percentage of penetration of a candle within another candle
    """
    return None, 1

def CDLMORNINGDOJISTAR_Lookback(Penetration):
    """CDLMORNINGDOJISTAR_Lookback([Penetration]) -> int"""
    return -1

def CDLMORNINGSTAR(Open, High, Low, Close, Penetration):
    """CDLMORNINGSTAR(Open, High, Low, Close[, Penetration]) -> (BegIdx, Integer)

    TA_CDLMORNINGSTAR - Morning Star
    Input  = Open, High, Low, Close
    Output = int
    Optional Parameters
    -------------------
    optInPenetration:(From 0 to TA_REAL_MAX)
       Percentage of penetration of a candle within another candle
    """
    return None, 1

def CDLMORNINGSTAR_Lookback(Penetration):
    """CDLMORNINGSTAR_Lookback([Penetration]) -> int"""
    return -1

def CDLONNECK(Open, High, Low, Close):
    """CDLONNECK(Open, High, Low, Close) -> (BegIdx, Integer)

    TA_CDLONNECK - On-Neck Pattern
    Input  = Open, High, Low, Close
    Output = int
    """
    return None, 1

def CDLONNECK_Lookback():
    """CDLONNECK_Lookback() -> int"""
    return -1

def CDLPIERCING(Open, High, Low, Close):
    """CDLPIERCING(Open, High, Low, Close) -> (BegIdx, Integer)

    TA_CDLPIERCING - Piercing Pattern
    Input  = Open, High, Low, Close
    Output = int
    """
    return None, 1

def CDLPIERCING_Lookback():
    """CDLPIERCING_Lookback() -> int"""
    return -1

def CDLRICKSHAWMAN(Open, High, Low, Close):
    """CDLRICKSHAWMAN(Open, High, Low, Close) -> (BegIdx, Integer)

    TA_CDLRICKSHAWMAN - Rickshaw Man
    Input  = Open, High, Low, Close
    Output = int
    """
    return None, 1

def CDLRICKSHAWMAN_Lookback():
    """CDLRICKSHAWMAN_Lookback() -> int"""
    return -1

def CDLRISEFALL3METHODS(Open, High, Low, Close):
    """CDLRISEFALL3METHODS(Open, High, Low, Close) -> (BegIdx, Integer)

    TA_CDLRISEFALL3METHODS - Rising/Falling Three Methods
    Input  = Open, High, Low, Close
    Output = int
    """
    return None, 1

def CDLRISEFALL3METHODS_Lookback():
    """CDLRISEFALL3METHODS_Lookback() -> int"""
    return -1

def CDLSEPARATINGLINES(Open, High, Low, Close):
    """CDLSEPARATINGLINES(Open, High, Low, Close) -> (BegIdx, Integer)

    TA_CDLSEPARATINGLINES - Separating Lines
    Input  = Open, High, Low, Close
    Output = int
    """
    return None, 1

def CDLSEPARATINGLINES_Lookback():
    """CDLSEPARATINGLINES_Lookback() -> int"""
    return -1

def CDLSHOOTINGSTAR(Open, High, Low, Close):
    """CDLSHOOTINGSTAR(Open, High, Low, Close) -> (BegIdx, Integer)

    TA_CDLSHOOTINGSTAR - Shooting Star
    Input  = Open, High, Low, Close
    Output = int
    """
    return None, 1

def CDLSHOOTINGSTAR_Lookback():
    """CDLSHOOTINGSTAR_Lookback() -> int"""
    return -1

def CDLSHORTLINE(Open, High, Low, Close):
    """CDLSHORTLINE(Open, High, Low, Close) -> (BegIdx, Integer)

    TA_CDLSHORTLINE - Short Line Candle
    Input  = Open, High, Low, Close
    Output = int
    """
    return None, 1

def CDLSHORTLINE_Lookback():
    """CDLSHORTLINE_Lookback() -> int"""
    return -1

def CDLSPINNINGTOP(Open, High, Low, Close):
    """CDLSPINNINGTOP(Open, High, Low, Close) -> (BegIdx, Integer)

    TA_CDLSPINNINGTOP - Spinning Top
    Input  = Open, High, Low, Close
    Output = int
    """
    return None, 1

def CDLSPINNINGTOP_Lookback():
    """CDLSPINNINGTOP_Lookback() -> int"""
    return -1

def CDLSTALLEDPATTERN(Open, High, Low, Close):
    """CDLSTALLEDPATTERN(Open, High, Low, Close) -> (BegIdx, Integer)

    TA_CDLSTALLEDPATTERN - Stalled Pattern
    Input  = Open, High, Low, Close
    Output = int
    """
    return None, 1

def CDLSTALLEDPATTERN_Lookback():
    """CDLSTALLEDPATTERN_Lookback() -> int"""
    return -1

def CDLSTICKSANDWICH(Open, High, Low, Close):
    """CDLSTICKSANDWICH(Open, High, Low, Close) -> (BegIdx, Integer)

    TA_CDLSTICKSANDWICH - Stick Sandwich
    Input  = Open, High, Low, Close
    Output = int
    """
    return None, 1

def CDLSTICKSANDWICH_Lookback():
    """CDLSTICKSANDWICH_Lookback() -> int"""
    return -1

def CDLTAKURI(Open, High, Low, Close):
    """CDLTAKURI(Open, High, Low, Close) -> (BegIdx, Integer)

    TA_CDLTAKURI - Takuri (Dragonfly Doji with very long lower shadow)
    Input  = Open, High, Low, Close
    Output = int
    """
    return None, 1

def CDLTAKURI_Lookback():
    """CDLTAKURI_Lookback() -> int"""
    return -1

def CDLTASUKIGAP(Open, High, Low, Close):
    """CDLTASUKIGAP(Open, High, Low, Close) -> (BegIdx, Integer)

    TA_CDLTASUKIGAP - Tasuki Gap
    Input  = Open, High, Low, Close
    Output = int
    """
    return None, 1

def CDLTASUKIGAP_Lookback():
    """CDLTASUKIGAP_Lookback() -> int"""
    return -1

def CDLTHRUSTING(Open, High, Low, Close):
    """CDLTHRUSTING(Open, High, Low, Close) -> (BegIdx, Integer)

    TA_CDLTHRUSTING - Thrusting Pattern
    Input  = Open, High, Low, Close
    Output = int
    """
    return None, 1

def CDLTHRUSTING_Lookback():
    """CDLTHRUSTING_Lookback() -> int"""
    return -1

def CDLTRISTAR(Open, High, Low, Close):
    """CDLTRISTAR(Open, High, Low, Close) -> (BegIdx, Integer)

    TA_CDLTRISTAR - Tristar Pattern
    Input  = Open, High, Low, Close
    Output = int
    """
    return None, 1

def CDLTRISTAR_Lookback():
    """CDLTRISTAR_Lookback() -> int"""
    return -1

def CDLUNIQUE3RIVER(Open, High, Low, Close):
    """CDLUNIQUE3RIVER(Open, High, Low, Close) -> (BegIdx, Integer)

    TA_CDLUNIQUE3RIVER - Unique 3 River
    Input  = Open, High, Low, Close
    Output = int
    """
    return None, 1

def CDLUNIQUE3RIVER_Lookback():
    """CDLUNIQUE3RIVER_Lookback() -> int"""
    return -1

def CDLUPSIDEGAP2CROWS(Open, High, Low, Close):
    """CDLUPSIDEGAP2CROWS(Open, High, Low, Close) -> (BegIdx, Integer)

    TA_CDLUPSIDEGAP2CROWS - Upside Gap Two Crows
    Input  = Open, High, Low, Close
    Output = int
    """
    return None, 1

def CDLUPSIDEGAP2CROWS_Lookback():
    """CDLUPSIDEGAP2CROWS_Lookback() -> int"""
    return -1

def CDLXSIDEGAP3METHODS(Open, High, Low, Close):
    """CDLXSIDEGAP3METHODS(Open, High, Low, Close) -> (BegIdx, Integer)

    TA_CDLXSIDEGAP3METHODS - Upside/Downside Gap Three Methods
    Input  = Open, High, Low, Close
    Output = int
    """
    return None, 1

def CDLXSIDEGAP3METHODS_Lookback():
    """CDLXSIDEGAP3METHODS_Lookback() -> int"""
    return -1

def CEIL(Real):
    """CEIL(Real) -> (BegIdx, Real)

    TA_CEIL - Vector Ceil
    Input  = double
    Output = double
    """
    return None, 1

def CEIL_Lookback():
    """CEIL_Lookback() -> int"""
    return -1

def CMO(Real, TimePeriod):
    """CMO(Real[, TimePeriod]) -> (BegIdx, Real)

    TA_CMO - Chande Momentum Oscillator
    Input  = double
    Output = double
    Optional Parameters
    -------------------
    optInTimePeriod:(From 2 to 100000)
       Number of period
    """
    return None, 1

def CMO_Lookback(TimePeriod):
    """CMO_Lookback([TimePeriod]) -> int"""
    return -1

def CORREL(Real0, Real1, TimePeriod):
    """CORREL(Real0, Real1[, TimePeriod]) -> (BegIdx, Real)

    TA_CORREL - Pearson's Correlation Coefficient (r)
    Input  = double, double
    Output = double
    Optional Parameters
    -------------------
    optInTimePeriod:(From 1 to 100000)
       Number of period
    """
    return None, 1

def CORREL_Lookback(TimePeriod):
    """CORREL_Lookback([TimePeriod]) -> int"""
    return -1

def COS(Real):
    """COS(Real) -> (BegIdx, Real)

    TA_COS - Vector Trigonometric Cos
    Input  = double
    Output = double
    """
    return None, 1

def COS_Lookback():
    """COS_Lookback() -> int"""
    return -1

def COSH(Real):
    """COSH(Real) -> (BegIdx, Real)

    TA_COSH - Vector Trigonometric Cosh
    Input  = double
    Output = double
    """
    return None, 1

def COSH_Lookback():
    """COSH_Lookback() -> int"""
    return -1

def DEMA(Real, TimePeriod):
    """DEMA(Real[, TimePeriod]) -> (BegIdx, Real)

    TA_DEMA - Double Exponential Moving Average
    Input  = double
    Output = double
    Optional Parameters
    -------------------
    optInTimePeriod:(From 2 to 100000)
       Number of period
    """
    return None, 1

def DEMA_Lookback(TimePeriod):
    """DEMA_Lookback([TimePeriod]) -> int"""
    return -1

def DIV(Real0, Real1):
    """DIV(Real0, Real1) -> (BegIdx, Real)

    TA_DIV - Vector Arithmetic Div
    Input  = double, double
    Output = double
    """
    return None, 1

def DIV_Lookback():
    """DIV_Lookback() -> int"""
    return -1

def DX(High, Low, Close, TimePeriod):
    """DX(High, Low, Close[, TimePeriod]) -> (BegIdx, Real)

    TA_DX - Directional Movement Index
    Input  = High, Low, Close
    Output = double
    Optional Parameters
    -------------------
    optInTimePeriod:(From 2 to 100000)
       Number of period
    """
    return None, 1

def DX_Lookback(TimePeriod):
    """DX_Lookback([TimePeriod]) -> int"""
    return -1

def EMA(Real, TimePeriod):
    """EMA(Real[, TimePeriod]) -> (BegIdx, Real)

    TA_EMA - Exponential Moving Average
    Input  = double
    Output = double
    Optional Parameters
    -------------------
    optInTimePeriod:(From 2 to 100000)
       Number of period
    """
    return None, 1

def EMA_Lookback(TimePeriod):
    """EMA_Lookback([TimePeriod]) -> int"""
    return -1

def EXP(Real):
    """EXP(Real) -> (BegIdx, Real)

    TA_EXP - Vector Arithmetic Exp
    Input  = double
    Output = double
    """
    return None, 1

def EXP_Lookback():
    """EXP_Lookback() -> int"""
    return -1

def FLOOR(Real):
    """FLOOR(Real) -> (BegIdx, Real)

    TA_FLOOR - Vector Floor
    Input  = double
    Output = double
    """
    return None, 1

def FLOOR_Lookback():
    """FLOOR_Lookback() -> int"""
    return -1

def HT_DCPERIOD(Real):
    """HT_DCPERIOD(Real) -> (BegIdx, Real)

    TA_HT_DCPERIOD - Hilbert Transform - Dominant Cycle Period
    Input  = double
    Output = double
    """
    return None, 1

def HT_DCPERIOD_Lookback():
    """HT_DCPERIOD_Lookback() -> int"""
    return -1

def HT_DCPHASE(Real):
    """HT_DCPHASE(Real) -> (BegIdx, Real)

    TA_HT_DCPHASE - Hilbert Transform - Dominant Cycle Phase
    Input  = double
    Output = double
    """
    return None, 1

def HT_DCPHASE_Lookback():
    """HT_DCPHASE_Lookback() -> int"""
    return -1

def HT_PHASOR(Real):
    """HT_PHASOR(Real) -> (BegIdx, InPhase, Quadrature)

    TA_HT_PHASOR - Hilbert Transform - Phasor Components
    Input  = double
    Output = double, double
    """
    return None, 1, None

def HT_PHASOR_Lookback():
    """HT_PHASOR_Lookback() -> int"""
    return -1

def HT_SINE(Real):
    """HT_SINE(Real) -> (BegIdx, Sine, LeadSine)

    TA_HT_SINE - Hilbert Transform - SineWave
    Input  = double
    Output = double, double
    """
    return None, 1, None

def HT_SINE_Lookback():
    """HT_SINE_Lookback() -> int"""
    return -1

def HT_TRENDLINE(Real):
    """HT_TRENDLINE(Real) -> (BegIdx, Real)

    TA_HT_TRENDLINE - Hilbert Transform - Instantaneous Trendline
    Input  = double
    Output = double
    """
    return None, 1

def HT_TRENDLINE_Lookback():
    """HT_TRENDLINE_Lookback() -> int"""
    return -1

def HT_TRENDMODE(Real):
    """HT_TRENDMODE(Real) -> (BegIdx, Integer)

    TA_HT_TRENDMODE - Hilbert Transform - Trend vs Cycle Mode
    Input  = double
    Output = int
    """
    return None, 1

def HT_TRENDMODE_Lookback():
    """HT_TRENDMODE_Lookback() -> int"""
    return -1

def KAMA(Real, TimePeriod):
    """KAMA(Real[, TimePeriod]) -> (BegIdx, Real)

    TA_KAMA - Kaufman Adaptive Moving Average
    Input  = double
    Output = double
    Optional Parameters
    -------------------
    optInTimePeriod:(From 2 to 100000)
       Number of period
    """
    return None, 1

def KAMA_Lookback(TimePeriod):
    """KAMA_Lookback([TimePeriod]) -> int"""
    return -1

def LINEARREG(Real, TimePeriod):
    """LINEARREG(Real[, TimePeriod]) -> (BegIdx, Real)

    TA_LINEARREG - Linear Regression
    Input  = double
    Output = double
    Optional Parameters
    -------------------
    optInTimePeriod:(From 2 to 100000)
       Number of period
    """
    return None, 1

def LINEARREG_Lookback(TimePeriod):
    """LINEARREG_Lookback([TimePeriod]) -> int"""
    return -1

def LINEARREG_ANGLE(Real, TimePeriod):
    """LINEARREG_ANGLE(Real[, TimePeriod]) -> (BegIdx, Real)

    TA_LINEARREG_ANGLE - Linear Regression Angle
    Input  = double
    Output = double
    Optional Parameters
    -------------------
    optInTimePeriod:(From 2 to 100000)
       Number of period
    """
    return None, 1

def LINEARREG_ANGLE_Lookback(TimePeriod):
    """LINEARREG_ANGLE_Lookback([TimePeriod]) -> int"""
    return -1

def LINEARREG_INTERCEPT(Real, TimePeriod):
    """LINEARREG_INTERCEPT(Real[, TimePeriod]) -> (BegIdx, Real)

    TA_LINEARREG_INTERCEPT - Linear Regression Intercept
    Input  = double
    Output = double
    Optional Parameters
    -------------------
    optInTimePeriod:(From 2 to 100000)
       Number of period
    """
    return None, 1

def LINEARREG_INTERCEPT_Lookback(TimePeriod):
    """LINEARREG_INTERCEPT_Lookback([TimePeriod]) -> int"""
    return -1

def LINEARREG_SLOPE(Real, TimePeriod):
    """LINEARREG_SLOPE(Real[, TimePeriod]) -> (BegIdx, Real)

    TA_LINEARREG_SLOPE - Linear Regression Slope
    Input  = double
    Output = double
    Optional Parameters
    -------------------
    optInTimePeriod:(From 2 to 100000)
       Number of period
    """
    return None, 1

def LINEARREG_SLOPE_Lookback(TimePeriod):
    """LINEARREG_SLOPE_Lookback([TimePeriod]) -> int"""
    return -1

def LN(Real):
    """LN(Real) -> (BegIdx, Real)

    TA_LN - Vector Log Natural
    Input  = double
    Output = double
    """
    return None, 1

def LN_Lookback():
    """LN_Lookback() -> int"""
    return -1

def LOG10(Real):
    """LOG10(Real) -> (BegIdx, Real)

    TA_LOG10 - Vector Log10
    Input  = double
    Output = double
    """
    return None, 1

def LOG10_Lookback():
    """LOG10_Lookback() -> int"""
    return -1

def MA(Real, TimePeriod, MAType):
    """MA(Real[, TimePeriod, MAType]) -> (BegIdx, Real)

    TA_MA - Moving average
    Input  = double
    Output = double
    Optional Parameters
    -------------------
    optInTimePeriod:(From 1 to 100000)
       Number of period
    optInMAType:
       Type of Moving Average
    """
    return None, 1

def MA_Lookback(TimePeriod, MAType):
    """MA_Lookback([TimePeriod, MAType]) -> int"""
    return -1

def MACD(Real, FastPeriod, SlowPeriod, SignalPeriod):
    """MACD(Real[, FastPeriod, SlowPeriod, SignalPeriod]) -> (BegIdx, MACD, MACDSignal, MACDHist)

    TA_MACD - Moving Average Convergence/Divergence
    Input  = double
    Output = double, double, double
    Optional Parameters
    -------------------
    optInFastPeriod:(From 2 to 100000)
       Number of period for the fast MA
    optInSlowPeriod:(From 2 to 100000)
       Number of period for the slow MA
    optInSignalPeriod:(From 1 to 100000)
       Smoothing for the signal line (nb of period)
    """
    return None, 1, None, None

def MACD_Lookback(FastPeriod, SlowPeriod, SignalPeriod):
    """MACD_Lookback([FastPeriod, SlowPeriod, SignalPeriod]) -> int"""
    return -1

def MACDEXT(Real, FastPeriod, FastMAType, SlowPeriod, SlowMAType, SignalPeriod, SignalMAType):
    """MACDEXT(Real[, FastPeriod, FastMAType, SlowPeriod, SlowMAType, SignalPeriod, SignalMAType]) -> (BegIdx, MACD, MACDSignal, MACDHist)

    TA_MACDEXT - MACD with controllable MA type
    Input  = double
    Output = double, double, double
    Optional Parameters
    -------------------
    optInFastPeriod:(From 2 to 100000)
       Number of period for the fast MA
    optInFastMAType:
       Type of Moving Average for fast MA
    optInSlowPeriod:(From 2 to 100000)
       Number of period for the slow MA
    optInSlowMAType:
       Type of Moving Average for slow MA
    optInSignalPeriod:(From 1 to 100000)
       Smoothing for the signal line (nb of period)
    optInSignalMAType:
       Type of Moving Average for signal line
    """
    return None, 1, None, None

def MACDEXT_Lookback(FastPeriod, FastMAType, SlowPeriod, SlowMAType, SignalPeriod, SignalMAType):
    """MACDEXT_Lookback([FastPeriod, FastMAType, SlowPeriod, SlowMAType, SignalPeriod, SignalMAType]) -> int"""
    return -1

def MACDFIX(Real, SignalPeriod):
    """MACDFIX(Real[, SignalPeriod]) -> (BegIdx, MACD, MACDSignal, MACDHist)

    TA_MACDFIX - Moving Average Convergence/Divergence Fix 12/26
    Input  = double
    Output = double, double, double
    Optional Parameters
    -------------------
    optInSignalPeriod:(From 1 to 100000)
       Smoothing for the signal line (nb of period)
    """
    return None, 1, None, None

def MACDFIX_Lookback(SignalPeriod):
    """MACDFIX_Lookback([SignalPeriod]) -> int"""
    return -1

def MAMA(Real, FastLimit, SlowLimit):
    """MAMA(Real[, FastLimit, SlowLimit]) -> (BegIdx, MAMA, FAMA)

    TA_MAMA - MESA Adaptive Moving Average
    Input  = double
    Output = double, double
    Optional Parameters
    -------------------
    optInFastLimit:(From 0.01 to 0.99)
       Upper limit use in the adaptive algorithm
    optInSlowLimit:(From 0.01 to 0.99)
       Lower limit use in the adaptive algorithm
    """
    return None, 1, None

def MAMA_Lookback(FastLimit, SlowLimit):
    """MAMA_Lookback([FastLimit, SlowLimit]) -> int"""
    return -1

def MAVP(Real, Periods, MinPeriod, MaxPeriod, MAType):
    """MAVP(Real, Periods[, MinPeriod, MaxPeriod, MAType]) -> (BegIdx, Real)

    TA_MAVP - Moving average with variable period
    Input  = double, double
    Output = double
    Optional Parameters
    -------------------
    optInMinPeriod:(From 2 to 100000)
       Value less than minimum will be changed to Minimum period
    optInMaxPeriod:(From 2 to 100000)
       Value higher than maximum will be changed to Maximum period
    optInMAType:
       Type of Moving Average
    """
    return None, 1

def MAVP_Lookback(MinPeriod, MaxPeriod, MAType):
    """MAVP_Lookback([MinPeriod, MaxPeriod, MAType]) -> int"""
    return -1

def MAX(Real, TimePeriod):
    """MAX(Real[, TimePeriod]) -> (BegIdx, Real)

    TA_MAX - Highest value over a specified period
    Input  = double
    Output = double
    Optional Parameters
    -------------------
    optInTimePeriod:(From 2 to 100000)
       Number of period
    """
    return None, 1

def MAX_Lookback(TimePeriod):
    """MAX_Lookback([TimePeriod]) -> int"""
    return -1

def MAXINDEX(Real, TimePeriod):
    """MAXINDEX(Real[, TimePeriod]) -> (BegIdx, Integer)

    TA_MAXINDEX - Index of highest value over a specified period
    Input  = double
    Output = int
    Optional Parameters
    -------------------
    optInTimePeriod:(From 2 to 100000)
       Number of period
    """
    return None, 1

def MAXINDEX_Lookback(TimePeriod):
    """MAXINDEX_Lookback([TimePeriod]) -> int"""
    return -1

def MEDPRICE(High, Low):
    """MEDPRICE(High, Low) -> (BegIdx, Real)

    TA_MEDPRICE - Median Price
    Input  = High, Low
    Output = double
    """
    return None, 1

def MEDPRICE_Lookback():
    """MEDPRICE_Lookback() -> int"""
    return -1

def MFI(High, Low, Close, Volume, TimePeriod):
    """MFI(High, Low, Close, Volume[, TimePeriod]) -> (BegIdx, Real)

    TA_MFI - Money Flow Index
    Input  = High, Low, Close, Volume
    Output = double
    Optional Parameters
    -------------------
    optInTimePeriod:(From 2 to 100000)
       Number of period
    """
    return None, 1

def MFI_Lookback(TimePeriod):
    """MFI_Lookback([TimePeriod]) -> int"""
    return -1

def MIDPOINT(Real, TimePeriod):
    """MIDPOINT(Real[, TimePeriod]) -> (BegIdx, Real)

    TA_MIDPOINT - MidPoint over period
    Input  = double
    Output = double
    Optional Parameters
    -------------------
    optInTimePeriod:(From 2 to 100000)
       Number of period
    """
    return None, 1

def MIDPOINT_Lookback(TimePeriod):
    """MIDPOINT_Lookback([TimePeriod]) -> int"""
    return -1

def MIDPRICE(High, Low, TimePeriod):
    """MIDPRICE(High, Low[, TimePeriod]) -> (BegIdx, Real)

    TA_MIDPRICE - Midpoint Price over period
    Input  = High, Low
    Output = double
    Optional Parameters
    -------------------
    optInTimePeriod:(From 2 to 100000)
       Number of period
    """
    return None, 1

def MIDPRICE_Lookback(TimePeriod):
    """MIDPRICE_Lookback([TimePeriod]) -> int"""
    return -1

def MIN(Real, TimePeriod):
    """MIN(Real[, TimePeriod]) -> (BegIdx, Real)

    TA_MIN - Lowest value over a specified period
    Input  = double
    Output = double
    Optional Parameters
    -------------------
    optInTimePeriod:(From 2 to 100000)
       Number of period
    """
    return None, 1

def MIN_Lookback(TimePeriod):
    """MIN_Lookback([TimePeriod]) -> int"""
    return -1

def MININDEX(Real, TimePeriod):
    """MININDEX(Real[, TimePeriod]) -> (BegIdx, Integer)

    TA_MININDEX - Index of lowest value over a specified period
    Input  = double
    Output = int
    Optional Parameters
    -------------------
    optInTimePeriod:(From 2 to 100000)
       Number of period
    """
    return None, 1

def MININDEX_Lookback(TimePeriod):
    """MININDEX_Lookback([TimePeriod]) -> int"""
    return -1

def MINMAX(Real, TimePeriod):
    """MINMAX(Real[, TimePeriod]) -> (BegIdx, Min, Max)

    TA_MINMAX - Lowest and highest values over a specified period
    Input  = double
    Output = double, double
    Optional Parameters
    -------------------
    optInTimePeriod:(From 2 to 100000)
       Number of period
    """
    return None, 1, None

def MINMAX_Lookback(TimePeriod):
    """MINMAX_Lookback([TimePeriod]) -> int"""
    return -1

def MINMAXINDEX(Real, TimePeriod):
    """MINMAXINDEX(Real[, TimePeriod]) -> (BegIdx, MinIdx, MaxIdx)

    TA_MINMAXINDEX - Indexes of lowest and highest values over a specified period
    Input  = double
    Output = int, int
    Optional Parameters
    -------------------
    optInTimePeriod:(From 2 to 100000)
       Number of period
    """
    return None, 1, None

def MINMAXINDEX_Lookback(TimePeriod):
    """MINMAXINDEX_Lookback([TimePeriod]) -> int"""
    return -1

def MINUS_DI(High, Low, Close, TimePeriod):
    """MINUS_DI(High, Low, Close[, TimePeriod]) -> (BegIdx, Real)

    TA_MINUS_DI - Minus Directional Indicator
    Input  = High, Low, Close
    Output = double
    Optional Parameters
    -------------------
    optInTimePeriod:(From 1 to 100000)
       Number of period
    """
    return None, 1

def MINUS_DI_Lookback(TimePeriod):
    """MINUS_DI_Lookback([TimePeriod]) -> int"""
    return -1

def MINUS_DM(High, Low, TimePeriod):
    """MINUS_DM(High, Low[, TimePeriod]) -> (BegIdx, Real)

    TA_MINUS_DM - Minus Directional Movement
    Input  = High, Low
    Output = double
    Optional Parameters
    -------------------
    optInTimePeriod:(From 1 to 100000)
       Number of period
    """
    return None, 1

def MINUS_DM_Lookback(TimePeriod):
    """MINUS_DM_Lookback([TimePeriod]) -> int"""
    return -1

def MOM(Real, TimePeriod):
    """MOM(Real[, TimePeriod]) -> (BegIdx, Real)

    TA_MOM - Momentum
    Input  = double
    Output = double
    Optional Parameters
    -------------------
    optInTimePeriod:(From 1 to 100000)
       Number of period
    """
    return None, 1

def MOM_Lookback(TimePeriod):
    """MOM_Lookback([TimePeriod]) -> int"""
    return -1

def MULT(Real0, Real1):
    """MULT(Real0, Real1) -> (BegIdx, Real)

    TA_MULT - Vector Arithmetic Mult
    Input  = double, double
    Output = double
    """
    return None, 1

def MULT_Lookback():
    """MULT_Lookback() -> int"""
    return -1

def NATR(High, Low, Close, TimePeriod):
    """NATR(High, Low, Close[, TimePeriod]) -> (BegIdx, Real)

    TA_NATR - Normalized Average True Range
    Input  = High, Low, Close
    Output = double
    Optional Parameters
    -------------------
    optInTimePeriod:(From 1 to 100000)
       Number of period
    """
    return None, 1

def NATR_Lookback(TimePeriod):
    """NATR_Lookback([TimePeriod]) -> int"""
    return -1

def OBV(Real, Volume):
    """OBV(Real, Volume) -> (BegIdx, Real)

    TA_OBV - On Balance Volume
    Input  = double, Volume
    Output = double
    """
    return None, 1

def OBV_Lookback():
    """OBV_Lookback() -> int"""
    return -1

def PLUS_DI(High, Low, Close, TimePeriod):
    """PLUS_DI(High, Low, Close[, TimePeriod]) -> (BegIdx, Real)

    TA_PLUS_DI - Plus Directional Indicator
    Input  = High, Low, Close
    Output = double
    Optional Parameters
    -------------------
    optInTimePeriod:(From 1 to 100000)
       Number of period
    """
    return None, 1

def PLUS_DI_Lookback(TimePeriod):
    """PLUS_DI_Lookback([TimePeriod]) -> int"""
    return -1

def PLUS_DM(High, Low, TimePeriod):
    """PLUS_DM(High, Low[, TimePeriod]) -> (BegIdx, Real)

    TA_PLUS_DM - Plus Directional Movement
    Input  = High, Low
    Output = double
    Optional Parameters
    -------------------
    optInTimePeriod:(From 1 to 100000)
       Number of period
    """
    return None, 1

def PLUS_DM_Lookback(TimePeriod):
    """PLUS_DM_Lookback([TimePeriod]) -> int"""
    return -1

def PPO(Real, FastPeriod, SlowPeriod, MAType):
    """PPO(Real[, FastPeriod, SlowPeriod, MAType]) -> (BegIdx, Real)

    TA_PPO - Percentage Price Oscillator
    Input  = double
    Output = double
    Optional Parameters
    -------------------
    optInFastPeriod:(From 2 to 100000)
       Number of period for the fast MA
    optInSlowPeriod:(From 2 to 100000)
       Number of period for the slow MA
    optInMAType:
       Type of Moving Average
    """
    return None, 1

def PPO_Lookback(FastPeriod, SlowPeriod, MAType):
    """PPO_Lookback([FastPeriod, SlowPeriod, MAType]) -> int"""
    return -1

def ROC(Real, TimePeriod):
    """ROC(Real[, TimePeriod]) -> (BegIdx, Real)

    TA_ROC - Rate of change : ((price/prevPrice)-1)*100
    Input  = double
    Output = double
    Optional Parameters
    -------------------
    optInTimePeriod:(From 1 to 100000)
       Number of period
    """
    return None, 1

def ROC_Lookback(TimePeriod):
    """ROC_Lookback([TimePeriod]) -> int"""
    return -1

def ROCP(Real, TimePeriod):
    """ROCP(Real[, TimePeriod]) -> (BegIdx, Real)

    TA_ROCP - Rate of change Percentage: (price-prevPrice)/prevPrice
    Input  = double
    Output = double
    Optional Parameters
    -------------------
    optInTimePeriod:(From 1 to 100000)
       Number of period
    """
    return None, 1

def ROCP_Lookback(TimePeriod):
    """ROCP_Lookback([TimePeriod]) -> int"""
    return -1

def ROCR(Real, TimePeriod):
    """ROCR(Real[, TimePeriod]) -> (BegIdx, Real)

    TA_ROCR - Rate of change ratio: (price/prevPrice)
    Input  = double
    Output = double
    Optional Parameters
    -------------------
    optInTimePeriod:(From 1 to 100000)
       Number of period
    """
    return None, 1

def ROCR_Lookback(TimePeriod):
    """ROCR_Lookback([TimePeriod]) -> int"""
    return -1

def ROCR100(Real, TimePeriod):
    """ROCR100(Real[, TimePeriod]) -> (BegIdx, Real)

    TA_ROCR100 - Rate of change ratio 100 scale: (price/prevPrice)*100
    Input  = double
    Output = double
    Optional Parameters
    -------------------
    optInTimePeriod:(From 1 to 100000)
       Number of period
    """
    return None, 1

def ROCR100_Lookback(TimePeriod):
    """ROCR100_Lookback([TimePeriod]) -> int"""
    return -1

def RSI(Real, TimePeriod):
    """RSI(Real[, TimePeriod]) -> (BegIdx, Real)

    TA_RSI - Relative Strength Index
    Input  = double
    Output = double
    Optional Parameters
    -------------------
    optInTimePeriod:(From 2 to 100000)
       Number of period
    """
    return None, 1

def RSI_Lookback(TimePeriod):
    """RSI_Lookback([TimePeriod]) -> int"""
    return -1

def SAR(High, Low, Acceleration, Maximum):
    """SAR(High, Low[, Acceleration, Maximum]) -> (BegIdx, Real)

    TA_SAR - Parabolic SAR
    Input  = High, Low
    Output = double
    Optional Parameters
    -------------------
    optInAcceleration:(From 0 to TA_REAL_MAX)
       Acceleration Factor used up to the Maximum value
    optInMaximum:(From 0 to TA_REAL_MAX)
       Acceleration Factor Maximum value
    """
    return None, 1

def SAR_Lookback(Acceleration, Maximum):
    """SAR_Lookback([Acceleration, Maximum]) -> int"""
    return -1

def SAREXT(High, Low, StartValue, OffsetOnReverse, AccelerationInitLong, AccelerationLong, AccelerationMaxLong, AccelerationInitShort, AccelerationShort, AccelerationMaxShort):
    """SAREXT(High, Low[, StartValue, OffsetOnReverse, AccelerationInitLong, AccelerationLong, AccelerationMaxLong, AccelerationInitShort, AccelerationShort, AccelerationMaxShort]) -> (BegIdx, Real)

    TA_SAREXT - Parabolic SAR - Extended
    Input  = High, Low
    Output = double
    Optional Parameters
    -------------------
    optInStartValue:(From TA_REAL_MIN to TA_REAL_MAX)
       Start value and direction. 0 for Auto, >0 for Long, <0 for Short
    optInOffsetOnReverse:(From 0 to TA_REAL_MAX)
       Percent offset added/removed to initial stop on short/long reversal
    optInAccelerationInitLong:(From 0 to TA_REAL_MAX)
       Acceleration Factor initial value for the Long direction
    optInAccelerationLong:(From 0 to TA_REAL_MAX)
       Acceleration Factor for the Long direction
    optInAccelerationMaxLong:(From 0 to TA_REAL_MAX)
       Acceleration Factor maximum value for the Long direction
    optInAccelerationInitShort:(From 0 to TA_REAL_MAX)
       Acceleration Factor initial value for the Short direction
    optInAccelerationShort:(From 0 to TA_REAL_MAX)
       Acceleration Factor for the Short direction
    optInAccelerationMaxShort:(From 0 to TA_REAL_MAX)
       Acceleration Factor maximum value for the Short direction
    """
    return None, 1

def SAREXT_Lookback(StartValue, OffsetOnReverse, AccelerationInitLong, AccelerationLong, AccelerationMaxLong, AccelerationInitShort, AccelerationShort, AccelerationMaxShort):
    """SAREXT_Lookback([StartValue, OffsetOnReverse, AccelerationInitLong, AccelerationLong, AccelerationMaxLong, AccelerationInitShort, AccelerationShort, AccelerationMaxShort]) -> int"""
    return -1

def SIN(Real):
    """SIN(Real) -> (BegIdx, Real)

    TA_SIN - Vector Trigonometric Sin
    Input  = double
    Output = double
    """
    return None, 1

def SIN_Lookback():
    """SIN_Lookback() -> int"""
    return -1

def SINH(Real):
    """SINH(Real) -> (BegIdx, Real)

    TA_SINH - Vector Trigonometric Sinh
    Input  = double
    Output = double
    """
    return None, 1

def SINH_Lookback():
    """SINH_Lookback() -> int"""
    return -1

def SMA(Real, TimePeriod):
    """SMA(Real[, TimePeriod]) -> (BegIdx, Real)

    TA_SMA - Simple Moving Average
    Input  = double
    Output = double
    Optional Parameters
    -------------------
    optInTimePeriod:(From 2 to 100000)
       Number of period
    """
    return None, 1

def SMA_Lookback(TimePeriod):
    """SMA_Lookback([TimePeriod]) -> int"""
    return -1

def SQRT(Real):
    """SQRT(Real) -> (BegIdx, Real)

    TA_SQRT - Vector Square Root
    Input  = double
    Output = double
    """
    return None, 1

def SQRT_Lookback():
    """SQRT_Lookback() -> int"""
    return -1

def STDDEV(Real, TimePeriod, NbDev):
    """STDDEV(Real[, TimePeriod, NbDev]) -> (BegIdx, Real)

    TA_STDDEV - Standard Deviation
    Input  = double
    Output = double
    Optional Parameters
    -------------------
    optInTimePeriod:(From 2 to 100000)
       Number of period
    optInNbDev:(From TA_REAL_MIN to TA_REAL_MAX)
       Nb of deviations
    """
    return None, 1

def STDDEV_Lookback(TimePeriod, NbDev):
    """STDDEV_Lookback([TimePeriod, NbDev]) -> int"""
    return -1

def STOCH(High, Low, Close, FastK_Period, SlowK_Period, SlowK_MAType, SlowD_Period, SlowD_MAType):
    """STOCH(High, Low, Close[, FastK_Period, SlowK_Period, SlowK_MAType, SlowD_Period, SlowD_MAType]) -> (BegIdx, SlowK, SlowD)

    TA_STOCH - Stochastic
    Input  = High, Low, Close
    Output = double, double
    Optional Parameters
    -------------------
    optInFastK_Period:(From 1 to 100000)
       Time period for building the Fast-K line
    optInSlowK_Period:(From 1 to 100000)
       Smoothing for making the Slow-K line. Usually set to 3
    optInSlowK_MAType:
       Type of Moving Average for Slow-K
    optInSlowD_Period:(From 1 to 100000)
       Smoothing for making the Slow-D line
    optInSlowD_MAType:
       Type of Moving Average for Slow-D
    """
    return None, 1, None

def STOCH_Lookback(FastK_Period, SlowK_Period, SlowK_MAType, SlowD_Period, SlowD_MAType):
    """STOCH_Lookback([FastK_Period, SlowK_Period, SlowK_MAType, SlowD_Period, SlowD_MAType]) -> int"""
    return -1

def STOCHF(High, Low, Close, FastK_Period, FastD_Period, FastD_MAType):
    """STOCHF(High, Low, Close[, FastK_Period, FastD_Period, FastD_MAType]) -> (BegIdx, FastK, FastD)

    TA_STOCHF - Stochastic Fast
    Input  = High, Low, Close
    Output = double, double
    Optional Parameters
    -------------------
    optInFastK_Period:(From 1 to 100000)
       Time period for building the Fast-K line
    optInFastD_Period:(From 1 to 100000)
       Smoothing for making the Fast-D line. Usually set to 3
    optInFastD_MAType:
       Type of Moving Average for Fast-D
    """
    return None, 1, None

def STOCHF_Lookback(FastK_Period, FastD_Period, FastD_MAType):
    """STOCHF_Lookback([FastK_Period, FastD_Period, FastD_MAType]) -> int"""
    return -1

def STOCHRSI(Real, TimePeriod, FastK_Period, FastD_Period, FastD_MAType):
    """STOCHRSI(Real[, TimePeriod, FastK_Period, FastD_Period, FastD_MAType]) -> (BegIdx, FastK, FastD)

    TA_STOCHRSI - Stochastic Relative Strength Index
    Input  = double
    Output = double, double
    Optional Parameters
    -------------------
    optInTimePeriod:(From 2 to 100000)
       Number of period
    optInFastK_Period:(From 1 to 100000)
       Time period for building the Fast-K line
    optInFastD_Period:(From 1 to 100000)
       Smoothing for making the Fast-D line. Usually set to 3
    optInFastD_MAType:
       Type of Moving Average for Fast-D
    """
    return None, 1, None

def STOCHRSI_Lookback(TimePeriod, FastK_Period, FastD_Period, FastD_MAType):
    """STOCHRSI_Lookback([TimePeriod, FastK_Period, FastD_Period, FastD_MAType]) -> int"""
    return -1

def SUB(Real0, Real1):
    """SUB(Real0, Real1) -> (BegIdx, Real)

    TA_SUB - Vector Arithmetic Substraction
    Input  = double, double
    Output = double
    """
    return None, 1

def SUB_Lookback():
    """SUB_Lookback() -> int"""
    return -1

def SUM(Real, TimePeriod):
    """SUM(Real[, TimePeriod]) -> (BegIdx, Real)

    TA_SUM - Summation
    Input  = double
    Output = double
    Optional Parameters
    -------------------
    optInTimePeriod:(From 2 to 100000)
       Number of period
    """
    return None, 1

def SUM_Lookback(TimePeriod):
    """SUM_Lookback([TimePeriod]) -> int"""
    return -1

def T3(Real, TimePeriod, VFactor):
    """T3(Real[, TimePeriod, VFactor]) -> (BegIdx, Real)

    TA_T3 - Triple Exponential Moving Average (T3)
    Input  = double
    Output = double
    Optional Parameters
    -------------------
    optInTimePeriod:(From 2 to 100000)
       Number of period
    optInVFactor:(From 0 to 1)
       Volume Factor
    """
    return None, 1

def T3_Lookback(TimePeriod, VFactor):
    """T3_Lookback([TimePeriod, VFactor]) -> int"""
    return -1

def TAN(Real):
    """TAN(Real) -> (BegIdx, Real)

    TA_TAN - Vector Trigonometric Tan
    Input  = double
    Output = double
    """
    return None, 1

def TAN_Lookback():
    """TAN_Lookback() -> int"""
    return -1

def TANH(Real):
    """TANH(Real) -> (BegIdx, Real)

    TA_TANH - Vector Trigonometric Tanh
    Input  = double
    Output = double
    """
    return None, 1

def TANH_Lookback():
    """TANH_Lookback() -> int"""
    return -1

def TEMA(Real, TimePeriod):
    """TEMA(Real[, TimePeriod]) -> (BegIdx, Real)

    TA_TEMA - Triple Exponential Moving Average
    Input  = double
    Output = double
    Optional Parameters
    -------------------
    optInTimePeriod:(From 2 to 100000)
       Number of period
    """
    return None, 1

def TEMA_Lookback(TimePeriod):
    """TEMA_Lookback([TimePeriod]) -> int"""
    return -1

def TRANGE(High, Low, Close):
    """TRANGE(High, Low, Close) -> (BegIdx, Real)

    TA_TRANGE - True Range
    Input  = High, Low, Close
    Output = double
    """
    return None, 1

def TRANGE_Lookback():
    """TRANGE_Lookback() -> int"""
    return -1

def TRIMA(Real, TimePeriod):
    """TRIMA(Real[, TimePeriod]) -> (BegIdx, Real)

    TA_TRIMA - Triangular Moving Average
    Input  = double
    Output = double
    Optional Parameters
    -------------------
    optInTimePeriod:(From 2 to 100000)
       Number of period
    """
    return None, 1

def TRIMA_Lookback(TimePeriod):
    """TRIMA_Lookback([TimePeriod]) -> int"""
    return -1

def TRIX(Real, TimePeriod):
    """TRIX(Real[, TimePeriod]) -> (BegIdx, Real)

    TA_TRIX - 1-day Rate-Of-Change (ROC) of a Triple Smooth EMA
    Input  = double
    Output = double
    Optional Parameters
    -------------------
    optInTimePeriod:(From 1 to 100000)
       Number of period
    """
    return None, 1

def TRIX_Lookback(TimePeriod):
    """TRIX_Lookback([TimePeriod]) -> int"""
    return -1

def TSF(Real, TimePeriod):
    """TSF(Real[, TimePeriod]) -> (BegIdx, Real)

    TA_TSF - Time Series Forecast
    Input  = double
    Output = double
    Optional Parameters
    -------------------
    optInTimePeriod:(From 2 to 100000)
       Number of period
    """
    return None, 1

def TSF_Lookback(TimePeriod):
    """TSF_Lookback([TimePeriod]) -> int"""
    return -1

def TYPPRICE(High, Low, Close):
    """TYPPRICE(High, Low, Close) -> (BegIdx, Real)

    TA_TYPPRICE - Typical Price
    Input  = High, Low, Close
    Output = double
    """
    return None, 1

def TYPPRICE_Lookback():
    """TYPPRICE_Lookback() -> int"""
    return -1

def ULTOSC(High, Low, Close, TimePeriod1, TimePeriod2, TimePeriod3):
    """ULTOSC(High, Low, Close[, TimePeriod1, TimePeriod2, TimePeriod3]) -> (BegIdx, Real)

    TA_ULTOSC - Ultimate Oscillator
    Input  = High, Low, Close
    Output = double
    Optional Parameters
    -------------------
    optInTimePeriod1:(From 1 to 100000)
       Number of bars for 1st period.
    optInTimePeriod2:(From 1 to 100000)
       Number of bars fro 2nd period
    optInTimePeriod3:(From 1 to 100000)
       Number of bars for 3rd period
    """
    return None, 1

def ULTOSC_Lookback(TimePeriod1, TimePeriod2, TimePeriod3):
    """ULTOSC_Lookback([TimePeriod1, TimePeriod2, TimePeriod3]) -> int"""
    return -1

def VAR(Real, TimePeriod, NbDev):
    """VAR(Real[, TimePeriod, NbDev]) -> (BegIdx, Real)

    TA_VAR - Variance
    Input  = double
    Output = double
    Optional Parameters
    -------------------
    optInTimePeriod:(From 1 to 100000)
       Number of period
    optInNbDev:(From TA_REAL_MIN to TA_REAL_MAX)
       Nb of deviations
    """
    return None, 1

def VAR_Lookback(TimePeriod, NbDev):
    """VAR_Lookback([TimePeriod, NbDev]) -> int"""
    return -1

def WCLPRICE(High, Low, Close):
    """WCLPRICE(High, Low, Close) -> (BegIdx, Real)

    TA_WCLPRICE - Weighted Close Price
    Input  = High, Low, Close
    Output = double
    """
    return None, 1

def WCLPRICE_Lookback():
    """WCLPRICE_Lookback() -> int"""
    return -1

def WILLR(High, Low, Close, TimePeriod):
    """WILLR(High, Low, Close[, TimePeriod]) -> (BegIdx, Real)

    TA_WILLR - Williams' %R
    Input  = High, Low, Close
    Output = double
    Optional Parameters
    -------------------
    optInTimePeriod:(From 2 to 100000)
       Number of period
    """
    return None, 1

def WILLR_Lookback(TimePeriod):
    """WILLR_Lookback([TimePeriod]) -> int"""
    return -1

def WMA(Real, TimePeriod):
    """WMA(Real[, TimePeriod]) -> (BegIdx, Real)

    TA_WMA - Weighted Moving Average
    Input  = double
    Output = double
    Optional Parameters
    -------------------
    optInTimePeriod:(From 2 to 100000)
       Number of period
    """
    return None, 1

def WMA_Lookback(TimePeriod):
    """WMA_Lookback([TimePeriod]) -> int"""
    return -1

def GetRetCodeInfo(retCode):
    """GetRetCodeInfo(retCode) -> (enumStr, infoStr)"""
    return '', ''

def _init():
    from ._talib import _talib as lib

    ENV = globals(); del ENV['_init']
    version, info, range = lib.GetLibInfo()
    names = []; any(names.extend((i,'%s_Lookback'%i)) for v in info.values() for i in v)
    names.append('GetRetCodeInfo')
    ENV.update(TA_VERSION=version, TA_FUNCS=info, __all__=names)
    ENV.update((k, getattr(lib, k)) for k in names)
    Range = 'INT_MIN', 'INT_MAX', 'INT_DEFAULT', 'REAL_MIN', 'REAL_MAX', 'REAL_DEFAULT'
    names.extend(Range); ENV.update(zip(Range, range))
    MAType = 'MA_S', 'MA_E', 'MA_W', 'MA_DE', 'MA_TE', 'MA_TRI', 'MA_KA', 'MA_MA', 'MA_T3'
    names.extend(MAType); ENV.update((v,i) for i,v in enumerate(MAType))
_init()
