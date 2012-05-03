     //here you place the ids of every element you want.
     var ids=new Array('content','contact-info');

     function switchid(id)
     { 
      hideallids();
      showdiv(id);
     }

    function hideallids()
    {
    //loop through the array and hide each element by id
      for (var i=0;i<ids.length;i++)
      {
        hidediv(ids[i]);
      }       
    }

    function hidediv(id) 
    {
      //safe function to hide an element with a specified id
        Effect.Fade(id);
    }

    function showdiv(id) 
    {
      Effect.Appear(id);
      Effect.Appear(id, { duration: 3.0 });

    }
    
    function showAll()
    {
    //loop through the array and show each element by id
      for (var i=0;i<ids.length;i++)
      {
        showdiv(ids[i]);
      }       
    }



