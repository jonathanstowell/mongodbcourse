use zips;
db.zips.aggregate([
    {$project: 
     {
        first_char: {$substr : ["$city",0,1]},
        pop: "$pop"
     }   
    },
    {$match:
        {
            first_char : { $in : ["0","1","2","3","4","5","6","7","8","9"]}
        }
    },
    {$group:
        {
            _id : "$first_char",
            count : {$sum:"$pop"}
        }
    },
    {$project:
        {
            _id:0,
            pop : "$count"
        }
    }
])