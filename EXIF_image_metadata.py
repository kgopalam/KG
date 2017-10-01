#image file format Jpeg 
#uses EXifread 2.1.2 , python2.7

import exifread

photo_path = "test.jpg"
f = open(photo_path,'rb')
tags = exifread.process_file(f,details =False)
#tags = exifread.process_file(f,strict = True)
#tags = exifread.process_file(f,stop_tag = 'GPS')
for tag in tags.keys():
	if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
		print "Key: %s, value %s" % (tag, tags[tag])
		