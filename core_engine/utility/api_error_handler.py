import linecache
import sys

def PrintException():
	    exc_type, exc_obj, tb = sys.exc_info()
	    f = tb.tb_frame
	    lineno = tb.tb_lineno
	    filename = f.f_code.co_filename
	    linecache.checkcache(filename)
	    line = linecache.getline(filename, lineno, f.f_globals)
	    return [filename, lineno, line.strip(), str(exc_obj)]