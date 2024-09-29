#ifndef BASE64C_H
#define BASE64C_H

#include <Python.h>

// Function prototypes
static PyObject* b64encode(PyObject* self, PyObject* args);
static PyObject* b64decode(PyObject* self, PyObject* args);
static PyObject* standard_b64encode(PyObject* self, PyObject* args);
static PyObject* standard_b64decode(PyObject* self, PyObject* args);
static PyObject* urlsafe_b64encode(PyObject* self, PyObject* args);
static PyObject* urlsafe_b64decode(PyObject* self, PyObject* args);

// Helper function prototypes
static PyObject* encode_base64(const uint8_t* input, Py_ssize_t input_len, const uint8_t* table);
static PyObject* decode_base64(const uint8_t* input, Py_ssize_t input_len, const uint8_t* decode_table);

// Constants
extern const uint8_t base64_table[64];
extern const uint8_t base64_urlsafe_table[64];
extern const uint8_t base64_decode_table[256];

// Module definition
extern PyMethodDef Base64Methods[];
extern struct PyModuleDef base64cmodule;

// Module initialization function
PyMODINIT_FUNC PyInit_base64c(void);

#endif // BASE64C_H