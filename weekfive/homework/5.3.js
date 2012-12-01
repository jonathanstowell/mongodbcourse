
use 53;
db.student.aggregate([
	{$unwind: "$scores"},
    {'$group':
     { _id: {class_id:"$class_id", student_id:"$student_id"}, 
       'average': {"$avg":"$scores.score"}
   	 }
   	},
    {'$group':{_id:"$_id.class_id", 'average':{"$avg":"$average"}}},
    {$sort:{'average':-1}},
    {"$limit":5}
])