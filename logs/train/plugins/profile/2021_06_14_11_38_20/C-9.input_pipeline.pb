	}?5^??m@}?5^??m@!}?5^??m@	J??4?`&@J??4?`&@!J??4?`&@"e
=type.googleapis.com/tensorflow.profiler.PerGenericStepDetails$}?5^??m@?Fx$??A?!??upj@Y`??"۩:@*	????l?@2?
JIterator::Model::MaxIntraOpParallelism::Map::BatchV2::Shuffle::Zip[0]::Map??N@?6@!\??NYU@)????ƻ6@1??KUTU@:Preprocessing2k
4Iterator::Model::MaxIntraOpParallelism::Map::BatchV2?S㥛9@!"?+q?W@)?e?c]?@1?DA	?? @:Preprocessing2b
+Iterator::Model::MaxIntraOpParallelism::Map????:@!?6???X@)ё\?C???1L?JWo@:Preprocessing2y
BIterator::Model::MaxIntraOpParallelism::Map::BatchV2::Shuffle::Zip??ZӼ?6@!\?ߚ?jU@)??|гY??1\}?? ??:Preprocessing2?
RIterator::Model::MaxIntraOpParallelism::Map::BatchV2::Shuffle::Zip[1]::TensorSlice?q??????!??׾???)?q??????1??׾???:Preprocessing2t
=Iterator::Model::MaxIntraOpParallelism::Map::BatchV2::ShuffleEGr??6@!????oU@)??_?L??1????????:Preprocessing2?
WIterator::Model::MaxIntraOpParallelism::Map::BatchV2::Shuffle::Zip[0]::Map::TensorSliceQ?|a2??!o?'<???)Q?|a2??1o?'<???:Preprocessing2]
&Iterator::Model::MaxIntraOpParallelismio??ɤ:@!ϝ???X@)?J?4a?1<(?L$??:Preprocessing2F
Iterator::Model?_?L?:@!      Y@)????Mb`?1????~?:Preprocessing:?
]Enqueuing data: you may want to combine small input data chunks into fewer but larger chunks.
?Data preprocessing: you may increase num_parallel_calls in <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map" target="_blank">Dataset map()</a> or preprocess the data OFFLINE.
?Reading data from files in advance: you may tune parameters in the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch size</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave cycle_length</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer_size</a>)
?Reading data from files on demand: you should read data IN ADVANCE using the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer</a>)
?Other data reading or processing: you may consider using the <a href="https://www.tensorflow.org/programmers_guide/datasets" target="_blank">tf.data API</a> (if you are not using it now)?
:type.googleapis.com/tensorflow.profiler.BottleneckAnalysis?
both?Your program is MODERATELY input-bound because 11.2% of the total step time sampled is waiting for input. Therefore, you would need to reduce both the input time and other time.no*no9J??4?`&@IW#d??3V@Zno>Look at Section 3 for the breakdown of input time on the host.B?
@type.googleapis.com/tensorflow.profiler.GenericStepTimeBreakdown?
	?Fx$???Fx$??!?Fx$??      ??!       "      ??!       *      ??!       2	?!??upj@?!??upj@!?!??upj@:      ??!       B      ??!       J	`??"۩:@`??"۩:@!`??"۩:@R      ??!       Z	`??"۩:@`??"۩:@!`??"۩:@b      ??!       JCPU_ONLYYJ??4?`&@b qW#d??3V@