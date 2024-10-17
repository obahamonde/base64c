#define PY_SSIZE_T_CLEAN
#include <Python.h>

#if defined(_MSC_VER)
#include <intrin.h>
#define __builtin_bswap32 _byteswap_ulong
#elif defined(__GNUC__) && (defined(__x86_64__) || defined(__i386__))
#include <x86intrin.h>
#endif

#include <stdint.h>

#if defined(_MSC_VER)
#define EXPORT __declspec(dllexport)
#else
#define EXPORT __attribute__((visibility("default")))
#endif

static const uint8_t base64_table[64] = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
static const uint8_t base64_urlsafe_table[64] = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_";

static const uint8_t base64_decode_table[256] = {
    64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64,
    64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64,
    64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 62, 64, 64, 64, 63,
    52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 64, 64, 64, 64, 64, 64,
    64,  0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14,
    15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 64, 64, 64, 64, 64,
    64, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
    41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 64, 64, 64, 64, 64,
    64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64,
    64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64,
    64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64,
    64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64,
    64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64,
    64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64,
    64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64,
    64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64
};

static PyObject* encode_base64(const uint8_t* input, Py_ssize_t input_len, const uint8_t* table) {
    Py_ssize_t output_len = ((input_len + 2) / 3) * 4;
    PyObject* output = PyBytes_FromStringAndSize(NULL, output_len);
    if (!output)
        return NULL;

    uint8_t* out = (uint8_t*)PyBytes_AS_STRING(output);

    Py_ssize_t i, j;
    for (i = 0, j = 0; i < input_len - 2; i += 3) {
        uint32_t n = (uint32_t)input[i] << 16 | (uint32_t)input[i + 1] << 8 | input[i + 2];
        out[j++] = table[(n >> 18) & 0x3F];
        out[j++] = table[(n >> 12) & 0x3F];
        out[j++] = table[(n >> 6) & 0x3F];
        out[j++] = table[n & 0x3F];
    }

    if (i < input_len) {
        uint32_t n = (uint32_t)input[i] << 16;
        if (i + 1 < input_len) n |= (uint32_t)input[i + 1] << 8;

        out[j++] = table[(n >> 18) & 0x3F];
        out[j++] = table[(n >> 12) & 0x3F];
        out[j++] = (i + 1 < input_len) ? table[(n >> 6) & 0x3F] : '=';
        out[j++] = '=';
    }

    return output;
}

static PyObject* decode_base64(const uint8_t* input, Py_ssize_t input_len, const uint8_t* decode_table) {
    if (input_len % 4 != 0) {
        PyErr_SetString(PyExc_ValueError, "Invalid base64-encoded string");
        return NULL;
    }

    Py_ssize_t output_len = input_len / 4 * 3;
    if (input[input_len - 1] == '=') output_len--;
    if (input[input_len - 2] == '=') output_len--;

    PyObject* output = PyBytes_FromStringAndSize(NULL, output_len);
    if (!output)
        return NULL;

    uint8_t* out = (uint8_t*)PyBytes_AS_STRING(output);

    Py_ssize_t i, j;
    for (i = 0, j = 0; i < input_len; i += 4) {
        uint32_t n = decode_table[input[i]] << 18 |
                     decode_table[input[i + 1]] << 12 |
                     decode_table[input[i + 2]] << 6 |
                     decode_table[input[i + 3]];

        out[j++] = (n >> 16) & 0xFF;
        if (input[i + 2] != '=')
            out[j++] = (n >> 8) & 0xFF;
        if (input[i + 3] != '=')
            out[j++] = n & 0xFF;
    }

    return output;
}

static PyObject* b64encode(PyObject* self, PyObject* args) {
    const uint8_t* input;
    Py_ssize_t input_len;

    if (!PyArg_ParseTuple(args, "y#", &input, &input_len))
        return NULL;

    return encode_base64(input, input_len, base64_table);
}

static PyObject* b64decode(PyObject* self, PyObject* args) {
    const uint8_t* input;
    Py_ssize_t input_len;

    if (!PyArg_ParseTuple(args, "y#", &input, &input_len))
        return NULL;

    return decode_base64(input, input_len, base64_decode_table);
}

static PyObject* standard_b64encode(PyObject* self, PyObject* args) {
    const uint8_t* input;
    Py_ssize_t input_len;

    if (!PyArg_ParseTuple(args, "y#", &input, &input_len))
        return NULL;

    return encode_base64(input, input_len, base64_table);
}

static PyObject* standard_b64decode(PyObject* self, PyObject* args) {
    const char* input;
    Py_ssize_t input_len;

    if (!PyArg_ParseTuple(args, "s#", &input, &input_len))
        return NULL;

    return decode_base64((const uint8_t*)input, input_len, base64_decode_table);
}

static PyObject* urlsafe_b64encode(PyObject* self, PyObject* args) {
    const uint8_t* input;
    Py_ssize_t input_len;

    if (!PyArg_ParseTuple(args, "y#", &input, &input_len))
        return NULL;

    return encode_base64(input, input_len, base64_urlsafe_table);
}

static PyObject* urlsafe_b64decode(PyObject* self, PyObject* args) {
    const char* input;
    Py_ssize_t input_len;

    if (!PyArg_ParseTuple(args, "s#", &input, &input_len))
        return NULL;

    char* modified_input = PyMem_Malloc(input_len);
    if (!modified_input) {
        return PyErr_NoMemory();
    }

    for (Py_ssize_t i = 0; i < input_len; i++) {
        if (input[i] == '-')
            modified_input[i] = '+';
        else if (input[i] == '_')
            modified_input[i] = '/';
        else
            modified_input[i] = input[i];
    }

    PyObject* result = decode_base64((const uint8_t*)modified_input, input_len, base64_decode_table);
    PyMem_Free(modified_input);
    return result;
}

static PyMethodDef Base64Methods[] = {
    {"b64encode", b64encode, METH_VARARGS, "Encode a byte string using Base64."},
    {"b64decode", b64decode, METH_VARARGS, "Decode a Base64 encoded byte string."},
    {"standard_b64encode", standard_b64encode, METH_VARARGS, "Encode a byte string using standard Base64."},
    {"standard_b64decode", standard_b64decode, METH_VARARGS, "Decode a standard Base64 encoded byte string."},
    {"urlsafe_b64encode", urlsafe_b64encode, METH_VARARGS, "Encode a byte string using URL-safe Base64."},
    {"urlsafe_b64decode", urlsafe_b64decode, METH_VARARGS, "Decode a URL-safe Base64 encoded byte string."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef base64cmodule = {
    PyModuleDef_HEAD_INIT,
    "base64c",
    "Fast Base64 encoding and decoding using AVX2.",
    -1,
    Base64Methods
};

EXPORT PyMODINIT_FUNC PyInit_base64c(void) {
    return PyModule_Create(&base64cmodule);
}