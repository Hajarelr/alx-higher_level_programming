#include "Python.h"

/**
 * print_python_string - Function that prints information about Python strings
 * @p:String
 * Return: Void
 */
void print_python_string(PyObject *p)
{
long int n;
fflush(stdout);
printf("[.] string object info\n");
if (strcmp(p->ob_type->tp_name, "str") != 0)
{
printf("  [ERROR] Invalid String Object\n");
return;
}
n = ((PyASCIIObject *)(p))->n;
if (PyUnicode_IS_COMPACT_ASCII(p))
printf("  type: compact ascii\n");
else
printf("  type: compact unicode object\n");
printf("  length: %ld\n", n);
printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &n));
}
