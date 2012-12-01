use zips;
db.zips.aggregate([
    {$match:
     {
         state: { $in : ["CA", "NJ"] },
         pop: { $gt: 25000 }
     }
    },
    {$group:
     {
	 _id: "$city",
	 population: {$sum:"$pop"}
     }
    },
    {$group:
     {
	 _id: "$state",
	 population: {$avg:"$population"}
     }
    }
 ])