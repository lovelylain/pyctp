#define PY_SSIZE_T_CLEAN
#ifndef CYTHON_USE_PYLONG_INTERNALS
#ifdef PYLONG_BITS_IN_DIGIT
#define CYTHON_USE_PYLONG_INTERNALS 0
#else
#include "pyconfig.h"
#ifdef PYLONG_BITS_IN_DIGIT
#define CYTHON_USE_PYLONG_INTERNALS 1
#else
#define CYTHON_USE_PYLONG_INTERNALS 0
#endif
#endif
#endif
#include "Python.h"
#ifndef Py_PYTHON_H
    #error Python headers needed to compile C extensions, please install development version of Python.
#elif PY_VERSION_HEX < 0x02040000
    #error Cython requires Python 2.4+.
#else
#define CYTHON_ABI "0_20_2"
#include <stddef.h> 
#ifndef offsetof
#define offsetof(type, member) ( (size_t) & ((type*)0) -> member )
#endif
#if !defined(WIN32) && !defined(MS_WINDOWS)
  #ifndef __stdcall
    #define __stdcall
  #endif
  #ifndef __cdecl
    #define __cdecl
  #endif
  #ifndef __fastcall
    #define __fastcall
  #endif
#endif
#ifndef DL_IMPORT
  #define DL_IMPORT(t) t
#endif
#ifndef DL_EXPORT
  #define DL_EXPORT(t) t
#endif
#ifndef PY_LONG_LONG
  #define PY_LONG_LONG LONG_LONG
#endif
#ifndef Py_HUGE_VAL
  #define Py_HUGE_VAL HUGE_VAL
#endif
#ifdef PYPY_VERSION
#define CYTHON_COMPILING_IN_PYPY 1
#define CYTHON_COMPILING_IN_CPYTHON 0
#else
#define CYTHON_COMPILING_IN_PYPY 0
#define CYTHON_COMPILING_IN_CPYTHON 1
#endif
#if CYTHON_COMPILING_IN_PYPY && PY_VERSION_HEX < 0x02070600
#define Py_OptimizeFlag 0
#endif
#if PY_VERSION_HEX < 0x02050000
  typedef int Py_ssize_t;
  #define PY_SSIZE_T_MAX INT_MAX
  #define PY_SSIZE_T_MIN INT_MIN
  #define PY_FORMAT_SIZE_T ""
  #define CYTHON_FORMAT_SSIZE_T ""
  #define PyInt_FromSsize_t(z) PyInt_FromLong(z)
  #define PyInt_AsSsize_t(o) __Pyx_PyInt_As_int(o)
  #define PyNumber_Index(o) ((PyNumber_Check(o) && !PyFloat_Check(o)) ? PyNumber_Int(o) : \
                                (PyErr_Format(PyExc_TypeError, \
                                              "expected index value, got %.200s", Py_TYPE(o)->tp_name), \
                                 (PyObject*)0))
  #define __Pyx_PyIndex_Check(o) (PyNumber_Check(o) && !PyFloat_Check(o) && \
                                  !PyComplex_Check(o))
  #define PyIndex_Check __Pyx_PyIndex_Check
  #define PyErr_WarnEx(category, message, stacklevel) PyErr_Warn(category, message)
  #define __PYX_BUILD_PY_SSIZE_T "i"
#else
  #define __PYX_BUILD_PY_SSIZE_T "n"
  #define CYTHON_FORMAT_SSIZE_T "z"
  #define __Pyx_PyIndex_Check PyIndex_Check
#endif
#if PY_VERSION_HEX < 0x02060000
  #define Py_REFCNT(ob) (((PyObject*)(ob))->ob_refcnt)
  #define Py_TYPE(ob) (((PyObject*)(ob))->ob_type)
  #define Py_SIZE(ob) (((PyVarObject*)(ob))->ob_size)
  #define PyVarObject_HEAD_INIT(type, size) \
          PyObject_HEAD_INIT(type) size,
  #define PyType_Modified(t)
  typedef struct {
     void *buf;
     PyObject *obj;
     Py_ssize_t len;
     Py_ssize_t itemsize;
     int readonly;
     int ndim;
     char *format;
     Py_ssize_t *shape;
     Py_ssize_t *strides;
     Py_ssize_t *suboffsets;
     void *internal;
  } Py_buffer;
  #define PyBUF_SIMPLE 0
  #define PyBUF_WRITABLE 0x0001
  #define PyBUF_FORMAT 0x0004
  #define PyBUF_ND 0x0008
  #define PyBUF_STRIDES (0x0010 | PyBUF_ND)
  #define PyBUF_C_CONTIGUOUS (0x0020 | PyBUF_STRIDES)
  #define PyBUF_F_CONTIGUOUS (0x0040 | PyBUF_STRIDES)
  #define PyBUF_ANY_CONTIGUOUS (0x0080 | PyBUF_STRIDES)
  #define PyBUF_INDIRECT (0x0100 | PyBUF_STRIDES)
  #define PyBUF_RECORDS (PyBUF_STRIDES | PyBUF_FORMAT | PyBUF_WRITABLE)
  #define PyBUF_FULL (PyBUF_INDIRECT | PyBUF_FORMAT | PyBUF_WRITABLE)
  typedef int (*getbufferproc)(PyObject *, Py_buffer *, int);
  typedef void (*releasebufferproc)(PyObject *, Py_buffer *);
#endif
#if PY_MAJOR_VERSION < 3
  #define __Pyx_BUILTIN_MODULE_NAME "__builtin__"
  #define __Pyx_PyCode_New(a, k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos) \
          PyCode_New(a+k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)
  #define __Pyx_DefaultClassType PyClass_Type
#else
  #define __Pyx_BUILTIN_MODULE_NAME "builtins"
  #define __Pyx_PyCode_New(a, k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos) \
          PyCode_New(a, k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)
  #define __Pyx_DefaultClassType PyType_Type
#endif
#if PY_VERSION_HEX < 0x02060000
  #define PyUnicode_FromString(s) PyUnicode_Decode(s, strlen(s), "UTF-8", "strict")
#endif
#if PY_MAJOR_VERSION >= 3
  #define Py_TPFLAGS_CHECKTYPES 0
  #define Py_TPFLAGS_HAVE_INDEX 0
#endif
#if (PY_VERSION_HEX < 0x02060000) || (PY_MAJOR_VERSION >= 3)
  #define Py_TPFLAGS_HAVE_NEWBUFFER 0
#endif
#if PY_VERSION_HEX < 0x02060000
  #define Py_TPFLAGS_HAVE_VERSION_TAG 0
#endif
#if PY_VERSION_HEX < 0x02060000 && !defined(Py_TPFLAGS_IS_ABSTRACT)
  #define Py_TPFLAGS_IS_ABSTRACT 0
#endif
#if PY_VERSION_HEX < 0x030400a1 && !defined(Py_TPFLAGS_HAVE_FINALIZE)
  #define Py_TPFLAGS_HAVE_FINALIZE 0
#endif
#if PY_VERSION_HEX > 0x03030000 && defined(PyUnicode_KIND)
  #define CYTHON_PEP393_ENABLED 1
  #define __Pyx_PyUnicode_READY(op) (likely(PyUnicode_IS_READY(op)) ? \
                                              0 : _PyUnicode_Ready((PyObject *)(op)))
  #define __Pyx_PyUnicode_GET_LENGTH(u) PyUnicode_GET_LENGTH(u)
  #define __Pyx_PyUnicode_READ_CHAR(u, i) PyUnicode_READ_CHAR(u, i)
  #define __Pyx_PyUnicode_KIND(u) PyUnicode_KIND(u)
  #define __Pyx_PyUnicode_DATA(u) PyUnicode_DATA(u)
  #define __Pyx_PyUnicode_READ(k, d, i) PyUnicode_READ(k, d, i)
#else
  #define CYTHON_PEP393_ENABLED 0
  #define __Pyx_PyUnicode_READY(op) (0)
  #define __Pyx_PyUnicode_GET_LENGTH(u) PyUnicode_GET_SIZE(u)
  #define __Pyx_PyUnicode_READ_CHAR(u, i) ((Py_UCS4)(PyUnicode_AS_UNICODE(u)[i]))
  #define __Pyx_PyUnicode_KIND(u) (sizeof(Py_UNICODE))
  #define __Pyx_PyUnicode_DATA(u) ((void*)PyUnicode_AS_UNICODE(u))
  #define __Pyx_PyUnicode_READ(k, d, i) ((void)(k), (Py_UCS4)(((Py_UNICODE*)d)[i]))
#endif
#if CYTHON_COMPILING_IN_PYPY
  #define __Pyx_PyUnicode_Concat(a, b) PyNumber_Add(a, b)
  #define __Pyx_PyUnicode_ConcatSafe(a, b) PyNumber_Add(a, b)
#else
  #define __Pyx_PyUnicode_Concat(a, b) PyUnicode_Concat(a, b)
  #define __Pyx_PyUnicode_ConcatSafe(a, b) ((unlikely((a) == Py_None) || unlikely((b) == Py_None)) ? \
      PyNumber_Add(a, b) : __Pyx_PyUnicode_Concat(a, b))
#endif
#define __Pyx_PyString_FormatSafe(a, b) ((unlikely((a) == Py_None)) ? PyNumber_Remainder(a, b) : __Pyx_PyString_Format(a, b))
#define __Pyx_PyUnicode_FormatSafe(a, b) ((unlikely((a) == Py_None)) ? PyNumber_Remainder(a, b) : PyUnicode_Format(a, b))
#if PY_MAJOR_VERSION >= 3
  #define __Pyx_PyString_Format(a, b) PyUnicode_Format(a, b)
#else
  #define __Pyx_PyString_Format(a, b) PyString_Format(a, b)
#endif
#if PY_MAJOR_VERSION >= 3
  #define PyBaseString_Type PyUnicode_Type
  #define PyStringObject PyUnicodeObject
  #define PyString_Type PyUnicode_Type
  #define PyString_Check PyUnicode_Check
  #define PyString_CheckExact PyUnicode_CheckExact
#endif
#if PY_VERSION_HEX < 0x02060000
  #define PyBytesObject PyStringObject
  #define PyBytes_Type PyString_Type
  #define PyBytes_Check PyString_Check
  #define PyBytes_CheckExact PyString_CheckExact
  #define PyBytes_FromString PyString_FromString
  #define PyBytes_FromStringAndSize PyString_FromStringAndSize
  #define PyBytes_FromFormat PyString_FromFormat
  #define PyBytes_DecodeEscape PyString_DecodeEscape
  #define PyBytes_AsString PyString_AsString
  #define PyBytes_AsStringAndSize PyString_AsStringAndSize
  #define PyBytes_Size PyString_Size
  #define PyBytes_AS_STRING PyString_AS_STRING
  #define PyBytes_GET_SIZE PyString_GET_SIZE
  #define PyBytes_Repr PyString_Repr
  #define PyBytes_Concat PyString_Concat
  #define PyBytes_ConcatAndDel PyString_ConcatAndDel
#endif
#if PY_MAJOR_VERSION >= 3
  #define __Pyx_PyBaseString_Check(obj) PyUnicode_Check(obj)
  #define __Pyx_PyBaseString_CheckExact(obj) PyUnicode_CheckExact(obj)
#else
  #define __Pyx_PyBaseString_Check(obj) (PyString_CheckExact(obj) || PyUnicode_CheckExact(obj) || \
                                         PyString_Check(obj) || PyUnicode_Check(obj))
  #define __Pyx_PyBaseString_CheckExact(obj) (PyString_CheckExact(obj) || PyUnicode_CheckExact(obj))
#endif
#if PY_VERSION_HEX < 0x02060000
  #define PySet_Check(obj) PyObject_TypeCheck(obj, &PySet_Type)
  #define PyFrozenSet_Check(obj) PyObject_TypeCheck(obj, &PyFrozenSet_Type)
#endif
#ifndef PySet_CheckExact
  #define PySet_CheckExact(obj) (Py_TYPE(obj) == &PySet_Type)
#endif
#define __Pyx_TypeCheck(obj, type) PyObject_TypeCheck(obj, (PyTypeObject *)type)
#if PY_MAJOR_VERSION >= 3
  #define PyIntObject PyLongObject
  #define PyInt_Type PyLong_Type
  #define PyInt_Check(op) PyLong_Check(op)
  #define PyInt_CheckExact(op) PyLong_CheckExact(op)
  #define PyInt_FromString PyLong_FromString
  #define PyInt_FromUnicode PyLong_FromUnicode
  #define PyInt_FromLong PyLong_FromLong
  #define PyInt_FromSize_t PyLong_FromSize_t
  #define PyInt_FromSsize_t PyLong_FromSsize_t
  #define PyInt_AsLong PyLong_AsLong
  #define PyInt_AS_LONG PyLong_AS_LONG
  #define PyInt_AsSsize_t PyLong_AsSsize_t
  #define PyInt_AsUnsignedLongMask PyLong_AsUnsignedLongMask
  #define PyInt_AsUnsignedLongLongMask PyLong_AsUnsignedLongLongMask
  #define PyNumber_Int PyNumber_Long
#endif
#if PY_MAJOR_VERSION >= 3
  #define PyBoolObject PyLongObject
#endif
#if PY_VERSION_HEX < 0x030200A4
  typedef long Py_hash_t;
  #define __Pyx_PyInt_FromHash_t PyInt_FromLong
  #define __Pyx_PyInt_AsHash_t PyInt_AsLong
#else
  #define __Pyx_PyInt_FromHash_t PyInt_FromSsize_t
  #define __Pyx_PyInt_AsHash_t PyInt_AsSsize_t
#endif
#if (PY_MAJOR_VERSION < 3) || (PY_VERSION_HEX >= 0x03010300)
  #define __Pyx_PySequence_GetSlice(obj, a, b) PySequence_GetSlice(obj, a, b)
  #define __Pyx_PySequence_SetSlice(obj, a, b, value) PySequence_SetSlice(obj, a, b, value)
  #define __Pyx_PySequence_DelSlice(obj, a, b) PySequence_DelSlice(obj, a, b)
#else
  #define __Pyx_PySequence_GetSlice(obj, a, b) (unlikely(!(obj)) ? \
        (PyErr_SetString(PyExc_SystemError, "null argument to internal routine"), (PyObject*)0) : \
        (likely((obj)->ob_type->tp_as_mapping) ? (PySequence_GetSlice(obj, a, b)) : \
            (PyErr_Format(PyExc_TypeError, "'%.200s' object is unsliceable", (obj)->ob_type->tp_name), (PyObject*)0)))
  #define __Pyx_PySequence_SetSlice(obj, a, b, value) (unlikely(!(obj)) ? \
        (PyErr_SetString(PyExc_SystemError, "null argument to internal routine"), -1) : \
        (likely((obj)->ob_type->tp_as_mapping) ? (PySequence_SetSlice(obj, a, b, value)) : \
            (PyErr_Format(PyExc_TypeError, "'%.200s' object doesn't support slice assignment", (obj)->ob_type->tp_name), -1)))
  #define __Pyx_PySequence_DelSlice(obj, a, b) (unlikely(!(obj)) ? \
        (PyErr_SetString(PyExc_SystemError, "null argument to internal routine"), -1) : \
        (likely((obj)->ob_type->tp_as_mapping) ? (PySequence_DelSlice(obj, a, b)) : \
            (PyErr_Format(PyExc_TypeError, "'%.200s' object doesn't support slice deletion", (obj)->ob_type->tp_name), -1)))
#endif
#if PY_MAJOR_VERSION >= 3
  #define PyMethod_New(func, self, klass) ((self) ? PyMethod_New(func, self) : PyInstanceMethod_New(func))
#endif
#if PY_VERSION_HEX < 0x02050000
  #define __Pyx_GetAttrString(o,n) PyObject_GetAttrString((o),((char *)(n)))
  #define __Pyx_SetAttrString(o,n,a) PyObject_SetAttrString((o),((char *)(n)),(a))
  #define __Pyx_DelAttrString(o,n) PyObject_DelAttrString((o),((char *)(n)))
#else
  #define __Pyx_GetAttrString(o,n) PyObject_GetAttrString((o),(n))
  #define __Pyx_SetAttrString(o,n,a) PyObject_SetAttrString((o),(n),(a))
  #define __Pyx_DelAttrString(o,n) PyObject_DelAttrString((o),(n))
#endif
#if PY_VERSION_HEX < 0x02050000
  #define __Pyx_NAMESTR(n) ((char *)(n))
  #define __Pyx_DOCSTR(n) ((char *)(n))
#else
  #define __Pyx_NAMESTR(n) (n)
  #define __Pyx_DOCSTR(n) (n)
#endif
#ifndef CYTHON_INLINE
  #if defined(__GNUC__)
    #define CYTHON_INLINE __inline__
  #elif defined(_MSC_VER)
    #define CYTHON_INLINE __inline
  #elif defined (__STDC_VERSION__) && __STDC_VERSION__ >= 199901L
    #define CYTHON_INLINE inline
  #else
    #define CYTHON_INLINE
  #endif
#endif
#ifndef CYTHON_RESTRICT
  #if defined(__GNUC__)
    #define CYTHON_RESTRICT __restrict__
  #elif defined(_MSC_VER) && _MSC_VER >= 1400
    #define CYTHON_RESTRICT __restrict
  #elif defined (__STDC_VERSION__) && __STDC_VERSION__ >= 199901L
    #define CYTHON_RESTRICT restrict
  #else
    #define CYTHON_RESTRICT
  #endif
#endif
#ifdef NAN
#define __PYX_NAN() ((float) NAN)
#else
static CYTHON_INLINE float __PYX_NAN() {
  float value;
  memset(&value, 0xFF, sizeof(value));
  return value;
}
#endif
#ifdef __cplusplus
template<typename T>
void __Pyx_call_destructor(T* x) {
    x->~T();
}
#endif
#if PY_MAJOR_VERSION >= 3
  #define __Pyx_PyNumber_Divide(x,y) PyNumber_TrueDivide(x,y)
  #define __Pyx_PyNumber_InPlaceDivide(x,y) PyNumber_InPlaceTrueDivide(x,y)
#else
  #define __Pyx_PyNumber_Divide(x,y) PyNumber_Divide(x,y)
  #define __Pyx_PyNumber_InPlaceDivide(x,y) PyNumber_InPlaceDivide(x,y)
#endif
#ifndef __PYX_EXTERN_C
  #ifdef __cplusplus
    #define __PYX_EXTERN_C extern "C"
  #else
    #define __PYX_EXTERN_C extern
  #endif
#endif
#if defined(WIN32) || defined(MS_WINDOWS)
#define _USE_MATH_DEFINES
#endif
#include <math.h>
#define __PYX_HAVE__ctp___TraderApi
#define __PYX_HAVE_API__ctp___TraderApi
#include "ThostFtdcUserApiDataType.h"
#include "ThostFtdcUserApiStruct.h"
#include "string.h"
#include "ThostFtdcTraderApi.h"
#include "ios"
#include "new"
#include "stdexcept"
#include "typeinfo"
#include "CTraderApi.h"
#ifdef _OPENMP
#include <omp.h>
#endif 
#ifdef PYREX_WITHOUT_ASSERTIONS
#define CYTHON_WITHOUT_ASSERTIONS
#endif
#ifndef CYTHON_UNUSED
#if defined(__GNUC__)
#if !(defined(__cplusplus)) || (__GNUC__ > 3 || (__GNUC__ == 3 && __GNUC_MINOR__ >= 4))
#define CYTHON_UNUSED __attribute__ ((__unused__))
#else
#define CYTHON_UNUSED
#endif
#elif defined(__ICC) || (defined(__INTEL_COMPILER) && !defined(_MSC_VER))
#define CYTHON_UNUSED __attribute__ ((__unused__))
#else
#define CYTHON_UNUSED
#endif
#endif
typedef struct {PyObject **p; char *s; const Py_ssize_t n; const char* encoding;
                const char is_unicode; const char is_str; const char intern; } __Pyx_StringTabEntry; 
#define __PYX_DEFAULT_STRING_ENCODING_IS_ASCII 0
#define __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT 0
#define __PYX_DEFAULT_STRING_ENCODING ""
#define __Pyx_PyObject_FromString __Pyx_PyBytes_FromString
#define __Pyx_PyObject_FromStringAndSize __Pyx_PyBytes_FromStringAndSize
#define __Pyx_fits_Py_ssize_t(v, type, is_signed) ( \
    (sizeof(type) < sizeof(Py_ssize_t)) || \
    (sizeof(type) > sizeof(Py_ssize_t) && \
          likely(v < (type)PY_SSIZE_T_MAX || \
                 v == (type)PY_SSIZE_T_MAX) && \
          (!is_signed || likely(v > (type)PY_SSIZE_T_MIN || \
                                v == (type)PY_SSIZE_T_MIN))) || \
    (sizeof(type) == sizeof(Py_ssize_t) && \
          (is_signed || likely(v < (type)PY_SSIZE_T_MAX || \
                               v == (type)PY_SSIZE_T_MAX))) )
static CYTHON_INLINE char* __Pyx_PyObject_AsString(PyObject*);
static CYTHON_INLINE char* __Pyx_PyObject_AsStringAndSize(PyObject*, Py_ssize_t* length);
#define __Pyx_PyByteArray_FromString(s) PyByteArray_FromStringAndSize((const char*)s, strlen((const char*)s))
#define __Pyx_PyByteArray_FromStringAndSize(s, l) PyByteArray_FromStringAndSize((const char*)s, l)
#define __Pyx_PyBytes_FromString PyBytes_FromString
#define __Pyx_PyBytes_FromStringAndSize PyBytes_FromStringAndSize
static CYTHON_INLINE PyObject* __Pyx_PyUnicode_FromString(const char*);
#if PY_MAJOR_VERSION < 3
    #define __Pyx_PyStr_FromString __Pyx_PyBytes_FromString
    #define __Pyx_PyStr_FromStringAndSize __Pyx_PyBytes_FromStringAndSize
#else
    #define __Pyx_PyStr_FromString __Pyx_PyUnicode_FromString
    #define __Pyx_PyStr_FromStringAndSize __Pyx_PyUnicode_FromStringAndSize
#endif
#define __Pyx_PyObject_AsSString(s) ((signed char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_AsUString(s) ((unsigned char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_FromUString(s) __Pyx_PyObject_FromString((const char*)s)
#define __Pyx_PyBytes_FromUString(s) __Pyx_PyBytes_FromString((const char*)s)
#define __Pyx_PyByteArray_FromUString(s) __Pyx_PyByteArray_FromString((const char*)s)
#define __Pyx_PyStr_FromUString(s) __Pyx_PyStr_FromString((const char*)s)
#define __Pyx_PyUnicode_FromUString(s) __Pyx_PyUnicode_FromString((const char*)s)
#if PY_MAJOR_VERSION < 3
static CYTHON_INLINE size_t __Pyx_Py_UNICODE_strlen(const Py_UNICODE *u)
{
    const Py_UNICODE *u_end = u;
    while (*u_end++) ;
    return (size_t)(u_end - u - 1);
}
#else
#define __Pyx_Py_UNICODE_strlen Py_UNICODE_strlen
#endif
#define __Pyx_PyUnicode_FromUnicode(u) PyUnicode_FromUnicode(u, __Pyx_Py_UNICODE_strlen(u))
#define __Pyx_PyUnicode_FromUnicodeAndLength PyUnicode_FromUnicode
#define __Pyx_PyUnicode_AsUnicode PyUnicode_AsUnicode
#define __Pyx_Owned_Py_None(b) (Py_INCREF(Py_None), Py_None)
#define __Pyx_PyBool_FromLong(b) ((b) ? (Py_INCREF(Py_True), Py_True) : (Py_INCREF(Py_False), Py_False))
static CYTHON_INLINE int __Pyx_PyObject_IsTrue(PyObject*);
static CYTHON_INLINE PyObject* __Pyx_PyNumber_Int(PyObject* x);
static CYTHON_INLINE Py_ssize_t __Pyx_PyIndex_AsSsize_t(PyObject*);
static CYTHON_INLINE PyObject * __Pyx_PyInt_FromSize_t(size_t);
#if CYTHON_COMPILING_IN_CPYTHON
#define __pyx_PyFloat_AsDouble(x) (PyFloat_CheckExact(x) ? PyFloat_AS_DOUBLE(x) : PyFloat_AsDouble(x))
#else
#define __pyx_PyFloat_AsDouble(x) PyFloat_AsDouble(x)
#endif
#define __pyx_PyFloat_AsFloat(x) ((float) __pyx_PyFloat_AsDouble(x))
#if PY_MAJOR_VERSION < 3 && __PYX_DEFAULT_STRING_ENCODING_IS_ASCII
static int __Pyx_sys_getdefaultencoding_not_ascii;
static int __Pyx_init_sys_getdefaultencoding_params(void) {
    PyObject* sys;
    PyObject* default_encoding = NULL;
    PyObject* ascii_chars_u = NULL;
    PyObject* ascii_chars_b = NULL;
    const char* default_encoding_c;
    sys = PyImport_ImportModule("sys");
    if (!sys) goto bad;
    default_encoding = PyObject_CallMethod(sys, (char*) (const char*) "getdefaultencoding", NULL);
    Py_DECREF(sys);
    if (!default_encoding) goto bad;
    default_encoding_c = PyBytes_AsString(default_encoding);
    if (!default_encoding_c) goto bad;
    if (strcmp(default_encoding_c, "ascii") == 0) {
        __Pyx_sys_getdefaultencoding_not_ascii = 0;
    } else {
        char ascii_chars[128];
        int c;
        for (c = 0; c < 128; c++) {
            ascii_chars[c] = c;
        }
        __Pyx_sys_getdefaultencoding_not_ascii = 1;
        ascii_chars_u = PyUnicode_DecodeASCII(ascii_chars, 128, NULL);
        if (!ascii_chars_u) goto bad;
        ascii_chars_b = PyUnicode_AsEncodedString(ascii_chars_u, default_encoding_c, NULL);
        if (!ascii_chars_b || !PyBytes_Check(ascii_chars_b) || memcmp(ascii_chars, PyBytes_AS_STRING(ascii_chars_b), 128) != 0) {
            PyErr_Format(
                PyExc_ValueError,
                "This module compiled with c_string_encoding=ascii, but default encoding '%.200s' is not a superset of ascii.",
                default_encoding_c);
            goto bad;
        }
        Py_DECREF(ascii_chars_u);
        Py_DECREF(ascii_chars_b);
    }
    Py_DECREF(default_encoding);
    return 0;
bad:
    Py_XDECREF(default_encoding);
    Py_XDECREF(ascii_chars_u);
    Py_XDECREF(ascii_chars_b);
    return -1;
}
#endif
#if __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT && PY_MAJOR_VERSION >= 3
#define __Pyx_PyUnicode_FromStringAndSize(c_str, size) PyUnicode_DecodeUTF8(c_str, size, NULL)
#else
#define __Pyx_PyUnicode_FromStringAndSize(c_str, size) PyUnicode_Decode(c_str, size, __PYX_DEFAULT_STRING_ENCODING, NULL)
#if __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT
static char* __PYX_DEFAULT_STRING_ENCODING;
static int __Pyx_init_sys_getdefaultencoding_params(void) {
    PyObject* sys;
    PyObject* default_encoding = NULL;
    char* default_encoding_c;
    sys = PyImport_ImportModule("sys");
    if (!sys) goto bad;
    default_encoding = PyObject_CallMethod(sys, (char*) (const char*) "getdefaultencoding", NULL);
    Py_DECREF(sys);
    if (!default_encoding) goto bad;
    default_encoding_c = PyBytes_AsString(default_encoding);
    if (!default_encoding_c) goto bad;
    __PYX_DEFAULT_STRING_ENCODING = (char*) malloc(strlen(default_encoding_c));
    if (!__PYX_DEFAULT_STRING_ENCODING) goto bad;
    strcpy(__PYX_DEFAULT_STRING_ENCODING, default_encoding_c);
    Py_DECREF(default_encoding);
    return 0;
bad:
    Py_XDECREF(default_encoding);
    return -1;
}
#endif
#endif
#if defined(__GNUC__) && (__GNUC__ > 2 || (__GNUC__ == 2 && (__GNUC_MINOR__ > 95)))
  #define likely(x) __builtin_expect(!!(x), 1)
  #define unlikely(x) __builtin_expect(!!(x), 0)
#else 
  #define likely(x) (x)
  #define unlikely(x) (x)
#endif 
static PyObject *__pyx_m;
static PyObject *__pyx_d;
static PyObject *__pyx_b;
static PyObject *__pyx_empty_tuple;
static PyObject *__pyx_empty_bytes;
static int __pyx_lineno;
static int __pyx_clineno = 0;
static const char * __pyx_cfilenm= __FILE__;
static const char *__pyx_filename;
static const char *__pyx_f[] = {
  "TraderApi.pyx",
};
struct __pyx_obj_3ctp_10_TraderApi_TraderApi;
struct __pyx_obj_3ctp_10_TraderApi_TraderApi {
  PyObject_HEAD
  CThostFtdcTraderApi *api;
  CTraderSpi *spi;
};
#ifndef CYTHON_REFNANNY
  #define CYTHON_REFNANNY 0
#endif
#if CYTHON_REFNANNY
  typedef struct {
    void (*INCREF)(void*, PyObject*, int);
    void (*DECREF)(void*, PyObject*, int);
    void (*GOTREF)(void*, PyObject*, int);
    void (*GIVEREF)(void*, PyObject*, int);
    void* (*SetupContext)(const char*, int, const char*);
    void (*FinishContext)(void**);
  } __Pyx_RefNannyAPIStruct;
  static __Pyx_RefNannyAPIStruct *__Pyx_RefNanny = NULL;
  static __Pyx_RefNannyAPIStruct *__Pyx_RefNannyImportAPI(const char *modname); 
  #define __Pyx_RefNannyDeclarations void *__pyx_refnanny = NULL;
#ifdef WITH_THREAD
  #define __Pyx_RefNannySetupContext(name, acquire_gil) \
          if (acquire_gil) { \
              PyGILState_STATE __pyx_gilstate_save = PyGILState_Ensure(); \
              __pyx_refnanny = __Pyx_RefNanny->SetupContext((name), __LINE__, __FILE__); \
              PyGILState_Release(__pyx_gilstate_save); \
          } else { \
              __pyx_refnanny = __Pyx_RefNanny->SetupContext((name), __LINE__, __FILE__); \
          }
#else
  #define __Pyx_RefNannySetupContext(name, acquire_gil) \
          __pyx_refnanny = __Pyx_RefNanny->SetupContext((name), __LINE__, __FILE__)
#endif
  #define __Pyx_RefNannyFinishContext() \
          __Pyx_RefNanny->FinishContext(&__pyx_refnanny)
  #define __Pyx_INCREF(r) __Pyx_RefNanny->INCREF(__pyx_refnanny, (PyObject *)(r), __LINE__)
  #define __Pyx_DECREF(r) __Pyx_RefNanny->DECREF(__pyx_refnanny, (PyObject *)(r), __LINE__)
  #define __Pyx_GOTREF(r) __Pyx_RefNanny->GOTREF(__pyx_refnanny, (PyObject *)(r), __LINE__)
  #define __Pyx_GIVEREF(r) __Pyx_RefNanny->GIVEREF(__pyx_refnanny, (PyObject *)(r), __LINE__)
  #define __Pyx_XINCREF(r) do { if((r) != NULL) {__Pyx_INCREF(r); }} while(0)
  #define __Pyx_XDECREF(r) do { if((r) != NULL) {__Pyx_DECREF(r); }} while(0)
  #define __Pyx_XGOTREF(r) do { if((r) != NULL) {__Pyx_GOTREF(r); }} while(0)
  #define __Pyx_XGIVEREF(r) do { if((r) != NULL) {__Pyx_GIVEREF(r);}} while(0)
#else
  #define __Pyx_RefNannyDeclarations
  #define __Pyx_RefNannySetupContext(name, acquire_gil)
  #define __Pyx_RefNannyFinishContext()
  #define __Pyx_INCREF(r) Py_INCREF(r)
  #define __Pyx_DECREF(r) Py_DECREF(r)
  #define __Pyx_GOTREF(r)
  #define __Pyx_GIVEREF(r)
  #define __Pyx_XINCREF(r) Py_XINCREF(r)
  #define __Pyx_XDECREF(r) Py_XDECREF(r)
  #define __Pyx_XGOTREF(r)
  #define __Pyx_XGIVEREF(r)
#endif 
#define __Pyx_XDECREF_SET(r, v) do { \
        PyObject *tmp = (PyObject *) r; \
        r = v; __Pyx_XDECREF(tmp); \
    } while (0)
#define __Pyx_DECREF_SET(r, v) do { \
        PyObject *tmp = (PyObject *) r; \
        r = v; __Pyx_DECREF(tmp); \
    } while (0)
#define __Pyx_CLEAR(r) do { PyObject* tmp = ((PyObject*)(r)); r = NULL; __Pyx_DECREF(tmp);} while(0)
#define __Pyx_XCLEAR(r) do { if((r) != NULL) {PyObject* tmp = ((PyObject*)(r)); r = NULL; __Pyx_DECREF(tmp);}} while(0)
static void __Pyx_RaiseDoubleKeywordsError(const char* func_name, PyObject* kw_name); 
static int __Pyx_ParseOptionalKeywords(PyObject *kwds, PyObject **argnames[], \
    PyObject *kwds2, PyObject *values[], Py_ssize_t num_pos_args, \
    const char* function_name); 
static void __Pyx_RaiseArgtupleInvalid(const char* func_name, int exact,
    Py_ssize_t num_min, Py_ssize_t num_max, Py_ssize_t num_found); 
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_Call(PyObject *func, PyObject *arg, PyObject *kw); 
#else
#define __Pyx_PyObject_Call(func, arg, kw) PyObject_Call(func, arg, kw)
#endif
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_GetAttrStr(PyObject* obj, PyObject* attr_name) {
    PyTypeObject* tp = Py_TYPE(obj);
    if (likely(tp->tp_getattro))
        return tp->tp_getattro(obj, attr_name);
#if PY_MAJOR_VERSION < 3
    if (likely(tp->tp_getattr))
        return tp->tp_getattr(obj, PyString_AS_STRING(attr_name));
#endif
    return PyObject_GetAttr(obj, attr_name);
}
#else
#define __Pyx_PyObject_GetAttrStr(o,n) PyObject_GetAttr(o,n)
#endif
static CYTHON_INLINE int __Pyx_PyInt_As_int(PyObject *);
static CYTHON_INLINE PyObject* __Pyx_PyInt_From_long(long value);
#ifndef __Pyx_CppExn2PyErr
#include <new>
#include <typeinfo>
#include <stdexcept>
#include <ios>
static void __Pyx_CppExn2PyErr() {
  try {
    if (PyErr_Occurred())
      ; 
    else
      throw;
  } catch (const std::bad_alloc& exn) {
    PyErr_SetString(PyExc_MemoryError, exn.what());
  } catch (const std::bad_cast& exn) {
    PyErr_SetString(PyExc_TypeError, exn.what());
  } catch (const std::domain_error& exn) {
    PyErr_SetString(PyExc_ValueError, exn.what());
  } catch (const std::invalid_argument& exn) {
    PyErr_SetString(PyExc_ValueError, exn.what());
  } catch (const std::ios_base::failure& exn) {
    PyErr_SetString(PyExc_IOError, exn.what());
  } catch (const std::out_of_range& exn) {
    PyErr_SetString(PyExc_IndexError, exn.what());
  } catch (const std::overflow_error& exn) {
    PyErr_SetString(PyExc_OverflowError, exn.what());
  } catch (const std::range_error& exn) {
    PyErr_SetString(PyExc_ArithmeticError, exn.what());
  } catch (const std::underflow_error& exn) {
    PyErr_SetString(PyExc_ArithmeticError, exn.what());
  } catch (const std::exception& exn) {
    PyErr_SetString(PyExc_RuntimeError, exn.what());
  }
  catch (...)
  {
    PyErr_SetString(PyExc_RuntimeError, "Unknown exception");
  }
}
#endif
#ifndef __PYX_FORCE_INIT_THREADS
  #define __PYX_FORCE_INIT_THREADS 0
#endif
static CYTHON_INLINE PyObject* __Pyx_PyInt_From_int(int value);
static CYTHON_INLINE size_t __Pyx_PyInt_As_size_t(PyObject *);
static CYTHON_INLINE long __Pyx_PyInt_As_long(PyObject *);
static int __Pyx_check_binary_version(void);
typedef struct {
    int code_line;
    PyCodeObject* code_object;
} __Pyx_CodeObjectCacheEntry;
struct __Pyx_CodeObjectCache {
    int count;
    int max_count;
    __Pyx_CodeObjectCacheEntry* entries;
};
static struct __Pyx_CodeObjectCache __pyx_code_cache = {0,0,NULL};
static int __pyx_bisect_code_objects(__Pyx_CodeObjectCacheEntry* entries, int count, int code_line);
static PyCodeObject *__pyx_find_code_object(int code_line);
static void __pyx_insert_code_object(int code_line, PyCodeObject* code_object);
static void __Pyx_AddTraceback(const char *funcname, int c_line,
                               int py_line, const char *filename); 
static int __Pyx_InitStrings(__Pyx_StringTabEntry *t); 
static PyTypeObject *__pyx_ptype_3ctp_10_TraderApi_TraderApi = 0;
static PyObject *__pyx_v_3ctp_10_TraderApi_ApiStruct_addressof = 0;
static PyObject *__pyx_v_3ctp_10_TraderApi_ApiStruct_Accountregister = 0;
static PyObject *__pyx_v_3ctp_10_TraderApi_ApiStruct_BrokerTradingAlgos = 0;
static PyObject *__pyx_v_3ctp_10_TraderApi_ApiStruct_BrokerTradingParams = 0;
static PyObject *__pyx_v_3ctp_10_TraderApi_ApiStruct_CFMMCTradingAccountKey = 0;
static PyObject *__pyx_v_3ctp_10_TraderApi_ApiStruct_CFMMCTradingAccountToken = 0;
static PyObject *__pyx_v_3ctp_10_TraderApi_ApiStruct_CancelAccount = 0;
static PyObject *__pyx_v_3ctp_10_TraderApi_ApiStruct_ChangeAccount = 0;
static PyObject *__pyx_v_3ctp_10_TraderApi_ApiStruct_ContractBank = 0;
static PyObject *__pyx_v_3ctp_10_TraderApi_ApiStruct_DepthMarketData = 0;
static PyObject *__pyx_v_3ctp_10_TraderApi_ApiStruct_EWarrantOffset = 0;
static PyObject *__pyx_v_3ctp_10_TraderApi_ApiStruct_ErrorConditionalOrder = 0;
static PyObject *__pyx_v_3ctp_10_TraderApi_ApiStruct_Exchange = 0;
static PyObject *__pyx_v_3ctp_10_TraderApi_ApiStruct_ExchangeMarginRate = 0;
static PyObject *__pyx_v_3ctp_10_TraderApi_ApiStruct_ExchangeMarginRateAdjust = 0;
static PyObject *__pyx_v_3ctp_10_TraderApi_ApiStruct_ExchangeRate = 0;
static PyObject *__pyx_v_3ctp_10_TraderApi_ApiStruct_InputOrder = 0;
static PyObject *__pyx_v_3ctp_10_TraderApi_ApiStruct_InputOrderAction = 0;
static PyObject *__pyx_v_3ctp_10_TraderApi_ApiStruct_Instrument = 0;
static PyObject *__pyx_v_3ctp_10_TraderApi_ApiStruct_InstrumentCommissionRate = 0;
static PyObject *__pyx_v_3ctp_10_TraderApi_ApiStruct_InstrumentMarginRate = 0;
static PyObject *__pyx_v_3ctp_10_TraderApi_ApiStruct_InstrumentStatus = 0;
static PyObject *__pyx_v_3ctp_10_TraderApi_ApiStruct_Investor = 0;
static PyObject *__pyx_v_3ctp_10_TraderApi_ApiStruct_InvestorPosition = 0;
static PyObject *__pyx_v_3ctp_10_TraderApi_ApiStruct_InvestorPositionCombineDetail = 0;
static PyObject *__pyx_v_3ctp_10_TraderApi_ApiStruct_InvestorPositionDetail = 0;
static PyObject *__pyx_v_3ctp_10_TraderApi_ApiStruct_InvestorProductGroupMargin = 0;
static PyObject *__pyx_v_3ctp_10_TraderApi_ApiStruct_Notice = 0;
static PyObject *__pyx_v_3ctp_10_TraderApi_ApiStruct_NotifyQueryAccount = 0;
static PyObject *__pyx_v_3ctp_10_TraderApi_ApiStruct_OpenAccount = 0;
static PyObject *__pyx_v_3ctp_10_TraderApi_ApiStruct_Order = 0;
static PyObject *__pyx_v_3ctp_10_TraderApi_ApiStruct_OrderAction = 0;
static PyObject *__pyx_v_3ctp_10_TraderApi_ApiStruct_ParkedOrder = 0;
static PyObject *__pyx_v_3ctp_10_TraderApi_ApiStruct_ParkedOrderAction = 0;
static PyObject *__pyx_v_3ctp_10_TraderApi_ApiStruct_Product = 0;
static PyObject *__pyx_v_3ctp_10_TraderApi_ApiStruct_QueryCFMMCTradingAccountToken = 0;
static PyObject *__pyx_v_3ctp_10_TraderApi_ApiStruct_QueryMaxOrderVolume = 0;
static PyObject *__pyx_v_3ctp_10_TraderApi_ApiStruct_RemoveParkedOrder = 0;
static PyObject *__pyx_v_3ctp_10_TraderApi_ApiStruct_RemoveParkedOrderAction = 0;
static PyObject *__pyx_v_3ctp_10_TraderApi_ApiStruct_ReqQueryAccount = 0;
static PyObject *__pyx_v_3ctp_10_TraderApi_ApiStruct_ReqRepeal = 0;
static PyObject *__pyx_v_3ctp_10_TraderApi_ApiStruct_ReqTransfer = 0;
static PyObject *__pyx_v_3ctp_10_TraderApi_ApiStruct_RspAuthenticate = 0;
static PyObject *__pyx_v_3ctp_10_TraderApi_ApiStruct_RspInfo = 0;
static PyObject *__pyx_v_3ctp_10_TraderApi_ApiStruct_RspRepeal = 0;
static PyObject *__pyx_v_3ctp_10_TraderApi_ApiStruct_RspTransfer = 0;
static PyObject *__pyx_v_3ctp_10_TraderApi_ApiStruct_RspUserLogin = 0;
static PyObject *__pyx_v_3ctp_10_TraderApi_ApiStruct_SecAgentACIDMap = 0;
static PyObject *__pyx_v_3ctp_10_TraderApi_ApiStruct_SettlementInfo = 0;
static PyObject *__pyx_v_3ctp_10_TraderApi_ApiStruct_SettlementInfoConfirm = 0;
static PyObject *__pyx_v_3ctp_10_TraderApi_ApiStruct_Trade = 0;
static PyObject *__pyx_v_3ctp_10_TraderApi_ApiStruct_TradingAccount = 0;
static PyObject *__pyx_v_3ctp_10_TraderApi_ApiStruct_TradingAccountPasswordUpdate = 0;
static PyObject *__pyx_v_3ctp_10_TraderApi_ApiStruct_TradingCode = 0;
static PyObject *__pyx_v_3ctp_10_TraderApi_ApiStruct_TradingNotice = 0;
static PyObject *__pyx_v_3ctp_10_TraderApi_ApiStruct_TradingNoticeInfo = 0;
static PyObject *__pyx_v_3ctp_10_TraderApi_ApiStruct_TransferBank = 0;
static PyObject *__pyx_v_3ctp_10_TraderApi_ApiStruct_TransferSerial = 0;
static PyObject *__pyx_v_3ctp_10_TraderApi_ApiStruct_UserLogout = 0;
static PyObject *__pyx_v_3ctp_10_TraderApi_ApiStruct_UserPasswordUpdate = 0;
static void __pyx_f_3ctp_10_TraderApi_TraderApi_Release(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *); 
#define __Pyx_MODULE_NAME "ctp._TraderApi"
int __pyx_module_is_main_ctp___TraderApi = 0;
static void __pyx_pf_3ctp_10_TraderApi_9TraderApi___dealloc__(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self); 
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_2Alive(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self); 
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_4Create(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, const char *__pyx_v_pszFlowPath); 
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_6Release(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self); 
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_8Init(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self); 
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_10Join(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self); 
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_12GetTradingDay(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self); 
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_14RegisterFront(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, char *__pyx_v_pszFrontAddress); 
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_16RegisterNameServer(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, char *__pyx_v_pszNsAddress); 
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_18RegisterFensUserInfo(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pFensUserInfo); 
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_20SubscribePrivateTopic(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, enum THOST_TE_RESUME_TYPE __pyx_v_nResumeType); 
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_22SubscribePublicTopic(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, enum THOST_TE_RESUME_TYPE __pyx_v_nResumeType); 
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_24ReqAuthenticate(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pReqAuthenticate, int __pyx_v_nRequestID); 
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_26ReqUserLogin(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pReqUserLogin, int __pyx_v_nRequestID); 
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_28ReqUserLogout(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pUserLogout, int __pyx_v_nRequestID); 
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_30ReqUserPasswordUpdate(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pUserPasswordUpdate, int __pyx_v_nRequestID); 
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_32ReqTradingAccountPasswordUpdate(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pTradingAccountPasswordUpdate, int __pyx_v_nRequestID); 
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_34ReqOrderInsert(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pInputOrder, int __pyx_v_nRequestID); 
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_36ReqParkedOrderInsert(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pParkedOrder, int __pyx_v_nRequestID); 
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_38ReqParkedOrderAction(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pParkedOrderAction, int __pyx_v_nRequestID); 
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_40ReqOrderAction(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pInputOrderAction, int __pyx_v_nRequestID); 
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_42ReqQueryMaxOrderVolume(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQueryMaxOrderVolume, int __pyx_v_nRequestID); 
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_44ReqSettlementInfoConfirm(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pSettlementInfoConfirm, int __pyx_v_nRequestID); 
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_46ReqRemoveParkedOrder(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pRemoveParkedOrder, int __pyx_v_nRequestID); 
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_48ReqRemoveParkedOrderAction(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pRemoveParkedOrderAction, int __pyx_v_nRequestID); 
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_50ReqQryOrder(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQryOrder, int __pyx_v_nRequestID); 
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_52ReqQryTrade(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQryTrade, int __pyx_v_nRequestID); 
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_54ReqQryInvestorPosition(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQryInvestorPosition, int __pyx_v_nRequestID); 
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_56ReqQryTradingAccount(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQryTradingAccount, int __pyx_v_nRequestID); 
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_58ReqQryInvestor(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQryInvestor, int __pyx_v_nRequestID); 
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_60ReqQryTradingCode(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQryTradingCode, int __pyx_v_nRequestID); 
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_62ReqQryInstrumentMarginRate(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQryInstrumentMarginRate, int __pyx_v_nRequestID); 
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_64ReqQryInstrumentCommissionRate(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQryInstrumentCommissionRate, int __pyx_v_nRequestID); 
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_66ReqQryExchange(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQryExchange, int __pyx_v_nRequestID); 
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_68ReqQryProduct(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQryProduct, int __pyx_v_nRequestID); 
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_70ReqQryInstrument(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQryInstrument, int __pyx_v_nRequestID); 
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_72ReqQryDepthMarketData(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQryDepthMarketData, int __pyx_v_nRequestID); 
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_74ReqQrySettlementInfo(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQrySettlementInfo, int __pyx_v_nRequestID); 
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_76ReqQryTransferBank(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQryTransferBank, int __pyx_v_nRequestID); 
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_78ReqQryInvestorPositionDetail(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQryInvestorPositionDetail, int __pyx_v_nRequestID); 
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_80ReqQryNotice(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQryNotice, int __pyx_v_nRequestID); 
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_82ReqQrySettlementInfoConfirm(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQrySettlementInfoConfirm, int __pyx_v_nRequestID); 
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_84ReqQryInvestorPositionCombineDetail(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQryInvestorPositionCombineDetail, int __pyx_v_nRequestID); 
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_86ReqQryCFMMCTradingAccountKey(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQryCFMMCTradingAccountKey, int __pyx_v_nRequestID); 
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_88ReqQryEWarrantOffset(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQryEWarrantOffset, int __pyx_v_nRequestID); 
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_90ReqQryInvestorProductGroupMargin(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQryInvestorProductGroupMargin, int __pyx_v_nRequestID); 
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_92ReqQryExchangeMarginRate(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQryExchangeMarginRate, int __pyx_v_nRequestID); 
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_94ReqQryExchangeMarginRateAdjust(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQryExchangeMarginRateAdjust, int __pyx_v_nRequestID); 
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_96ReqQryExchangeRate(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQryExchangeRate, int __pyx_v_nRequestID); 
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_98ReqQrySecAgentACIDMap(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQrySecAgentACIDMap, int __pyx_v_nRequestID); 
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_100ReqQryTransferSerial(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQryTransferSerial, int __pyx_v_nRequestID); 
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_102ReqQryAccountregister(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQryAccountregister, int __pyx_v_nRequestID); 
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_104ReqQryContractBank(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQryContractBank, int __pyx_v_nRequestID); 
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_106ReqQryParkedOrder(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQryParkedOrder, int __pyx_v_nRequestID); 
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_108ReqQryParkedOrderAction(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQryParkedOrderAction, int __pyx_v_nRequestID); 
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_110ReqQryTradingNotice(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQryTradingNotice, int __pyx_v_nRequestID); 
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_112ReqQryBrokerTradingParams(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQryBrokerTradingParams, int __pyx_v_nRequestID); 
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_114ReqQryBrokerTradingAlgos(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQryBrokerTradingAlgos, int __pyx_v_nRequestID); 
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_116ReqQueryCFMMCTradingAccountToken(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQueryCFMMCTradingAccountToken, int __pyx_v_nRequestID); 
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_118ReqFromBankToFutureByFuture(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pReqTransfer, int __pyx_v_nRequestID); 
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_120ReqFromFutureToBankByFuture(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pReqTransfer, int __pyx_v_nRequestID); 
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_122ReqQueryBankAccountMoneyByFuture(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pReqQueryAccount, int __pyx_v_nRequestID); 
static PyObject *__pyx_tp_new_3ctp_10_TraderApi_TraderApi(PyTypeObject *t, PyObject *a, PyObject *k); 
static char __pyx_k_[] = "";
static char __pyx_k_main[] = "__main__";
static char __pyx_k_test[] = "__test__";
static char __pyx_k_pQryOrder[] = "pQryOrder";
static char __pyx_k_pQryTrade[] = "pQryTrade";
static char __pyx_k_OnRspError[] = "OnRspError";
static char __pyx_k_OnRtnOrder[] = "OnRtnOrder";
static char __pyx_k_OnRtnTrade[] = "OnRtnTrade";
static char __pyx_k_nRequestID[] = "nRequestID";
static char __pyx_k_pQryNotice[] = "pQryNotice";
static char __pyx_k_pInputOrder[] = "pInputOrder";
static char __pyx_k_pQryProduct[] = "pQryProduct";
static char __pyx_k_pUserLogout[] = "pUserLogout";
static char __pyx_k_pszFlowPath[] = "pszFlowPath";
static char __pyx_k_pParkedOrder[] = "pParkedOrder";
static char __pyx_k_pQryExchange[] = "pQryExchange";
static char __pyx_k_pQryInvestor[] = "pQryInvestor";
static char __pyx_k_pReqTransfer[] = "pReqTransfer";
static char __pyx_k_OnRspQryOrder[] = "OnRspQryOrder";
static char __pyx_k_OnRspQryTrade[] = "OnRspQryTrade";
static char __pyx_k_pReqUserLogin[] = "pReqUserLogin";
static char __pyx_k_OnRspQryNotice[] = "OnRspQryNotice";
static char __pyx_k_OnRspUserLogin[] = "OnRspUserLogin";
static char __pyx_k_pQryInstrument[] = "pQryInstrument";
static char __pyx_k_OnRspQryProduct[] = "OnRspQryProduct";
static char __pyx_k_OnRspUserLogout[] = "OnRspUserLogout";
static char __pyx_k_pQryParkedOrder[] = "pQryParkedOrder";
static char __pyx_k_pQryTradingCode[] = "pQryTradingCode";
static char __pyx_k_OnFrontConnected[] = "OnFrontConnected";
static char __pyx_k_OnRspOrderAction[] = "OnRspOrderAction";
static char __pyx_k_OnRspOrderInsert[] = "OnRspOrderInsert";
static char __pyx_k_OnRspQryExchange[] = "OnRspQryExchange";
static char __pyx_k_OnRspQryInvestor[] = "OnRspQryInvestor";
static char __pyx_k_pQryContractBank[] = "pQryContractBank";
static char __pyx_k_pQryExchangeRate[] = "pQryExchangeRate";
static char __pyx_k_pQryTransferBank[] = "pQryTransferBank";
static char __pyx_k_pReqAuthenticate[] = "pReqAuthenticate";
static char __pyx_k_pReqQueryAccount[] = "pReqQueryAccount";
static char __pyx_k_OnRspAuthenticate[] = "OnRspAuthenticate";
static char __pyx_k_pInputOrderAction[] = "pInputOrderAction";
static char __pyx_k_pQryTradingNotice[] = "pQryTradingNotice";
static char __pyx_k_OnHeartBeatWarning[] = "OnHeartBeatWarning";
static char __pyx_k_OnRspQryInstrument[] = "OnRspQryInstrument";
static char __pyx_k_OnRtnTradingNotice[] = "OnRtnTradingNotice";
static char __pyx_k_pParkedOrderAction[] = "pParkedOrderAction";
static char __pyx_k_pQryEWarrantOffset[] = "pQryEWarrantOffset";
static char __pyx_k_pQrySettlementInfo[] = "pQrySettlementInfo";
static char __pyx_k_pQryTradingAccount[] = "pQryTradingAccount";
static char __pyx_k_pQryTransferSerial[] = "pQryTransferSerial";
static char __pyx_k_pRemoveParkedOrder[] = "pRemoveParkedOrder";
static char __pyx_k_OnErrRtnOrderAction[] = "OnErrRtnOrderAction";
static char __pyx_k_OnErrRtnOrderInsert[] = "OnErrRtnOrderInsert";
static char __pyx_k_OnFrontDisconnected[] = "OnFrontDisconnected";
static char __pyx_k_OnRspQryParkedOrder[] = "OnRspQryParkedOrder";
static char __pyx_k_OnRspQryTradingCode[] = "OnRspQryTradingCode";
static char __pyx_k_pQryAccountregister[] = "pQryAccountregister";
static char __pyx_k_pQryDepthMarketData[] = "pQryDepthMarketData";
static char __pyx_k_pQrySecAgentACIDMap[] = "pQrySecAgentACIDMap";
static char __pyx_k_pUserPasswordUpdate[] = "pUserPasswordUpdate";
static char __pyx_k_OnRspQryContractBank[] = "OnRspQryContractBank";
static char __pyx_k_OnRspQryExchangeRate[] = "OnRspQryExchangeRate";
static char __pyx_k_OnRspQryTransferBank[] = "OnRspQryTransferBank";
static char __pyx_k_pQryInvestorPosition[] = "pQryInvestorPosition";
static char __pyx_k_pQueryMaxOrderVolume[] = "pQueryMaxOrderVolume";
static char __pyx_k_OnRspQryTradingNotice[] = "OnRspQryTradingNotice";
static char __pyx_k_OnRtnInstrumentStatus[] = "OnRtnInstrumentStatus";
static char __pyx_k_pQryParkedOrderAction[] = "pQryParkedOrderAction";
static char __pyx_k_OnRspParkedOrderAction[] = "OnRspParkedOrderAction";
static char __pyx_k_OnRspParkedOrderInsert[] = "OnRspParkedOrderInsert";
static char __pyx_k_OnRspQryEWarrantOffset[] = "OnRspQryEWarrantOffset";
static char __pyx_k_OnRspQrySettlementInfo[] = "OnRspQrySettlementInfo";
static char __pyx_k_OnRspQryTradingAccount[] = "OnRspQryTradingAccount";
static char __pyx_k_OnRspQryTransferSerial[] = "OnRspQryTransferSerial";
static char __pyx_k_OnRspRemoveParkedOrder[] = "OnRspRemoveParkedOrder";
static char __pyx_k_OnRtnOpenAccountByBank[] = "OnRtnOpenAccountByBank";
static char __pyx_k_pQryBrokerTradingAlgos[] = "pQryBrokerTradingAlgos";
static char __pyx_k_pQryExchangeMarginRate[] = "pQryExchangeMarginRate";
static char __pyx_k_pSettlementInfoConfirm[] = "pSettlementInfoConfirm";
static char __pyx_k_OnRspQryAccountregister[] = "OnRspQryAccountregister";
static char __pyx_k_OnRspQryDepthMarketData[] = "OnRspQryDepthMarketData";
static char __pyx_k_OnRspQrySecAgentACIDMap[] = "OnRspQrySecAgentACIDMap";
static char __pyx_k_OnRspUserPasswordUpdate[] = "OnRspUserPasswordUpdate";
static char __pyx_k_pQryBrokerTradingParams[] = "pQryBrokerTradingParams";
static char __pyx_k_OnRspQryInvestorPosition[] = "OnRspQryInvestorPosition";
static char __pyx_k_OnRspQueryMaxOrderVolume[] = "OnRspQueryMaxOrderVolume";
static char __pyx_k_OnRtnCancelAccountByBank[] = "OnRtnCancelAccountByBank";
static char __pyx_k_OnRtnChangeAccountByBank[] = "OnRtnChangeAccountByBank";
static char __pyx_k_pQryInstrumentMarginRate[] = "pQryInstrumentMarginRate";
static char __pyx_k_pRemoveParkedOrderAction[] = "pRemoveParkedOrderAction";
static char __pyx_k_OnRspQryParkedOrderAction[] = "OnRspQryParkedOrderAction";
static char __pyx_k_pQrySettlementInfoConfirm[] = "pQrySettlementInfoConfirm";
static char __pyx_k_OnRspQryBrokerTradingAlgos[] = "OnRspQryBrokerTradingAlgos";
static char __pyx_k_OnRspQryExchangeMarginRate[] = "OnRspQryExchangeMarginRate";
static char __pyx_k_OnRspSettlementInfoConfirm[] = "OnRspSettlementInfoConfirm";
static char __pyx_k_OnRtnErrorConditionalOrder[] = "OnRtnErrorConditionalOrder";
static char __pyx_k_pQryCFMMCTradingAccountKey[] = "pQryCFMMCTradingAccountKey";
static char __pyx_k_pQryInvestorPositionDetail[] = "pQryInvestorPositionDetail";
static char __pyx_k_OnRspQryBrokerTradingParams[] = "OnRspQryBrokerTradingParams";
static char __pyx_k_OnRtnFromBankToFutureByBank[] = "OnRtnFromBankToFutureByBank";
static char __pyx_k_OnRtnFromFutureToBankByBank[] = "OnRtnFromFutureToBankByBank";
static char __pyx_k_OnErrRtnBankToFutureByFuture[] = "OnErrRtnBankToFutureByFuture";
static char __pyx_k_OnErrRtnFutureToBankByFuture[] = "OnErrRtnFutureToBankByFuture";
static char __pyx_k_OnRspQryInstrumentMarginRate[] = "OnRspQryInstrumentMarginRate";
static char __pyx_k_OnRspRemoveParkedOrderAction[] = "OnRspRemoveParkedOrderAction";
static char __pyx_k_pQryExchangeMarginRateAdjust[] = "pQryExchangeMarginRateAdjust";
static char __pyx_k_pQryInstrumentCommissionRate[] = "pQryInstrumentCommissionRate";
static char __pyx_k_OnRspFromBankToFutureByFuture[] = "OnRspFromBankToFutureByFuture";
static char __pyx_k_OnRspFromFutureToBankByFuture[] = "OnRspFromFutureToBankByFuture";
static char __pyx_k_OnRspQrySettlementInfoConfirm[] = "OnRspQrySettlementInfoConfirm";
static char __pyx_k_OnRtnCFMMCTradingAccountToken[] = "OnRtnCFMMCTradingAccountToken";
static char __pyx_k_OnRtnFromBankToFutureByFuture[] = "OnRtnFromBankToFutureByFuture";
static char __pyx_k_OnRtnFromFutureToBankByFuture[] = "OnRtnFromFutureToBankByFuture";
static char __pyx_k_OnRtnQueryBankBalanceByFuture[] = "OnRtnQueryBankBalanceByFuture";
static char __pyx_k_pTradingAccountPasswordUpdate[] = "pTradingAccountPasswordUpdate";
static char __pyx_k_OnRspQryCFMMCTradingAccountKey[] = "OnRspQryCFMMCTradingAccountKey";
static char __pyx_k_OnRspQryInvestorPositionDetail[] = "OnRspQryInvestorPositionDetail";
static char __pyx_k_pQryInvestorProductGroupMargin[] = "pQryInvestorProductGroupMargin";
static char __pyx_k_pQueryCFMMCTradingAccountToken[] = "pQueryCFMMCTradingAccountToken";
static char __pyx_k_OnErrRtnQueryBankBalanceByFuture[] = "OnErrRtnQueryBankBalanceByFuture";
static char __pyx_k_OnErrRtnRepealBankToFutureByFutu[] = "OnErrRtnRepealBankToFutureByFutureManual";
static char __pyx_k_OnErrRtnRepealFutureToBankByFutu[] = "OnErrRtnRepealFutureToBankByFutureManual";
static char __pyx_k_OnRspQryExchangeMarginRateAdjust[] = "OnRspQryExchangeMarginRateAdjust";
static char __pyx_k_OnRspQryInstrumentCommissionRate[] = "OnRspQryInstrumentCommissionRate";
static char __pyx_k_OnRspQryInvestorPositionCombineD[] = "OnRspQryInvestorPositionCombineDetail";
static char __pyx_k_OnRspQryInvestorProductGroupMarg[] = "OnRspQryInvestorProductGroupMargin";
static char __pyx_k_OnRspQueryBankAccountMoneyByFutu[] = "OnRspQueryBankAccountMoneyByFuture";
static char __pyx_k_OnRspQueryCFMMCTradingAccountTok[] = "OnRspQueryCFMMCTradingAccountToken";
static char __pyx_k_OnRspTradingAccountPasswordUpdat[] = "OnRspTradingAccountPasswordUpdate";
static char __pyx_k_OnRtnRepealFromBankToFutureByBan[] = "OnRtnRepealFromBankToFutureByBank";
static char __pyx_k_OnRtnRepealFromBankToFutureByFut[] = "OnRtnRepealFromBankToFutureByFutureManual";
static char __pyx_k_OnRtnRepealFromFutureToBankByBan[] = "OnRtnRepealFromFutureToBankByBank";
static char __pyx_k_OnRtnRepealFromFutureToBankByFut[] = "OnRtnRepealFromFutureToBankByFutureManual";
static char __pyx_k_pQryInvestorPositionCombineDetai[] = "pQryInvestorPositionCombineDetail";
static char __pyx_k_OnRtnRepealFromBankToFutureByFut_2[] = "OnRtnRepealFromBankToFutureByFuture";
static char __pyx_k_OnRtnRepealFromFutureToBankByFut_2[] = "OnRtnRepealFromFutureToBankByFuture";
static PyObject *__pyx_n_s_OnErrRtnBankToFutureByFuture;
static PyObject *__pyx_n_s_OnErrRtnFutureToBankByFuture;
static PyObject *__pyx_n_s_OnErrRtnOrderAction;
static PyObject *__pyx_n_s_OnErrRtnOrderInsert;
static PyObject *__pyx_n_s_OnErrRtnQueryBankBalanceByFuture;
static PyObject *__pyx_n_s_OnErrRtnRepealBankToFutureByFutu;
static PyObject *__pyx_n_s_OnErrRtnRepealFutureToBankByFutu;
static PyObject *__pyx_n_s_OnFrontConnected;
static PyObject *__pyx_n_s_OnFrontDisconnected;
static PyObject *__pyx_n_s_OnHeartBeatWarning;
static PyObject *__pyx_n_s_OnRspAuthenticate;
static PyObject *__pyx_n_s_OnRspError;
static PyObject *__pyx_n_s_OnRspFromBankToFutureByFuture;
static PyObject *__pyx_n_s_OnRspFromFutureToBankByFuture;
static PyObject *__pyx_n_s_OnRspOrderAction;
static PyObject *__pyx_n_s_OnRspOrderInsert;
static PyObject *__pyx_n_s_OnRspParkedOrderAction;
static PyObject *__pyx_n_s_OnRspParkedOrderInsert;
static PyObject *__pyx_n_s_OnRspQryAccountregister;
static PyObject *__pyx_n_s_OnRspQryBrokerTradingAlgos;
static PyObject *__pyx_n_s_OnRspQryBrokerTradingParams;
static PyObject *__pyx_n_s_OnRspQryCFMMCTradingAccountKey;
static PyObject *__pyx_n_s_OnRspQryContractBank;
static PyObject *__pyx_n_s_OnRspQryDepthMarketData;
static PyObject *__pyx_n_s_OnRspQryEWarrantOffset;
static PyObject *__pyx_n_s_OnRspQryExchange;
static PyObject *__pyx_n_s_OnRspQryExchangeMarginRate;
static PyObject *__pyx_n_s_OnRspQryExchangeMarginRateAdjust;
static PyObject *__pyx_n_s_OnRspQryExchangeRate;
static PyObject *__pyx_n_s_OnRspQryInstrument;
static PyObject *__pyx_n_s_OnRspQryInstrumentCommissionRate;
static PyObject *__pyx_n_s_OnRspQryInstrumentMarginRate;
static PyObject *__pyx_n_s_OnRspQryInvestor;
static PyObject *__pyx_n_s_OnRspQryInvestorPosition;
static PyObject *__pyx_n_s_OnRspQryInvestorPositionCombineD;
static PyObject *__pyx_n_s_OnRspQryInvestorPositionDetail;
static PyObject *__pyx_n_s_OnRspQryInvestorProductGroupMarg;
static PyObject *__pyx_n_s_OnRspQryNotice;
static PyObject *__pyx_n_s_OnRspQryOrder;
static PyObject *__pyx_n_s_OnRspQryParkedOrder;
static PyObject *__pyx_n_s_OnRspQryParkedOrderAction;
static PyObject *__pyx_n_s_OnRspQryProduct;
static PyObject *__pyx_n_s_OnRspQrySecAgentACIDMap;
static PyObject *__pyx_n_s_OnRspQrySettlementInfo;
static PyObject *__pyx_n_s_OnRspQrySettlementInfoConfirm;
static PyObject *__pyx_n_s_OnRspQryTrade;
static PyObject *__pyx_n_s_OnRspQryTradingAccount;
static PyObject *__pyx_n_s_OnRspQryTradingCode;
static PyObject *__pyx_n_s_OnRspQryTradingNotice;
static PyObject *__pyx_n_s_OnRspQryTransferBank;
static PyObject *__pyx_n_s_OnRspQryTransferSerial;
static PyObject *__pyx_n_s_OnRspQueryBankAccountMoneyByFutu;
static PyObject *__pyx_n_s_OnRspQueryCFMMCTradingAccountTok;
static PyObject *__pyx_n_s_OnRspQueryMaxOrderVolume;
static PyObject *__pyx_n_s_OnRspRemoveParkedOrder;
static PyObject *__pyx_n_s_OnRspRemoveParkedOrderAction;
static PyObject *__pyx_n_s_OnRspSettlementInfoConfirm;
static PyObject *__pyx_n_s_OnRspTradingAccountPasswordUpdat;
static PyObject *__pyx_n_s_OnRspUserLogin;
static PyObject *__pyx_n_s_OnRspUserLogout;
static PyObject *__pyx_n_s_OnRspUserPasswordUpdate;
static PyObject *__pyx_n_s_OnRtnCFMMCTradingAccountToken;
static PyObject *__pyx_n_s_OnRtnCancelAccountByBank;
static PyObject *__pyx_n_s_OnRtnChangeAccountByBank;
static PyObject *__pyx_n_s_OnRtnErrorConditionalOrder;
static PyObject *__pyx_n_s_OnRtnFromBankToFutureByBank;
static PyObject *__pyx_n_s_OnRtnFromBankToFutureByFuture;
static PyObject *__pyx_n_s_OnRtnFromFutureToBankByBank;
static PyObject *__pyx_n_s_OnRtnFromFutureToBankByFuture;
static PyObject *__pyx_n_s_OnRtnInstrumentStatus;
static PyObject *__pyx_n_s_OnRtnOpenAccountByBank;
static PyObject *__pyx_n_s_OnRtnOrder;
static PyObject *__pyx_n_s_OnRtnQueryBankBalanceByFuture;
static PyObject *__pyx_n_s_OnRtnRepealFromBankToFutureByBan;
static PyObject *__pyx_n_s_OnRtnRepealFromBankToFutureByFut;
static PyObject *__pyx_n_s_OnRtnRepealFromBankToFutureByFut_2;
static PyObject *__pyx_n_s_OnRtnRepealFromFutureToBankByBan;
static PyObject *__pyx_n_s_OnRtnRepealFromFutureToBankByFut;
static PyObject *__pyx_n_s_OnRtnRepealFromFutureToBankByFut_2;
static PyObject *__pyx_n_s_OnRtnTrade;
static PyObject *__pyx_n_s_OnRtnTradingNotice;
static PyObject *__pyx_n_s_main;
static PyObject *__pyx_n_s_nRequestID;
static PyObject *__pyx_n_s_pInputOrder;
static PyObject *__pyx_n_s_pInputOrderAction;
static PyObject *__pyx_n_s_pParkedOrder;
static PyObject *__pyx_n_s_pParkedOrderAction;
static PyObject *__pyx_n_s_pQryAccountregister;
static PyObject *__pyx_n_s_pQryBrokerTradingAlgos;
static PyObject *__pyx_n_s_pQryBrokerTradingParams;
static PyObject *__pyx_n_s_pQryCFMMCTradingAccountKey;
static PyObject *__pyx_n_s_pQryContractBank;
static PyObject *__pyx_n_s_pQryDepthMarketData;
static PyObject *__pyx_n_s_pQryEWarrantOffset;
static PyObject *__pyx_n_s_pQryExchange;
static PyObject *__pyx_n_s_pQryExchangeMarginRate;
static PyObject *__pyx_n_s_pQryExchangeMarginRateAdjust;
static PyObject *__pyx_n_s_pQryExchangeRate;
static PyObject *__pyx_n_s_pQryInstrument;
static PyObject *__pyx_n_s_pQryInstrumentCommissionRate;
static PyObject *__pyx_n_s_pQryInstrumentMarginRate;
static PyObject *__pyx_n_s_pQryInvestor;
static PyObject *__pyx_n_s_pQryInvestorPosition;
static PyObject *__pyx_n_s_pQryInvestorPositionCombineDetai;
static PyObject *__pyx_n_s_pQryInvestorPositionDetail;
static PyObject *__pyx_n_s_pQryInvestorProductGroupMargin;
static PyObject *__pyx_n_s_pQryNotice;
static PyObject *__pyx_n_s_pQryOrder;
static PyObject *__pyx_n_s_pQryParkedOrder;
static PyObject *__pyx_n_s_pQryParkedOrderAction;
static PyObject *__pyx_n_s_pQryProduct;
static PyObject *__pyx_n_s_pQrySecAgentACIDMap;
static PyObject *__pyx_n_s_pQrySettlementInfo;
static PyObject *__pyx_n_s_pQrySettlementInfoConfirm;
static PyObject *__pyx_n_s_pQryTrade;
static PyObject *__pyx_n_s_pQryTradingAccount;
static PyObject *__pyx_n_s_pQryTradingCode;
static PyObject *__pyx_n_s_pQryTradingNotice;
static PyObject *__pyx_n_s_pQryTransferBank;
static PyObject *__pyx_n_s_pQryTransferSerial;
static PyObject *__pyx_n_s_pQueryCFMMCTradingAccountToken;
static PyObject *__pyx_n_s_pQueryMaxOrderVolume;
static PyObject *__pyx_n_s_pRemoveParkedOrder;
static PyObject *__pyx_n_s_pRemoveParkedOrderAction;
static PyObject *__pyx_n_s_pReqAuthenticate;
static PyObject *__pyx_n_s_pReqQueryAccount;
static PyObject *__pyx_n_s_pReqTransfer;
static PyObject *__pyx_n_s_pReqUserLogin;
static PyObject *__pyx_n_s_pSettlementInfoConfirm;
static PyObject *__pyx_n_s_pTradingAccountPasswordUpdate;
static PyObject *__pyx_n_s_pUserLogout;
static PyObject *__pyx_n_s_pUserPasswordUpdate;
static PyObject *__pyx_n_s_pszFlowPath;
static PyObject *__pyx_n_s_test;
PyObject *_init(CYTHON_UNUSED PyObject *__pyx_v_self, PyObject *__pyx_v_m) {
  PyObject *__pyx_v_fa = NULL;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("_init", 0);
  __pyx_t_1 = PyImport_ImportModule(S_ctypes); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 8; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = PyObject_GetAttrString(__pyx_t_1, S_addressof); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 8; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_XGOTREF(__pyx_v_3ctp_10_TraderApi_ApiStruct_addressof);
  __Pyx_DECREF_SET(__pyx_v_3ctp_10_TraderApi_ApiStruct_addressof, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  __pyx_t_2 = 0;
  __pyx_t_2 = XStr(S_from_address); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 9; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_v_fa = __pyx_t_2;
  __pyx_t_2 = 0;
  __pyx_t_2 = PyObject_GetAttrString(__pyx_v_m, S_Accountregister); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 10; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_1 = PyObject_GetAttr(__pyx_t_2, __pyx_v_fa); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 10; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_XGOTREF(__pyx_v_3ctp_10_TraderApi_ApiStruct_Accountregister);
  __Pyx_DECREF_SET(__pyx_v_3ctp_10_TraderApi_ApiStruct_Accountregister, __pyx_t_1);
  __Pyx_GIVEREF(__pyx_t_1);
  __pyx_t_1 = 0;
  __pyx_t_1 = PyObject_GetAttrString(__pyx_v_m, S_BrokerTradingAlgos); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 11; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = PyObject_GetAttr(__pyx_t_1, __pyx_v_fa); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 11; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_XGOTREF(__pyx_v_3ctp_10_TraderApi_ApiStruct_BrokerTradingAlgos);
  __Pyx_DECREF_SET(__pyx_v_3ctp_10_TraderApi_ApiStruct_BrokerTradingAlgos, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  __pyx_t_2 = 0;
  __pyx_t_2 = PyObject_GetAttrString(__pyx_v_m, S_BrokerTradingParams); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 12; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_1 = PyObject_GetAttr(__pyx_t_2, __pyx_v_fa); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 12; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_XGOTREF(__pyx_v_3ctp_10_TraderApi_ApiStruct_BrokerTradingParams);
  __Pyx_DECREF_SET(__pyx_v_3ctp_10_TraderApi_ApiStruct_BrokerTradingParams, __pyx_t_1);
  __Pyx_GIVEREF(__pyx_t_1);
  __pyx_t_1 = 0;
  __pyx_t_1 = PyObject_GetAttrString(__pyx_v_m, S_CFMMCTradingAccountKey); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 13; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = PyObject_GetAttr(__pyx_t_1, __pyx_v_fa); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 13; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_XGOTREF(__pyx_v_3ctp_10_TraderApi_ApiStruct_CFMMCTradingAccountKey);
  __Pyx_DECREF_SET(__pyx_v_3ctp_10_TraderApi_ApiStruct_CFMMCTradingAccountKey, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  __pyx_t_2 = 0;
  __pyx_t_2 = PyObject_GetAttrString(__pyx_v_m, S_CFMMCTradingAccountToken); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 14; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_1 = PyObject_GetAttr(__pyx_t_2, __pyx_v_fa); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 14; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_XGOTREF(__pyx_v_3ctp_10_TraderApi_ApiStruct_CFMMCTradingAccountToken);
  __Pyx_DECREF_SET(__pyx_v_3ctp_10_TraderApi_ApiStruct_CFMMCTradingAccountToken, __pyx_t_1);
  __Pyx_GIVEREF(__pyx_t_1);
  __pyx_t_1 = 0;
  __pyx_t_1 = PyObject_GetAttrString(__pyx_v_m, S_CancelAccount); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 15; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = PyObject_GetAttr(__pyx_t_1, __pyx_v_fa); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 15; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_XGOTREF(__pyx_v_3ctp_10_TraderApi_ApiStruct_CancelAccount);
  __Pyx_DECREF_SET(__pyx_v_3ctp_10_TraderApi_ApiStruct_CancelAccount, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  __pyx_t_2 = 0;
  __pyx_t_2 = PyObject_GetAttrString(__pyx_v_m, S_ChangeAccount); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 16; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_1 = PyObject_GetAttr(__pyx_t_2, __pyx_v_fa); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 16; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_XGOTREF(__pyx_v_3ctp_10_TraderApi_ApiStruct_ChangeAccount);
  __Pyx_DECREF_SET(__pyx_v_3ctp_10_TraderApi_ApiStruct_ChangeAccount, __pyx_t_1);
  __Pyx_GIVEREF(__pyx_t_1);
  __pyx_t_1 = 0;
  __pyx_t_1 = PyObject_GetAttrString(__pyx_v_m, S_ContractBank); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 17; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = PyObject_GetAttr(__pyx_t_1, __pyx_v_fa); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 17; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_XGOTREF(__pyx_v_3ctp_10_TraderApi_ApiStruct_ContractBank);
  __Pyx_DECREF_SET(__pyx_v_3ctp_10_TraderApi_ApiStruct_ContractBank, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  __pyx_t_2 = 0;
  __pyx_t_2 = PyObject_GetAttrString(__pyx_v_m, S_DepthMarketData); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 18; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_1 = PyObject_GetAttr(__pyx_t_2, __pyx_v_fa); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 18; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_XGOTREF(__pyx_v_3ctp_10_TraderApi_ApiStruct_DepthMarketData);
  __Pyx_DECREF_SET(__pyx_v_3ctp_10_TraderApi_ApiStruct_DepthMarketData, __pyx_t_1);
  __Pyx_GIVEREF(__pyx_t_1);
  __pyx_t_1 = 0;
  __pyx_t_1 = PyObject_GetAttrString(__pyx_v_m, S_EWarrantOffset); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 19; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = PyObject_GetAttr(__pyx_t_1, __pyx_v_fa); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 19; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_XGOTREF(__pyx_v_3ctp_10_TraderApi_ApiStruct_EWarrantOffset);
  __Pyx_DECREF_SET(__pyx_v_3ctp_10_TraderApi_ApiStruct_EWarrantOffset, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  __pyx_t_2 = 0;
  __pyx_t_2 = PyObject_GetAttrString(__pyx_v_m, S_ErrorConditionalOrder); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 20; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_1 = PyObject_GetAttr(__pyx_t_2, __pyx_v_fa); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 20; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_XGOTREF(__pyx_v_3ctp_10_TraderApi_ApiStruct_ErrorConditionalOrder);
  __Pyx_DECREF_SET(__pyx_v_3ctp_10_TraderApi_ApiStruct_ErrorConditionalOrder, __pyx_t_1);
  __Pyx_GIVEREF(__pyx_t_1);
  __pyx_t_1 = 0;
  __pyx_t_1 = PyObject_GetAttrString(__pyx_v_m, S_Exchange); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 21; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = PyObject_GetAttr(__pyx_t_1, __pyx_v_fa); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 21; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_XGOTREF(__pyx_v_3ctp_10_TraderApi_ApiStruct_Exchange);
  __Pyx_DECREF_SET(__pyx_v_3ctp_10_TraderApi_ApiStruct_Exchange, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  __pyx_t_2 = 0;
  __pyx_t_2 = PyObject_GetAttrString(__pyx_v_m, S_ExchangeMarginRate); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 22; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_1 = PyObject_GetAttr(__pyx_t_2, __pyx_v_fa); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 22; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_XGOTREF(__pyx_v_3ctp_10_TraderApi_ApiStruct_ExchangeMarginRate);
  __Pyx_DECREF_SET(__pyx_v_3ctp_10_TraderApi_ApiStruct_ExchangeMarginRate, __pyx_t_1);
  __Pyx_GIVEREF(__pyx_t_1);
  __pyx_t_1 = 0;
  __pyx_t_1 = PyObject_GetAttrString(__pyx_v_m, S_ExchangeMarginRateAdjust); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 23; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = PyObject_GetAttr(__pyx_t_1, __pyx_v_fa); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 23; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_XGOTREF(__pyx_v_3ctp_10_TraderApi_ApiStruct_ExchangeMarginRateAdjust);
  __Pyx_DECREF_SET(__pyx_v_3ctp_10_TraderApi_ApiStruct_ExchangeMarginRateAdjust, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  __pyx_t_2 = 0;
  __pyx_t_2 = PyObject_GetAttrString(__pyx_v_m, S_ExchangeRate); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 24; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_1 = PyObject_GetAttr(__pyx_t_2, __pyx_v_fa); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 24; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_XGOTREF(__pyx_v_3ctp_10_TraderApi_ApiStruct_ExchangeRate);
  __Pyx_DECREF_SET(__pyx_v_3ctp_10_TraderApi_ApiStruct_ExchangeRate, __pyx_t_1);
  __Pyx_GIVEREF(__pyx_t_1);
  __pyx_t_1 = 0;
  __pyx_t_1 = PyObject_GetAttrString(__pyx_v_m, S_InputOrder); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 25; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = PyObject_GetAttr(__pyx_t_1, __pyx_v_fa); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 25; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_XGOTREF(__pyx_v_3ctp_10_TraderApi_ApiStruct_InputOrder);
  __Pyx_DECREF_SET(__pyx_v_3ctp_10_TraderApi_ApiStruct_InputOrder, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  __pyx_t_2 = 0;
  __pyx_t_2 = PyObject_GetAttrString(__pyx_v_m, S_InputOrderAction); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 26; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_1 = PyObject_GetAttr(__pyx_t_2, __pyx_v_fa); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 26; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_XGOTREF(__pyx_v_3ctp_10_TraderApi_ApiStruct_InputOrderAction);
  __Pyx_DECREF_SET(__pyx_v_3ctp_10_TraderApi_ApiStruct_InputOrderAction, __pyx_t_1);
  __Pyx_GIVEREF(__pyx_t_1);
  __pyx_t_1 = 0;
  __pyx_t_1 = PyObject_GetAttrString(__pyx_v_m, S_Instrument); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 27; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = PyObject_GetAttr(__pyx_t_1, __pyx_v_fa); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 27; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_XGOTREF(__pyx_v_3ctp_10_TraderApi_ApiStruct_Instrument);
  __Pyx_DECREF_SET(__pyx_v_3ctp_10_TraderApi_ApiStruct_Instrument, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  __pyx_t_2 = 0;
  __pyx_t_2 = PyObject_GetAttrString(__pyx_v_m, S_InstrumentCommissionRate); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 28; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_1 = PyObject_GetAttr(__pyx_t_2, __pyx_v_fa); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 28; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_XGOTREF(__pyx_v_3ctp_10_TraderApi_ApiStruct_InstrumentCommissionRate);
  __Pyx_DECREF_SET(__pyx_v_3ctp_10_TraderApi_ApiStruct_InstrumentCommissionRate, __pyx_t_1);
  __Pyx_GIVEREF(__pyx_t_1);
  __pyx_t_1 = 0;
  __pyx_t_1 = PyObject_GetAttrString(__pyx_v_m, S_InstrumentMarginRate); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 29; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = PyObject_GetAttr(__pyx_t_1, __pyx_v_fa); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 29; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_XGOTREF(__pyx_v_3ctp_10_TraderApi_ApiStruct_InstrumentMarginRate);
  __Pyx_DECREF_SET(__pyx_v_3ctp_10_TraderApi_ApiStruct_InstrumentMarginRate, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  __pyx_t_2 = 0;
  __pyx_t_2 = PyObject_GetAttrString(__pyx_v_m, S_InstrumentStatus); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 30; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_1 = PyObject_GetAttr(__pyx_t_2, __pyx_v_fa); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 30; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_XGOTREF(__pyx_v_3ctp_10_TraderApi_ApiStruct_InstrumentStatus);
  __Pyx_DECREF_SET(__pyx_v_3ctp_10_TraderApi_ApiStruct_InstrumentStatus, __pyx_t_1);
  __Pyx_GIVEREF(__pyx_t_1);
  __pyx_t_1 = 0;
  __pyx_t_1 = PyObject_GetAttrString(__pyx_v_m, S_Investor); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 31; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = PyObject_GetAttr(__pyx_t_1, __pyx_v_fa); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 31; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_XGOTREF(__pyx_v_3ctp_10_TraderApi_ApiStruct_Investor);
  __Pyx_DECREF_SET(__pyx_v_3ctp_10_TraderApi_ApiStruct_Investor, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  __pyx_t_2 = 0;
  __pyx_t_2 = PyObject_GetAttrString(__pyx_v_m, S_InvestorPosition); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 32; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_1 = PyObject_GetAttr(__pyx_t_2, __pyx_v_fa); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 32; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_XGOTREF(__pyx_v_3ctp_10_TraderApi_ApiStruct_InvestorPosition);
  __Pyx_DECREF_SET(__pyx_v_3ctp_10_TraderApi_ApiStruct_InvestorPosition, __pyx_t_1);
  __Pyx_GIVEREF(__pyx_t_1);
  __pyx_t_1 = 0;
  __pyx_t_1 = PyObject_GetAttrString(__pyx_v_m, S_InvestorPositionCombineDetail); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 33; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = PyObject_GetAttr(__pyx_t_1, __pyx_v_fa); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 33; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_XGOTREF(__pyx_v_3ctp_10_TraderApi_ApiStruct_InvestorPositionCombineDetail);
  __Pyx_DECREF_SET(__pyx_v_3ctp_10_TraderApi_ApiStruct_InvestorPositionCombineDetail, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  __pyx_t_2 = 0;
  __pyx_t_2 = PyObject_GetAttrString(__pyx_v_m, S_InvestorPositionDetail); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 34; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_1 = PyObject_GetAttr(__pyx_t_2, __pyx_v_fa); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 34; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_XGOTREF(__pyx_v_3ctp_10_TraderApi_ApiStruct_InvestorPositionDetail);
  __Pyx_DECREF_SET(__pyx_v_3ctp_10_TraderApi_ApiStruct_InvestorPositionDetail, __pyx_t_1);
  __Pyx_GIVEREF(__pyx_t_1);
  __pyx_t_1 = 0;
  __pyx_t_1 = PyObject_GetAttrString(__pyx_v_m, S_InvestorProductGroupMargin); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 35; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = PyObject_GetAttr(__pyx_t_1, __pyx_v_fa); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 35; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_XGOTREF(__pyx_v_3ctp_10_TraderApi_ApiStruct_InvestorProductGroupMargin);
  __Pyx_DECREF_SET(__pyx_v_3ctp_10_TraderApi_ApiStruct_InvestorProductGroupMargin, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  __pyx_t_2 = 0;
  __pyx_t_2 = PyObject_GetAttrString(__pyx_v_m, S_Notice); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 36; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_1 = PyObject_GetAttr(__pyx_t_2, __pyx_v_fa); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 36; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_XGOTREF(__pyx_v_3ctp_10_TraderApi_ApiStruct_Notice);
  __Pyx_DECREF_SET(__pyx_v_3ctp_10_TraderApi_ApiStruct_Notice, __pyx_t_1);
  __Pyx_GIVEREF(__pyx_t_1);
  __pyx_t_1 = 0;
  __pyx_t_1 = PyObject_GetAttrString(__pyx_v_m, S_NotifyQueryAccount); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 37; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = PyObject_GetAttr(__pyx_t_1, __pyx_v_fa); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 37; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_XGOTREF(__pyx_v_3ctp_10_TraderApi_ApiStruct_NotifyQueryAccount);
  __Pyx_DECREF_SET(__pyx_v_3ctp_10_TraderApi_ApiStruct_NotifyQueryAccount, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  __pyx_t_2 = 0;
  __pyx_t_2 = PyObject_GetAttrString(__pyx_v_m, S_OpenAccount); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 38; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_1 = PyObject_GetAttr(__pyx_t_2, __pyx_v_fa); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 38; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_XGOTREF(__pyx_v_3ctp_10_TraderApi_ApiStruct_OpenAccount);
  __Pyx_DECREF_SET(__pyx_v_3ctp_10_TraderApi_ApiStruct_OpenAccount, __pyx_t_1);
  __Pyx_GIVEREF(__pyx_t_1);
  __pyx_t_1 = 0;
  __pyx_t_1 = PyObject_GetAttrString(__pyx_v_m, S_Order); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 39; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = PyObject_GetAttr(__pyx_t_1, __pyx_v_fa); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 39; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_XGOTREF(__pyx_v_3ctp_10_TraderApi_ApiStruct_Order);
  __Pyx_DECREF_SET(__pyx_v_3ctp_10_TraderApi_ApiStruct_Order, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  __pyx_t_2 = 0;
  __pyx_t_2 = PyObject_GetAttrString(__pyx_v_m, S_OrderAction); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 40; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_1 = PyObject_GetAttr(__pyx_t_2, __pyx_v_fa); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 40; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_XGOTREF(__pyx_v_3ctp_10_TraderApi_ApiStruct_OrderAction);
  __Pyx_DECREF_SET(__pyx_v_3ctp_10_TraderApi_ApiStruct_OrderAction, __pyx_t_1);
  __Pyx_GIVEREF(__pyx_t_1);
  __pyx_t_1 = 0;
  __pyx_t_1 = PyObject_GetAttrString(__pyx_v_m, S_ParkedOrder); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 41; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = PyObject_GetAttr(__pyx_t_1, __pyx_v_fa); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 41; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_XGOTREF(__pyx_v_3ctp_10_TraderApi_ApiStruct_ParkedOrder);
  __Pyx_DECREF_SET(__pyx_v_3ctp_10_TraderApi_ApiStruct_ParkedOrder, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  __pyx_t_2 = 0;
  __pyx_t_2 = PyObject_GetAttrString(__pyx_v_m, S_ParkedOrderAction); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 42; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_1 = PyObject_GetAttr(__pyx_t_2, __pyx_v_fa); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 42; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_XGOTREF(__pyx_v_3ctp_10_TraderApi_ApiStruct_ParkedOrderAction);
  __Pyx_DECREF_SET(__pyx_v_3ctp_10_TraderApi_ApiStruct_ParkedOrderAction, __pyx_t_1);
  __Pyx_GIVEREF(__pyx_t_1);
  __pyx_t_1 = 0;
  __pyx_t_1 = PyObject_GetAttrString(__pyx_v_m, S_Product); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 43; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = PyObject_GetAttr(__pyx_t_1, __pyx_v_fa); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 43; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_XGOTREF(__pyx_v_3ctp_10_TraderApi_ApiStruct_Product);
  __Pyx_DECREF_SET(__pyx_v_3ctp_10_TraderApi_ApiStruct_Product, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  __pyx_t_2 = 0;
  __pyx_t_2 = PyObject_GetAttrString(__pyx_v_m, S_QueryCFMMCTradingAccountToken); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 44; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_1 = PyObject_GetAttr(__pyx_t_2, __pyx_v_fa); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 44; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_XGOTREF(__pyx_v_3ctp_10_TraderApi_ApiStruct_QueryCFMMCTradingAccountToken);
  __Pyx_DECREF_SET(__pyx_v_3ctp_10_TraderApi_ApiStruct_QueryCFMMCTradingAccountToken, __pyx_t_1);
  __Pyx_GIVEREF(__pyx_t_1);
  __pyx_t_1 = 0;
  __pyx_t_1 = PyObject_GetAttrString(__pyx_v_m, S_QueryMaxOrderVolume); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 45; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = PyObject_GetAttr(__pyx_t_1, __pyx_v_fa); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 45; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_XGOTREF(__pyx_v_3ctp_10_TraderApi_ApiStruct_QueryMaxOrderVolume);
  __Pyx_DECREF_SET(__pyx_v_3ctp_10_TraderApi_ApiStruct_QueryMaxOrderVolume, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  __pyx_t_2 = 0;
  __pyx_t_2 = PyObject_GetAttrString(__pyx_v_m, S_RemoveParkedOrder); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 46; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_1 = PyObject_GetAttr(__pyx_t_2, __pyx_v_fa); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 46; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_XGOTREF(__pyx_v_3ctp_10_TraderApi_ApiStruct_RemoveParkedOrder);
  __Pyx_DECREF_SET(__pyx_v_3ctp_10_TraderApi_ApiStruct_RemoveParkedOrder, __pyx_t_1);
  __Pyx_GIVEREF(__pyx_t_1);
  __pyx_t_1 = 0;
  __pyx_t_1 = PyObject_GetAttrString(__pyx_v_m, S_RemoveParkedOrderAction); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 47; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = PyObject_GetAttr(__pyx_t_1, __pyx_v_fa); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 47; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_XGOTREF(__pyx_v_3ctp_10_TraderApi_ApiStruct_RemoveParkedOrderAction);
  __Pyx_DECREF_SET(__pyx_v_3ctp_10_TraderApi_ApiStruct_RemoveParkedOrderAction, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  __pyx_t_2 = 0;
  __pyx_t_2 = PyObject_GetAttrString(__pyx_v_m, S_ReqQueryAccount); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 48; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_1 = PyObject_GetAttr(__pyx_t_2, __pyx_v_fa); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 48; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_XGOTREF(__pyx_v_3ctp_10_TraderApi_ApiStruct_ReqQueryAccount);
  __Pyx_DECREF_SET(__pyx_v_3ctp_10_TraderApi_ApiStruct_ReqQueryAccount, __pyx_t_1);
  __Pyx_GIVEREF(__pyx_t_1);
  __pyx_t_1 = 0;
  __pyx_t_1 = PyObject_GetAttrString(__pyx_v_m, S_ReqRepeal); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 49; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = PyObject_GetAttr(__pyx_t_1, __pyx_v_fa); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 49; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_XGOTREF(__pyx_v_3ctp_10_TraderApi_ApiStruct_ReqRepeal);
  __Pyx_DECREF_SET(__pyx_v_3ctp_10_TraderApi_ApiStruct_ReqRepeal, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  __pyx_t_2 = 0;
  __pyx_t_2 = PyObject_GetAttrString(__pyx_v_m, S_ReqTransfer); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 50; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_1 = PyObject_GetAttr(__pyx_t_2, __pyx_v_fa); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 50; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_XGOTREF(__pyx_v_3ctp_10_TraderApi_ApiStruct_ReqTransfer);
  __Pyx_DECREF_SET(__pyx_v_3ctp_10_TraderApi_ApiStruct_ReqTransfer, __pyx_t_1);
  __Pyx_GIVEREF(__pyx_t_1);
  __pyx_t_1 = 0;
  __pyx_t_1 = PyObject_GetAttrString(__pyx_v_m, S_RspAuthenticate); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 51; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = PyObject_GetAttr(__pyx_t_1, __pyx_v_fa); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 51; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_XGOTREF(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspAuthenticate);
  __Pyx_DECREF_SET(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspAuthenticate, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  __pyx_t_2 = 0;
  __pyx_t_2 = PyObject_GetAttrString(__pyx_v_m, S_RspInfo); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 52; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_1 = PyObject_GetAttr(__pyx_t_2, __pyx_v_fa); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 52; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_XGOTREF(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspInfo);
  __Pyx_DECREF_SET(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspInfo, __pyx_t_1);
  __Pyx_GIVEREF(__pyx_t_1);
  __pyx_t_1 = 0;
  __pyx_t_1 = PyObject_GetAttrString(__pyx_v_m, S_RspRepeal); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 53; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = PyObject_GetAttr(__pyx_t_1, __pyx_v_fa); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 53; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_XGOTREF(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspRepeal);
  __Pyx_DECREF_SET(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspRepeal, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  __pyx_t_2 = 0;
  __pyx_t_2 = PyObject_GetAttrString(__pyx_v_m, S_RspTransfer); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 54; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_1 = PyObject_GetAttr(__pyx_t_2, __pyx_v_fa); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 54; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_XGOTREF(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspTransfer);
  __Pyx_DECREF_SET(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspTransfer, __pyx_t_1);
  __Pyx_GIVEREF(__pyx_t_1);
  __pyx_t_1 = 0;
  __pyx_t_1 = PyObject_GetAttrString(__pyx_v_m, S_RspUserLogin); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 55; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = PyObject_GetAttr(__pyx_t_1, __pyx_v_fa); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 55; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_XGOTREF(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspUserLogin);
  __Pyx_DECREF_SET(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspUserLogin, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  __pyx_t_2 = 0;
  __pyx_t_2 = PyObject_GetAttrString(__pyx_v_m, S_SecAgentACIDMap); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 56; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_1 = PyObject_GetAttr(__pyx_t_2, __pyx_v_fa); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 56; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_XGOTREF(__pyx_v_3ctp_10_TraderApi_ApiStruct_SecAgentACIDMap);
  __Pyx_DECREF_SET(__pyx_v_3ctp_10_TraderApi_ApiStruct_SecAgentACIDMap, __pyx_t_1);
  __Pyx_GIVEREF(__pyx_t_1);
  __pyx_t_1 = 0;
  __pyx_t_1 = PyObject_GetAttrString(__pyx_v_m, S_SettlementInfo); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 57; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = PyObject_GetAttr(__pyx_t_1, __pyx_v_fa); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 57; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_XGOTREF(__pyx_v_3ctp_10_TraderApi_ApiStruct_SettlementInfo);
  __Pyx_DECREF_SET(__pyx_v_3ctp_10_TraderApi_ApiStruct_SettlementInfo, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  __pyx_t_2 = 0;
  __pyx_t_2 = PyObject_GetAttrString(__pyx_v_m, S_SettlementInfoConfirm); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 58; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_1 = PyObject_GetAttr(__pyx_t_2, __pyx_v_fa); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 58; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_XGOTREF(__pyx_v_3ctp_10_TraderApi_ApiStruct_SettlementInfoConfirm);
  __Pyx_DECREF_SET(__pyx_v_3ctp_10_TraderApi_ApiStruct_SettlementInfoConfirm, __pyx_t_1);
  __Pyx_GIVEREF(__pyx_t_1);
  __pyx_t_1 = 0;
  __pyx_t_1 = PyObject_GetAttrString(__pyx_v_m, S_Trade); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 59; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = PyObject_GetAttr(__pyx_t_1, __pyx_v_fa); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 59; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_XGOTREF(__pyx_v_3ctp_10_TraderApi_ApiStruct_Trade);
  __Pyx_DECREF_SET(__pyx_v_3ctp_10_TraderApi_ApiStruct_Trade, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  __pyx_t_2 = 0;
  __pyx_t_2 = PyObject_GetAttrString(__pyx_v_m, S_TradingAccount); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 60; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_1 = PyObject_GetAttr(__pyx_t_2, __pyx_v_fa); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 60; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_XGOTREF(__pyx_v_3ctp_10_TraderApi_ApiStruct_TradingAccount);
  __Pyx_DECREF_SET(__pyx_v_3ctp_10_TraderApi_ApiStruct_TradingAccount, __pyx_t_1);
  __Pyx_GIVEREF(__pyx_t_1);
  __pyx_t_1 = 0;
  __pyx_t_1 = PyObject_GetAttrString(__pyx_v_m, S_TradingAccountPasswordUpdate); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 61; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = PyObject_GetAttr(__pyx_t_1, __pyx_v_fa); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 61; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_XGOTREF(__pyx_v_3ctp_10_TraderApi_ApiStruct_TradingAccountPasswordUpdate);
  __Pyx_DECREF_SET(__pyx_v_3ctp_10_TraderApi_ApiStruct_TradingAccountPasswordUpdate, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  __pyx_t_2 = 0;
  __pyx_t_2 = PyObject_GetAttrString(__pyx_v_m, S_TradingCode); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 62; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_1 = PyObject_GetAttr(__pyx_t_2, __pyx_v_fa); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 62; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_XGOTREF(__pyx_v_3ctp_10_TraderApi_ApiStruct_TradingCode);
  __Pyx_DECREF_SET(__pyx_v_3ctp_10_TraderApi_ApiStruct_TradingCode, __pyx_t_1);
  __Pyx_GIVEREF(__pyx_t_1);
  __pyx_t_1 = 0;
  __pyx_t_1 = PyObject_GetAttrString(__pyx_v_m, S_TradingNotice); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 63; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = PyObject_GetAttr(__pyx_t_1, __pyx_v_fa); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 63; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_XGOTREF(__pyx_v_3ctp_10_TraderApi_ApiStruct_TradingNotice);
  __Pyx_DECREF_SET(__pyx_v_3ctp_10_TraderApi_ApiStruct_TradingNotice, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  __pyx_t_2 = 0;
  __pyx_t_2 = PyObject_GetAttrString(__pyx_v_m, S_TradingNoticeInfo); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 64; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_1 = PyObject_GetAttr(__pyx_t_2, __pyx_v_fa); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 64; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_XGOTREF(__pyx_v_3ctp_10_TraderApi_ApiStruct_TradingNoticeInfo);
  __Pyx_DECREF_SET(__pyx_v_3ctp_10_TraderApi_ApiStruct_TradingNoticeInfo, __pyx_t_1);
  __Pyx_GIVEREF(__pyx_t_1);
  __pyx_t_1 = 0;
  __pyx_t_1 = PyObject_GetAttrString(__pyx_v_m, S_TransferBank); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 65; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = PyObject_GetAttr(__pyx_t_1, __pyx_v_fa); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 65; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_XGOTREF(__pyx_v_3ctp_10_TraderApi_ApiStruct_TransferBank);
  __Pyx_DECREF_SET(__pyx_v_3ctp_10_TraderApi_ApiStruct_TransferBank, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  __pyx_t_2 = 0;
  __pyx_t_2 = PyObject_GetAttrString(__pyx_v_m, S_TransferSerial); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 66; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_1 = PyObject_GetAttr(__pyx_t_2, __pyx_v_fa); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 66; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_XGOTREF(__pyx_v_3ctp_10_TraderApi_ApiStruct_TransferSerial);
  __Pyx_DECREF_SET(__pyx_v_3ctp_10_TraderApi_ApiStruct_TransferSerial, __pyx_t_1);
  __Pyx_GIVEREF(__pyx_t_1);
  __pyx_t_1 = 0;
  __pyx_t_1 = PyObject_GetAttrString(__pyx_v_m, S_UserLogout); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 67; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = PyObject_GetAttr(__pyx_t_1, __pyx_v_fa); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 67; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_XGOTREF(__pyx_v_3ctp_10_TraderApi_ApiStruct_UserLogout);
  __Pyx_DECREF_SET(__pyx_v_3ctp_10_TraderApi_ApiStruct_UserLogout, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  __pyx_t_2 = 0;
  __pyx_t_2 = PyObject_GetAttrString(__pyx_v_m, S_UserPasswordUpdate); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 68; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_1 = PyObject_GetAttr(__pyx_t_2, __pyx_v_fa); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 68; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_XGOTREF(__pyx_v_3ctp_10_TraderApi_ApiStruct_UserPasswordUpdate);
  __Pyx_DECREF_SET(__pyx_v_3ctp_10_TraderApi_ApiStruct_UserPasswordUpdate, __pyx_t_1);
  __Pyx_GIVEREF(__pyx_t_1);
  __pyx_t_1 = 0;
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_AddTraceback("ctp._TraderApi._init", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = 0;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_fa);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static void __pyx_f_3ctp_10_TraderApi_TraderApi_Release(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("TraderApi_Release", 0);
  ReleaseTraderApi(__pyx_v_self->api, __pyx_v_self->spi);
  __pyx_v_self->api = NULL;
  __pyx_v_self->spi = NULL;
  __Pyx_RefNannyFinishContext();
}
static void __pyx_pw_3ctp_10_TraderApi_9TraderApi_1__dealloc__(PyObject *__pyx_v_self); 
static void __pyx_pw_3ctp_10_TraderApi_9TraderApi_1__dealloc__(PyObject *__pyx_v_self) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__dealloc__ (wrapper)", 0);
  __pyx_pf_3ctp_10_TraderApi_9TraderApi___dealloc__(((struct __pyx_obj_3ctp_10_TraderApi_TraderApi *)__pyx_v_self));
  __Pyx_RefNannyFinishContext();
}
static void __pyx_pf_3ctp_10_TraderApi_9TraderApi___dealloc__(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__dealloc__", 0);
  __pyx_f_3ctp_10_TraderApi_TraderApi_Release(__pyx_v_self);
  __Pyx_RefNannyFinishContext();
}
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_3Alive(PyObject *__pyx_v_self, CYTHON_UNUSED PyObject *unused); 
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_3Alive(PyObject *__pyx_v_self, CYTHON_UNUSED PyObject *unused) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("Alive (wrapper)", 0);
  __pyx_r = __pyx_pf_3ctp_10_TraderApi_9TraderApi_2Alive(((struct __pyx_obj_3ctp_10_TraderApi_TraderApi *)__pyx_v_self));
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_2Alive(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self) {
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_t_1;
  PyObject *__pyx_t_2 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("Alive", 0);
  __pyx_t_1 = ((__pyx_v_self->spi != NULL) != 0);
  if (__pyx_t_1) {
    __Pyx_XDECREF(__pyx_r);
    __pyx_t_2 = __Pyx_PyInt_From_long(__pyx_v_self->spi->tid); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 85; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_r = __pyx_t_2;
    __pyx_t_2 = 0;
    goto __pyx_L0;
  }
  __pyx_t_1 = ((__pyx_v_self->api != NULL) != 0);
  if (__pyx_t_1) {
    __Pyx_XDECREF(__pyx_r);
    __Pyx_INCREF(Py_False);
    __pyx_r = Py_False;
    goto __pyx_L0;
  }
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.Alive", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_5Create(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds); 
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_5Create(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  const char *__pyx_v_pszFlowPath;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("Create (wrapper)", 0);
  {
    static PyObject **__pyx_pyargnames[] = {&__pyx_n_s_pszFlowPath,0};
    PyObject* values[1] = {0};
    if (unlikely(__pyx_kwds)) {
      Py_ssize_t kw_args;
      const Py_ssize_t pos_args = PyTuple_GET_SIZE(__pyx_args);
      switch (pos_args) {
        case 1: values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
        case 0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      kw_args = PyDict_Size(__pyx_kwds);
      switch (pos_args) {
        case 0:
        if (kw_args > 0) {
          PyObject* value = PyDict_GetItem(__pyx_kwds, __pyx_n_s_pszFlowPath);
          if (value) { values[0] = value; kw_args--; }
        }
      }
      if (unlikely(kw_args > 0)) {
        if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_pyargnames, 0, values, pos_args, "Create") < 0)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 88; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
      }
    } else {
      switch (PyTuple_GET_SIZE(__pyx_args)) {
        case 1: values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
        case 0: break;
        default: goto __pyx_L5_argtuple_error;
      }
    }
    if (values[0]) {
      __pyx_v_pszFlowPath = __Pyx_PyObject_AsString(values[0]); if (unlikely((!__pyx_v_pszFlowPath) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 88; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
    } else {
      __pyx_v_pszFlowPath = ((const char *)__pyx_k_);
    }
  }
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("Create", 0, 0, 1, PyTuple_GET_SIZE(__pyx_args)); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 88; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  __pyx_L3_error:;
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.Create", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_3ctp_10_TraderApi_9TraderApi_4Create(((struct __pyx_obj_3ctp_10_TraderApi_TraderApi *)__pyx_v_self), __pyx_v_pszFlowPath);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_4Create(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, const char *__pyx_v_pszFlowPath) {
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_t_1;
  CThostFtdcTraderApi *__pyx_t_2;
  int __pyx_t_3;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("Create", 0);
  __pyx_t_1 = ((__pyx_v_self->api != NULL) != 0);
  if (__pyx_t_1) {
    __Pyx_XDECREF(__pyx_r);
    __pyx_r = Py_None; __Pyx_INCREF(Py_None);
    goto __pyx_L0;
  }
  try {
    __pyx_t_2 = CThostFtdcTraderApi::CreateFtdcTraderApi(__pyx_v_pszFlowPath);
  } catch(...) {
    __Pyx_CppExn2PyErr();
    {__pyx_filename = __pyx_f[0]; __pyx_lineno = 90; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  }
  __pyx_v_self->api = __pyx_t_2;
  __pyx_t_3 = CheckMemory(__pyx_v_self->api); if (unlikely(__pyx_t_3 == 0)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 91; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.Create", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_7Release(PyObject *__pyx_v_self, CYTHON_UNUSED PyObject *unused); 
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_7Release(PyObject *__pyx_v_self, CYTHON_UNUSED PyObject *unused) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("Release (wrapper)", 0);
  __pyx_r = __pyx_pf_3ctp_10_TraderApi_9TraderApi_6Release(((struct __pyx_obj_3ctp_10_TraderApi_TraderApi *)__pyx_v_self));
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_6Release(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self) {
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("Release", 0);
  __pyx_f_3ctp_10_TraderApi_TraderApi_Release(__pyx_v_self);
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_9Init(PyObject *__pyx_v_self, CYTHON_UNUSED PyObject *unused); 
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_9Init(PyObject *__pyx_v_self, CYTHON_UNUSED PyObject *unused) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("Init (wrapper)", 0);
  __pyx_r = __pyx_pf_3ctp_10_TraderApi_9TraderApi_8Init(((struct __pyx_obj_3ctp_10_TraderApi_TraderApi *)__pyx_v_self));
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_8Init(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self) {
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_t_1;
  int __pyx_t_2;
  int __pyx_t_3;
  int __pyx_t_4;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("Init", 0);
  __pyx_t_1 = ((__pyx_v_self->api == NULL) != 0);
  if (!__pyx_t_1) {
    __pyx_t_2 = ((__pyx_v_self->spi != NULL) != 0);
    __pyx_t_3 = __pyx_t_2;
  } else {
    __pyx_t_3 = __pyx_t_1;
  }
  if (__pyx_t_3) {
    __Pyx_XDECREF(__pyx_r);
    __pyx_r = Py_None; __Pyx_INCREF(Py_None);
    goto __pyx_L0;
  }
  __pyx_v_self->spi = new CTraderSpi(((PyObject *)__pyx_v_self));
  __pyx_t_4 = CheckMemory(__pyx_v_self->spi); if (unlikely(__pyx_t_4 == 0)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 99; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __pyx_v_self->api->RegisterSpi(__pyx_v_self->spi);
  __pyx_v_self->api->Init();
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.Init", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_11Join(PyObject *__pyx_v_self, CYTHON_UNUSED PyObject *unused); 
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_11Join(PyObject *__pyx_v_self, CYTHON_UNUSED PyObject *unused) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("Join (wrapper)", 0);
  __pyx_r = __pyx_pf_3ctp_10_TraderApi_9TraderApi_10Join(((struct __pyx_obj_3ctp_10_TraderApi_TraderApi *)__pyx_v_self));
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_10Join(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self) {
  int __pyx_v_ret;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_t_1;
  PyObject *__pyx_t_2 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("Join", 0);
  __pyx_t_1 = ((__pyx_v_self->spi == NULL) != 0);
  if (__pyx_t_1) {
    __Pyx_XDECREF(__pyx_r);
    __pyx_r = Py_None; __Pyx_INCREF(Py_None);
    goto __pyx_L0;
  }
  {
      #ifdef WITH_THREAD
      PyThreadState *_save;
      Py_UNBLOCK_THREADS
      #endif
      {
        __pyx_v_ret = __pyx_v_self->api->Join();
      }
      {
        {
          #ifdef WITH_THREAD
          Py_BLOCK_THREADS
          #endif
          goto __pyx_L6;
        }
        __pyx_L6:;
      }
  }
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_2 = __Pyx_PyInt_From_int(__pyx_v_ret); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 107; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_r = __pyx_t_2;
  __pyx_t_2 = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.Join", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_13GetTradingDay(PyObject *__pyx_v_self, CYTHON_UNUSED PyObject *unused); 
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_13GetTradingDay(PyObject *__pyx_v_self, CYTHON_UNUSED PyObject *unused) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("GetTradingDay (wrapper)", 0);
  __pyx_r = __pyx_pf_3ctp_10_TraderApi_9TraderApi_12GetTradingDay(((struct __pyx_obj_3ctp_10_TraderApi_TraderApi *)__pyx_v_self));
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_12GetTradingDay(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self) {
  const char *__pyx_v_ret;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_t_1;
  PyObject *__pyx_t_2 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("GetTradingDay", 0);
  __pyx_t_1 = ((__pyx_v_self->spi == NULL) != 0);
  if (__pyx_t_1) {
    __Pyx_XDECREF(__pyx_r);
    __pyx_r = Py_None; __Pyx_INCREF(Py_None);
    goto __pyx_L0;
  }
  {
      #ifdef WITH_THREAD
      PyThreadState *_save;
      Py_UNBLOCK_THREADS
      #endif
      {
        __pyx_v_ret = __pyx_v_self->api->GetTradingDay();
      }
      {
        {
          #ifdef WITH_THREAD
          Py_BLOCK_THREADS
          #endif
          goto __pyx_L6;
        }
        __pyx_L6:;
      }
  }
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_2 = __Pyx_PyBytes_FromString(__pyx_v_ret); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 113; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_r = __pyx_t_2;
  __pyx_t_2 = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.GetTradingDay", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_15RegisterFront(PyObject *__pyx_v_self, PyObject *__pyx_arg_pszFrontAddress); 
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_15RegisterFront(PyObject *__pyx_v_self, PyObject *__pyx_arg_pszFrontAddress) {
  char *__pyx_v_pszFrontAddress;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("RegisterFront (wrapper)", 0);
  assert(__pyx_arg_pszFrontAddress); {
    __pyx_v_pszFrontAddress = __Pyx_PyObject_AsString(__pyx_arg_pszFrontAddress); if (unlikely((!__pyx_v_pszFrontAddress) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 115; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  }
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.RegisterFront", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_3ctp_10_TraderApi_9TraderApi_14RegisterFront(((struct __pyx_obj_3ctp_10_TraderApi_TraderApi *)__pyx_v_self), ((char *)__pyx_v_pszFrontAddress));
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_14RegisterFront(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, char *__pyx_v_pszFrontAddress) {
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_t_1;
  __Pyx_RefNannySetupContext("RegisterFront", 0);
  __pyx_t_1 = ((__pyx_v_self->api == NULL) != 0);
  if (__pyx_t_1) {
    __Pyx_XDECREF(__pyx_r);
    __pyx_r = Py_None; __Pyx_INCREF(Py_None);
    goto __pyx_L0;
  }
  __pyx_v_self->api->RegisterFront(__pyx_v_pszFrontAddress);
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_17RegisterNameServer(PyObject *__pyx_v_self, PyObject *__pyx_arg_pszNsAddress); 
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_17RegisterNameServer(PyObject *__pyx_v_self, PyObject *__pyx_arg_pszNsAddress) {
  char *__pyx_v_pszNsAddress;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("RegisterNameServer (wrapper)", 0);
  assert(__pyx_arg_pszNsAddress); {
    __pyx_v_pszNsAddress = __Pyx_PyObject_AsString(__pyx_arg_pszNsAddress); if (unlikely((!__pyx_v_pszNsAddress) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 119; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  }
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.RegisterNameServer", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_3ctp_10_TraderApi_9TraderApi_16RegisterNameServer(((struct __pyx_obj_3ctp_10_TraderApi_TraderApi *)__pyx_v_self), ((char *)__pyx_v_pszNsAddress));
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_16RegisterNameServer(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, char *__pyx_v_pszNsAddress) {
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_t_1;
  __Pyx_RefNannySetupContext("RegisterNameServer", 0);
  __pyx_t_1 = ((__pyx_v_self->api == NULL) != 0);
  if (__pyx_t_1) {
    __Pyx_XDECREF(__pyx_r);
    __pyx_r = Py_None; __Pyx_INCREF(Py_None);
    goto __pyx_L0;
  }
  __pyx_v_self->api->RegisterNameServer(__pyx_v_pszNsAddress);
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_19RegisterFensUserInfo(PyObject *__pyx_v_self, PyObject *__pyx_v_pFensUserInfo); 
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_19RegisterFensUserInfo(PyObject *__pyx_v_self, PyObject *__pyx_v_pFensUserInfo) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("RegisterFensUserInfo (wrapper)", 0);
  __pyx_r = __pyx_pf_3ctp_10_TraderApi_9TraderApi_18RegisterFensUserInfo(((struct __pyx_obj_3ctp_10_TraderApi_TraderApi *)__pyx_v_self), ((PyObject *)__pyx_v_pFensUserInfo));
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_18RegisterFensUserInfo(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pFensUserInfo) {
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_t_1;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  size_t __pyx_t_4;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("RegisterFensUserInfo", 0);
  __pyx_t_1 = ((__pyx_v_self->api == NULL) != 0);
  if (__pyx_t_1) {
    __Pyx_XDECREF(__pyx_r);
    __pyx_r = Py_None; __Pyx_INCREF(Py_None);
    goto __pyx_L0;
  }
  __pyx_t_2 = PyTuple_New(1); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 125; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_v_pFensUserInfo);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_v_pFensUserInfo);
  __Pyx_GIVEREF(__pyx_v_pFensUserInfo);
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_addressof, __pyx_t_2, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 125; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_4 = __Pyx_PyInt_As_size_t(__pyx_t_3); if (unlikely((__pyx_t_4 == (size_t)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 125; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_v_self->api->RegisterFensUserInfo(((struct CThostFtdcFensUserInfoField *)((size_t)__pyx_t_4)));
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.RegisterFensUserInfo", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_21SubscribePrivateTopic(PyObject *__pyx_v_self, PyObject *__pyx_arg_nResumeType); 
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_21SubscribePrivateTopic(PyObject *__pyx_v_self, PyObject *__pyx_arg_nResumeType) {
  enum THOST_TE_RESUME_TYPE __pyx_v_nResumeType;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("SubscribePrivateTopic (wrapper)", 0);
  assert(__pyx_arg_nResumeType); {
    __pyx_v_nResumeType = ((enum THOST_TE_RESUME_TYPE)PyInt_AsLong(__pyx_arg_nResumeType)); if (unlikely(PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 127; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  }
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.SubscribePrivateTopic", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_3ctp_10_TraderApi_9TraderApi_20SubscribePrivateTopic(((struct __pyx_obj_3ctp_10_TraderApi_TraderApi *)__pyx_v_self), ((enum THOST_TE_RESUME_TYPE)__pyx_v_nResumeType));
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_20SubscribePrivateTopic(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, enum THOST_TE_RESUME_TYPE __pyx_v_nResumeType) {
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_t_1;
  __Pyx_RefNannySetupContext("SubscribePrivateTopic", 0);
  __pyx_t_1 = ((__pyx_v_self->api == NULL) != 0);
  if (__pyx_t_1) {
    __Pyx_XDECREF(__pyx_r);
    __pyx_r = Py_None; __Pyx_INCREF(Py_None);
    goto __pyx_L0;
  }
  __pyx_v_self->api->SubscribePrivateTopic(__pyx_v_nResumeType);
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_23SubscribePublicTopic(PyObject *__pyx_v_self, PyObject *__pyx_arg_nResumeType); 
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_23SubscribePublicTopic(PyObject *__pyx_v_self, PyObject *__pyx_arg_nResumeType) {
  enum THOST_TE_RESUME_TYPE __pyx_v_nResumeType;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("SubscribePublicTopic (wrapper)", 0);
  assert(__pyx_arg_nResumeType); {
    __pyx_v_nResumeType = ((enum THOST_TE_RESUME_TYPE)PyInt_AsLong(__pyx_arg_nResumeType)); if (unlikely(PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 131; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  }
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L3_error:;
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.SubscribePublicTopic", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_3ctp_10_TraderApi_9TraderApi_22SubscribePublicTopic(((struct __pyx_obj_3ctp_10_TraderApi_TraderApi *)__pyx_v_self), ((enum THOST_TE_RESUME_TYPE)__pyx_v_nResumeType));
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_22SubscribePublicTopic(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, enum THOST_TE_RESUME_TYPE __pyx_v_nResumeType) {
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_t_1;
  __Pyx_RefNannySetupContext("SubscribePublicTopic", 0);
  __pyx_t_1 = ((__pyx_v_self->api == NULL) != 0);
  if (__pyx_t_1) {
    __Pyx_XDECREF(__pyx_r);
    __pyx_r = Py_None; __Pyx_INCREF(Py_None);
    goto __pyx_L0;
  }
  __pyx_v_self->api->SubscribePublicTopic(__pyx_v_nResumeType);
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_25ReqAuthenticate(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds); 
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_25ReqAuthenticate(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_pReqAuthenticate = 0;
  int __pyx_v_nRequestID;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("ReqAuthenticate (wrapper)", 0);
  {
    static PyObject **__pyx_pyargnames[] = {&__pyx_n_s_pReqAuthenticate,&__pyx_n_s_nRequestID,0};
    PyObject* values[2] = {0,0};
    if (unlikely(__pyx_kwds)) {
      Py_ssize_t kw_args;
      const Py_ssize_t pos_args = PyTuple_GET_SIZE(__pyx_args);
      switch (pos_args) {
        case 2: values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
        case 1: values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
        case 0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      kw_args = PyDict_Size(__pyx_kwds);
      switch (pos_args) {
        case 0:
        if (likely((values[0] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_pReqAuthenticate)) != 0)) kw_args--;
        else goto __pyx_L5_argtuple_error;
        case 1:
        if (likely((values[1] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_nRequestID)) != 0)) kw_args--;
        else {
          __Pyx_RaiseArgtupleInvalid("ReqAuthenticate", 1, 2, 2, 1); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 135; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
        }
      }
      if (unlikely(kw_args > 0)) {
        if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_pyargnames, 0, values, pos_args, "ReqAuthenticate") < 0)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 135; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
      }
    } else if (PyTuple_GET_SIZE(__pyx_args) != 2) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
      values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
    }
    __pyx_v_pReqAuthenticate = values[0];
    __pyx_v_nRequestID = __Pyx_PyInt_As_int(values[1]); if (unlikely((__pyx_v_nRequestID == (int)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 135; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  }
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("ReqAuthenticate", 1, 2, 2, PyTuple_GET_SIZE(__pyx_args)); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 135; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  __pyx_L3_error:;
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqAuthenticate", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_3ctp_10_TraderApi_9TraderApi_24ReqAuthenticate(((struct __pyx_obj_3ctp_10_TraderApi_TraderApi *)__pyx_v_self), __pyx_v_pReqAuthenticate, __pyx_v_nRequestID);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_24ReqAuthenticate(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pReqAuthenticate, int __pyx_v_nRequestID) {
  size_t __pyx_v_address;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_t_1;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  size_t __pyx_t_4;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("ReqAuthenticate", 0);
  __pyx_t_1 = ((__pyx_v_self->spi == NULL) != 0);
  if (__pyx_t_1) {
    __Pyx_XDECREF(__pyx_r);
    __pyx_r = Py_None; __Pyx_INCREF(Py_None);
    goto __pyx_L0;
  }
  __pyx_t_2 = PyTuple_New(1); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 138; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_v_pReqAuthenticate);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_v_pReqAuthenticate);
  __Pyx_GIVEREF(__pyx_v_pReqAuthenticate);
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_addressof, __pyx_t_2, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 138; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_4 = __Pyx_PyInt_As_size_t(__pyx_t_3); if (unlikely((__pyx_t_4 == (size_t)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 138; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_v_address = __pyx_t_4;
  {
      #ifdef WITH_THREAD
      PyThreadState *_save;
      Py_UNBLOCK_THREADS
      #endif
      {
        __pyx_v_nRequestID = __pyx_v_self->api->ReqAuthenticate(((struct CThostFtdcReqAuthenticateField *)__pyx_v_address), __pyx_v_nRequestID);
      }
      {
        {
          #ifdef WITH_THREAD
          Py_BLOCK_THREADS
          #endif
          goto __pyx_L6;
        }
        __pyx_L6:;
      }
  }
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_3 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 140; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_r = __pyx_t_3;
  __pyx_t_3 = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqAuthenticate", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_27ReqUserLogin(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds); 
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_27ReqUserLogin(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_pReqUserLogin = 0;
  int __pyx_v_nRequestID;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("ReqUserLogin (wrapper)", 0);
  {
    static PyObject **__pyx_pyargnames[] = {&__pyx_n_s_pReqUserLogin,&__pyx_n_s_nRequestID,0};
    PyObject* values[2] = {0,0};
    if (unlikely(__pyx_kwds)) {
      Py_ssize_t kw_args;
      const Py_ssize_t pos_args = PyTuple_GET_SIZE(__pyx_args);
      switch (pos_args) {
        case 2: values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
        case 1: values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
        case 0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      kw_args = PyDict_Size(__pyx_kwds);
      switch (pos_args) {
        case 0:
        if (likely((values[0] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_pReqUserLogin)) != 0)) kw_args--;
        else goto __pyx_L5_argtuple_error;
        case 1:
        if (likely((values[1] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_nRequestID)) != 0)) kw_args--;
        else {
          __Pyx_RaiseArgtupleInvalid("ReqUserLogin", 1, 2, 2, 1); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 142; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
        }
      }
      if (unlikely(kw_args > 0)) {
        if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_pyargnames, 0, values, pos_args, "ReqUserLogin") < 0)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 142; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
      }
    } else if (PyTuple_GET_SIZE(__pyx_args) != 2) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
      values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
    }
    __pyx_v_pReqUserLogin = values[0];
    __pyx_v_nRequestID = __Pyx_PyInt_As_int(values[1]); if (unlikely((__pyx_v_nRequestID == (int)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 142; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  }
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("ReqUserLogin", 1, 2, 2, PyTuple_GET_SIZE(__pyx_args)); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 142; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  __pyx_L3_error:;
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqUserLogin", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_3ctp_10_TraderApi_9TraderApi_26ReqUserLogin(((struct __pyx_obj_3ctp_10_TraderApi_TraderApi *)__pyx_v_self), __pyx_v_pReqUserLogin, __pyx_v_nRequestID);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_26ReqUserLogin(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pReqUserLogin, int __pyx_v_nRequestID) {
  size_t __pyx_v_address;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_t_1;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  size_t __pyx_t_4;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("ReqUserLogin", 0);
  __pyx_t_1 = ((__pyx_v_self->spi == NULL) != 0);
  if (__pyx_t_1) {
    __Pyx_XDECREF(__pyx_r);
    __pyx_r = Py_None; __Pyx_INCREF(Py_None);
    goto __pyx_L0;
  }
  __pyx_t_2 = PyTuple_New(1); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 145; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_v_pReqUserLogin);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_v_pReqUserLogin);
  __Pyx_GIVEREF(__pyx_v_pReqUserLogin);
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_addressof, __pyx_t_2, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 145; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_4 = __Pyx_PyInt_As_size_t(__pyx_t_3); if (unlikely((__pyx_t_4 == (size_t)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 145; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_v_address = __pyx_t_4;
  {
      #ifdef WITH_THREAD
      PyThreadState *_save;
      Py_UNBLOCK_THREADS
      #endif
      {
        __pyx_v_nRequestID = __pyx_v_self->api->ReqUserLogin(((struct CThostFtdcReqUserLoginField *)__pyx_v_address), __pyx_v_nRequestID);
      }
      {
        {
          #ifdef WITH_THREAD
          Py_BLOCK_THREADS
          #endif
          goto __pyx_L6;
        }
        __pyx_L6:;
      }
  }
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_3 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 147; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_r = __pyx_t_3;
  __pyx_t_3 = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqUserLogin", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_29ReqUserLogout(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds); 
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_29ReqUserLogout(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_pUserLogout = 0;
  int __pyx_v_nRequestID;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("ReqUserLogout (wrapper)", 0);
  {
    static PyObject **__pyx_pyargnames[] = {&__pyx_n_s_pUserLogout,&__pyx_n_s_nRequestID,0};
    PyObject* values[2] = {0,0};
    if (unlikely(__pyx_kwds)) {
      Py_ssize_t kw_args;
      const Py_ssize_t pos_args = PyTuple_GET_SIZE(__pyx_args);
      switch (pos_args) {
        case 2: values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
        case 1: values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
        case 0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      kw_args = PyDict_Size(__pyx_kwds);
      switch (pos_args) {
        case 0:
        if (likely((values[0] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_pUserLogout)) != 0)) kw_args--;
        else goto __pyx_L5_argtuple_error;
        case 1:
        if (likely((values[1] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_nRequestID)) != 0)) kw_args--;
        else {
          __Pyx_RaiseArgtupleInvalid("ReqUserLogout", 1, 2, 2, 1); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 149; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
        }
      }
      if (unlikely(kw_args > 0)) {
        if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_pyargnames, 0, values, pos_args, "ReqUserLogout") < 0)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 149; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
      }
    } else if (PyTuple_GET_SIZE(__pyx_args) != 2) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
      values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
    }
    __pyx_v_pUserLogout = values[0];
    __pyx_v_nRequestID = __Pyx_PyInt_As_int(values[1]); if (unlikely((__pyx_v_nRequestID == (int)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 149; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  }
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("ReqUserLogout", 1, 2, 2, PyTuple_GET_SIZE(__pyx_args)); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 149; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  __pyx_L3_error:;
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqUserLogout", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_3ctp_10_TraderApi_9TraderApi_28ReqUserLogout(((struct __pyx_obj_3ctp_10_TraderApi_TraderApi *)__pyx_v_self), __pyx_v_pUserLogout, __pyx_v_nRequestID);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_28ReqUserLogout(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pUserLogout, int __pyx_v_nRequestID) {
  size_t __pyx_v_address;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_t_1;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  size_t __pyx_t_4;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("ReqUserLogout", 0);
  __pyx_t_1 = ((__pyx_v_self->spi == NULL) != 0);
  if (__pyx_t_1) {
    __Pyx_XDECREF(__pyx_r);
    __pyx_r = Py_None; __Pyx_INCREF(Py_None);
    goto __pyx_L0;
  }
  __pyx_t_2 = PyTuple_New(1); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 152; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_v_pUserLogout);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_v_pUserLogout);
  __Pyx_GIVEREF(__pyx_v_pUserLogout);
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_addressof, __pyx_t_2, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 152; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_4 = __Pyx_PyInt_As_size_t(__pyx_t_3); if (unlikely((__pyx_t_4 == (size_t)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 152; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_v_address = __pyx_t_4;
  {
      #ifdef WITH_THREAD
      PyThreadState *_save;
      Py_UNBLOCK_THREADS
      #endif
      {
        __pyx_v_nRequestID = __pyx_v_self->api->ReqUserLogout(((struct CThostFtdcUserLogoutField *)__pyx_v_address), __pyx_v_nRequestID);
      }
      {
        {
          #ifdef WITH_THREAD
          Py_BLOCK_THREADS
          #endif
          goto __pyx_L6;
        }
        __pyx_L6:;
      }
  }
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_3 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 154; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_r = __pyx_t_3;
  __pyx_t_3 = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqUserLogout", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_31ReqUserPasswordUpdate(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds); 
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_31ReqUserPasswordUpdate(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_pUserPasswordUpdate = 0;
  int __pyx_v_nRequestID;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("ReqUserPasswordUpdate (wrapper)", 0);
  {
    static PyObject **__pyx_pyargnames[] = {&__pyx_n_s_pUserPasswordUpdate,&__pyx_n_s_nRequestID,0};
    PyObject* values[2] = {0,0};
    if (unlikely(__pyx_kwds)) {
      Py_ssize_t kw_args;
      const Py_ssize_t pos_args = PyTuple_GET_SIZE(__pyx_args);
      switch (pos_args) {
        case 2: values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
        case 1: values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
        case 0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      kw_args = PyDict_Size(__pyx_kwds);
      switch (pos_args) {
        case 0:
        if (likely((values[0] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_pUserPasswordUpdate)) != 0)) kw_args--;
        else goto __pyx_L5_argtuple_error;
        case 1:
        if (likely((values[1] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_nRequestID)) != 0)) kw_args--;
        else {
          __Pyx_RaiseArgtupleInvalid("ReqUserPasswordUpdate", 1, 2, 2, 1); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 156; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
        }
      }
      if (unlikely(kw_args > 0)) {
        if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_pyargnames, 0, values, pos_args, "ReqUserPasswordUpdate") < 0)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 156; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
      }
    } else if (PyTuple_GET_SIZE(__pyx_args) != 2) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
      values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
    }
    __pyx_v_pUserPasswordUpdate = values[0];
    __pyx_v_nRequestID = __Pyx_PyInt_As_int(values[1]); if (unlikely((__pyx_v_nRequestID == (int)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 156; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  }
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("ReqUserPasswordUpdate", 1, 2, 2, PyTuple_GET_SIZE(__pyx_args)); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 156; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  __pyx_L3_error:;
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqUserPasswordUpdate", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_3ctp_10_TraderApi_9TraderApi_30ReqUserPasswordUpdate(((struct __pyx_obj_3ctp_10_TraderApi_TraderApi *)__pyx_v_self), __pyx_v_pUserPasswordUpdate, __pyx_v_nRequestID);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_30ReqUserPasswordUpdate(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pUserPasswordUpdate, int __pyx_v_nRequestID) {
  size_t __pyx_v_address;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_t_1;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  size_t __pyx_t_4;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("ReqUserPasswordUpdate", 0);
  __pyx_t_1 = ((__pyx_v_self->spi == NULL) != 0);
  if (__pyx_t_1) {
    __Pyx_XDECREF(__pyx_r);
    __pyx_r = Py_None; __Pyx_INCREF(Py_None);
    goto __pyx_L0;
  }
  __pyx_t_2 = PyTuple_New(1); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 159; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_v_pUserPasswordUpdate);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_v_pUserPasswordUpdate);
  __Pyx_GIVEREF(__pyx_v_pUserPasswordUpdate);
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_addressof, __pyx_t_2, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 159; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_4 = __Pyx_PyInt_As_size_t(__pyx_t_3); if (unlikely((__pyx_t_4 == (size_t)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 159; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_v_address = __pyx_t_4;
  {
      #ifdef WITH_THREAD
      PyThreadState *_save;
      Py_UNBLOCK_THREADS
      #endif
      {
        __pyx_v_nRequestID = __pyx_v_self->api->ReqUserPasswordUpdate(((struct CThostFtdcUserPasswordUpdateField *)__pyx_v_address), __pyx_v_nRequestID);
      }
      {
        {
          #ifdef WITH_THREAD
          Py_BLOCK_THREADS
          #endif
          goto __pyx_L6;
        }
        __pyx_L6:;
      }
  }
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_3 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 161; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_r = __pyx_t_3;
  __pyx_t_3 = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqUserPasswordUpdate", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_33ReqTradingAccountPasswordUpdate(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds); 
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_33ReqTradingAccountPasswordUpdate(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_pTradingAccountPasswordUpdate = 0;
  int __pyx_v_nRequestID;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("ReqTradingAccountPasswordUpdate (wrapper)", 0);
  {
    static PyObject **__pyx_pyargnames[] = {&__pyx_n_s_pTradingAccountPasswordUpdate,&__pyx_n_s_nRequestID,0};
    PyObject* values[2] = {0,0};
    if (unlikely(__pyx_kwds)) {
      Py_ssize_t kw_args;
      const Py_ssize_t pos_args = PyTuple_GET_SIZE(__pyx_args);
      switch (pos_args) {
        case 2: values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
        case 1: values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
        case 0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      kw_args = PyDict_Size(__pyx_kwds);
      switch (pos_args) {
        case 0:
        if (likely((values[0] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_pTradingAccountPasswordUpdate)) != 0)) kw_args--;
        else goto __pyx_L5_argtuple_error;
        case 1:
        if (likely((values[1] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_nRequestID)) != 0)) kw_args--;
        else {
          __Pyx_RaiseArgtupleInvalid("ReqTradingAccountPasswordUpdate", 1, 2, 2, 1); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 163; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
        }
      }
      if (unlikely(kw_args > 0)) {
        if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_pyargnames, 0, values, pos_args, "ReqTradingAccountPasswordUpdate") < 0)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 163; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
      }
    } else if (PyTuple_GET_SIZE(__pyx_args) != 2) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
      values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
    }
    __pyx_v_pTradingAccountPasswordUpdate = values[0];
    __pyx_v_nRequestID = __Pyx_PyInt_As_int(values[1]); if (unlikely((__pyx_v_nRequestID == (int)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 163; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  }
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("ReqTradingAccountPasswordUpdate", 1, 2, 2, PyTuple_GET_SIZE(__pyx_args)); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 163; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  __pyx_L3_error:;
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqTradingAccountPasswordUpdate", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_3ctp_10_TraderApi_9TraderApi_32ReqTradingAccountPasswordUpdate(((struct __pyx_obj_3ctp_10_TraderApi_TraderApi *)__pyx_v_self), __pyx_v_pTradingAccountPasswordUpdate, __pyx_v_nRequestID);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_32ReqTradingAccountPasswordUpdate(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pTradingAccountPasswordUpdate, int __pyx_v_nRequestID) {
  size_t __pyx_v_address;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_t_1;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  size_t __pyx_t_4;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("ReqTradingAccountPasswordUpdate", 0);
  __pyx_t_1 = ((__pyx_v_self->spi == NULL) != 0);
  if (__pyx_t_1) {
    __Pyx_XDECREF(__pyx_r);
    __pyx_r = Py_None; __Pyx_INCREF(Py_None);
    goto __pyx_L0;
  }
  __pyx_t_2 = PyTuple_New(1); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 166; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_v_pTradingAccountPasswordUpdate);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_v_pTradingAccountPasswordUpdate);
  __Pyx_GIVEREF(__pyx_v_pTradingAccountPasswordUpdate);
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_addressof, __pyx_t_2, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 166; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_4 = __Pyx_PyInt_As_size_t(__pyx_t_3); if (unlikely((__pyx_t_4 == (size_t)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 166; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_v_address = __pyx_t_4;
  {
      #ifdef WITH_THREAD
      PyThreadState *_save;
      Py_UNBLOCK_THREADS
      #endif
      {
        __pyx_v_nRequestID = __pyx_v_self->api->ReqTradingAccountPasswordUpdate(((struct CThostFtdcTradingAccountPasswordUpdateField *)__pyx_v_address), __pyx_v_nRequestID);
      }
      {
        {
          #ifdef WITH_THREAD
          Py_BLOCK_THREADS
          #endif
          goto __pyx_L6;
        }
        __pyx_L6:;
      }
  }
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_3 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 168; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_r = __pyx_t_3;
  __pyx_t_3 = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqTradingAccountPasswordUpdate", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_35ReqOrderInsert(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds); 
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_35ReqOrderInsert(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_pInputOrder = 0;
  int __pyx_v_nRequestID;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("ReqOrderInsert (wrapper)", 0);
  {
    static PyObject **__pyx_pyargnames[] = {&__pyx_n_s_pInputOrder,&__pyx_n_s_nRequestID,0};
    PyObject* values[2] = {0,0};
    if (unlikely(__pyx_kwds)) {
      Py_ssize_t kw_args;
      const Py_ssize_t pos_args = PyTuple_GET_SIZE(__pyx_args);
      switch (pos_args) {
        case 2: values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
        case 1: values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
        case 0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      kw_args = PyDict_Size(__pyx_kwds);
      switch (pos_args) {
        case 0:
        if (likely((values[0] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_pInputOrder)) != 0)) kw_args--;
        else goto __pyx_L5_argtuple_error;
        case 1:
        if (likely((values[1] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_nRequestID)) != 0)) kw_args--;
        else {
          __Pyx_RaiseArgtupleInvalid("ReqOrderInsert", 1, 2, 2, 1); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 170; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
        }
      }
      if (unlikely(kw_args > 0)) {
        if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_pyargnames, 0, values, pos_args, "ReqOrderInsert") < 0)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 170; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
      }
    } else if (PyTuple_GET_SIZE(__pyx_args) != 2) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
      values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
    }
    __pyx_v_pInputOrder = values[0];
    __pyx_v_nRequestID = __Pyx_PyInt_As_int(values[1]); if (unlikely((__pyx_v_nRequestID == (int)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 170; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  }
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("ReqOrderInsert", 1, 2, 2, PyTuple_GET_SIZE(__pyx_args)); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 170; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  __pyx_L3_error:;
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqOrderInsert", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_3ctp_10_TraderApi_9TraderApi_34ReqOrderInsert(((struct __pyx_obj_3ctp_10_TraderApi_TraderApi *)__pyx_v_self), __pyx_v_pInputOrder, __pyx_v_nRequestID);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_34ReqOrderInsert(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pInputOrder, int __pyx_v_nRequestID) {
  size_t __pyx_v_address;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_t_1;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  size_t __pyx_t_4;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("ReqOrderInsert", 0);
  __pyx_t_1 = ((__pyx_v_self->spi == NULL) != 0);
  if (__pyx_t_1) {
    __Pyx_XDECREF(__pyx_r);
    __pyx_r = Py_None; __Pyx_INCREF(Py_None);
    goto __pyx_L0;
  }
  __pyx_t_2 = PyTuple_New(1); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 173; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_v_pInputOrder);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_v_pInputOrder);
  __Pyx_GIVEREF(__pyx_v_pInputOrder);
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_addressof, __pyx_t_2, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 173; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_4 = __Pyx_PyInt_As_size_t(__pyx_t_3); if (unlikely((__pyx_t_4 == (size_t)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 173; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_v_address = __pyx_t_4;
  {
      #ifdef WITH_THREAD
      PyThreadState *_save;
      Py_UNBLOCK_THREADS
      #endif
      {
        __pyx_v_nRequestID = __pyx_v_self->api->ReqOrderInsert(((struct CThostFtdcInputOrderField *)__pyx_v_address), __pyx_v_nRequestID);
      }
      {
        {
          #ifdef WITH_THREAD
          Py_BLOCK_THREADS
          #endif
          goto __pyx_L6;
        }
        __pyx_L6:;
      }
  }
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_3 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 175; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_r = __pyx_t_3;
  __pyx_t_3 = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqOrderInsert", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_37ReqParkedOrderInsert(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds); 
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_37ReqParkedOrderInsert(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_pParkedOrder = 0;
  int __pyx_v_nRequestID;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("ReqParkedOrderInsert (wrapper)", 0);
  {
    static PyObject **__pyx_pyargnames[] = {&__pyx_n_s_pParkedOrder,&__pyx_n_s_nRequestID,0};
    PyObject* values[2] = {0,0};
    if (unlikely(__pyx_kwds)) {
      Py_ssize_t kw_args;
      const Py_ssize_t pos_args = PyTuple_GET_SIZE(__pyx_args);
      switch (pos_args) {
        case 2: values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
        case 1: values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
        case 0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      kw_args = PyDict_Size(__pyx_kwds);
      switch (pos_args) {
        case 0:
        if (likely((values[0] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_pParkedOrder)) != 0)) kw_args--;
        else goto __pyx_L5_argtuple_error;
        case 1:
        if (likely((values[1] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_nRequestID)) != 0)) kw_args--;
        else {
          __Pyx_RaiseArgtupleInvalid("ReqParkedOrderInsert", 1, 2, 2, 1); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 177; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
        }
      }
      if (unlikely(kw_args > 0)) {
        if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_pyargnames, 0, values, pos_args, "ReqParkedOrderInsert") < 0)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 177; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
      }
    } else if (PyTuple_GET_SIZE(__pyx_args) != 2) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
      values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
    }
    __pyx_v_pParkedOrder = values[0];
    __pyx_v_nRequestID = __Pyx_PyInt_As_int(values[1]); if (unlikely((__pyx_v_nRequestID == (int)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 177; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  }
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("ReqParkedOrderInsert", 1, 2, 2, PyTuple_GET_SIZE(__pyx_args)); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 177; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  __pyx_L3_error:;
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqParkedOrderInsert", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_3ctp_10_TraderApi_9TraderApi_36ReqParkedOrderInsert(((struct __pyx_obj_3ctp_10_TraderApi_TraderApi *)__pyx_v_self), __pyx_v_pParkedOrder, __pyx_v_nRequestID);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_36ReqParkedOrderInsert(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pParkedOrder, int __pyx_v_nRequestID) {
  size_t __pyx_v_address;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_t_1;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  size_t __pyx_t_4;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("ReqParkedOrderInsert", 0);
  __pyx_t_1 = ((__pyx_v_self->spi == NULL) != 0);
  if (__pyx_t_1) {
    __Pyx_XDECREF(__pyx_r);
    __pyx_r = Py_None; __Pyx_INCREF(Py_None);
    goto __pyx_L0;
  }
  __pyx_t_2 = PyTuple_New(1); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 180; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_v_pParkedOrder);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_v_pParkedOrder);
  __Pyx_GIVEREF(__pyx_v_pParkedOrder);
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_addressof, __pyx_t_2, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 180; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_4 = __Pyx_PyInt_As_size_t(__pyx_t_3); if (unlikely((__pyx_t_4 == (size_t)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 180; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_v_address = __pyx_t_4;
  {
      #ifdef WITH_THREAD
      PyThreadState *_save;
      Py_UNBLOCK_THREADS
      #endif
      {
        __pyx_v_nRequestID = __pyx_v_self->api->ReqParkedOrderInsert(((struct CThostFtdcParkedOrderField *)__pyx_v_address), __pyx_v_nRequestID);
      }
      {
        {
          #ifdef WITH_THREAD
          Py_BLOCK_THREADS
          #endif
          goto __pyx_L6;
        }
        __pyx_L6:;
      }
  }
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_3 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 182; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_r = __pyx_t_3;
  __pyx_t_3 = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqParkedOrderInsert", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_39ReqParkedOrderAction(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds); 
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_39ReqParkedOrderAction(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_pParkedOrderAction = 0;
  int __pyx_v_nRequestID;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("ReqParkedOrderAction (wrapper)", 0);
  {
    static PyObject **__pyx_pyargnames[] = {&__pyx_n_s_pParkedOrderAction,&__pyx_n_s_nRequestID,0};
    PyObject* values[2] = {0,0};
    if (unlikely(__pyx_kwds)) {
      Py_ssize_t kw_args;
      const Py_ssize_t pos_args = PyTuple_GET_SIZE(__pyx_args);
      switch (pos_args) {
        case 2: values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
        case 1: values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
        case 0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      kw_args = PyDict_Size(__pyx_kwds);
      switch (pos_args) {
        case 0:
        if (likely((values[0] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_pParkedOrderAction)) != 0)) kw_args--;
        else goto __pyx_L5_argtuple_error;
        case 1:
        if (likely((values[1] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_nRequestID)) != 0)) kw_args--;
        else {
          __Pyx_RaiseArgtupleInvalid("ReqParkedOrderAction", 1, 2, 2, 1); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 184; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
        }
      }
      if (unlikely(kw_args > 0)) {
        if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_pyargnames, 0, values, pos_args, "ReqParkedOrderAction") < 0)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 184; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
      }
    } else if (PyTuple_GET_SIZE(__pyx_args) != 2) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
      values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
    }
    __pyx_v_pParkedOrderAction = values[0];
    __pyx_v_nRequestID = __Pyx_PyInt_As_int(values[1]); if (unlikely((__pyx_v_nRequestID == (int)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 184; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  }
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("ReqParkedOrderAction", 1, 2, 2, PyTuple_GET_SIZE(__pyx_args)); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 184; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  __pyx_L3_error:;
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqParkedOrderAction", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_3ctp_10_TraderApi_9TraderApi_38ReqParkedOrderAction(((struct __pyx_obj_3ctp_10_TraderApi_TraderApi *)__pyx_v_self), __pyx_v_pParkedOrderAction, __pyx_v_nRequestID);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_38ReqParkedOrderAction(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pParkedOrderAction, int __pyx_v_nRequestID) {
  size_t __pyx_v_address;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_t_1;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  size_t __pyx_t_4;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("ReqParkedOrderAction", 0);
  __pyx_t_1 = ((__pyx_v_self->spi == NULL) != 0);
  if (__pyx_t_1) {
    __Pyx_XDECREF(__pyx_r);
    __pyx_r = Py_None; __Pyx_INCREF(Py_None);
    goto __pyx_L0;
  }
  __pyx_t_2 = PyTuple_New(1); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 187; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_v_pParkedOrderAction);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_v_pParkedOrderAction);
  __Pyx_GIVEREF(__pyx_v_pParkedOrderAction);
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_addressof, __pyx_t_2, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 187; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_4 = __Pyx_PyInt_As_size_t(__pyx_t_3); if (unlikely((__pyx_t_4 == (size_t)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 187; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_v_address = __pyx_t_4;
  {
      #ifdef WITH_THREAD
      PyThreadState *_save;
      Py_UNBLOCK_THREADS
      #endif
      {
        __pyx_v_nRequestID = __pyx_v_self->api->ReqParkedOrderAction(((struct CThostFtdcParkedOrderActionField *)__pyx_v_address), __pyx_v_nRequestID);
      }
      {
        {
          #ifdef WITH_THREAD
          Py_BLOCK_THREADS
          #endif
          goto __pyx_L6;
        }
        __pyx_L6:;
      }
  }
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_3 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 189; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_r = __pyx_t_3;
  __pyx_t_3 = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqParkedOrderAction", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_41ReqOrderAction(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds); 
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_41ReqOrderAction(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_pInputOrderAction = 0;
  int __pyx_v_nRequestID;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("ReqOrderAction (wrapper)", 0);
  {
    static PyObject **__pyx_pyargnames[] = {&__pyx_n_s_pInputOrderAction,&__pyx_n_s_nRequestID,0};
    PyObject* values[2] = {0,0};
    if (unlikely(__pyx_kwds)) {
      Py_ssize_t kw_args;
      const Py_ssize_t pos_args = PyTuple_GET_SIZE(__pyx_args);
      switch (pos_args) {
        case 2: values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
        case 1: values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
        case 0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      kw_args = PyDict_Size(__pyx_kwds);
      switch (pos_args) {
        case 0:
        if (likely((values[0] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_pInputOrderAction)) != 0)) kw_args--;
        else goto __pyx_L5_argtuple_error;
        case 1:
        if (likely((values[1] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_nRequestID)) != 0)) kw_args--;
        else {
          __Pyx_RaiseArgtupleInvalid("ReqOrderAction", 1, 2, 2, 1); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 191; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
        }
      }
      if (unlikely(kw_args > 0)) {
        if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_pyargnames, 0, values, pos_args, "ReqOrderAction") < 0)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 191; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
      }
    } else if (PyTuple_GET_SIZE(__pyx_args) != 2) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
      values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
    }
    __pyx_v_pInputOrderAction = values[0];
    __pyx_v_nRequestID = __Pyx_PyInt_As_int(values[1]); if (unlikely((__pyx_v_nRequestID == (int)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 191; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  }
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("ReqOrderAction", 1, 2, 2, PyTuple_GET_SIZE(__pyx_args)); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 191; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  __pyx_L3_error:;
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqOrderAction", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_3ctp_10_TraderApi_9TraderApi_40ReqOrderAction(((struct __pyx_obj_3ctp_10_TraderApi_TraderApi *)__pyx_v_self), __pyx_v_pInputOrderAction, __pyx_v_nRequestID);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_40ReqOrderAction(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pInputOrderAction, int __pyx_v_nRequestID) {
  size_t __pyx_v_address;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_t_1;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  size_t __pyx_t_4;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("ReqOrderAction", 0);
  __pyx_t_1 = ((__pyx_v_self->spi == NULL) != 0);
  if (__pyx_t_1) {
    __Pyx_XDECREF(__pyx_r);
    __pyx_r = Py_None; __Pyx_INCREF(Py_None);
    goto __pyx_L0;
  }
  __pyx_t_2 = PyTuple_New(1); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 194; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_v_pInputOrderAction);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_v_pInputOrderAction);
  __Pyx_GIVEREF(__pyx_v_pInputOrderAction);
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_addressof, __pyx_t_2, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 194; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_4 = __Pyx_PyInt_As_size_t(__pyx_t_3); if (unlikely((__pyx_t_4 == (size_t)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 194; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_v_address = __pyx_t_4;
  {
      #ifdef WITH_THREAD
      PyThreadState *_save;
      Py_UNBLOCK_THREADS
      #endif
      {
        __pyx_v_nRequestID = __pyx_v_self->api->ReqOrderAction(((struct CThostFtdcInputOrderActionField *)__pyx_v_address), __pyx_v_nRequestID);
      }
      {
        {
          #ifdef WITH_THREAD
          Py_BLOCK_THREADS
          #endif
          goto __pyx_L6;
        }
        __pyx_L6:;
      }
  }
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_3 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 196; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_r = __pyx_t_3;
  __pyx_t_3 = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqOrderAction", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_43ReqQueryMaxOrderVolume(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds); 
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_43ReqQueryMaxOrderVolume(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_pQueryMaxOrderVolume = 0;
  int __pyx_v_nRequestID;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("ReqQueryMaxOrderVolume (wrapper)", 0);
  {
    static PyObject **__pyx_pyargnames[] = {&__pyx_n_s_pQueryMaxOrderVolume,&__pyx_n_s_nRequestID,0};
    PyObject* values[2] = {0,0};
    if (unlikely(__pyx_kwds)) {
      Py_ssize_t kw_args;
      const Py_ssize_t pos_args = PyTuple_GET_SIZE(__pyx_args);
      switch (pos_args) {
        case 2: values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
        case 1: values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
        case 0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      kw_args = PyDict_Size(__pyx_kwds);
      switch (pos_args) {
        case 0:
        if (likely((values[0] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_pQueryMaxOrderVolume)) != 0)) kw_args--;
        else goto __pyx_L5_argtuple_error;
        case 1:
        if (likely((values[1] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_nRequestID)) != 0)) kw_args--;
        else {
          __Pyx_RaiseArgtupleInvalid("ReqQueryMaxOrderVolume", 1, 2, 2, 1); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 198; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
        }
      }
      if (unlikely(kw_args > 0)) {
        if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_pyargnames, 0, values, pos_args, "ReqQueryMaxOrderVolume") < 0)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 198; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
      }
    } else if (PyTuple_GET_SIZE(__pyx_args) != 2) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
      values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
    }
    __pyx_v_pQueryMaxOrderVolume = values[0];
    __pyx_v_nRequestID = __Pyx_PyInt_As_int(values[1]); if (unlikely((__pyx_v_nRequestID == (int)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 198; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  }
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("ReqQueryMaxOrderVolume", 1, 2, 2, PyTuple_GET_SIZE(__pyx_args)); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 198; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  __pyx_L3_error:;
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQueryMaxOrderVolume", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_3ctp_10_TraderApi_9TraderApi_42ReqQueryMaxOrderVolume(((struct __pyx_obj_3ctp_10_TraderApi_TraderApi *)__pyx_v_self), __pyx_v_pQueryMaxOrderVolume, __pyx_v_nRequestID);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_42ReqQueryMaxOrderVolume(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQueryMaxOrderVolume, int __pyx_v_nRequestID) {
  size_t __pyx_v_address;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_t_1;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  size_t __pyx_t_4;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("ReqQueryMaxOrderVolume", 0);
  __pyx_t_1 = ((__pyx_v_self->spi == NULL) != 0);
  if (__pyx_t_1) {
    __Pyx_XDECREF(__pyx_r);
    __pyx_r = Py_None; __Pyx_INCREF(Py_None);
    goto __pyx_L0;
  }
  __pyx_t_2 = PyTuple_New(1); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 201; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_v_pQueryMaxOrderVolume);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_v_pQueryMaxOrderVolume);
  __Pyx_GIVEREF(__pyx_v_pQueryMaxOrderVolume);
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_addressof, __pyx_t_2, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 201; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_4 = __Pyx_PyInt_As_size_t(__pyx_t_3); if (unlikely((__pyx_t_4 == (size_t)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 201; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_v_address = __pyx_t_4;
  {
      #ifdef WITH_THREAD
      PyThreadState *_save;
      Py_UNBLOCK_THREADS
      #endif
      {
        __pyx_v_nRequestID = __pyx_v_self->api->ReqQueryMaxOrderVolume(((struct CThostFtdcQueryMaxOrderVolumeField *)__pyx_v_address), __pyx_v_nRequestID);
      }
      {
        {
          #ifdef WITH_THREAD
          Py_BLOCK_THREADS
          #endif
          goto __pyx_L6;
        }
        __pyx_L6:;
      }
  }
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_3 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 203; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_r = __pyx_t_3;
  __pyx_t_3 = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQueryMaxOrderVolume", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_45ReqSettlementInfoConfirm(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds); 
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_45ReqSettlementInfoConfirm(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_pSettlementInfoConfirm = 0;
  int __pyx_v_nRequestID;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("ReqSettlementInfoConfirm (wrapper)", 0);
  {
    static PyObject **__pyx_pyargnames[] = {&__pyx_n_s_pSettlementInfoConfirm,&__pyx_n_s_nRequestID,0};
    PyObject* values[2] = {0,0};
    if (unlikely(__pyx_kwds)) {
      Py_ssize_t kw_args;
      const Py_ssize_t pos_args = PyTuple_GET_SIZE(__pyx_args);
      switch (pos_args) {
        case 2: values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
        case 1: values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
        case 0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      kw_args = PyDict_Size(__pyx_kwds);
      switch (pos_args) {
        case 0:
        if (likely((values[0] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_pSettlementInfoConfirm)) != 0)) kw_args--;
        else goto __pyx_L5_argtuple_error;
        case 1:
        if (likely((values[1] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_nRequestID)) != 0)) kw_args--;
        else {
          __Pyx_RaiseArgtupleInvalid("ReqSettlementInfoConfirm", 1, 2, 2, 1); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 205; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
        }
      }
      if (unlikely(kw_args > 0)) {
        if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_pyargnames, 0, values, pos_args, "ReqSettlementInfoConfirm") < 0)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 205; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
      }
    } else if (PyTuple_GET_SIZE(__pyx_args) != 2) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
      values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
    }
    __pyx_v_pSettlementInfoConfirm = values[0];
    __pyx_v_nRequestID = __Pyx_PyInt_As_int(values[1]); if (unlikely((__pyx_v_nRequestID == (int)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 205; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  }
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("ReqSettlementInfoConfirm", 1, 2, 2, PyTuple_GET_SIZE(__pyx_args)); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 205; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  __pyx_L3_error:;
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqSettlementInfoConfirm", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_3ctp_10_TraderApi_9TraderApi_44ReqSettlementInfoConfirm(((struct __pyx_obj_3ctp_10_TraderApi_TraderApi *)__pyx_v_self), __pyx_v_pSettlementInfoConfirm, __pyx_v_nRequestID);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_44ReqSettlementInfoConfirm(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pSettlementInfoConfirm, int __pyx_v_nRequestID) {
  size_t __pyx_v_address;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_t_1;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  size_t __pyx_t_4;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("ReqSettlementInfoConfirm", 0);
  __pyx_t_1 = ((__pyx_v_self->spi == NULL) != 0);
  if (__pyx_t_1) {
    __Pyx_XDECREF(__pyx_r);
    __pyx_r = Py_None; __Pyx_INCREF(Py_None);
    goto __pyx_L0;
  }
  __pyx_t_2 = PyTuple_New(1); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 208; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_v_pSettlementInfoConfirm);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_v_pSettlementInfoConfirm);
  __Pyx_GIVEREF(__pyx_v_pSettlementInfoConfirm);
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_addressof, __pyx_t_2, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 208; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_4 = __Pyx_PyInt_As_size_t(__pyx_t_3); if (unlikely((__pyx_t_4 == (size_t)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 208; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_v_address = __pyx_t_4;
  {
      #ifdef WITH_THREAD
      PyThreadState *_save;
      Py_UNBLOCK_THREADS
      #endif
      {
        __pyx_v_nRequestID = __pyx_v_self->api->ReqSettlementInfoConfirm(((struct CThostFtdcSettlementInfoConfirmField *)__pyx_v_address), __pyx_v_nRequestID);
      }
      {
        {
          #ifdef WITH_THREAD
          Py_BLOCK_THREADS
          #endif
          goto __pyx_L6;
        }
        __pyx_L6:;
      }
  }
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_3 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 210; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_r = __pyx_t_3;
  __pyx_t_3 = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqSettlementInfoConfirm", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_47ReqRemoveParkedOrder(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds); 
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_47ReqRemoveParkedOrder(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_pRemoveParkedOrder = 0;
  int __pyx_v_nRequestID;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("ReqRemoveParkedOrder (wrapper)", 0);
  {
    static PyObject **__pyx_pyargnames[] = {&__pyx_n_s_pRemoveParkedOrder,&__pyx_n_s_nRequestID,0};
    PyObject* values[2] = {0,0};
    if (unlikely(__pyx_kwds)) {
      Py_ssize_t kw_args;
      const Py_ssize_t pos_args = PyTuple_GET_SIZE(__pyx_args);
      switch (pos_args) {
        case 2: values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
        case 1: values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
        case 0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      kw_args = PyDict_Size(__pyx_kwds);
      switch (pos_args) {
        case 0:
        if (likely((values[0] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_pRemoveParkedOrder)) != 0)) kw_args--;
        else goto __pyx_L5_argtuple_error;
        case 1:
        if (likely((values[1] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_nRequestID)) != 0)) kw_args--;
        else {
          __Pyx_RaiseArgtupleInvalid("ReqRemoveParkedOrder", 1, 2, 2, 1); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 212; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
        }
      }
      if (unlikely(kw_args > 0)) {
        if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_pyargnames, 0, values, pos_args, "ReqRemoveParkedOrder") < 0)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 212; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
      }
    } else if (PyTuple_GET_SIZE(__pyx_args) != 2) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
      values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
    }
    __pyx_v_pRemoveParkedOrder = values[0];
    __pyx_v_nRequestID = __Pyx_PyInt_As_int(values[1]); if (unlikely((__pyx_v_nRequestID == (int)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 212; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  }
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("ReqRemoveParkedOrder", 1, 2, 2, PyTuple_GET_SIZE(__pyx_args)); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 212; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  __pyx_L3_error:;
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqRemoveParkedOrder", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_3ctp_10_TraderApi_9TraderApi_46ReqRemoveParkedOrder(((struct __pyx_obj_3ctp_10_TraderApi_TraderApi *)__pyx_v_self), __pyx_v_pRemoveParkedOrder, __pyx_v_nRequestID);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_46ReqRemoveParkedOrder(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pRemoveParkedOrder, int __pyx_v_nRequestID) {
  size_t __pyx_v_address;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_t_1;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  size_t __pyx_t_4;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("ReqRemoveParkedOrder", 0);
  __pyx_t_1 = ((__pyx_v_self->spi == NULL) != 0);
  if (__pyx_t_1) {
    __Pyx_XDECREF(__pyx_r);
    __pyx_r = Py_None; __Pyx_INCREF(Py_None);
    goto __pyx_L0;
  }
  __pyx_t_2 = PyTuple_New(1); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 215; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_v_pRemoveParkedOrder);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_v_pRemoveParkedOrder);
  __Pyx_GIVEREF(__pyx_v_pRemoveParkedOrder);
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_addressof, __pyx_t_2, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 215; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_4 = __Pyx_PyInt_As_size_t(__pyx_t_3); if (unlikely((__pyx_t_4 == (size_t)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 215; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_v_address = __pyx_t_4;
  {
      #ifdef WITH_THREAD
      PyThreadState *_save;
      Py_UNBLOCK_THREADS
      #endif
      {
        __pyx_v_nRequestID = __pyx_v_self->api->ReqRemoveParkedOrder(((struct CThostFtdcRemoveParkedOrderField *)__pyx_v_address), __pyx_v_nRequestID);
      }
      {
        {
          #ifdef WITH_THREAD
          Py_BLOCK_THREADS
          #endif
          goto __pyx_L6;
        }
        __pyx_L6:;
      }
  }
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_3 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 217; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_r = __pyx_t_3;
  __pyx_t_3 = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqRemoveParkedOrder", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_49ReqRemoveParkedOrderAction(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds); 
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_49ReqRemoveParkedOrderAction(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_pRemoveParkedOrderAction = 0;
  int __pyx_v_nRequestID;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("ReqRemoveParkedOrderAction (wrapper)", 0);
  {
    static PyObject **__pyx_pyargnames[] = {&__pyx_n_s_pRemoveParkedOrderAction,&__pyx_n_s_nRequestID,0};
    PyObject* values[2] = {0,0};
    if (unlikely(__pyx_kwds)) {
      Py_ssize_t kw_args;
      const Py_ssize_t pos_args = PyTuple_GET_SIZE(__pyx_args);
      switch (pos_args) {
        case 2: values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
        case 1: values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
        case 0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      kw_args = PyDict_Size(__pyx_kwds);
      switch (pos_args) {
        case 0:
        if (likely((values[0] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_pRemoveParkedOrderAction)) != 0)) kw_args--;
        else goto __pyx_L5_argtuple_error;
        case 1:
        if (likely((values[1] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_nRequestID)) != 0)) kw_args--;
        else {
          __Pyx_RaiseArgtupleInvalid("ReqRemoveParkedOrderAction", 1, 2, 2, 1); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 219; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
        }
      }
      if (unlikely(kw_args > 0)) {
        if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_pyargnames, 0, values, pos_args, "ReqRemoveParkedOrderAction") < 0)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 219; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
      }
    } else if (PyTuple_GET_SIZE(__pyx_args) != 2) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
      values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
    }
    __pyx_v_pRemoveParkedOrderAction = values[0];
    __pyx_v_nRequestID = __Pyx_PyInt_As_int(values[1]); if (unlikely((__pyx_v_nRequestID == (int)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 219; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  }
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("ReqRemoveParkedOrderAction", 1, 2, 2, PyTuple_GET_SIZE(__pyx_args)); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 219; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  __pyx_L3_error:;
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqRemoveParkedOrderAction", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_3ctp_10_TraderApi_9TraderApi_48ReqRemoveParkedOrderAction(((struct __pyx_obj_3ctp_10_TraderApi_TraderApi *)__pyx_v_self), __pyx_v_pRemoveParkedOrderAction, __pyx_v_nRequestID);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_48ReqRemoveParkedOrderAction(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pRemoveParkedOrderAction, int __pyx_v_nRequestID) {
  size_t __pyx_v_address;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_t_1;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  size_t __pyx_t_4;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("ReqRemoveParkedOrderAction", 0);
  __pyx_t_1 = ((__pyx_v_self->spi == NULL) != 0);
  if (__pyx_t_1) {
    __Pyx_XDECREF(__pyx_r);
    __pyx_r = Py_None; __Pyx_INCREF(Py_None);
    goto __pyx_L0;
  }
  __pyx_t_2 = PyTuple_New(1); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 222; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_v_pRemoveParkedOrderAction);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_v_pRemoveParkedOrderAction);
  __Pyx_GIVEREF(__pyx_v_pRemoveParkedOrderAction);
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_addressof, __pyx_t_2, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 222; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_4 = __Pyx_PyInt_As_size_t(__pyx_t_3); if (unlikely((__pyx_t_4 == (size_t)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 222; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_v_address = __pyx_t_4;
  {
      #ifdef WITH_THREAD
      PyThreadState *_save;
      Py_UNBLOCK_THREADS
      #endif
      {
        __pyx_v_nRequestID = __pyx_v_self->api->ReqRemoveParkedOrderAction(((struct CThostFtdcRemoveParkedOrderActionField *)__pyx_v_address), __pyx_v_nRequestID);
      }
      {
        {
          #ifdef WITH_THREAD
          Py_BLOCK_THREADS
          #endif
          goto __pyx_L6;
        }
        __pyx_L6:;
      }
  }
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_3 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 224; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_r = __pyx_t_3;
  __pyx_t_3 = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqRemoveParkedOrderAction", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_51ReqQryOrder(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds); 
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_51ReqQryOrder(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_pQryOrder = 0;
  int __pyx_v_nRequestID;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("ReqQryOrder (wrapper)", 0);
  {
    static PyObject **__pyx_pyargnames[] = {&__pyx_n_s_pQryOrder,&__pyx_n_s_nRequestID,0};
    PyObject* values[2] = {0,0};
    if (unlikely(__pyx_kwds)) {
      Py_ssize_t kw_args;
      const Py_ssize_t pos_args = PyTuple_GET_SIZE(__pyx_args);
      switch (pos_args) {
        case 2: values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
        case 1: values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
        case 0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      kw_args = PyDict_Size(__pyx_kwds);
      switch (pos_args) {
        case 0:
        if (likely((values[0] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_pQryOrder)) != 0)) kw_args--;
        else goto __pyx_L5_argtuple_error;
        case 1:
        if (likely((values[1] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_nRequestID)) != 0)) kw_args--;
        else {
          __Pyx_RaiseArgtupleInvalid("ReqQryOrder", 1, 2, 2, 1); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 226; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
        }
      }
      if (unlikely(kw_args > 0)) {
        if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_pyargnames, 0, values, pos_args, "ReqQryOrder") < 0)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 226; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
      }
    } else if (PyTuple_GET_SIZE(__pyx_args) != 2) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
      values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
    }
    __pyx_v_pQryOrder = values[0];
    __pyx_v_nRequestID = __Pyx_PyInt_As_int(values[1]); if (unlikely((__pyx_v_nRequestID == (int)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 226; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  }
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("ReqQryOrder", 1, 2, 2, PyTuple_GET_SIZE(__pyx_args)); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 226; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  __pyx_L3_error:;
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQryOrder", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_3ctp_10_TraderApi_9TraderApi_50ReqQryOrder(((struct __pyx_obj_3ctp_10_TraderApi_TraderApi *)__pyx_v_self), __pyx_v_pQryOrder, __pyx_v_nRequestID);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_50ReqQryOrder(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQryOrder, int __pyx_v_nRequestID) {
  size_t __pyx_v_address;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_t_1;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  size_t __pyx_t_4;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("ReqQryOrder", 0);
  __pyx_t_1 = ((__pyx_v_self->spi == NULL) != 0);
  if (__pyx_t_1) {
    __Pyx_XDECREF(__pyx_r);
    __pyx_r = Py_None; __Pyx_INCREF(Py_None);
    goto __pyx_L0;
  }
  __pyx_t_2 = PyTuple_New(1); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 229; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_v_pQryOrder);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_v_pQryOrder);
  __Pyx_GIVEREF(__pyx_v_pQryOrder);
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_addressof, __pyx_t_2, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 229; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_4 = __Pyx_PyInt_As_size_t(__pyx_t_3); if (unlikely((__pyx_t_4 == (size_t)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 229; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_v_address = __pyx_t_4;
  {
      #ifdef WITH_THREAD
      PyThreadState *_save;
      Py_UNBLOCK_THREADS
      #endif
      {
        __pyx_v_nRequestID = __pyx_v_self->api->ReqQryOrder(((struct CThostFtdcQryOrderField *)__pyx_v_address), __pyx_v_nRequestID);
      }
      {
        {
          #ifdef WITH_THREAD
          Py_BLOCK_THREADS
          #endif
          goto __pyx_L6;
        }
        __pyx_L6:;
      }
  }
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_3 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 231; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_r = __pyx_t_3;
  __pyx_t_3 = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQryOrder", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_53ReqQryTrade(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds); 
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_53ReqQryTrade(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_pQryTrade = 0;
  int __pyx_v_nRequestID;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("ReqQryTrade (wrapper)", 0);
  {
    static PyObject **__pyx_pyargnames[] = {&__pyx_n_s_pQryTrade,&__pyx_n_s_nRequestID,0};
    PyObject* values[2] = {0,0};
    if (unlikely(__pyx_kwds)) {
      Py_ssize_t kw_args;
      const Py_ssize_t pos_args = PyTuple_GET_SIZE(__pyx_args);
      switch (pos_args) {
        case 2: values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
        case 1: values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
        case 0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      kw_args = PyDict_Size(__pyx_kwds);
      switch (pos_args) {
        case 0:
        if (likely((values[0] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_pQryTrade)) != 0)) kw_args--;
        else goto __pyx_L5_argtuple_error;
        case 1:
        if (likely((values[1] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_nRequestID)) != 0)) kw_args--;
        else {
          __Pyx_RaiseArgtupleInvalid("ReqQryTrade", 1, 2, 2, 1); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 233; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
        }
      }
      if (unlikely(kw_args > 0)) {
        if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_pyargnames, 0, values, pos_args, "ReqQryTrade") < 0)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 233; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
      }
    } else if (PyTuple_GET_SIZE(__pyx_args) != 2) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
      values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
    }
    __pyx_v_pQryTrade = values[0];
    __pyx_v_nRequestID = __Pyx_PyInt_As_int(values[1]); if (unlikely((__pyx_v_nRequestID == (int)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 233; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  }
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("ReqQryTrade", 1, 2, 2, PyTuple_GET_SIZE(__pyx_args)); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 233; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  __pyx_L3_error:;
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQryTrade", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_3ctp_10_TraderApi_9TraderApi_52ReqQryTrade(((struct __pyx_obj_3ctp_10_TraderApi_TraderApi *)__pyx_v_self), __pyx_v_pQryTrade, __pyx_v_nRequestID);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_52ReqQryTrade(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQryTrade, int __pyx_v_nRequestID) {
  size_t __pyx_v_address;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_t_1;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  size_t __pyx_t_4;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("ReqQryTrade", 0);
  __pyx_t_1 = ((__pyx_v_self->spi == NULL) != 0);
  if (__pyx_t_1) {
    __Pyx_XDECREF(__pyx_r);
    __pyx_r = Py_None; __Pyx_INCREF(Py_None);
    goto __pyx_L0;
  }
  __pyx_t_2 = PyTuple_New(1); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 236; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_v_pQryTrade);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_v_pQryTrade);
  __Pyx_GIVEREF(__pyx_v_pQryTrade);
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_addressof, __pyx_t_2, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 236; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_4 = __Pyx_PyInt_As_size_t(__pyx_t_3); if (unlikely((__pyx_t_4 == (size_t)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 236; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_v_address = __pyx_t_4;
  {
      #ifdef WITH_THREAD
      PyThreadState *_save;
      Py_UNBLOCK_THREADS
      #endif
      {
        __pyx_v_nRequestID = __pyx_v_self->api->ReqQryTrade(((struct CThostFtdcQryTradeField *)__pyx_v_address), __pyx_v_nRequestID);
      }
      {
        {
          #ifdef WITH_THREAD
          Py_BLOCK_THREADS
          #endif
          goto __pyx_L6;
        }
        __pyx_L6:;
      }
  }
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_3 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 238; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_r = __pyx_t_3;
  __pyx_t_3 = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQryTrade", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_55ReqQryInvestorPosition(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds); 
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_55ReqQryInvestorPosition(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_pQryInvestorPosition = 0;
  int __pyx_v_nRequestID;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("ReqQryInvestorPosition (wrapper)", 0);
  {
    static PyObject **__pyx_pyargnames[] = {&__pyx_n_s_pQryInvestorPosition,&__pyx_n_s_nRequestID,0};
    PyObject* values[2] = {0,0};
    if (unlikely(__pyx_kwds)) {
      Py_ssize_t kw_args;
      const Py_ssize_t pos_args = PyTuple_GET_SIZE(__pyx_args);
      switch (pos_args) {
        case 2: values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
        case 1: values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
        case 0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      kw_args = PyDict_Size(__pyx_kwds);
      switch (pos_args) {
        case 0:
        if (likely((values[0] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_pQryInvestorPosition)) != 0)) kw_args--;
        else goto __pyx_L5_argtuple_error;
        case 1:
        if (likely((values[1] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_nRequestID)) != 0)) kw_args--;
        else {
          __Pyx_RaiseArgtupleInvalid("ReqQryInvestorPosition", 1, 2, 2, 1); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 240; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
        }
      }
      if (unlikely(kw_args > 0)) {
        if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_pyargnames, 0, values, pos_args, "ReqQryInvestorPosition") < 0)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 240; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
      }
    } else if (PyTuple_GET_SIZE(__pyx_args) != 2) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
      values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
    }
    __pyx_v_pQryInvestorPosition = values[0];
    __pyx_v_nRequestID = __Pyx_PyInt_As_int(values[1]); if (unlikely((__pyx_v_nRequestID == (int)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 240; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  }
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("ReqQryInvestorPosition", 1, 2, 2, PyTuple_GET_SIZE(__pyx_args)); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 240; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  __pyx_L3_error:;
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQryInvestorPosition", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_3ctp_10_TraderApi_9TraderApi_54ReqQryInvestorPosition(((struct __pyx_obj_3ctp_10_TraderApi_TraderApi *)__pyx_v_self), __pyx_v_pQryInvestorPosition, __pyx_v_nRequestID);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_54ReqQryInvestorPosition(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQryInvestorPosition, int __pyx_v_nRequestID) {
  size_t __pyx_v_address;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_t_1;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  size_t __pyx_t_4;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("ReqQryInvestorPosition", 0);
  __pyx_t_1 = ((__pyx_v_self->spi == NULL) != 0);
  if (__pyx_t_1) {
    __Pyx_XDECREF(__pyx_r);
    __pyx_r = Py_None; __Pyx_INCREF(Py_None);
    goto __pyx_L0;
  }
  __pyx_t_2 = PyTuple_New(1); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 243; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_v_pQryInvestorPosition);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_v_pQryInvestorPosition);
  __Pyx_GIVEREF(__pyx_v_pQryInvestorPosition);
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_addressof, __pyx_t_2, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 243; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_4 = __Pyx_PyInt_As_size_t(__pyx_t_3); if (unlikely((__pyx_t_4 == (size_t)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 243; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_v_address = __pyx_t_4;
  {
      #ifdef WITH_THREAD
      PyThreadState *_save;
      Py_UNBLOCK_THREADS
      #endif
      {
        __pyx_v_nRequestID = __pyx_v_self->api->ReqQryInvestorPosition(((struct CThostFtdcQryInvestorPositionField *)__pyx_v_address), __pyx_v_nRequestID);
      }
      {
        {
          #ifdef WITH_THREAD
          Py_BLOCK_THREADS
          #endif
          goto __pyx_L6;
        }
        __pyx_L6:;
      }
  }
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_3 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 245; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_r = __pyx_t_3;
  __pyx_t_3 = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQryInvestorPosition", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_57ReqQryTradingAccount(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds); 
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_57ReqQryTradingAccount(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_pQryTradingAccount = 0;
  int __pyx_v_nRequestID;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("ReqQryTradingAccount (wrapper)", 0);
  {
    static PyObject **__pyx_pyargnames[] = {&__pyx_n_s_pQryTradingAccount,&__pyx_n_s_nRequestID,0};
    PyObject* values[2] = {0,0};
    if (unlikely(__pyx_kwds)) {
      Py_ssize_t kw_args;
      const Py_ssize_t pos_args = PyTuple_GET_SIZE(__pyx_args);
      switch (pos_args) {
        case 2: values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
        case 1: values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
        case 0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      kw_args = PyDict_Size(__pyx_kwds);
      switch (pos_args) {
        case 0:
        if (likely((values[0] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_pQryTradingAccount)) != 0)) kw_args--;
        else goto __pyx_L5_argtuple_error;
        case 1:
        if (likely((values[1] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_nRequestID)) != 0)) kw_args--;
        else {
          __Pyx_RaiseArgtupleInvalid("ReqQryTradingAccount", 1, 2, 2, 1); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 247; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
        }
      }
      if (unlikely(kw_args > 0)) {
        if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_pyargnames, 0, values, pos_args, "ReqQryTradingAccount") < 0)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 247; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
      }
    } else if (PyTuple_GET_SIZE(__pyx_args) != 2) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
      values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
    }
    __pyx_v_pQryTradingAccount = values[0];
    __pyx_v_nRequestID = __Pyx_PyInt_As_int(values[1]); if (unlikely((__pyx_v_nRequestID == (int)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 247; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  }
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("ReqQryTradingAccount", 1, 2, 2, PyTuple_GET_SIZE(__pyx_args)); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 247; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  __pyx_L3_error:;
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQryTradingAccount", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_3ctp_10_TraderApi_9TraderApi_56ReqQryTradingAccount(((struct __pyx_obj_3ctp_10_TraderApi_TraderApi *)__pyx_v_self), __pyx_v_pQryTradingAccount, __pyx_v_nRequestID);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_56ReqQryTradingAccount(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQryTradingAccount, int __pyx_v_nRequestID) {
  size_t __pyx_v_address;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_t_1;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  size_t __pyx_t_4;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("ReqQryTradingAccount", 0);
  __pyx_t_1 = ((__pyx_v_self->spi == NULL) != 0);
  if (__pyx_t_1) {
    __Pyx_XDECREF(__pyx_r);
    __pyx_r = Py_None; __Pyx_INCREF(Py_None);
    goto __pyx_L0;
  }
  __pyx_t_2 = PyTuple_New(1); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 250; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_v_pQryTradingAccount);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_v_pQryTradingAccount);
  __Pyx_GIVEREF(__pyx_v_pQryTradingAccount);
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_addressof, __pyx_t_2, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 250; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_4 = __Pyx_PyInt_As_size_t(__pyx_t_3); if (unlikely((__pyx_t_4 == (size_t)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 250; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_v_address = __pyx_t_4;
  {
      #ifdef WITH_THREAD
      PyThreadState *_save;
      Py_UNBLOCK_THREADS
      #endif
      {
        __pyx_v_nRequestID = __pyx_v_self->api->ReqQryTradingAccount(((struct CThostFtdcQryTradingAccountField *)__pyx_v_address), __pyx_v_nRequestID);
      }
      {
        {
          #ifdef WITH_THREAD
          Py_BLOCK_THREADS
          #endif
          goto __pyx_L6;
        }
        __pyx_L6:;
      }
  }
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_3 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 252; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_r = __pyx_t_3;
  __pyx_t_3 = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQryTradingAccount", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_59ReqQryInvestor(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds); 
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_59ReqQryInvestor(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_pQryInvestor = 0;
  int __pyx_v_nRequestID;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("ReqQryInvestor (wrapper)", 0);
  {
    static PyObject **__pyx_pyargnames[] = {&__pyx_n_s_pQryInvestor,&__pyx_n_s_nRequestID,0};
    PyObject* values[2] = {0,0};
    if (unlikely(__pyx_kwds)) {
      Py_ssize_t kw_args;
      const Py_ssize_t pos_args = PyTuple_GET_SIZE(__pyx_args);
      switch (pos_args) {
        case 2: values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
        case 1: values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
        case 0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      kw_args = PyDict_Size(__pyx_kwds);
      switch (pos_args) {
        case 0:
        if (likely((values[0] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_pQryInvestor)) != 0)) kw_args--;
        else goto __pyx_L5_argtuple_error;
        case 1:
        if (likely((values[1] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_nRequestID)) != 0)) kw_args--;
        else {
          __Pyx_RaiseArgtupleInvalid("ReqQryInvestor", 1, 2, 2, 1); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 254; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
        }
      }
      if (unlikely(kw_args > 0)) {
        if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_pyargnames, 0, values, pos_args, "ReqQryInvestor") < 0)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 254; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
      }
    } else if (PyTuple_GET_SIZE(__pyx_args) != 2) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
      values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
    }
    __pyx_v_pQryInvestor = values[0];
    __pyx_v_nRequestID = __Pyx_PyInt_As_int(values[1]); if (unlikely((__pyx_v_nRequestID == (int)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 254; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  }
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("ReqQryInvestor", 1, 2, 2, PyTuple_GET_SIZE(__pyx_args)); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 254; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  __pyx_L3_error:;
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQryInvestor", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_3ctp_10_TraderApi_9TraderApi_58ReqQryInvestor(((struct __pyx_obj_3ctp_10_TraderApi_TraderApi *)__pyx_v_self), __pyx_v_pQryInvestor, __pyx_v_nRequestID);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_58ReqQryInvestor(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQryInvestor, int __pyx_v_nRequestID) {
  size_t __pyx_v_address;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_t_1;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  size_t __pyx_t_4;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("ReqQryInvestor", 0);
  __pyx_t_1 = ((__pyx_v_self->spi == NULL) != 0);
  if (__pyx_t_1) {
    __Pyx_XDECREF(__pyx_r);
    __pyx_r = Py_None; __Pyx_INCREF(Py_None);
    goto __pyx_L0;
  }
  __pyx_t_2 = PyTuple_New(1); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 257; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_v_pQryInvestor);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_v_pQryInvestor);
  __Pyx_GIVEREF(__pyx_v_pQryInvestor);
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_addressof, __pyx_t_2, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 257; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_4 = __Pyx_PyInt_As_size_t(__pyx_t_3); if (unlikely((__pyx_t_4 == (size_t)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 257; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_v_address = __pyx_t_4;
  {
      #ifdef WITH_THREAD
      PyThreadState *_save;
      Py_UNBLOCK_THREADS
      #endif
      {
        __pyx_v_nRequestID = __pyx_v_self->api->ReqQryInvestor(((struct CThostFtdcQryInvestorField *)__pyx_v_address), __pyx_v_nRequestID);
      }
      {
        {
          #ifdef WITH_THREAD
          Py_BLOCK_THREADS
          #endif
          goto __pyx_L6;
        }
        __pyx_L6:;
      }
  }
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_3 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 259; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_r = __pyx_t_3;
  __pyx_t_3 = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQryInvestor", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_61ReqQryTradingCode(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds); 
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_61ReqQryTradingCode(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_pQryTradingCode = 0;
  int __pyx_v_nRequestID;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("ReqQryTradingCode (wrapper)", 0);
  {
    static PyObject **__pyx_pyargnames[] = {&__pyx_n_s_pQryTradingCode,&__pyx_n_s_nRequestID,0};
    PyObject* values[2] = {0,0};
    if (unlikely(__pyx_kwds)) {
      Py_ssize_t kw_args;
      const Py_ssize_t pos_args = PyTuple_GET_SIZE(__pyx_args);
      switch (pos_args) {
        case 2: values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
        case 1: values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
        case 0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      kw_args = PyDict_Size(__pyx_kwds);
      switch (pos_args) {
        case 0:
        if (likely((values[0] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_pQryTradingCode)) != 0)) kw_args--;
        else goto __pyx_L5_argtuple_error;
        case 1:
        if (likely((values[1] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_nRequestID)) != 0)) kw_args--;
        else {
          __Pyx_RaiseArgtupleInvalid("ReqQryTradingCode", 1, 2, 2, 1); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 261; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
        }
      }
      if (unlikely(kw_args > 0)) {
        if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_pyargnames, 0, values, pos_args, "ReqQryTradingCode") < 0)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 261; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
      }
    } else if (PyTuple_GET_SIZE(__pyx_args) != 2) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
      values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
    }
    __pyx_v_pQryTradingCode = values[0];
    __pyx_v_nRequestID = __Pyx_PyInt_As_int(values[1]); if (unlikely((__pyx_v_nRequestID == (int)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 261; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  }
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("ReqQryTradingCode", 1, 2, 2, PyTuple_GET_SIZE(__pyx_args)); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 261; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  __pyx_L3_error:;
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQryTradingCode", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_3ctp_10_TraderApi_9TraderApi_60ReqQryTradingCode(((struct __pyx_obj_3ctp_10_TraderApi_TraderApi *)__pyx_v_self), __pyx_v_pQryTradingCode, __pyx_v_nRequestID);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_60ReqQryTradingCode(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQryTradingCode, int __pyx_v_nRequestID) {
  size_t __pyx_v_address;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_t_1;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  size_t __pyx_t_4;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("ReqQryTradingCode", 0);
  __pyx_t_1 = ((__pyx_v_self->spi == NULL) != 0);
  if (__pyx_t_1) {
    __Pyx_XDECREF(__pyx_r);
    __pyx_r = Py_None; __Pyx_INCREF(Py_None);
    goto __pyx_L0;
  }
  __pyx_t_2 = PyTuple_New(1); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 264; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_v_pQryTradingCode);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_v_pQryTradingCode);
  __Pyx_GIVEREF(__pyx_v_pQryTradingCode);
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_addressof, __pyx_t_2, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 264; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_4 = __Pyx_PyInt_As_size_t(__pyx_t_3); if (unlikely((__pyx_t_4 == (size_t)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 264; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_v_address = __pyx_t_4;
  {
      #ifdef WITH_THREAD
      PyThreadState *_save;
      Py_UNBLOCK_THREADS
      #endif
      {
        __pyx_v_nRequestID = __pyx_v_self->api->ReqQryTradingCode(((struct CThostFtdcQryTradingCodeField *)__pyx_v_address), __pyx_v_nRequestID);
      }
      {
        {
          #ifdef WITH_THREAD
          Py_BLOCK_THREADS
          #endif
          goto __pyx_L6;
        }
        __pyx_L6:;
      }
  }
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_3 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 266; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_r = __pyx_t_3;
  __pyx_t_3 = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQryTradingCode", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_63ReqQryInstrumentMarginRate(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds); 
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_63ReqQryInstrumentMarginRate(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_pQryInstrumentMarginRate = 0;
  int __pyx_v_nRequestID;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("ReqQryInstrumentMarginRate (wrapper)", 0);
  {
    static PyObject **__pyx_pyargnames[] = {&__pyx_n_s_pQryInstrumentMarginRate,&__pyx_n_s_nRequestID,0};
    PyObject* values[2] = {0,0};
    if (unlikely(__pyx_kwds)) {
      Py_ssize_t kw_args;
      const Py_ssize_t pos_args = PyTuple_GET_SIZE(__pyx_args);
      switch (pos_args) {
        case 2: values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
        case 1: values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
        case 0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      kw_args = PyDict_Size(__pyx_kwds);
      switch (pos_args) {
        case 0:
        if (likely((values[0] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_pQryInstrumentMarginRate)) != 0)) kw_args--;
        else goto __pyx_L5_argtuple_error;
        case 1:
        if (likely((values[1] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_nRequestID)) != 0)) kw_args--;
        else {
          __Pyx_RaiseArgtupleInvalid("ReqQryInstrumentMarginRate", 1, 2, 2, 1); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 268; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
        }
      }
      if (unlikely(kw_args > 0)) {
        if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_pyargnames, 0, values, pos_args, "ReqQryInstrumentMarginRate") < 0)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 268; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
      }
    } else if (PyTuple_GET_SIZE(__pyx_args) != 2) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
      values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
    }
    __pyx_v_pQryInstrumentMarginRate = values[0];
    __pyx_v_nRequestID = __Pyx_PyInt_As_int(values[1]); if (unlikely((__pyx_v_nRequestID == (int)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 268; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  }
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("ReqQryInstrumentMarginRate", 1, 2, 2, PyTuple_GET_SIZE(__pyx_args)); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 268; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  __pyx_L3_error:;
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQryInstrumentMarginRate", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_3ctp_10_TraderApi_9TraderApi_62ReqQryInstrumentMarginRate(((struct __pyx_obj_3ctp_10_TraderApi_TraderApi *)__pyx_v_self), __pyx_v_pQryInstrumentMarginRate, __pyx_v_nRequestID);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_62ReqQryInstrumentMarginRate(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQryInstrumentMarginRate, int __pyx_v_nRequestID) {
  size_t __pyx_v_address;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_t_1;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  size_t __pyx_t_4;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("ReqQryInstrumentMarginRate", 0);
  __pyx_t_1 = ((__pyx_v_self->spi == NULL) != 0);
  if (__pyx_t_1) {
    __Pyx_XDECREF(__pyx_r);
    __pyx_r = Py_None; __Pyx_INCREF(Py_None);
    goto __pyx_L0;
  }
  __pyx_t_2 = PyTuple_New(1); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 271; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_v_pQryInstrumentMarginRate);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_v_pQryInstrumentMarginRate);
  __Pyx_GIVEREF(__pyx_v_pQryInstrumentMarginRate);
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_addressof, __pyx_t_2, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 271; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_4 = __Pyx_PyInt_As_size_t(__pyx_t_3); if (unlikely((__pyx_t_4 == (size_t)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 271; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_v_address = __pyx_t_4;
  {
      #ifdef WITH_THREAD
      PyThreadState *_save;
      Py_UNBLOCK_THREADS
      #endif
      {
        __pyx_v_nRequestID = __pyx_v_self->api->ReqQryInstrumentMarginRate(((struct CThostFtdcQryInstrumentMarginRateField *)__pyx_v_address), __pyx_v_nRequestID);
      }
      {
        {
          #ifdef WITH_THREAD
          Py_BLOCK_THREADS
          #endif
          goto __pyx_L6;
        }
        __pyx_L6:;
      }
  }
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_3 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 273; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_r = __pyx_t_3;
  __pyx_t_3 = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQryInstrumentMarginRate", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_65ReqQryInstrumentCommissionRate(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds); 
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_65ReqQryInstrumentCommissionRate(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_pQryInstrumentCommissionRate = 0;
  int __pyx_v_nRequestID;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("ReqQryInstrumentCommissionRate (wrapper)", 0);
  {
    static PyObject **__pyx_pyargnames[] = {&__pyx_n_s_pQryInstrumentCommissionRate,&__pyx_n_s_nRequestID,0};
    PyObject* values[2] = {0,0};
    if (unlikely(__pyx_kwds)) {
      Py_ssize_t kw_args;
      const Py_ssize_t pos_args = PyTuple_GET_SIZE(__pyx_args);
      switch (pos_args) {
        case 2: values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
        case 1: values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
        case 0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      kw_args = PyDict_Size(__pyx_kwds);
      switch (pos_args) {
        case 0:
        if (likely((values[0] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_pQryInstrumentCommissionRate)) != 0)) kw_args--;
        else goto __pyx_L5_argtuple_error;
        case 1:
        if (likely((values[1] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_nRequestID)) != 0)) kw_args--;
        else {
          __Pyx_RaiseArgtupleInvalid("ReqQryInstrumentCommissionRate", 1, 2, 2, 1); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 275; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
        }
      }
      if (unlikely(kw_args > 0)) {
        if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_pyargnames, 0, values, pos_args, "ReqQryInstrumentCommissionRate") < 0)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 275; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
      }
    } else if (PyTuple_GET_SIZE(__pyx_args) != 2) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
      values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
    }
    __pyx_v_pQryInstrumentCommissionRate = values[0];
    __pyx_v_nRequestID = __Pyx_PyInt_As_int(values[1]); if (unlikely((__pyx_v_nRequestID == (int)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 275; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  }
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("ReqQryInstrumentCommissionRate", 1, 2, 2, PyTuple_GET_SIZE(__pyx_args)); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 275; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  __pyx_L3_error:;
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQryInstrumentCommissionRate", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_3ctp_10_TraderApi_9TraderApi_64ReqQryInstrumentCommissionRate(((struct __pyx_obj_3ctp_10_TraderApi_TraderApi *)__pyx_v_self), __pyx_v_pQryInstrumentCommissionRate, __pyx_v_nRequestID);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_64ReqQryInstrumentCommissionRate(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQryInstrumentCommissionRate, int __pyx_v_nRequestID) {
  size_t __pyx_v_address;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_t_1;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  size_t __pyx_t_4;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("ReqQryInstrumentCommissionRate", 0);
  __pyx_t_1 = ((__pyx_v_self->spi == NULL) != 0);
  if (__pyx_t_1) {
    __Pyx_XDECREF(__pyx_r);
    __pyx_r = Py_None; __Pyx_INCREF(Py_None);
    goto __pyx_L0;
  }
  __pyx_t_2 = PyTuple_New(1); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 278; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_v_pQryInstrumentCommissionRate);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_v_pQryInstrumentCommissionRate);
  __Pyx_GIVEREF(__pyx_v_pQryInstrumentCommissionRate);
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_addressof, __pyx_t_2, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 278; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_4 = __Pyx_PyInt_As_size_t(__pyx_t_3); if (unlikely((__pyx_t_4 == (size_t)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 278; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_v_address = __pyx_t_4;
  {
      #ifdef WITH_THREAD
      PyThreadState *_save;
      Py_UNBLOCK_THREADS
      #endif
      {
        __pyx_v_nRequestID = __pyx_v_self->api->ReqQryInstrumentCommissionRate(((struct CThostFtdcQryInstrumentCommissionRateField *)__pyx_v_address), __pyx_v_nRequestID);
      }
      {
        {
          #ifdef WITH_THREAD
          Py_BLOCK_THREADS
          #endif
          goto __pyx_L6;
        }
        __pyx_L6:;
      }
  }
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_3 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 280; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_r = __pyx_t_3;
  __pyx_t_3 = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQryInstrumentCommissionRate", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_67ReqQryExchange(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds); 
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_67ReqQryExchange(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_pQryExchange = 0;
  int __pyx_v_nRequestID;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("ReqQryExchange (wrapper)", 0);
  {
    static PyObject **__pyx_pyargnames[] = {&__pyx_n_s_pQryExchange,&__pyx_n_s_nRequestID,0};
    PyObject* values[2] = {0,0};
    if (unlikely(__pyx_kwds)) {
      Py_ssize_t kw_args;
      const Py_ssize_t pos_args = PyTuple_GET_SIZE(__pyx_args);
      switch (pos_args) {
        case 2: values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
        case 1: values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
        case 0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      kw_args = PyDict_Size(__pyx_kwds);
      switch (pos_args) {
        case 0:
        if (likely((values[0] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_pQryExchange)) != 0)) kw_args--;
        else goto __pyx_L5_argtuple_error;
        case 1:
        if (likely((values[1] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_nRequestID)) != 0)) kw_args--;
        else {
          __Pyx_RaiseArgtupleInvalid("ReqQryExchange", 1, 2, 2, 1); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 282; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
        }
      }
      if (unlikely(kw_args > 0)) {
        if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_pyargnames, 0, values, pos_args, "ReqQryExchange") < 0)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 282; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
      }
    } else if (PyTuple_GET_SIZE(__pyx_args) != 2) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
      values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
    }
    __pyx_v_pQryExchange = values[0];
    __pyx_v_nRequestID = __Pyx_PyInt_As_int(values[1]); if (unlikely((__pyx_v_nRequestID == (int)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 282; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  }
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("ReqQryExchange", 1, 2, 2, PyTuple_GET_SIZE(__pyx_args)); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 282; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  __pyx_L3_error:;
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQryExchange", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_3ctp_10_TraderApi_9TraderApi_66ReqQryExchange(((struct __pyx_obj_3ctp_10_TraderApi_TraderApi *)__pyx_v_self), __pyx_v_pQryExchange, __pyx_v_nRequestID);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_66ReqQryExchange(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQryExchange, int __pyx_v_nRequestID) {
  size_t __pyx_v_address;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_t_1;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  size_t __pyx_t_4;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("ReqQryExchange", 0);
  __pyx_t_1 = ((__pyx_v_self->spi == NULL) != 0);
  if (__pyx_t_1) {
    __Pyx_XDECREF(__pyx_r);
    __pyx_r = Py_None; __Pyx_INCREF(Py_None);
    goto __pyx_L0;
  }
  __pyx_t_2 = PyTuple_New(1); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 285; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_v_pQryExchange);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_v_pQryExchange);
  __Pyx_GIVEREF(__pyx_v_pQryExchange);
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_addressof, __pyx_t_2, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 285; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_4 = __Pyx_PyInt_As_size_t(__pyx_t_3); if (unlikely((__pyx_t_4 == (size_t)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 285; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_v_address = __pyx_t_4;
  {
      #ifdef WITH_THREAD
      PyThreadState *_save;
      Py_UNBLOCK_THREADS
      #endif
      {
        __pyx_v_nRequestID = __pyx_v_self->api->ReqQryExchange(((struct CThostFtdcQryExchangeField *)__pyx_v_address), __pyx_v_nRequestID);
      }
      {
        {
          #ifdef WITH_THREAD
          Py_BLOCK_THREADS
          #endif
          goto __pyx_L6;
        }
        __pyx_L6:;
      }
  }
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_3 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 287; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_r = __pyx_t_3;
  __pyx_t_3 = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQryExchange", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_69ReqQryProduct(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds); 
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_69ReqQryProduct(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_pQryProduct = 0;
  int __pyx_v_nRequestID;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("ReqQryProduct (wrapper)", 0);
  {
    static PyObject **__pyx_pyargnames[] = {&__pyx_n_s_pQryProduct,&__pyx_n_s_nRequestID,0};
    PyObject* values[2] = {0,0};
    if (unlikely(__pyx_kwds)) {
      Py_ssize_t kw_args;
      const Py_ssize_t pos_args = PyTuple_GET_SIZE(__pyx_args);
      switch (pos_args) {
        case 2: values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
        case 1: values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
        case 0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      kw_args = PyDict_Size(__pyx_kwds);
      switch (pos_args) {
        case 0:
        if (likely((values[0] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_pQryProduct)) != 0)) kw_args--;
        else goto __pyx_L5_argtuple_error;
        case 1:
        if (likely((values[1] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_nRequestID)) != 0)) kw_args--;
        else {
          __Pyx_RaiseArgtupleInvalid("ReqQryProduct", 1, 2, 2, 1); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 289; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
        }
      }
      if (unlikely(kw_args > 0)) {
        if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_pyargnames, 0, values, pos_args, "ReqQryProduct") < 0)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 289; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
      }
    } else if (PyTuple_GET_SIZE(__pyx_args) != 2) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
      values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
    }
    __pyx_v_pQryProduct = values[0];
    __pyx_v_nRequestID = __Pyx_PyInt_As_int(values[1]); if (unlikely((__pyx_v_nRequestID == (int)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 289; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  }
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("ReqQryProduct", 1, 2, 2, PyTuple_GET_SIZE(__pyx_args)); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 289; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  __pyx_L3_error:;
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQryProduct", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_3ctp_10_TraderApi_9TraderApi_68ReqQryProduct(((struct __pyx_obj_3ctp_10_TraderApi_TraderApi *)__pyx_v_self), __pyx_v_pQryProduct, __pyx_v_nRequestID);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_68ReqQryProduct(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQryProduct, int __pyx_v_nRequestID) {
  size_t __pyx_v_address;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_t_1;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  size_t __pyx_t_4;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("ReqQryProduct", 0);
  __pyx_t_1 = ((__pyx_v_self->spi == NULL) != 0);
  if (__pyx_t_1) {
    __Pyx_XDECREF(__pyx_r);
    __pyx_r = Py_None; __Pyx_INCREF(Py_None);
    goto __pyx_L0;
  }
  __pyx_t_2 = PyTuple_New(1); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 292; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_v_pQryProduct);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_v_pQryProduct);
  __Pyx_GIVEREF(__pyx_v_pQryProduct);
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_addressof, __pyx_t_2, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 292; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_4 = __Pyx_PyInt_As_size_t(__pyx_t_3); if (unlikely((__pyx_t_4 == (size_t)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 292; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_v_address = __pyx_t_4;
  {
      #ifdef WITH_THREAD
      PyThreadState *_save;
      Py_UNBLOCK_THREADS
      #endif
      {
        __pyx_v_nRequestID = __pyx_v_self->api->ReqQryProduct(((struct CThostFtdcQryProductField *)__pyx_v_address), __pyx_v_nRequestID);
      }
      {
        {
          #ifdef WITH_THREAD
          Py_BLOCK_THREADS
          #endif
          goto __pyx_L6;
        }
        __pyx_L6:;
      }
  }
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_3 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 294; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_r = __pyx_t_3;
  __pyx_t_3 = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQryProduct", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_71ReqQryInstrument(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds); 
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_71ReqQryInstrument(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_pQryInstrument = 0;
  int __pyx_v_nRequestID;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("ReqQryInstrument (wrapper)", 0);
  {
    static PyObject **__pyx_pyargnames[] = {&__pyx_n_s_pQryInstrument,&__pyx_n_s_nRequestID,0};
    PyObject* values[2] = {0,0};
    if (unlikely(__pyx_kwds)) {
      Py_ssize_t kw_args;
      const Py_ssize_t pos_args = PyTuple_GET_SIZE(__pyx_args);
      switch (pos_args) {
        case 2: values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
        case 1: values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
        case 0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      kw_args = PyDict_Size(__pyx_kwds);
      switch (pos_args) {
        case 0:
        if (likely((values[0] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_pQryInstrument)) != 0)) kw_args--;
        else goto __pyx_L5_argtuple_error;
        case 1:
        if (likely((values[1] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_nRequestID)) != 0)) kw_args--;
        else {
          __Pyx_RaiseArgtupleInvalid("ReqQryInstrument", 1, 2, 2, 1); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 296; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
        }
      }
      if (unlikely(kw_args > 0)) {
        if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_pyargnames, 0, values, pos_args, "ReqQryInstrument") < 0)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 296; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
      }
    } else if (PyTuple_GET_SIZE(__pyx_args) != 2) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
      values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
    }
    __pyx_v_pQryInstrument = values[0];
    __pyx_v_nRequestID = __Pyx_PyInt_As_int(values[1]); if (unlikely((__pyx_v_nRequestID == (int)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 296; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  }
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("ReqQryInstrument", 1, 2, 2, PyTuple_GET_SIZE(__pyx_args)); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 296; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  __pyx_L3_error:;
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQryInstrument", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_3ctp_10_TraderApi_9TraderApi_70ReqQryInstrument(((struct __pyx_obj_3ctp_10_TraderApi_TraderApi *)__pyx_v_self), __pyx_v_pQryInstrument, __pyx_v_nRequestID);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_70ReqQryInstrument(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQryInstrument, int __pyx_v_nRequestID) {
  size_t __pyx_v_address;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_t_1;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  size_t __pyx_t_4;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("ReqQryInstrument", 0);
  __pyx_t_1 = ((__pyx_v_self->spi == NULL) != 0);
  if (__pyx_t_1) {
    __Pyx_XDECREF(__pyx_r);
    __pyx_r = Py_None; __Pyx_INCREF(Py_None);
    goto __pyx_L0;
  }
  __pyx_t_2 = PyTuple_New(1); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 299; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_v_pQryInstrument);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_v_pQryInstrument);
  __Pyx_GIVEREF(__pyx_v_pQryInstrument);
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_addressof, __pyx_t_2, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 299; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_4 = __Pyx_PyInt_As_size_t(__pyx_t_3); if (unlikely((__pyx_t_4 == (size_t)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 299; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_v_address = __pyx_t_4;
  {
      #ifdef WITH_THREAD
      PyThreadState *_save;
      Py_UNBLOCK_THREADS
      #endif
      {
        __pyx_v_nRequestID = __pyx_v_self->api->ReqQryInstrument(((struct CThostFtdcQryInstrumentField *)__pyx_v_address), __pyx_v_nRequestID);
      }
      {
        {
          #ifdef WITH_THREAD
          Py_BLOCK_THREADS
          #endif
          goto __pyx_L6;
        }
        __pyx_L6:;
      }
  }
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_3 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 301; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_r = __pyx_t_3;
  __pyx_t_3 = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQryInstrument", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_73ReqQryDepthMarketData(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds); 
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_73ReqQryDepthMarketData(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_pQryDepthMarketData = 0;
  int __pyx_v_nRequestID;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("ReqQryDepthMarketData (wrapper)", 0);
  {
    static PyObject **__pyx_pyargnames[] = {&__pyx_n_s_pQryDepthMarketData,&__pyx_n_s_nRequestID,0};
    PyObject* values[2] = {0,0};
    if (unlikely(__pyx_kwds)) {
      Py_ssize_t kw_args;
      const Py_ssize_t pos_args = PyTuple_GET_SIZE(__pyx_args);
      switch (pos_args) {
        case 2: values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
        case 1: values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
        case 0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      kw_args = PyDict_Size(__pyx_kwds);
      switch (pos_args) {
        case 0:
        if (likely((values[0] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_pQryDepthMarketData)) != 0)) kw_args--;
        else goto __pyx_L5_argtuple_error;
        case 1:
        if (likely((values[1] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_nRequestID)) != 0)) kw_args--;
        else {
          __Pyx_RaiseArgtupleInvalid("ReqQryDepthMarketData", 1, 2, 2, 1); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 303; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
        }
      }
      if (unlikely(kw_args > 0)) {
        if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_pyargnames, 0, values, pos_args, "ReqQryDepthMarketData") < 0)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 303; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
      }
    } else if (PyTuple_GET_SIZE(__pyx_args) != 2) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
      values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
    }
    __pyx_v_pQryDepthMarketData = values[0];
    __pyx_v_nRequestID = __Pyx_PyInt_As_int(values[1]); if (unlikely((__pyx_v_nRequestID == (int)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 303; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  }
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("ReqQryDepthMarketData", 1, 2, 2, PyTuple_GET_SIZE(__pyx_args)); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 303; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  __pyx_L3_error:;
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQryDepthMarketData", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_3ctp_10_TraderApi_9TraderApi_72ReqQryDepthMarketData(((struct __pyx_obj_3ctp_10_TraderApi_TraderApi *)__pyx_v_self), __pyx_v_pQryDepthMarketData, __pyx_v_nRequestID);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_72ReqQryDepthMarketData(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQryDepthMarketData, int __pyx_v_nRequestID) {
  size_t __pyx_v_address;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_t_1;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  size_t __pyx_t_4;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("ReqQryDepthMarketData", 0);
  __pyx_t_1 = ((__pyx_v_self->spi == NULL) != 0);
  if (__pyx_t_1) {
    __Pyx_XDECREF(__pyx_r);
    __pyx_r = Py_None; __Pyx_INCREF(Py_None);
    goto __pyx_L0;
  }
  __pyx_t_2 = PyTuple_New(1); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 306; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_v_pQryDepthMarketData);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_v_pQryDepthMarketData);
  __Pyx_GIVEREF(__pyx_v_pQryDepthMarketData);
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_addressof, __pyx_t_2, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 306; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_4 = __Pyx_PyInt_As_size_t(__pyx_t_3); if (unlikely((__pyx_t_4 == (size_t)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 306; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_v_address = __pyx_t_4;
  {
      #ifdef WITH_THREAD
      PyThreadState *_save;
      Py_UNBLOCK_THREADS
      #endif
      {
        __pyx_v_nRequestID = __pyx_v_self->api->ReqQryDepthMarketData(((struct CThostFtdcQryDepthMarketDataField *)__pyx_v_address), __pyx_v_nRequestID);
      }
      {
        {
          #ifdef WITH_THREAD
          Py_BLOCK_THREADS
          #endif
          goto __pyx_L6;
        }
        __pyx_L6:;
      }
  }
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_3 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 308; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_r = __pyx_t_3;
  __pyx_t_3 = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQryDepthMarketData", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_75ReqQrySettlementInfo(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds); 
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_75ReqQrySettlementInfo(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_pQrySettlementInfo = 0;
  int __pyx_v_nRequestID;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("ReqQrySettlementInfo (wrapper)", 0);
  {
    static PyObject **__pyx_pyargnames[] = {&__pyx_n_s_pQrySettlementInfo,&__pyx_n_s_nRequestID,0};
    PyObject* values[2] = {0,0};
    if (unlikely(__pyx_kwds)) {
      Py_ssize_t kw_args;
      const Py_ssize_t pos_args = PyTuple_GET_SIZE(__pyx_args);
      switch (pos_args) {
        case 2: values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
        case 1: values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
        case 0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      kw_args = PyDict_Size(__pyx_kwds);
      switch (pos_args) {
        case 0:
        if (likely((values[0] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_pQrySettlementInfo)) != 0)) kw_args--;
        else goto __pyx_L5_argtuple_error;
        case 1:
        if (likely((values[1] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_nRequestID)) != 0)) kw_args--;
        else {
          __Pyx_RaiseArgtupleInvalid("ReqQrySettlementInfo", 1, 2, 2, 1); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 310; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
        }
      }
      if (unlikely(kw_args > 0)) {
        if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_pyargnames, 0, values, pos_args, "ReqQrySettlementInfo") < 0)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 310; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
      }
    } else if (PyTuple_GET_SIZE(__pyx_args) != 2) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
      values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
    }
    __pyx_v_pQrySettlementInfo = values[0];
    __pyx_v_nRequestID = __Pyx_PyInt_As_int(values[1]); if (unlikely((__pyx_v_nRequestID == (int)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 310; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  }
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("ReqQrySettlementInfo", 1, 2, 2, PyTuple_GET_SIZE(__pyx_args)); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 310; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  __pyx_L3_error:;
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQrySettlementInfo", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_3ctp_10_TraderApi_9TraderApi_74ReqQrySettlementInfo(((struct __pyx_obj_3ctp_10_TraderApi_TraderApi *)__pyx_v_self), __pyx_v_pQrySettlementInfo, __pyx_v_nRequestID);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_74ReqQrySettlementInfo(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQrySettlementInfo, int __pyx_v_nRequestID) {
  size_t __pyx_v_address;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_t_1;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  size_t __pyx_t_4;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("ReqQrySettlementInfo", 0);
  __pyx_t_1 = ((__pyx_v_self->spi == NULL) != 0);
  if (__pyx_t_1) {
    __Pyx_XDECREF(__pyx_r);
    __pyx_r = Py_None; __Pyx_INCREF(Py_None);
    goto __pyx_L0;
  }
  __pyx_t_2 = PyTuple_New(1); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 313; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_v_pQrySettlementInfo);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_v_pQrySettlementInfo);
  __Pyx_GIVEREF(__pyx_v_pQrySettlementInfo);
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_addressof, __pyx_t_2, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 313; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_4 = __Pyx_PyInt_As_size_t(__pyx_t_3); if (unlikely((__pyx_t_4 == (size_t)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 313; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_v_address = __pyx_t_4;
  {
      #ifdef WITH_THREAD
      PyThreadState *_save;
      Py_UNBLOCK_THREADS
      #endif
      {
        __pyx_v_nRequestID = __pyx_v_self->api->ReqQrySettlementInfo(((struct CThostFtdcQrySettlementInfoField *)__pyx_v_address), __pyx_v_nRequestID);
      }
      {
        {
          #ifdef WITH_THREAD
          Py_BLOCK_THREADS
          #endif
          goto __pyx_L6;
        }
        __pyx_L6:;
      }
  }
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_3 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 315; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_r = __pyx_t_3;
  __pyx_t_3 = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQrySettlementInfo", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_77ReqQryTransferBank(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds); 
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_77ReqQryTransferBank(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_pQryTransferBank = 0;
  int __pyx_v_nRequestID;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("ReqQryTransferBank (wrapper)", 0);
  {
    static PyObject **__pyx_pyargnames[] = {&__pyx_n_s_pQryTransferBank,&__pyx_n_s_nRequestID,0};
    PyObject* values[2] = {0,0};
    if (unlikely(__pyx_kwds)) {
      Py_ssize_t kw_args;
      const Py_ssize_t pos_args = PyTuple_GET_SIZE(__pyx_args);
      switch (pos_args) {
        case 2: values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
        case 1: values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
        case 0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      kw_args = PyDict_Size(__pyx_kwds);
      switch (pos_args) {
        case 0:
        if (likely((values[0] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_pQryTransferBank)) != 0)) kw_args--;
        else goto __pyx_L5_argtuple_error;
        case 1:
        if (likely((values[1] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_nRequestID)) != 0)) kw_args--;
        else {
          __Pyx_RaiseArgtupleInvalid("ReqQryTransferBank", 1, 2, 2, 1); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 317; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
        }
      }
      if (unlikely(kw_args > 0)) {
        if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_pyargnames, 0, values, pos_args, "ReqQryTransferBank") < 0)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 317; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
      }
    } else if (PyTuple_GET_SIZE(__pyx_args) != 2) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
      values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
    }
    __pyx_v_pQryTransferBank = values[0];
    __pyx_v_nRequestID = __Pyx_PyInt_As_int(values[1]); if (unlikely((__pyx_v_nRequestID == (int)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 317; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  }
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("ReqQryTransferBank", 1, 2, 2, PyTuple_GET_SIZE(__pyx_args)); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 317; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  __pyx_L3_error:;
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQryTransferBank", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_3ctp_10_TraderApi_9TraderApi_76ReqQryTransferBank(((struct __pyx_obj_3ctp_10_TraderApi_TraderApi *)__pyx_v_self), __pyx_v_pQryTransferBank, __pyx_v_nRequestID);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_76ReqQryTransferBank(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQryTransferBank, int __pyx_v_nRequestID) {
  size_t __pyx_v_address;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_t_1;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  size_t __pyx_t_4;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("ReqQryTransferBank", 0);
  __pyx_t_1 = ((__pyx_v_self->spi == NULL) != 0);
  if (__pyx_t_1) {
    __Pyx_XDECREF(__pyx_r);
    __pyx_r = Py_None; __Pyx_INCREF(Py_None);
    goto __pyx_L0;
  }
  __pyx_t_2 = PyTuple_New(1); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 320; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_v_pQryTransferBank);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_v_pQryTransferBank);
  __Pyx_GIVEREF(__pyx_v_pQryTransferBank);
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_addressof, __pyx_t_2, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 320; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_4 = __Pyx_PyInt_As_size_t(__pyx_t_3); if (unlikely((__pyx_t_4 == (size_t)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 320; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_v_address = __pyx_t_4;
  {
      #ifdef WITH_THREAD
      PyThreadState *_save;
      Py_UNBLOCK_THREADS
      #endif
      {
        __pyx_v_nRequestID = __pyx_v_self->api->ReqQryTransferBank(((struct CThostFtdcQryTransferBankField *)__pyx_v_address), __pyx_v_nRequestID);
      }
      {
        {
          #ifdef WITH_THREAD
          Py_BLOCK_THREADS
          #endif
          goto __pyx_L6;
        }
        __pyx_L6:;
      }
  }
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_3 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 322; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_r = __pyx_t_3;
  __pyx_t_3 = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQryTransferBank", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_79ReqQryInvestorPositionDetail(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds); 
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_79ReqQryInvestorPositionDetail(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_pQryInvestorPositionDetail = 0;
  int __pyx_v_nRequestID;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("ReqQryInvestorPositionDetail (wrapper)", 0);
  {
    static PyObject **__pyx_pyargnames[] = {&__pyx_n_s_pQryInvestorPositionDetail,&__pyx_n_s_nRequestID,0};
    PyObject* values[2] = {0,0};
    if (unlikely(__pyx_kwds)) {
      Py_ssize_t kw_args;
      const Py_ssize_t pos_args = PyTuple_GET_SIZE(__pyx_args);
      switch (pos_args) {
        case 2: values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
        case 1: values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
        case 0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      kw_args = PyDict_Size(__pyx_kwds);
      switch (pos_args) {
        case 0:
        if (likely((values[0] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_pQryInvestorPositionDetail)) != 0)) kw_args--;
        else goto __pyx_L5_argtuple_error;
        case 1:
        if (likely((values[1] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_nRequestID)) != 0)) kw_args--;
        else {
          __Pyx_RaiseArgtupleInvalid("ReqQryInvestorPositionDetail", 1, 2, 2, 1); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 324; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
        }
      }
      if (unlikely(kw_args > 0)) {
        if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_pyargnames, 0, values, pos_args, "ReqQryInvestorPositionDetail") < 0)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 324; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
      }
    } else if (PyTuple_GET_SIZE(__pyx_args) != 2) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
      values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
    }
    __pyx_v_pQryInvestorPositionDetail = values[0];
    __pyx_v_nRequestID = __Pyx_PyInt_As_int(values[1]); if (unlikely((__pyx_v_nRequestID == (int)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 324; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  }
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("ReqQryInvestorPositionDetail", 1, 2, 2, PyTuple_GET_SIZE(__pyx_args)); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 324; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  __pyx_L3_error:;
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQryInvestorPositionDetail", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_3ctp_10_TraderApi_9TraderApi_78ReqQryInvestorPositionDetail(((struct __pyx_obj_3ctp_10_TraderApi_TraderApi *)__pyx_v_self), __pyx_v_pQryInvestorPositionDetail, __pyx_v_nRequestID);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_78ReqQryInvestorPositionDetail(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQryInvestorPositionDetail, int __pyx_v_nRequestID) {
  size_t __pyx_v_address;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_t_1;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  size_t __pyx_t_4;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("ReqQryInvestorPositionDetail", 0);
  __pyx_t_1 = ((__pyx_v_self->spi == NULL) != 0);
  if (__pyx_t_1) {
    __Pyx_XDECREF(__pyx_r);
    __pyx_r = Py_None; __Pyx_INCREF(Py_None);
    goto __pyx_L0;
  }
  __pyx_t_2 = PyTuple_New(1); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 327; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_v_pQryInvestorPositionDetail);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_v_pQryInvestorPositionDetail);
  __Pyx_GIVEREF(__pyx_v_pQryInvestorPositionDetail);
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_addressof, __pyx_t_2, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 327; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_4 = __Pyx_PyInt_As_size_t(__pyx_t_3); if (unlikely((__pyx_t_4 == (size_t)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 327; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_v_address = __pyx_t_4;
  {
      #ifdef WITH_THREAD
      PyThreadState *_save;
      Py_UNBLOCK_THREADS
      #endif
      {
        __pyx_v_nRequestID = __pyx_v_self->api->ReqQryInvestorPositionDetail(((struct CThostFtdcQryInvestorPositionDetailField *)__pyx_v_address), __pyx_v_nRequestID);
      }
      {
        {
          #ifdef WITH_THREAD
          Py_BLOCK_THREADS
          #endif
          goto __pyx_L6;
        }
        __pyx_L6:;
      }
  }
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_3 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 329; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_r = __pyx_t_3;
  __pyx_t_3 = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQryInvestorPositionDetail", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_81ReqQryNotice(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds); 
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_81ReqQryNotice(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_pQryNotice = 0;
  int __pyx_v_nRequestID;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("ReqQryNotice (wrapper)", 0);
  {
    static PyObject **__pyx_pyargnames[] = {&__pyx_n_s_pQryNotice,&__pyx_n_s_nRequestID,0};
    PyObject* values[2] = {0,0};
    if (unlikely(__pyx_kwds)) {
      Py_ssize_t kw_args;
      const Py_ssize_t pos_args = PyTuple_GET_SIZE(__pyx_args);
      switch (pos_args) {
        case 2: values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
        case 1: values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
        case 0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      kw_args = PyDict_Size(__pyx_kwds);
      switch (pos_args) {
        case 0:
        if (likely((values[0] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_pQryNotice)) != 0)) kw_args--;
        else goto __pyx_L5_argtuple_error;
        case 1:
        if (likely((values[1] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_nRequestID)) != 0)) kw_args--;
        else {
          __Pyx_RaiseArgtupleInvalid("ReqQryNotice", 1, 2, 2, 1); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 331; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
        }
      }
      if (unlikely(kw_args > 0)) {
        if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_pyargnames, 0, values, pos_args, "ReqQryNotice") < 0)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 331; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
      }
    } else if (PyTuple_GET_SIZE(__pyx_args) != 2) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
      values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
    }
    __pyx_v_pQryNotice = values[0];
    __pyx_v_nRequestID = __Pyx_PyInt_As_int(values[1]); if (unlikely((__pyx_v_nRequestID == (int)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 331; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  }
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("ReqQryNotice", 1, 2, 2, PyTuple_GET_SIZE(__pyx_args)); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 331; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  __pyx_L3_error:;
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQryNotice", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_3ctp_10_TraderApi_9TraderApi_80ReqQryNotice(((struct __pyx_obj_3ctp_10_TraderApi_TraderApi *)__pyx_v_self), __pyx_v_pQryNotice, __pyx_v_nRequestID);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_80ReqQryNotice(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQryNotice, int __pyx_v_nRequestID) {
  size_t __pyx_v_address;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_t_1;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  size_t __pyx_t_4;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("ReqQryNotice", 0);
  __pyx_t_1 = ((__pyx_v_self->spi == NULL) != 0);
  if (__pyx_t_1) {
    __Pyx_XDECREF(__pyx_r);
    __pyx_r = Py_None; __Pyx_INCREF(Py_None);
    goto __pyx_L0;
  }
  __pyx_t_2 = PyTuple_New(1); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 334; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_v_pQryNotice);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_v_pQryNotice);
  __Pyx_GIVEREF(__pyx_v_pQryNotice);
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_addressof, __pyx_t_2, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 334; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_4 = __Pyx_PyInt_As_size_t(__pyx_t_3); if (unlikely((__pyx_t_4 == (size_t)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 334; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_v_address = __pyx_t_4;
  {
      #ifdef WITH_THREAD
      PyThreadState *_save;
      Py_UNBLOCK_THREADS
      #endif
      {
        __pyx_v_nRequestID = __pyx_v_self->api->ReqQryNotice(((struct CThostFtdcQryNoticeField *)__pyx_v_address), __pyx_v_nRequestID);
      }
      {
        {
          #ifdef WITH_THREAD
          Py_BLOCK_THREADS
          #endif
          goto __pyx_L6;
        }
        __pyx_L6:;
      }
  }
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_3 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 336; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_r = __pyx_t_3;
  __pyx_t_3 = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQryNotice", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_83ReqQrySettlementInfoConfirm(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds); 
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_83ReqQrySettlementInfoConfirm(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_pQrySettlementInfoConfirm = 0;
  int __pyx_v_nRequestID;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("ReqQrySettlementInfoConfirm (wrapper)", 0);
  {
    static PyObject **__pyx_pyargnames[] = {&__pyx_n_s_pQrySettlementInfoConfirm,&__pyx_n_s_nRequestID,0};
    PyObject* values[2] = {0,0};
    if (unlikely(__pyx_kwds)) {
      Py_ssize_t kw_args;
      const Py_ssize_t pos_args = PyTuple_GET_SIZE(__pyx_args);
      switch (pos_args) {
        case 2: values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
        case 1: values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
        case 0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      kw_args = PyDict_Size(__pyx_kwds);
      switch (pos_args) {
        case 0:
        if (likely((values[0] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_pQrySettlementInfoConfirm)) != 0)) kw_args--;
        else goto __pyx_L5_argtuple_error;
        case 1:
        if (likely((values[1] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_nRequestID)) != 0)) kw_args--;
        else {
          __Pyx_RaiseArgtupleInvalid("ReqQrySettlementInfoConfirm", 1, 2, 2, 1); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 338; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
        }
      }
      if (unlikely(kw_args > 0)) {
        if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_pyargnames, 0, values, pos_args, "ReqQrySettlementInfoConfirm") < 0)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 338; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
      }
    } else if (PyTuple_GET_SIZE(__pyx_args) != 2) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
      values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
    }
    __pyx_v_pQrySettlementInfoConfirm = values[0];
    __pyx_v_nRequestID = __Pyx_PyInt_As_int(values[1]); if (unlikely((__pyx_v_nRequestID == (int)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 338; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  }
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("ReqQrySettlementInfoConfirm", 1, 2, 2, PyTuple_GET_SIZE(__pyx_args)); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 338; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  __pyx_L3_error:;
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQrySettlementInfoConfirm", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_3ctp_10_TraderApi_9TraderApi_82ReqQrySettlementInfoConfirm(((struct __pyx_obj_3ctp_10_TraderApi_TraderApi *)__pyx_v_self), __pyx_v_pQrySettlementInfoConfirm, __pyx_v_nRequestID);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_82ReqQrySettlementInfoConfirm(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQrySettlementInfoConfirm, int __pyx_v_nRequestID) {
  size_t __pyx_v_address;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_t_1;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  size_t __pyx_t_4;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("ReqQrySettlementInfoConfirm", 0);
  __pyx_t_1 = ((__pyx_v_self->spi == NULL) != 0);
  if (__pyx_t_1) {
    __Pyx_XDECREF(__pyx_r);
    __pyx_r = Py_None; __Pyx_INCREF(Py_None);
    goto __pyx_L0;
  }
  __pyx_t_2 = PyTuple_New(1); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 341; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_v_pQrySettlementInfoConfirm);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_v_pQrySettlementInfoConfirm);
  __Pyx_GIVEREF(__pyx_v_pQrySettlementInfoConfirm);
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_addressof, __pyx_t_2, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 341; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_4 = __Pyx_PyInt_As_size_t(__pyx_t_3); if (unlikely((__pyx_t_4 == (size_t)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 341; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_v_address = __pyx_t_4;
  {
      #ifdef WITH_THREAD
      PyThreadState *_save;
      Py_UNBLOCK_THREADS
      #endif
      {
        __pyx_v_nRequestID = __pyx_v_self->api->ReqQrySettlementInfoConfirm(((struct CThostFtdcQrySettlementInfoConfirmField *)__pyx_v_address), __pyx_v_nRequestID);
      }
      {
        {
          #ifdef WITH_THREAD
          Py_BLOCK_THREADS
          #endif
          goto __pyx_L6;
        }
        __pyx_L6:;
      }
  }
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_3 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 343; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_r = __pyx_t_3;
  __pyx_t_3 = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQrySettlementInfoConfirm", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_85ReqQryInvestorPositionCombineDetail(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds); 
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_85ReqQryInvestorPositionCombineDetail(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_pQryInvestorPositionCombineDetail = 0;
  int __pyx_v_nRequestID;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("ReqQryInvestorPositionCombineDetail (wrapper)", 0);
  {
    static PyObject **__pyx_pyargnames[] = {&__pyx_n_s_pQryInvestorPositionCombineDetai,&__pyx_n_s_nRequestID,0};
    PyObject* values[2] = {0,0};
    if (unlikely(__pyx_kwds)) {
      Py_ssize_t kw_args;
      const Py_ssize_t pos_args = PyTuple_GET_SIZE(__pyx_args);
      switch (pos_args) {
        case 2: values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
        case 1: values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
        case 0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      kw_args = PyDict_Size(__pyx_kwds);
      switch (pos_args) {
        case 0:
        if (likely((values[0] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_pQryInvestorPositionCombineDetai)) != 0)) kw_args--;
        else goto __pyx_L5_argtuple_error;
        case 1:
        if (likely((values[1] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_nRequestID)) != 0)) kw_args--;
        else {
          __Pyx_RaiseArgtupleInvalid("ReqQryInvestorPositionCombineDetail", 1, 2, 2, 1); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 345; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
        }
      }
      if (unlikely(kw_args > 0)) {
        if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_pyargnames, 0, values, pos_args, "ReqQryInvestorPositionCombineDetail") < 0)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 345; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
      }
    } else if (PyTuple_GET_SIZE(__pyx_args) != 2) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
      values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
    }
    __pyx_v_pQryInvestorPositionCombineDetail = values[0];
    __pyx_v_nRequestID = __Pyx_PyInt_As_int(values[1]); if (unlikely((__pyx_v_nRequestID == (int)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 345; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  }
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("ReqQryInvestorPositionCombineDetail", 1, 2, 2, PyTuple_GET_SIZE(__pyx_args)); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 345; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  __pyx_L3_error:;
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQryInvestorPositionCombineDetail", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_3ctp_10_TraderApi_9TraderApi_84ReqQryInvestorPositionCombineDetail(((struct __pyx_obj_3ctp_10_TraderApi_TraderApi *)__pyx_v_self), __pyx_v_pQryInvestorPositionCombineDetail, __pyx_v_nRequestID);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_84ReqQryInvestorPositionCombineDetail(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQryInvestorPositionCombineDetail, int __pyx_v_nRequestID) {
  size_t __pyx_v_address;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_t_1;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  size_t __pyx_t_4;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("ReqQryInvestorPositionCombineDetail", 0);
  __pyx_t_1 = ((__pyx_v_self->spi == NULL) != 0);
  if (__pyx_t_1) {
    __Pyx_XDECREF(__pyx_r);
    __pyx_r = Py_None; __Pyx_INCREF(Py_None);
    goto __pyx_L0;
  }
  __pyx_t_2 = PyTuple_New(1); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 348; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_v_pQryInvestorPositionCombineDetail);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_v_pQryInvestorPositionCombineDetail);
  __Pyx_GIVEREF(__pyx_v_pQryInvestorPositionCombineDetail);
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_addressof, __pyx_t_2, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 348; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_4 = __Pyx_PyInt_As_size_t(__pyx_t_3); if (unlikely((__pyx_t_4 == (size_t)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 348; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_v_address = __pyx_t_4;
  {
      #ifdef WITH_THREAD
      PyThreadState *_save;
      Py_UNBLOCK_THREADS
      #endif
      {
        __pyx_v_nRequestID = __pyx_v_self->api->ReqQryInvestorPositionCombineDetail(((struct CThostFtdcQryInvestorPositionCombineDetailField *)__pyx_v_address), __pyx_v_nRequestID);
      }
      {
        {
          #ifdef WITH_THREAD
          Py_BLOCK_THREADS
          #endif
          goto __pyx_L6;
        }
        __pyx_L6:;
      }
  }
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_3 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 350; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_r = __pyx_t_3;
  __pyx_t_3 = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQryInvestorPositionCombineDetail", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_87ReqQryCFMMCTradingAccountKey(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds); 
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_87ReqQryCFMMCTradingAccountKey(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_pQryCFMMCTradingAccountKey = 0;
  int __pyx_v_nRequestID;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("ReqQryCFMMCTradingAccountKey (wrapper)", 0);
  {
    static PyObject **__pyx_pyargnames[] = {&__pyx_n_s_pQryCFMMCTradingAccountKey,&__pyx_n_s_nRequestID,0};
    PyObject* values[2] = {0,0};
    if (unlikely(__pyx_kwds)) {
      Py_ssize_t kw_args;
      const Py_ssize_t pos_args = PyTuple_GET_SIZE(__pyx_args);
      switch (pos_args) {
        case 2: values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
        case 1: values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
        case 0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      kw_args = PyDict_Size(__pyx_kwds);
      switch (pos_args) {
        case 0:
        if (likely((values[0] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_pQryCFMMCTradingAccountKey)) != 0)) kw_args--;
        else goto __pyx_L5_argtuple_error;
        case 1:
        if (likely((values[1] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_nRequestID)) != 0)) kw_args--;
        else {
          __Pyx_RaiseArgtupleInvalid("ReqQryCFMMCTradingAccountKey", 1, 2, 2, 1); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 352; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
        }
      }
      if (unlikely(kw_args > 0)) {
        if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_pyargnames, 0, values, pos_args, "ReqQryCFMMCTradingAccountKey") < 0)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 352; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
      }
    } else if (PyTuple_GET_SIZE(__pyx_args) != 2) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
      values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
    }
    __pyx_v_pQryCFMMCTradingAccountKey = values[0];
    __pyx_v_nRequestID = __Pyx_PyInt_As_int(values[1]); if (unlikely((__pyx_v_nRequestID == (int)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 352; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  }
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("ReqQryCFMMCTradingAccountKey", 1, 2, 2, PyTuple_GET_SIZE(__pyx_args)); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 352; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  __pyx_L3_error:;
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQryCFMMCTradingAccountKey", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_3ctp_10_TraderApi_9TraderApi_86ReqQryCFMMCTradingAccountKey(((struct __pyx_obj_3ctp_10_TraderApi_TraderApi *)__pyx_v_self), __pyx_v_pQryCFMMCTradingAccountKey, __pyx_v_nRequestID);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_86ReqQryCFMMCTradingAccountKey(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQryCFMMCTradingAccountKey, int __pyx_v_nRequestID) {
  size_t __pyx_v_address;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_t_1;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  size_t __pyx_t_4;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("ReqQryCFMMCTradingAccountKey", 0);
  __pyx_t_1 = ((__pyx_v_self->spi == NULL) != 0);
  if (__pyx_t_1) {
    __Pyx_XDECREF(__pyx_r);
    __pyx_r = Py_None; __Pyx_INCREF(Py_None);
    goto __pyx_L0;
  }
  __pyx_t_2 = PyTuple_New(1); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 355; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_v_pQryCFMMCTradingAccountKey);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_v_pQryCFMMCTradingAccountKey);
  __Pyx_GIVEREF(__pyx_v_pQryCFMMCTradingAccountKey);
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_addressof, __pyx_t_2, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 355; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_4 = __Pyx_PyInt_As_size_t(__pyx_t_3); if (unlikely((__pyx_t_4 == (size_t)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 355; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_v_address = __pyx_t_4;
  {
      #ifdef WITH_THREAD
      PyThreadState *_save;
      Py_UNBLOCK_THREADS
      #endif
      {
        __pyx_v_nRequestID = __pyx_v_self->api->ReqQryCFMMCTradingAccountKey(((struct CThostFtdcQryCFMMCTradingAccountKeyField *)__pyx_v_address), __pyx_v_nRequestID);
      }
      {
        {
          #ifdef WITH_THREAD
          Py_BLOCK_THREADS
          #endif
          goto __pyx_L6;
        }
        __pyx_L6:;
      }
  }
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_3 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 357; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_r = __pyx_t_3;
  __pyx_t_3 = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQryCFMMCTradingAccountKey", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_89ReqQryEWarrantOffset(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds); 
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_89ReqQryEWarrantOffset(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_pQryEWarrantOffset = 0;
  int __pyx_v_nRequestID;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("ReqQryEWarrantOffset (wrapper)", 0);
  {
    static PyObject **__pyx_pyargnames[] = {&__pyx_n_s_pQryEWarrantOffset,&__pyx_n_s_nRequestID,0};
    PyObject* values[2] = {0,0};
    if (unlikely(__pyx_kwds)) {
      Py_ssize_t kw_args;
      const Py_ssize_t pos_args = PyTuple_GET_SIZE(__pyx_args);
      switch (pos_args) {
        case 2: values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
        case 1: values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
        case 0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      kw_args = PyDict_Size(__pyx_kwds);
      switch (pos_args) {
        case 0:
        if (likely((values[0] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_pQryEWarrantOffset)) != 0)) kw_args--;
        else goto __pyx_L5_argtuple_error;
        case 1:
        if (likely((values[1] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_nRequestID)) != 0)) kw_args--;
        else {
          __Pyx_RaiseArgtupleInvalid("ReqQryEWarrantOffset", 1, 2, 2, 1); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 359; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
        }
      }
      if (unlikely(kw_args > 0)) {
        if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_pyargnames, 0, values, pos_args, "ReqQryEWarrantOffset") < 0)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 359; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
      }
    } else if (PyTuple_GET_SIZE(__pyx_args) != 2) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
      values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
    }
    __pyx_v_pQryEWarrantOffset = values[0];
    __pyx_v_nRequestID = __Pyx_PyInt_As_int(values[1]); if (unlikely((__pyx_v_nRequestID == (int)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 359; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  }
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("ReqQryEWarrantOffset", 1, 2, 2, PyTuple_GET_SIZE(__pyx_args)); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 359; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  __pyx_L3_error:;
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQryEWarrantOffset", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_3ctp_10_TraderApi_9TraderApi_88ReqQryEWarrantOffset(((struct __pyx_obj_3ctp_10_TraderApi_TraderApi *)__pyx_v_self), __pyx_v_pQryEWarrantOffset, __pyx_v_nRequestID);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_88ReqQryEWarrantOffset(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQryEWarrantOffset, int __pyx_v_nRequestID) {
  size_t __pyx_v_address;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_t_1;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  size_t __pyx_t_4;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("ReqQryEWarrantOffset", 0);
  __pyx_t_1 = ((__pyx_v_self->spi == NULL) != 0);
  if (__pyx_t_1) {
    __Pyx_XDECREF(__pyx_r);
    __pyx_r = Py_None; __Pyx_INCREF(Py_None);
    goto __pyx_L0;
  }
  __pyx_t_2 = PyTuple_New(1); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 362; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_v_pQryEWarrantOffset);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_v_pQryEWarrantOffset);
  __Pyx_GIVEREF(__pyx_v_pQryEWarrantOffset);
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_addressof, __pyx_t_2, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 362; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_4 = __Pyx_PyInt_As_size_t(__pyx_t_3); if (unlikely((__pyx_t_4 == (size_t)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 362; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_v_address = __pyx_t_4;
  {
      #ifdef WITH_THREAD
      PyThreadState *_save;
      Py_UNBLOCK_THREADS
      #endif
      {
        __pyx_v_nRequestID = __pyx_v_self->api->ReqQryEWarrantOffset(((struct CThostFtdcQryEWarrantOffsetField *)__pyx_v_address), __pyx_v_nRequestID);
      }
      {
        {
          #ifdef WITH_THREAD
          Py_BLOCK_THREADS
          #endif
          goto __pyx_L6;
        }
        __pyx_L6:;
      }
  }
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_3 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 364; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_r = __pyx_t_3;
  __pyx_t_3 = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQryEWarrantOffset", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_91ReqQryInvestorProductGroupMargin(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds); 
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_91ReqQryInvestorProductGroupMargin(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_pQryInvestorProductGroupMargin = 0;
  int __pyx_v_nRequestID;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("ReqQryInvestorProductGroupMargin (wrapper)", 0);
  {
    static PyObject **__pyx_pyargnames[] = {&__pyx_n_s_pQryInvestorProductGroupMargin,&__pyx_n_s_nRequestID,0};
    PyObject* values[2] = {0,0};
    if (unlikely(__pyx_kwds)) {
      Py_ssize_t kw_args;
      const Py_ssize_t pos_args = PyTuple_GET_SIZE(__pyx_args);
      switch (pos_args) {
        case 2: values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
        case 1: values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
        case 0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      kw_args = PyDict_Size(__pyx_kwds);
      switch (pos_args) {
        case 0:
        if (likely((values[0] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_pQryInvestorProductGroupMargin)) != 0)) kw_args--;
        else goto __pyx_L5_argtuple_error;
        case 1:
        if (likely((values[1] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_nRequestID)) != 0)) kw_args--;
        else {
          __Pyx_RaiseArgtupleInvalid("ReqQryInvestorProductGroupMargin", 1, 2, 2, 1); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 366; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
        }
      }
      if (unlikely(kw_args > 0)) {
        if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_pyargnames, 0, values, pos_args, "ReqQryInvestorProductGroupMargin") < 0)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 366; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
      }
    } else if (PyTuple_GET_SIZE(__pyx_args) != 2) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
      values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
    }
    __pyx_v_pQryInvestorProductGroupMargin = values[0];
    __pyx_v_nRequestID = __Pyx_PyInt_As_int(values[1]); if (unlikely((__pyx_v_nRequestID == (int)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 366; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  }
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("ReqQryInvestorProductGroupMargin", 1, 2, 2, PyTuple_GET_SIZE(__pyx_args)); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 366; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  __pyx_L3_error:;
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQryInvestorProductGroupMargin", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_3ctp_10_TraderApi_9TraderApi_90ReqQryInvestorProductGroupMargin(((struct __pyx_obj_3ctp_10_TraderApi_TraderApi *)__pyx_v_self), __pyx_v_pQryInvestorProductGroupMargin, __pyx_v_nRequestID);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_90ReqQryInvestorProductGroupMargin(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQryInvestorProductGroupMargin, int __pyx_v_nRequestID) {
  size_t __pyx_v_address;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_t_1;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  size_t __pyx_t_4;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("ReqQryInvestorProductGroupMargin", 0);
  __pyx_t_1 = ((__pyx_v_self->spi == NULL) != 0);
  if (__pyx_t_1) {
    __Pyx_XDECREF(__pyx_r);
    __pyx_r = Py_None; __Pyx_INCREF(Py_None);
    goto __pyx_L0;
  }
  __pyx_t_2 = PyTuple_New(1); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 369; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_v_pQryInvestorProductGroupMargin);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_v_pQryInvestorProductGroupMargin);
  __Pyx_GIVEREF(__pyx_v_pQryInvestorProductGroupMargin);
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_addressof, __pyx_t_2, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 369; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_4 = __Pyx_PyInt_As_size_t(__pyx_t_3); if (unlikely((__pyx_t_4 == (size_t)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 369; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_v_address = __pyx_t_4;
  {
      #ifdef WITH_THREAD
      PyThreadState *_save;
      Py_UNBLOCK_THREADS
      #endif
      {
        __pyx_v_nRequestID = __pyx_v_self->api->ReqQryInvestorProductGroupMargin(((struct CThostFtdcQryInvestorProductGroupMarginField *)__pyx_v_address), __pyx_v_nRequestID);
      }
      {
        {
          #ifdef WITH_THREAD
          Py_BLOCK_THREADS
          #endif
          goto __pyx_L6;
        }
        __pyx_L6:;
      }
  }
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_3 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 371; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_r = __pyx_t_3;
  __pyx_t_3 = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQryInvestorProductGroupMargin", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_93ReqQryExchangeMarginRate(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds); 
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_93ReqQryExchangeMarginRate(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_pQryExchangeMarginRate = 0;
  int __pyx_v_nRequestID;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("ReqQryExchangeMarginRate (wrapper)", 0);
  {
    static PyObject **__pyx_pyargnames[] = {&__pyx_n_s_pQryExchangeMarginRate,&__pyx_n_s_nRequestID,0};
    PyObject* values[2] = {0,0};
    if (unlikely(__pyx_kwds)) {
      Py_ssize_t kw_args;
      const Py_ssize_t pos_args = PyTuple_GET_SIZE(__pyx_args);
      switch (pos_args) {
        case 2: values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
        case 1: values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
        case 0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      kw_args = PyDict_Size(__pyx_kwds);
      switch (pos_args) {
        case 0:
        if (likely((values[0] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_pQryExchangeMarginRate)) != 0)) kw_args--;
        else goto __pyx_L5_argtuple_error;
        case 1:
        if (likely((values[1] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_nRequestID)) != 0)) kw_args--;
        else {
          __Pyx_RaiseArgtupleInvalid("ReqQryExchangeMarginRate", 1, 2, 2, 1); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 373; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
        }
      }
      if (unlikely(kw_args > 0)) {
        if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_pyargnames, 0, values, pos_args, "ReqQryExchangeMarginRate") < 0)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 373; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
      }
    } else if (PyTuple_GET_SIZE(__pyx_args) != 2) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
      values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
    }
    __pyx_v_pQryExchangeMarginRate = values[0];
    __pyx_v_nRequestID = __Pyx_PyInt_As_int(values[1]); if (unlikely((__pyx_v_nRequestID == (int)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 373; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  }
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("ReqQryExchangeMarginRate", 1, 2, 2, PyTuple_GET_SIZE(__pyx_args)); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 373; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  __pyx_L3_error:;
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQryExchangeMarginRate", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_3ctp_10_TraderApi_9TraderApi_92ReqQryExchangeMarginRate(((struct __pyx_obj_3ctp_10_TraderApi_TraderApi *)__pyx_v_self), __pyx_v_pQryExchangeMarginRate, __pyx_v_nRequestID);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_92ReqQryExchangeMarginRate(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQryExchangeMarginRate, int __pyx_v_nRequestID) {
  size_t __pyx_v_address;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_t_1;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  size_t __pyx_t_4;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("ReqQryExchangeMarginRate", 0);
  __pyx_t_1 = ((__pyx_v_self->spi == NULL) != 0);
  if (__pyx_t_1) {
    __Pyx_XDECREF(__pyx_r);
    __pyx_r = Py_None; __Pyx_INCREF(Py_None);
    goto __pyx_L0;
  }
  __pyx_t_2 = PyTuple_New(1); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 376; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_v_pQryExchangeMarginRate);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_v_pQryExchangeMarginRate);
  __Pyx_GIVEREF(__pyx_v_pQryExchangeMarginRate);
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_addressof, __pyx_t_2, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 376; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_4 = __Pyx_PyInt_As_size_t(__pyx_t_3); if (unlikely((__pyx_t_4 == (size_t)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 376; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_v_address = __pyx_t_4;
  {
      #ifdef WITH_THREAD
      PyThreadState *_save;
      Py_UNBLOCK_THREADS
      #endif
      {
        __pyx_v_nRequestID = __pyx_v_self->api->ReqQryExchangeMarginRate(((struct CThostFtdcQryExchangeMarginRateField *)__pyx_v_address), __pyx_v_nRequestID);
      }
      {
        {
          #ifdef WITH_THREAD
          Py_BLOCK_THREADS
          #endif
          goto __pyx_L6;
        }
        __pyx_L6:;
      }
  }
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_3 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 378; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_r = __pyx_t_3;
  __pyx_t_3 = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQryExchangeMarginRate", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_95ReqQryExchangeMarginRateAdjust(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds); 
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_95ReqQryExchangeMarginRateAdjust(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_pQryExchangeMarginRateAdjust = 0;
  int __pyx_v_nRequestID;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("ReqQryExchangeMarginRateAdjust (wrapper)", 0);
  {
    static PyObject **__pyx_pyargnames[] = {&__pyx_n_s_pQryExchangeMarginRateAdjust,&__pyx_n_s_nRequestID,0};
    PyObject* values[2] = {0,0};
    if (unlikely(__pyx_kwds)) {
      Py_ssize_t kw_args;
      const Py_ssize_t pos_args = PyTuple_GET_SIZE(__pyx_args);
      switch (pos_args) {
        case 2: values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
        case 1: values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
        case 0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      kw_args = PyDict_Size(__pyx_kwds);
      switch (pos_args) {
        case 0:
        if (likely((values[0] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_pQryExchangeMarginRateAdjust)) != 0)) kw_args--;
        else goto __pyx_L5_argtuple_error;
        case 1:
        if (likely((values[1] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_nRequestID)) != 0)) kw_args--;
        else {
          __Pyx_RaiseArgtupleInvalid("ReqQryExchangeMarginRateAdjust", 1, 2, 2, 1); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 380; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
        }
      }
      if (unlikely(kw_args > 0)) {
        if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_pyargnames, 0, values, pos_args, "ReqQryExchangeMarginRateAdjust") < 0)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 380; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
      }
    } else if (PyTuple_GET_SIZE(__pyx_args) != 2) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
      values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
    }
    __pyx_v_pQryExchangeMarginRateAdjust = values[0];
    __pyx_v_nRequestID = __Pyx_PyInt_As_int(values[1]); if (unlikely((__pyx_v_nRequestID == (int)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 380; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  }
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("ReqQryExchangeMarginRateAdjust", 1, 2, 2, PyTuple_GET_SIZE(__pyx_args)); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 380; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  __pyx_L3_error:;
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQryExchangeMarginRateAdjust", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_3ctp_10_TraderApi_9TraderApi_94ReqQryExchangeMarginRateAdjust(((struct __pyx_obj_3ctp_10_TraderApi_TraderApi *)__pyx_v_self), __pyx_v_pQryExchangeMarginRateAdjust, __pyx_v_nRequestID);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_94ReqQryExchangeMarginRateAdjust(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQryExchangeMarginRateAdjust, int __pyx_v_nRequestID) {
  size_t __pyx_v_address;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_t_1;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  size_t __pyx_t_4;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("ReqQryExchangeMarginRateAdjust", 0);
  __pyx_t_1 = ((__pyx_v_self->spi == NULL) != 0);
  if (__pyx_t_1) {
    __Pyx_XDECREF(__pyx_r);
    __pyx_r = Py_None; __Pyx_INCREF(Py_None);
    goto __pyx_L0;
  }
  __pyx_t_2 = PyTuple_New(1); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 383; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_v_pQryExchangeMarginRateAdjust);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_v_pQryExchangeMarginRateAdjust);
  __Pyx_GIVEREF(__pyx_v_pQryExchangeMarginRateAdjust);
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_addressof, __pyx_t_2, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 383; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_4 = __Pyx_PyInt_As_size_t(__pyx_t_3); if (unlikely((__pyx_t_4 == (size_t)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 383; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_v_address = __pyx_t_4;
  {
      #ifdef WITH_THREAD
      PyThreadState *_save;
      Py_UNBLOCK_THREADS
      #endif
      {
        __pyx_v_nRequestID = __pyx_v_self->api->ReqQryExchangeMarginRateAdjust(((struct CThostFtdcQryExchangeMarginRateAdjustField *)__pyx_v_address), __pyx_v_nRequestID);
      }
      {
        {
          #ifdef WITH_THREAD
          Py_BLOCK_THREADS
          #endif
          goto __pyx_L6;
        }
        __pyx_L6:;
      }
  }
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_3 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 385; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_r = __pyx_t_3;
  __pyx_t_3 = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQryExchangeMarginRateAdjust", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_97ReqQryExchangeRate(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds); 
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_97ReqQryExchangeRate(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_pQryExchangeRate = 0;
  int __pyx_v_nRequestID;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("ReqQryExchangeRate (wrapper)", 0);
  {
    static PyObject **__pyx_pyargnames[] = {&__pyx_n_s_pQryExchangeRate,&__pyx_n_s_nRequestID,0};
    PyObject* values[2] = {0,0};
    if (unlikely(__pyx_kwds)) {
      Py_ssize_t kw_args;
      const Py_ssize_t pos_args = PyTuple_GET_SIZE(__pyx_args);
      switch (pos_args) {
        case 2: values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
        case 1: values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
        case 0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      kw_args = PyDict_Size(__pyx_kwds);
      switch (pos_args) {
        case 0:
        if (likely((values[0] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_pQryExchangeRate)) != 0)) kw_args--;
        else goto __pyx_L5_argtuple_error;
        case 1:
        if (likely((values[1] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_nRequestID)) != 0)) kw_args--;
        else {
          __Pyx_RaiseArgtupleInvalid("ReqQryExchangeRate", 1, 2, 2, 1); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 387; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
        }
      }
      if (unlikely(kw_args > 0)) {
        if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_pyargnames, 0, values, pos_args, "ReqQryExchangeRate") < 0)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 387; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
      }
    } else if (PyTuple_GET_SIZE(__pyx_args) != 2) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
      values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
    }
    __pyx_v_pQryExchangeRate = values[0];
    __pyx_v_nRequestID = __Pyx_PyInt_As_int(values[1]); if (unlikely((__pyx_v_nRequestID == (int)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 387; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  }
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("ReqQryExchangeRate", 1, 2, 2, PyTuple_GET_SIZE(__pyx_args)); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 387; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  __pyx_L3_error:;
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQryExchangeRate", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_3ctp_10_TraderApi_9TraderApi_96ReqQryExchangeRate(((struct __pyx_obj_3ctp_10_TraderApi_TraderApi *)__pyx_v_self), __pyx_v_pQryExchangeRate, __pyx_v_nRequestID);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_96ReqQryExchangeRate(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQryExchangeRate, int __pyx_v_nRequestID) {
  size_t __pyx_v_address;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_t_1;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  size_t __pyx_t_4;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("ReqQryExchangeRate", 0);
  __pyx_t_1 = ((__pyx_v_self->spi == NULL) != 0);
  if (__pyx_t_1) {
    __Pyx_XDECREF(__pyx_r);
    __pyx_r = Py_None; __Pyx_INCREF(Py_None);
    goto __pyx_L0;
  }
  __pyx_t_2 = PyTuple_New(1); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 390; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_v_pQryExchangeRate);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_v_pQryExchangeRate);
  __Pyx_GIVEREF(__pyx_v_pQryExchangeRate);
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_addressof, __pyx_t_2, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 390; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_4 = __Pyx_PyInt_As_size_t(__pyx_t_3); if (unlikely((__pyx_t_4 == (size_t)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 390; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_v_address = __pyx_t_4;
  {
      #ifdef WITH_THREAD
      PyThreadState *_save;
      Py_UNBLOCK_THREADS
      #endif
      {
        __pyx_v_nRequestID = __pyx_v_self->api->ReqQryExchangeRate(((struct CThostFtdcQryExchangeRateField *)__pyx_v_address), __pyx_v_nRequestID);
      }
      {
        {
          #ifdef WITH_THREAD
          Py_BLOCK_THREADS
          #endif
          goto __pyx_L6;
        }
        __pyx_L6:;
      }
  }
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_3 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 392; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_r = __pyx_t_3;
  __pyx_t_3 = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQryExchangeRate", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_99ReqQrySecAgentACIDMap(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds); 
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_99ReqQrySecAgentACIDMap(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_pQrySecAgentACIDMap = 0;
  int __pyx_v_nRequestID;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("ReqQrySecAgentACIDMap (wrapper)", 0);
  {
    static PyObject **__pyx_pyargnames[] = {&__pyx_n_s_pQrySecAgentACIDMap,&__pyx_n_s_nRequestID,0};
    PyObject* values[2] = {0,0};
    if (unlikely(__pyx_kwds)) {
      Py_ssize_t kw_args;
      const Py_ssize_t pos_args = PyTuple_GET_SIZE(__pyx_args);
      switch (pos_args) {
        case 2: values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
        case 1: values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
        case 0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      kw_args = PyDict_Size(__pyx_kwds);
      switch (pos_args) {
        case 0:
        if (likely((values[0] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_pQrySecAgentACIDMap)) != 0)) kw_args--;
        else goto __pyx_L5_argtuple_error;
        case 1:
        if (likely((values[1] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_nRequestID)) != 0)) kw_args--;
        else {
          __Pyx_RaiseArgtupleInvalid("ReqQrySecAgentACIDMap", 1, 2, 2, 1); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 394; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
        }
      }
      if (unlikely(kw_args > 0)) {
        if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_pyargnames, 0, values, pos_args, "ReqQrySecAgentACIDMap") < 0)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 394; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
      }
    } else if (PyTuple_GET_SIZE(__pyx_args) != 2) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
      values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
    }
    __pyx_v_pQrySecAgentACIDMap = values[0];
    __pyx_v_nRequestID = __Pyx_PyInt_As_int(values[1]); if (unlikely((__pyx_v_nRequestID == (int)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 394; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  }
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("ReqQrySecAgentACIDMap", 1, 2, 2, PyTuple_GET_SIZE(__pyx_args)); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 394; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  __pyx_L3_error:;
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQrySecAgentACIDMap", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_3ctp_10_TraderApi_9TraderApi_98ReqQrySecAgentACIDMap(((struct __pyx_obj_3ctp_10_TraderApi_TraderApi *)__pyx_v_self), __pyx_v_pQrySecAgentACIDMap, __pyx_v_nRequestID);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_98ReqQrySecAgentACIDMap(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQrySecAgentACIDMap, int __pyx_v_nRequestID) {
  size_t __pyx_v_address;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_t_1;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  size_t __pyx_t_4;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("ReqQrySecAgentACIDMap", 0);
  __pyx_t_1 = ((__pyx_v_self->spi == NULL) != 0);
  if (__pyx_t_1) {
    __Pyx_XDECREF(__pyx_r);
    __pyx_r = Py_None; __Pyx_INCREF(Py_None);
    goto __pyx_L0;
  }
  __pyx_t_2 = PyTuple_New(1); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 397; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_v_pQrySecAgentACIDMap);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_v_pQrySecAgentACIDMap);
  __Pyx_GIVEREF(__pyx_v_pQrySecAgentACIDMap);
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_addressof, __pyx_t_2, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 397; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_4 = __Pyx_PyInt_As_size_t(__pyx_t_3); if (unlikely((__pyx_t_4 == (size_t)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 397; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_v_address = __pyx_t_4;
  {
      #ifdef WITH_THREAD
      PyThreadState *_save;
      Py_UNBLOCK_THREADS
      #endif
      {
        __pyx_v_nRequestID = __pyx_v_self->api->ReqQrySecAgentACIDMap(((struct CThostFtdcQrySecAgentACIDMapField *)__pyx_v_address), __pyx_v_nRequestID);
      }
      {
        {
          #ifdef WITH_THREAD
          Py_BLOCK_THREADS
          #endif
          goto __pyx_L6;
        }
        __pyx_L6:;
      }
  }
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_3 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 399; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_r = __pyx_t_3;
  __pyx_t_3 = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQrySecAgentACIDMap", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_101ReqQryTransferSerial(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds); 
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_101ReqQryTransferSerial(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_pQryTransferSerial = 0;
  int __pyx_v_nRequestID;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("ReqQryTransferSerial (wrapper)", 0);
  {
    static PyObject **__pyx_pyargnames[] = {&__pyx_n_s_pQryTransferSerial,&__pyx_n_s_nRequestID,0};
    PyObject* values[2] = {0,0};
    if (unlikely(__pyx_kwds)) {
      Py_ssize_t kw_args;
      const Py_ssize_t pos_args = PyTuple_GET_SIZE(__pyx_args);
      switch (pos_args) {
        case 2: values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
        case 1: values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
        case 0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      kw_args = PyDict_Size(__pyx_kwds);
      switch (pos_args) {
        case 0:
        if (likely((values[0] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_pQryTransferSerial)) != 0)) kw_args--;
        else goto __pyx_L5_argtuple_error;
        case 1:
        if (likely((values[1] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_nRequestID)) != 0)) kw_args--;
        else {
          __Pyx_RaiseArgtupleInvalid("ReqQryTransferSerial", 1, 2, 2, 1); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 401; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
        }
      }
      if (unlikely(kw_args > 0)) {
        if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_pyargnames, 0, values, pos_args, "ReqQryTransferSerial") < 0)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 401; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
      }
    } else if (PyTuple_GET_SIZE(__pyx_args) != 2) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
      values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
    }
    __pyx_v_pQryTransferSerial = values[0];
    __pyx_v_nRequestID = __Pyx_PyInt_As_int(values[1]); if (unlikely((__pyx_v_nRequestID == (int)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 401; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  }
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("ReqQryTransferSerial", 1, 2, 2, PyTuple_GET_SIZE(__pyx_args)); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 401; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  __pyx_L3_error:;
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQryTransferSerial", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_3ctp_10_TraderApi_9TraderApi_100ReqQryTransferSerial(((struct __pyx_obj_3ctp_10_TraderApi_TraderApi *)__pyx_v_self), __pyx_v_pQryTransferSerial, __pyx_v_nRequestID);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_100ReqQryTransferSerial(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQryTransferSerial, int __pyx_v_nRequestID) {
  size_t __pyx_v_address;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_t_1;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  size_t __pyx_t_4;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("ReqQryTransferSerial", 0);
  __pyx_t_1 = ((__pyx_v_self->spi == NULL) != 0);
  if (__pyx_t_1) {
    __Pyx_XDECREF(__pyx_r);
    __pyx_r = Py_None; __Pyx_INCREF(Py_None);
    goto __pyx_L0;
  }
  __pyx_t_2 = PyTuple_New(1); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 404; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_v_pQryTransferSerial);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_v_pQryTransferSerial);
  __Pyx_GIVEREF(__pyx_v_pQryTransferSerial);
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_addressof, __pyx_t_2, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 404; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_4 = __Pyx_PyInt_As_size_t(__pyx_t_3); if (unlikely((__pyx_t_4 == (size_t)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 404; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_v_address = __pyx_t_4;
  {
      #ifdef WITH_THREAD
      PyThreadState *_save;
      Py_UNBLOCK_THREADS
      #endif
      {
        __pyx_v_nRequestID = __pyx_v_self->api->ReqQryTransferSerial(((struct CThostFtdcQryTransferSerialField *)__pyx_v_address), __pyx_v_nRequestID);
      }
      {
        {
          #ifdef WITH_THREAD
          Py_BLOCK_THREADS
          #endif
          goto __pyx_L6;
        }
        __pyx_L6:;
      }
  }
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_3 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 406; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_r = __pyx_t_3;
  __pyx_t_3 = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQryTransferSerial", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_103ReqQryAccountregister(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds); 
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_103ReqQryAccountregister(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_pQryAccountregister = 0;
  int __pyx_v_nRequestID;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("ReqQryAccountregister (wrapper)", 0);
  {
    static PyObject **__pyx_pyargnames[] = {&__pyx_n_s_pQryAccountregister,&__pyx_n_s_nRequestID,0};
    PyObject* values[2] = {0,0};
    if (unlikely(__pyx_kwds)) {
      Py_ssize_t kw_args;
      const Py_ssize_t pos_args = PyTuple_GET_SIZE(__pyx_args);
      switch (pos_args) {
        case 2: values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
        case 1: values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
        case 0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      kw_args = PyDict_Size(__pyx_kwds);
      switch (pos_args) {
        case 0:
        if (likely((values[0] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_pQryAccountregister)) != 0)) kw_args--;
        else goto __pyx_L5_argtuple_error;
        case 1:
        if (likely((values[1] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_nRequestID)) != 0)) kw_args--;
        else {
          __Pyx_RaiseArgtupleInvalid("ReqQryAccountregister", 1, 2, 2, 1); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 408; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
        }
      }
      if (unlikely(kw_args > 0)) {
        if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_pyargnames, 0, values, pos_args, "ReqQryAccountregister") < 0)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 408; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
      }
    } else if (PyTuple_GET_SIZE(__pyx_args) != 2) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
      values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
    }
    __pyx_v_pQryAccountregister = values[0];
    __pyx_v_nRequestID = __Pyx_PyInt_As_int(values[1]); if (unlikely((__pyx_v_nRequestID == (int)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 408; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  }
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("ReqQryAccountregister", 1, 2, 2, PyTuple_GET_SIZE(__pyx_args)); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 408; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  __pyx_L3_error:;
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQryAccountregister", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_3ctp_10_TraderApi_9TraderApi_102ReqQryAccountregister(((struct __pyx_obj_3ctp_10_TraderApi_TraderApi *)__pyx_v_self), __pyx_v_pQryAccountregister, __pyx_v_nRequestID);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_102ReqQryAccountregister(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQryAccountregister, int __pyx_v_nRequestID) {
  size_t __pyx_v_address;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_t_1;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  size_t __pyx_t_4;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("ReqQryAccountregister", 0);
  __pyx_t_1 = ((__pyx_v_self->spi == NULL) != 0);
  if (__pyx_t_1) {
    __Pyx_XDECREF(__pyx_r);
    __pyx_r = Py_None; __Pyx_INCREF(Py_None);
    goto __pyx_L0;
  }
  __pyx_t_2 = PyTuple_New(1); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 411; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_v_pQryAccountregister);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_v_pQryAccountregister);
  __Pyx_GIVEREF(__pyx_v_pQryAccountregister);
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_addressof, __pyx_t_2, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 411; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_4 = __Pyx_PyInt_As_size_t(__pyx_t_3); if (unlikely((__pyx_t_4 == (size_t)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 411; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_v_address = __pyx_t_4;
  {
      #ifdef WITH_THREAD
      PyThreadState *_save;
      Py_UNBLOCK_THREADS
      #endif
      {
        __pyx_v_nRequestID = __pyx_v_self->api->ReqQryAccountregister(((struct CThostFtdcQryAccountregisterField *)__pyx_v_address), __pyx_v_nRequestID);
      }
      {
        {
          #ifdef WITH_THREAD
          Py_BLOCK_THREADS
          #endif
          goto __pyx_L6;
        }
        __pyx_L6:;
      }
  }
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_3 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 413; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_r = __pyx_t_3;
  __pyx_t_3 = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQryAccountregister", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_105ReqQryContractBank(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds); 
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_105ReqQryContractBank(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_pQryContractBank = 0;
  int __pyx_v_nRequestID;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("ReqQryContractBank (wrapper)", 0);
  {
    static PyObject **__pyx_pyargnames[] = {&__pyx_n_s_pQryContractBank,&__pyx_n_s_nRequestID,0};
    PyObject* values[2] = {0,0};
    if (unlikely(__pyx_kwds)) {
      Py_ssize_t kw_args;
      const Py_ssize_t pos_args = PyTuple_GET_SIZE(__pyx_args);
      switch (pos_args) {
        case 2: values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
        case 1: values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
        case 0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      kw_args = PyDict_Size(__pyx_kwds);
      switch (pos_args) {
        case 0:
        if (likely((values[0] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_pQryContractBank)) != 0)) kw_args--;
        else goto __pyx_L5_argtuple_error;
        case 1:
        if (likely((values[1] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_nRequestID)) != 0)) kw_args--;
        else {
          __Pyx_RaiseArgtupleInvalid("ReqQryContractBank", 1, 2, 2, 1); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 415; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
        }
      }
      if (unlikely(kw_args > 0)) {
        if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_pyargnames, 0, values, pos_args, "ReqQryContractBank") < 0)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 415; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
      }
    } else if (PyTuple_GET_SIZE(__pyx_args) != 2) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
      values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
    }
    __pyx_v_pQryContractBank = values[0];
    __pyx_v_nRequestID = __Pyx_PyInt_As_int(values[1]); if (unlikely((__pyx_v_nRequestID == (int)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 415; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  }
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("ReqQryContractBank", 1, 2, 2, PyTuple_GET_SIZE(__pyx_args)); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 415; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  __pyx_L3_error:;
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQryContractBank", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_3ctp_10_TraderApi_9TraderApi_104ReqQryContractBank(((struct __pyx_obj_3ctp_10_TraderApi_TraderApi *)__pyx_v_self), __pyx_v_pQryContractBank, __pyx_v_nRequestID);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_104ReqQryContractBank(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQryContractBank, int __pyx_v_nRequestID) {
  size_t __pyx_v_address;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_t_1;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  size_t __pyx_t_4;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("ReqQryContractBank", 0);
  __pyx_t_1 = ((__pyx_v_self->spi == NULL) != 0);
  if (__pyx_t_1) {
    __Pyx_XDECREF(__pyx_r);
    __pyx_r = Py_None; __Pyx_INCREF(Py_None);
    goto __pyx_L0;
  }
  __pyx_t_2 = PyTuple_New(1); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 418; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_v_pQryContractBank);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_v_pQryContractBank);
  __Pyx_GIVEREF(__pyx_v_pQryContractBank);
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_addressof, __pyx_t_2, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 418; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_4 = __Pyx_PyInt_As_size_t(__pyx_t_3); if (unlikely((__pyx_t_4 == (size_t)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 418; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_v_address = __pyx_t_4;
  {
      #ifdef WITH_THREAD
      PyThreadState *_save;
      Py_UNBLOCK_THREADS
      #endif
      {
        __pyx_v_nRequestID = __pyx_v_self->api->ReqQryContractBank(((struct CThostFtdcQryContractBankField *)__pyx_v_address), __pyx_v_nRequestID);
      }
      {
        {
          #ifdef WITH_THREAD
          Py_BLOCK_THREADS
          #endif
          goto __pyx_L6;
        }
        __pyx_L6:;
      }
  }
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_3 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 420; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_r = __pyx_t_3;
  __pyx_t_3 = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQryContractBank", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_107ReqQryParkedOrder(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds); 
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_107ReqQryParkedOrder(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_pQryParkedOrder = 0;
  int __pyx_v_nRequestID;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("ReqQryParkedOrder (wrapper)", 0);
  {
    static PyObject **__pyx_pyargnames[] = {&__pyx_n_s_pQryParkedOrder,&__pyx_n_s_nRequestID,0};
    PyObject* values[2] = {0,0};
    if (unlikely(__pyx_kwds)) {
      Py_ssize_t kw_args;
      const Py_ssize_t pos_args = PyTuple_GET_SIZE(__pyx_args);
      switch (pos_args) {
        case 2: values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
        case 1: values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
        case 0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      kw_args = PyDict_Size(__pyx_kwds);
      switch (pos_args) {
        case 0:
        if (likely((values[0] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_pQryParkedOrder)) != 0)) kw_args--;
        else goto __pyx_L5_argtuple_error;
        case 1:
        if (likely((values[1] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_nRequestID)) != 0)) kw_args--;
        else {
          __Pyx_RaiseArgtupleInvalid("ReqQryParkedOrder", 1, 2, 2, 1); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 422; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
        }
      }
      if (unlikely(kw_args > 0)) {
        if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_pyargnames, 0, values, pos_args, "ReqQryParkedOrder") < 0)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 422; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
      }
    } else if (PyTuple_GET_SIZE(__pyx_args) != 2) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
      values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
    }
    __pyx_v_pQryParkedOrder = values[0];
    __pyx_v_nRequestID = __Pyx_PyInt_As_int(values[1]); if (unlikely((__pyx_v_nRequestID == (int)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 422; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  }
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("ReqQryParkedOrder", 1, 2, 2, PyTuple_GET_SIZE(__pyx_args)); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 422; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  __pyx_L3_error:;
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQryParkedOrder", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_3ctp_10_TraderApi_9TraderApi_106ReqQryParkedOrder(((struct __pyx_obj_3ctp_10_TraderApi_TraderApi *)__pyx_v_self), __pyx_v_pQryParkedOrder, __pyx_v_nRequestID);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_106ReqQryParkedOrder(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQryParkedOrder, int __pyx_v_nRequestID) {
  size_t __pyx_v_address;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_t_1;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  size_t __pyx_t_4;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("ReqQryParkedOrder", 0);
  __pyx_t_1 = ((__pyx_v_self->spi == NULL) != 0);
  if (__pyx_t_1) {
    __Pyx_XDECREF(__pyx_r);
    __pyx_r = Py_None; __Pyx_INCREF(Py_None);
    goto __pyx_L0;
  }
  __pyx_t_2 = PyTuple_New(1); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 425; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_v_pQryParkedOrder);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_v_pQryParkedOrder);
  __Pyx_GIVEREF(__pyx_v_pQryParkedOrder);
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_addressof, __pyx_t_2, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 425; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_4 = __Pyx_PyInt_As_size_t(__pyx_t_3); if (unlikely((__pyx_t_4 == (size_t)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 425; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_v_address = __pyx_t_4;
  {
      #ifdef WITH_THREAD
      PyThreadState *_save;
      Py_UNBLOCK_THREADS
      #endif
      {
        __pyx_v_nRequestID = __pyx_v_self->api->ReqQryParkedOrder(((struct CThostFtdcQryParkedOrderField *)__pyx_v_address), __pyx_v_nRequestID);
      }
      {
        {
          #ifdef WITH_THREAD
          Py_BLOCK_THREADS
          #endif
          goto __pyx_L6;
        }
        __pyx_L6:;
      }
  }
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_3 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 427; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_r = __pyx_t_3;
  __pyx_t_3 = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQryParkedOrder", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_109ReqQryParkedOrderAction(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds); 
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_109ReqQryParkedOrderAction(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_pQryParkedOrderAction = 0;
  int __pyx_v_nRequestID;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("ReqQryParkedOrderAction (wrapper)", 0);
  {
    static PyObject **__pyx_pyargnames[] = {&__pyx_n_s_pQryParkedOrderAction,&__pyx_n_s_nRequestID,0};
    PyObject* values[2] = {0,0};
    if (unlikely(__pyx_kwds)) {
      Py_ssize_t kw_args;
      const Py_ssize_t pos_args = PyTuple_GET_SIZE(__pyx_args);
      switch (pos_args) {
        case 2: values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
        case 1: values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
        case 0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      kw_args = PyDict_Size(__pyx_kwds);
      switch (pos_args) {
        case 0:
        if (likely((values[0] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_pQryParkedOrderAction)) != 0)) kw_args--;
        else goto __pyx_L5_argtuple_error;
        case 1:
        if (likely((values[1] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_nRequestID)) != 0)) kw_args--;
        else {
          __Pyx_RaiseArgtupleInvalid("ReqQryParkedOrderAction", 1, 2, 2, 1); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 429; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
        }
      }
      if (unlikely(kw_args > 0)) {
        if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_pyargnames, 0, values, pos_args, "ReqQryParkedOrderAction") < 0)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 429; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
      }
    } else if (PyTuple_GET_SIZE(__pyx_args) != 2) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
      values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
    }
    __pyx_v_pQryParkedOrderAction = values[0];
    __pyx_v_nRequestID = __Pyx_PyInt_As_int(values[1]); if (unlikely((__pyx_v_nRequestID == (int)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 429; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  }
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("ReqQryParkedOrderAction", 1, 2, 2, PyTuple_GET_SIZE(__pyx_args)); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 429; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  __pyx_L3_error:;
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQryParkedOrderAction", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_3ctp_10_TraderApi_9TraderApi_108ReqQryParkedOrderAction(((struct __pyx_obj_3ctp_10_TraderApi_TraderApi *)__pyx_v_self), __pyx_v_pQryParkedOrderAction, __pyx_v_nRequestID);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_108ReqQryParkedOrderAction(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQryParkedOrderAction, int __pyx_v_nRequestID) {
  size_t __pyx_v_address;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_t_1;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  size_t __pyx_t_4;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("ReqQryParkedOrderAction", 0);
  __pyx_t_1 = ((__pyx_v_self->spi == NULL) != 0);
  if (__pyx_t_1) {
    __Pyx_XDECREF(__pyx_r);
    __pyx_r = Py_None; __Pyx_INCREF(Py_None);
    goto __pyx_L0;
  }
  __pyx_t_2 = PyTuple_New(1); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 432; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_v_pQryParkedOrderAction);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_v_pQryParkedOrderAction);
  __Pyx_GIVEREF(__pyx_v_pQryParkedOrderAction);
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_addressof, __pyx_t_2, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 432; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_4 = __Pyx_PyInt_As_size_t(__pyx_t_3); if (unlikely((__pyx_t_4 == (size_t)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 432; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_v_address = __pyx_t_4;
  {
      #ifdef WITH_THREAD
      PyThreadState *_save;
      Py_UNBLOCK_THREADS
      #endif
      {
        __pyx_v_nRequestID = __pyx_v_self->api->ReqQryParkedOrderAction(((struct CThostFtdcQryParkedOrderActionField *)__pyx_v_address), __pyx_v_nRequestID);
      }
      {
        {
          #ifdef WITH_THREAD
          Py_BLOCK_THREADS
          #endif
          goto __pyx_L6;
        }
        __pyx_L6:;
      }
  }
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_3 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 434; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_r = __pyx_t_3;
  __pyx_t_3 = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQryParkedOrderAction", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_111ReqQryTradingNotice(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds); 
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_111ReqQryTradingNotice(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_pQryTradingNotice = 0;
  int __pyx_v_nRequestID;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("ReqQryTradingNotice (wrapper)", 0);
  {
    static PyObject **__pyx_pyargnames[] = {&__pyx_n_s_pQryTradingNotice,&__pyx_n_s_nRequestID,0};
    PyObject* values[2] = {0,0};
    if (unlikely(__pyx_kwds)) {
      Py_ssize_t kw_args;
      const Py_ssize_t pos_args = PyTuple_GET_SIZE(__pyx_args);
      switch (pos_args) {
        case 2: values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
        case 1: values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
        case 0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      kw_args = PyDict_Size(__pyx_kwds);
      switch (pos_args) {
        case 0:
        if (likely((values[0] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_pQryTradingNotice)) != 0)) kw_args--;
        else goto __pyx_L5_argtuple_error;
        case 1:
        if (likely((values[1] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_nRequestID)) != 0)) kw_args--;
        else {
          __Pyx_RaiseArgtupleInvalid("ReqQryTradingNotice", 1, 2, 2, 1); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 436; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
        }
      }
      if (unlikely(kw_args > 0)) {
        if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_pyargnames, 0, values, pos_args, "ReqQryTradingNotice") < 0)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 436; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
      }
    } else if (PyTuple_GET_SIZE(__pyx_args) != 2) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
      values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
    }
    __pyx_v_pQryTradingNotice = values[0];
    __pyx_v_nRequestID = __Pyx_PyInt_As_int(values[1]); if (unlikely((__pyx_v_nRequestID == (int)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 436; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  }
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("ReqQryTradingNotice", 1, 2, 2, PyTuple_GET_SIZE(__pyx_args)); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 436; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  __pyx_L3_error:;
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQryTradingNotice", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_3ctp_10_TraderApi_9TraderApi_110ReqQryTradingNotice(((struct __pyx_obj_3ctp_10_TraderApi_TraderApi *)__pyx_v_self), __pyx_v_pQryTradingNotice, __pyx_v_nRequestID);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_110ReqQryTradingNotice(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQryTradingNotice, int __pyx_v_nRequestID) {
  size_t __pyx_v_address;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_t_1;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  size_t __pyx_t_4;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("ReqQryTradingNotice", 0);
  __pyx_t_1 = ((__pyx_v_self->spi == NULL) != 0);
  if (__pyx_t_1) {
    __Pyx_XDECREF(__pyx_r);
    __pyx_r = Py_None; __Pyx_INCREF(Py_None);
    goto __pyx_L0;
  }
  __pyx_t_2 = PyTuple_New(1); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 439; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_v_pQryTradingNotice);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_v_pQryTradingNotice);
  __Pyx_GIVEREF(__pyx_v_pQryTradingNotice);
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_addressof, __pyx_t_2, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 439; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_4 = __Pyx_PyInt_As_size_t(__pyx_t_3); if (unlikely((__pyx_t_4 == (size_t)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 439; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_v_address = __pyx_t_4;
  {
      #ifdef WITH_THREAD
      PyThreadState *_save;
      Py_UNBLOCK_THREADS
      #endif
      {
        __pyx_v_nRequestID = __pyx_v_self->api->ReqQryTradingNotice(((struct CThostFtdcQryTradingNoticeField *)__pyx_v_address), __pyx_v_nRequestID);
      }
      {
        {
          #ifdef WITH_THREAD
          Py_BLOCK_THREADS
          #endif
          goto __pyx_L6;
        }
        __pyx_L6:;
      }
  }
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_3 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 441; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_r = __pyx_t_3;
  __pyx_t_3 = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQryTradingNotice", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_113ReqQryBrokerTradingParams(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds); 
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_113ReqQryBrokerTradingParams(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_pQryBrokerTradingParams = 0;
  int __pyx_v_nRequestID;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("ReqQryBrokerTradingParams (wrapper)", 0);
  {
    static PyObject **__pyx_pyargnames[] = {&__pyx_n_s_pQryBrokerTradingParams,&__pyx_n_s_nRequestID,0};
    PyObject* values[2] = {0,0};
    if (unlikely(__pyx_kwds)) {
      Py_ssize_t kw_args;
      const Py_ssize_t pos_args = PyTuple_GET_SIZE(__pyx_args);
      switch (pos_args) {
        case 2: values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
        case 1: values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
        case 0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      kw_args = PyDict_Size(__pyx_kwds);
      switch (pos_args) {
        case 0:
        if (likely((values[0] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_pQryBrokerTradingParams)) != 0)) kw_args--;
        else goto __pyx_L5_argtuple_error;
        case 1:
        if (likely((values[1] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_nRequestID)) != 0)) kw_args--;
        else {
          __Pyx_RaiseArgtupleInvalid("ReqQryBrokerTradingParams", 1, 2, 2, 1); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 443; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
        }
      }
      if (unlikely(kw_args > 0)) {
        if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_pyargnames, 0, values, pos_args, "ReqQryBrokerTradingParams") < 0)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 443; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
      }
    } else if (PyTuple_GET_SIZE(__pyx_args) != 2) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
      values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
    }
    __pyx_v_pQryBrokerTradingParams = values[0];
    __pyx_v_nRequestID = __Pyx_PyInt_As_int(values[1]); if (unlikely((__pyx_v_nRequestID == (int)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 443; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  }
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("ReqQryBrokerTradingParams", 1, 2, 2, PyTuple_GET_SIZE(__pyx_args)); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 443; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  __pyx_L3_error:;
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQryBrokerTradingParams", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_3ctp_10_TraderApi_9TraderApi_112ReqQryBrokerTradingParams(((struct __pyx_obj_3ctp_10_TraderApi_TraderApi *)__pyx_v_self), __pyx_v_pQryBrokerTradingParams, __pyx_v_nRequestID);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_112ReqQryBrokerTradingParams(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQryBrokerTradingParams, int __pyx_v_nRequestID) {
  size_t __pyx_v_address;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_t_1;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  size_t __pyx_t_4;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("ReqQryBrokerTradingParams", 0);
  __pyx_t_1 = ((__pyx_v_self->spi == NULL) != 0);
  if (__pyx_t_1) {
    __Pyx_XDECREF(__pyx_r);
    __pyx_r = Py_None; __Pyx_INCREF(Py_None);
    goto __pyx_L0;
  }
  __pyx_t_2 = PyTuple_New(1); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 446; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_v_pQryBrokerTradingParams);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_v_pQryBrokerTradingParams);
  __Pyx_GIVEREF(__pyx_v_pQryBrokerTradingParams);
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_addressof, __pyx_t_2, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 446; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_4 = __Pyx_PyInt_As_size_t(__pyx_t_3); if (unlikely((__pyx_t_4 == (size_t)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 446; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_v_address = __pyx_t_4;
  {
      #ifdef WITH_THREAD
      PyThreadState *_save;
      Py_UNBLOCK_THREADS
      #endif
      {
        __pyx_v_nRequestID = __pyx_v_self->api->ReqQryBrokerTradingParams(((struct CThostFtdcQryBrokerTradingParamsField *)__pyx_v_address), __pyx_v_nRequestID);
      }
      {
        {
          #ifdef WITH_THREAD
          Py_BLOCK_THREADS
          #endif
          goto __pyx_L6;
        }
        __pyx_L6:;
      }
  }
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_3 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 448; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_r = __pyx_t_3;
  __pyx_t_3 = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQryBrokerTradingParams", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_115ReqQryBrokerTradingAlgos(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds); 
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_115ReqQryBrokerTradingAlgos(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_pQryBrokerTradingAlgos = 0;
  int __pyx_v_nRequestID;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("ReqQryBrokerTradingAlgos (wrapper)", 0);
  {
    static PyObject **__pyx_pyargnames[] = {&__pyx_n_s_pQryBrokerTradingAlgos,&__pyx_n_s_nRequestID,0};
    PyObject* values[2] = {0,0};
    if (unlikely(__pyx_kwds)) {
      Py_ssize_t kw_args;
      const Py_ssize_t pos_args = PyTuple_GET_SIZE(__pyx_args);
      switch (pos_args) {
        case 2: values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
        case 1: values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
        case 0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      kw_args = PyDict_Size(__pyx_kwds);
      switch (pos_args) {
        case 0:
        if (likely((values[0] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_pQryBrokerTradingAlgos)) != 0)) kw_args--;
        else goto __pyx_L5_argtuple_error;
        case 1:
        if (likely((values[1] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_nRequestID)) != 0)) kw_args--;
        else {
          __Pyx_RaiseArgtupleInvalid("ReqQryBrokerTradingAlgos", 1, 2, 2, 1); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 450; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
        }
      }
      if (unlikely(kw_args > 0)) {
        if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_pyargnames, 0, values, pos_args, "ReqQryBrokerTradingAlgos") < 0)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 450; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
      }
    } else if (PyTuple_GET_SIZE(__pyx_args) != 2) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
      values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
    }
    __pyx_v_pQryBrokerTradingAlgos = values[0];
    __pyx_v_nRequestID = __Pyx_PyInt_As_int(values[1]); if (unlikely((__pyx_v_nRequestID == (int)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 450; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  }
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("ReqQryBrokerTradingAlgos", 1, 2, 2, PyTuple_GET_SIZE(__pyx_args)); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 450; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  __pyx_L3_error:;
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQryBrokerTradingAlgos", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_3ctp_10_TraderApi_9TraderApi_114ReqQryBrokerTradingAlgos(((struct __pyx_obj_3ctp_10_TraderApi_TraderApi *)__pyx_v_self), __pyx_v_pQryBrokerTradingAlgos, __pyx_v_nRequestID);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_114ReqQryBrokerTradingAlgos(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQryBrokerTradingAlgos, int __pyx_v_nRequestID) {
  size_t __pyx_v_address;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_t_1;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  size_t __pyx_t_4;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("ReqQryBrokerTradingAlgos", 0);
  __pyx_t_1 = ((__pyx_v_self->spi == NULL) != 0);
  if (__pyx_t_1) {
    __Pyx_XDECREF(__pyx_r);
    __pyx_r = Py_None; __Pyx_INCREF(Py_None);
    goto __pyx_L0;
  }
  __pyx_t_2 = PyTuple_New(1); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 453; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_v_pQryBrokerTradingAlgos);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_v_pQryBrokerTradingAlgos);
  __Pyx_GIVEREF(__pyx_v_pQryBrokerTradingAlgos);
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_addressof, __pyx_t_2, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 453; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_4 = __Pyx_PyInt_As_size_t(__pyx_t_3); if (unlikely((__pyx_t_4 == (size_t)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 453; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_v_address = __pyx_t_4;
  {
      #ifdef WITH_THREAD
      PyThreadState *_save;
      Py_UNBLOCK_THREADS
      #endif
      {
        __pyx_v_nRequestID = __pyx_v_self->api->ReqQryBrokerTradingAlgos(((struct CThostFtdcQryBrokerTradingAlgosField *)__pyx_v_address), __pyx_v_nRequestID);
      }
      {
        {
          #ifdef WITH_THREAD
          Py_BLOCK_THREADS
          #endif
          goto __pyx_L6;
        }
        __pyx_L6:;
      }
  }
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_3 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 455; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_r = __pyx_t_3;
  __pyx_t_3 = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQryBrokerTradingAlgos", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_117ReqQueryCFMMCTradingAccountToken(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds); 
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_117ReqQueryCFMMCTradingAccountToken(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_pQueryCFMMCTradingAccountToken = 0;
  int __pyx_v_nRequestID;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("ReqQueryCFMMCTradingAccountToken (wrapper)", 0);
  {
    static PyObject **__pyx_pyargnames[] = {&__pyx_n_s_pQueryCFMMCTradingAccountToken,&__pyx_n_s_nRequestID,0};
    PyObject* values[2] = {0,0};
    if (unlikely(__pyx_kwds)) {
      Py_ssize_t kw_args;
      const Py_ssize_t pos_args = PyTuple_GET_SIZE(__pyx_args);
      switch (pos_args) {
        case 2: values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
        case 1: values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
        case 0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      kw_args = PyDict_Size(__pyx_kwds);
      switch (pos_args) {
        case 0:
        if (likely((values[0] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_pQueryCFMMCTradingAccountToken)) != 0)) kw_args--;
        else goto __pyx_L5_argtuple_error;
        case 1:
        if (likely((values[1] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_nRequestID)) != 0)) kw_args--;
        else {
          __Pyx_RaiseArgtupleInvalid("ReqQueryCFMMCTradingAccountToken", 1, 2, 2, 1); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 457; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
        }
      }
      if (unlikely(kw_args > 0)) {
        if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_pyargnames, 0, values, pos_args, "ReqQueryCFMMCTradingAccountToken") < 0)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 457; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
      }
    } else if (PyTuple_GET_SIZE(__pyx_args) != 2) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
      values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
    }
    __pyx_v_pQueryCFMMCTradingAccountToken = values[0];
    __pyx_v_nRequestID = __Pyx_PyInt_As_int(values[1]); if (unlikely((__pyx_v_nRequestID == (int)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 457; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  }
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("ReqQueryCFMMCTradingAccountToken", 1, 2, 2, PyTuple_GET_SIZE(__pyx_args)); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 457; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  __pyx_L3_error:;
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQueryCFMMCTradingAccountToken", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_3ctp_10_TraderApi_9TraderApi_116ReqQueryCFMMCTradingAccountToken(((struct __pyx_obj_3ctp_10_TraderApi_TraderApi *)__pyx_v_self), __pyx_v_pQueryCFMMCTradingAccountToken, __pyx_v_nRequestID);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_116ReqQueryCFMMCTradingAccountToken(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pQueryCFMMCTradingAccountToken, int __pyx_v_nRequestID) {
  size_t __pyx_v_address;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_t_1;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  size_t __pyx_t_4;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("ReqQueryCFMMCTradingAccountToken", 0);
  __pyx_t_1 = ((__pyx_v_self->spi == NULL) != 0);
  if (__pyx_t_1) {
    __Pyx_XDECREF(__pyx_r);
    __pyx_r = Py_None; __Pyx_INCREF(Py_None);
    goto __pyx_L0;
  }
  __pyx_t_2 = PyTuple_New(1); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 460; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_v_pQueryCFMMCTradingAccountToken);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_v_pQueryCFMMCTradingAccountToken);
  __Pyx_GIVEREF(__pyx_v_pQueryCFMMCTradingAccountToken);
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_addressof, __pyx_t_2, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 460; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_4 = __Pyx_PyInt_As_size_t(__pyx_t_3); if (unlikely((__pyx_t_4 == (size_t)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 460; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_v_address = __pyx_t_4;
  {
      #ifdef WITH_THREAD
      PyThreadState *_save;
      Py_UNBLOCK_THREADS
      #endif
      {
        __pyx_v_nRequestID = __pyx_v_self->api->ReqQueryCFMMCTradingAccountToken(((struct CThostFtdcQueryCFMMCTradingAccountTokenField *)__pyx_v_address), __pyx_v_nRequestID);
      }
      {
        {
          #ifdef WITH_THREAD
          Py_BLOCK_THREADS
          #endif
          goto __pyx_L6;
        }
        __pyx_L6:;
      }
  }
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_3 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 462; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_r = __pyx_t_3;
  __pyx_t_3 = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQueryCFMMCTradingAccountToken", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_119ReqFromBankToFutureByFuture(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds); 
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_119ReqFromBankToFutureByFuture(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_pReqTransfer = 0;
  int __pyx_v_nRequestID;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("ReqFromBankToFutureByFuture (wrapper)", 0);
  {
    static PyObject **__pyx_pyargnames[] = {&__pyx_n_s_pReqTransfer,&__pyx_n_s_nRequestID,0};
    PyObject* values[2] = {0,0};
    if (unlikely(__pyx_kwds)) {
      Py_ssize_t kw_args;
      const Py_ssize_t pos_args = PyTuple_GET_SIZE(__pyx_args);
      switch (pos_args) {
        case 2: values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
        case 1: values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
        case 0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      kw_args = PyDict_Size(__pyx_kwds);
      switch (pos_args) {
        case 0:
        if (likely((values[0] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_pReqTransfer)) != 0)) kw_args--;
        else goto __pyx_L5_argtuple_error;
        case 1:
        if (likely((values[1] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_nRequestID)) != 0)) kw_args--;
        else {
          __Pyx_RaiseArgtupleInvalid("ReqFromBankToFutureByFuture", 1, 2, 2, 1); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 464; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
        }
      }
      if (unlikely(kw_args > 0)) {
        if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_pyargnames, 0, values, pos_args, "ReqFromBankToFutureByFuture") < 0)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 464; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
      }
    } else if (PyTuple_GET_SIZE(__pyx_args) != 2) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
      values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
    }
    __pyx_v_pReqTransfer = values[0];
    __pyx_v_nRequestID = __Pyx_PyInt_As_int(values[1]); if (unlikely((__pyx_v_nRequestID == (int)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 464; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  }
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("ReqFromBankToFutureByFuture", 1, 2, 2, PyTuple_GET_SIZE(__pyx_args)); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 464; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  __pyx_L3_error:;
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqFromBankToFutureByFuture", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_3ctp_10_TraderApi_9TraderApi_118ReqFromBankToFutureByFuture(((struct __pyx_obj_3ctp_10_TraderApi_TraderApi *)__pyx_v_self), __pyx_v_pReqTransfer, __pyx_v_nRequestID);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_118ReqFromBankToFutureByFuture(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pReqTransfer, int __pyx_v_nRequestID) {
  size_t __pyx_v_address;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_t_1;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  size_t __pyx_t_4;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("ReqFromBankToFutureByFuture", 0);
  __pyx_t_1 = ((__pyx_v_self->spi == NULL) != 0);
  if (__pyx_t_1) {
    __Pyx_XDECREF(__pyx_r);
    __pyx_r = Py_None; __Pyx_INCREF(Py_None);
    goto __pyx_L0;
  }
  __pyx_t_2 = PyTuple_New(1); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 467; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_v_pReqTransfer);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_v_pReqTransfer);
  __Pyx_GIVEREF(__pyx_v_pReqTransfer);
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_addressof, __pyx_t_2, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 467; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_4 = __Pyx_PyInt_As_size_t(__pyx_t_3); if (unlikely((__pyx_t_4 == (size_t)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 467; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_v_address = __pyx_t_4;
  {
      #ifdef WITH_THREAD
      PyThreadState *_save;
      Py_UNBLOCK_THREADS
      #endif
      {
        __pyx_v_nRequestID = __pyx_v_self->api->ReqFromBankToFutureByFuture(((struct CThostFtdcReqTransferField *)__pyx_v_address), __pyx_v_nRequestID);
      }
      {
        {
          #ifdef WITH_THREAD
          Py_BLOCK_THREADS
          #endif
          goto __pyx_L6;
        }
        __pyx_L6:;
      }
  }
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_3 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 469; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_r = __pyx_t_3;
  __pyx_t_3 = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqFromBankToFutureByFuture", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_121ReqFromFutureToBankByFuture(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds); 
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_121ReqFromFutureToBankByFuture(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_pReqTransfer = 0;
  int __pyx_v_nRequestID;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("ReqFromFutureToBankByFuture (wrapper)", 0);
  {
    static PyObject **__pyx_pyargnames[] = {&__pyx_n_s_pReqTransfer,&__pyx_n_s_nRequestID,0};
    PyObject* values[2] = {0,0};
    if (unlikely(__pyx_kwds)) {
      Py_ssize_t kw_args;
      const Py_ssize_t pos_args = PyTuple_GET_SIZE(__pyx_args);
      switch (pos_args) {
        case 2: values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
        case 1: values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
        case 0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      kw_args = PyDict_Size(__pyx_kwds);
      switch (pos_args) {
        case 0:
        if (likely((values[0] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_pReqTransfer)) != 0)) kw_args--;
        else goto __pyx_L5_argtuple_error;
        case 1:
        if (likely((values[1] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_nRequestID)) != 0)) kw_args--;
        else {
          __Pyx_RaiseArgtupleInvalid("ReqFromFutureToBankByFuture", 1, 2, 2, 1); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 471; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
        }
      }
      if (unlikely(kw_args > 0)) {
        if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_pyargnames, 0, values, pos_args, "ReqFromFutureToBankByFuture") < 0)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 471; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
      }
    } else if (PyTuple_GET_SIZE(__pyx_args) != 2) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
      values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
    }
    __pyx_v_pReqTransfer = values[0];
    __pyx_v_nRequestID = __Pyx_PyInt_As_int(values[1]); if (unlikely((__pyx_v_nRequestID == (int)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 471; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  }
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("ReqFromFutureToBankByFuture", 1, 2, 2, PyTuple_GET_SIZE(__pyx_args)); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 471; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  __pyx_L3_error:;
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqFromFutureToBankByFuture", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_3ctp_10_TraderApi_9TraderApi_120ReqFromFutureToBankByFuture(((struct __pyx_obj_3ctp_10_TraderApi_TraderApi *)__pyx_v_self), __pyx_v_pReqTransfer, __pyx_v_nRequestID);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_120ReqFromFutureToBankByFuture(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pReqTransfer, int __pyx_v_nRequestID) {
  size_t __pyx_v_address;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_t_1;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  size_t __pyx_t_4;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("ReqFromFutureToBankByFuture", 0);
  __pyx_t_1 = ((__pyx_v_self->spi == NULL) != 0);
  if (__pyx_t_1) {
    __Pyx_XDECREF(__pyx_r);
    __pyx_r = Py_None; __Pyx_INCREF(Py_None);
    goto __pyx_L0;
  }
  __pyx_t_2 = PyTuple_New(1); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 474; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_v_pReqTransfer);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_v_pReqTransfer);
  __Pyx_GIVEREF(__pyx_v_pReqTransfer);
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_addressof, __pyx_t_2, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 474; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_4 = __Pyx_PyInt_As_size_t(__pyx_t_3); if (unlikely((__pyx_t_4 == (size_t)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 474; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_v_address = __pyx_t_4;
  {
      #ifdef WITH_THREAD
      PyThreadState *_save;
      Py_UNBLOCK_THREADS
      #endif
      {
        __pyx_v_nRequestID = __pyx_v_self->api->ReqFromFutureToBankByFuture(((struct CThostFtdcReqTransferField *)__pyx_v_address), __pyx_v_nRequestID);
      }
      {
        {
          #ifdef WITH_THREAD
          Py_BLOCK_THREADS
          #endif
          goto __pyx_L6;
        }
        __pyx_L6:;
      }
  }
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_3 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 476; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_r = __pyx_t_3;
  __pyx_t_3 = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqFromFutureToBankByFuture", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_123ReqQueryBankAccountMoneyByFuture(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds); 
static PyObject *__pyx_pw_3ctp_10_TraderApi_9TraderApi_123ReqQueryBankAccountMoneyByFuture(PyObject *__pyx_v_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_pReqQueryAccount = 0;
  int __pyx_v_nRequestID;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("ReqQueryBankAccountMoneyByFuture (wrapper)", 0);
  {
    static PyObject **__pyx_pyargnames[] = {&__pyx_n_s_pReqQueryAccount,&__pyx_n_s_nRequestID,0};
    PyObject* values[2] = {0,0};
    if (unlikely(__pyx_kwds)) {
      Py_ssize_t kw_args;
      const Py_ssize_t pos_args = PyTuple_GET_SIZE(__pyx_args);
      switch (pos_args) {
        case 2: values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
        case 1: values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
        case 0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      kw_args = PyDict_Size(__pyx_kwds);
      switch (pos_args) {
        case 0:
        if (likely((values[0] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_pReqQueryAccount)) != 0)) kw_args--;
        else goto __pyx_L5_argtuple_error;
        case 1:
        if (likely((values[1] = PyDict_GetItem(__pyx_kwds, __pyx_n_s_nRequestID)) != 0)) kw_args--;
        else {
          __Pyx_RaiseArgtupleInvalid("ReqQueryBankAccountMoneyByFuture", 1, 2, 2, 1); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 478; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
        }
      }
      if (unlikely(kw_args > 0)) {
        if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_pyargnames, 0, values, pos_args, "ReqQueryBankAccountMoneyByFuture") < 0)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 478; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
      }
    } else if (PyTuple_GET_SIZE(__pyx_args) != 2) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
      values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
    }
    __pyx_v_pReqQueryAccount = values[0];
    __pyx_v_nRequestID = __Pyx_PyInt_As_int(values[1]); if (unlikely((__pyx_v_nRequestID == (int)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 478; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  }
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("ReqQueryBankAccountMoneyByFuture", 1, 2, 2, PyTuple_GET_SIZE(__pyx_args)); {__pyx_filename = __pyx_f[0]; __pyx_lineno = 478; __pyx_clineno = __LINE__; goto __pyx_L3_error;}
  __pyx_L3_error:;
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQueryBankAccountMoneyByFuture", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_3ctp_10_TraderApi_9TraderApi_122ReqQueryBankAccountMoneyByFuture(((struct __pyx_obj_3ctp_10_TraderApi_TraderApi *)__pyx_v_self), __pyx_v_pReqQueryAccount, __pyx_v_nRequestID);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_pf_3ctp_10_TraderApi_9TraderApi_122ReqQueryBankAccountMoneyByFuture(struct __pyx_obj_3ctp_10_TraderApi_TraderApi *__pyx_v_self, PyObject *__pyx_v_pReqQueryAccount, int __pyx_v_nRequestID) {
  size_t __pyx_v_address;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_t_1;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  size_t __pyx_t_4;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("ReqQueryBankAccountMoneyByFuture", 0);
  __pyx_t_1 = ((__pyx_v_self->spi == NULL) != 0);
  if (__pyx_t_1) {
    __Pyx_XDECREF(__pyx_r);
    __pyx_r = Py_None; __Pyx_INCREF(Py_None);
    goto __pyx_L0;
  }
  __pyx_t_2 = PyTuple_New(1); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 481; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_v_pReqQueryAccount);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_v_pReqQueryAccount);
  __Pyx_GIVEREF(__pyx_v_pReqQueryAccount);
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_addressof, __pyx_t_2, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 481; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_4 = __Pyx_PyInt_As_size_t(__pyx_t_3); if (unlikely((__pyx_t_4 == (size_t)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 481; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_v_address = __pyx_t_4;
  {
      #ifdef WITH_THREAD
      PyThreadState *_save;
      Py_UNBLOCK_THREADS
      #endif
      {
        __pyx_v_nRequestID = __pyx_v_self->api->ReqQueryBankAccountMoneyByFuture(((struct CThostFtdcReqQueryAccountField *)__pyx_v_address), __pyx_v_nRequestID);
      }
      {
        {
          #ifdef WITH_THREAD
          Py_BLOCK_THREADS
          #endif
          goto __pyx_L6;
        }
        __pyx_L6:;
      }
  }
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_3 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 483; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_r = __pyx_t_3;
  __pyx_t_3 = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("ctp._TraderApi.TraderApi.ReqQueryBankAccountMoneyByFuture", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnFrontConnected(PyObject *__pyx_v_self) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnFrontConnected", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnFrontConnected); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 487; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_empty_tuple, NULL); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 487; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnFrontConnected", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnFrontDisconnected(PyObject *__pyx_v_self, int __pyx_v_nReason) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnFrontDisconnected", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnFrontDisconnected); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 491; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_PyInt_From_int(__pyx_v_nReason); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 491; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = PyTuple_New(1); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 491; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_3, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_3, NULL); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 491; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnFrontDisconnected", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnHeartBeatWarning(PyObject *__pyx_v_self, int __pyx_v_nTimeLapse) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnHeartBeatWarning", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnHeartBeatWarning); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 495; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_PyInt_From_int(__pyx_v_nTimeLapse); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 495; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = PyTuple_New(1); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 495; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_3, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_3, NULL); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 495; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnHeartBeatWarning", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRspAuthenticate(PyObject *__pyx_v_self, struct CThostFtdcRspAuthenticateField *__pyx_v_pRspAuthenticate, struct CThostFtdcRspInfoField *__pyx_v_pRspInfo, int __pyx_v_nRequestID, bool __pyx_v_bIsLast) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRspAuthenticate", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRspAuthenticate); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 499; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pRspAuthenticate == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspAuthenticate)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 499; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 499; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspAuthenticate, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 499; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  if (((__pyx_v_pRspInfo == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_3 = Py_None;
  } else {
    __pyx_t_4 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspInfo)); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 499; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_5 = PyTuple_New(1); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 499; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_5);
    PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_4);
    __Pyx_GIVEREF(__pyx_t_4);
    __pyx_t_4 = 0;
    __pyx_t_4 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspInfo, __pyx_t_5, NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 499; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_3 = __pyx_t_4;
    __pyx_t_4 = 0;
  }
  __pyx_t_4 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 499; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = __Pyx_PyBool_FromLong(__pyx_v_bIsLast); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 499; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_6 = PyTuple_New(4); if (unlikely(!__pyx_t_6)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 499; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_6);
  PyTuple_SET_ITEM(__pyx_t_6, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_6, 1, __pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_6, 2, __pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_6, 3, __pyx_t_5);
  __Pyx_GIVEREF(__pyx_t_5);
  __pyx_t_2 = 0;
  __pyx_t_3 = 0;
  __pyx_t_4 = 0;
  __pyx_t_5 = 0;
  __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_6, NULL); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 499; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRspAuthenticate", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRspUserLogin(PyObject *__pyx_v_self, struct CThostFtdcRspUserLoginField *__pyx_v_pRspUserLogin, struct CThostFtdcRspInfoField *__pyx_v_pRspInfo, int __pyx_v_nRequestID, bool __pyx_v_bIsLast) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRspUserLogin", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRspUserLogin); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 503; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pRspUserLogin == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspUserLogin)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 503; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 503; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspUserLogin, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 503; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  if (((__pyx_v_pRspInfo == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_3 = Py_None;
  } else {
    __pyx_t_4 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspInfo)); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 503; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_5 = PyTuple_New(1); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 503; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_5);
    PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_4);
    __Pyx_GIVEREF(__pyx_t_4);
    __pyx_t_4 = 0;
    __pyx_t_4 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspInfo, __pyx_t_5, NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 503; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_3 = __pyx_t_4;
    __pyx_t_4 = 0;
  }
  __pyx_t_4 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 503; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = __Pyx_PyBool_FromLong(__pyx_v_bIsLast); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 503; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_6 = PyTuple_New(4); if (unlikely(!__pyx_t_6)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 503; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_6);
  PyTuple_SET_ITEM(__pyx_t_6, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_6, 1, __pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_6, 2, __pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_6, 3, __pyx_t_5);
  __Pyx_GIVEREF(__pyx_t_5);
  __pyx_t_2 = 0;
  __pyx_t_3 = 0;
  __pyx_t_4 = 0;
  __pyx_t_5 = 0;
  __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_6, NULL); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 503; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRspUserLogin", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRspUserLogout(PyObject *__pyx_v_self, struct CThostFtdcUserLogoutField *__pyx_v_pUserLogout, struct CThostFtdcRspInfoField *__pyx_v_pRspInfo, int __pyx_v_nRequestID, bool __pyx_v_bIsLast) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRspUserLogout", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRspUserLogout); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 507; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pUserLogout == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pUserLogout)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 507; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 507; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_UserLogout, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 507; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  if (((__pyx_v_pRspInfo == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_3 = Py_None;
  } else {
    __pyx_t_4 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspInfo)); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 507; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_5 = PyTuple_New(1); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 507; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_5);
    PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_4);
    __Pyx_GIVEREF(__pyx_t_4);
    __pyx_t_4 = 0;
    __pyx_t_4 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspInfo, __pyx_t_5, NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 507; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_3 = __pyx_t_4;
    __pyx_t_4 = 0;
  }
  __pyx_t_4 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 507; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = __Pyx_PyBool_FromLong(__pyx_v_bIsLast); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 507; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_6 = PyTuple_New(4); if (unlikely(!__pyx_t_6)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 507; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_6);
  PyTuple_SET_ITEM(__pyx_t_6, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_6, 1, __pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_6, 2, __pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_6, 3, __pyx_t_5);
  __Pyx_GIVEREF(__pyx_t_5);
  __pyx_t_2 = 0;
  __pyx_t_3 = 0;
  __pyx_t_4 = 0;
  __pyx_t_5 = 0;
  __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_6, NULL); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 507; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRspUserLogout", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRspUserPasswordUpdate(PyObject *__pyx_v_self, struct CThostFtdcUserPasswordUpdateField *__pyx_v_pUserPasswordUpdate, struct CThostFtdcRspInfoField *__pyx_v_pRspInfo, int __pyx_v_nRequestID, bool __pyx_v_bIsLast) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRspUserPasswordUpdate", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRspUserPasswordUpdate); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 511; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pUserPasswordUpdate == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pUserPasswordUpdate)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 511; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 511; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_UserPasswordUpdate, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 511; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  if (((__pyx_v_pRspInfo == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_3 = Py_None;
  } else {
    __pyx_t_4 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspInfo)); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 511; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_5 = PyTuple_New(1); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 511; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_5);
    PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_4);
    __Pyx_GIVEREF(__pyx_t_4);
    __pyx_t_4 = 0;
    __pyx_t_4 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspInfo, __pyx_t_5, NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 511; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_3 = __pyx_t_4;
    __pyx_t_4 = 0;
  }
  __pyx_t_4 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 511; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = __Pyx_PyBool_FromLong(__pyx_v_bIsLast); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 511; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_6 = PyTuple_New(4); if (unlikely(!__pyx_t_6)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 511; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_6);
  PyTuple_SET_ITEM(__pyx_t_6, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_6, 1, __pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_6, 2, __pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_6, 3, __pyx_t_5);
  __Pyx_GIVEREF(__pyx_t_5);
  __pyx_t_2 = 0;
  __pyx_t_3 = 0;
  __pyx_t_4 = 0;
  __pyx_t_5 = 0;
  __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_6, NULL); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 511; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRspUserPasswordUpdate", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRspTradingAccountPasswordUpdate(PyObject *__pyx_v_self, struct CThostFtdcTradingAccountPasswordUpdateField *__pyx_v_pTradingAccountPasswordUpdate, struct CThostFtdcRspInfoField *__pyx_v_pRspInfo, int __pyx_v_nRequestID, bool __pyx_v_bIsLast) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRspTradingAccountPasswordUpdate", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRspTradingAccountPasswordUpdat); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 515; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pTradingAccountPasswordUpdate == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pTradingAccountPasswordUpdate)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 515; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 515; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_TradingAccountPasswordUpdate, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 515; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  if (((__pyx_v_pRspInfo == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_3 = Py_None;
  } else {
    __pyx_t_4 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspInfo)); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 515; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_5 = PyTuple_New(1); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 515; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_5);
    PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_4);
    __Pyx_GIVEREF(__pyx_t_4);
    __pyx_t_4 = 0;
    __pyx_t_4 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspInfo, __pyx_t_5, NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 515; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_3 = __pyx_t_4;
    __pyx_t_4 = 0;
  }
  __pyx_t_4 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 515; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = __Pyx_PyBool_FromLong(__pyx_v_bIsLast); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 515; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_6 = PyTuple_New(4); if (unlikely(!__pyx_t_6)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 515; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_6);
  PyTuple_SET_ITEM(__pyx_t_6, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_6, 1, __pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_6, 2, __pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_6, 3, __pyx_t_5);
  __Pyx_GIVEREF(__pyx_t_5);
  __pyx_t_2 = 0;
  __pyx_t_3 = 0;
  __pyx_t_4 = 0;
  __pyx_t_5 = 0;
  __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_6, NULL); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 515; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRspTradingAccountPasswordUpdate", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRspOrderInsert(PyObject *__pyx_v_self, struct CThostFtdcInputOrderField *__pyx_v_pInputOrder, struct CThostFtdcRspInfoField *__pyx_v_pRspInfo, int __pyx_v_nRequestID, bool __pyx_v_bIsLast) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRspOrderInsert", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRspOrderInsert); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 519; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pInputOrder == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pInputOrder)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 519; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 519; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_InputOrder, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 519; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  if (((__pyx_v_pRspInfo == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_3 = Py_None;
  } else {
    __pyx_t_4 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspInfo)); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 519; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_5 = PyTuple_New(1); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 519; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_5);
    PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_4);
    __Pyx_GIVEREF(__pyx_t_4);
    __pyx_t_4 = 0;
    __pyx_t_4 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspInfo, __pyx_t_5, NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 519; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_3 = __pyx_t_4;
    __pyx_t_4 = 0;
  }
  __pyx_t_4 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 519; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = __Pyx_PyBool_FromLong(__pyx_v_bIsLast); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 519; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_6 = PyTuple_New(4); if (unlikely(!__pyx_t_6)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 519; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_6);
  PyTuple_SET_ITEM(__pyx_t_6, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_6, 1, __pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_6, 2, __pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_6, 3, __pyx_t_5);
  __Pyx_GIVEREF(__pyx_t_5);
  __pyx_t_2 = 0;
  __pyx_t_3 = 0;
  __pyx_t_4 = 0;
  __pyx_t_5 = 0;
  __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_6, NULL); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 519; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRspOrderInsert", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRspParkedOrderInsert(PyObject *__pyx_v_self, struct CThostFtdcParkedOrderField *__pyx_v_pParkedOrder, struct CThostFtdcRspInfoField *__pyx_v_pRspInfo, int __pyx_v_nRequestID, bool __pyx_v_bIsLast) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRspParkedOrderInsert", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRspParkedOrderInsert); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 523; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pParkedOrder == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pParkedOrder)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 523; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 523; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_ParkedOrder, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 523; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  if (((__pyx_v_pRspInfo == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_3 = Py_None;
  } else {
    __pyx_t_4 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspInfo)); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 523; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_5 = PyTuple_New(1); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 523; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_5);
    PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_4);
    __Pyx_GIVEREF(__pyx_t_4);
    __pyx_t_4 = 0;
    __pyx_t_4 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspInfo, __pyx_t_5, NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 523; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_3 = __pyx_t_4;
    __pyx_t_4 = 0;
  }
  __pyx_t_4 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 523; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = __Pyx_PyBool_FromLong(__pyx_v_bIsLast); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 523; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_6 = PyTuple_New(4); if (unlikely(!__pyx_t_6)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 523; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_6);
  PyTuple_SET_ITEM(__pyx_t_6, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_6, 1, __pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_6, 2, __pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_6, 3, __pyx_t_5);
  __Pyx_GIVEREF(__pyx_t_5);
  __pyx_t_2 = 0;
  __pyx_t_3 = 0;
  __pyx_t_4 = 0;
  __pyx_t_5 = 0;
  __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_6, NULL); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 523; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRspParkedOrderInsert", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRspParkedOrderAction(PyObject *__pyx_v_self, struct CThostFtdcParkedOrderActionField *__pyx_v_pParkedOrderAction, struct CThostFtdcRspInfoField *__pyx_v_pRspInfo, int __pyx_v_nRequestID, bool __pyx_v_bIsLast) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRspParkedOrderAction", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRspParkedOrderAction); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 527; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pParkedOrderAction == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pParkedOrderAction)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 527; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 527; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_ParkedOrderAction, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 527; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  if (((__pyx_v_pRspInfo == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_3 = Py_None;
  } else {
    __pyx_t_4 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspInfo)); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 527; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_5 = PyTuple_New(1); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 527; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_5);
    PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_4);
    __Pyx_GIVEREF(__pyx_t_4);
    __pyx_t_4 = 0;
    __pyx_t_4 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspInfo, __pyx_t_5, NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 527; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_3 = __pyx_t_4;
    __pyx_t_4 = 0;
  }
  __pyx_t_4 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 527; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = __Pyx_PyBool_FromLong(__pyx_v_bIsLast); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 527; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_6 = PyTuple_New(4); if (unlikely(!__pyx_t_6)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 527; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_6);
  PyTuple_SET_ITEM(__pyx_t_6, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_6, 1, __pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_6, 2, __pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_6, 3, __pyx_t_5);
  __Pyx_GIVEREF(__pyx_t_5);
  __pyx_t_2 = 0;
  __pyx_t_3 = 0;
  __pyx_t_4 = 0;
  __pyx_t_5 = 0;
  __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_6, NULL); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 527; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRspParkedOrderAction", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRspOrderAction(PyObject *__pyx_v_self, struct CThostFtdcInputOrderActionField *__pyx_v_pInputOrderAction, struct CThostFtdcRspInfoField *__pyx_v_pRspInfo, int __pyx_v_nRequestID, bool __pyx_v_bIsLast) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRspOrderAction", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRspOrderAction); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 531; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pInputOrderAction == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pInputOrderAction)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 531; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 531; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_InputOrderAction, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 531; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  if (((__pyx_v_pRspInfo == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_3 = Py_None;
  } else {
    __pyx_t_4 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspInfo)); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 531; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_5 = PyTuple_New(1); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 531; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_5);
    PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_4);
    __Pyx_GIVEREF(__pyx_t_4);
    __pyx_t_4 = 0;
    __pyx_t_4 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspInfo, __pyx_t_5, NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 531; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_3 = __pyx_t_4;
    __pyx_t_4 = 0;
  }
  __pyx_t_4 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 531; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = __Pyx_PyBool_FromLong(__pyx_v_bIsLast); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 531; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_6 = PyTuple_New(4); if (unlikely(!__pyx_t_6)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 531; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_6);
  PyTuple_SET_ITEM(__pyx_t_6, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_6, 1, __pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_6, 2, __pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_6, 3, __pyx_t_5);
  __Pyx_GIVEREF(__pyx_t_5);
  __pyx_t_2 = 0;
  __pyx_t_3 = 0;
  __pyx_t_4 = 0;
  __pyx_t_5 = 0;
  __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_6, NULL); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 531; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRspOrderAction", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRspQueryMaxOrderVolume(PyObject *__pyx_v_self, struct CThostFtdcQueryMaxOrderVolumeField *__pyx_v_pQueryMaxOrderVolume, struct CThostFtdcRspInfoField *__pyx_v_pRspInfo, int __pyx_v_nRequestID, bool __pyx_v_bIsLast) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRspQueryMaxOrderVolume", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRspQueryMaxOrderVolume); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 535; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pQueryMaxOrderVolume == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pQueryMaxOrderVolume)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 535; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 535; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_QueryMaxOrderVolume, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 535; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  if (((__pyx_v_pRspInfo == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_3 = Py_None;
  } else {
    __pyx_t_4 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspInfo)); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 535; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_5 = PyTuple_New(1); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 535; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_5);
    PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_4);
    __Pyx_GIVEREF(__pyx_t_4);
    __pyx_t_4 = 0;
    __pyx_t_4 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspInfo, __pyx_t_5, NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 535; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_3 = __pyx_t_4;
    __pyx_t_4 = 0;
  }
  __pyx_t_4 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 535; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = __Pyx_PyBool_FromLong(__pyx_v_bIsLast); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 535; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_6 = PyTuple_New(4); if (unlikely(!__pyx_t_6)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 535; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_6);
  PyTuple_SET_ITEM(__pyx_t_6, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_6, 1, __pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_6, 2, __pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_6, 3, __pyx_t_5);
  __Pyx_GIVEREF(__pyx_t_5);
  __pyx_t_2 = 0;
  __pyx_t_3 = 0;
  __pyx_t_4 = 0;
  __pyx_t_5 = 0;
  __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_6, NULL); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 535; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRspQueryMaxOrderVolume", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRspSettlementInfoConfirm(PyObject *__pyx_v_self, struct CThostFtdcSettlementInfoConfirmField *__pyx_v_pSettlementInfoConfirm, struct CThostFtdcRspInfoField *__pyx_v_pRspInfo, int __pyx_v_nRequestID, bool __pyx_v_bIsLast) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRspSettlementInfoConfirm", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRspSettlementInfoConfirm); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 539; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pSettlementInfoConfirm == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pSettlementInfoConfirm)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 539; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 539; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_SettlementInfoConfirm, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 539; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  if (((__pyx_v_pRspInfo == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_3 = Py_None;
  } else {
    __pyx_t_4 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspInfo)); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 539; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_5 = PyTuple_New(1); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 539; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_5);
    PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_4);
    __Pyx_GIVEREF(__pyx_t_4);
    __pyx_t_4 = 0;
    __pyx_t_4 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspInfo, __pyx_t_5, NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 539; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_3 = __pyx_t_4;
    __pyx_t_4 = 0;
  }
  __pyx_t_4 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 539; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = __Pyx_PyBool_FromLong(__pyx_v_bIsLast); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 539; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_6 = PyTuple_New(4); if (unlikely(!__pyx_t_6)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 539; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_6);
  PyTuple_SET_ITEM(__pyx_t_6, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_6, 1, __pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_6, 2, __pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_6, 3, __pyx_t_5);
  __Pyx_GIVEREF(__pyx_t_5);
  __pyx_t_2 = 0;
  __pyx_t_3 = 0;
  __pyx_t_4 = 0;
  __pyx_t_5 = 0;
  __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_6, NULL); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 539; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRspSettlementInfoConfirm", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRspRemoveParkedOrder(PyObject *__pyx_v_self, struct CThostFtdcRemoveParkedOrderField *__pyx_v_pRemoveParkedOrder, struct CThostFtdcRspInfoField *__pyx_v_pRspInfo, int __pyx_v_nRequestID, bool __pyx_v_bIsLast) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRspRemoveParkedOrder", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRspRemoveParkedOrder); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 543; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pRemoveParkedOrder == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRemoveParkedOrder)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 543; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 543; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RemoveParkedOrder, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 543; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  if (((__pyx_v_pRspInfo == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_3 = Py_None;
  } else {
    __pyx_t_4 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspInfo)); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 543; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_5 = PyTuple_New(1); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 543; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_5);
    PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_4);
    __Pyx_GIVEREF(__pyx_t_4);
    __pyx_t_4 = 0;
    __pyx_t_4 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspInfo, __pyx_t_5, NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 543; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_3 = __pyx_t_4;
    __pyx_t_4 = 0;
  }
  __pyx_t_4 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 543; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = __Pyx_PyBool_FromLong(__pyx_v_bIsLast); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 543; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_6 = PyTuple_New(4); if (unlikely(!__pyx_t_6)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 543; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_6);
  PyTuple_SET_ITEM(__pyx_t_6, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_6, 1, __pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_6, 2, __pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_6, 3, __pyx_t_5);
  __Pyx_GIVEREF(__pyx_t_5);
  __pyx_t_2 = 0;
  __pyx_t_3 = 0;
  __pyx_t_4 = 0;
  __pyx_t_5 = 0;
  __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_6, NULL); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 543; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRspRemoveParkedOrder", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRspRemoveParkedOrderAction(PyObject *__pyx_v_self, struct CThostFtdcRemoveParkedOrderActionField *__pyx_v_pRemoveParkedOrderAction, struct CThostFtdcRspInfoField *__pyx_v_pRspInfo, int __pyx_v_nRequestID, bool __pyx_v_bIsLast) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRspRemoveParkedOrderAction", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRspRemoveParkedOrderAction); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 547; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pRemoveParkedOrderAction == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRemoveParkedOrderAction)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 547; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 547; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RemoveParkedOrderAction, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 547; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  if (((__pyx_v_pRspInfo == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_3 = Py_None;
  } else {
    __pyx_t_4 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspInfo)); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 547; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_5 = PyTuple_New(1); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 547; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_5);
    PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_4);
    __Pyx_GIVEREF(__pyx_t_4);
    __pyx_t_4 = 0;
    __pyx_t_4 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspInfo, __pyx_t_5, NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 547; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_3 = __pyx_t_4;
    __pyx_t_4 = 0;
  }
  __pyx_t_4 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 547; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = __Pyx_PyBool_FromLong(__pyx_v_bIsLast); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 547; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_6 = PyTuple_New(4); if (unlikely(!__pyx_t_6)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 547; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_6);
  PyTuple_SET_ITEM(__pyx_t_6, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_6, 1, __pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_6, 2, __pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_6, 3, __pyx_t_5);
  __Pyx_GIVEREF(__pyx_t_5);
  __pyx_t_2 = 0;
  __pyx_t_3 = 0;
  __pyx_t_4 = 0;
  __pyx_t_5 = 0;
  __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_6, NULL); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 547; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRspRemoveParkedOrderAction", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRspQryOrder(PyObject *__pyx_v_self, struct CThostFtdcOrderField *__pyx_v_pOrder, struct CThostFtdcRspInfoField *__pyx_v_pRspInfo, int __pyx_v_nRequestID, bool __pyx_v_bIsLast) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRspQryOrder", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRspQryOrder); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 551; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pOrder == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pOrder)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 551; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 551; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_Order, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 551; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  if (((__pyx_v_pRspInfo == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_3 = Py_None;
  } else {
    __pyx_t_4 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspInfo)); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 551; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_5 = PyTuple_New(1); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 551; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_5);
    PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_4);
    __Pyx_GIVEREF(__pyx_t_4);
    __pyx_t_4 = 0;
    __pyx_t_4 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspInfo, __pyx_t_5, NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 551; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_3 = __pyx_t_4;
    __pyx_t_4 = 0;
  }
  __pyx_t_4 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 551; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = __Pyx_PyBool_FromLong(__pyx_v_bIsLast); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 551; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_6 = PyTuple_New(4); if (unlikely(!__pyx_t_6)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 551; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_6);
  PyTuple_SET_ITEM(__pyx_t_6, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_6, 1, __pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_6, 2, __pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_6, 3, __pyx_t_5);
  __Pyx_GIVEREF(__pyx_t_5);
  __pyx_t_2 = 0;
  __pyx_t_3 = 0;
  __pyx_t_4 = 0;
  __pyx_t_5 = 0;
  __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_6, NULL); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 551; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRspQryOrder", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRspQryTrade(PyObject *__pyx_v_self, struct CThostFtdcTradeField *__pyx_v_pTrade, struct CThostFtdcRspInfoField *__pyx_v_pRspInfo, int __pyx_v_nRequestID, bool __pyx_v_bIsLast) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRspQryTrade", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRspQryTrade); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 555; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pTrade == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pTrade)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 555; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 555; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_Trade, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 555; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  if (((__pyx_v_pRspInfo == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_3 = Py_None;
  } else {
    __pyx_t_4 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspInfo)); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 555; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_5 = PyTuple_New(1); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 555; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_5);
    PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_4);
    __Pyx_GIVEREF(__pyx_t_4);
    __pyx_t_4 = 0;
    __pyx_t_4 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspInfo, __pyx_t_5, NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 555; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_3 = __pyx_t_4;
    __pyx_t_4 = 0;
  }
  __pyx_t_4 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 555; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = __Pyx_PyBool_FromLong(__pyx_v_bIsLast); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 555; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_6 = PyTuple_New(4); if (unlikely(!__pyx_t_6)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 555; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_6);
  PyTuple_SET_ITEM(__pyx_t_6, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_6, 1, __pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_6, 2, __pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_6, 3, __pyx_t_5);
  __Pyx_GIVEREF(__pyx_t_5);
  __pyx_t_2 = 0;
  __pyx_t_3 = 0;
  __pyx_t_4 = 0;
  __pyx_t_5 = 0;
  __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_6, NULL); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 555; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRspQryTrade", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRspQryInvestorPosition(PyObject *__pyx_v_self, struct CThostFtdcInvestorPositionField *__pyx_v_pInvestorPosition, struct CThostFtdcRspInfoField *__pyx_v_pRspInfo, int __pyx_v_nRequestID, bool __pyx_v_bIsLast) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRspQryInvestorPosition", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRspQryInvestorPosition); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 559; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pInvestorPosition == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pInvestorPosition)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 559; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 559; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_InvestorPosition, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 559; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  if (((__pyx_v_pRspInfo == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_3 = Py_None;
  } else {
    __pyx_t_4 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspInfo)); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 559; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_5 = PyTuple_New(1); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 559; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_5);
    PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_4);
    __Pyx_GIVEREF(__pyx_t_4);
    __pyx_t_4 = 0;
    __pyx_t_4 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspInfo, __pyx_t_5, NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 559; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_3 = __pyx_t_4;
    __pyx_t_4 = 0;
  }
  __pyx_t_4 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 559; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = __Pyx_PyBool_FromLong(__pyx_v_bIsLast); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 559; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_6 = PyTuple_New(4); if (unlikely(!__pyx_t_6)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 559; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_6);
  PyTuple_SET_ITEM(__pyx_t_6, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_6, 1, __pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_6, 2, __pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_6, 3, __pyx_t_5);
  __Pyx_GIVEREF(__pyx_t_5);
  __pyx_t_2 = 0;
  __pyx_t_3 = 0;
  __pyx_t_4 = 0;
  __pyx_t_5 = 0;
  __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_6, NULL); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 559; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRspQryInvestorPosition", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRspQryTradingAccount(PyObject *__pyx_v_self, struct CThostFtdcTradingAccountField *__pyx_v_pTradingAccount, struct CThostFtdcRspInfoField *__pyx_v_pRspInfo, int __pyx_v_nRequestID, bool __pyx_v_bIsLast) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRspQryTradingAccount", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRspQryTradingAccount); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 563; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pTradingAccount == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pTradingAccount)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 563; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 563; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_TradingAccount, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 563; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  if (((__pyx_v_pRspInfo == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_3 = Py_None;
  } else {
    __pyx_t_4 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspInfo)); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 563; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_5 = PyTuple_New(1); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 563; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_5);
    PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_4);
    __Pyx_GIVEREF(__pyx_t_4);
    __pyx_t_4 = 0;
    __pyx_t_4 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspInfo, __pyx_t_5, NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 563; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_3 = __pyx_t_4;
    __pyx_t_4 = 0;
  }
  __pyx_t_4 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 563; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = __Pyx_PyBool_FromLong(__pyx_v_bIsLast); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 563; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_6 = PyTuple_New(4); if (unlikely(!__pyx_t_6)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 563; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_6);
  PyTuple_SET_ITEM(__pyx_t_6, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_6, 1, __pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_6, 2, __pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_6, 3, __pyx_t_5);
  __Pyx_GIVEREF(__pyx_t_5);
  __pyx_t_2 = 0;
  __pyx_t_3 = 0;
  __pyx_t_4 = 0;
  __pyx_t_5 = 0;
  __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_6, NULL); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 563; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRspQryTradingAccount", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRspQryInvestor(PyObject *__pyx_v_self, struct CThostFtdcInvestorField *__pyx_v_pInvestor, struct CThostFtdcRspInfoField *__pyx_v_pRspInfo, int __pyx_v_nRequestID, bool __pyx_v_bIsLast) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRspQryInvestor", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRspQryInvestor); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 567; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pInvestor == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pInvestor)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 567; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 567; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_Investor, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 567; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  if (((__pyx_v_pRspInfo == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_3 = Py_None;
  } else {
    __pyx_t_4 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspInfo)); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 567; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_5 = PyTuple_New(1); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 567; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_5);
    PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_4);
    __Pyx_GIVEREF(__pyx_t_4);
    __pyx_t_4 = 0;
    __pyx_t_4 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspInfo, __pyx_t_5, NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 567; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_3 = __pyx_t_4;
    __pyx_t_4 = 0;
  }
  __pyx_t_4 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 567; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = __Pyx_PyBool_FromLong(__pyx_v_bIsLast); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 567; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_6 = PyTuple_New(4); if (unlikely(!__pyx_t_6)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 567; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_6);
  PyTuple_SET_ITEM(__pyx_t_6, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_6, 1, __pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_6, 2, __pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_6, 3, __pyx_t_5);
  __Pyx_GIVEREF(__pyx_t_5);
  __pyx_t_2 = 0;
  __pyx_t_3 = 0;
  __pyx_t_4 = 0;
  __pyx_t_5 = 0;
  __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_6, NULL); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 567; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRspQryInvestor", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRspQryTradingCode(PyObject *__pyx_v_self, struct CThostFtdcTradingCodeField *__pyx_v_pTradingCode, struct CThostFtdcRspInfoField *__pyx_v_pRspInfo, int __pyx_v_nRequestID, bool __pyx_v_bIsLast) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRspQryTradingCode", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRspQryTradingCode); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 571; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pTradingCode == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pTradingCode)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 571; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 571; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_TradingCode, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 571; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  if (((__pyx_v_pRspInfo == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_3 = Py_None;
  } else {
    __pyx_t_4 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspInfo)); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 571; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_5 = PyTuple_New(1); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 571; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_5);
    PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_4);
    __Pyx_GIVEREF(__pyx_t_4);
    __pyx_t_4 = 0;
    __pyx_t_4 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspInfo, __pyx_t_5, NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 571; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_3 = __pyx_t_4;
    __pyx_t_4 = 0;
  }
  __pyx_t_4 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 571; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = __Pyx_PyBool_FromLong(__pyx_v_bIsLast); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 571; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_6 = PyTuple_New(4); if (unlikely(!__pyx_t_6)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 571; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_6);
  PyTuple_SET_ITEM(__pyx_t_6, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_6, 1, __pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_6, 2, __pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_6, 3, __pyx_t_5);
  __Pyx_GIVEREF(__pyx_t_5);
  __pyx_t_2 = 0;
  __pyx_t_3 = 0;
  __pyx_t_4 = 0;
  __pyx_t_5 = 0;
  __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_6, NULL); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 571; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRspQryTradingCode", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRspQryInstrumentMarginRate(PyObject *__pyx_v_self, struct CThostFtdcInstrumentMarginRateField *__pyx_v_pInstrumentMarginRate, struct CThostFtdcRspInfoField *__pyx_v_pRspInfo, int __pyx_v_nRequestID, bool __pyx_v_bIsLast) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRspQryInstrumentMarginRate", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRspQryInstrumentMarginRate); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 575; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pInstrumentMarginRate == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pInstrumentMarginRate)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 575; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 575; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_InstrumentMarginRate, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 575; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  if (((__pyx_v_pRspInfo == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_3 = Py_None;
  } else {
    __pyx_t_4 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspInfo)); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 575; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_5 = PyTuple_New(1); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 575; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_5);
    PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_4);
    __Pyx_GIVEREF(__pyx_t_4);
    __pyx_t_4 = 0;
    __pyx_t_4 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspInfo, __pyx_t_5, NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 575; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_3 = __pyx_t_4;
    __pyx_t_4 = 0;
  }
  __pyx_t_4 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 575; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = __Pyx_PyBool_FromLong(__pyx_v_bIsLast); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 575; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_6 = PyTuple_New(4); if (unlikely(!__pyx_t_6)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 575; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_6);
  PyTuple_SET_ITEM(__pyx_t_6, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_6, 1, __pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_6, 2, __pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_6, 3, __pyx_t_5);
  __Pyx_GIVEREF(__pyx_t_5);
  __pyx_t_2 = 0;
  __pyx_t_3 = 0;
  __pyx_t_4 = 0;
  __pyx_t_5 = 0;
  __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_6, NULL); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 575; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRspQryInstrumentMarginRate", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRspQryInstrumentCommissionRate(PyObject *__pyx_v_self, struct CThostFtdcInstrumentCommissionRateField *__pyx_v_pInstrumentCommissionRate, struct CThostFtdcRspInfoField *__pyx_v_pRspInfo, int __pyx_v_nRequestID, bool __pyx_v_bIsLast) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRspQryInstrumentCommissionRate", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRspQryInstrumentCommissionRate); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 579; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pInstrumentCommissionRate == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pInstrumentCommissionRate)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 579; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 579; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_InstrumentCommissionRate, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 579; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  if (((__pyx_v_pRspInfo == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_3 = Py_None;
  } else {
    __pyx_t_4 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspInfo)); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 579; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_5 = PyTuple_New(1); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 579; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_5);
    PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_4);
    __Pyx_GIVEREF(__pyx_t_4);
    __pyx_t_4 = 0;
    __pyx_t_4 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspInfo, __pyx_t_5, NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 579; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_3 = __pyx_t_4;
    __pyx_t_4 = 0;
  }
  __pyx_t_4 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 579; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = __Pyx_PyBool_FromLong(__pyx_v_bIsLast); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 579; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_6 = PyTuple_New(4); if (unlikely(!__pyx_t_6)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 579; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_6);
  PyTuple_SET_ITEM(__pyx_t_6, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_6, 1, __pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_6, 2, __pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_6, 3, __pyx_t_5);
  __Pyx_GIVEREF(__pyx_t_5);
  __pyx_t_2 = 0;
  __pyx_t_3 = 0;
  __pyx_t_4 = 0;
  __pyx_t_5 = 0;
  __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_6, NULL); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 579; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRspQryInstrumentCommissionRate", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRspQryExchange(PyObject *__pyx_v_self, struct CThostFtdcExchangeField *__pyx_v_pExchange, struct CThostFtdcRspInfoField *__pyx_v_pRspInfo, int __pyx_v_nRequestID, bool __pyx_v_bIsLast) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRspQryExchange", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRspQryExchange); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 583; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pExchange == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pExchange)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 583; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 583; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_Exchange, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 583; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  if (((__pyx_v_pRspInfo == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_3 = Py_None;
  } else {
    __pyx_t_4 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspInfo)); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 583; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_5 = PyTuple_New(1); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 583; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_5);
    PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_4);
    __Pyx_GIVEREF(__pyx_t_4);
    __pyx_t_4 = 0;
    __pyx_t_4 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspInfo, __pyx_t_5, NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 583; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_3 = __pyx_t_4;
    __pyx_t_4 = 0;
  }
  __pyx_t_4 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 583; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = __Pyx_PyBool_FromLong(__pyx_v_bIsLast); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 583; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_6 = PyTuple_New(4); if (unlikely(!__pyx_t_6)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 583; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_6);
  PyTuple_SET_ITEM(__pyx_t_6, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_6, 1, __pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_6, 2, __pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_6, 3, __pyx_t_5);
  __Pyx_GIVEREF(__pyx_t_5);
  __pyx_t_2 = 0;
  __pyx_t_3 = 0;
  __pyx_t_4 = 0;
  __pyx_t_5 = 0;
  __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_6, NULL); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 583; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRspQryExchange", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRspQryProduct(PyObject *__pyx_v_self, struct CThostFtdcProductField *__pyx_v_pProduct, struct CThostFtdcRspInfoField *__pyx_v_pRspInfo, int __pyx_v_nRequestID, bool __pyx_v_bIsLast) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRspQryProduct", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRspQryProduct); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 587; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pProduct == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pProduct)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 587; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 587; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_Product, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 587; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  if (((__pyx_v_pRspInfo == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_3 = Py_None;
  } else {
    __pyx_t_4 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspInfo)); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 587; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_5 = PyTuple_New(1); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 587; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_5);
    PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_4);
    __Pyx_GIVEREF(__pyx_t_4);
    __pyx_t_4 = 0;
    __pyx_t_4 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspInfo, __pyx_t_5, NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 587; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_3 = __pyx_t_4;
    __pyx_t_4 = 0;
  }
  __pyx_t_4 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 587; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = __Pyx_PyBool_FromLong(__pyx_v_bIsLast); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 587; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_6 = PyTuple_New(4); if (unlikely(!__pyx_t_6)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 587; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_6);
  PyTuple_SET_ITEM(__pyx_t_6, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_6, 1, __pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_6, 2, __pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_6, 3, __pyx_t_5);
  __Pyx_GIVEREF(__pyx_t_5);
  __pyx_t_2 = 0;
  __pyx_t_3 = 0;
  __pyx_t_4 = 0;
  __pyx_t_5 = 0;
  __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_6, NULL); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 587; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRspQryProduct", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRspQryInstrument(PyObject *__pyx_v_self, struct CThostFtdcInstrumentField *__pyx_v_pInstrument, struct CThostFtdcRspInfoField *__pyx_v_pRspInfo, int __pyx_v_nRequestID, bool __pyx_v_bIsLast) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRspQryInstrument", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRspQryInstrument); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 591; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pInstrument == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pInstrument)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 591; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 591; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_Instrument, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 591; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  if (((__pyx_v_pRspInfo == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_3 = Py_None;
  } else {
    __pyx_t_4 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspInfo)); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 591; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_5 = PyTuple_New(1); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 591; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_5);
    PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_4);
    __Pyx_GIVEREF(__pyx_t_4);
    __pyx_t_4 = 0;
    __pyx_t_4 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspInfo, __pyx_t_5, NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 591; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_3 = __pyx_t_4;
    __pyx_t_4 = 0;
  }
  __pyx_t_4 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 591; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = __Pyx_PyBool_FromLong(__pyx_v_bIsLast); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 591; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_6 = PyTuple_New(4); if (unlikely(!__pyx_t_6)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 591; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_6);
  PyTuple_SET_ITEM(__pyx_t_6, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_6, 1, __pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_6, 2, __pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_6, 3, __pyx_t_5);
  __Pyx_GIVEREF(__pyx_t_5);
  __pyx_t_2 = 0;
  __pyx_t_3 = 0;
  __pyx_t_4 = 0;
  __pyx_t_5 = 0;
  __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_6, NULL); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 591; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRspQryInstrument", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRspQryDepthMarketData(PyObject *__pyx_v_self, struct CThostFtdcDepthMarketDataField *__pyx_v_pDepthMarketData, struct CThostFtdcRspInfoField *__pyx_v_pRspInfo, int __pyx_v_nRequestID, bool __pyx_v_bIsLast) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRspQryDepthMarketData", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRspQryDepthMarketData); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 595; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pDepthMarketData == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pDepthMarketData)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 595; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 595; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_DepthMarketData, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 595; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  if (((__pyx_v_pRspInfo == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_3 = Py_None;
  } else {
    __pyx_t_4 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspInfo)); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 595; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_5 = PyTuple_New(1); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 595; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_5);
    PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_4);
    __Pyx_GIVEREF(__pyx_t_4);
    __pyx_t_4 = 0;
    __pyx_t_4 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspInfo, __pyx_t_5, NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 595; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_3 = __pyx_t_4;
    __pyx_t_4 = 0;
  }
  __pyx_t_4 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 595; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = __Pyx_PyBool_FromLong(__pyx_v_bIsLast); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 595; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_6 = PyTuple_New(4); if (unlikely(!__pyx_t_6)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 595; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_6);
  PyTuple_SET_ITEM(__pyx_t_6, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_6, 1, __pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_6, 2, __pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_6, 3, __pyx_t_5);
  __Pyx_GIVEREF(__pyx_t_5);
  __pyx_t_2 = 0;
  __pyx_t_3 = 0;
  __pyx_t_4 = 0;
  __pyx_t_5 = 0;
  __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_6, NULL); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 595; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRspQryDepthMarketData", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRspQrySettlementInfo(PyObject *__pyx_v_self, struct CThostFtdcSettlementInfoField *__pyx_v_pSettlementInfo, struct CThostFtdcRspInfoField *__pyx_v_pRspInfo, int __pyx_v_nRequestID, bool __pyx_v_bIsLast) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRspQrySettlementInfo", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRspQrySettlementInfo); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 599; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pSettlementInfo == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pSettlementInfo)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 599; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 599; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_SettlementInfo, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 599; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  if (((__pyx_v_pRspInfo == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_3 = Py_None;
  } else {
    __pyx_t_4 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspInfo)); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 599; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_5 = PyTuple_New(1); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 599; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_5);
    PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_4);
    __Pyx_GIVEREF(__pyx_t_4);
    __pyx_t_4 = 0;
    __pyx_t_4 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspInfo, __pyx_t_5, NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 599; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_3 = __pyx_t_4;
    __pyx_t_4 = 0;
  }
  __pyx_t_4 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 599; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = __Pyx_PyBool_FromLong(__pyx_v_bIsLast); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 599; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_6 = PyTuple_New(4); if (unlikely(!__pyx_t_6)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 599; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_6);
  PyTuple_SET_ITEM(__pyx_t_6, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_6, 1, __pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_6, 2, __pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_6, 3, __pyx_t_5);
  __Pyx_GIVEREF(__pyx_t_5);
  __pyx_t_2 = 0;
  __pyx_t_3 = 0;
  __pyx_t_4 = 0;
  __pyx_t_5 = 0;
  __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_6, NULL); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 599; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRspQrySettlementInfo", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRspQryTransferBank(PyObject *__pyx_v_self, struct CThostFtdcTransferBankField *__pyx_v_pTransferBank, struct CThostFtdcRspInfoField *__pyx_v_pRspInfo, int __pyx_v_nRequestID, bool __pyx_v_bIsLast) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRspQryTransferBank", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRspQryTransferBank); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 603; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pTransferBank == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pTransferBank)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 603; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 603; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_TransferBank, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 603; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  if (((__pyx_v_pRspInfo == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_3 = Py_None;
  } else {
    __pyx_t_4 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspInfo)); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 603; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_5 = PyTuple_New(1); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 603; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_5);
    PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_4);
    __Pyx_GIVEREF(__pyx_t_4);
    __pyx_t_4 = 0;
    __pyx_t_4 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspInfo, __pyx_t_5, NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 603; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_3 = __pyx_t_4;
    __pyx_t_4 = 0;
  }
  __pyx_t_4 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 603; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = __Pyx_PyBool_FromLong(__pyx_v_bIsLast); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 603; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_6 = PyTuple_New(4); if (unlikely(!__pyx_t_6)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 603; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_6);
  PyTuple_SET_ITEM(__pyx_t_6, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_6, 1, __pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_6, 2, __pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_6, 3, __pyx_t_5);
  __Pyx_GIVEREF(__pyx_t_5);
  __pyx_t_2 = 0;
  __pyx_t_3 = 0;
  __pyx_t_4 = 0;
  __pyx_t_5 = 0;
  __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_6, NULL); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 603; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRspQryTransferBank", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRspQryInvestorPositionDetail(PyObject *__pyx_v_self, struct CThostFtdcInvestorPositionDetailField *__pyx_v_pInvestorPositionDetail, struct CThostFtdcRspInfoField *__pyx_v_pRspInfo, int __pyx_v_nRequestID, bool __pyx_v_bIsLast) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRspQryInvestorPositionDetail", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRspQryInvestorPositionDetail); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 607; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pInvestorPositionDetail == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pInvestorPositionDetail)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 607; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 607; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_InvestorPositionDetail, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 607; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  if (((__pyx_v_pRspInfo == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_3 = Py_None;
  } else {
    __pyx_t_4 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspInfo)); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 607; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_5 = PyTuple_New(1); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 607; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_5);
    PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_4);
    __Pyx_GIVEREF(__pyx_t_4);
    __pyx_t_4 = 0;
    __pyx_t_4 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspInfo, __pyx_t_5, NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 607; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_3 = __pyx_t_4;
    __pyx_t_4 = 0;
  }
  __pyx_t_4 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 607; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = __Pyx_PyBool_FromLong(__pyx_v_bIsLast); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 607; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_6 = PyTuple_New(4); if (unlikely(!__pyx_t_6)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 607; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_6);
  PyTuple_SET_ITEM(__pyx_t_6, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_6, 1, __pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_6, 2, __pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_6, 3, __pyx_t_5);
  __Pyx_GIVEREF(__pyx_t_5);
  __pyx_t_2 = 0;
  __pyx_t_3 = 0;
  __pyx_t_4 = 0;
  __pyx_t_5 = 0;
  __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_6, NULL); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 607; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRspQryInvestorPositionDetail", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRspQryNotice(PyObject *__pyx_v_self, struct CThostFtdcNoticeField *__pyx_v_pNotice, struct CThostFtdcRspInfoField *__pyx_v_pRspInfo, int __pyx_v_nRequestID, bool __pyx_v_bIsLast) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRspQryNotice", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRspQryNotice); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 611; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pNotice == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pNotice)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 611; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 611; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_Notice, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 611; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  if (((__pyx_v_pRspInfo == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_3 = Py_None;
  } else {
    __pyx_t_4 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspInfo)); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 611; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_5 = PyTuple_New(1); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 611; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_5);
    PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_4);
    __Pyx_GIVEREF(__pyx_t_4);
    __pyx_t_4 = 0;
    __pyx_t_4 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspInfo, __pyx_t_5, NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 611; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_3 = __pyx_t_4;
    __pyx_t_4 = 0;
  }
  __pyx_t_4 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 611; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = __Pyx_PyBool_FromLong(__pyx_v_bIsLast); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 611; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_6 = PyTuple_New(4); if (unlikely(!__pyx_t_6)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 611; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_6);
  PyTuple_SET_ITEM(__pyx_t_6, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_6, 1, __pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_6, 2, __pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_6, 3, __pyx_t_5);
  __Pyx_GIVEREF(__pyx_t_5);
  __pyx_t_2 = 0;
  __pyx_t_3 = 0;
  __pyx_t_4 = 0;
  __pyx_t_5 = 0;
  __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_6, NULL); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 611; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRspQryNotice", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRspQrySettlementInfoConfirm(PyObject *__pyx_v_self, struct CThostFtdcSettlementInfoConfirmField *__pyx_v_pSettlementInfoConfirm, struct CThostFtdcRspInfoField *__pyx_v_pRspInfo, int __pyx_v_nRequestID, bool __pyx_v_bIsLast) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRspQrySettlementInfoConfirm", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRspQrySettlementInfoConfirm); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 615; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pSettlementInfoConfirm == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pSettlementInfoConfirm)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 615; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 615; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_SettlementInfoConfirm, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 615; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  if (((__pyx_v_pRspInfo == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_3 = Py_None;
  } else {
    __pyx_t_4 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspInfo)); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 615; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_5 = PyTuple_New(1); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 615; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_5);
    PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_4);
    __Pyx_GIVEREF(__pyx_t_4);
    __pyx_t_4 = 0;
    __pyx_t_4 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspInfo, __pyx_t_5, NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 615; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_3 = __pyx_t_4;
    __pyx_t_4 = 0;
  }
  __pyx_t_4 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 615; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = __Pyx_PyBool_FromLong(__pyx_v_bIsLast); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 615; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_6 = PyTuple_New(4); if (unlikely(!__pyx_t_6)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 615; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_6);
  PyTuple_SET_ITEM(__pyx_t_6, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_6, 1, __pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_6, 2, __pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_6, 3, __pyx_t_5);
  __Pyx_GIVEREF(__pyx_t_5);
  __pyx_t_2 = 0;
  __pyx_t_3 = 0;
  __pyx_t_4 = 0;
  __pyx_t_5 = 0;
  __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_6, NULL); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 615; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRspQrySettlementInfoConfirm", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRspQryInvestorPositionCombineDetail(PyObject *__pyx_v_self, struct CThostFtdcInvestorPositionCombineDetailField *__pyx_v_pInvestorPositionCombineDetail, struct CThostFtdcRspInfoField *__pyx_v_pRspInfo, int __pyx_v_nRequestID, bool __pyx_v_bIsLast) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRspQryInvestorPositionCombineDetail", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRspQryInvestorPositionCombineD); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 619; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pInvestorPositionCombineDetail == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pInvestorPositionCombineDetail)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 619; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 619; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_InvestorPositionCombineDetail, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 619; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  if (((__pyx_v_pRspInfo == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_3 = Py_None;
  } else {
    __pyx_t_4 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspInfo)); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 619; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_5 = PyTuple_New(1); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 619; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_5);
    PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_4);
    __Pyx_GIVEREF(__pyx_t_4);
    __pyx_t_4 = 0;
    __pyx_t_4 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspInfo, __pyx_t_5, NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 619; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_3 = __pyx_t_4;
    __pyx_t_4 = 0;
  }
  __pyx_t_4 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 619; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = __Pyx_PyBool_FromLong(__pyx_v_bIsLast); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 619; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_6 = PyTuple_New(4); if (unlikely(!__pyx_t_6)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 619; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_6);
  PyTuple_SET_ITEM(__pyx_t_6, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_6, 1, __pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_6, 2, __pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_6, 3, __pyx_t_5);
  __Pyx_GIVEREF(__pyx_t_5);
  __pyx_t_2 = 0;
  __pyx_t_3 = 0;
  __pyx_t_4 = 0;
  __pyx_t_5 = 0;
  __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_6, NULL); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 619; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRspQryInvestorPositionCombineDetail", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRspQryCFMMCTradingAccountKey(PyObject *__pyx_v_self, struct CThostFtdcCFMMCTradingAccountKeyField *__pyx_v_pCFMMCTradingAccountKey, struct CThostFtdcRspInfoField *__pyx_v_pRspInfo, int __pyx_v_nRequestID, bool __pyx_v_bIsLast) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRspQryCFMMCTradingAccountKey", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRspQryCFMMCTradingAccountKey); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 623; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pCFMMCTradingAccountKey == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pCFMMCTradingAccountKey)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 623; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 623; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_CFMMCTradingAccountKey, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 623; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  if (((__pyx_v_pRspInfo == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_3 = Py_None;
  } else {
    __pyx_t_4 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspInfo)); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 623; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_5 = PyTuple_New(1); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 623; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_5);
    PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_4);
    __Pyx_GIVEREF(__pyx_t_4);
    __pyx_t_4 = 0;
    __pyx_t_4 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspInfo, __pyx_t_5, NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 623; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_3 = __pyx_t_4;
    __pyx_t_4 = 0;
  }
  __pyx_t_4 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 623; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = __Pyx_PyBool_FromLong(__pyx_v_bIsLast); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 623; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_6 = PyTuple_New(4); if (unlikely(!__pyx_t_6)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 623; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_6);
  PyTuple_SET_ITEM(__pyx_t_6, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_6, 1, __pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_6, 2, __pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_6, 3, __pyx_t_5);
  __Pyx_GIVEREF(__pyx_t_5);
  __pyx_t_2 = 0;
  __pyx_t_3 = 0;
  __pyx_t_4 = 0;
  __pyx_t_5 = 0;
  __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_6, NULL); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 623; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRspQryCFMMCTradingAccountKey", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRspQryEWarrantOffset(PyObject *__pyx_v_self, struct CThostFtdcEWarrantOffsetField *__pyx_v_pEWarrantOffset, struct CThostFtdcRspInfoField *__pyx_v_pRspInfo, int __pyx_v_nRequestID, bool __pyx_v_bIsLast) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRspQryEWarrantOffset", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRspQryEWarrantOffset); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 627; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pEWarrantOffset == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pEWarrantOffset)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 627; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 627; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_EWarrantOffset, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 627; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  if (((__pyx_v_pRspInfo == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_3 = Py_None;
  } else {
    __pyx_t_4 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspInfo)); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 627; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_5 = PyTuple_New(1); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 627; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_5);
    PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_4);
    __Pyx_GIVEREF(__pyx_t_4);
    __pyx_t_4 = 0;
    __pyx_t_4 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspInfo, __pyx_t_5, NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 627; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_3 = __pyx_t_4;
    __pyx_t_4 = 0;
  }
  __pyx_t_4 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 627; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = __Pyx_PyBool_FromLong(__pyx_v_bIsLast); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 627; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_6 = PyTuple_New(4); if (unlikely(!__pyx_t_6)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 627; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_6);
  PyTuple_SET_ITEM(__pyx_t_6, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_6, 1, __pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_6, 2, __pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_6, 3, __pyx_t_5);
  __Pyx_GIVEREF(__pyx_t_5);
  __pyx_t_2 = 0;
  __pyx_t_3 = 0;
  __pyx_t_4 = 0;
  __pyx_t_5 = 0;
  __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_6, NULL); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 627; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRspQryEWarrantOffset", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRspQryInvestorProductGroupMargin(PyObject *__pyx_v_self, struct CThostFtdcInvestorProductGroupMarginField *__pyx_v_pInvestorProductGroupMargin, struct CThostFtdcRspInfoField *__pyx_v_pRspInfo, int __pyx_v_nRequestID, bool __pyx_v_bIsLast) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRspQryInvestorProductGroupMargin", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRspQryInvestorProductGroupMarg); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 631; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pInvestorProductGroupMargin == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pInvestorProductGroupMargin)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 631; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 631; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_InvestorProductGroupMargin, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 631; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  if (((__pyx_v_pRspInfo == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_3 = Py_None;
  } else {
    __pyx_t_4 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspInfo)); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 631; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_5 = PyTuple_New(1); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 631; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_5);
    PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_4);
    __Pyx_GIVEREF(__pyx_t_4);
    __pyx_t_4 = 0;
    __pyx_t_4 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspInfo, __pyx_t_5, NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 631; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_3 = __pyx_t_4;
    __pyx_t_4 = 0;
  }
  __pyx_t_4 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 631; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = __Pyx_PyBool_FromLong(__pyx_v_bIsLast); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 631; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_6 = PyTuple_New(4); if (unlikely(!__pyx_t_6)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 631; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_6);
  PyTuple_SET_ITEM(__pyx_t_6, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_6, 1, __pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_6, 2, __pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_6, 3, __pyx_t_5);
  __Pyx_GIVEREF(__pyx_t_5);
  __pyx_t_2 = 0;
  __pyx_t_3 = 0;
  __pyx_t_4 = 0;
  __pyx_t_5 = 0;
  __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_6, NULL); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 631; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRspQryInvestorProductGroupMargin", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRspQryExchangeMarginRate(PyObject *__pyx_v_self, struct CThostFtdcExchangeMarginRateField *__pyx_v_pExchangeMarginRate, struct CThostFtdcRspInfoField *__pyx_v_pRspInfo, int __pyx_v_nRequestID, bool __pyx_v_bIsLast) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRspQryExchangeMarginRate", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRspQryExchangeMarginRate); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 635; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pExchangeMarginRate == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pExchangeMarginRate)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 635; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 635; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_ExchangeMarginRate, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 635; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  if (((__pyx_v_pRspInfo == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_3 = Py_None;
  } else {
    __pyx_t_4 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspInfo)); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 635; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_5 = PyTuple_New(1); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 635; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_5);
    PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_4);
    __Pyx_GIVEREF(__pyx_t_4);
    __pyx_t_4 = 0;
    __pyx_t_4 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspInfo, __pyx_t_5, NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 635; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_3 = __pyx_t_4;
    __pyx_t_4 = 0;
  }
  __pyx_t_4 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 635; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = __Pyx_PyBool_FromLong(__pyx_v_bIsLast); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 635; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_6 = PyTuple_New(4); if (unlikely(!__pyx_t_6)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 635; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_6);
  PyTuple_SET_ITEM(__pyx_t_6, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_6, 1, __pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_6, 2, __pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_6, 3, __pyx_t_5);
  __Pyx_GIVEREF(__pyx_t_5);
  __pyx_t_2 = 0;
  __pyx_t_3 = 0;
  __pyx_t_4 = 0;
  __pyx_t_5 = 0;
  __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_6, NULL); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 635; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRspQryExchangeMarginRate", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRspQryExchangeMarginRateAdjust(PyObject *__pyx_v_self, struct CThostFtdcExchangeMarginRateAdjustField *__pyx_v_pExchangeMarginRateAdjust, struct CThostFtdcRspInfoField *__pyx_v_pRspInfo, int __pyx_v_nRequestID, bool __pyx_v_bIsLast) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRspQryExchangeMarginRateAdjust", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRspQryExchangeMarginRateAdjust); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 639; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pExchangeMarginRateAdjust == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pExchangeMarginRateAdjust)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 639; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 639; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_ExchangeMarginRateAdjust, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 639; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  if (((__pyx_v_pRspInfo == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_3 = Py_None;
  } else {
    __pyx_t_4 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspInfo)); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 639; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_5 = PyTuple_New(1); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 639; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_5);
    PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_4);
    __Pyx_GIVEREF(__pyx_t_4);
    __pyx_t_4 = 0;
    __pyx_t_4 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspInfo, __pyx_t_5, NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 639; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_3 = __pyx_t_4;
    __pyx_t_4 = 0;
  }
  __pyx_t_4 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 639; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = __Pyx_PyBool_FromLong(__pyx_v_bIsLast); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 639; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_6 = PyTuple_New(4); if (unlikely(!__pyx_t_6)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 639; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_6);
  PyTuple_SET_ITEM(__pyx_t_6, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_6, 1, __pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_6, 2, __pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_6, 3, __pyx_t_5);
  __Pyx_GIVEREF(__pyx_t_5);
  __pyx_t_2 = 0;
  __pyx_t_3 = 0;
  __pyx_t_4 = 0;
  __pyx_t_5 = 0;
  __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_6, NULL); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 639; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRspQryExchangeMarginRateAdjust", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRspQryExchangeRate(PyObject *__pyx_v_self, struct CThostFtdcExchangeRateField *__pyx_v_pExchangeRate, struct CThostFtdcRspInfoField *__pyx_v_pRspInfo, int __pyx_v_nRequestID, bool __pyx_v_bIsLast) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRspQryExchangeRate", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRspQryExchangeRate); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 643; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pExchangeRate == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pExchangeRate)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 643; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 643; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_ExchangeRate, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 643; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  if (((__pyx_v_pRspInfo == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_3 = Py_None;
  } else {
    __pyx_t_4 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspInfo)); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 643; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_5 = PyTuple_New(1); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 643; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_5);
    PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_4);
    __Pyx_GIVEREF(__pyx_t_4);
    __pyx_t_4 = 0;
    __pyx_t_4 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspInfo, __pyx_t_5, NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 643; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_3 = __pyx_t_4;
    __pyx_t_4 = 0;
  }
  __pyx_t_4 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 643; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = __Pyx_PyBool_FromLong(__pyx_v_bIsLast); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 643; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_6 = PyTuple_New(4); if (unlikely(!__pyx_t_6)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 643; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_6);
  PyTuple_SET_ITEM(__pyx_t_6, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_6, 1, __pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_6, 2, __pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_6, 3, __pyx_t_5);
  __Pyx_GIVEREF(__pyx_t_5);
  __pyx_t_2 = 0;
  __pyx_t_3 = 0;
  __pyx_t_4 = 0;
  __pyx_t_5 = 0;
  __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_6, NULL); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 643; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRspQryExchangeRate", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRspQrySecAgentACIDMap(PyObject *__pyx_v_self, struct CThostFtdcSecAgentACIDMapField *__pyx_v_pSecAgentACIDMap, struct CThostFtdcRspInfoField *__pyx_v_pRspInfo, int __pyx_v_nRequestID, bool __pyx_v_bIsLast) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRspQrySecAgentACIDMap", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRspQrySecAgentACIDMap); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 647; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pSecAgentACIDMap == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pSecAgentACIDMap)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 647; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 647; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_SecAgentACIDMap, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 647; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  if (((__pyx_v_pRspInfo == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_3 = Py_None;
  } else {
    __pyx_t_4 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspInfo)); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 647; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_5 = PyTuple_New(1); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 647; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_5);
    PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_4);
    __Pyx_GIVEREF(__pyx_t_4);
    __pyx_t_4 = 0;
    __pyx_t_4 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspInfo, __pyx_t_5, NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 647; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_3 = __pyx_t_4;
    __pyx_t_4 = 0;
  }
  __pyx_t_4 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 647; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = __Pyx_PyBool_FromLong(__pyx_v_bIsLast); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 647; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_6 = PyTuple_New(4); if (unlikely(!__pyx_t_6)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 647; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_6);
  PyTuple_SET_ITEM(__pyx_t_6, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_6, 1, __pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_6, 2, __pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_6, 3, __pyx_t_5);
  __Pyx_GIVEREF(__pyx_t_5);
  __pyx_t_2 = 0;
  __pyx_t_3 = 0;
  __pyx_t_4 = 0;
  __pyx_t_5 = 0;
  __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_6, NULL); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 647; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRspQrySecAgentACIDMap", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRspQryTransferSerial(PyObject *__pyx_v_self, struct CThostFtdcTransferSerialField *__pyx_v_pTransferSerial, struct CThostFtdcRspInfoField *__pyx_v_pRspInfo, int __pyx_v_nRequestID, bool __pyx_v_bIsLast) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRspQryTransferSerial", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRspQryTransferSerial); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 651; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pTransferSerial == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pTransferSerial)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 651; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 651; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_TransferSerial, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 651; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  if (((__pyx_v_pRspInfo == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_3 = Py_None;
  } else {
    __pyx_t_4 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspInfo)); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 651; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_5 = PyTuple_New(1); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 651; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_5);
    PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_4);
    __Pyx_GIVEREF(__pyx_t_4);
    __pyx_t_4 = 0;
    __pyx_t_4 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspInfo, __pyx_t_5, NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 651; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_3 = __pyx_t_4;
    __pyx_t_4 = 0;
  }
  __pyx_t_4 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 651; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = __Pyx_PyBool_FromLong(__pyx_v_bIsLast); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 651; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_6 = PyTuple_New(4); if (unlikely(!__pyx_t_6)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 651; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_6);
  PyTuple_SET_ITEM(__pyx_t_6, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_6, 1, __pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_6, 2, __pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_6, 3, __pyx_t_5);
  __Pyx_GIVEREF(__pyx_t_5);
  __pyx_t_2 = 0;
  __pyx_t_3 = 0;
  __pyx_t_4 = 0;
  __pyx_t_5 = 0;
  __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_6, NULL); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 651; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRspQryTransferSerial", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRspQryAccountregister(PyObject *__pyx_v_self, struct CThostFtdcAccountregisterField *__pyx_v_pAccountregister, struct CThostFtdcRspInfoField *__pyx_v_pRspInfo, int __pyx_v_nRequestID, bool __pyx_v_bIsLast) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRspQryAccountregister", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRspQryAccountregister); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 655; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pAccountregister == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pAccountregister)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 655; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 655; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_Accountregister, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 655; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  if (((__pyx_v_pRspInfo == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_3 = Py_None;
  } else {
    __pyx_t_4 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspInfo)); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 655; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_5 = PyTuple_New(1); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 655; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_5);
    PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_4);
    __Pyx_GIVEREF(__pyx_t_4);
    __pyx_t_4 = 0;
    __pyx_t_4 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspInfo, __pyx_t_5, NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 655; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_3 = __pyx_t_4;
    __pyx_t_4 = 0;
  }
  __pyx_t_4 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 655; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = __Pyx_PyBool_FromLong(__pyx_v_bIsLast); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 655; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_6 = PyTuple_New(4); if (unlikely(!__pyx_t_6)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 655; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_6);
  PyTuple_SET_ITEM(__pyx_t_6, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_6, 1, __pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_6, 2, __pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_6, 3, __pyx_t_5);
  __Pyx_GIVEREF(__pyx_t_5);
  __pyx_t_2 = 0;
  __pyx_t_3 = 0;
  __pyx_t_4 = 0;
  __pyx_t_5 = 0;
  __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_6, NULL); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 655; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRspQryAccountregister", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRspError(PyObject *__pyx_v_self, struct CThostFtdcRspInfoField *__pyx_v_pRspInfo, int __pyx_v_nRequestID, bool __pyx_v_bIsLast) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRspError", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRspError); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 659; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pRspInfo == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspInfo)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 659; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 659; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspInfo, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 659; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  __pyx_t_3 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 659; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_4 = __Pyx_PyBool_FromLong(__pyx_v_bIsLast); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 659; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = PyTuple_New(3); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 659; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_5, 1, __pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_5, 2, __pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  __pyx_t_2 = 0;
  __pyx_t_3 = 0;
  __pyx_t_4 = 0;
  __pyx_t_4 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_5, NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 659; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRspError", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRtnOrder(PyObject *__pyx_v_self, struct CThostFtdcOrderField *__pyx_v_pOrder) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRtnOrder", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRtnOrder); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 663; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pOrder == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pOrder)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 663; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 663; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_Order, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 663; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  __pyx_t_3 = PyTuple_New(1); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 663; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_3, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_3, NULL); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 663; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRtnOrder", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRtnTrade(PyObject *__pyx_v_self, struct CThostFtdcTradeField *__pyx_v_pTrade) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRtnTrade", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRtnTrade); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 667; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pTrade == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pTrade)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 667; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 667; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_Trade, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 667; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  __pyx_t_3 = PyTuple_New(1); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 667; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_3, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_3, NULL); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 667; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRtnTrade", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnErrRtnOrderInsert(PyObject *__pyx_v_self, struct CThostFtdcInputOrderField *__pyx_v_pInputOrder, struct CThostFtdcRspInfoField *__pyx_v_pRspInfo) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnErrRtnOrderInsert", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnErrRtnOrderInsert); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 671; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pInputOrder == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pInputOrder)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 671; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 671; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_InputOrder, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 671; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  if (((__pyx_v_pRspInfo == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_3 = Py_None;
  } else {
    __pyx_t_4 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspInfo)); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 671; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_5 = PyTuple_New(1); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 671; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_5);
    PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_4);
    __Pyx_GIVEREF(__pyx_t_4);
    __pyx_t_4 = 0;
    __pyx_t_4 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspInfo, __pyx_t_5, NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 671; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_3 = __pyx_t_4;
    __pyx_t_4 = 0;
  }
  __pyx_t_4 = PyTuple_New(2); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 671; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_4, 1, __pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  __pyx_t_2 = 0;
  __pyx_t_3 = 0;
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 671; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnErrRtnOrderInsert", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnErrRtnOrderAction(PyObject *__pyx_v_self, struct CThostFtdcOrderActionField *__pyx_v_pOrderAction, struct CThostFtdcRspInfoField *__pyx_v_pRspInfo) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnErrRtnOrderAction", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnErrRtnOrderAction); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 675; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pOrderAction == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pOrderAction)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 675; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 675; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_OrderAction, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 675; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  if (((__pyx_v_pRspInfo == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_3 = Py_None;
  } else {
    __pyx_t_4 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspInfo)); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 675; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_5 = PyTuple_New(1); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 675; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_5);
    PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_4);
    __Pyx_GIVEREF(__pyx_t_4);
    __pyx_t_4 = 0;
    __pyx_t_4 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspInfo, __pyx_t_5, NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 675; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_3 = __pyx_t_4;
    __pyx_t_4 = 0;
  }
  __pyx_t_4 = PyTuple_New(2); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 675; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_4, 1, __pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  __pyx_t_2 = 0;
  __pyx_t_3 = 0;
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 675; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnErrRtnOrderAction", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRtnInstrumentStatus(PyObject *__pyx_v_self, struct CThostFtdcInstrumentStatusField *__pyx_v_pInstrumentStatus) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRtnInstrumentStatus", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRtnInstrumentStatus); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 679; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pInstrumentStatus == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pInstrumentStatus)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 679; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 679; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_InstrumentStatus, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 679; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  __pyx_t_3 = PyTuple_New(1); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 679; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_3, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_3, NULL); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 679; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRtnInstrumentStatus", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRtnTradingNotice(PyObject *__pyx_v_self, struct CThostFtdcTradingNoticeInfoField *__pyx_v_pTradingNoticeInfo) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRtnTradingNotice", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRtnTradingNotice); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 683; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pTradingNoticeInfo == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pTradingNoticeInfo)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 683; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 683; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_TradingNoticeInfo, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 683; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  __pyx_t_3 = PyTuple_New(1); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 683; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_3, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_3, NULL); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 683; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRtnTradingNotice", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRtnErrorConditionalOrder(PyObject *__pyx_v_self, struct CThostFtdcErrorConditionalOrderField *__pyx_v_pErrorConditionalOrder) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRtnErrorConditionalOrder", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRtnErrorConditionalOrder); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 687; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pErrorConditionalOrder == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pErrorConditionalOrder)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 687; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 687; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_ErrorConditionalOrder, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 687; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  __pyx_t_3 = PyTuple_New(1); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 687; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_3, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_3, NULL); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 687; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRtnErrorConditionalOrder", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRtnCFMMCTradingAccountToken(PyObject *__pyx_v_self, struct CThostFtdcCFMMCTradingAccountTokenField *__pyx_v_pCFMMCTradingAccountToken) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRtnCFMMCTradingAccountToken", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRtnCFMMCTradingAccountToken); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 691; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pCFMMCTradingAccountToken == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pCFMMCTradingAccountToken)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 691; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 691; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_CFMMCTradingAccountToken, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 691; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  __pyx_t_3 = PyTuple_New(1); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 691; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_3, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_3, NULL); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 691; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRtnCFMMCTradingAccountToken", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRspQryContractBank(PyObject *__pyx_v_self, struct CThostFtdcContractBankField *__pyx_v_pContractBank, struct CThostFtdcRspInfoField *__pyx_v_pRspInfo, int __pyx_v_nRequestID, bool __pyx_v_bIsLast) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRspQryContractBank", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRspQryContractBank); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 695; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pContractBank == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pContractBank)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 695; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 695; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_ContractBank, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 695; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  if (((__pyx_v_pRspInfo == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_3 = Py_None;
  } else {
    __pyx_t_4 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspInfo)); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 695; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_5 = PyTuple_New(1); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 695; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_5);
    PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_4);
    __Pyx_GIVEREF(__pyx_t_4);
    __pyx_t_4 = 0;
    __pyx_t_4 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspInfo, __pyx_t_5, NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 695; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_3 = __pyx_t_4;
    __pyx_t_4 = 0;
  }
  __pyx_t_4 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 695; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = __Pyx_PyBool_FromLong(__pyx_v_bIsLast); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 695; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_6 = PyTuple_New(4); if (unlikely(!__pyx_t_6)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 695; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_6);
  PyTuple_SET_ITEM(__pyx_t_6, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_6, 1, __pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_6, 2, __pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_6, 3, __pyx_t_5);
  __Pyx_GIVEREF(__pyx_t_5);
  __pyx_t_2 = 0;
  __pyx_t_3 = 0;
  __pyx_t_4 = 0;
  __pyx_t_5 = 0;
  __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_6, NULL); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 695; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRspQryContractBank", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRspQryParkedOrder(PyObject *__pyx_v_self, struct CThostFtdcParkedOrderField *__pyx_v_pParkedOrder, struct CThostFtdcRspInfoField *__pyx_v_pRspInfo, int __pyx_v_nRequestID, bool __pyx_v_bIsLast) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRspQryParkedOrder", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRspQryParkedOrder); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 699; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pParkedOrder == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pParkedOrder)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 699; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 699; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_ParkedOrder, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 699; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  if (((__pyx_v_pRspInfo == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_3 = Py_None;
  } else {
    __pyx_t_4 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspInfo)); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 699; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_5 = PyTuple_New(1); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 699; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_5);
    PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_4);
    __Pyx_GIVEREF(__pyx_t_4);
    __pyx_t_4 = 0;
    __pyx_t_4 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspInfo, __pyx_t_5, NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 699; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_3 = __pyx_t_4;
    __pyx_t_4 = 0;
  }
  __pyx_t_4 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 699; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = __Pyx_PyBool_FromLong(__pyx_v_bIsLast); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 699; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_6 = PyTuple_New(4); if (unlikely(!__pyx_t_6)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 699; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_6);
  PyTuple_SET_ITEM(__pyx_t_6, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_6, 1, __pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_6, 2, __pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_6, 3, __pyx_t_5);
  __Pyx_GIVEREF(__pyx_t_5);
  __pyx_t_2 = 0;
  __pyx_t_3 = 0;
  __pyx_t_4 = 0;
  __pyx_t_5 = 0;
  __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_6, NULL); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 699; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRspQryParkedOrder", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRspQryParkedOrderAction(PyObject *__pyx_v_self, struct CThostFtdcParkedOrderActionField *__pyx_v_pParkedOrderAction, struct CThostFtdcRspInfoField *__pyx_v_pRspInfo, int __pyx_v_nRequestID, bool __pyx_v_bIsLast) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRspQryParkedOrderAction", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRspQryParkedOrderAction); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 703; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pParkedOrderAction == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pParkedOrderAction)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 703; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 703; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_ParkedOrderAction, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 703; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  if (((__pyx_v_pRspInfo == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_3 = Py_None;
  } else {
    __pyx_t_4 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspInfo)); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 703; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_5 = PyTuple_New(1); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 703; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_5);
    PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_4);
    __Pyx_GIVEREF(__pyx_t_4);
    __pyx_t_4 = 0;
    __pyx_t_4 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspInfo, __pyx_t_5, NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 703; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_3 = __pyx_t_4;
    __pyx_t_4 = 0;
  }
  __pyx_t_4 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 703; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = __Pyx_PyBool_FromLong(__pyx_v_bIsLast); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 703; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_6 = PyTuple_New(4); if (unlikely(!__pyx_t_6)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 703; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_6);
  PyTuple_SET_ITEM(__pyx_t_6, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_6, 1, __pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_6, 2, __pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_6, 3, __pyx_t_5);
  __Pyx_GIVEREF(__pyx_t_5);
  __pyx_t_2 = 0;
  __pyx_t_3 = 0;
  __pyx_t_4 = 0;
  __pyx_t_5 = 0;
  __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_6, NULL); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 703; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRspQryParkedOrderAction", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRspQryTradingNotice(PyObject *__pyx_v_self, struct CThostFtdcTradingNoticeField *__pyx_v_pTradingNotice, struct CThostFtdcRspInfoField *__pyx_v_pRspInfo, int __pyx_v_nRequestID, bool __pyx_v_bIsLast) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRspQryTradingNotice", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRspQryTradingNotice); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 707; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pTradingNotice == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pTradingNotice)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 707; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 707; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_TradingNotice, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 707; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  if (((__pyx_v_pRspInfo == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_3 = Py_None;
  } else {
    __pyx_t_4 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspInfo)); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 707; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_5 = PyTuple_New(1); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 707; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_5);
    PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_4);
    __Pyx_GIVEREF(__pyx_t_4);
    __pyx_t_4 = 0;
    __pyx_t_4 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspInfo, __pyx_t_5, NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 707; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_3 = __pyx_t_4;
    __pyx_t_4 = 0;
  }
  __pyx_t_4 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 707; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = __Pyx_PyBool_FromLong(__pyx_v_bIsLast); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 707; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_6 = PyTuple_New(4); if (unlikely(!__pyx_t_6)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 707; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_6);
  PyTuple_SET_ITEM(__pyx_t_6, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_6, 1, __pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_6, 2, __pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_6, 3, __pyx_t_5);
  __Pyx_GIVEREF(__pyx_t_5);
  __pyx_t_2 = 0;
  __pyx_t_3 = 0;
  __pyx_t_4 = 0;
  __pyx_t_5 = 0;
  __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_6, NULL); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 707; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRspQryTradingNotice", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRspQryBrokerTradingParams(PyObject *__pyx_v_self, struct CThostFtdcBrokerTradingParamsField *__pyx_v_pBrokerTradingParams, struct CThostFtdcRspInfoField *__pyx_v_pRspInfo, int __pyx_v_nRequestID, bool __pyx_v_bIsLast) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRspQryBrokerTradingParams", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRspQryBrokerTradingParams); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 711; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pBrokerTradingParams == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pBrokerTradingParams)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 711; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 711; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_BrokerTradingParams, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 711; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  if (((__pyx_v_pRspInfo == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_3 = Py_None;
  } else {
    __pyx_t_4 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspInfo)); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 711; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_5 = PyTuple_New(1); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 711; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_5);
    PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_4);
    __Pyx_GIVEREF(__pyx_t_4);
    __pyx_t_4 = 0;
    __pyx_t_4 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspInfo, __pyx_t_5, NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 711; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_3 = __pyx_t_4;
    __pyx_t_4 = 0;
  }
  __pyx_t_4 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 711; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = __Pyx_PyBool_FromLong(__pyx_v_bIsLast); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 711; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_6 = PyTuple_New(4); if (unlikely(!__pyx_t_6)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 711; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_6);
  PyTuple_SET_ITEM(__pyx_t_6, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_6, 1, __pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_6, 2, __pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_6, 3, __pyx_t_5);
  __Pyx_GIVEREF(__pyx_t_5);
  __pyx_t_2 = 0;
  __pyx_t_3 = 0;
  __pyx_t_4 = 0;
  __pyx_t_5 = 0;
  __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_6, NULL); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 711; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRspQryBrokerTradingParams", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRspQryBrokerTradingAlgos(PyObject *__pyx_v_self, struct CThostFtdcBrokerTradingAlgosField *__pyx_v_pBrokerTradingAlgos, struct CThostFtdcRspInfoField *__pyx_v_pRspInfo, int __pyx_v_nRequestID, bool __pyx_v_bIsLast) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRspQryBrokerTradingAlgos", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRspQryBrokerTradingAlgos); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 715; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pBrokerTradingAlgos == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pBrokerTradingAlgos)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 715; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 715; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_BrokerTradingAlgos, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 715; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  if (((__pyx_v_pRspInfo == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_3 = Py_None;
  } else {
    __pyx_t_4 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspInfo)); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 715; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_5 = PyTuple_New(1); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 715; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_5);
    PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_4);
    __Pyx_GIVEREF(__pyx_t_4);
    __pyx_t_4 = 0;
    __pyx_t_4 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspInfo, __pyx_t_5, NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 715; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_3 = __pyx_t_4;
    __pyx_t_4 = 0;
  }
  __pyx_t_4 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 715; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = __Pyx_PyBool_FromLong(__pyx_v_bIsLast); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 715; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_6 = PyTuple_New(4); if (unlikely(!__pyx_t_6)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 715; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_6);
  PyTuple_SET_ITEM(__pyx_t_6, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_6, 1, __pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_6, 2, __pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_6, 3, __pyx_t_5);
  __Pyx_GIVEREF(__pyx_t_5);
  __pyx_t_2 = 0;
  __pyx_t_3 = 0;
  __pyx_t_4 = 0;
  __pyx_t_5 = 0;
  __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_6, NULL); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 715; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRspQryBrokerTradingAlgos", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRspQueryCFMMCTradingAccountToken(PyObject *__pyx_v_self, struct CThostFtdcQueryCFMMCTradingAccountTokenField *__pyx_v_pQueryCFMMCTradingAccountToken, struct CThostFtdcRspInfoField *__pyx_v_pRspInfo, int __pyx_v_nRequestID, bool __pyx_v_bIsLast) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRspQueryCFMMCTradingAccountToken", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRspQueryCFMMCTradingAccountTok); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 719; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pQueryCFMMCTradingAccountToken == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pQueryCFMMCTradingAccountToken)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 719; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 719; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_QueryCFMMCTradingAccountToken, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 719; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  if (((__pyx_v_pRspInfo == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_3 = Py_None;
  } else {
    __pyx_t_4 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspInfo)); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 719; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_5 = PyTuple_New(1); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 719; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_5);
    PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_4);
    __Pyx_GIVEREF(__pyx_t_4);
    __pyx_t_4 = 0;
    __pyx_t_4 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspInfo, __pyx_t_5, NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 719; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_3 = __pyx_t_4;
    __pyx_t_4 = 0;
  }
  __pyx_t_4 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 719; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = __Pyx_PyBool_FromLong(__pyx_v_bIsLast); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 719; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_6 = PyTuple_New(4); if (unlikely(!__pyx_t_6)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 719; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_6);
  PyTuple_SET_ITEM(__pyx_t_6, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_6, 1, __pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_6, 2, __pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_6, 3, __pyx_t_5);
  __Pyx_GIVEREF(__pyx_t_5);
  __pyx_t_2 = 0;
  __pyx_t_3 = 0;
  __pyx_t_4 = 0;
  __pyx_t_5 = 0;
  __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_6, NULL); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 719; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRspQueryCFMMCTradingAccountToken", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRtnFromBankToFutureByBank(PyObject *__pyx_v_self, struct CThostFtdcRspTransferField *__pyx_v_pRspTransfer) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRtnFromBankToFutureByBank", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRtnFromBankToFutureByBank); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 723; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pRspTransfer == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspTransfer)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 723; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 723; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspTransfer, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 723; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  __pyx_t_3 = PyTuple_New(1); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 723; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_3, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_3, NULL); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 723; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRtnFromBankToFutureByBank", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRtnFromFutureToBankByBank(PyObject *__pyx_v_self, struct CThostFtdcRspTransferField *__pyx_v_pRspTransfer) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRtnFromFutureToBankByBank", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRtnFromFutureToBankByBank); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 727; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pRspTransfer == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspTransfer)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 727; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 727; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspTransfer, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 727; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  __pyx_t_3 = PyTuple_New(1); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 727; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_3, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_3, NULL); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 727; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRtnFromFutureToBankByBank", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRtnRepealFromBankToFutureByBank(PyObject *__pyx_v_self, struct CThostFtdcRspRepealField *__pyx_v_pRspRepeal) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRtnRepealFromBankToFutureByBank", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRtnRepealFromBankToFutureByBan); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 731; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pRspRepeal == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspRepeal)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 731; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 731; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspRepeal, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 731; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  __pyx_t_3 = PyTuple_New(1); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 731; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_3, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_3, NULL); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 731; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRtnRepealFromBankToFutureByBank", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRtnRepealFromFutureToBankByBank(PyObject *__pyx_v_self, struct CThostFtdcRspRepealField *__pyx_v_pRspRepeal) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRtnRepealFromFutureToBankByBank", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRtnRepealFromFutureToBankByBan); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 735; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pRspRepeal == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspRepeal)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 735; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 735; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspRepeal, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 735; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  __pyx_t_3 = PyTuple_New(1); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 735; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_3, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_3, NULL); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 735; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRtnRepealFromFutureToBankByBank", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRtnFromBankToFutureByFuture(PyObject *__pyx_v_self, struct CThostFtdcRspTransferField *__pyx_v_pRspTransfer) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRtnFromBankToFutureByFuture", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRtnFromBankToFutureByFuture); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 739; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pRspTransfer == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspTransfer)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 739; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 739; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspTransfer, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 739; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  __pyx_t_3 = PyTuple_New(1); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 739; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_3, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_3, NULL); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 739; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRtnFromBankToFutureByFuture", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRtnFromFutureToBankByFuture(PyObject *__pyx_v_self, struct CThostFtdcRspTransferField *__pyx_v_pRspTransfer) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRtnFromFutureToBankByFuture", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRtnFromFutureToBankByFuture); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 743; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pRspTransfer == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspTransfer)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 743; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 743; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspTransfer, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 743; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  __pyx_t_3 = PyTuple_New(1); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 743; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_3, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_3, NULL); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 743; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRtnFromFutureToBankByFuture", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRtnRepealFromBankToFutureByFutureManual(PyObject *__pyx_v_self, struct CThostFtdcRspRepealField *__pyx_v_pRspRepeal) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRtnRepealFromBankToFutureByFutureManual", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRtnRepealFromBankToFutureByFut); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 747; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pRspRepeal == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspRepeal)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 747; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 747; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspRepeal, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 747; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  __pyx_t_3 = PyTuple_New(1); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 747; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_3, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_3, NULL); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 747; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRtnRepealFromBankToFutureByFutureManual", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRtnRepealFromFutureToBankByFutureManual(PyObject *__pyx_v_self, struct CThostFtdcRspRepealField *__pyx_v_pRspRepeal) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRtnRepealFromFutureToBankByFutureManual", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRtnRepealFromFutureToBankByFut); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 751; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pRspRepeal == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspRepeal)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 751; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 751; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspRepeal, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 751; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  __pyx_t_3 = PyTuple_New(1); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 751; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_3, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_3, NULL); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 751; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRtnRepealFromFutureToBankByFutureManual", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRtnQueryBankBalanceByFuture(PyObject *__pyx_v_self, struct CThostFtdcNotifyQueryAccountField *__pyx_v_pNotifyQueryAccount) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRtnQueryBankBalanceByFuture", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRtnQueryBankBalanceByFuture); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 755; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pNotifyQueryAccount == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pNotifyQueryAccount)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 755; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 755; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_NotifyQueryAccount, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 755; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  __pyx_t_3 = PyTuple_New(1); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 755; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_3, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_3, NULL); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 755; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRtnQueryBankBalanceByFuture", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnErrRtnBankToFutureByFuture(PyObject *__pyx_v_self, struct CThostFtdcReqTransferField *__pyx_v_pReqTransfer, struct CThostFtdcRspInfoField *__pyx_v_pRspInfo) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnErrRtnBankToFutureByFuture", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnErrRtnBankToFutureByFuture); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 759; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pReqTransfer == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pReqTransfer)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 759; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 759; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_ReqTransfer, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 759; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  if (((__pyx_v_pRspInfo == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_3 = Py_None;
  } else {
    __pyx_t_4 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspInfo)); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 759; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_5 = PyTuple_New(1); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 759; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_5);
    PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_4);
    __Pyx_GIVEREF(__pyx_t_4);
    __pyx_t_4 = 0;
    __pyx_t_4 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspInfo, __pyx_t_5, NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 759; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_3 = __pyx_t_4;
    __pyx_t_4 = 0;
  }
  __pyx_t_4 = PyTuple_New(2); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 759; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_4, 1, __pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  __pyx_t_2 = 0;
  __pyx_t_3 = 0;
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 759; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnErrRtnBankToFutureByFuture", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnErrRtnFutureToBankByFuture(PyObject *__pyx_v_self, struct CThostFtdcReqTransferField *__pyx_v_pReqTransfer, struct CThostFtdcRspInfoField *__pyx_v_pRspInfo) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnErrRtnFutureToBankByFuture", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnErrRtnFutureToBankByFuture); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 763; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pReqTransfer == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pReqTransfer)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 763; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 763; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_ReqTransfer, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 763; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  if (((__pyx_v_pRspInfo == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_3 = Py_None;
  } else {
    __pyx_t_4 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspInfo)); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 763; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_5 = PyTuple_New(1); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 763; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_5);
    PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_4);
    __Pyx_GIVEREF(__pyx_t_4);
    __pyx_t_4 = 0;
    __pyx_t_4 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspInfo, __pyx_t_5, NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 763; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_3 = __pyx_t_4;
    __pyx_t_4 = 0;
  }
  __pyx_t_4 = PyTuple_New(2); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 763; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_4, 1, __pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  __pyx_t_2 = 0;
  __pyx_t_3 = 0;
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 763; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnErrRtnFutureToBankByFuture", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnErrRtnRepealBankToFutureByFutureManual(PyObject *__pyx_v_self, struct CThostFtdcReqRepealField *__pyx_v_pReqRepeal, struct CThostFtdcRspInfoField *__pyx_v_pRspInfo) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnErrRtnRepealBankToFutureByFutureManual", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnErrRtnRepealBankToFutureByFutu); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 767; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pReqRepeal == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pReqRepeal)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 767; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 767; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_ReqRepeal, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 767; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  if (((__pyx_v_pRspInfo == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_3 = Py_None;
  } else {
    __pyx_t_4 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspInfo)); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 767; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_5 = PyTuple_New(1); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 767; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_5);
    PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_4);
    __Pyx_GIVEREF(__pyx_t_4);
    __pyx_t_4 = 0;
    __pyx_t_4 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspInfo, __pyx_t_5, NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 767; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_3 = __pyx_t_4;
    __pyx_t_4 = 0;
  }
  __pyx_t_4 = PyTuple_New(2); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 767; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_4, 1, __pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  __pyx_t_2 = 0;
  __pyx_t_3 = 0;
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 767; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnErrRtnRepealBankToFutureByFutureManual", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnErrRtnRepealFutureToBankByFutureManual(PyObject *__pyx_v_self, struct CThostFtdcReqRepealField *__pyx_v_pReqRepeal, struct CThostFtdcRspInfoField *__pyx_v_pRspInfo) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnErrRtnRepealFutureToBankByFutureManual", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnErrRtnRepealFutureToBankByFutu); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 771; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pReqRepeal == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pReqRepeal)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 771; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 771; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_ReqRepeal, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 771; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  if (((__pyx_v_pRspInfo == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_3 = Py_None;
  } else {
    __pyx_t_4 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspInfo)); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 771; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_5 = PyTuple_New(1); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 771; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_5);
    PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_4);
    __Pyx_GIVEREF(__pyx_t_4);
    __pyx_t_4 = 0;
    __pyx_t_4 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspInfo, __pyx_t_5, NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 771; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_3 = __pyx_t_4;
    __pyx_t_4 = 0;
  }
  __pyx_t_4 = PyTuple_New(2); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 771; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_4, 1, __pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  __pyx_t_2 = 0;
  __pyx_t_3 = 0;
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 771; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnErrRtnRepealFutureToBankByFutureManual", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnErrRtnQueryBankBalanceByFuture(PyObject *__pyx_v_self, struct CThostFtdcReqQueryAccountField *__pyx_v_pReqQueryAccount, struct CThostFtdcRspInfoField *__pyx_v_pRspInfo) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnErrRtnQueryBankBalanceByFuture", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnErrRtnQueryBankBalanceByFuture); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 775; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pReqQueryAccount == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pReqQueryAccount)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 775; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 775; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_ReqQueryAccount, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 775; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  if (((__pyx_v_pRspInfo == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_3 = Py_None;
  } else {
    __pyx_t_4 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspInfo)); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 775; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_5 = PyTuple_New(1); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 775; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_5);
    PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_4);
    __Pyx_GIVEREF(__pyx_t_4);
    __pyx_t_4 = 0;
    __pyx_t_4 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspInfo, __pyx_t_5, NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 775; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_3 = __pyx_t_4;
    __pyx_t_4 = 0;
  }
  __pyx_t_4 = PyTuple_New(2); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 775; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_4, 1, __pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  __pyx_t_2 = 0;
  __pyx_t_3 = 0;
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 775; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnErrRtnQueryBankBalanceByFuture", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRtnRepealFromBankToFutureByFuture(PyObject *__pyx_v_self, struct CThostFtdcRspRepealField *__pyx_v_pRspRepeal) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRtnRepealFromBankToFutureByFuture", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRtnRepealFromBankToFutureByFut_2); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 779; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pRspRepeal == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspRepeal)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 779; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 779; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspRepeal, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 779; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  __pyx_t_3 = PyTuple_New(1); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 779; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_3, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_3, NULL); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 779; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRtnRepealFromBankToFutureByFuture", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRtnRepealFromFutureToBankByFuture(PyObject *__pyx_v_self, struct CThostFtdcRspRepealField *__pyx_v_pRspRepeal) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRtnRepealFromFutureToBankByFuture", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRtnRepealFromFutureToBankByFut_2); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 783; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pRspRepeal == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspRepeal)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 783; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 783; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspRepeal, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 783; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  __pyx_t_3 = PyTuple_New(1); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 783; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_3, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_3, NULL); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 783; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRtnRepealFromFutureToBankByFuture", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRspFromBankToFutureByFuture(PyObject *__pyx_v_self, struct CThostFtdcReqTransferField *__pyx_v_pReqTransfer, struct CThostFtdcRspInfoField *__pyx_v_pRspInfo, int __pyx_v_nRequestID, bool __pyx_v_bIsLast) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRspFromBankToFutureByFuture", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRspFromBankToFutureByFuture); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 787; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pReqTransfer == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pReqTransfer)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 787; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 787; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_ReqTransfer, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 787; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  if (((__pyx_v_pRspInfo == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_3 = Py_None;
  } else {
    __pyx_t_4 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspInfo)); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 787; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_5 = PyTuple_New(1); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 787; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_5);
    PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_4);
    __Pyx_GIVEREF(__pyx_t_4);
    __pyx_t_4 = 0;
    __pyx_t_4 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspInfo, __pyx_t_5, NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 787; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_3 = __pyx_t_4;
    __pyx_t_4 = 0;
  }
  __pyx_t_4 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 787; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = __Pyx_PyBool_FromLong(__pyx_v_bIsLast); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 787; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_6 = PyTuple_New(4); if (unlikely(!__pyx_t_6)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 787; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_6);
  PyTuple_SET_ITEM(__pyx_t_6, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_6, 1, __pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_6, 2, __pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_6, 3, __pyx_t_5);
  __Pyx_GIVEREF(__pyx_t_5);
  __pyx_t_2 = 0;
  __pyx_t_3 = 0;
  __pyx_t_4 = 0;
  __pyx_t_5 = 0;
  __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_6, NULL); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 787; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRspFromBankToFutureByFuture", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRspFromFutureToBankByFuture(PyObject *__pyx_v_self, struct CThostFtdcReqTransferField *__pyx_v_pReqTransfer, struct CThostFtdcRspInfoField *__pyx_v_pRspInfo, int __pyx_v_nRequestID, bool __pyx_v_bIsLast) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRspFromFutureToBankByFuture", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRspFromFutureToBankByFuture); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 791; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pReqTransfer == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pReqTransfer)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 791; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 791; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_ReqTransfer, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 791; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  if (((__pyx_v_pRspInfo == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_3 = Py_None;
  } else {
    __pyx_t_4 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspInfo)); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 791; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_5 = PyTuple_New(1); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 791; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_5);
    PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_4);
    __Pyx_GIVEREF(__pyx_t_4);
    __pyx_t_4 = 0;
    __pyx_t_4 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspInfo, __pyx_t_5, NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 791; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_3 = __pyx_t_4;
    __pyx_t_4 = 0;
  }
  __pyx_t_4 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 791; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = __Pyx_PyBool_FromLong(__pyx_v_bIsLast); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 791; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_6 = PyTuple_New(4); if (unlikely(!__pyx_t_6)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 791; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_6);
  PyTuple_SET_ITEM(__pyx_t_6, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_6, 1, __pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_6, 2, __pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_6, 3, __pyx_t_5);
  __Pyx_GIVEREF(__pyx_t_5);
  __pyx_t_2 = 0;
  __pyx_t_3 = 0;
  __pyx_t_4 = 0;
  __pyx_t_5 = 0;
  __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_6, NULL); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 791; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRspFromFutureToBankByFuture", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRspQueryBankAccountMoneyByFuture(PyObject *__pyx_v_self, struct CThostFtdcReqQueryAccountField *__pyx_v_pReqQueryAccount, struct CThostFtdcRspInfoField *__pyx_v_pRspInfo, int __pyx_v_nRequestID, bool __pyx_v_bIsLast) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRspQueryBankAccountMoneyByFuture", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRspQueryBankAccountMoneyByFutu); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 795; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pReqQueryAccount == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pReqQueryAccount)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 795; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 795; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_ReqQueryAccount, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 795; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  if (((__pyx_v_pRspInfo == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_3 = Py_None;
  } else {
    __pyx_t_4 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pRspInfo)); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 795; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_5 = PyTuple_New(1); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 795; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_5);
    PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_4);
    __Pyx_GIVEREF(__pyx_t_4);
    __pyx_t_4 = 0;
    __pyx_t_4 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_RspInfo, __pyx_t_5, NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 795; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_3 = __pyx_t_4;
    __pyx_t_4 = 0;
  }
  __pyx_t_4 = __Pyx_PyInt_From_int(__pyx_v_nRequestID); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 795; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = __Pyx_PyBool_FromLong(__pyx_v_bIsLast); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 795; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_6 = PyTuple_New(4); if (unlikely(!__pyx_t_6)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 795; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_6);
  PyTuple_SET_ITEM(__pyx_t_6, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_6, 1, __pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_6, 2, __pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_6, 3, __pyx_t_5);
  __Pyx_GIVEREF(__pyx_t_5);
  __pyx_t_2 = 0;
  __pyx_t_3 = 0;
  __pyx_t_4 = 0;
  __pyx_t_5 = 0;
  __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_6, NULL); if (unlikely(!__pyx_t_5)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 795; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRspQueryBankAccountMoneyByFuture", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRtnOpenAccountByBank(PyObject *__pyx_v_self, struct CThostFtdcOpenAccountField *__pyx_v_pOpenAccount) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRtnOpenAccountByBank", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRtnOpenAccountByBank); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 799; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pOpenAccount == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pOpenAccount)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 799; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 799; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_OpenAccount, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 799; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  __pyx_t_3 = PyTuple_New(1); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 799; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_3, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_3, NULL); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 799; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRtnOpenAccountByBank", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRtnCancelAccountByBank(PyObject *__pyx_v_self, struct CThostFtdcCancelAccountField *__pyx_v_pCancelAccount) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRtnCancelAccountByBank", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRtnCancelAccountByBank); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 803; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pCancelAccount == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pCancelAccount)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 803; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 803; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_CancelAccount, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 803; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  __pyx_t_3 = PyTuple_New(1); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 803; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_3, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_3, NULL); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 803; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRtnCancelAccountByBank", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
int TraderSpi_OnRtnChangeAccountByBank(PyObject *__pyx_v_self, struct CThostFtdcChangeAccountField *__pyx_v_pChangeAccount) {
  int __pyx_r;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("TraderSpi_OnRtnChangeAccountByBank", 0);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_OnRtnChangeAccountByBank); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 807; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  if (((__pyx_v_pChangeAccount == NULL) != 0)) {
    __Pyx_INCREF(Py_None);
    __pyx_t_2 = Py_None;
  } else {
    __pyx_t_3 = __Pyx_PyInt_FromSize_t(((size_t)__pyx_v_pChangeAccount)); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 807; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 807; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_v_3ctp_10_TraderApi_ApiStruct_ChangeAccount, __pyx_t_4, NULL); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 807; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
  }
  __pyx_t_3 = PyTuple_New(1); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 807; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_3, 0, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_3, NULL); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 807; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_r = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_AddTraceback("ctp._TraderApi.TraderSpi_OnRtnChangeAccountByBank", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = -1;
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_tp_new_3ctp_10_TraderApi_TraderApi(PyTypeObject *t, CYTHON_UNUSED PyObject *a, CYTHON_UNUSED PyObject *k) {
  PyObject *o;
  if (likely((t->tp_flags & Py_TPFLAGS_IS_ABSTRACT) == 0)) {
    o = (*t->tp_alloc)(t, 0);
  } else {
    o = (PyObject *) PyBaseObject_Type.tp_new(t, __pyx_empty_tuple, 0);
  }
  if (unlikely(!o)) return 0;
  return o;
}
static void __pyx_tp_dealloc_3ctp_10_TraderApi_TraderApi(PyObject *o) {
  #if PY_VERSION_HEX >= 0x030400a1
  if (unlikely(Py_TYPE(o)->tp_finalize) && (!PyType_IS_GC(Py_TYPE(o)) || !_PyGC_FINALIZED(o))) {
    if (PyObject_CallFinalizerFromDealloc(o)) return;
  }
  #endif
  {
    PyObject *etype, *eval, *etb;
    PyErr_Fetch(&etype, &eval, &etb);
    ++Py_REFCNT(o);
    __pyx_pw_3ctp_10_TraderApi_9TraderApi_1__dealloc__(o);
    --Py_REFCNT(o);
    PyErr_Restore(etype, eval, etb);
  }
  (*Py_TYPE(o)->tp_free)(o);
}
static PyMethodDef __pyx_methods_3ctp_10_TraderApi_TraderApi[] = {
  {__Pyx_NAMESTR("Alive"), (PyCFunction)__pyx_pw_3ctp_10_TraderApi_9TraderApi_3Alive, METH_NOARGS, __Pyx_DOCSTR(0)},
  {__Pyx_NAMESTR("Create"), (PyCFunction)__pyx_pw_3ctp_10_TraderApi_9TraderApi_5Create, METH_VARARGS|METH_KEYWORDS, __Pyx_DOCSTR(0)},
  {__Pyx_NAMESTR("Release"), (PyCFunction)__pyx_pw_3ctp_10_TraderApi_9TraderApi_7Release, METH_NOARGS, __Pyx_DOCSTR(0)},
  {__Pyx_NAMESTR("Init"), (PyCFunction)__pyx_pw_3ctp_10_TraderApi_9TraderApi_9Init, METH_NOARGS, __Pyx_DOCSTR(0)},
  {__Pyx_NAMESTR("Join"), (PyCFunction)__pyx_pw_3ctp_10_TraderApi_9TraderApi_11Join, METH_NOARGS, __Pyx_DOCSTR(0)},
  {__Pyx_NAMESTR("GetTradingDay"), (PyCFunction)__pyx_pw_3ctp_10_TraderApi_9TraderApi_13GetTradingDay, METH_NOARGS, __Pyx_DOCSTR(0)},
  {__Pyx_NAMESTR("RegisterFront"), (PyCFunction)__pyx_pw_3ctp_10_TraderApi_9TraderApi_15RegisterFront, METH_O, __Pyx_DOCSTR(0)},
  {__Pyx_NAMESTR("RegisterNameServer"), (PyCFunction)__pyx_pw_3ctp_10_TraderApi_9TraderApi_17RegisterNameServer, METH_O, __Pyx_DOCSTR(0)},
  {__Pyx_NAMESTR("RegisterFensUserInfo"), (PyCFunction)__pyx_pw_3ctp_10_TraderApi_9TraderApi_19RegisterFensUserInfo, METH_O, __Pyx_DOCSTR(0)},
  {__Pyx_NAMESTR("SubscribePrivateTopic"), (PyCFunction)__pyx_pw_3ctp_10_TraderApi_9TraderApi_21SubscribePrivateTopic, METH_O, __Pyx_DOCSTR(0)},
  {__Pyx_NAMESTR("SubscribePublicTopic"), (PyCFunction)__pyx_pw_3ctp_10_TraderApi_9TraderApi_23SubscribePublicTopic, METH_O, __Pyx_DOCSTR(0)},
  {__Pyx_NAMESTR("ReqAuthenticate"), (PyCFunction)__pyx_pw_3ctp_10_TraderApi_9TraderApi_25ReqAuthenticate, METH_VARARGS|METH_KEYWORDS, __Pyx_DOCSTR(0)},
  {__Pyx_NAMESTR("ReqUserLogin"), (PyCFunction)__pyx_pw_3ctp_10_TraderApi_9TraderApi_27ReqUserLogin, METH_VARARGS|METH_KEYWORDS, __Pyx_DOCSTR(0)},
  {__Pyx_NAMESTR("ReqUserLogout"), (PyCFunction)__pyx_pw_3ctp_10_TraderApi_9TraderApi_29ReqUserLogout, METH_VARARGS|METH_KEYWORDS, __Pyx_DOCSTR(0)},
  {__Pyx_NAMESTR("ReqUserPasswordUpdate"), (PyCFunction)__pyx_pw_3ctp_10_TraderApi_9TraderApi_31ReqUserPasswordUpdate, METH_VARARGS|METH_KEYWORDS, __Pyx_DOCSTR(0)},
  {__Pyx_NAMESTR("ReqTradingAccountPasswordUpdate"), (PyCFunction)__pyx_pw_3ctp_10_TraderApi_9TraderApi_33ReqTradingAccountPasswordUpdate, METH_VARARGS|METH_KEYWORDS, __Pyx_DOCSTR(0)},
  {__Pyx_NAMESTR("ReqOrderInsert"), (PyCFunction)__pyx_pw_3ctp_10_TraderApi_9TraderApi_35ReqOrderInsert, METH_VARARGS|METH_KEYWORDS, __Pyx_DOCSTR(0)},
  {__Pyx_NAMESTR("ReqParkedOrderInsert"), (PyCFunction)__pyx_pw_3ctp_10_TraderApi_9TraderApi_37ReqParkedOrderInsert, METH_VARARGS|METH_KEYWORDS, __Pyx_DOCSTR(0)},
  {__Pyx_NAMESTR("ReqParkedOrderAction"), (PyCFunction)__pyx_pw_3ctp_10_TraderApi_9TraderApi_39ReqParkedOrderAction, METH_VARARGS|METH_KEYWORDS, __Pyx_DOCSTR(0)},
  {__Pyx_NAMESTR("ReqOrderAction"), (PyCFunction)__pyx_pw_3ctp_10_TraderApi_9TraderApi_41ReqOrderAction, METH_VARARGS|METH_KEYWORDS, __Pyx_DOCSTR(0)},
  {__Pyx_NAMESTR("ReqQueryMaxOrderVolume"), (PyCFunction)__pyx_pw_3ctp_10_TraderApi_9TraderApi_43ReqQueryMaxOrderVolume, METH_VARARGS|METH_KEYWORDS, __Pyx_DOCSTR(0)},
  {__Pyx_NAMESTR("ReqSettlementInfoConfirm"), (PyCFunction)__pyx_pw_3ctp_10_TraderApi_9TraderApi_45ReqSettlementInfoConfirm, METH_VARARGS|METH_KEYWORDS, __Pyx_DOCSTR(0)},
  {__Pyx_NAMESTR("ReqRemoveParkedOrder"), (PyCFunction)__pyx_pw_3ctp_10_TraderApi_9TraderApi_47ReqRemoveParkedOrder, METH_VARARGS|METH_KEYWORDS, __Pyx_DOCSTR(0)},
  {__Pyx_NAMESTR("ReqRemoveParkedOrderAction"), (PyCFunction)__pyx_pw_3ctp_10_TraderApi_9TraderApi_49ReqRemoveParkedOrderAction, METH_VARARGS|METH_KEYWORDS, __Pyx_DOCSTR(0)},
  {__Pyx_NAMESTR("ReqQryOrder"), (PyCFunction)__pyx_pw_3ctp_10_TraderApi_9TraderApi_51ReqQryOrder, METH_VARARGS|METH_KEYWORDS, __Pyx_DOCSTR(0)},
  {__Pyx_NAMESTR("ReqQryTrade"), (PyCFunction)__pyx_pw_3ctp_10_TraderApi_9TraderApi_53ReqQryTrade, METH_VARARGS|METH_KEYWORDS, __Pyx_DOCSTR(0)},
  {__Pyx_NAMESTR("ReqQryInvestorPosition"), (PyCFunction)__pyx_pw_3ctp_10_TraderApi_9TraderApi_55ReqQryInvestorPosition, METH_VARARGS|METH_KEYWORDS, __Pyx_DOCSTR(0)},
  {__Pyx_NAMESTR("ReqQryTradingAccount"), (PyCFunction)__pyx_pw_3ctp_10_TraderApi_9TraderApi_57ReqQryTradingAccount, METH_VARARGS|METH_KEYWORDS, __Pyx_DOCSTR(0)},
  {__Pyx_NAMESTR("ReqQryInvestor"), (PyCFunction)__pyx_pw_3ctp_10_TraderApi_9TraderApi_59ReqQryInvestor, METH_VARARGS|METH_KEYWORDS, __Pyx_DOCSTR(0)},
  {__Pyx_NAMESTR("ReqQryTradingCode"), (PyCFunction)__pyx_pw_3ctp_10_TraderApi_9TraderApi_61ReqQryTradingCode, METH_VARARGS|METH_KEYWORDS, __Pyx_DOCSTR(0)},
  {__Pyx_NAMESTR("ReqQryInstrumentMarginRate"), (PyCFunction)__pyx_pw_3ctp_10_TraderApi_9TraderApi_63ReqQryInstrumentMarginRate, METH_VARARGS|METH_KEYWORDS, __Pyx_DOCSTR(0)},
  {__Pyx_NAMESTR("ReqQryInstrumentCommissionRate"), (PyCFunction)__pyx_pw_3ctp_10_TraderApi_9TraderApi_65ReqQryInstrumentCommissionRate, METH_VARARGS|METH_KEYWORDS, __Pyx_DOCSTR(0)},
  {__Pyx_NAMESTR("ReqQryExchange"), (PyCFunction)__pyx_pw_3ctp_10_TraderApi_9TraderApi_67ReqQryExchange, METH_VARARGS|METH_KEYWORDS, __Pyx_DOCSTR(0)},
  {__Pyx_NAMESTR("ReqQryProduct"), (PyCFunction)__pyx_pw_3ctp_10_TraderApi_9TraderApi_69ReqQryProduct, METH_VARARGS|METH_KEYWORDS, __Pyx_DOCSTR(0)},
  {__Pyx_NAMESTR("ReqQryInstrument"), (PyCFunction)__pyx_pw_3ctp_10_TraderApi_9TraderApi_71ReqQryInstrument, METH_VARARGS|METH_KEYWORDS, __Pyx_DOCSTR(0)},
  {__Pyx_NAMESTR("ReqQryDepthMarketData"), (PyCFunction)__pyx_pw_3ctp_10_TraderApi_9TraderApi_73ReqQryDepthMarketData, METH_VARARGS|METH_KEYWORDS, __Pyx_DOCSTR(0)},
  {__Pyx_NAMESTR("ReqQrySettlementInfo"), (PyCFunction)__pyx_pw_3ctp_10_TraderApi_9TraderApi_75ReqQrySettlementInfo, METH_VARARGS|METH_KEYWORDS, __Pyx_DOCSTR(0)},
  {__Pyx_NAMESTR("ReqQryTransferBank"), (PyCFunction)__pyx_pw_3ctp_10_TraderApi_9TraderApi_77ReqQryTransferBank, METH_VARARGS|METH_KEYWORDS, __Pyx_DOCSTR(0)},
  {__Pyx_NAMESTR("ReqQryInvestorPositionDetail"), (PyCFunction)__pyx_pw_3ctp_10_TraderApi_9TraderApi_79ReqQryInvestorPositionDetail, METH_VARARGS|METH_KEYWORDS, __Pyx_DOCSTR(0)},
  {__Pyx_NAMESTR("ReqQryNotice"), (PyCFunction)__pyx_pw_3ctp_10_TraderApi_9TraderApi_81ReqQryNotice, METH_VARARGS|METH_KEYWORDS, __Pyx_DOCSTR(0)},
  {__Pyx_NAMESTR("ReqQrySettlementInfoConfirm"), (PyCFunction)__pyx_pw_3ctp_10_TraderApi_9TraderApi_83ReqQrySettlementInfoConfirm, METH_VARARGS|METH_KEYWORDS, __Pyx_DOCSTR(0)},
  {__Pyx_NAMESTR("ReqQryInvestorPositionCombineDetail"), (PyCFunction)__pyx_pw_3ctp_10_TraderApi_9TraderApi_85ReqQryInvestorPositionCombineDetail, METH_VARARGS|METH_KEYWORDS, __Pyx_DOCSTR(0)},
  {__Pyx_NAMESTR("ReqQryCFMMCTradingAccountKey"), (PyCFunction)__pyx_pw_3ctp_10_TraderApi_9TraderApi_87ReqQryCFMMCTradingAccountKey, METH_VARARGS|METH_KEYWORDS, __Pyx_DOCSTR(0)},
  {__Pyx_NAMESTR("ReqQryEWarrantOffset"), (PyCFunction)__pyx_pw_3ctp_10_TraderApi_9TraderApi_89ReqQryEWarrantOffset, METH_VARARGS|METH_KEYWORDS, __Pyx_DOCSTR(0)},
  {__Pyx_NAMESTR("ReqQryInvestorProductGroupMargin"), (PyCFunction)__pyx_pw_3ctp_10_TraderApi_9TraderApi_91ReqQryInvestorProductGroupMargin, METH_VARARGS|METH_KEYWORDS, __Pyx_DOCSTR(0)},
  {__Pyx_NAMESTR("ReqQryExchangeMarginRate"), (PyCFunction)__pyx_pw_3ctp_10_TraderApi_9TraderApi_93ReqQryExchangeMarginRate, METH_VARARGS|METH_KEYWORDS, __Pyx_DOCSTR(0)},
  {__Pyx_NAMESTR("ReqQryExchangeMarginRateAdjust"), (PyCFunction)__pyx_pw_3ctp_10_TraderApi_9TraderApi_95ReqQryExchangeMarginRateAdjust, METH_VARARGS|METH_KEYWORDS, __Pyx_DOCSTR(0)},
  {__Pyx_NAMESTR("ReqQryExchangeRate"), (PyCFunction)__pyx_pw_3ctp_10_TraderApi_9TraderApi_97ReqQryExchangeRate, METH_VARARGS|METH_KEYWORDS, __Pyx_DOCSTR(0)},
  {__Pyx_NAMESTR("ReqQrySecAgentACIDMap"), (PyCFunction)__pyx_pw_3ctp_10_TraderApi_9TraderApi_99ReqQrySecAgentACIDMap, METH_VARARGS|METH_KEYWORDS, __Pyx_DOCSTR(0)},
  {__Pyx_NAMESTR("ReqQryTransferSerial"), (PyCFunction)__pyx_pw_3ctp_10_TraderApi_9TraderApi_101ReqQryTransferSerial, METH_VARARGS|METH_KEYWORDS, __Pyx_DOCSTR(0)},
  {__Pyx_NAMESTR("ReqQryAccountregister"), (PyCFunction)__pyx_pw_3ctp_10_TraderApi_9TraderApi_103ReqQryAccountregister, METH_VARARGS|METH_KEYWORDS, __Pyx_DOCSTR(0)},
  {__Pyx_NAMESTR("ReqQryContractBank"), (PyCFunction)__pyx_pw_3ctp_10_TraderApi_9TraderApi_105ReqQryContractBank, METH_VARARGS|METH_KEYWORDS, __Pyx_DOCSTR(0)},
  {__Pyx_NAMESTR("ReqQryParkedOrder"), (PyCFunction)__pyx_pw_3ctp_10_TraderApi_9TraderApi_107ReqQryParkedOrder, METH_VARARGS|METH_KEYWORDS, __Pyx_DOCSTR(0)},
  {__Pyx_NAMESTR("ReqQryParkedOrderAction"), (PyCFunction)__pyx_pw_3ctp_10_TraderApi_9TraderApi_109ReqQryParkedOrderAction, METH_VARARGS|METH_KEYWORDS, __Pyx_DOCSTR(0)},
  {__Pyx_NAMESTR("ReqQryTradingNotice"), (PyCFunction)__pyx_pw_3ctp_10_TraderApi_9TraderApi_111ReqQryTradingNotice, METH_VARARGS|METH_KEYWORDS, __Pyx_DOCSTR(0)},
  {__Pyx_NAMESTR("ReqQryBrokerTradingParams"), (PyCFunction)__pyx_pw_3ctp_10_TraderApi_9TraderApi_113ReqQryBrokerTradingParams, METH_VARARGS|METH_KEYWORDS, __Pyx_DOCSTR(0)},
  {__Pyx_NAMESTR("ReqQryBrokerTradingAlgos"), (PyCFunction)__pyx_pw_3ctp_10_TraderApi_9TraderApi_115ReqQryBrokerTradingAlgos, METH_VARARGS|METH_KEYWORDS, __Pyx_DOCSTR(0)},
  {__Pyx_NAMESTR("ReqQueryCFMMCTradingAccountToken"), (PyCFunction)__pyx_pw_3ctp_10_TraderApi_9TraderApi_117ReqQueryCFMMCTradingAccountToken, METH_VARARGS|METH_KEYWORDS, __Pyx_DOCSTR(0)},
  {__Pyx_NAMESTR("ReqFromBankToFutureByFuture"), (PyCFunction)__pyx_pw_3ctp_10_TraderApi_9TraderApi_119ReqFromBankToFutureByFuture, METH_VARARGS|METH_KEYWORDS, __Pyx_DOCSTR(0)},
  {__Pyx_NAMESTR("ReqFromFutureToBankByFuture"), (PyCFunction)__pyx_pw_3ctp_10_TraderApi_9TraderApi_121ReqFromFutureToBankByFuture, METH_VARARGS|METH_KEYWORDS, __Pyx_DOCSTR(0)},
  {__Pyx_NAMESTR("ReqQueryBankAccountMoneyByFuture"), (PyCFunction)__pyx_pw_3ctp_10_TraderApi_9TraderApi_123ReqQueryBankAccountMoneyByFuture, METH_VARARGS|METH_KEYWORDS, __Pyx_DOCSTR(0)},
  {0, 0, 0, 0}
};
static PyTypeObject __pyx_type_3ctp_10_TraderApi_TraderApi = {
  PyVarObject_HEAD_INIT(0, 0)
  __Pyx_NAMESTR("ctp._TraderApi.TraderApi"), 
  sizeof(struct __pyx_obj_3ctp_10_TraderApi_TraderApi), 
  0, 
  __pyx_tp_dealloc_3ctp_10_TraderApi_TraderApi, 
  0, 
  0, 
  0, 
  #if PY_MAJOR_VERSION < 3
  0, 
  #else
  0, 
  #endif
  0, 
  0, 
  0, 
  0, 
  0, 
  0, 
  0, 
  0, 
  0, 
  0, 
  Py_TPFLAGS_DEFAULT|Py_TPFLAGS_HAVE_VERSION_TAG|Py_TPFLAGS_CHECKTYPES|Py_TPFLAGS_HAVE_NEWBUFFER|Py_TPFLAGS_BASETYPE, 
  0, 
  0, 
  0, 
  0, 
  0, 
  0, 
  0, 
  __pyx_methods_3ctp_10_TraderApi_TraderApi, 
  0, 
  0, 
  0, 
  0, 
  0, 
  0, 
  0, 
  0, 
  0, 
  __pyx_tp_new_3ctp_10_TraderApi_TraderApi, 
  0, 
  0, 
  0, 
  0, 
  0, 
  0, 
  0, 
  0, 
  #if PY_VERSION_HEX >= 0x02060000
  0, 
  #endif
  #if PY_VERSION_HEX >= 0x030400a1
  0, 
  #endif
};
static PyMethodDef __pyx_methods[] = {
  {0, 0, 0, 0}
};
#if PY_MAJOR_VERSION >= 3
static struct PyModuleDef __pyx_moduledef = {
  #if PY_VERSION_HEX < 0x03020000
    { PyObject_HEAD_INIT(NULL) NULL, 0, NULL },
  #else
    PyModuleDef_HEAD_INIT,
  #endif
    __Pyx_NAMESTR("_TraderApi"),
    0, 
    -1, 
    __pyx_methods ,
    NULL, 
    NULL, 
    NULL, 
    NULL 
};
#endif
static __Pyx_StringTabEntry __pyx_string_tab[] = {
  {&__pyx_n_s_OnErrRtnBankToFutureByFuture, __pyx_k_OnErrRtnBankToFutureByFuture, sizeof(__pyx_k_OnErrRtnBankToFutureByFuture), 0, 0, 1, 1},
  {&__pyx_n_s_OnErrRtnFutureToBankByFuture, __pyx_k_OnErrRtnFutureToBankByFuture, sizeof(__pyx_k_OnErrRtnFutureToBankByFuture), 0, 0, 1, 1},
  {&__pyx_n_s_OnErrRtnOrderAction, __pyx_k_OnErrRtnOrderAction, sizeof(__pyx_k_OnErrRtnOrderAction), 0, 0, 1, 1},
  {&__pyx_n_s_OnErrRtnOrderInsert, __pyx_k_OnErrRtnOrderInsert, sizeof(__pyx_k_OnErrRtnOrderInsert), 0, 0, 1, 1},
  {&__pyx_n_s_OnErrRtnQueryBankBalanceByFuture, __pyx_k_OnErrRtnQueryBankBalanceByFuture, sizeof(__pyx_k_OnErrRtnQueryBankBalanceByFuture), 0, 0, 1, 1},
  {&__pyx_n_s_OnErrRtnRepealBankToFutureByFutu, __pyx_k_OnErrRtnRepealBankToFutureByFutu, sizeof(__pyx_k_OnErrRtnRepealBankToFutureByFutu), 0, 0, 1, 1},
  {&__pyx_n_s_OnErrRtnRepealFutureToBankByFutu, __pyx_k_OnErrRtnRepealFutureToBankByFutu, sizeof(__pyx_k_OnErrRtnRepealFutureToBankByFutu), 0, 0, 1, 1},
  {&__pyx_n_s_OnFrontConnected, __pyx_k_OnFrontConnected, sizeof(__pyx_k_OnFrontConnected), 0, 0, 1, 1},
  {&__pyx_n_s_OnFrontDisconnected, __pyx_k_OnFrontDisconnected, sizeof(__pyx_k_OnFrontDisconnected), 0, 0, 1, 1},
  {&__pyx_n_s_OnHeartBeatWarning, __pyx_k_OnHeartBeatWarning, sizeof(__pyx_k_OnHeartBeatWarning), 0, 0, 1, 1},
  {&__pyx_n_s_OnRspAuthenticate, __pyx_k_OnRspAuthenticate, sizeof(__pyx_k_OnRspAuthenticate), 0, 0, 1, 1},
  {&__pyx_n_s_OnRspError, __pyx_k_OnRspError, sizeof(__pyx_k_OnRspError), 0, 0, 1, 1},
  {&__pyx_n_s_OnRspFromBankToFutureByFuture, __pyx_k_OnRspFromBankToFutureByFuture, sizeof(__pyx_k_OnRspFromBankToFutureByFuture), 0, 0, 1, 1},
  {&__pyx_n_s_OnRspFromFutureToBankByFuture, __pyx_k_OnRspFromFutureToBankByFuture, sizeof(__pyx_k_OnRspFromFutureToBankByFuture), 0, 0, 1, 1},
  {&__pyx_n_s_OnRspOrderAction, __pyx_k_OnRspOrderAction, sizeof(__pyx_k_OnRspOrderAction), 0, 0, 1, 1},
  {&__pyx_n_s_OnRspOrderInsert, __pyx_k_OnRspOrderInsert, sizeof(__pyx_k_OnRspOrderInsert), 0, 0, 1, 1},
  {&__pyx_n_s_OnRspParkedOrderAction, __pyx_k_OnRspParkedOrderAction, sizeof(__pyx_k_OnRspParkedOrderAction), 0, 0, 1, 1},
  {&__pyx_n_s_OnRspParkedOrderInsert, __pyx_k_OnRspParkedOrderInsert, sizeof(__pyx_k_OnRspParkedOrderInsert), 0, 0, 1, 1},
  {&__pyx_n_s_OnRspQryAccountregister, __pyx_k_OnRspQryAccountregister, sizeof(__pyx_k_OnRspQryAccountregister), 0, 0, 1, 1},
  {&__pyx_n_s_OnRspQryBrokerTradingAlgos, __pyx_k_OnRspQryBrokerTradingAlgos, sizeof(__pyx_k_OnRspQryBrokerTradingAlgos), 0, 0, 1, 1},
  {&__pyx_n_s_OnRspQryBrokerTradingParams, __pyx_k_OnRspQryBrokerTradingParams, sizeof(__pyx_k_OnRspQryBrokerTradingParams), 0, 0, 1, 1},
  {&__pyx_n_s_OnRspQryCFMMCTradingAccountKey, __pyx_k_OnRspQryCFMMCTradingAccountKey, sizeof(__pyx_k_OnRspQryCFMMCTradingAccountKey), 0, 0, 1, 1},
  {&__pyx_n_s_OnRspQryContractBank, __pyx_k_OnRspQryContractBank, sizeof(__pyx_k_OnRspQryContractBank), 0, 0, 1, 1},
  {&__pyx_n_s_OnRspQryDepthMarketData, __pyx_k_OnRspQryDepthMarketData, sizeof(__pyx_k_OnRspQryDepthMarketData), 0, 0, 1, 1},
  {&__pyx_n_s_OnRspQryEWarrantOffset, __pyx_k_OnRspQryEWarrantOffset, sizeof(__pyx_k_OnRspQryEWarrantOffset), 0, 0, 1, 1},
  {&__pyx_n_s_OnRspQryExchange, __pyx_k_OnRspQryExchange, sizeof(__pyx_k_OnRspQryExchange), 0, 0, 1, 1},
  {&__pyx_n_s_OnRspQryExchangeMarginRate, __pyx_k_OnRspQryExchangeMarginRate, sizeof(__pyx_k_OnRspQryExchangeMarginRate), 0, 0, 1, 1},
  {&__pyx_n_s_OnRspQryExchangeMarginRateAdjust, __pyx_k_OnRspQryExchangeMarginRateAdjust, sizeof(__pyx_k_OnRspQryExchangeMarginRateAdjust), 0, 0, 1, 1},
  {&__pyx_n_s_OnRspQryExchangeRate, __pyx_k_OnRspQryExchangeRate, sizeof(__pyx_k_OnRspQryExchangeRate), 0, 0, 1, 1},
  {&__pyx_n_s_OnRspQryInstrument, __pyx_k_OnRspQryInstrument, sizeof(__pyx_k_OnRspQryInstrument), 0, 0, 1, 1},
  {&__pyx_n_s_OnRspQryInstrumentCommissionRate, __pyx_k_OnRspQryInstrumentCommissionRate, sizeof(__pyx_k_OnRspQryInstrumentCommissionRate), 0, 0, 1, 1},
  {&__pyx_n_s_OnRspQryInstrumentMarginRate, __pyx_k_OnRspQryInstrumentMarginRate, sizeof(__pyx_k_OnRspQryInstrumentMarginRate), 0, 0, 1, 1},
  {&__pyx_n_s_OnRspQryInvestor, __pyx_k_OnRspQryInvestor, sizeof(__pyx_k_OnRspQryInvestor), 0, 0, 1, 1},
  {&__pyx_n_s_OnRspQryInvestorPosition, __pyx_k_OnRspQryInvestorPosition, sizeof(__pyx_k_OnRspQryInvestorPosition), 0, 0, 1, 1},
  {&__pyx_n_s_OnRspQryInvestorPositionCombineD, __pyx_k_OnRspQryInvestorPositionCombineD, sizeof(__pyx_k_OnRspQryInvestorPositionCombineD), 0, 0, 1, 1},
  {&__pyx_n_s_OnRspQryInvestorPositionDetail, __pyx_k_OnRspQryInvestorPositionDetail, sizeof(__pyx_k_OnRspQryInvestorPositionDetail), 0, 0, 1, 1},
  {&__pyx_n_s_OnRspQryInvestorProductGroupMarg, __pyx_k_OnRspQryInvestorProductGroupMarg, sizeof(__pyx_k_OnRspQryInvestorProductGroupMarg), 0, 0, 1, 1},
  {&__pyx_n_s_OnRspQryNotice, __pyx_k_OnRspQryNotice, sizeof(__pyx_k_OnRspQryNotice), 0, 0, 1, 1},
  {&__pyx_n_s_OnRspQryOrder, __pyx_k_OnRspQryOrder, sizeof(__pyx_k_OnRspQryOrder), 0, 0, 1, 1},
  {&__pyx_n_s_OnRspQryParkedOrder, __pyx_k_OnRspQryParkedOrder, sizeof(__pyx_k_OnRspQryParkedOrder), 0, 0, 1, 1},
  {&__pyx_n_s_OnRspQryParkedOrderAction, __pyx_k_OnRspQryParkedOrderAction, sizeof(__pyx_k_OnRspQryParkedOrderAction), 0, 0, 1, 1},
  {&__pyx_n_s_OnRspQryProduct, __pyx_k_OnRspQryProduct, sizeof(__pyx_k_OnRspQryProduct), 0, 0, 1, 1},
  {&__pyx_n_s_OnRspQrySecAgentACIDMap, __pyx_k_OnRspQrySecAgentACIDMap, sizeof(__pyx_k_OnRspQrySecAgentACIDMap), 0, 0, 1, 1},
  {&__pyx_n_s_OnRspQrySettlementInfo, __pyx_k_OnRspQrySettlementInfo, sizeof(__pyx_k_OnRspQrySettlementInfo), 0, 0, 1, 1},
  {&__pyx_n_s_OnRspQrySettlementInfoConfirm, __pyx_k_OnRspQrySettlementInfoConfirm, sizeof(__pyx_k_OnRspQrySettlementInfoConfirm), 0, 0, 1, 1},
  {&__pyx_n_s_OnRspQryTrade, __pyx_k_OnRspQryTrade, sizeof(__pyx_k_OnRspQryTrade), 0, 0, 1, 1},
  {&__pyx_n_s_OnRspQryTradingAccount, __pyx_k_OnRspQryTradingAccount, sizeof(__pyx_k_OnRspQryTradingAccount), 0, 0, 1, 1},
  {&__pyx_n_s_OnRspQryTradingCode, __pyx_k_OnRspQryTradingCode, sizeof(__pyx_k_OnRspQryTradingCode), 0, 0, 1, 1},
  {&__pyx_n_s_OnRspQryTradingNotice, __pyx_k_OnRspQryTradingNotice, sizeof(__pyx_k_OnRspQryTradingNotice), 0, 0, 1, 1},
  {&__pyx_n_s_OnRspQryTransferBank, __pyx_k_OnRspQryTransferBank, sizeof(__pyx_k_OnRspQryTransferBank), 0, 0, 1, 1},
  {&__pyx_n_s_OnRspQryTransferSerial, __pyx_k_OnRspQryTransferSerial, sizeof(__pyx_k_OnRspQryTransferSerial), 0, 0, 1, 1},
  {&__pyx_n_s_OnRspQueryBankAccountMoneyByFutu, __pyx_k_OnRspQueryBankAccountMoneyByFutu, sizeof(__pyx_k_OnRspQueryBankAccountMoneyByFutu), 0, 0, 1, 1},
  {&__pyx_n_s_OnRspQueryCFMMCTradingAccountTok, __pyx_k_OnRspQueryCFMMCTradingAccountTok, sizeof(__pyx_k_OnRspQueryCFMMCTradingAccountTok), 0, 0, 1, 1},
  {&__pyx_n_s_OnRspQueryMaxOrderVolume, __pyx_k_OnRspQueryMaxOrderVolume, sizeof(__pyx_k_OnRspQueryMaxOrderVolume), 0, 0, 1, 1},
  {&__pyx_n_s_OnRspRemoveParkedOrder, __pyx_k_OnRspRemoveParkedOrder, sizeof(__pyx_k_OnRspRemoveParkedOrder), 0, 0, 1, 1},
  {&__pyx_n_s_OnRspRemoveParkedOrderAction, __pyx_k_OnRspRemoveParkedOrderAction, sizeof(__pyx_k_OnRspRemoveParkedOrderAction), 0, 0, 1, 1},
  {&__pyx_n_s_OnRspSettlementInfoConfirm, __pyx_k_OnRspSettlementInfoConfirm, sizeof(__pyx_k_OnRspSettlementInfoConfirm), 0, 0, 1, 1},
  {&__pyx_n_s_OnRspTradingAccountPasswordUpdat, __pyx_k_OnRspTradingAccountPasswordUpdat, sizeof(__pyx_k_OnRspTradingAccountPasswordUpdat), 0, 0, 1, 1},
  {&__pyx_n_s_OnRspUserLogin, __pyx_k_OnRspUserLogin, sizeof(__pyx_k_OnRspUserLogin), 0, 0, 1, 1},
  {&__pyx_n_s_OnRspUserLogout, __pyx_k_OnRspUserLogout, sizeof(__pyx_k_OnRspUserLogout), 0, 0, 1, 1},
  {&__pyx_n_s_OnRspUserPasswordUpdate, __pyx_k_OnRspUserPasswordUpdate, sizeof(__pyx_k_OnRspUserPasswordUpdate), 0, 0, 1, 1},
  {&__pyx_n_s_OnRtnCFMMCTradingAccountToken, __pyx_k_OnRtnCFMMCTradingAccountToken, sizeof(__pyx_k_OnRtnCFMMCTradingAccountToken), 0, 0, 1, 1},
  {&__pyx_n_s_OnRtnCancelAccountByBank, __pyx_k_OnRtnCancelAccountByBank, sizeof(__pyx_k_OnRtnCancelAccountByBank), 0, 0, 1, 1},
  {&__pyx_n_s_OnRtnChangeAccountByBank, __pyx_k_OnRtnChangeAccountByBank, sizeof(__pyx_k_OnRtnChangeAccountByBank), 0, 0, 1, 1},
  {&__pyx_n_s_OnRtnErrorConditionalOrder, __pyx_k_OnRtnErrorConditionalOrder, sizeof(__pyx_k_OnRtnErrorConditionalOrder), 0, 0, 1, 1},
  {&__pyx_n_s_OnRtnFromBankToFutureByBank, __pyx_k_OnRtnFromBankToFutureByBank, sizeof(__pyx_k_OnRtnFromBankToFutureByBank), 0, 0, 1, 1},
  {&__pyx_n_s_OnRtnFromBankToFutureByFuture, __pyx_k_OnRtnFromBankToFutureByFuture, sizeof(__pyx_k_OnRtnFromBankToFutureByFuture), 0, 0, 1, 1},
  {&__pyx_n_s_OnRtnFromFutureToBankByBank, __pyx_k_OnRtnFromFutureToBankByBank, sizeof(__pyx_k_OnRtnFromFutureToBankByBank), 0, 0, 1, 1},
  {&__pyx_n_s_OnRtnFromFutureToBankByFuture, __pyx_k_OnRtnFromFutureToBankByFuture, sizeof(__pyx_k_OnRtnFromFutureToBankByFuture), 0, 0, 1, 1},
  {&__pyx_n_s_OnRtnInstrumentStatus, __pyx_k_OnRtnInstrumentStatus, sizeof(__pyx_k_OnRtnInstrumentStatus), 0, 0, 1, 1},
  {&__pyx_n_s_OnRtnOpenAccountByBank, __pyx_k_OnRtnOpenAccountByBank, sizeof(__pyx_k_OnRtnOpenAccountByBank), 0, 0, 1, 1},
  {&__pyx_n_s_OnRtnOrder, __pyx_k_OnRtnOrder, sizeof(__pyx_k_OnRtnOrder), 0, 0, 1, 1},
  {&__pyx_n_s_OnRtnQueryBankBalanceByFuture, __pyx_k_OnRtnQueryBankBalanceByFuture, sizeof(__pyx_k_OnRtnQueryBankBalanceByFuture), 0, 0, 1, 1},
  {&__pyx_n_s_OnRtnRepealFromBankToFutureByBan, __pyx_k_OnRtnRepealFromBankToFutureByBan, sizeof(__pyx_k_OnRtnRepealFromBankToFutureByBan), 0, 0, 1, 1},
  {&__pyx_n_s_OnRtnRepealFromBankToFutureByFut, __pyx_k_OnRtnRepealFromBankToFutureByFut, sizeof(__pyx_k_OnRtnRepealFromBankToFutureByFut), 0, 0, 1, 1},
  {&__pyx_n_s_OnRtnRepealFromBankToFutureByFut_2, __pyx_k_OnRtnRepealFromBankToFutureByFut_2, sizeof(__pyx_k_OnRtnRepealFromBankToFutureByFut_2), 0, 0, 1, 1},
  {&__pyx_n_s_OnRtnRepealFromFutureToBankByBan, __pyx_k_OnRtnRepealFromFutureToBankByBan, sizeof(__pyx_k_OnRtnRepealFromFutureToBankByBan), 0, 0, 1, 1},
  {&__pyx_n_s_OnRtnRepealFromFutureToBankByFut, __pyx_k_OnRtnRepealFromFutureToBankByFut, sizeof(__pyx_k_OnRtnRepealFromFutureToBankByFut), 0, 0, 1, 1},
  {&__pyx_n_s_OnRtnRepealFromFutureToBankByFut_2, __pyx_k_OnRtnRepealFromFutureToBankByFut_2, sizeof(__pyx_k_OnRtnRepealFromFutureToBankByFut_2), 0, 0, 1, 1},
  {&__pyx_n_s_OnRtnTrade, __pyx_k_OnRtnTrade, sizeof(__pyx_k_OnRtnTrade), 0, 0, 1, 1},
  {&__pyx_n_s_OnRtnTradingNotice, __pyx_k_OnRtnTradingNotice, sizeof(__pyx_k_OnRtnTradingNotice), 0, 0, 1, 1},
  {&__pyx_n_s_main, __pyx_k_main, sizeof(__pyx_k_main), 0, 0, 1, 1},
  {&__pyx_n_s_nRequestID, __pyx_k_nRequestID, sizeof(__pyx_k_nRequestID), 0, 0, 1, 1},
  {&__pyx_n_s_pInputOrder, __pyx_k_pInputOrder, sizeof(__pyx_k_pInputOrder), 0, 0, 1, 1},
  {&__pyx_n_s_pInputOrderAction, __pyx_k_pInputOrderAction, sizeof(__pyx_k_pInputOrderAction), 0, 0, 1, 1},
  {&__pyx_n_s_pParkedOrder, __pyx_k_pParkedOrder, sizeof(__pyx_k_pParkedOrder), 0, 0, 1, 1},
  {&__pyx_n_s_pParkedOrderAction, __pyx_k_pParkedOrderAction, sizeof(__pyx_k_pParkedOrderAction), 0, 0, 1, 1},
  {&__pyx_n_s_pQryAccountregister, __pyx_k_pQryAccountregister, sizeof(__pyx_k_pQryAccountregister), 0, 0, 1, 1},
  {&__pyx_n_s_pQryBrokerTradingAlgos, __pyx_k_pQryBrokerTradingAlgos, sizeof(__pyx_k_pQryBrokerTradingAlgos), 0, 0, 1, 1},
  {&__pyx_n_s_pQryBrokerTradingParams, __pyx_k_pQryBrokerTradingParams, sizeof(__pyx_k_pQryBrokerTradingParams), 0, 0, 1, 1},
  {&__pyx_n_s_pQryCFMMCTradingAccountKey, __pyx_k_pQryCFMMCTradingAccountKey, sizeof(__pyx_k_pQryCFMMCTradingAccountKey), 0, 0, 1, 1},
  {&__pyx_n_s_pQryContractBank, __pyx_k_pQryContractBank, sizeof(__pyx_k_pQryContractBank), 0, 0, 1, 1},
  {&__pyx_n_s_pQryDepthMarketData, __pyx_k_pQryDepthMarketData, sizeof(__pyx_k_pQryDepthMarketData), 0, 0, 1, 1},
  {&__pyx_n_s_pQryEWarrantOffset, __pyx_k_pQryEWarrantOffset, sizeof(__pyx_k_pQryEWarrantOffset), 0, 0, 1, 1},
  {&__pyx_n_s_pQryExchange, __pyx_k_pQryExchange, sizeof(__pyx_k_pQryExchange), 0, 0, 1, 1},
  {&__pyx_n_s_pQryExchangeMarginRate, __pyx_k_pQryExchangeMarginRate, sizeof(__pyx_k_pQryExchangeMarginRate), 0, 0, 1, 1},
  {&__pyx_n_s_pQryExchangeMarginRateAdjust, __pyx_k_pQryExchangeMarginRateAdjust, sizeof(__pyx_k_pQryExchangeMarginRateAdjust), 0, 0, 1, 1},
  {&__pyx_n_s_pQryExchangeRate, __pyx_k_pQryExchangeRate, sizeof(__pyx_k_pQryExchangeRate), 0, 0, 1, 1},
  {&__pyx_n_s_pQryInstrument, __pyx_k_pQryInstrument, sizeof(__pyx_k_pQryInstrument), 0, 0, 1, 1},
  {&__pyx_n_s_pQryInstrumentCommissionRate, __pyx_k_pQryInstrumentCommissionRate, sizeof(__pyx_k_pQryInstrumentCommissionRate), 0, 0, 1, 1},
  {&__pyx_n_s_pQryInstrumentMarginRate, __pyx_k_pQryInstrumentMarginRate, sizeof(__pyx_k_pQryInstrumentMarginRate), 0, 0, 1, 1},
  {&__pyx_n_s_pQryInvestor, __pyx_k_pQryInvestor, sizeof(__pyx_k_pQryInvestor), 0, 0, 1, 1},
  {&__pyx_n_s_pQryInvestorPosition, __pyx_k_pQryInvestorPosition, sizeof(__pyx_k_pQryInvestorPosition), 0, 0, 1, 1},
  {&__pyx_n_s_pQryInvestorPositionCombineDetai, __pyx_k_pQryInvestorPositionCombineDetai, sizeof(__pyx_k_pQryInvestorPositionCombineDetai), 0, 0, 1, 1},
  {&__pyx_n_s_pQryInvestorPositionDetail, __pyx_k_pQryInvestorPositionDetail, sizeof(__pyx_k_pQryInvestorPositionDetail), 0, 0, 1, 1},
  {&__pyx_n_s_pQryInvestorProductGroupMargin, __pyx_k_pQryInvestorProductGroupMargin, sizeof(__pyx_k_pQryInvestorProductGroupMargin), 0, 0, 1, 1},
  {&__pyx_n_s_pQryNotice, __pyx_k_pQryNotice, sizeof(__pyx_k_pQryNotice), 0, 0, 1, 1},
  {&__pyx_n_s_pQryOrder, __pyx_k_pQryOrder, sizeof(__pyx_k_pQryOrder), 0, 0, 1, 1},
  {&__pyx_n_s_pQryParkedOrder, __pyx_k_pQryParkedOrder, sizeof(__pyx_k_pQryParkedOrder), 0, 0, 1, 1},
  {&__pyx_n_s_pQryParkedOrderAction, __pyx_k_pQryParkedOrderAction, sizeof(__pyx_k_pQryParkedOrderAction), 0, 0, 1, 1},
  {&__pyx_n_s_pQryProduct, __pyx_k_pQryProduct, sizeof(__pyx_k_pQryProduct), 0, 0, 1, 1},
  {&__pyx_n_s_pQrySecAgentACIDMap, __pyx_k_pQrySecAgentACIDMap, sizeof(__pyx_k_pQrySecAgentACIDMap), 0, 0, 1, 1},
  {&__pyx_n_s_pQrySettlementInfo, __pyx_k_pQrySettlementInfo, sizeof(__pyx_k_pQrySettlementInfo), 0, 0, 1, 1},
  {&__pyx_n_s_pQrySettlementInfoConfirm, __pyx_k_pQrySettlementInfoConfirm, sizeof(__pyx_k_pQrySettlementInfoConfirm), 0, 0, 1, 1},
  {&__pyx_n_s_pQryTrade, __pyx_k_pQryTrade, sizeof(__pyx_k_pQryTrade), 0, 0, 1, 1},
  {&__pyx_n_s_pQryTradingAccount, __pyx_k_pQryTradingAccount, sizeof(__pyx_k_pQryTradingAccount), 0, 0, 1, 1},
  {&__pyx_n_s_pQryTradingCode, __pyx_k_pQryTradingCode, sizeof(__pyx_k_pQryTradingCode), 0, 0, 1, 1},
  {&__pyx_n_s_pQryTradingNotice, __pyx_k_pQryTradingNotice, sizeof(__pyx_k_pQryTradingNotice), 0, 0, 1, 1},
  {&__pyx_n_s_pQryTransferBank, __pyx_k_pQryTransferBank, sizeof(__pyx_k_pQryTransferBank), 0, 0, 1, 1},
  {&__pyx_n_s_pQryTransferSerial, __pyx_k_pQryTransferSerial, sizeof(__pyx_k_pQryTransferSerial), 0, 0, 1, 1},
  {&__pyx_n_s_pQueryCFMMCTradingAccountToken, __pyx_k_pQueryCFMMCTradingAccountToken, sizeof(__pyx_k_pQueryCFMMCTradingAccountToken), 0, 0, 1, 1},
  {&__pyx_n_s_pQueryMaxOrderVolume, __pyx_k_pQueryMaxOrderVolume, sizeof(__pyx_k_pQueryMaxOrderVolume), 0, 0, 1, 1},
  {&__pyx_n_s_pRemoveParkedOrder, __pyx_k_pRemoveParkedOrder, sizeof(__pyx_k_pRemoveParkedOrder), 0, 0, 1, 1},
  {&__pyx_n_s_pRemoveParkedOrderAction, __pyx_k_pRemoveParkedOrderAction, sizeof(__pyx_k_pRemoveParkedOrderAction), 0, 0, 1, 1},
  {&__pyx_n_s_pReqAuthenticate, __pyx_k_pReqAuthenticate, sizeof(__pyx_k_pReqAuthenticate), 0, 0, 1, 1},
  {&__pyx_n_s_pReqQueryAccount, __pyx_k_pReqQueryAccount, sizeof(__pyx_k_pReqQueryAccount), 0, 0, 1, 1},
  {&__pyx_n_s_pReqTransfer, __pyx_k_pReqTransfer, sizeof(__pyx_k_pReqTransfer), 0, 0, 1, 1},
  {&__pyx_n_s_pReqUserLogin, __pyx_k_pReqUserLogin, sizeof(__pyx_k_pReqUserLogin), 0, 0, 1, 1},
  {&__pyx_n_s_pSettlementInfoConfirm, __pyx_k_pSettlementInfoConfirm, sizeof(__pyx_k_pSettlementInfoConfirm), 0, 0, 1, 1},
  {&__pyx_n_s_pTradingAccountPasswordUpdate, __pyx_k_pTradingAccountPasswordUpdate, sizeof(__pyx_k_pTradingAccountPasswordUpdate), 0, 0, 1, 1},
  {&__pyx_n_s_pUserLogout, __pyx_k_pUserLogout, sizeof(__pyx_k_pUserLogout), 0, 0, 1, 1},
  {&__pyx_n_s_pUserPasswordUpdate, __pyx_k_pUserPasswordUpdate, sizeof(__pyx_k_pUserPasswordUpdate), 0, 0, 1, 1},
  {&__pyx_n_s_pszFlowPath, __pyx_k_pszFlowPath, sizeof(__pyx_k_pszFlowPath), 0, 0, 1, 1},
  {&__pyx_n_s_test, __pyx_k_test, sizeof(__pyx_k_test), 0, 0, 1, 1},
  {0, 0, 0, 0, 0, 0, 0}
};
static int __Pyx_InitCachedBuiltins(void) {
  return 0;
}
static int __Pyx_InitCachedConstants(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_InitCachedConstants", 0);
  __Pyx_RefNannyFinishContext();
  return 0;
}
static int __Pyx_InitGlobals(void) {
  if (__Pyx_InitStrings(__pyx_string_tab) < 0) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 1; __pyx_clineno = __LINE__; goto __pyx_L1_error;};
  return 0;
  __pyx_L1_error:;
  return -1;
}
#if PY_MAJOR_VERSION < 3
PyMODINIT_FUNC init_TraderApi(void); 
PyMODINIT_FUNC init_TraderApi(void)
#else
PyMODINIT_FUNC PyInit__TraderApi(void); 
PyMODINIT_FUNC PyInit__TraderApi(void)
#endif
{
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  int __pyx_t_3;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannyDeclarations
  #if CYTHON_REFNANNY
  __Pyx_RefNanny = __Pyx_RefNannyImportAPI("refnanny");
  if (!__Pyx_RefNanny) {
      PyErr_Clear();
      __Pyx_RefNanny = __Pyx_RefNannyImportAPI("Cython.Runtime.refnanny");
      if (!__Pyx_RefNanny)
          Py_FatalError("failed to import 'refnanny' module");
  }
  #endif
  __Pyx_RefNannySetupContext("PyMODINIT_FUNC PyInit__TraderApi(void)", 0);
  if ( __Pyx_check_binary_version() < 0) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 1; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __pyx_empty_tuple = PyTuple_New(0); if (unlikely(!__pyx_empty_tuple)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 1; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __pyx_empty_bytes = PyBytes_FromStringAndSize("", 0); if (unlikely(!__pyx_empty_bytes)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 1; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  #ifdef __Pyx_CyFunction_USED
  if (__Pyx_CyFunction_init() < 0) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 1; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  #endif
  #ifdef __Pyx_FusedFunction_USED
  if (__pyx_FusedFunction_init() < 0) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 1; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  #endif
  #ifdef __Pyx_Generator_USED
  if (__pyx_Generator_init() < 0) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 1; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  #endif
  #if defined(__PYX_FORCE_INIT_THREADS) && __PYX_FORCE_INIT_THREADS
  #ifdef WITH_THREAD 
  PyEval_InitThreads();
  #endif
  #endif
  #if PY_MAJOR_VERSION < 3
  __pyx_m = Py_InitModule4(__Pyx_NAMESTR("_TraderApi"), __pyx_methods, 0, 0, PYTHON_API_VERSION); Py_XINCREF(__pyx_m);
  #else
  __pyx_m = PyModule_Create(&__pyx_moduledef);
  #endif
  if (unlikely(!__pyx_m)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 1; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __pyx_d = PyModule_GetDict(__pyx_m); if (unlikely(!__pyx_d)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 1; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  Py_INCREF(__pyx_d);
  __pyx_b = PyImport_AddModule(__Pyx_NAMESTR(__Pyx_BUILTIN_MODULE_NAME)); if (unlikely(!__pyx_b)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 1; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  #if CYTHON_COMPILING_IN_PYPY
  Py_INCREF(__pyx_b);
  #endif
  if (__Pyx_SetAttrString(__pyx_m, "__builtins__", __pyx_b) < 0) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 1; __pyx_clineno = __LINE__; goto __pyx_L1_error;};
  if (unlikely(__Pyx_InitGlobals() < 0)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 1; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  #if PY_MAJOR_VERSION < 3 && (__PYX_DEFAULT_STRING_ENCODING_IS_ASCII || __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT)
  if (__Pyx_init_sys_getdefaultencoding_params() < 0) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 1; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  #endif
  if (__pyx_module_is_main_ctp___TraderApi) {
    if (__Pyx_SetAttrString(__pyx_m, "__name__", __pyx_n_s_main) < 0) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 1; __pyx_clineno = __LINE__; goto __pyx_L1_error;};
  }
  #if PY_MAJOR_VERSION >= 3
  {
    PyObject *modules = PyImport_GetModuleDict(); if (unlikely(!modules)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 1; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    if (!PyDict_GetItemString(modules, "ctp._TraderApi")) {
      if (unlikely(PyDict_SetItemString(modules, "ctp._TraderApi", __pyx_m) < 0)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 1; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    }
  }
  #endif
  if (unlikely(__Pyx_InitCachedBuiltins() < 0)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 1; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  if (unlikely(__Pyx_InitCachedConstants() < 0)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 1; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __pyx_v_3ctp_10_TraderApi_ApiStruct_addressof = Py_None; Py_INCREF(Py_None);
  __pyx_v_3ctp_10_TraderApi_ApiStruct_Accountregister = Py_None; Py_INCREF(Py_None);
  __pyx_v_3ctp_10_TraderApi_ApiStruct_BrokerTradingAlgos = Py_None; Py_INCREF(Py_None);
  __pyx_v_3ctp_10_TraderApi_ApiStruct_BrokerTradingParams = Py_None; Py_INCREF(Py_None);
  __pyx_v_3ctp_10_TraderApi_ApiStruct_CFMMCTradingAccountKey = Py_None; Py_INCREF(Py_None);
  __pyx_v_3ctp_10_TraderApi_ApiStruct_CFMMCTradingAccountToken = Py_None; Py_INCREF(Py_None);
  __pyx_v_3ctp_10_TraderApi_ApiStruct_CancelAccount = Py_None; Py_INCREF(Py_None);
  __pyx_v_3ctp_10_TraderApi_ApiStruct_ChangeAccount = Py_None; Py_INCREF(Py_None);
  __pyx_v_3ctp_10_TraderApi_ApiStruct_ContractBank = Py_None; Py_INCREF(Py_None);
  __pyx_v_3ctp_10_TraderApi_ApiStruct_DepthMarketData = Py_None; Py_INCREF(Py_None);
  __pyx_v_3ctp_10_TraderApi_ApiStruct_EWarrantOffset = Py_None; Py_INCREF(Py_None);
  __pyx_v_3ctp_10_TraderApi_ApiStruct_ErrorConditionalOrder = Py_None; Py_INCREF(Py_None);
  __pyx_v_3ctp_10_TraderApi_ApiStruct_Exchange = Py_None; Py_INCREF(Py_None);
  __pyx_v_3ctp_10_TraderApi_ApiStruct_ExchangeMarginRate = Py_None; Py_INCREF(Py_None);
  __pyx_v_3ctp_10_TraderApi_ApiStruct_ExchangeMarginRateAdjust = Py_None; Py_INCREF(Py_None);
  __pyx_v_3ctp_10_TraderApi_ApiStruct_ExchangeRate = Py_None; Py_INCREF(Py_None);
  __pyx_v_3ctp_10_TraderApi_ApiStruct_InputOrder = Py_None; Py_INCREF(Py_None);
  __pyx_v_3ctp_10_TraderApi_ApiStruct_InputOrderAction = Py_None; Py_INCREF(Py_None);
  __pyx_v_3ctp_10_TraderApi_ApiStruct_Instrument = Py_None; Py_INCREF(Py_None);
  __pyx_v_3ctp_10_TraderApi_ApiStruct_InstrumentCommissionRate = Py_None; Py_INCREF(Py_None);
  __pyx_v_3ctp_10_TraderApi_ApiStruct_InstrumentMarginRate = Py_None; Py_INCREF(Py_None);
  __pyx_v_3ctp_10_TraderApi_ApiStruct_InstrumentStatus = Py_None; Py_INCREF(Py_None);
  __pyx_v_3ctp_10_TraderApi_ApiStruct_Investor = Py_None; Py_INCREF(Py_None);
  __pyx_v_3ctp_10_TraderApi_ApiStruct_InvestorPosition = Py_None; Py_INCREF(Py_None);
  __pyx_v_3ctp_10_TraderApi_ApiStruct_InvestorPositionCombineDetail = Py_None; Py_INCREF(Py_None);
  __pyx_v_3ctp_10_TraderApi_ApiStruct_InvestorPositionDetail = Py_None; Py_INCREF(Py_None);
  __pyx_v_3ctp_10_TraderApi_ApiStruct_InvestorProductGroupMargin = Py_None; Py_INCREF(Py_None);
  __pyx_v_3ctp_10_TraderApi_ApiStruct_Notice = Py_None; Py_INCREF(Py_None);
  __pyx_v_3ctp_10_TraderApi_ApiStruct_NotifyQueryAccount = Py_None; Py_INCREF(Py_None);
  __pyx_v_3ctp_10_TraderApi_ApiStruct_OpenAccount = Py_None; Py_INCREF(Py_None);
  __pyx_v_3ctp_10_TraderApi_ApiStruct_Order = Py_None; Py_INCREF(Py_None);
  __pyx_v_3ctp_10_TraderApi_ApiStruct_OrderAction = Py_None; Py_INCREF(Py_None);
  __pyx_v_3ctp_10_TraderApi_ApiStruct_ParkedOrder = Py_None; Py_INCREF(Py_None);
  __pyx_v_3ctp_10_TraderApi_ApiStruct_ParkedOrderAction = Py_None; Py_INCREF(Py_None);
  __pyx_v_3ctp_10_TraderApi_ApiStruct_Product = Py_None; Py_INCREF(Py_None);
  __pyx_v_3ctp_10_TraderApi_ApiStruct_QueryCFMMCTradingAccountToken = Py_None; Py_INCREF(Py_None);
  __pyx_v_3ctp_10_TraderApi_ApiStruct_QueryMaxOrderVolume = Py_None; Py_INCREF(Py_None);
  __pyx_v_3ctp_10_TraderApi_ApiStruct_RemoveParkedOrder = Py_None; Py_INCREF(Py_None);
  __pyx_v_3ctp_10_TraderApi_ApiStruct_RemoveParkedOrderAction = Py_None; Py_INCREF(Py_None);
  __pyx_v_3ctp_10_TraderApi_ApiStruct_ReqQueryAccount = Py_None; Py_INCREF(Py_None);
  __pyx_v_3ctp_10_TraderApi_ApiStruct_ReqRepeal = Py_None; Py_INCREF(Py_None);
  __pyx_v_3ctp_10_TraderApi_ApiStruct_ReqTransfer = Py_None; Py_INCREF(Py_None);
  __pyx_v_3ctp_10_TraderApi_ApiStruct_RspAuthenticate = Py_None; Py_INCREF(Py_None);
  __pyx_v_3ctp_10_TraderApi_ApiStruct_RspInfo = Py_None; Py_INCREF(Py_None);
  __pyx_v_3ctp_10_TraderApi_ApiStruct_RspRepeal = Py_None; Py_INCREF(Py_None);
  __pyx_v_3ctp_10_TraderApi_ApiStruct_RspTransfer = Py_None; Py_INCREF(Py_None);
  __pyx_v_3ctp_10_TraderApi_ApiStruct_RspUserLogin = Py_None; Py_INCREF(Py_None);
  __pyx_v_3ctp_10_TraderApi_ApiStruct_SecAgentACIDMap = Py_None; Py_INCREF(Py_None);
  __pyx_v_3ctp_10_TraderApi_ApiStruct_SettlementInfo = Py_None; Py_INCREF(Py_None);
  __pyx_v_3ctp_10_TraderApi_ApiStruct_SettlementInfoConfirm = Py_None; Py_INCREF(Py_None);
  __pyx_v_3ctp_10_TraderApi_ApiStruct_Trade = Py_None; Py_INCREF(Py_None);
  __pyx_v_3ctp_10_TraderApi_ApiStruct_TradingAccount = Py_None; Py_INCREF(Py_None);
  __pyx_v_3ctp_10_TraderApi_ApiStruct_TradingAccountPasswordUpdate = Py_None; Py_INCREF(Py_None);
  __pyx_v_3ctp_10_TraderApi_ApiStruct_TradingCode = Py_None; Py_INCREF(Py_None);
  __pyx_v_3ctp_10_TraderApi_ApiStruct_TradingNotice = Py_None; Py_INCREF(Py_None);
  __pyx_v_3ctp_10_TraderApi_ApiStruct_TradingNoticeInfo = Py_None; Py_INCREF(Py_None);
  __pyx_v_3ctp_10_TraderApi_ApiStruct_TransferBank = Py_None; Py_INCREF(Py_None);
  __pyx_v_3ctp_10_TraderApi_ApiStruct_TransferSerial = Py_None; Py_INCREF(Py_None);
  __pyx_v_3ctp_10_TraderApi_ApiStruct_UserLogout = Py_None; Py_INCREF(Py_None);
  __pyx_v_3ctp_10_TraderApi_ApiStruct_UserPasswordUpdate = Py_None; Py_INCREF(Py_None);
  if (PyType_Ready(&__pyx_type_3ctp_10_TraderApi_TraderApi) < 0) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 77; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __pyx_type_3ctp_10_TraderApi_TraderApi.tp_print = 0;
  if (__Pyx_SetAttrString(__pyx_m, "TraderApi", (PyObject *)&__pyx_type_3ctp_10_TraderApi_TraderApi) < 0) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 77; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __pyx_ptype_3ctp_10_TraderApi_TraderApi = &__pyx_type_3ctp_10_TraderApi_TraderApi;
  XFixSysModules();
  __pyx_t_1 = PyObject_GetAttrString(__pyx_m, S___name__); if (unlikely(!__pyx_t_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 70; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = PyCFunction_NewEx((&_init_method), NULL, __pyx_t_1); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 70; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_3 = PyObject_SetAttrString(__pyx_m, _init_method.ml_name, __pyx_t_2); if (unlikely(__pyx_t_3 == -1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 70; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = PyDict_New(); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 1; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_test, __pyx_t_2) < 0) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 1; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  if (__pyx_m) {
    __Pyx_AddTraceback("init ctp._TraderApi", __pyx_clineno, __pyx_lineno, __pyx_filename);
    Py_DECREF(__pyx_m); __pyx_m = 0;
  } else if (!PyErr_Occurred()) {
    PyErr_SetString(PyExc_ImportError, "init ctp._TraderApi");
  }
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  #if PY_MAJOR_VERSION < 3
  return;
  #else
  return __pyx_m;
  #endif
}
#if CYTHON_REFNANNY
static __Pyx_RefNannyAPIStruct *__Pyx_RefNannyImportAPI(const char *modname) {
    PyObject *m = NULL, *p = NULL;
    void *r = NULL;
    m = PyImport_ImportModule((char *)modname);
    if (!m) goto end;
    p = PyObject_GetAttrString(m, (char *)"RefNannyAPI");
    if (!p) goto end;
    r = PyLong_AsVoidPtr(p);
end:
    Py_XDECREF(p);
    Py_XDECREF(m);
    return (__Pyx_RefNannyAPIStruct *)r;
}
#endif 
static void __Pyx_RaiseDoubleKeywordsError(
    const char* func_name,
    PyObject* kw_name)
{
    PyErr_Format(PyExc_TypeError,
        #if PY_MAJOR_VERSION >= 3
        "%s() got multiple values for keyword argument '%U'", func_name, kw_name);
        #else
        "%s() got multiple values for keyword argument '%s'", func_name,
        PyString_AsString(kw_name));
        #endif
}
static int __Pyx_ParseOptionalKeywords(
    PyObject *kwds,
    PyObject **argnames[],
    PyObject *kwds2,
    PyObject *values[],
    Py_ssize_t num_pos_args,
    const char* function_name)
{
    PyObject *key = 0, *value = 0;
    Py_ssize_t pos = 0;
    PyObject*** name;
    PyObject*** first_kw_arg = argnames + num_pos_args;
    while (PyDict_Next(kwds, &pos, &key, &value)) {
        name = first_kw_arg;
        while (*name && (**name != key)) name++;
        if (*name) {
            values[name-argnames] = value;
            continue;
        }
        name = first_kw_arg;
        #if PY_MAJOR_VERSION < 3
        if (likely(PyString_CheckExact(key)) || likely(PyString_Check(key))) {
            while (*name) {
                if ((CYTHON_COMPILING_IN_PYPY || PyString_GET_SIZE(**name) == PyString_GET_SIZE(key))
                        && _PyString_Eq(**name, key)) {
                    values[name-argnames] = value;
                    break;
                }
                name++;
            }
            if (*name) continue;
            else {
                PyObject*** argname = argnames;
                while (argname != first_kw_arg) {
                    if ((**argname == key) || (
                            (CYTHON_COMPILING_IN_PYPY || PyString_GET_SIZE(**argname) == PyString_GET_SIZE(key))
                             && _PyString_Eq(**argname, key))) {
                        goto arg_passed_twice;
                    }
                    argname++;
                }
            }
        } else
        #endif
        if (likely(PyUnicode_Check(key))) {
            while (*name) {
                int cmp = (**name == key) ? 0 :
                #if !CYTHON_COMPILING_IN_PYPY && PY_MAJOR_VERSION >= 3
                    (PyUnicode_GET_SIZE(**name) != PyUnicode_GET_SIZE(key)) ? 1 :
                #endif
                    PyUnicode_Compare(**name, key);
                if (cmp < 0 && unlikely(PyErr_Occurred())) goto bad;
                if (cmp == 0) {
                    values[name-argnames] = value;
                    break;
                }
                name++;
            }
            if (*name) continue;
            else {
                PyObject*** argname = argnames;
                while (argname != first_kw_arg) {
                    int cmp = (**argname == key) ? 0 :
                    #if !CYTHON_COMPILING_IN_PYPY && PY_MAJOR_VERSION >= 3
                        (PyUnicode_GET_SIZE(**argname) != PyUnicode_GET_SIZE(key)) ? 1 :
                    #endif
                        PyUnicode_Compare(**argname, key);
                    if (cmp < 0 && unlikely(PyErr_Occurred())) goto bad;
                    if (cmp == 0) goto arg_passed_twice;
                    argname++;
                }
            }
        } else
            goto invalid_keyword_type;
        if (kwds2) {
            if (unlikely(PyDict_SetItem(kwds2, key, value))) goto bad;
        } else {
            goto invalid_keyword;
        }
    }
    return 0;
arg_passed_twice:
    __Pyx_RaiseDoubleKeywordsError(function_name, key);
    goto bad;
invalid_keyword_type:
    PyErr_Format(PyExc_TypeError,
        "%.200s() keywords must be strings", function_name);
    goto bad;
invalid_keyword:
    PyErr_Format(PyExc_TypeError,
    #if PY_MAJOR_VERSION < 3
        "%.200s() got an unexpected keyword argument '%.200s'",
        function_name, PyString_AsString(key));
    #else
        "%s() got an unexpected keyword argument '%U'",
        function_name, key);
    #endif
bad:
    return -1;
}
static void __Pyx_RaiseArgtupleInvalid(
    const char* func_name,
    int exact,
    Py_ssize_t num_min,
    Py_ssize_t num_max,
    Py_ssize_t num_found)
{
    Py_ssize_t num_expected;
    const char *more_or_less;
    if (num_found < num_min) {
        num_expected = num_min;
        more_or_less = "at least";
    } else {
        num_expected = num_max;
        more_or_less = "at most";
    }
    if (exact) {
        more_or_less = "exactly";
    }
    PyErr_Format(PyExc_TypeError,
                 "%.200s() takes %.8s %" CYTHON_FORMAT_SSIZE_T "d positional argument%.1s (%" CYTHON_FORMAT_SSIZE_T "d given)",
                 func_name, more_or_less, num_expected,
                 (num_expected == 1) ? "" : "s", num_found);
}
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_Call(PyObject *func, PyObject *arg, PyObject *kw) {
    PyObject *result;
    ternaryfunc call = func->ob_type->tp_call;
    if (unlikely(!call))
        return PyObject_Call(func, arg, kw);
#if PY_VERSION_HEX >= 0x02060000
    if (unlikely(Py_EnterRecursiveCall((char*)" while calling a Python object")))
        return NULL;
#endif
    result = (*call)(func, arg, kw);
#if PY_VERSION_HEX >= 0x02060000
    Py_LeaveRecursiveCall();
#endif
    if (unlikely(!result) && unlikely(!PyErr_Occurred())) {
        PyErr_SetString(
            PyExc_SystemError,
            "NULL result without error in PyObject_Call");
    }
    return result;
}
#endif
#define __PYX_VERIFY_RETURN_INT(target_type, func_type, func) \
    { \
        func_type value = func(x); \
        if (sizeof(target_type) < sizeof(func_type)) { \
            if (unlikely(value != (func_type) (target_type) value)) { \
                func_type zero = 0; \
                PyErr_SetString(PyExc_OverflowError, \
                    (is_unsigned && unlikely(value < zero)) ? \
                    "can't convert negative value to " #target_type : \
                    "value too large to convert to " #target_type); \
                return (target_type) -1; \
            } \
        } \
        return (target_type) value; \
    }
#if CYTHON_COMPILING_IN_CPYTHON && PY_MAJOR_VERSION >= 3
 #if CYTHON_USE_PYLONG_INTERNALS
  #include "longintrepr.h"
 #endif
#endif
static CYTHON_INLINE int __Pyx_PyInt_As_int(PyObject *x) {
    const int neg_one = (int) -1, const_zero = 0;
    const int is_unsigned = neg_one > const_zero;
#if PY_MAJOR_VERSION < 3
    if (likely(PyInt_Check(x))) {
        if (sizeof(int) < sizeof(long)) {
            __PYX_VERIFY_RETURN_INT(int, long, PyInt_AS_LONG)
        } else {
            long val = PyInt_AS_LONG(x);
            if (is_unsigned && unlikely(val < 0)) {
                PyErr_SetString(PyExc_OverflowError,
                                "can't convert negative value to int");
                return (int) -1;
            }
            return (int) val;
        }
    } else
#endif
    if (likely(PyLong_Check(x))) {
        if (is_unsigned) {
#if CYTHON_COMPILING_IN_CPYTHON && PY_MAJOR_VERSION >= 3
 #if CYTHON_USE_PYLONG_INTERNALS
            if (sizeof(digit) <= sizeof(int)) {
                switch (Py_SIZE(x)) {
                    case 0: return 0;
                    case 1: return (int) ((PyLongObject*)x)->ob_digit[0];
                }
            }
 #endif
#endif
            if (unlikely(Py_SIZE(x) < 0)) {
                PyErr_SetString(PyExc_OverflowError,
                                "can't convert negative value to int");
                return (int) -1;
            }
            if (sizeof(int) <= sizeof(unsigned long)) {
                __PYX_VERIFY_RETURN_INT(int, unsigned long, PyLong_AsUnsignedLong)
            } else if (sizeof(int) <= sizeof(unsigned long long)) {
                __PYX_VERIFY_RETURN_INT(int, unsigned long long, PyLong_AsUnsignedLongLong)
            }
        } else {
#if CYTHON_COMPILING_IN_CPYTHON && PY_MAJOR_VERSION >= 3
 #if CYTHON_USE_PYLONG_INTERNALS
            if (sizeof(digit) <= sizeof(int)) {
                switch (Py_SIZE(x)) {
                    case 0: return 0;
                    case 1: return +(int) ((PyLongObject*)x)->ob_digit[0];
                    case -1: return -(int) ((PyLongObject*)x)->ob_digit[0];
                }
            }
 #endif
#endif
            if (sizeof(int) <= sizeof(long)) {
                __PYX_VERIFY_RETURN_INT(int, long, PyLong_AsLong)
            } else if (sizeof(int) <= sizeof(long long)) {
                __PYX_VERIFY_RETURN_INT(int, long long, PyLong_AsLongLong)
            }
        }
        {
#if CYTHON_COMPILING_IN_PYPY && !defined(_PyLong_AsByteArray)
            PyErr_SetString(PyExc_RuntimeError,
                            "_PyLong_AsByteArray() not available in PyPy, cannot convert large numbers");
#else
            int val;
            PyObject *v = __Pyx_PyNumber_Int(x);
 #if PY_MAJOR_VERSION < 3
            if (likely(v) && !PyLong_Check(v)) {
                PyObject *tmp = v;
                v = PyNumber_Long(tmp);
                Py_DECREF(tmp);
            }
 #endif
            if (likely(v)) {
                int one = 1; int is_little = (int)*(unsigned char *)&one;
                unsigned char *bytes = (unsigned char *)&val;
                int ret = _PyLong_AsByteArray((PyLongObject *)v,
                                              bytes, sizeof(val),
                                              is_little, !is_unsigned);
                Py_DECREF(v);
                if (likely(!ret))
                    return val;
            }
#endif
            return (int) -1;
        }
    } else {
        int val;
        PyObject *tmp = __Pyx_PyNumber_Int(x);
        if (!tmp) return (int) -1;
        val = __Pyx_PyInt_As_int(tmp);
        Py_DECREF(tmp);
        return val;
    }
}
static CYTHON_INLINE PyObject* __Pyx_PyInt_From_long(long value) {
    const long neg_one = (long) -1, const_zero = 0;
    const int is_unsigned = neg_one > const_zero;
    if (is_unsigned) {
        if (sizeof(long) < sizeof(long)) {
            return PyInt_FromLong((long) value);
        } else if (sizeof(long) <= sizeof(unsigned long)) {
            return PyLong_FromUnsignedLong((unsigned long) value);
        } else if (sizeof(long) <= sizeof(unsigned long long)) {
            return PyLong_FromUnsignedLongLong((unsigned long long) value);
        }
    } else {
        if (sizeof(long) <= sizeof(long)) {
            return PyInt_FromLong((long) value);
        } else if (sizeof(long) <= sizeof(long long)) {
            return PyLong_FromLongLong((long long) value);
        }
    }
    {
        int one = 1; int little = (int)*(unsigned char *)&one;
        unsigned char *bytes = (unsigned char *)&value;
        return _PyLong_FromByteArray(bytes, sizeof(long),
                                     little, !is_unsigned);
    }
}
static CYTHON_INLINE PyObject* __Pyx_PyInt_From_int(int value) {
    const int neg_one = (int) -1, const_zero = 0;
    const int is_unsigned = neg_one > const_zero;
    if (is_unsigned) {
        if (sizeof(int) < sizeof(long)) {
            return PyInt_FromLong((long) value);
        } else if (sizeof(int) <= sizeof(unsigned long)) {
            return PyLong_FromUnsignedLong((unsigned long) value);
        } else if (sizeof(int) <= sizeof(unsigned long long)) {
            return PyLong_FromUnsignedLongLong((unsigned long long) value);
        }
    } else {
        if (sizeof(int) <= sizeof(long)) {
            return PyInt_FromLong((long) value);
        } else if (sizeof(int) <= sizeof(long long)) {
            return PyLong_FromLongLong((long long) value);
        }
    }
    {
        int one = 1; int little = (int)*(unsigned char *)&one;
        unsigned char *bytes = (unsigned char *)&value;
        return _PyLong_FromByteArray(bytes, sizeof(int),
                                     little, !is_unsigned);
    }
}
#if CYTHON_COMPILING_IN_CPYTHON && PY_MAJOR_VERSION >= 3
 #if CYTHON_USE_PYLONG_INTERNALS
  #include "longintrepr.h"
 #endif
#endif
static CYTHON_INLINE size_t __Pyx_PyInt_As_size_t(PyObject *x) {
    const size_t neg_one = (size_t) -1, const_zero = 0;
    const int is_unsigned = neg_one > const_zero;
#if PY_MAJOR_VERSION < 3
    if (likely(PyInt_Check(x))) {
        if (sizeof(size_t) < sizeof(long)) {
            __PYX_VERIFY_RETURN_INT(size_t, long, PyInt_AS_LONG)
        } else {
            long val = PyInt_AS_LONG(x);
            if (is_unsigned && unlikely(val < 0)) {
                PyErr_SetString(PyExc_OverflowError,
                                "can't convert negative value to size_t");
                return (size_t) -1;
            }
            return (size_t) val;
        }
    } else
#endif
    if (likely(PyLong_Check(x))) {
        if (is_unsigned) {
#if CYTHON_COMPILING_IN_CPYTHON && PY_MAJOR_VERSION >= 3
 #if CYTHON_USE_PYLONG_INTERNALS
            if (sizeof(digit) <= sizeof(size_t)) {
                switch (Py_SIZE(x)) {
                    case 0: return 0;
                    case 1: return (size_t) ((PyLongObject*)x)->ob_digit[0];
                }
            }
 #endif
#endif
            if (unlikely(Py_SIZE(x) < 0)) {
                PyErr_SetString(PyExc_OverflowError,
                                "can't convert negative value to size_t");
                return (size_t) -1;
            }
            if (sizeof(size_t) <= sizeof(unsigned long)) {
                __PYX_VERIFY_RETURN_INT(size_t, unsigned long, PyLong_AsUnsignedLong)
            } else if (sizeof(size_t) <= sizeof(unsigned long long)) {
                __PYX_VERIFY_RETURN_INT(size_t, unsigned long long, PyLong_AsUnsignedLongLong)
            }
        } else {
#if CYTHON_COMPILING_IN_CPYTHON && PY_MAJOR_VERSION >= 3
 #if CYTHON_USE_PYLONG_INTERNALS
            if (sizeof(digit) <= sizeof(size_t)) {
                switch (Py_SIZE(x)) {
                    case 0: return 0;
                    case 1: return +(size_t) ((PyLongObject*)x)->ob_digit[0];
                    case -1: return -(size_t) ((PyLongObject*)x)->ob_digit[0];
                }
            }
 #endif
#endif
            if (sizeof(size_t) <= sizeof(long)) {
                __PYX_VERIFY_RETURN_INT(size_t, long, PyLong_AsLong)
            } else if (sizeof(size_t) <= sizeof(long long)) {
                __PYX_VERIFY_RETURN_INT(size_t, long long, PyLong_AsLongLong)
            }
        }
        {
#if CYTHON_COMPILING_IN_PYPY && !defined(_PyLong_AsByteArray)
            PyErr_SetString(PyExc_RuntimeError,
                            "_PyLong_AsByteArray() not available in PyPy, cannot convert large numbers");
#else
            size_t val;
            PyObject *v = __Pyx_PyNumber_Int(x);
 #if PY_MAJOR_VERSION < 3
            if (likely(v) && !PyLong_Check(v)) {
                PyObject *tmp = v;
                v = PyNumber_Long(tmp);
                Py_DECREF(tmp);
            }
 #endif
            if (likely(v)) {
                int one = 1; int is_little = (int)*(unsigned char *)&one;
                unsigned char *bytes = (unsigned char *)&val;
                int ret = _PyLong_AsByteArray((PyLongObject *)v,
                                              bytes, sizeof(val),
                                              is_little, !is_unsigned);
                Py_DECREF(v);
                if (likely(!ret))
                    return val;
            }
#endif
            return (size_t) -1;
        }
    } else {
        size_t val;
        PyObject *tmp = __Pyx_PyNumber_Int(x);
        if (!tmp) return (size_t) -1;
        val = __Pyx_PyInt_As_size_t(tmp);
        Py_DECREF(tmp);
        return val;
    }
}
#if CYTHON_COMPILING_IN_CPYTHON && PY_MAJOR_VERSION >= 3
 #if CYTHON_USE_PYLONG_INTERNALS
  #include "longintrepr.h"
 #endif
#endif
static CYTHON_INLINE long __Pyx_PyInt_As_long(PyObject *x) {
    const long neg_one = (long) -1, const_zero = 0;
    const int is_unsigned = neg_one > const_zero;
#if PY_MAJOR_VERSION < 3
    if (likely(PyInt_Check(x))) {
        if (sizeof(long) < sizeof(long)) {
            __PYX_VERIFY_RETURN_INT(long, long, PyInt_AS_LONG)
        } else {
            long val = PyInt_AS_LONG(x);
            if (is_unsigned && unlikely(val < 0)) {
                PyErr_SetString(PyExc_OverflowError,
                                "can't convert negative value to long");
                return (long) -1;
            }
            return (long) val;
        }
    } else
#endif
    if (likely(PyLong_Check(x))) {
        if (is_unsigned) {
#if CYTHON_COMPILING_IN_CPYTHON && PY_MAJOR_VERSION >= 3
 #if CYTHON_USE_PYLONG_INTERNALS
            if (sizeof(digit) <= sizeof(long)) {
                switch (Py_SIZE(x)) {
                    case 0: return 0;
                    case 1: return (long) ((PyLongObject*)x)->ob_digit[0];
                }
            }
 #endif
#endif
            if (unlikely(Py_SIZE(x) < 0)) {
                PyErr_SetString(PyExc_OverflowError,
                                "can't convert negative value to long");
                return (long) -1;
            }
            if (sizeof(long) <= sizeof(unsigned long)) {
                __PYX_VERIFY_RETURN_INT(long, unsigned long, PyLong_AsUnsignedLong)
            } else if (sizeof(long) <= sizeof(unsigned long long)) {
                __PYX_VERIFY_RETURN_INT(long, unsigned long long, PyLong_AsUnsignedLongLong)
            }
        } else {
#if CYTHON_COMPILING_IN_CPYTHON && PY_MAJOR_VERSION >= 3
 #if CYTHON_USE_PYLONG_INTERNALS
            if (sizeof(digit) <= sizeof(long)) {
                switch (Py_SIZE(x)) {
                    case 0: return 0;
                    case 1: return +(long) ((PyLongObject*)x)->ob_digit[0];
                    case -1: return -(long) ((PyLongObject*)x)->ob_digit[0];
                }
            }
 #endif
#endif
            if (sizeof(long) <= sizeof(long)) {
                __PYX_VERIFY_RETURN_INT(long, long, PyLong_AsLong)
            } else if (sizeof(long) <= sizeof(long long)) {
                __PYX_VERIFY_RETURN_INT(long, long long, PyLong_AsLongLong)
            }
        }
        {
#if CYTHON_COMPILING_IN_PYPY && !defined(_PyLong_AsByteArray)
            PyErr_SetString(PyExc_RuntimeError,
                            "_PyLong_AsByteArray() not available in PyPy, cannot convert large numbers");
#else
            long val;
            PyObject *v = __Pyx_PyNumber_Int(x);
 #if PY_MAJOR_VERSION < 3
            if (likely(v) && !PyLong_Check(v)) {
                PyObject *tmp = v;
                v = PyNumber_Long(tmp);
                Py_DECREF(tmp);
            }
 #endif
            if (likely(v)) {
                int one = 1; int is_little = (int)*(unsigned char *)&one;
                unsigned char *bytes = (unsigned char *)&val;
                int ret = _PyLong_AsByteArray((PyLongObject *)v,
                                              bytes, sizeof(val),
                                              is_little, !is_unsigned);
                Py_DECREF(v);
                if (likely(!ret))
                    return val;
            }
#endif
            return (long) -1;
        }
    } else {
        long val;
        PyObject *tmp = __Pyx_PyNumber_Int(x);
        if (!tmp) return (long) -1;
        val = __Pyx_PyInt_As_long(tmp);
        Py_DECREF(tmp);
        return val;
    }
}
static int __Pyx_check_binary_version(void) {
    char ctversion[4], rtversion[4];
    PyOS_snprintf(ctversion, 4, "%d.%d", PY_MAJOR_VERSION, PY_MINOR_VERSION);
    PyOS_snprintf(rtversion, 4, "%s", Py_GetVersion());
    if (ctversion[0] != rtversion[0] || ctversion[2] != rtversion[2]) {
        char message[200];
        PyOS_snprintf(message, sizeof(message),
                      "compiletime version %s of module '%.100s' "
                      "does not match runtime version %s",
                      ctversion, __Pyx_MODULE_NAME, rtversion);
        #if PY_VERSION_HEX < 0x02050000
        return PyErr_Warn(NULL, message);
        #else
        return PyErr_WarnEx(NULL, message, 1);
        #endif
    }
    return 0;
}
static int __pyx_bisect_code_objects(__Pyx_CodeObjectCacheEntry* entries, int count, int code_line) {
    int start = 0, mid = 0, end = count - 1;
    if (end >= 0 && code_line > entries[end].code_line) {
        return count;
    }
    while (start < end) {
        mid = (start + end) / 2;
        if (code_line < entries[mid].code_line) {
            end = mid;
        } else if (code_line > entries[mid].code_line) {
             start = mid + 1;
        } else {
            return mid;
        }
    }
    if (code_line <= entries[mid].code_line) {
        return mid;
    } else {
        return mid + 1;
    }
}
static PyCodeObject *__pyx_find_code_object(int code_line) {
    PyCodeObject* code_object;
    int pos;
    if (unlikely(!code_line) || unlikely(!__pyx_code_cache.entries)) {
        return NULL;
    }
    pos = __pyx_bisect_code_objects(__pyx_code_cache.entries, __pyx_code_cache.count, code_line);
    if (unlikely(pos >= __pyx_code_cache.count) || unlikely(__pyx_code_cache.entries[pos].code_line != code_line)) {
        return NULL;
    }
    code_object = __pyx_code_cache.entries[pos].code_object;
    Py_INCREF(code_object);
    return code_object;
}
static void __pyx_insert_code_object(int code_line, PyCodeObject* code_object) {
    int pos, i;
    __Pyx_CodeObjectCacheEntry* entries = __pyx_code_cache.entries;
    if (unlikely(!code_line)) {
        return;
    }
    if (unlikely(!entries)) {
        entries = (__Pyx_CodeObjectCacheEntry*)PyMem_Malloc(64*sizeof(__Pyx_CodeObjectCacheEntry));
        if (likely(entries)) {
            __pyx_code_cache.entries = entries;
            __pyx_code_cache.max_count = 64;
            __pyx_code_cache.count = 1;
            entries[0].code_line = code_line;
            entries[0].code_object = code_object;
            Py_INCREF(code_object);
        }
        return;
    }
    pos = __pyx_bisect_code_objects(__pyx_code_cache.entries, __pyx_code_cache.count, code_line);
    if ((pos < __pyx_code_cache.count) && unlikely(__pyx_code_cache.entries[pos].code_line == code_line)) {
        PyCodeObject* tmp = entries[pos].code_object;
        entries[pos].code_object = code_object;
        Py_DECREF(tmp);
        return;
    }
    if (__pyx_code_cache.count == __pyx_code_cache.max_count) {
        int new_max = __pyx_code_cache.max_count + 64;
        entries = (__Pyx_CodeObjectCacheEntry*)PyMem_Realloc(
            __pyx_code_cache.entries, (size_t)new_max*sizeof(__Pyx_CodeObjectCacheEntry));
        if (unlikely(!entries)) {
            return;
        }
        __pyx_code_cache.entries = entries;
        __pyx_code_cache.max_count = new_max;
    }
    for (i=__pyx_code_cache.count; i>pos; i--) {
        entries[i] = entries[i-1];
    }
    entries[pos].code_line = code_line;
    entries[pos].code_object = code_object;
    __pyx_code_cache.count++;
    Py_INCREF(code_object);
}
#include "compile.h"
#include "frameobject.h"
#include "traceback.h"
static PyCodeObject* __Pyx_CreateCodeObjectForTraceback(
            const char *funcname, int c_line,
            int py_line, const char *filename) {
    PyCodeObject *py_code = 0;
    PyObject *py_srcfile = 0;
    PyObject *py_funcname = 0;
    #if PY_MAJOR_VERSION < 3
    py_srcfile = PyString_FromString(filename);
    #else
    py_srcfile = PyUnicode_FromString(filename);
    #endif
    if (!py_srcfile) goto bad;
    if (c_line) {
        #if PY_MAJOR_VERSION < 3
        py_funcname = PyString_FromFormat( "%s (%s:%d)", funcname, __pyx_cfilenm, c_line);
        #else
        py_funcname = PyUnicode_FromFormat( "%s (%s:%d)", funcname, __pyx_cfilenm, c_line);
        #endif
    }
    else {
        #if PY_MAJOR_VERSION < 3
        py_funcname = PyString_FromString(funcname);
        #else
        py_funcname = PyUnicode_FromString(funcname);
        #endif
    }
    if (!py_funcname) goto bad;
    py_code = __Pyx_PyCode_New(
        0, 
        0, 
        0, 
        0, 
        0, 
        __pyx_empty_bytes, 
        __pyx_empty_tuple, 
        __pyx_empty_tuple, 
        __pyx_empty_tuple, 
        __pyx_empty_tuple, 
        __pyx_empty_tuple, 
        py_srcfile, 
        py_funcname, 
        py_line, 
        __pyx_empty_bytes 
    );
    Py_DECREF(py_srcfile);
    Py_DECREF(py_funcname);
    return py_code;
bad:
    Py_XDECREF(py_srcfile);
    Py_XDECREF(py_funcname);
    return NULL;
}
static void __Pyx_AddTraceback(const char *funcname, int c_line,
                               int py_line, const char *filename) {
    PyCodeObject *py_code = 0;
    PyObject *py_globals = 0;
    PyFrameObject *py_frame = 0;
    py_code = __pyx_find_code_object(c_line ? c_line : py_line);
    if (!py_code) {
        py_code = __Pyx_CreateCodeObjectForTraceback(
            funcname, c_line, py_line, filename);
        if (!py_code) goto bad;
        __pyx_insert_code_object(c_line ? c_line : py_line, py_code);
    }
    py_globals = PyModule_GetDict(__pyx_m);
    if (!py_globals) goto bad;
    py_frame = PyFrame_New(
        PyThreadState_GET(), 
        py_code, 
        py_globals, 
        0 
    );
    if (!py_frame) goto bad;
    py_frame->f_lineno = py_line;
    PyTraceBack_Here(py_frame);
bad:
    Py_XDECREF(py_code);
    Py_XDECREF(py_frame);
}
static int __Pyx_InitStrings(__Pyx_StringTabEntry *t) {
    while (t->p) {
        #if PY_MAJOR_VERSION < 3
        if (t->is_unicode) {
            *t->p = PyUnicode_DecodeUTF8(t->s, t->n - 1, NULL);
        } else if (t->intern) {
            *t->p = PyString_InternFromString(t->s);
        } else {
            *t->p = PyString_FromStringAndSize(t->s, t->n - 1);
        }
        #else 
        if (t->is_unicode | t->is_str) {
            if (t->intern) {
                *t->p = PyUnicode_InternFromString(t->s);
            } else if (t->encoding) {
                *t->p = PyUnicode_Decode(t->s, t->n - 1, t->encoding, NULL);
            } else {
                *t->p = PyUnicode_FromStringAndSize(t->s, t->n - 1);
            }
        } else {
            *t->p = PyBytes_FromStringAndSize(t->s, t->n - 1);
        }
        #endif
        if (!*t->p)
            return -1;
        ++t;
    }
    return 0;
}
static CYTHON_INLINE PyObject* __Pyx_PyUnicode_FromString(const char* c_str) {
    return __Pyx_PyUnicode_FromStringAndSize(c_str, (Py_ssize_t)strlen(c_str));
}
static CYTHON_INLINE char* __Pyx_PyObject_AsString(PyObject* o) {
    Py_ssize_t ignore;
    return __Pyx_PyObject_AsStringAndSize(o, &ignore);
}
static CYTHON_INLINE char* __Pyx_PyObject_AsStringAndSize(PyObject* o, Py_ssize_t *length) {
#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII || __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT
    if (
#if PY_MAJOR_VERSION < 3 && __PYX_DEFAULT_STRING_ENCODING_IS_ASCII
            __Pyx_sys_getdefaultencoding_not_ascii &&
#endif
            PyUnicode_Check(o)) {
#if PY_VERSION_HEX < 0x03030000
        char* defenc_c;
        PyObject* defenc = _PyUnicode_AsDefaultEncodedString(o, NULL);
        if (!defenc) return NULL;
        defenc_c = PyBytes_AS_STRING(defenc);
#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII
        {
            char* end = defenc_c + PyBytes_GET_SIZE(defenc);
            char* c;
            for (c = defenc_c; c < end; c++) {
                if ((unsigned char) (*c) >= 128) {
                    PyUnicode_AsASCIIString(o);
                    return NULL;
                }
            }
        }
#endif 
        *length = PyBytes_GET_SIZE(defenc);
        return defenc_c;
#else 
        if (PyUnicode_READY(o) == -1) return NULL;
#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII
        if (PyUnicode_IS_ASCII(o)) {
            *length = PyUnicode_GET_LENGTH(o);
            return PyUnicode_AsUTF8(o);
        } else {
            PyUnicode_AsASCIIString(o);
            return NULL;
        }
#else 
        return PyUnicode_AsUTF8AndSize(o, length);
#endif 
#endif 
    } else
#endif 
#if !CYTHON_COMPILING_IN_PYPY
#if PY_VERSION_HEX >= 0x02060000
    if (PyByteArray_Check(o)) {
        *length = PyByteArray_GET_SIZE(o);
        return PyByteArray_AS_STRING(o);
    } else
#endif
#endif
    {
        char* result;
        int r = PyBytes_AsStringAndSize(o, &result, length);
        if (unlikely(r < 0)) {
            return NULL;
        } else {
            return result;
        }
    }
}
static CYTHON_INLINE int __Pyx_PyObject_IsTrue(PyObject* x) {
   int is_true = x == Py_True;
   if (is_true | (x == Py_False) | (x == Py_None)) return is_true;
   else return PyObject_IsTrue(x);
}
static CYTHON_INLINE PyObject* __Pyx_PyNumber_Int(PyObject* x) {
  PyNumberMethods *m;
  const char *name = NULL;
  PyObject *res = NULL;
#if PY_MAJOR_VERSION < 3
  if (PyInt_Check(x) || PyLong_Check(x))
#else
  if (PyLong_Check(x))
#endif
    return Py_INCREF(x), x;
  m = Py_TYPE(x)->tp_as_number;
#if PY_MAJOR_VERSION < 3
  if (m && m->nb_int) {
    name = "int";
    res = PyNumber_Int(x);
  }
  else if (m && m->nb_long) {
    name = "long";
    res = PyNumber_Long(x);
  }
#else
  if (m && m->nb_int) {
    name = "int";
    res = PyNumber_Long(x);
  }
#endif
  if (res) {
#if PY_MAJOR_VERSION < 3
    if (!PyInt_Check(res) && !PyLong_Check(res)) {
#else
    if (!PyLong_Check(res)) {
#endif
      PyErr_Format(PyExc_TypeError,
                   "__%.4s__ returned non-%.4s (type %.200s)",
                   name, name, Py_TYPE(res)->tp_name);
      Py_DECREF(res);
      return NULL;
    }
  }
  else if (!PyErr_Occurred()) {
    PyErr_SetString(PyExc_TypeError,
                    "an integer is required");
  }
  return res;
}
#if CYTHON_COMPILING_IN_CPYTHON && PY_MAJOR_VERSION >= 3
 #if CYTHON_USE_PYLONG_INTERNALS
  #include "longintrepr.h"
 #endif
#endif
static CYTHON_INLINE Py_ssize_t __Pyx_PyIndex_AsSsize_t(PyObject* b) {
  Py_ssize_t ival;
  PyObject *x;
#if PY_MAJOR_VERSION < 3
  if (likely(PyInt_CheckExact(b)))
      return PyInt_AS_LONG(b);
#endif
  if (likely(PyLong_CheckExact(b))) {
    #if CYTHON_COMPILING_IN_CPYTHON && PY_MAJOR_VERSION >= 3
     #if CYTHON_USE_PYLONG_INTERNALS
       switch (Py_SIZE(b)) {
       case -1: return -(sdigit)((PyLongObject*)b)->ob_digit[0];
       case 0: return 0;
       case 1: return ((PyLongObject*)b)->ob_digit[0];
       }
     #endif
    #endif
  #if PY_VERSION_HEX < 0x02060000
    return PyInt_AsSsize_t(b);
  #else
    return PyLong_AsSsize_t(b);
  #endif
  }
  x = PyNumber_Index(b);
  if (!x) return -1;
  ival = PyInt_AsSsize_t(x);
  Py_DECREF(x);
  return ival;
}
static CYTHON_INLINE PyObject * __Pyx_PyInt_FromSize_t(size_t ival) {
#if PY_VERSION_HEX < 0x02050000
   if (ival <= LONG_MAX)
       return PyInt_FromLong((long)ival);
   else {
       unsigned char *bytes = (unsigned char *) &ival;
       int one = 1; int little = (int)*(unsigned char*)&one;
       return _PyLong_FromByteArray(bytes, sizeof(size_t), little, 0);
   }
#else
   return PyInt_FromSize_t(ival);
#endif
}
#endif 
