import numpy 
import pyopencl as cl

myNumbers = numpy.random.randn(128,128)
myNumbers = myNumbers.astype(numpy.float32)

ctx = cl.create_some_context()
queue = cl.CommandQueue(ctx)


mf = cl.mem_flags
gpuBuffer = cl.Buffer(ctx, mf.READ_WRITE | mf.COPY_HOST_PTR, hostbuf=myNumbers)

prg = cl.Program(ctx,"""
  __kernel void squareArray(__global float *data )
  {
    int col = get_global_id(0);
	int row = get_global_id(1);
	int threadId = col + get_global_size(0)*row ;

	data[threadId] = data[threadId]*data[threadId];
  }
  """).build()
 

prg.squareArray(queue, myNumbers.shape, (8,8), gpuBuffer)

myResults = numpy.empty([128,128], dtype=numpy.float32)

cl.enqueue_copy(queue, myResults, gpuBuffer)

print("Numbers")
print(myNumbers)

print("GPU Results")
print(myResults)

print("CPU Results")
print(myNumbers*myNumbers)