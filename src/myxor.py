#!/usr/bin/env python3

import os,sys



def test(src,dst):
 
  with open(src,'rb') as srcfb:
    content = srcfb.read()
    ret = bytes(a ^ 0xff for a in content)
    with open(dst,'wb') as dstfb:
      dstfb.write(ret)






if __name__=='__main__':
  test(sys.argv[1],sys.argv[2])
