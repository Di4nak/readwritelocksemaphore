from threading import Lock
from contextlib import contextmanager

class ReadWriteLock(object)

  def _init_(self):
     self.write_lock = Lock()
     self.num_read_lock = Lock()
     self.num_read = 0

#read method
   def read_acquire(self)
      self.num_read_lock.acquire()
      self.num_read +=1
      if self.num_read ==1:
         self.write_lock.acquire()
      self.num_read_lock.release()
      print("Reader {self.num_r} is reading")
   def read_release(self):
      assert self.num_read > 0
      self.num_read -= 1
      if self.num_read == 0
         self.write_lock.release()
      self.num_read_lock.release()

    @contextmanager
    def read_locked(self)
      try:
        self.read_acquire()
        yield
      finally:
        self.read.release()
#write method

     def write_acquire(self)
         self.write_lock.acquire()
         print("writing")
     def write_release(self)
         self.write_lock.release()

     @contextmanager
     def write_locked(self)
           try:
             self.write_acquire()
             yield
           finally:
              self.write_release()