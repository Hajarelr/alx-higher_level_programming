#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

void print_python_bytes(PyObject *p)
{
	long int a;
	int b;
	char *c = NULL;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	PyBytes_AsStringAndSize(p, &c, &a);

	printf("  size: %li\n", a);
	printf("  trying string: %s\n", c);
	if (a < 10)
		printf("  first %li bytes:", a + 1);
	else
		printf("  first 10 bytes:");
	for (i = 0; b <= a && b < 10; b++)
		printf(" %02hhx", c[b]);
	printf("\n");
}
void print_python_list(PyObject *p)
{
        long int a = PyList_Size(p);
        int b;
        PyListObject *c = (PyListObject *)p;
        const char *d;

        printf("[*] Python list info\n");
        printf("[*] Size of the Python List = %li\n", a);
        printf("[*] Allocated = %li\n", c->allocated);
        for (b = 0; b < a; b++)
        {
                d = (c->ob_item[b])->ob_type->tp_name;
		printf("Element %i: %s\n", b, d);
                if (!strcmp(d, "bytes"))
                        print_python_bytes(c->ob_item[b]);
        }
}
