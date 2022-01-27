# Do 

  Simple function for interleaving two videos

# Use

  comparevideos(clip1: vs.VideoNode=None, clip2: vs.VideoNode=None, show: bool = True)

# Return value

  vs.VideoNode object
  
# Custom messages handler. 

They are not needed because the core of vapoursynth reports errors at runtime. I leave it as documentation

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

