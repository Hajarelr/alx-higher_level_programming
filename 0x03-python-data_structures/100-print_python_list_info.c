#include <Python.h>
/**
 * print_python_list_info - Function that prints basic informations of 
 * Python lists.
 * @p: Input
 * return: Void
 */
void print_python_list_info(PyObject *p)
{
	int size, n, m;
	PyObject *o;

	size = Py_SIZE(p);
	n = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", n);

	for (m = 0; m < size; m++)
	{
		printf("Element %d: ", m);

		o = PyList_GetItem(p, m);
		printf("%s\n", Py_TYPE(o)->tp_name);
	}
}
