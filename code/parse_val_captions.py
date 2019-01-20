import numpy as np
import nltk
import mmap
def main():
	Ngram = 1.
	f1 = open('captionTrain.5826821.bw.out', 'r')
	count = 0
	predicted_captions = []
	sentence_length = []
	probs = []
	for line in f1:
		# if len(line) > 2 and line[2]=='0':
		# 	sentence = find_between(line, ') ', ' (')
		# 	probs.append(np.float(find_between(line, '(p=', ')')))
		# 	predicted_captions.append(sentence)
		# 	sentence_length.append(sentence.count(' '))
		if len(line) > 2 and line[0:7] == 'Caption':
			file_name = find_between(line, 'image ', ':')
			fcap = open('Captions_50K.txt')
			caplines = fcap.readlines()
			s = mmap.mmap(fcap.fileno(), 0, access=mmap.ACCESS_READ)
			if s.find(file_name) != -1:
			    for i in range(len(caplines)):
			    	line1 = caplines[i]
			    	if len(line1) > 2 and line1[0:7] == 'Caption':
				        file_name1 = find_between(line, 'image ', ':')
				        if file_name == file_name1:
						    sentence = find_between(caplines[i+1], ') ', ' (')
						    probs.append(np.float(find_between(caplines[i+1], '(p=', ')')))
						    predicted_captions.append(sentence)
						    sentence_length.append(sentence.count(' '))
						    break
			    count+=1
	print count
	print len(probs)
	f1.close()
	print "%d files are captioned"%len(predicted_captions)
	print "Average caption length %d"%np.mean(sentence_length)
	print "Average probs = %f"%np.mean(probs)
	f2 = open('val_captions.txt', 'r')
	real_captions = []
	for line in f2:
		real_captions.append(line)
	scores = []
	error_count = 0
	for i in range(len(predicted_captions)):
		try:
			bs = nltk.translate.bleu_score.sentence_bleu(predicted_captions[i], real_captions[i], np.ones(int(Ngram))/Ngram)
			scores.append(bs)
			# print "predicted_captions %s"%predicted_captions[i]
			# print "real_captions %s"%real_captions[i]
		except Exception, e:
			error_count+=1
			# print e
	# print scores	
	print np.mean(np.asarray(scores))
	print "Error in %d files"%error_count
	print nltk.translate.bleu_score.corpus_bleu(predicted_captions, real_captions, np.ones(int(Ngram))/Ngram)

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError, e:
        return ""

main()