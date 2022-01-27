import vapoursynth as vs
core = vs.core

def comparevideos(clip_1, clip_2, show: bool = True):
	
	# If is False return clip 2
	if show == False:
		return clip_2

	# Parameters are not None but check type vs.VideoNode
	if not isinstance(clip_1, vs.VideoNode):
		raise ValueError("The parameter 'clip_1' is not a clip")
	if not isinstance(clip_2, vs.VideoNode):
		raise ValueError("The parameter 'clip_2' is not a clip")

	# If both parameters are clips
	try:
		clip_1 = core.sub.Subtitle(clip_1, "Clip 1")
		clip_2 = core.sub.Subtitle(clip_2, "Clip 2")
		interleave = core.std.Interleave([clip_1,clip_2])
		return interleave
	except Exception as e:
		raise ValueError(e)
