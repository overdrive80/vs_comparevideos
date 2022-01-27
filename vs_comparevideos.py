import vapoursynth as vs
core = vs.core

def compareVideos(clip_1, clip_2, show: bool = True):
	
	# Vaporsynth already checks if the input video format does not match
	if show == False:
		return clip_1
	
	try:
		clip_1 = core.sub.Subtitle(clip_1, "Clip 1")
		clip_2 = core.sub.Subtitle(clip_2, "Clip 2")
		interleave = core.std.Interleave([clip_1,clip_2])
		return interleave.set_output()
	except Exception as e:
		raise ValueError(e)
