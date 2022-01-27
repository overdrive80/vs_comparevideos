# What does? 

  Simple function for interleaving two videos. The main use is to compare a loaded video and the same edited one to be able to contrast the "before and after".

# Use
  
  Clip1 and Clips2 must have same format (framerate, framecount, dimensions). 

  ```python
  comparevideos(clip1, clip2)
  ```
  
  For default, bool parameter is True. Header definition:
  
  comparevideos(clip1: vs.VideoNode, clip2: vs.VideoNode, show: bool = True)

# Return value

  vs.VideoNode (object)
  
  Return VideoNode.set_output()
  
  Therefore, there is no need to add a call to clip.set_output() after calling the function  
  
# Custom messages handler. 

They are not needed because the core of vapoursynth reports errors at runtime. I leave it as documentation
```python
# Custom control obligatory parameters. If we define optional parameters (clip_1, clip_2) 
if clip_1 == None:
	raise ValueError("The parameter 'clip_1' is mandatory.")
if clip_2 == None:
	raise ValueError("The parameter 'clip_2' is mandatory.")

# Parameters are not None but check type vs.VideoNode
if not isinstance(clip_1, vs.VideoNode):
	raise ValueError("The parameter 'clip_1' is not a clip")
if not isinstance(clip_2, vs.VideoNode):
	raise ValueError("The parameter 'clip_2' is not a clip")

# Check video dimensions
if not clip_1.height == clip_2.height or not clip_1.width == clip_2.width:
	raise ValueError("The clips dimension's must be the same.")

# Check framerate
if not clip_1.fps.numerator == clip_2.fps.numerator or not clip_1.fps.denominator == clip_2.fps.denominator:
	raise ValueError("The clips framerate's must be the same.")
```

