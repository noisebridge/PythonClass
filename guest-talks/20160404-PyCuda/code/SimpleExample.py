import pycuda.driver as cuda
import pycuda.autoinit
from pycuda.compiler import SourceModule

import numpy
myNumbers = numpy.random.randn(128,128)
myNumbers = myNumbers.astype(numpy.float32)

gpuBuffer = cuda.mem_alloc(myNumbers.nbytes)
cuda.memcpy_htod(gpuBuffer, myNumbers)

mod = SourceModule("""

  __global__ void squareArray(float *data)
  {
    int col = threadIdx.x + blockIdx.x * blockDim.x;
	int row = threadIdx.y + blockIdx.y * blockDim.y;
	int threadId = col + (blockDim.x*gridDim.x)*row ;

	data[threadId] = data[threadId]*data[threadId];
  }
  """)

  
squareFunc = mod.get_function("squareArray")
squareFunc(gpuBuffer, block=(16,16,1), grid=(8,8,1))

myResults = numpy.empty([128,128], dtype=numpy.float32)
cuda.memcpy_dtoh(myResults, gpuBuffer)

print("Numbers")
print(myNumbers)

print("GPU Results")
print(myResults)

print("CPU Results")
print(myNumbers*myNumbers)