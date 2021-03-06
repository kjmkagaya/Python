


"""



Python 3 - File Methods
Advertisements
 Previous Page Next Page  
A file object is created using open function and here is a list of functions which can be called on this object −

S.No.	Methods & Description
1	file.close()
Close the file. A closed file cannot be read or written any more.

2	file.flush()
Flush the internal buffer, like stdio's fflush. This may be a no-op on some file-like objects.

3	file.fileno()
Returns the integer file descriptor that is used by the underlying implementation to request I/O operations from the operating system.

4	file.isatty()
Returns True if the file is connected to a tty(-like) device, else False.

5	next(file)
Returns the next line from the file each time it is being called.

6	file.read([size])
Reads at most size bytes from the file (less if the read hits EOF before obtaining size bytes).

7	file.readline([size])
Reads one entire line from the file. A trailing newline character is kept in the string.

8	file.readlines([sizehint])
Reads until EOF using readline() and return a list containing the lines. If the optional sizehint argument is present, instead of reading up to EOF, whole lines totalling approximately sizehint bytes (possibly after rounding up to an internal buffer size) are read.

9	file.seek(offset[, whence])
Sets the file's current position

10	file.tell()
Returns the file's current position

11	file.truncate([size])
Truncates the file's size. If the optional size argument is present, the file is truncated to (at most) that size.

12	file.write(str)
Writes a string to the file. There is no return value.

13	file.writelines(sequence)
Writes a sequence of strings to the file. The sequence can be any iterable object producing strings, typically a list of strings.

"""
